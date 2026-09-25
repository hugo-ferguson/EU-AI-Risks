"""
Server-rendered web UI for the EU AI Risks assessment pipeline.
"""

from __future__ import annotations

import asyncio
import json
import logging
import re
import tempfile
import uuid
from pathlib import Path
from typing import Any

from dotenv import load_dotenv
from fastapi import FastAPI, File, Form, HTTPException, Request, UploadFile
from fastapi.responses import FileResponse, HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from eu_ai_risks.analysis.risk_report import (
    collect_citations,
    entries_from_assessments,
    render_markdown_report,
)
from eu_ai_risks.db.graph import list_categories
from eu_ai_risks.requirements.loader import (
    SUPPORTED_EXTENSIONS,
    load_requirements,
    parse_requirements,
)
from eu_ai_risks.requirements.models import Requirement

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent
WEB_DIR = BASE_DIR / "web"
TEMPLATE_DIR = WEB_DIR / "templates"
STATIC_DIR = WEB_DIR / "static"
OUTPUT_DIR = Path(tempfile.gettempdir()) / "eu_ai_risks_web_reports"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

UPLOAD_PREFIX = "eu_ai_risks_upload_"
RE_HEX_TOKEN = re.compile(r"^[0-9a-f]{32}$")
RE_UPLOAD_TOKEN = re.compile(r"^eu_ai_risks_upload_[a-zA-Z0-9_-]+$")
RE_REPORT_FILENAME = re.compile(r"^risk-assessment-[0-9a-f]{32}\.md$")
MAX_UPLOAD_SIZE = 25 * 1024 * 1024  # 25 MB

app = FastAPI(title="EU AI Risk Mapper")
app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")
templates = Jinja2Templates(directory=str(TEMPLATE_DIR))


def _entry_counts(entries: list[dict[str, Any]]) -> dict[str, int]:
    counts = {"high": 0, "medium": 0, "low": 0}
    for entry in entries:
        level = str(entry.get("risk_level", "medium")).lower()
        if level in counts:
            counts[level] += 1
    return counts


def _categories_from_entries(entries: list[dict[str, Any]]) -> list[str]:
    categories: set[str] = set()
    for entry in entries:
        for risk in entry.get("risks", []) or []:
            category = risk.get("obligation_category")
            if category:
                categories.add(category)
    return sorted(categories)


def _normalise_entries(entries: list[dict[str, Any]]) -> list[dict[str, Any]]:
    for entry in entries:
        entry["risk_level"] = str(entry.get("risk_level", "medium")).lower()
        for risk in entry.get("risks", []) or []:
            risk["obligation_category_label"] = _pretty_category(
                risk.get("obligation_category", "")
            )
    return entries


def _pretty_category(category: str) -> str:
    return category.replace("_", " ").replace("-", " ").strip() or "mapped obligation"


def _render(
    request: Request,
    *,
    phase: str = "empty",
    requirements: list[dict[str, str]] | None = None,
    entries: list[dict[str, Any]] | None = None,
    status: str = "Upload a requirements document to begin",
    error: str | None = None,
    report_path: Path | None = None,
    uploaded_filename: str | None = None,
    upload_token: str | None = None,
) -> HTMLResponse:
    if entries:
        entries = _normalise_entries(entries)
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "phase": phase,
            "requirements": requirements or [],
            "entries": entries or [],
            "counts": _entry_counts(entries or []),
            "categories": _categories_from_entries(entries or []),
            "status": status,
            "error": error,
            "report_token": report_path.name if report_path else None,
            "uploaded_filename": uploaded_filename,
            "upload_token": upload_token,
        },
    )


def _save_state(prefix: str, data: dict) -> str:
    """Write JSON state to OUTPUT_DIR and return a hex token."""
    token = uuid.uuid4().hex
    path = OUTPUT_DIR / f"{prefix}-{token}.json"
    path.write_text(json.dumps(data), encoding="utf-8")
    return token


def _load_state(prefix: str, token: str) -> dict | None:
    if not RE_HEX_TOKEN.match(token):
        return None
    path = (OUTPUT_DIR / f"{prefix}-{token}.json").resolve()
    try:
        path.relative_to(OUTPUT_DIR.resolve())
    except ValueError:
        return None
    if not path.is_file() or path.is_symlink():
        return None
    return json.loads(path.read_text(encoding="utf-8"))


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/", response_class=HTMLResponse)
def home(request: Request) -> HTMLResponse:
    # POST handlers redirect here with a token so refreshing doesn't re-submit
    upload_token = request.query_params.get("upload")
    report_token = request.query_params.get("report")
    error_message = request.query_params.get("error")

    if report_token:
        state = _load_state("results", report_token)
        if state:
            entries = state["entries"]
            report_name = state.get("report_token", "")
            report_path = (OUTPUT_DIR / report_name) if report_name else None
            return _render(
                request,
                phase="assessed",
                entries=entries,
                status=f"Assessment complete — {len(entries)} requirements reviewed",
                report_path=report_path,
                uploaded_filename=state.get("filename"),
            )

    if upload_token:
        state = _load_state("upload", upload_token)
        if state:
            return _render(
                request,
                phase="uploaded",
                requirements=state["requirements"],
                status=f"{len(state['requirements'])} requirements parsed from {state['filename']}",
                uploaded_filename=state["filename"],
                upload_token=state["upload_token"],
            )

    if error_message:
        return _render(request, phase="error", status="Error", error=error_message)

    return _render(request)


@app.get("/download/{report_token}")
def download_report(report_token: str) -> FileResponse:
    """Download a markdown report with strict containment check."""
    if not RE_REPORT_FILENAME.match(report_token):
        raise HTTPException(status_code=404, detail="Report not found or invalid.")
    path = (OUTPUT_DIR / report_token).resolve()
    try:
        path.relative_to(OUTPUT_DIR.resolve())
    except ValueError:
        raise HTTPException(status_code=404, detail="Report not found.")
    if not path.is_file() or path.is_symlink():
        raise HTTPException(status_code=404, detail="Report not found or expired.")
    return FileResponse(path, filename="eu-ai-risk-assessment.md", media_type="text/markdown")


def _save_upload(requirements_file: UploadFile, file_bytes: bytes) -> tuple[Path, str, str]:
    """Save uploaded file to a temp dir and return (path, token, filename)."""
    filename = Path(requirements_file.filename or "requirements.txt").name
    suffix = Path(filename).suffix.lower()
    upload_dir = Path(tempfile.mkdtemp(prefix=UPLOAD_PREFIX))
    upload_path = upload_dir / f"uploaded{suffix}"
    upload_path.write_bytes(file_bytes)
    return upload_path, upload_dir.name, filename


def _resolve_upload_token(token: str) -> Path | None:
    """Reconstruct upload path from token, with strict validation and canonical containment."""
    if not token or not RE_UPLOAD_TOKEN.match(token):
        return None
    temp_dir = Path(tempfile.gettempdir()).resolve()
    upload_dir = (temp_dir / token).resolve()
    try:
        upload_dir.relative_to(temp_dir)
    except ValueError:
        return None
    if not upload_dir.is_dir() or upload_dir.is_symlink():
        return None
    for child in upload_dir.iterdir():
        if child.is_file() and not child.is_symlink():
            return child
    return None


@app.post("/upload")
async def upload(
    requirements_file: UploadFile = File(...),
) -> RedirectResponse:
    """Parse requirements asynchronously and redirect to GET with results."""
    filename = Path(requirements_file.filename or "requirements.txt").name
    suffix = Path(filename).suffix.lower()
    if suffix not in SUPPORTED_EXTENSIONS:
        return RedirectResponse(
            url=f"/?error=Unsupported+file+type+'{suffix}'.+Upload+JSON,+TXT,+MD,+PDF,+or+DOCX.",
            status_code=303,
        )

    file_bytes = await requirements_file.read()
    if len(file_bytes) > MAX_UPLOAD_SIZE:
        return RedirectResponse(
            url="/?error=File+exceeds+maximum+upload+limit+of+25MB.",
            status_code=303,
        )

    upload_path, dir_token, filename = _save_upload(requirements_file, file_bytes)

    loop = asyncio.get_event_loop()
    try:
        # Offload file parsing from the async event loop
        requirements = await loop.run_in_executor(None, parse_requirements, upload_path)
        if not requirements:
            raise ValueError("No requirements found.")
    except Exception as exc:
        return RedirectResponse(url=f"/?error={exc}", status_code=303)

    state_token = _save_state("upload", {
        "requirements": [{"id": r.id, "text": r.text} for r in requirements],
        "upload_token": dir_token,
        "filename": filename,
    })
    return RedirectResponse(url=f"/?upload={state_token}", status_code=303)


@app.post("/assess")
async def assess(
    upload_token: str = Form(...),
    mode: str = Form("non-agent"),
    uploaded_filename: str = Form(""),
) -> RedirectResponse:
    """Run full assessment pipeline in executor and redirect to GET with results."""
    upload_path = _resolve_upload_token(upload_token)
    if not upload_path:
        return RedirectResponse(
            url="/?error=Upload+expired+or+invalid.+Please+upload+again.",
            status_code=303,
        )

    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(
        None, _assess_sync, upload_path, mode, uploaded_filename or None,
    )


def _assess_sync(
    upload_path: Path,
    mode: str,
    uploaded_filename: str | None,
) -> RedirectResponse:
    try:
        # Web pipeline evaluates requirements in-memory; disable unused LLM triple extraction
        requirements = load_requirements(upload_path, with_triples=False)
        if not requirements:
            raise ValueError("No requirements found.")

        entries, report_path = _run_assessment(
            requirements, use_agent=(mode == "agent")
        )
        state_token = _save_state("results", {
            "entries": entries,
            "report_token": report_path.name,
            "filename": uploaded_filename,
        })
        return RedirectResponse(url=f"/?report={state_token}", status_code=303)
    except Exception as exc:
        return RedirectResponse(url=f"/?error={exc}", status_code=303)


def _run_assessment(
    requirements: list[Requirement],
    use_agent: bool = False,
) -> tuple[list[dict[str, Any]], Path]:
    logger = logging.getLogger("eu_ai_risks.web")

    if use_agent:
        from eu_ai_risks.analysis.risk_assessor_agent import assess_requirement
    else:
        from eu_ai_risks.analysis.risk_assessor import assess_requirement

    categories = list_categories()
    article_cache: dict[str, dict] = {}
    assessment_entries: list[dict[str, Any]] = []
    total = len(requirements)

    for index, requirement in enumerate(requirements, start=1):
        logger.info("[%d/%d] Assessing %s ...", index, total, requirement.id)
        assessment, fetched_articles, _raw = assess_requirement(
            requirement.id,
            requirement.text,
            categories=categories,
        )
        logger.info("[%d/%d] %s → %s", index, total,
                    requirement.id, assessment.risk_level)
        article_cache.update(fetched_articles)
        citations = collect_citations(assessment.risks, article_cache)
        assessment_entries.append(
            {
                "requirement": {"id": requirement.id, "text": requirement.text},
                "assessment": assessment,
                "citations": citations,
            }
        )

    entries = _normalise_entries(entries_from_assessments(assessment_entries))
    markdown = render_markdown_report(entries)
    report_path = OUTPUT_DIR / f"risk-assessment-{uuid.uuid4().hex}.md"
    report_path.write_text(markdown, encoding="utf-8")
    return entries, report_path

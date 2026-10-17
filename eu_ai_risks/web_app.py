"""
Server-rendered web UI for the EU AI Risks assessment pipeline.
"""

from __future__ import annotations

import json
import os
import re
import tempfile
import uuid
from datetime import datetime
from functools import partial
from pathlib import Path
from typing import Any

from dotenv import load_dotenv
from fastapi import FastAPI, File, Form, Request, UploadFile
from fastapi.responses import FileResponse, HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from eu_ai_risks.analysis.risk_report import (
    build_overall_analysis,
    collect_citations,
    entries_from_assessments,
    pretty_category,
    render_markdown_report,
)
from eu_ai_risks.db import get_session
from eu_ai_risks.requirements.loader import (
    SUPPORTED_EXTENSIONS,
    parse_requirements,
    reset_requirements,
    write_triples,
)
from eu_ai_risks.requirements.models import Requirement

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent
WEB_DIR = BASE_DIR / "web"
TEMPLATE_DIR = WEB_DIR / "templates"
STATIC_DIR = WEB_DIR / "static"
# Saved results are listed as previous assessments; set EU_AI_RISKS_OUTPUT_DIR
# to keep them across reboots instead of in the system temp folder
OUTPUT_DIR = Path(
    os.environ.get("EU_AI_RISKS_OUTPUT_DIR")
    or Path(tempfile.gettempdir()) / "eu_ai_risks_web_reports"
)
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
MAX_PREVIOUS_ASSESSMENTS = 10

UPLOAD_PREFIX = "eu_ai_risks_upload_"
RE_HEX_TOKEN = re.compile(r"^[0-9a-f]{32}$")

app = FastAPI(title="EU AI Risk Mapper")
app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")
templates = Jinja2Templates(directory=str(TEMPLATE_DIR))
# Appended to static asset URLs so browsers fetch them again after they change
templates.env.globals["asset_version"] = str(int(max(
    path.stat().st_mtime for path in STATIC_DIR.iterdir() if path.is_file()
)))


def _entry_counts(entries: list[dict[str, Any]]) -> dict[str, int]:
    counts = {"high": 0, "medium": 0, "low": 0}
    for entry in entries:
        level = str(entry.get("risk_level", "medium")).lower()
        if level in counts:
            counts[level] += 1
    return counts


def _normalise_entries(entries: list[dict[str, Any]]) -> list[dict[str, Any]]:
    for entry in entries:
        entry["risk_level"] = str(entry.get("risk_level", "medium")).lower()
        for risk in entry.get("risks", []) or []:
            risk["obligation_category_label"] = pretty_category(
                risk.get("obligation_category", ""))
    return entries


def _previous_assessments() -> list[dict[str, Any]]:
    """Summarise saved results, newest first, so earlier runs can be reopened."""
    paths = sorted(
        OUTPUT_DIR.glob("results-*.json"),
        key=lambda path: path.stat().st_mtime,
        reverse=True,
    )
    previous = []
    for path in paths[:MAX_PREVIOUS_ASSESSMENTS]:
        try:
            state = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            continue
        entries = state.get("entries", [])
        previous.append({
            "token": path.stem.removeprefix("results-"),
            "filename": state.get("filename") or "Unnamed document",
            "saved_at": datetime.fromtimestamp(path.stat().st_mtime).strftime("%d %b %Y %H:%M"),
            "total": len(entries),
            "counts": _entry_counts(entries),
        })
    return previous


def _render(
    request: Request,
    *,
    phase: str = "empty",
    requirements: list[dict[str, str]] | None = None,
    entries: list[dict[str, Any]] | None = None,
    error: str | None = None,
    report_path: Path | None = None,
    uploaded_filename: str | None = None,
    upload_token: str | None = None,
    results_token: str | None = None,
    upload_state: str | None = None,
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
            "error": error,
            "report_token": report_path.name if report_path else None,
            "uploaded_filename": uploaded_filename,
            "upload_token": upload_token,
            "previous": _previous_assessments(),
            "results_token": results_token,
            "upload_state": upload_state,
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
    path = OUTPUT_DIR / f"{prefix}-{token}.json"
    if not path.exists():
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
            report_path = OUTPUT_DIR / report_name if report_name else None
            return _render(
                request,
                phase="assessed",
                entries=entries,
                report_path=report_path,
                uploaded_filename=state.get("filename"),
                results_token=report_token,
                upload_state=state.get("upload_state"),
            )

    if upload_token:
        state = _load_state("upload", upload_token)
        if state:
            # Coming back from a results page keeps its Review step reachable
            results_token = request.query_params.get("results")
            if results_token and not _load_state("results", results_token):
                results_token = None
            return _render(
                request,
                phase="uploaded",
                requirements=state["requirements"],
                uploaded_filename=state["filename"],
                upload_token=state["upload_token"],
                upload_state=upload_token,
                results_token=results_token,
            )

    if error_message:
        return _render(request, error=error_message)

    return _render(request)


@app.get("/download/{report_token}")
def download_report(report_token: str) -> FileResponse:
    safe_name = Path(report_token).name
    path = OUTPUT_DIR / safe_name
    if not path.exists():
        raise FileNotFoundError("Report not found or expired.")
    return FileResponse(path, filename="eu-ai-risk-assessment.md", media_type="text/markdown")


def _save_upload(requirements_file: UploadFile, file_bytes: bytes) -> tuple[Path, str, str]:
    """Save uploaded file to a temp dir and return (path, token, filename)."""
    filename = requirements_file.filename or "requirements.txt"
    suffix = Path(filename).suffix.lower()
    upload_dir = Path(tempfile.mkdtemp(prefix=UPLOAD_PREFIX))
    upload_path = upload_dir / f"uploaded{suffix}"
    upload_path.write_bytes(file_bytes)
    return upload_path, upload_dir.name, filename


def _resolve_upload_token(token: str) -> Path | None:
    """Reconstruct upload path from token, with basic validation."""
    if not token.startswith(UPLOAD_PREFIX):
        return None
    upload_dir = Path(tempfile.gettempdir()) / token
    if not upload_dir.is_dir():
        return None
    return next(upload_dir.iterdir(), None)


@app.post("/upload")
async def upload(
    requirements_file: UploadFile = File(...),
) -> RedirectResponse:
    """Parse requirements and redirect to GET with results."""
    filename = requirements_file.filename or "requirements.txt"
    suffix = Path(filename).suffix.lower()
    if suffix not in SUPPORTED_EXTENSIONS:
        return RedirectResponse(
            url=f"/?error=Unsupported+file+type+'{suffix}'.+Upload+JSON,+TXT,+MD,+PDF,+or+DOCX.",
            status_code=303,
        )

    upload_path, dir_token, filename = _save_upload(
        requirements_file, await requirements_file.read(),
    )

    try:
        requirements = parse_requirements(upload_path)
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
    upload_state: str = Form(""),
) -> RedirectResponse:
    """Run full assessment pipeline and redirect to GET with results."""
    upload_path = _resolve_upload_token(upload_token)
    if not upload_path:
        return RedirectResponse(
            url="/?error=Upload+expired+or+invalid.+Please+upload+again.",
            status_code=303,
        )

    import asyncio
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(
        None, _assess_sync, upload_path, mode, uploaded_filename or None,
        upload_state or None,
    )


def _assess_sync(
    upload_path: Path,
    mode: str,
    uploaded_filename: str | None,
    upload_state: str | None = None,
) -> RedirectResponse:
    try:
        # Rebuild the requirements graph from this upload so related-requirement
        # lookups come from this document, not a previously loaded one
        with get_session() as session:
            reset_requirements(session)
        requirements = write_triples(upload_path)
        if not requirements:
            raise ValueError("No requirements found.")

        entries, overall_analysis, report_path = _run_assessment(
            requirements, use_agent=(mode == "agent"))
        state_token = _save_state("results", {
            "entries": entries,
            "overall_analysis": overall_analysis,
            "report_token": report_path.name,
            "filename": uploaded_filename,
            # Lets the results page link back to the Assess step for this upload
            "upload_state": upload_state,
        })
        return RedirectResponse(url=f"/?report={state_token}", status_code=303)
    except Exception as exc:
        return RedirectResponse(url=f"/?error={exc}", status_code=303)


def _run_assessment(
    requirements: list[Requirement],
    use_agent: bool = False,
) -> tuple[list[dict[str, Any]], dict[str, Any], Path]:
    import logging
    logger = logging.getLogger("eu_ai_risks.web")

    if use_agent:
        from eu_ai_risks.analysis.risk_assessor_agent import assess_requirement
    else:
        from eu_ai_risks.analysis.risk_assessor import assess_requirement, classify_system
        system = classify_system([(requirement.id, requirement.text) for requirement in requirements])
        logger.info("System classified under: %s",
                    ", ".join(system.annex_iii_points) or "no Annex III point")
        assess_requirement = partial(assess_requirement, system=system)

    article_cache: dict[str, dict] = {}
    assessment_entries: list[dict[str, Any]] = []
    total = len(requirements)

    for index, requirement in enumerate(requirements, start=1):
        logger.info("[%d/%d] Assessing %s ...", index, total, requirement.id)
        assessment, _raw = assess_requirement(requirement.id, requirement.text)
        logger.info("[%d/%d] %s → %s", index, total,
                    requirement.id, assessment.risk_level)
        citations = collect_citations(assessment.risks, article_cache)
        assessment_entries.append(
            {
                "requirement": {"id": requirement.id, "text": requirement.text},
                "assessment": assessment,
                "citations": citations,
            }
        )

    entries = _normalise_entries(entries_from_assessments(assessment_entries))
    overall_analysis = build_overall_analysis(entries)
    markdown = render_markdown_report(entries, overall_analysis=overall_analysis)
    report_path = OUTPUT_DIR / f"risk-assessment-{uuid.uuid4().hex}.md"
    report_path.write_text(markdown, encoding="utf-8")
    return entries, overall_analysis, report_path

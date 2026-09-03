"""Lightweight server-rendered web UI for the EU AI Risks POC.

Run with:
    uvicorn eu_ai_risks.web_app:app --reload --host 0.0.0.0 --port 8000

The UI deliberately stays Python-only: FastAPI serves the page, Jinja renders
HTML, and a small amount of JavaScript handles filtering/selecting findings.
"""

from __future__ import annotations

import json
import os
import re
import tempfile
import uuid
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import pdfplumber
from docx import Document
from dotenv import load_dotenv
from fastapi import FastAPI, File, Form, Request, UploadFile
from fastapi.responses import FileResponse, HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from eu_ai_risks.analysis.risk_report import (
    collect_citations,
    entries_from_assessments,
    render_markdown_report,
)
from eu_ai_risks.db.graph import list_categories

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent
WEB_DIR = BASE_DIR / "web"
TEMPLATE_DIR = WEB_DIR / "templates"
STATIC_DIR = WEB_DIR / "static"
OUTPUT_DIR = Path(tempfile.gettempdir()) / "eu_ai_risks_web_reports"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

SUPPORTED_EXTENSIONS = {".json", ".txt", ".md", ".markdown", ".pdf", ".docx"}

RE_REQUIREMENT_ID = re.compile(
    r"\b((?:FR|NFR|REQ|R|UC|SR|SYS|SRS|CH3-FR|CH3-NFR)[-_ ]?\d+(?:\.\d+)*)\b",
    re.IGNORECASE,
)
RE_NUMBERED_ITEM = re.compile(r"^(\d+(?:\.\d+)*|[A-Z]+\d+)[.)]\s+(.+)$")
RE_REQUIREMENT_VERB = re.compile(
    r"\b(shall|should|must|needs to|is required to|may not|must not)\b",
    re.IGNORECASE,
)

app = FastAPI(title="EU AI Risk Mapper")
app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")
templates = Jinja2Templates(directory=str(TEMPLATE_DIR))


@dataclass
class ParsedRequirement:
    id: str
    text: str
    source: str = "uploaded document"


def _normalise_text(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def _looks_like_requirement(text: str) -> bool:
    if RE_REQUIREMENT_ID.search(text) and len(text.split()) >= 4:
        return True
    if RE_REQUIREMENT_VERB.search(text) and len(text.split()) >= 5:
        return True
    numbered_match = RE_NUMBERED_ITEM.match(text)
    return bool(numbered_match and RE_REQUIREMENT_VERB.search(numbered_match.group(2)))


def _extract_requirement_id(text: str, fallback_index: int) -> str:
    match = RE_REQUIREMENT_ID.search(text)
    if match:
        return re.sub(r"\s+", "-", match.group(1).upper())
    numbered_match = RE_NUMBERED_ITEM.match(text)
    if numbered_match:
        return f"REQ-{numbered_match.group(1).replace('.', '-')}"
    return f"REQ-{fallback_index:03d}"


def _strip_requirement_prefix(text: str) -> str:
    text = RE_REQUIREMENT_ID.sub("", text, count=1).strip(" :-\t")
    numbered_match = RE_NUMBERED_ITEM.match(text)
    if numbered_match:
        return numbered_match.group(2).strip()
    return text


def _dedupe_requirements(requirements: list[ParsedRequirement]) -> list[ParsedRequirement]:
    seen: set[str] = set()
    unique: list[ParsedRequirement] = []
    for requirement in requirements:
        key = requirement.text.lower()
        if key in seen:
            continue
        seen.add(key)
        unique.append(requirement)
    return unique


def _requirements_from_json(path: Path) -> list[ParsedRequirement]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if isinstance(data, dict):
        for key in ("requirements", "items", "data"):
            if isinstance(data.get(key), list):
                data = data[key]
                break
    if not isinstance(data, list):
        raise ValueError("JSON requirements file must contain a list of requirement objects.")

    requirements: list[ParsedRequirement] = []
    for index, item in enumerate(data, start=1):
        if isinstance(item, str):
            text = _normalise_text(item)
            req_id = f"REQ-{index:03d}"
        elif isinstance(item, dict):
            text = _normalise_text(
                str(item.get("text") or item.get("requirement") or item.get("description") or "")
            )
            req_id = str(item.get("id") or item.get("requirement_id") or f"REQ-{index:03d}")
        else:
            continue
        if text:
            requirements.append(ParsedRequirement(req_id, text, source=str(path)))
    return _dedupe_requirements(requirements)


def _read_document_lines(path: Path) -> list[str]:
    suffix = path.suffix.lower()
    if suffix == ".pdf":
        lines: list[str] = []
        with pdfplumber.open(path) as pdf:
            for page in pdf.pages:
                lines.extend((page.extract_text() or "").splitlines())
        return lines
    if suffix == ".docx":
        document = Document(str(path))
        return [paragraph.text for paragraph in document.paragraphs]
    return path.read_text(encoding="utf-8", errors="ignore").splitlines()


def _requirements_from_document(path: Path) -> list[ParsedRequirement]:
    requirements: list[ParsedRequirement] = []
    next_id = 1
    for raw_line in _read_document_lines(path):
        text = _normalise_text(raw_line)
        if not text or not _looks_like_requirement(text):
            continue
        req_id = _extract_requirement_id(text, next_id)
        req_text = _strip_requirement_prefix(text)
        requirements.append(ParsedRequirement(req_id, req_text, source=str(path)))
        next_id += 1
    return _dedupe_requirements(requirements)


def _extract_requirements(path: Path) -> list[ParsedRequirement]:
    suffix = path.suffix.lower()
    if suffix not in SUPPORTED_EXTENSIONS:
        raise ValueError(
            f"Unsupported file type '{suffix}'. Supported: {', '.join(sorted(SUPPORTED_EXTENSIONS))}."
        )
    if suffix == ".json":
        return _requirements_from_json(path)
    return _requirements_from_document(path)


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
            risk["obligation_category_label"] = _pretty_category(risk.get("obligation_category", ""))
    return entries


def _pretty_category(category: str) -> str:
    return category.replace("_", " ").replace("-", " ").strip() or "mapped obligation"


def _demo_entries() -> list[dict[str, Any]]:
    """Default demo preview shown before a user uploads a requirements file.

    This mirrors the Chapter 3 non-agent demo output so the landing page shows
    the same scenario used for project demonstrations: two medium review gaps
    and two low-control/clarification findings.
    """
    return _normalise_entries([
        {
            "id": "CH3-DEMO-1",
            "text": "The system shall ingest candidate resumes, cover letters, and application form responses for automated recruitment screening.",
            "risk_level": "medium",
            "analysis": "Semantic profile indicates a remaining data_governance, technical_documentation gap. Conservative risk retained for manual review.",
            "risks": [
                {
                    "description": "Data governance expectations not fully specified [medium]",
                    "provision": "Article 10(2)",
                    "obligation_category": "data_governance",
                    "engineering_action": "Define data source, quality, bias, and validation checks.",
                },
                {
                    "description": "Technical documentation expectations not fully specified [medium]",
                    "provision": "Article 11(1)",
                    "obligation_category": "technical_documentation",
                    "engineering_action": "Document design decisions, evidence, and compliance rationale.",
                },
            ],
            "citations": [
                {
                    "label": "Data and data governance, Article 10(2)",
                    "text": "Training, validation and testing data sets shall be subject to data governance and management practices appropriate for the intended purpose of the high-risk AI system.",
                },
                {
                    "label": "Technical documentation, Article 11(1)",
                    "text": "The technical documentation of a high-risk AI system shall be drawn up before that system is placed on the market or put into service and shall be kept up to date.",
                },
            ],
            "recommendations": [
                "Define data source, quality, bias, and validation checks.",
                "Document design decisions, evidence, and compliance rationale.",
            ],
        },
        {
            "id": "CH3-DEMO-2",
            "text": "The system shall generate and display a candidate suitability score with an explanation of the main factors that influenced the score.",
            "risk_level": "medium",
            "analysis": "Semantic profile indicates a remaining data_governance, transparency gap. Conservative risk retained for manual review.",
            "risks": [
                {
                    "description": "Data governance expectations not fully specified [medium]",
                    "provision": "Article 10(2)",
                    "obligation_category": "data_governance",
                    "engineering_action": "Define data source, quality, bias, and validation checks.",
                },
                {
                    "description": "Transparency expectations not fully specified [medium]",
                    "provision": "Article 13(1)",
                    "obligation_category": "transparency",
                    "engineering_action": "Define explanation detail, user information, and instructions for use.",
                },
            ],
            "citations": [
                {
                    "label": "Data and data governance, Article 10(2)",
                    "text": "Training, validation and testing data sets shall be subject to data governance and management practices appropriate for the intended purpose of the high-risk AI system.",
                },
                {
                    "label": "Transparency and provision of information to deployers, Article 13(1)",
                    "text": "High-risk AI systems shall be designed and developed so their operation is sufficiently transparent to enable deployers to interpret the output and use it appropriately.",
                },
            ],
            "recommendations": [
                "Define data source, quality, bias, and validation checks.",
                "Define explanation detail, user information, and instructions for use.",
            ],
        },
        {
            "id": "CH3-DEMO-3",
            "text": "The system shall allow a human recruiter to review, override, or reject an automated ranking before a candidate is removed from consideration.",
            "risk_level": "low",
            "analysis": "Semantic profile indicates a remaining human_oversight, transparency gap. Conservative risk retained for manual review.",
            "risks": [
                {
                    "description": "Human oversight expectations not fully specified [low]",
                    "provision": "Article 14(1)",
                    "obligation_category": "human_oversight",
                    "engineering_action": "Define reviewer authority, training, escalation, and monitoring.",
                },
                {
                    "description": "Transparency expectations not fully specified [low]",
                    "provision": "Article 13(1)",
                    "obligation_category": "transparency",
                    "engineering_action": "Define explanation detail, user information, and instructions for use.",
                },
            ],
            "citations": [
                {
                    "label": "Human oversight, Article 14(1)",
                    "text": "High-risk AI systems shall be designed and developed with appropriate human-machine interface tools so they can be effectively overseen by natural persons.",
                },
                {
                    "label": "Transparency and provision of information to deployers, Article 13(1)",
                    "text": "High-risk AI systems shall be designed and developed so their operation is sufficiently transparent to enable deployers to interpret the output and use it appropriately.",
                },
            ],
            "recommendations": [
                "Define reviewer authority, training, escalation, and monitoring.",
                "Define explanation detail, user information, and instructions for use.",
            ],
        },
        {
            "id": "CH3-DEMO-4",
            "text": "The system must log each automated score, ranking, explanation, recruiter override, final decision, and model version for audit review.",
            "risk_level": "low",
            "analysis": "The requirement describes a control/safeguard. A low remaining clarification risk is retained for manual review.",
            "risks": [
                {
                    "description": "Record-keeping expectations not fully specified [low]",
                    "provision": "Article 12(1)",
                    "obligation_category": "record_keeping",
                    "engineering_action": "Specify log fields, retention, access controls, and audit review.",
                },
                {
                    "description": "Technical documentation expectations not fully specified [low]",
                    "provision": "Article 11(1)",
                    "obligation_category": "technical_documentation",
                    "engineering_action": "Document design decisions, evidence, and compliance rationale.",
                },
            ],
            "citations": [
                {
                    "label": "Record-keeping, Article 12(1)",
                    "text": "High-risk AI systems shall technically allow for the automatic recording of events over the lifetime of the system.",
                },
                {
                    "label": "Technical documentation, Article 11(1)",
                    "text": "The technical documentation of a high-risk AI system shall be drawn up before that system is placed on the market or put into service and shall be kept up to date.",
                },
            ],
            "recommendations": [
                "Specify log fields, retention, access controls, and audit review.",
                "Document design decisions, evidence, and compliance rationale.",
            ],
        },
    ])

def _render(
    request: Request,
    entries: list[dict[str, Any]] | None = None,
    status: str = "Demo report loaded",
    error: str | None = None,
    report_path: Path | None = None,
    uploaded_filename: str | None = None,
) -> HTMLResponse:
    entries = _normalise_entries(entries or _demo_entries())
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "entries": entries,
            "counts": _entry_counts(entries),
            "categories": _categories_from_entries(entries),
            "status": status,
            "error": error,
            "report_token": report_path.name if report_path else None,
            "uploaded_filename": uploaded_filename,
        },
    )


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/", response_class=HTMLResponse)
def home(request: Request) -> HTMLResponse:
    return _render(request)


@app.get("/demo")
def demo() -> RedirectResponse:
    return RedirectResponse(url="/", status_code=303)


@app.get("/download/{report_token}")
def download_report(report_token: str) -> FileResponse:
    safe_name = Path(report_token).name
    path = OUTPUT_DIR / safe_name
    if not path.exists():
        raise FileNotFoundError("Report not found or expired.")
    return FileResponse(path, filename="eu-ai-risk-assessment.md", media_type="text/markdown")


@app.post("/assess", response_class=HTMLResponse)
async def assess(
    request: Request,
    requirements_file: UploadFile = File(...),
    mode: str = Form("non-agent"),
) -> HTMLResponse:
    suffix = Path(requirements_file.filename or "requirements.txt").suffix.lower()
    if suffix not in SUPPORTED_EXTENSIONS:
        return _render(
            request,
            status="Could not run assessment",
            error=f"Unsupported file type '{suffix}'. Upload JSON, TXT, MD, PDF, or DOCX.",
        )

    upload_dir = Path(tempfile.mkdtemp(prefix="eu_ai_risks_upload_"))
    upload_path = upload_dir / f"uploaded{suffix}"
    upload_path.write_bytes(await requirements_file.read())

    try:
        requirements = _extract_requirements(upload_path)
        if not requirements:
            raise ValueError("No requirements were found. Use JSON, or include shall/should/must requirement statements.")

        entries, report_path = _run_assessment(requirements, use_agent=(mode == "agent"))
        return _render(
            request,
            entries=entries,
            status=f"Assessment complete: {len(entries)} requirements reviewed",
            report_path=report_path,
            uploaded_filename=requirements_file.filename,
        )
    except Exception as exc:  # Keep the UI useful during local demo/debugging.
        return _render(
            request,
            status="Could not run assessment",
            error=str(exc),
            uploaded_filename=requirements_file.filename,
        )


def _run_assessment(
    requirements: list[ParsedRequirement],
    use_agent: bool = False,
) -> tuple[list[dict[str, Any]], Path]:
    if use_agent:
        from eu_ai_risks.analysis.risk_assessor_agent import assess_requirement
    else:
        from eu_ai_risks.analysis.risk_assessor import assess_requirement

    categories = list_categories()
    article_cache: dict[str, dict] = {}
    assessment_entries: list[dict[str, Any]] = []

    for requirement in requirements:
        assessment, fetched_articles, _raw = assess_requirement(
            requirement.id,
            requirement.text,
            categories=categories,
        )
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

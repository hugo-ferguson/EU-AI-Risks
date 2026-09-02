"""
FastAPI integration for the EU AI Act risk assessment proof of concept.

This exposes the existing CLI risk assessment pipeline to the frontend.
The endpoint accepts a requirements document upload, extracts requirement-like
statements, runs the semantic-profile risk assessor, and returns frontend-ready
JSON plus the generated Markdown report.
"""

from __future__ import annotations

import json
import re
import tempfile
from pathlib import Path
from typing import Any

import pdfplumber
from fastapi import FastAPI, File, HTTPException, UploadFile
from fastapi.middleware.cors import CORSMiddleware

from eu_ai_risks.analysis.risk_assessor import assess_requirement
from eu_ai_risks.analysis.risk_report import (
    collect_citations,
    entries_from_assessments,
    render_markdown_report,
)
from eu_ai_risks.db.graph import list_categories

SUPPORTED_REQUIREMENT_UPLOADS = {
    ".json",
    ".txt",
    ".md",
    ".markdown",
    ".pdf",
    ".docx",
}

RE_REQUIREMENT_ID = re.compile(
    r"\b((?:FR|NFR|REQ|R|UC|SR|SYS|SRS)[-_ ]?\d+(?:\.\d+)*)\b",
    re.IGNORECASE,
)
RE_REQUIREMENT_VERB = re.compile(
    r"\b(shall|should|must|needs to|is required to|may not|must not)\b",
    re.IGNORECASE,
)
RE_NUMBERED_ITEM = re.compile(r"^(\d+(?:\.\d+)*|[A-Z]\d+)[.)]\s+(.+)$")

app = FastAPI(title="EU AI Risk Mapper API", version="0.1.0")

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5174",
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "http://localhost:5174",
        "http://127.0.0.1:5174",
        "http://localhost:5180",
        "http://127.0.0.1:5180",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/api/assess-risks")
async def assess_risks_from_upload(
    file: UploadFile = File(...),
) -> dict[str, Any]:
    """Run risk assessment for an uploaded requirements document."""

    filename = file.filename or "requirements.txt"
    suffix = Path(filename).suffix.lower()
    if suffix not in SUPPORTED_REQUIREMENT_UPLOADS:
        raise HTTPException(
            status_code=400,
            detail=(
                f"Unsupported file type '{suffix}'. Upload JSON, TXT, MD, PDF, or DOCX."
            ),
        )

    with tempfile.TemporaryDirectory() as tmp_dir:
        upload_path = Path(tmp_dir) / Path(filename).name
        upload_path.write_bytes(await file.read())

        try:
            requirements = extract_requirements(upload_path)
        except Exception as exc:  # pragma: no cover - defensive API boundary
            raise HTTPException(status_code=400, detail=str(exc)) from exc

    if not requirements:
        raise HTTPException(
            status_code=400,
            detail="No requirements were found. Use JSON requirements or a document with shall/should/must style statements.",
        )

    try:
        entries = run_assessment(requirements)
    except Exception as exc:  # pragma: no cover - lets frontend show readable error
        raise HTTPException(status_code=500, detail=f"Risk assessment failed: {exc}") from exc

    markdown = render_markdown_report(entries)
    report = entries_to_frontend_report(entries)
    report["markdown"] = markdown
    report["requirements_count"] = len(requirements)
    return report


def extract_requirements(path: Path) -> list[dict[str, str]]:
    """
    Extract lightweight requirement objects from an uploaded file.

    JSON files can be either:
    - a list of {id, text} objects, or
    - an object with a requirements key containing that list.

    Text, Markdown, PDF, and DOCX files are parsed line-by-line for statements
    that look like software requirements. This intentionally avoids the heavier
    triple-extraction path used by load-requirements, so the frontend can run the
    assessment without doing unnecessary KG writes.
    """

    suffix = path.suffix.lower()
    if suffix == ".json":
        data = json.loads(path.read_text(encoding="utf-8"))
        if isinstance(data, dict):
            data = data.get("requirements", data.get("items", []))
        if not isinstance(data, list):
            raise ValueError("JSON must be a list of requirements or contain a requirements array.")
        return normalise_json_requirements(data)

    if suffix == ".pdf":
        lines = read_pdf_lines(path)
    elif suffix == ".docx":
        lines = read_docx_lines(path)
    else:
        lines = path.read_text(encoding="utf-8").splitlines()

    return extract_requirements_from_lines(lines)


def normalise_json_requirements(data: list[Any]) -> list[dict[str, str]]:
    requirements: list[dict[str, str]] = []
    for index, item in enumerate(data, start=1):
        if isinstance(item, str):
            text = item.strip()
            requirement_id = f"REQ-{index:03d}"
        elif isinstance(item, dict):
            text = str(
                item.get("text")
                or item.get("requirement")
                or item.get("description")
                or ""
            ).strip()
            requirement_id = str(item.get("id") or item.get("requirement_id") or f"REQ-{index:03d}").strip()
        else:
            continue

        if text:
            requirements.append({"id": requirement_id, "text": text})
    return requirements


def read_pdf_lines(path: Path) -> list[str]:
    lines: list[str] = []
    with pdfplumber.open(path) as pdf:
        for page in pdf.pages:
            text = page.extract_text() or ""
            lines.extend(text.splitlines())
    return lines


def read_docx_lines(path: Path) -> list[str]:
    try:
        from docx import Document
    except ImportError as exc:
        raise ValueError("DOCX upload requires python-docx to be installed.") from exc

    document = Document(str(path))
    return [paragraph.text for paragraph in document.paragraphs]


def extract_requirements_from_lines(lines: list[str]) -> list[dict[str, str]]:
    requirements: list[dict[str, str]] = []
    seen: set[str] = set()

    for raw_line in lines:
        line = normalise_requirement_line(raw_line)
        if not line or not looks_like_requirement(line):
            continue

        requirement_id = extract_requirement_id(line) or f"REQ-{len(requirements) + 1:03d}"
        text = strip_requirement_prefix(line)
        key = text.lower()
        if text and key not in seen:
            requirements.append({"id": requirement_id, "text": text})
            seen.add(key)

    return requirements


def normalise_requirement_line(line: str) -> str:
    line = re.sub(r"^[-*•]\s*", "", line.strip())
    return re.sub(r"\s+", " ", line).strip()


def looks_like_requirement(line: str) -> bool:
    if RE_REQUIREMENT_ID.search(line) and len(line.split()) >= 4:
        return True
    if RE_REQUIREMENT_VERB.search(line) and len(line.split()) >= 5:
        return True
    numbered_match = RE_NUMBERED_ITEM.match(line)
    return bool(numbered_match and RE_REQUIREMENT_VERB.search(numbered_match.group(2)))


def extract_requirement_id(line: str) -> str | None:
    match = RE_REQUIREMENT_ID.search(line)
    if not match:
        return None
    return re.sub(r"\s+", "-", match.group(1).upper())


def strip_requirement_prefix(line: str) -> str:
    line = RE_REQUIREMENT_ID.sub("", line, count=1).strip(" :-\t")
    numbered_match = RE_NUMBERED_ITEM.match(line)
    if numbered_match:
        return numbered_match.group(2).strip()
    return line


def run_assessment(requirements: list[dict[str, str]]) -> list[dict[str, Any]]:
    categories = list_categories()
    article_cache: dict[str, dict] = {}
    assessment_entries: list[dict[str, Any]] = []

    for requirement in requirements:
        requirement_id = requirement.get("id", "REQ")
        requirement_text = requirement.get("text", "")
        assessment, fetched_articles, _raw = assess_requirement(
            requirement_id,
            requirement_text,
            categories=categories,
        )
        article_cache.update(fetched_articles)
        citations = collect_citations(assessment.risks, article_cache)
        assessment_entries.append(
            {
                "requirement": requirement,
                "assessment": assessment,
                "citations": citations,
            }
        )

    return entries_from_assessments(assessment_entries)


def entries_to_frontend_report(entries: list[dict[str, Any]]) -> dict[str, Any]:
    summary = {"high": 0, "medium": 0, "low": 0, "unmapped": 0}
    findings = []

    for entry in entries:
        level = str(entry.get("risk_level") or "low").lower()
        summary[level] = summary.get(level, 0) + 1

        risks = []
        for risk in entry.get("risks", []):
            provision = risk.get("provision")
            description = risk.get("description", "")
            if provision and provision not in description:
                description = f"{description} — {provision}"

            risks.append(
                {
                    "description": description,
                    "category": risk.get("obligation_category") or risk.get("category") or "general",
                    "action": risk.get("engineering_action") or "Review this requirement manually.",
                    "provision": provision,
                }
            )

        findings.append(
            {
                "id": entry.get("id", "Unknown"),
                "level": level,
                "requirement": entry.get("text", ""),
                "analysis": entry.get("analysis", ""),
                "risks": risks,
                "recommendations": entry.get("recommendations", []),
                "citations": entry.get("citations", []),
            }
        )

    return {"summary": summary, "findings": findings}

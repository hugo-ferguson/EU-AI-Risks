"""
Generate traceable risk reports from requirement assessments.
"""

import json
import re
from pathlib import Path

MAX_CITATION_TEXT_LENGTH = 500

SEVERITY_RANK = {"low": 0, "medium": 1, "high": 2}


def _normalise_level(value: str | None, default: str = "medium") -> str:
    level = str(value or default).strip().lower()
    return level if level in SEVERITY_RANK else default


def _entry_risk_level(assessment) -> str:
    """Use the highest mapped risk severity as the requirement-level risk.

    This keeps the Markdown summary and frontend counters logically aligned with
    the detailed mapped provisions. For example, an Article 5 high-severity
    prohibited-practice item should make the whole requirement finding high.
    """
    risks = getattr(assessment, "risks", []) or []
    if not risks:
        return _normalise_level(getattr(assessment, "risk_level", None), "low")
    return max(
        (_normalise_level(getattr(risk, "severity", None), "medium") for risk in risks),
        key=lambda level: SEVERITY_RANK[level],
    )

# Extracts the value of "summary" from JSON even when the rest is truncated
_RE_SUMMARY_VALUE = re.compile(r'"summary"\s*:\s*"((?:[^"\\]|\\.)*)"')


def _sanitise_analysis(text: str) -> str:
    """If the analysis field is raw JSON, extract the summary from it."""
    stripped = text.strip()
    if not stripped.startswith("{"):
        return text
    try:
        data = json.loads(stripped)
        if isinstance(data, dict) and "summary" in data:
            return data["summary"]
    except (json.JSONDecodeError, ValueError):
        # JSON is malformed/truncated; try regex extraction
        match = _RE_SUMMARY_VALUE.search(stripped)
        if match:
            return match.group(1).replace('\\"', '"').replace("\\n", "\n")
    return text


def entries_from_assessments(assessment_entries: list[dict]) -> list[dict]:
    """Convert LLM assessment entries to the common report entry format."""
    entries = []
    for entry in assessment_entries:
        requirement = entry["requirement"]
        assessment = entry["assessment"]

        risks = []
        for risk in assessment.risks:
            severity = f" [{risk.severity}]" if risk.severity else ""
            risks.append({
                "description": f"{risk.description}{severity}",
                "severity": _normalise_level(risk.severity),
                "provision": risk.provision,
                "obligation_category": risk.obligation_category,
                "engineering_action": risk.engineering_action,
            })

        entries.append({
            "id": requirement.get("id", "Unknown"),
            "text": requirement.get("text", ""),
            "risk_level": _entry_risk_level(assessment),
            "analysis": _sanitise_analysis(assessment.summary),
            "risks": risks,
            "citations": entry.get("citations", []),
            "recommendations": assessment.recommendations,
        })

    return entries


def render_markdown_report(
    entries: list[dict],
    title: str = "EU AI Act Risk Assessment",
) -> str:
    lines = [
        f"# {title}",
        "",
        "This report identifies compliance risks between software requirements "
        "and the EU AI Act. It is an engineering review aid, not legal advice.",
        "",
        "## Summary",
        "",
    ]

    level_counts: dict[str, int] = {}
    for entry in entries:
        level = entry["risk_level"].capitalize()
        level_counts[level] = level_counts.get(level, 0) + 1
    for level in ("High", "Medium", "Low"):
        count = level_counts.get(level, 0)
        if count:
            lines.append(f"- {level}: {count}")

    lines.extend(["", "## Requirement Findings", ""])

    for entry in entries:
        lines.extend([
            f"### {entry['id']}",
            "",
            f"**Risk level:** {entry['risk_level']}",
            "",
            f"**Requirement:** {entry['text']}",
            "",
            f"**Analysis:** {entry['analysis']}",
            "",
        ])

        if entry.get("risks"):
            lines.append("**Risks:**")
            lines.append("")
            for risk in entry["risks"]:
                provision = f" - {risk['provision']}" if risk.get(
                    "provision") else ""
                lines.append(f"- {risk['description']}{provision}")
                if risk.get("obligation_category"):
                    lines.append(
                        f"  - Category: `{risk['obligation_category']}`")
                if risk.get("engineering_action"):
                    lines.append(
                        f"  - Action: {risk['engineering_action']}"
                    )
            lines.append("")

        if entry.get("citations"):
            lines.append("**Cited provisions:**")
            lines.append("")
            for citation in entry["citations"]:
                lines.append(f"- **{citation['label']}**")
                lines.append(f"  > {citation['text']}")
            lines.append("")

        if entry.get("recommendations"):
            lines.append("**Recommendations:**")
            lines.append("")
            for recommendation in entry["recommendations"]:
                lines.append(f"- {recommendation}")
            lines.append("")

        lines.append("---")
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def write_markdown_report(
    entries: list[dict],
    output_path: Path,
    title: str = "EU AI Act Risk Assessment",
) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(
        render_markdown_report(entries, title), encoding="utf-8",
    )


def collect_citations(
    risks: list,
    article_cache: dict[str, dict],
) -> list[dict]:
    """Look up source text for each risk's article/annex and paragraph number."""
    from eu_ai_risks.db.graph import get_article, get_annex

    seen: set[tuple[str, int | None]] = set()
    citations = []
    for risk in risks:
        if not risk.article_id:
            continue

        key = (risk.article_id, risk.paragraph_num)
        if key in seen:
            continue
        seen.add(key)

        if risk.article_id not in article_cache:
            fetched = (
                get_annex(risk.article_id)
                if str(risk.article_id).startswith("annex:")
                else get_article(risk.article_id)
            )
            if fetched:
                article_cache[risk.article_id] = fetched

        article = article_cache.get(risk.article_id)
        if not article:
            continue

        title = article.get("title", risk.article_id)
        article_num = article.get("num", "")

        if str(risk.article_id).startswith("annex:"):
            text = article.get("text", "")
            if text:
                citations.append({
                    "label": f"{title} ({risk.article_id})",
                    "text": text[:MAX_CITATION_TEXT_LENGTH],
                })
            continue

        if risk.paragraph_num is not None:
            paragraph = next(
                (candidate for candidate in article.get("paragraphs", [])
                 if candidate.get("num") == risk.paragraph_num),
                None,
            )
            if paragraph:
                citations.append({
                    "label": f"{title}, Article {article_num}({risk.paragraph_num})",
                    "text": paragraph["text"][:MAX_CITATION_TEXT_LENGTH],
                })
        else:
            text = article.get("text", "")
            if text:
                citations.append({
                    "label": title,
                    "text": text[:MAX_CITATION_TEXT_LENGTH],
                })

    return citations

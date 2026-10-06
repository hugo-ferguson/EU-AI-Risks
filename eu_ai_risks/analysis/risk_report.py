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


def _pretty_category(category: str) -> str:
    return category.replace("_", " ").replace("-", " ").strip() or "mapped provision"


def _highest_risk_level(entries: list[dict]) -> str:
    levels = [str(entry.get("risk_level", "")).lower() for entry in entries]
    if "high" in levels:
        return "high"
    if "medium" in levels:
        return "medium"
    return "low"


def build_overall_analysis(entries: list[dict]) -> dict:
    """Build an overall reviewer summary from individual requirement findings.

    This is intentionally deterministic: it summarises the returned
    requirement-level analyses rather than making another LLM call.
    """
    total = len(entries)
    counts = {"high": 0, "medium": 0, "low": 0}
    category_counts: dict[str, int] = {}
    recommendations: list[str] = []
    control_like = 0

    for entry in entries:
        level = str(entry.get("risk_level", "medium")).lower()
        if level in counts:
            counts[level] += 1
        if level == "low":
            analysis = str(entry.get("analysis", "")).lower()
            if "control" in analysis or "safeguard" in analysis:
                control_like += 1

        for risk in entry.get("risks", []) or []:
            category = risk.get("obligation_category")
            if category:
                category_counts[category] = category_counts.get(category, 0) + 1
            action = risk.get("engineering_action")
            if action and action not in recommendations:
                recommendations.append(action)

    priority_categories = [
        {
            "name": category,
            "label": _pretty_category(category),
            "count": count,
        }
        for category, count in sorted(
            category_counts.items(),
            key=lambda item: (-item[1], _pretty_category(item[0])),
        )
    ]

    if total == 0:
        text = "No requirement findings are available yet."
    else:
        count_bits = []
        for level in ("high", "medium", "low"):
            if counts[level]:
                label = "finding" if counts[level] == 1 else "findings"
                count_bits.append(f"{counts[level]} {level}-risk {label}")
        risk_sentence = ", ".join(count_bits) if count_bits else "no retained risk findings"
        if priority_categories:
            category_sentence = ", ".join(item["label"] for item in priority_categories[:5])
        else:
            category_sentence = "no specific EU AI Act provision area"

        text = (
            f"Overall, the assessment reviewed {total} requirements and identified {risk_sentence}. "
            f"The main review focus areas are {category_sentence}. "
            "Use the individual requirement findings below to confirm owners, evidence, and follow-up actions before using this as supporting compliance evidence."
        )

    key_points = [
        f"{total} requirements reviewed in total.",
        f"Risk distribution: {counts['high']} high, {counts['medium']} medium, {counts['low']} low.",
    ]
    if priority_categories:
        key_points.append(
            "Most frequent mapped EU AI Act provision areas: "
            + ", ".join(f"{item['label']} ({item['count']})" for item in priority_categories[:5])
            + "."
        )
    if control_like:
        if control_like == 1:
            key_points.append(
                "1 low-risk requirement appears to describe a control or safeguard, but still needs clarification/evidence review."
            )
        else:
            key_points.append(
                f"{control_like} low-risk requirements appear to describe controls or safeguards, but still need clarification/evidence review."
            )

    follow_up_actions = []
    if counts["high"]:
        follow_up_actions.append("Review and assign owners for high-risk findings before the next project checkpoint.")
    if counts["medium"]:
        follow_up_actions.append("Review medium-risk gaps and confirm which engineering actions need to be implemented or documented.")
    if priority_categories:
        follow_up_actions.append("Check that the most frequent provision areas have clear evidence, owners, and documentation links.")
    follow_up_actions.append("Use the individual requirement findings as the traceable evidence trail for detailed review.")

    return {
        "risk_level": _highest_risk_level(entries),
        "text": text,
        "counts": counts,
        "priority_categories": priority_categories,
        "key_points": key_points,
        "recommended_actions": follow_up_actions,
        "top_recommendations": recommendations[:5],
    }


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
    overall_analysis: dict | None = None,
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

    overall_analysis = overall_analysis or build_overall_analysis(entries)

    lines.extend([
        "",
        "### Overall analysis",
        "",
        overall_analysis["text"],
        "",
    ])

    if overall_analysis.get("key_points"):
        lines.append("**Review points:**")
        lines.append("")
        for point in overall_analysis["key_points"]:
            lines.append(f"- {point}")
        lines.append("")

    if overall_analysis.get("recommended_actions"):
        lines.append("**Recommended follow-up actions:**")
        lines.append("")
        for action in overall_analysis["recommended_actions"]:
            lines.append(f"- {action}")
        lines.append("")

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

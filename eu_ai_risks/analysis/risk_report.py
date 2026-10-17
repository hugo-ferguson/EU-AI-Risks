"""
Generate traceable risk reports from requirement assessments.
"""

import json
import re
from pathlib import Path

RISK_LEVELS = ("high", "medium", "low")
# Assessments that failed or had nothing retrieved; see risk_assessor._not_assessed
NOT_ASSESSED = "unknown"
MAX_PRIORITY_CATEGORIES = 5

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
    except json.JSONDecodeError:
        # JSON is malformed/truncated; try regex extraction
        match = _RE_SUMMARY_VALUE.search(stripped)
        if match:
            return match.group(1).replace('\\"', '"').replace("\\n", "\n")
    return text


def pretty_category(category: str) -> str:
    return category.replace("_", " ").replace("-", " ").strip() or "mapped obligation"


def _join(items: list[str]) -> str:
    return items[0] if len(items) == 1 else f"{', '.join(items[:-1])} and {items[-1]}"


def _highest_risk_level(entries: list[dict]) -> str:
    levels = {str(entry.get("risk_level", "")).lower() for entry in entries}
    return next((level for level in RISK_LEVELS if level in levels), "low")


def build_overall_analysis(entries: list[dict]) -> dict:
    """Build an overall review summary from individual requirement findings.

    This is intentionally deterministic: it summarises the returned
    requirement-level analyses rather than making another LLM call.
    """
    total = len(entries)
    counts = dict.fromkeys(RISK_LEVELS, 0)
    not_assessed = 0
    category_counts: dict[str, int] = {}
    control_like = 0

    for entry in entries:
        level = str(entry.get("risk_level", "medium")).lower()
        if level in counts:
            counts[level] += 1
        elif level == NOT_ASSESSED:
            not_assessed += 1
        if level == "low":
            analysis = str(entry.get("analysis", "")).lower()
            if "control" in analysis or "safeguard" in analysis:
                control_like += 1

        for risk in entry.get("risks") or []:
            category = risk.get("obligation_category")
            if category:
                category_counts[category] = category_counts.get(category, 0) + 1

    priority_categories = [
        {"name": category, "label": pretty_category(category), "count": count}
        for category, count in sorted(
            category_counts.items(), key=lambda item: (-item[1], pretty_category(item[0]))
        )
    ][:MAX_PRIORITY_CATEGORIES]

    if total == 0:
        text = "No requirement findings are available yet."
    else:
        rated = [f"{counts[level]} as {level} risk" for level in RISK_LEVELS if counts[level]]
        sentence = f"Overall, the assessment reviewed {total} requirements"
        if rated:
            sentence += f" and rated {_join(rated)}"
        if not_assessed:
            sentence += f"; {not_assessed} could not be assessed"
        focus = (
            _join([item["label"] for item in priority_categories])
            if priority_categories else "no specific obligation category"
        )
        text = (
            f"{sentence}. The main review focus areas are {focus}. "
            "Use the individual requirement findings below to confirm owners, evidence, "
            "and follow-up actions before using this as supporting compliance evidence."
        )

    distribution = ", ".join(f"{counts[level]} {level}" for level in RISK_LEVELS)
    if not_assessed:
        distribution += f", {not_assessed} not assessed"
    key_points = [
        f"{total} requirements reviewed in total.",
        f"Risk distribution: {distribution}.",
    ]
    if priority_categories:
        key_points.append(
            "Most frequent mapped obligation areas: "
            + ", ".join(f"{item['label']} ({item['count']})" for item in priority_categories)
            + "."
        )
    if control_like:
        label = "requirement appears" if control_like == 1 else "requirements appear"
        key_points.append(
            f"{control_like} low-risk {label} to describe a control or safeguard, "
            "but still needs clarification/evidence review."
        )

    actions = []
    if not_assessed:
        actions.append("Re-run or manually review the requirements that could not be assessed.")
    if counts["high"]:
        actions.append("Review and assign owners for high-risk findings before the next project checkpoint.")
    if counts["medium"]:
        actions.append("Review medium-risk gaps and confirm which engineering actions need to be implemented or documented.")
    if priority_categories:
        actions.append("Check that the most frequent obligation areas have clear evidence, owners, and documentation links.")
    actions.append("Use the individual requirement findings as the traceable evidence trail for detailed review.")

    return {
        "risk_level": _highest_risk_level(entries),
        "text": text,
        "counts": counts,
        "not_assessed": not_assessed,
        "priority_categories": priority_categories,
        "key_points": key_points,
        "recommended_actions": actions,
    }


def entries_from_assessments(assessment_entries: list[dict]) -> list[dict]:
    """Convert LLM assessment entries to the common report entry format."""
    entries = []
    for entry in assessment_entries:
        requirement = entry["requirement"]
        assessment = entry["assessment"]
        entries.append({
            "id": requirement.get("id", "Unknown"),
            "text": requirement.get("text", ""),
            "risk_level": assessment.risk_level,
            "analysis": _sanitise_analysis(assessment.summary),
            "risks": [
                {
                    "text": risk.description,
                    "severity": risk.severity,
                    "provision": risk.provision,
                    "obligation_category": risk.obligation_category,
                    "engineering_action": risk.engineering_action,
                    "provision_id": risk.provision_id,
                    "citation_supplied": risk.citation_supplied,
                    "trace": risk.trace,
                    "scope_warning": risk.scope_warning,
                }
                for risk in assessment.risks
            ],
            "citations": entry.get("citations", []),
            "recommendations": assessment.recommendations,
            "classification": assessment.classification,
            "selected_articles": assessment.selected_articles,
        })
    return entries


def _bullets(heading: str, items: list[str]) -> list[str]:
    return [f"**{heading}:**", "", *(f"- {item}" for item in items), ""] if items else []


def _risk_lines(risk: dict) -> list[str]:
    severity = f" [{risk['severity']}]" if risk.get("severity") else ""
    provision = f" - {risk['provision']}" if risk.get("provision") else ""
    node = f" (`{risk['provision_id']}`)" if risk.get("provision_id") else ""
    lines = [f"- {risk['text']}{severity}{provision}{node}"]
    if not risk.get("citation_supplied", True):
        lines.append(
            "  - Warning: the cited provision was not among the provisions "
            "retrieved for this assessment, so it is not grounded in the graph.")
    if risk.get("scope_warning"):
        lines.append(f"  - Scope warning: {risk['scope_warning']}")
    if risk.get("obligation_category"):
        lines.append(f"  - Category: `{risk['obligation_category']}`")
    if risk.get("engineering_action"):
        lines.append(f"  - Action: {risk['engineering_action']}")
    if risk.get("trace"):
        lines.append("  - Trace:")
        lines.extend(f"    - {step}" for step in risk["trace"])
    return lines


def _entry_lines(entry: dict) -> list[str]:
    lines = [
        f"### {entry['id']}",
        "",
        f"**Risk level:** {entry['risk_level']}",
        "",
        f"**Requirement:** {entry['text']}",
        "",
    ]
    if entry.get("classification"):
        lines.extend([f"**Classified as:** {'; '.join(entry['classification'])}", ""])
    if entry.get("selected_articles"):
        lines.extend([
            f"**Articles selected from the index:** {'; '.join(entry['selected_articles'])}",
            "",
        ])
    lines.extend([f"**Analysis:** {entry['analysis']}", ""])

    if entry.get("risks"):
        lines.extend(["**Risks:**", ""])
        for risk in entry["risks"]:
            lines.extend(_risk_lines(risk))
        lines.append("")

    if entry.get("citations"):
        lines.extend(["**Cited provisions:**", ""])
        for citation in entry["citations"]:
            lines.extend([f"- **{citation['label']}**", f"  > {citation['text']}"])
        lines.append("")

    lines.extend(_bullets("Recommendations", entry.get("recommendations") or []))
    lines.extend(["---", ""])
    return lines


def render_markdown_report(
    entries: list[dict],
    title: str = "EU AI Act Risk Assessment",
    overall_analysis: dict | None = None,
) -> str:
    overall_analysis = overall_analysis or build_overall_analysis(entries)
    counts = overall_analysis["counts"]

    lines = [
        f"# {title}",
        "",
        "This report identifies compliance risks between software requirements "
        "and the EU AI Act. It is an engineering review aid, not legal advice.",
        "",
        "## Summary",
        "",
    ]
    lines.extend(
        f"- {level.capitalize()}: {counts[level]}" for level in RISK_LEVELS if counts[level])
    # Failed or unretrievable assessments must stay visible, not vanish from the totals
    if overall_analysis.get("not_assessed"):
        lines.append(f"- Not assessed: {overall_analysis['not_assessed']}")

    lines.extend(["", "### Overall analysis", "", overall_analysis["text"], ""])
    lines.extend(_bullets("Review points", overall_analysis.get("key_points") or []))
    lines.extend(_bullets(
        "Recommended follow-up actions", overall_analysis.get("recommended_actions") or []))

    lines.extend(["## Requirement Findings", ""])
    for entry in entries:
        lines.extend(_entry_lines(entry))

    return "\n".join(lines).rstrip() + "\n"


def write_markdown_report(
    entries: list[dict],
    output_path: Path,
    title: str = "EU AI Act Risk Assessment",
    overall_analysis: dict | None = None,
) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(
        render_markdown_report(entries, title, overall_analysis), encoding="utf-8",
    )


def collect_citations(
    risks: list,
    article_cache: dict[str, dict],
) -> list[dict]:
    """Quote the exact provision each risk cites: a lettered point where one is
    cited, otherwise the paragraph, falling back to the whole article."""
    # Imported here so report rendering doesn't need a database connection
    from eu_ai_risks.db.graph import get_article, get_provisions, provision_label

    provisions = get_provisions(list(dict.fromkeys(
        risk.provision_id for risk in risks if risk.provision_id)))

    seen: set[str] = set()
    citations = []
    for risk in risks:
        node = provisions.get(risk.provision_id)
        if node:
            if risk.provision_id not in seen:
                seen.add(risk.provision_id)
                citations.append({
                    "label": f"{node['article_title']}, {provision_label(risk.provision_id)}",
                    "text": node["text"],
                })
            continue

        if not risk.article_id or risk.article_id in seen:
            continue
        seen.add(risk.article_id)

        if risk.article_id not in article_cache:
            fetched = get_article(risk.article_id)
            if fetched:
                article_cache[risk.article_id] = fetched
        article = article_cache.get(risk.article_id)
        if article and article.get("text"):
            citations.append({
                "label": article.get("title", risk.article_id),
                "text": article["text"],
            })

    return citations

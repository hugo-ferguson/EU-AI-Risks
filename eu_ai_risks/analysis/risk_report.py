"""
Generate traceable risk reports from requirement assessments.
"""

import json
import re
from pathlib import Path

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
    return category.replace("_", " ").replace("-", " ").strip() or "mapped obligation"


def _highest_risk_level(entries: list[dict]) -> str:
    levels = [str(entry.get("risk_level", "")).lower() for entry in entries]
    if "high" in levels:
        return "high"
    if "medium" in levels:
        return "medium"
    return "low"


def build_overall_analysis(entries: list[dict]) -> dict:
    """Build an overall review summary from individual requirement findings.

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
            category_counts.items(), key=lambda item: (-item[1], _pretty_category(item[0]))
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
            category_sentence = "no specific obligation category"

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
            "Most frequent mapped obligation areas: "
            + ", ".join(f"{item['label']} ({item['count']})" for item in priority_categories[:5])
            + "."
        )
    if control_like:
        label = "requirement appears" if control_like == 1 else "requirements appear"
        key_points.append(
            f"{control_like} low-risk {label} to describe a control or safeguard, but still needs clarification/evidence review."
        )

    pm_actions = []
    if counts["high"]:
        pm_actions.append("Review and assign owners for high-risk findings before the next project checkpoint.")
    if counts["medium"]:
        pm_actions.append("Review medium-risk gaps and confirm which engineering actions need to be implemented or documented.")
    if priority_categories:
        pm_actions.append("Check that the most frequent obligation areas have clear evidence, owners, and documentation links.")
    pm_actions.append("Use the individual requirement findings as the traceable evidence trail for detailed review.")

    return {
        "risk_level": _highest_risk_level(entries),
        "text": text,
        "counts": counts,
        "priority_categories": priority_categories,
        "key_points": key_points,
        "recommended_actions": pm_actions,
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
                "provision": risk.provision,
                "obligation_category": risk.obligation_category,
                "engineering_action": risk.engineering_action,
                "provision_id": risk.provision_id,
                "citation_supplied": risk.citation_supplied,
                "trace": risk.trace,
                "scope_warning": risk.scope_warning,
            })

        entries.append({
            "id": requirement.get("id", "Unknown"),
            "text": requirement.get("text", ""),
            "risk_level": assessment.risk_level,
            "analysis": _sanitise_analysis(assessment.summary),
            "risks": risks,
            "citations": entry.get("citations", []),
            "recommendations": assessment.recommendations,
            "classification": assessment.classification,
            "selected_articles": assessment.selected_articles,
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
    # Failed or unretrievable assessments must stay visible, not vanish from the totals
    if level_counts.get("Unknown"):
        lines.append(f"- Not assessed: {level_counts['Unknown']}")

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
        ])

        if entry.get("classification"):
            lines.extend([f"**Classified as:** {'; '.join(entry['classification'])}", ""])
        if entry.get("selected_articles"):
            lines.extend([
                f"**Articles selected from the index:** {'; '.join(entry['selected_articles'])}",
                "",
            ])

        lines.extend([
            f"**Analysis:** {entry['analysis']}",
            "",
        ])

        if entry.get("risks"):
            lines.append("**Risks:**")
            lines.append("")
            for risk in entry["risks"]:
                provision = f" - {risk['provision']}" if risk.get(
                    "provision") else ""
                node = f" (`{risk['provision_id']}`)" if risk.get("provision_id") else ""
                lines.append(f"- {risk['description']}{provision}{node}")
                if not risk.get("citation_supplied", True):
                    lines.append(
                        "  - Warning: the cited provision was not among the provisions "
                        "retrieved for this assessment, so it is not grounded in the graph.")
                if risk.get("scope_warning"):
                    lines.append(f"  - Scope warning: {risk['scope_warning']}")
                if risk.get("obligation_category"):
                    lines.append(
                        f"  - Category: `{risk['obligation_category']}`")
                if risk.get("engineering_action"):
                    lines.append(
                        f"  - Action: {risk['engineering_action']}"
                    )
                if risk.get("trace"):
                    lines.append("  - Trace:")
                    for step in risk["trace"]:
                        lines.append(f"    - {step}")
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
    from eu_ai_risks.db.graph import get_article, get_provisions, provision_label

    node_ids = list(dict.fromkeys(
        risk.provision_id for risk in risks if getattr(risk, "provision_id", "")))
    provisions = get_provisions(node_ids)

    seen: set[str] = set()
    citations = []
    for risk in risks:
        node_id = getattr(risk, "provision_id", "")
        node = provisions.get(node_id)
        if node:
            if node_id in seen:
                continue
            seen.add(node_id)
            citations.append({
                "label": f"{node['article_title']}, {provision_label(node_id)}",
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

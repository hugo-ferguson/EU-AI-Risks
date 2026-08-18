"""
Generate a traceable risk list from requirement-to-legislation mappings.
"""

import json
from pathlib import Path

from eu_ai_risks.analysis.risk_mapper import RiskMapping


def write_markdown_report(
	mappings: list[RiskMapping],
	output_path: Path,
	title: str = "EU AI Act Requirements Risk Report",
) -> None:
	"""
	Write a human-readable Markdown risk report.
	"""

	output_path.parent.mkdir(parents=True, exist_ok=True)
	output_path.write_text(render_markdown_report(mappings, title), encoding="utf-8")


def write_json_report(mappings: list[RiskMapping], output_path: Path) -> None:
	"""
	Write a machine-readable JSON risk report.
	"""

	output_path.parent.mkdir(parents=True, exist_ok=True)
	output_path.write_text(
		json.dumps([mapping.to_dict() for mapping in mappings], indent=2),
		encoding="utf-8",
	)


def render_markdown_report(
	mappings: list[RiskMapping],
	title: str = "EU AI Act Requirements Risk Report",
) -> str:
	lines = [
		f"# {title}",
		"",
		"This report maps extracted software requirements to candidate EU AI Act "
		"paragraphs using semantic similarity. It is an engineering review aid, "
		"not legal advice.",
		"",
		"## Summary",
		"",
	]

	level_counts = _count_risk_levels(mappings)
	for level in ("High", "Medium", "Low", "Unmapped"):
		lines.append(f"- {level}: {level_counts.get(level, 0)}")

	lines.extend(["", "## Requirement Findings", ""])

	for mapping in mappings:
		requirement = mapping.requirement
		lines.extend([
			f"### {requirement.id}",
			"",
			f"**Risk level:** {mapping.risk_level}",
			"",
			f"**Requirement:** {requirement.text}",
			"",
			f"**Source:** {_format_source(requirement)}",
			"",
			f"**Explanation:** {mapping.explanation}",
			"",
		])

		if mapping.risk_signals:
			lines.extend([
				"**Risk signals:** " + ", ".join(mapping.risk_signals),
				"",
			])

		if mapping.matches:
			lines.extend(["**Candidate EU AI Act provisions:**", ""])
			for match in mapping.matches:
				lines.extend([
					f"- Article {match.article_num}, paragraph "
					f"{match.paragraph_num} ({match.paragraph_id}), "
					f"score {match.score:.3f}",
					f"  - {match.article_title}",
					f"  - {match.paragraph_text}",
				])
			lines.append("")
		else:
			lines.extend([
				"**Candidate EU AI Act provisions:** None above threshold.",
				"",
			])

	return "\n".join(lines).rstrip() + "\n"


def _count_risk_levels(mappings: list[RiskMapping]) -> dict[str, int]:
	counts = {}
	for mapping in mappings:
		counts[mapping.risk_level] = counts.get(mapping.risk_level, 0) + 1
	return counts


def _format_source(requirement) -> str:
	parts = [requirement.source]
	if requirement.page:
		parts.append(f"page {requirement.page}")
	if requirement.section:
		parts.append(f"section {requirement.section}")
	if requirement.title:
		parts.append(requirement.title)
	return ", ".join(parts)

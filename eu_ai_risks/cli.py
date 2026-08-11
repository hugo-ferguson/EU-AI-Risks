"""
CLI entry point for eu-ai-risks.
"""

import json
import os
from pathlib import Path

import typer
from dotenv import load_dotenv

load_dotenv()

app = typer.Typer(help="Parse the EU AI Act into a Neo4j graph and query it.")


def _parse_and_build() -> tuple[dict, list]:
	"""Parse the PDF and build the in-memory graph."""
	from eu_ai_risks.legislation.eu_ai_act.parser import extract_segments
	from eu_ai_risks.legislation.eu_ai_act.graph_builder import (
		build_in_memory_graph,
		SEGMENT_TYPES,
	)

	pdf_path = Path(os.environ["PDF_PATH"])
	print(f"Parsing {pdf_path} ...")
	segments = extract_segments(pdf_path)

	nodes, edges = build_in_memory_graph(segments)

	for segment_type, type_config in SEGMENT_TYPES.items():
		node_count = sum(
			1 for node_properties in nodes.values() if
			node_properties["type"] == segment_type
		)
		print(f"  {node_count} {type_config['label']} nodes.")
	print(f"  {len(edges)} edges total.")

	return nodes, edges


@app.command()
def build():
	"""Parse the EU AI Act PDF and write the graph to Neo4j."""
	from eu_ai_risks.db import NEO4J_URI
	from eu_ai_risks.legislation.eu_ai_act.graph_builder import write_to_neo4j

	nodes, edges = _parse_and_build()

	print(f"\nWriting graph to Neo4j at {NEO4J_URI} ...")
	write_to_neo4j(nodes, edges)


@app.command()
def embed():
	"""Generate embeddings and write them to Neo4j."""
	from eu_ai_risks.legislation.eu_ai_act.graph_builder import (
		generate_and_write_embeddings,
	)

	nodes, _ = _parse_and_build()

	print("\nGenerating embeddings ...")
	generate_and_write_embeddings(nodes)


@app.command()
def chapter(chapter_id: str = typer.Argument(help="e.g. ch:III")):
	"""List articles in a chapter."""
	from eu_ai_risks.db.graph import articles_in_chapter

	for article_id, title in articles_in_chapter(chapter_id):
		print(f"  {article_id}: {title}")


@app.command()
def refs(article_id: str = typer.Argument(help="e.g. art:6")):
	"""List articles that reference the given article."""
	from eu_ai_risks.db.graph import referenced_by

	for ref_id, title in referenced_by(article_id):
		print(f"  {ref_id}: {title}")


@app.command("refs-from")
def refs_from(article_id: str = typer.Argument(help="e.g. art:5")):
	"""List articles that the given article references."""
	from eu_ai_risks.db.graph import references_from

	for ref_id, title in references_from(article_id):
		print(f"  {ref_id}: {title}")


@app.command()
def path(
	source: str = typer.Argument(help="e.g. art:5"),
	target: str = typer.Argument(help="e.g. art:85"),
):
	"""Find the shortest reference path between two articles."""
	from eu_ai_risks.db.graph import shortest_path

	reference_path = shortest_path(source, target)
	if reference_path:
		print(" -> ".join(reference_path))
	else:
		print("No path found.")


@app.command()
def search(
	query: str = typer.Argument(help="Natural language search query"),
	top_k: int = typer.Option(5, help="Number of results"),
	paragraphs: bool = typer.Option(
		False,
		"--paragraphs", "-p",
		help="Search paragraphs instead of articles"
	),
):
	"""Semantic search over articles or paragraphs."""
	from eu_ai_risks.db.graph import (
		vector_search_articles,
		vector_search_paragraphs,
	)
	from eu_ai_risks.embeddings import embed_text

	query_embedding = embed_text(query)

	if paragraphs:
		results = vector_search_paragraphs(query_embedding, top_k)
		for para_id, num, score in results:
			print(f"  {para_id} (para {num}) — score: {score:.4f}")
	else:
		results = vector_search_articles(query_embedding, top_k)
		for article_id, title, score in results:
			print(f"  {article_id}: {title} — score: {score:.4f}")


@app.command("parse-requirements")
def parse_requirements(
	document_path: Path = typer.Argument(help="Path to a .txt, .md, .pdf, or .docx SRS"),
	output: Path | None = typer.Option(
		None,
		"--output", "-o",
		help="Optional JSON output path",
	),
):
	"""Extract candidate software requirements from a requirements document."""
	from eu_ai_risks.requirements.loader import load_requirements

	requirements = load_requirements(document_path)

	if output:
		output.parent.mkdir(parents=True, exist_ok=True)
		output.write_text(
			json.dumps([requirement.to_dict() for requirement in requirements], indent=2),
			encoding="utf-8",
		)
		print(f"Wrote {len(requirements)} requirements to {output}.")
		return

	for requirement in requirements:
		location = []
		if requirement.page:
			location.append(f"page {requirement.page}")
		if requirement.section:
			location.append(f"section {requirement.section}")
		location_text = f" ({', '.join(location)})" if location else ""
		print(f"{requirement.id}{location_text}: {requirement.text}")


@app.command("analyze-requirements")
def analyze_requirements(
	document_path: Path = typer.Argument(help="Path to a .txt, .md, .pdf, or .docx SRS"),
	output: Path = typer.Option(
		Path("risk-report.md"),
		"--output", "-o",
		help="Markdown report output path",
	),
	json_output: Path | None = typer.Option(
		None,
		"--json-output",
		help="Optional JSON report output path",
	),
	top_k: int = typer.Option(5, help="Candidate EU AI Act paragraphs per requirement"),
	min_score: float = typer.Option(
		0.55,
		help="Minimum vector similarity score kept in the report",
	),
):
	"""
	Extract requirements, map them to EU AI Act paragraphs, and write a risk report.
	"""
	from eu_ai_risks.requirements.loader import load_requirements
	from eu_ai_risks.analysis.risk_mapper import map_requirements_to_legislation
	from eu_ai_risks.analysis.risk_report import (
		write_json_report,
		write_markdown_report,
	)

	requirements = load_requirements(document_path)
	if not requirements:
		print("No candidate requirements were extracted.")
		return

	print(f"Extracted {len(requirements)} requirements.")
	print("Mapping requirements to EU AI Act paragraph vectors in Neo4j ...")
	mappings = map_requirements_to_legislation(
		requirements,
		top_k=top_k,
		min_score=min_score,
	)

	write_markdown_report(mappings, output)
	print(f"Wrote Markdown risk report to {output}.")

	if json_output:
		write_json_report(mappings, json_output)
		print(f"Wrote JSON risk report to {json_output}.")


def main():
	app()


if __name__ == "__main__":
	main()

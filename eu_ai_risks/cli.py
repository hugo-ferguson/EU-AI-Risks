"""
CLI entry point for eu-ai-risks.
"""

import os
from pathlib import Path

import typer
from dotenv import load_dotenv

from eu_ai_risks.db import NEO4J_URI
from eu_ai_risks.db.graph import (
	articles_in_chapter,
	referenced_by,
	references_from,
	shortest_path,
	vector_search_articles,
	vector_search_paragraphs,
)
from eu_ai_risks.legislation.eu_ai_act.parser import extract_segments
from eu_ai_risks.legislation.eu_ai_act.graph_builder import (
	build_in_memory_graph,
	write_to_neo4j,
	generate_and_write_embeddings,
	SEGMENT_TYPES,
)

load_dotenv()

app = typer.Typer(help="Parse the EU AI Act into a Neo4j graph and query it.")


def _parse_and_build() -> tuple[dict, list]:
	"""Parse the PDF and build the in-memory graph."""
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
	nodes, edges = _parse_and_build()

	print(f"\nWriting graph to Neo4j at {NEO4J_URI} ...")
	write_to_neo4j(nodes, edges)


@app.command()
def embed():
	"""Generate embeddings and write them to Neo4j."""
	nodes, _ = _parse_and_build()

	print("\nGenerating embeddings ...")
	generate_and_write_embeddings(nodes)


@app.command()
def chapter(chapter_id: str = typer.Argument(help="e.g. ch:III")):
	"""List articles in a chapter."""
	for article_id, title in articles_in_chapter(chapter_id):
		print(f"  {article_id}: {title}")


@app.command()
def refs(article_id: str = typer.Argument(help="e.g. art:6")):
	"""List articles that reference the given article."""
	for ref_id, title in referenced_by(article_id):
		print(f"  {ref_id}: {title}")


@app.command("refs-from")
def refs_from(article_id: str = typer.Argument(help="e.g. art:5")):
	"""List articles that the given article references."""
	for ref_id, title in references_from(article_id):
		print(f"  {ref_id}: {title}")


@app.command()
def path(
	source: str = typer.Argument(help="e.g. art:5"),
	target: str = typer.Argument(help="e.g. art:85"),
):
	"""Find the shortest reference path between two articles."""
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


def main():
	app()


if __name__ == "__main__":
	main()

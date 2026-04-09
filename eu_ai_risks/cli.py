"""
CLI entry point for eu-ai-risks.
"""

import os
from pathlib import Path

from dotenv import load_dotenv

from eu_ai_risks.db import NEO4J_URI
from eu_ai_risks.db.graph import (
	articles_in_chapter,
	referenced_by,
	references_from,
	shortest_path,
)
from eu_ai_risks.legislation.eu_ai_act.parser import extract_segments
from eu_ai_risks.legislation.eu_ai_act.graph_builder import (
	build_in_memory_graph,
	write_to_neo4j,
	SEGMENT_TYPES,
)

load_dotenv()


def main():
	pdf_path = Path(os.environ["PDF_PATH"])

	# Parse the Act .PDF file into segments.
	print(f"Parsing {pdf_path} ...")
	segments = extract_segments(pdf_path)

	# Build a graph from the segments.
	nodes, edges = build_in_memory_graph(segments)

	# Show the graph metrics.
	for segment_type, type_config in SEGMENT_TYPES.items():
		node_count = sum(
			1 for node_properties in nodes.values() if
			node_properties["type"] == segment_type
		)
		print(f"  {node_count} {type_config['label']} nodes")

	print(f"  {len(edges)} edges total\n")

	# Write to the database.
	print(f"Writing to Neo4j at {NEO4J_URI} ...")
	write_to_neo4j(nodes, edges)

	# Perform some test queries.
	print("\n=== Articles in Chapter III (first 8) ===")
	for article_id, title in articles_in_chapter("ch:III")[:8]:
		print(f"  {article_id}: {title}")
	print("\n=== Articles that reference Article 6 ===")
	for article_id, title in referenced_by("art:6"):
		print(f"  {article_id}: {title}")
	print("\n=== Article 5 outgoing references ===")
	for article_id, title in references_from("art:5"):
		print(f"  {article_id}: {title}")
	print("\n=== Shortest reference path: Article 5 → Article 85 ===")
	reference_path = shortest_path("art:5", "art:85")
	print("  " + (" -> ".join(reference_path) if reference_path else "No path found."))


if __name__ == "__main__":
	main()

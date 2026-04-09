from eu_ai_risks.db import NEO4J_URI
from eu_ai_risks.parse_ai_act import extract_segments
from eu_ai_risks.generate_graph import (
	build_in_memory_graph,
	edges,
	nodes,
	write_to_neo4j,
	SEGMENT_TYPES,
	PDF_PATH,
)
from eu_ai_risks.query_graph import (
	articles_in_chapter,
	referenced_by,
	references_from,
	shortest_path,
)

def main():
	# Parse the Act .PDF file into segments.
	print(f"Parsing {PDF_PATH} ...")
	segments = extract_segments(PDF_PATH)

	# Build a graph from the segments.
	build_in_memory_graph(segments)

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
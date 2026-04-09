"""
Build an in-memory graph from EU AI Act segments and write it to Neo4j.
"""

import re
from collections import defaultdict
from typing import cast, LiteralString

from eu_ai_risks.db import get_session
from eu_ai_risks.models import Segment

# Regex that matches when an article references another. This defines
# 'REFERENCES' edges.
RE_ARTICLE_REF = re.compile(r'\bArticle\s+(\d+)\b')

# Types of Act segments (from the parser) and functions to construct them.
# Each props key contains a lambda function that returns the correct properties
# for the given segment type, based on the segment data provided.
SEGMENT_TYPES = {
	"chapter": {
		"label": "Chapter",
		"props": lambda segment: {"num": segment.num, "title": segment.title},
		"parent_rel": None,
		"parent_id": None,
		"cross_refs": None,
	},
	"article": {
		"label": "Article",
		"props": lambda segment: {
			"num": segment.num,
			"title": segment.title,
			"text": " ".join(segment.body),
		},
		"parent_rel": "CONTAINS",
		"parent_id": lambda segment: segment.parent_id,
		"cross_refs": lambda segment, all_nodes: [
			(f"art:{article_num}", "REFERENCES")
			for article_num in set(RE_ARTICLE_REF.findall(" ".join(segment.body)))
			if f"art:{article_num}" != segment.id and f"art:{article_num}" in all_nodes
		],
	},
	"paragraph": {
		"label": "Paragraph",
		"props": lambda segment: {
			"num": segment.num,
			"text": " ".join(segment.body),
		},
		"parent_rel": "HAS_PARAGRAPH",
		"parent_id": lambda segment: segment.parent_id,
		"cross_refs": None,
	},
}


def build_in_memory_graph(segments: list[Segment]) -> tuple[dict, list]:
	"""
	Build an in-memory graph from a list of segments.

	:param segments: the segments to build.
	:return: (nodes dict, edges list)
	"""

	nodes = {}
	edge_set = set()
	edges = []

	def add_node(node_id: str, node_type: str, **properties) -> None:
		nodes[node_id] = {"type": node_type, **properties}

	def add_edge(source_id: str, relationship: str, destination_id: str) -> None:
		key = (source_id, relationship, destination_id)
		if key not in edge_set:
			edge_set.add(key)
			edges.append({
				"src": source_id, "rel": relationship, "dst": destination_id
			})

	# Add the nodes.
	for segment in segments:
		type_config = SEGMENT_TYPES[segment.type]
		add_node(segment.id, segment.type, **type_config["props"](segment))

	# Add the edges (relationships) between nodes (segments).
	for segment in segments:
		type_config = SEGMENT_TYPES[segment.type]

		# Add the parent relationship.
		if type_config["parent_id"]:
			parent_id = type_config["parent_id"](segment)
			if parent_id and parent_id in nodes:
				add_edge(parent_id, type_config["parent_rel"], segment.id)

		# Add the references relationship.
		if type_config["cross_refs"]:
			for referenced_id, relationship in type_config["cross_refs"](segment, nodes):
				add_edge(segment.id, relationship, referenced_id)

	return nodes, edges


def write_to_neo4j(graph_nodes: dict, graph_edges: list) -> None:
	"""
	Send the graph to neo4j.

	:param graph_nodes: the nodes to write.
	:param graph_edges: the edges to write.
	:return: None
	"""
	with get_session() as session:
		for type_config in SEGMENT_TYPES.values():
			session.run(cast(LiteralString,
							 f"CREATE CONSTRAINT "
							 f"{type_config['label'].lower()}_id IF NOT EXISTS "
							 f"FOR (n:{type_config['label']}) "
							 f"REQUIRE n.id IS UNIQUE"
							 ))

		# Dictionary of node types. Each key contains the list of all nodes of
		# that type.
		# Used to send queries in bulk.
		nodes_by_type = defaultdict(list)

		# Group nodes into the nodes by type dictionary.
		for node_id, node_properties in graph_nodes.items():
			label = SEGMENT_TYPES[node_properties["type"]]["label"]
			node_data = {key: value for key, value in node_properties.items() if key != "type"}
			node_data["id"] = node_id
			nodes_by_type[label].append(node_data)

		# Push the nodes to the database.
		for label, node_batch in nodes_by_type.items():
			session.run(
				cast(LiteralString, f"""
					UNWIND $rows AS row
					MERGE (n:{label} {{id: row.id}})
					SET n += row
					"""),
				rows=node_batch,
			)

			print(f"  Wrote {len(node_batch)} {label} nodes.")

		# Dictionary of relationship types. Each key contains the list of all
		# relationships of that type.
		# Used to send queries in bulk.
		edges_by_relationship = defaultdict(list)

		# Group edges into the edges by relationship dictionary.
		for edge in graph_edges:
			edges_by_relationship[edge["rel"]].append(edge)

		# Push edges to the database.
		for relationship_type, relationship_edges in edges_by_relationship.items():
			session.run(
				cast(LiteralString, f"""
					UNWIND $rows AS row
					MATCH (a {{id: row.src}})
					MATCH (b {{id: row.dst}})
					MERGE (a)-[:{relationship_type}]->(b)
					"""),
				rows=relationship_edges,
			)

			print(f"  Wrote {len(relationship_edges)} {relationship_type} relationships.")

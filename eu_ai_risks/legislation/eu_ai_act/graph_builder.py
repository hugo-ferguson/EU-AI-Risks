"""
Build an in-memory graph from EU AI Act segments and write it to Neo4j.
"""

import re
from collections import defaultdict
from typing import cast, LiteralString

from eu_ai_risks.db import get_session
from eu_ai_risks.embeddings import embed_batch
from eu_ai_risks.embeddings.client import EMBEDDING_DIMENSIONS
from eu_ai_risks.models import Segment

# Article and annex cross-references define 'REFERENCES' edges. Citations
# appear in singular ('Article 6'), plural ('Articles 5 and 6'), and ranges
# ('Articles 8 to 15'). 
RE_ARTICLE_REF = re.compile(r'\bArticles?\s+(\d+(?:\s*(?:,|and|to)\s+\d+)*)')
RE_ANNEX_REF = re.compile(r'\bAnnex(?:es)?\s+([IVX]+(?:\s*(?:,|and)\s+[IVX]+)*)')
RE_ROMAN = re.compile(r'^[IVX]+$')


def expand_article_refs(number_list: str) -> set[int]:
	"""
	Expand a matched run of article numbers into the set it names.

	:param number_list: the text captured after 'Article(s)', e.g. '8 to 15'.
	:return: the set of article numbers referred to.
	"""
	numbers = set()

	# Split the run into its listed items, then expand any 'N to M' range.
	for item in re.split(r'\s*(?:,|and)\s+', number_list):
		range_match = re.match(r'(\d+)\s+to\s+(\d+)', item)
		if range_match:
			start, end = int(range_match.group(1)), int(range_match.group(2))
			numbers.update(range(start, end + 1))
		elif item.strip().isdigit():
			numbers.add(int(item.strip()))

	return numbers


def find_references(
		text: str, source_id: str, all_nodes: dict
) -> list[tuple[str, str]]:
	"""
	Find the articles and annexes that a block of text references.

	:param text: the text to scan for cross-references.
	:param source_id: the id of the referencing node, excluded from the result.
	:param all_nodes: the built nodes, used to drop references to unknown ids.
	:return: a list of (target id, 'REFERENCES') tuples.
	"""
	target_ids = set()

	for match in RE_ARTICLE_REF.finditer(text):
		for number in expand_article_refs(match.group(1)):
			target_ids.add(f"art:{number}")

	# Annex numbers are Roman, so list expansion is enough without ranges.
	for match in RE_ANNEX_REF.finditer(text):
		for roman in re.split(r'\s*(?:,|and)\s+', match.group(1)):
			if RE_ROMAN.match(roman.strip()):
				target_ids.add(f"annex:{roman.strip()}")

	return [
		(target_id, "REFERENCES")
		for target_id in target_ids
		if target_id != source_id and target_id in all_nodes
	]

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
		"embedding_text": None,
	},
	"section": {
		"label": "Section",
		"props": lambda segment: {"num": segment.num, "title": segment.title},
		"parent_rel": "CONTAINS",
		"parent_id": lambda segment: segment.parent_id,
		"cross_refs": None,
		"embedding_text": None,
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
		"cross_refs": lambda segment, all_nodes: find_references(
			" ".join(segment.body), segment.id, all_nodes
		),
		"embedding_text": lambda props, parent_props: (
			f"Article {props.get('num', '')}: {props.get('title', '')}. "
			f"{props.get('text', '')}"
		),
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
		"embedding_text": lambda props, parent_props: (
			f"Article {parent_props.get('num', '')}: {parent_props.get('title', '')}, "
			f"Paragraph {props.get('num', '')}. {props.get('text', '')}"
			if parent_props else
			f"Paragraph {props.get('num', '')}. {props.get('text', '')}"
		),
	},
	"annex": {
		"label": "Annex",
		"props": lambda segment: {
			"num": segment.num,
			"title": segment.title,
			"text": " ".join(segment.body),
		},
		"parent_rel": None,
		"parent_id": None,
		"cross_refs": lambda segment, all_nodes: find_references(
			" ".join(segment.body), segment.id, all_nodes
		),
		"embedding_text": lambda props, parent_props: (
			f"Annex {props.get('num', '')}: {props.get('title', '')}. "
			f"{props.get('text', '')}"
		),
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

		# Add the 'references' relationship.
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


def generate_and_write_embeddings(graph_nodes: dict) -> None:
	"""
	Generate embeddings for Article and Paragraph nodes and write them to
	Neo4j, then create vector indexes.

	:param graph_nodes: the nodes dict from build_in_memory_graph.
	"""

	# Build (node_id, label, text) tuples for nodes that should be embedded.
	to_embed = []

	for node_id, node_props in graph_nodes.items():
		node_type = node_props["type"]
		type_config = SEGMENT_TYPES[node_type]

		# Skip node types that don't have embedding text defined.
		if type_config["embedding_text"] is None:
			continue

		# Look up parent properties for child nodes.
		parent_props = None
		if type_config["parent_id"]:
			parent_id = ":".join(node_id.split(":")[:2])
			parent_props = graph_nodes.get(parent_id)

		text = type_config["embedding_text"](node_props, parent_props)
		label = type_config["label"]
		to_embed.append((node_id, label, text))

	if not to_embed:
		return

	# Generate embeddings in a single batch.
	texts = [text for _, _, text in to_embed]
	print(f"  Generating embeddings for {len(texts)} nodes ...")
	embeddings = embed_batch(texts)

	# Write embeddings to Neo4j.
	with get_session() as session:
		# Group by label for batch writes.
		by_label = defaultdict(list)
		for (node_id, label, _), embedding in zip(to_embed, embeddings):
			by_label[label].append({"id": node_id, "embedding": embedding})

		for label, rows in by_label.items():
			session.run(
				cast(LiteralString, f"""
					UNWIND $rows AS row
					MATCH (n:{label} {{id: row.id}})
					SET n.embedding = row.embedding
					"""),
				rows=rows,
			)
			print(f"  Wrote embeddings for {len(rows)} {label} nodes.")

		# Create vector indexes.
		for label in by_label:
			session.run(
				cast(LiteralString, f"""
					CREATE VECTOR INDEX {label.lower()}_embedding IF NOT EXISTS
					FOR (n:{label}) ON (n.embedding)
					OPTIONS {{indexConfig: {{
						`vector.dimensions`: {EMBEDDING_DIMENSIONS},
						`vector.similarity_function`: 'cosine'
					}}}}
					"""),
			)
			print(f"  Created vector index for {label}.")

"""
Build an in-memory graph from EU AI Act segments and write it to Neo4j.
"""

import re
from collections import defaultdict
from typing import cast, LiteralString

from eu_ai_risks.db import get_session
from eu_ai_risks.legislation.eu_ai_act.models import Segment

# Citations appear as singular, plural, and ranges (e.g. 'Articles 8 to 15')
RE_ARTICLE_REF = re.compile(r'\bArticles?\s+(\d+(?:\s*(?:,|and|to)\s+\d+)*)')
RE_ANNEX_REF = re.compile(
    r'\bAnnex(?:es)?\s+([IVX]+(?:\s*(?:,|and)\s+[IVX]+)*)')
RE_ROMAN = re.compile(r'^[IVX]+$')

# Precise references, e.g. 'Article 9(2)', 'points (f) and (g) of Article
# 10(2)', 'point 1 (a), of Annex III', 'paragraph 3', 'point (f)'
RE_ARTICLE_PARAGRAPH_REF = re.compile(r'\bArticle\s+(\d+)\s*\((\d+)\)')
RE_POINTS_OF_ARTICLE_REF = re.compile(
    r'\bpoints?\s+\(([a-z])\)(?:\s*(?:,|and|or)\s*\(([a-z])\))*\s+of\s+Article\s+(\d+)\s*\((\d+)\)')
# 'point 1(a) of Annex III', and lists such as 'points 1, 6 and 7 of Annex III'
RE_ANNEX_POINT_REF = re.compile(
    r'\bpoints?\s+(\d+(?:\s*\([a-z]\))?(?:\s*(?:,|and|or)\s*\d+(?:\s*\([a-z]\))?)*)'
    r'\s*,?\s*of\s+Annex\s+([IVX]+)')
RE_ANNEX_POINT_ITEM = re.compile(r'(\d+)\s*(?:\(([a-z])\))?')
RE_SAME_ARTICLE_PARAGRAPH_REF = re.compile(
    r'\bparagraph\s+(\d+)\b(?!\s+of\s+(?:Article|Regulation|Directive))')
RE_SAME_PARAGRAPH_POINT_REF = re.compile(r'\bpoint\s+\(([a-z])\)(?!\s+of\b)')
# A point of a named paragraph: 'Article 51(1), point (a)', 'paragraph 1,
# first subparagraph, point (h)', 'point (a) of paragraph 1'
RE_PROVISION_POINT_REF = re.compile(
    r'\b(?:Article\s+(\d+)\s*\((\d+)\)|paragraph\s+(\d+))\s*,\s*'
    r'(?:(?:first|second|third|fourth|fifth|sixth)\s+subparagraph\s*,\s*)?'
    r'points?\s+(\([a-z]\)(?:\s*(?:,|and|or)\s*\([a-z]\))*)')
RE_POINTS_OF_PARAGRAPH_REF = re.compile(
    r'\bpoints?\s+(\([a-z]\)(?:\s*(?:,|and|or)\s*\([a-z]\))*)\s+of\s+paragraph\s+(\d+)\b')
RE_POINT_LETTER = re.compile(r'\(([a-z])\)')

# What follows a citation of another act, e.g. 'Article 9(1) of Regulation
# (EU) 2016/679', 'Article 2(1), point (c), of Regulation ...', 'Article 16
# TFEU'; those article numbers are not this Act's
RE_OTHER_ACT = re.compile(
    r'^\s*(?:\(\d+\)\s*)?'
    r'(?:,?\s*(?:first|second|third|fourth|fifth|sixth)\s+subparagraph)?'
    r'(?:,?\s*points?\s+\([a-z0-9]+\)(?:\s*(?:,|and|or)\s*\([a-z0-9]+\))*)?'
    r'\s*,?\s*(?:(?:of|to)\s+(?:Regulation|Directive|Decision|Council|Commission|'
    r'the Treaty|the Charter|that Regulation|that Directive|that Decision)\b|(?:TFEU|TEU)\b)')


def cites_other_act(text: str, end: int) -> bool:
    """
    Check whether the citation ending at end names another act's provision.

    :param text: the text containing the citation.
    :param end: the index just after the cited article or annex.
    :return: whether the citation is of another act, not this Regulation.
    """
    return bool(RE_OTHER_ACT.match(text[end:end + 160]))


def expand_article_refs(number_list: str) -> set[int]:
    """
    Expand a matched run of article numbers into the set it names.

    :param number_list: the text captured after 'Article(s)', e.g. '8 to 15'.
    :return: the set of article numbers referred to.
    """
    numbers = set()

    # Split into items, then expand any 'N to M' range
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
        if cites_other_act(text, match.end()):
            continue
        for number in expand_article_refs(match.group(1)):
            target_ids.add(f"art:{number}")

    # Annex numbers are Roman numerals, so no range expansion needed
    for match in RE_ANNEX_REF.finditer(text):
        if cites_other_act(text, match.end()):
            continue
        for roman in re.split(r'\s*(?:,|and)\s+', match.group(1)):
            if RE_ROMAN.match(roman.strip()):
                target_ids.add(f"annex:{roman.strip()}")

    return [
        (target_id, "REFERENCES")
        for target_id in target_ids
        if target_id != source_id and target_id in all_nodes
    ]


def find_provision_references(
    text: str, source_id: str, all_nodes: dict
) -> list[tuple[str, str]]:
    """
    Find the most precise provisions a paragraph or point references.

    Paragraph- and point-level references (e.g. 'Article 9(2)', 'point 1(a)
    of Annex III', 'paragraph 3') point at those nodes; a reference that only
    names an article or annex falls back to that article or annex.

    :param text: the paragraph or point text.
    :param source_id: the referencing node id, e.g. 'art:10:p2' or 'art:10:p2:g'.
    :param all_nodes: the built nodes, used to drop references to unknown ids.
    :return: a list of (target id, 'REFERENCES') tuples.
    """
    parts = source_id.split(":")
    article_id = ":".join(parts[:2])
    paragraph_id = ":".join(parts[:3])
    target_ids = set()

    for match in RE_POINTS_OF_ARTICLE_REF.finditer(text):
        if cites_other_act(text, match.end()):
            continue
        article_number, paragraph_number = match.group(3), match.group(4)
        letters = RE_POINT_LETTER.findall(match.group(0).split(" of ")[0])
        for letter in letters:
            target_ids.add(f"art:{article_number}:p{paragraph_number}:{letter}")

    for match in RE_ARTICLE_PARAGRAPH_REF.finditer(text):
        if not cites_other_act(text, match.end()):
            target_ids.add(f"art:{match.group(1)}:p{match.group(2)}")

    for match in RE_ANNEX_POINT_REF.finditer(text):
        if cites_other_act(text, match.end()):
            continue
        roman = match.group(2)
        for number, letter in RE_ANNEX_POINT_ITEM.findall(match.group(1)):
            target_ids.add(f"annex:{roman}:{number}" + (f":{letter}" if letter else ""))

    # Points of a named paragraph; their spans are excluded from the
    # same-paragraph point lookup below, which would otherwise read
    # 'paragraph 2, point (d)' as point (d) of the citing paragraph
    named_point_spans = []
    for match in RE_PROVISION_POINT_REF.finditer(text):
        if cites_other_act(text, match.end()):
            continue
        if match.group(1):
            cited_paragraph = f"art:{match.group(1)}:p{match.group(2)}"
        elif source_id.startswith("art:"):
            cited_paragraph = f"{article_id}:p{match.group(3)}"
        else:
            continue
        named_point_spans.append(match.span())
        for letter in RE_POINT_LETTER.findall(match.group(4)):
            target_ids.add(f"{cited_paragraph}:{letter}")

    if source_id.startswith("art:"):
        for match in RE_POINTS_OF_PARAGRAPH_REF.finditer(text):
            named_point_spans.append(match.span())
            for letter in RE_POINT_LETTER.findall(match.group(1)):
                target_ids.add(f"{article_id}:p{match.group(2)}:{letter}")
        for match in RE_SAME_ARTICLE_PARAGRAPH_REF.finditer(text):
            target_ids.add(f"{article_id}:p{match.group(1)}")
        for match in RE_SAME_PARAGRAPH_POINT_REF.finditer(text):
            if not any(start <= match.start() < end for start, end in named_point_spans):
                target_ids.add(f"{paragraph_id}:{match.group(1)}")

    # A paragraph's text includes its own points, so ignore references
    # within the same branch (to itself, its ancestors or its own points)
    precise = {
        target_id for target_id in target_ids
        if target_id in all_nodes and target_id != source_id
        and not source_id.startswith(f"{target_id}:")
        and not target_id.startswith(f"{source_id}:")
    }

    # Keep article- and annex-level references only where nothing more
    # precise was found for that article or annex
    general = {
        target_id for target_id, _ in find_references(text, article_id, all_nodes)
        if not any(found.startswith(f"{target_id}:") for found in precise)
    }

    return [(target_id, "REFERENCES") for target_id in precise | general]


# Segment type configs drive graph construction, embedding, and cross-referencing
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
        "cross_refs": lambda segment, all_nodes: find_provision_references(
            " ".join(segment.body), segment.id, all_nodes
        ),
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
    # Lettered points of paragraphs (art:10:p2:f) and numbered/lettered
    # points of annexes (annex:III:4, annex:III:4:a), for precise citations
    "point": {
        "label": "Point",
        "props": lambda segment: {
            "num": segment.num,
            "label": segment.title,
            "text": " ".join(segment.body),
        },
        "parent_rel": "HAS_POINT",
        "parent_id": lambda segment: segment.parent_id,
        "cross_refs": lambda segment, all_nodes: find_provision_references(
            " ".join(segment.body), segment.id, all_nodes
        ),
        # Long paragraphs such as Art. 5(1) blur their points together, so
        # points are embedded too and ranked on their own
        "embedding_text": lambda props, parent_props: (
            f"{parent_props.get('title', '')}, point {props.get('label', '')}. "
            f"{props.get('text', '')}"
            if parent_props else
            f"Point {props.get('label', '')}. {props.get('text', '')}"
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

    for segment in segments:
        type_config = SEGMENT_TYPES[segment.type]
        add_node(segment.id, segment.type, **type_config["props"](segment))

    for segment in segments:
        type_config = SEGMENT_TYPES[segment.type]

        if type_config["parent_id"]:
            parent_id = type_config["parent_id"](segment)
            if parent_id and parent_id in nodes:
                add_edge(parent_id, type_config["parent_rel"], segment.id)

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

        nodes_by_type = defaultdict(list)
        for node_id, node_properties in graph_nodes.items():
            label = SEGMENT_TYPES[node_properties["type"]]["label"]
            node_data = {key: value for key,
                         value in node_properties.items() if key != "type"}
            node_data["id"] = node_id
            nodes_by_type[label].append(node_data)

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

        # Drop Act nodes the parser no longer produces (e.g. after a parsing
        # fix), with their enrichment; the rest keep their enrichment
        for label in {type_config["label"] for type_config in SEGMENT_TYPES.values()}:
            removed = session.run(
                cast(LiteralString, f"""
                MATCH (n:{label}) WHERE NOT n.id IN $ids
                DETACH DELETE n
                RETURN count(n) AS removed
                """),
                ids=[node["id"] for node in nodes_by_type.get(label, [])],
            ).single()["removed"]
            if removed:
                print(f"  Removed {removed} stale {label} nodes.")

        edges_by_relationship = defaultdict(list)
        for edge in graph_edges:
            edges_by_relationship[edge["rel"]].append(edge)

        # Only this builder writes these relationships, and MERGE never removes
        # one, so replace them: otherwise a reference the parser no longer
        # finds (e.g. one to another act's article) would outlive a rebuild
        labels = " OR ".join(
            f"a:{type_config['label']}" for type_config in SEGMENT_TYPES.values())
        removed = session.run(
            cast(LiteralString, f"""
            MATCH (a)-[r:{'|'.join(edges_by_relationship)}]->()
            WHERE {labels}
            DELETE r
            RETURN count(r) AS removed
            """),
        ).single()["removed"]
        print(f"  Replacing {removed} existing structural and reference relationships.")

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

            print(
                f"  Wrote {len(relationship_edges)} {relationship_type} relationships.")


def generate_and_write_embeddings(graph_nodes: dict) -> None:
    """
    Generate embeddings for Article and Paragraph nodes and write them to
    Neo4j, then create vector indexes.

    :param graph_nodes: the nodes dict from build_in_memory_graph.
    """
    from eu_ai_risks.embeddings import embed_batch
    from eu_ai_risks.embeddings.client import EMBEDDING_DIMENSIONS

    to_embed = []

    for node_id, node_props in graph_nodes.items():
        node_type = node_props["type"]
        type_config = SEGMENT_TYPES[node_type]

        if type_config["embedding_text"] is None:
            continue

        # Paragraphs need their parent article's title for context
        parent_props = None
        if type_config["parent_id"]:
            parent_id = ":".join(node_id.split(":")[:2])
            parent_props = graph_nodes.get(parent_id)

        text = type_config["embedding_text"](node_props, parent_props)
        label = type_config["label"]
        to_embed.append((node_id, label, text))

    if not to_embed:
        return

    texts = [text for _, _, text in to_embed]
    print(f"  Generating embeddings for {len(texts)} nodes ...")
    embeddings = embed_batch(texts)

    with get_session() as session:
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

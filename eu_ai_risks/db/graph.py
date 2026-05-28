"""
Generic graph query operations on the Neo4j database.
"""

import re
from pathlib import Path

import PyPDF2

from eu_ai_risks.db.session import get_session
from eu_ai_risks.embeddings.client import generate_requirements_embeddings as generate_requirement_embeddings

DEFAULT_REQUIREMENTS_PDF = "the_story_web_requirements_document.pdf"

REQUIREMENTS_GRAPH_QUERY = """
MERGE (r:Requirement {title: $title})
SET r.description = $desc, r.processing = $proc, r.input = $input

WITH r
UNWIND (
	CASE
	WHEN toLower($desc) CONTAINS 'super-admin' THEN ['User', 'Admin', 'Super-Admin']
	WHEN toLower($desc) CONTAINS 'admin' THEN ['User', 'Admin']
	ELSE ['User']
	END
) AS role
MERGE (a:Audience {name: role})
MERGE (r)-[:TARGETS]->(a)

WITH r
UNWIND split(toLower($title), ' ') AS word
WITH r, word
WHERE word CONTAINS 'ai'
MERGE (k:Keyword {name: word})
MERGE (r)-[:HAS_KEYWORD]->(k)
"""


def articles_in_chapter(chapter_id: str) -> list[tuple[str, str]]:
	"""
	List the articles of a chapter.
	Uses the 'CONTAINS' edge.

	:param chapter_id: the id of the chapter.
	:return: a list of tuples containing article ids and article titles.
	"""
	with get_session() as session:
		query_result = session.run(
			"""
			MATCH (c:Chapter {id: $chapter_id})-[:CONTAINS]->(a:Article)
			RETURN a.id AS id, a.title AS title
			ORDER BY a.num
			""",
			chapter_id=chapter_id,
		)

		return [(row["id"], row["title"]) for row in query_result]


def references_from(article_id: str) -> list[tuple[str, str]]:
	"""
	List the articles that an article references.

	:param article_id: the id of the article.
	:return: a list of tuples containing article ids and article titles.
	"""

	with get_session() as session:
		query_result = session.run(
			"""
			MATCH (a:Article {id: $article_id})-[:REFERENCES]->(b:Article)
			RETURN b.id AS id, b.title AS title
			ORDER BY b.num
			""",
			article_id=article_id,
		)

		return [(row["id"], row["title"]) for row in query_result]


def referenced_by(article_id: str) -> list[tuple[str, str]]:
	"""
	List the articles that reference an article.

	:param article_id: the id of the article.
	:return: a list of tuples containing article ids and article titles.
	"""

	with get_session() as session:
		query_result = session.run(
			"""
			MATCH (a:Article)-[:REFERENCES]->(b:Article {id: $article_id})
			RETURN a.id AS id, a.title AS title
			ORDER BY a.num
			""",
			article_id=article_id,
		)

		return [(row["id"], row["title"]) for row in query_result]


def shortest_path(source_id: str, target_id: str) -> list[str]:
	"""
	Find the shortest path between two nodes.

	:param source_id: the source node (chapter, article, paragraph) id.
	:param target_id: the target node (chapter, article, paragraph) id.
	:return: the path id that takes you from source to target.
	"""
	with get_session() as session:
		query_result = session.run(
			"""
			MATCH (a:Article {id: $source_id}), (b:Article {id: $target_id}),
				  p = shortestPath((a)-[:REFERENCES*]->(b))
			RETURN [n IN nodes(p) | n.id] AS path
			""",
			source_id=source_id,
			target_id=target_id,
		)

		path_record = query_result.single()

		return path_record["path"] if path_record else []


def vector_search_articles(
		query_embedding: list[float], top_k: int = 5
) -> list[tuple[str, str, float]]:
	"""
	Find the most similar articles by vector similarity.

	:param query_embedding: the query embedding vector.
	:param top_k: the number of results to return.
	:return: a list of (article_id, title, score) tuples.
	"""
	with get_session() as session:
		query_result = session.run(
			"""
			CALL db.index.vector.queryNodes('article_embedding', $top_k, $embedding)
			YIELD node, score
			RETURN node.id AS id, node.title AS title, score
			""",
			top_k=top_k,
			embedding=query_embedding,
		)

		return [(row["id"], row["title"], row["score"]) for row in query_result]


def vector_search_paragraphs(
		query_embedding: list[float], top_k: int = 5
) -> list[tuple[str, int, float]]:
	"""
	Find the most similar paragraphs by vector similarity.

	:param query_embedding: the query embedding vector.
	:param top_k: the number of results to return.
	:return: a list of (paragraph_id, num, score) tuples.
	"""
	with get_session() as session:
		query_result = session.run(
			"""
			CALL db.index.vector.queryNodes('paragraph_embedding', $top_k, $embedding)
			YIELD node, score
			RETURN node.id AS id, node.num AS num, score
			""",
			top_k=top_k,
			embedding=query_embedding,
		)

		return [(row["id"], row["num"], row["score"]) for row in query_result]


def extract_text_from_pdf(file_path: str | Path) -> str:
	"""Extract the full text from a PDF file."""
	text = ""
	with open(file_path, "rb") as file:
		reader = PyPDF2.PdfReader(file)
		for page in reader.pages:
			text += page.extract_text()

	return text


def parse_requirements(text: str) -> list[dict[str, str]]:
	"""Parse requirement blocks from the requirements PDF text."""
	blocks = re.split(r"(?=Requirement(?:\s+\d+)?)", text)
	requirements = []

	for block in blocks:
		if "Title:" not in block:
			continue

		title = re.search(r"Title:\s*(.*)", block, re.IGNORECASE)
		description = re.search(r"Description:\s*(.*)", block, re.IGNORECASE)
		input_value = re.search(r"Input:\s*(.*)", block, re.IGNORECASE)
		processing = re.search(r"Processing:\s*(.*)", block, re.IGNORECASE)

		if not all([title, description, input_value, processing]):
			continue

		requirements.append(
			{
				"title": title.group(1).strip(),
				"description": description.group(1).strip(),
				"input": input_value.group(1).strip(),
				"processing": processing.group(1).strip(),
			}
		)

	return requirements


def sanitize_affected_by_rows(records: list[dict[str, str | None]]) -> list[dict[str, str]]:
	"""Filter and deduplicate requirement-to-paragraph rows."""
	rows = []
	seen = set()

	for record in records:
		title = str(record.get("title") or "").strip()
		paragraph_id = str(record.get("paragraph_id") or "").strip()
		if not title or not paragraph_id:
			continue

		key = (title, paragraph_id)
		if key in seen:
			continue

		seen.add(key)
		rows.append({"title": title, "paragraph_id": paragraph_id})

	return rows


def create_requirement_graph(tx, req: dict[str, str]) -> None:
	"""Create a requirement node and its related audience/keyword nodes."""
	tx.run(
		REQUIREMENTS_GRAPH_QUERY,
		title=req["title"],
		desc=req["description"],
		proc=req["processing"],
		input=req["input"],
	)


def build_requirements_graph(file_path: str | Path = DEFAULT_REQUIREMENTS_PDF) -> int:
	"""Parse the requirements PDF and write the requirements graph to Neo4j."""
	raw_text = extract_text_from_pdf(file_path)
	parsed_requirements = parse_requirements(raw_text)

	with get_session() as session:
		for requirement in parsed_requirements:
			session.execute_write(create_requirement_graph, requirement)

	return len(parsed_requirements)


def create_affected_by_relationships(top_k: int = 10) -> int:
	"""Create affected by relationships from Requirement nodes to similar Paragraph nodes."""
	with get_session() as session:
		result = session.run(
			"""
			MATCH (r:Requirement)
			WHERE r.embedding IS NOT NULL
			WITH r
			MATCH (node)
			SEARCH node IN (
				VECTOR INDEX paragraph_embedding
				FOR r.embedding
				LIMIT $top_k
			) SCORE AS score
			WHERE score > 0.799
			RETURN r.title AS title, node.id AS paragraph_id, score
			""",
			top_k=top_k,
		)

		rows = sanitize_affected_by_rows([
			{"title": record.get("title"), "paragraph_id": record.get("paragraph_id")}
			for record in result
		])

		if not rows:
			return 0

		session.run(
			"""
			UNWIND $rows AS row
			MATCH (r:Requirement {title: row.title})
			MATCH (p:Paragraph {id: row.paragraph_id})
			MERGE (r)-[:`affected by`]->(p)
			""",
			rows=rows,
		)

		return len(rows)


def generate_requirements_embeddings() -> int:
	"""Generate embeddings for Requirement nodes and write them to Neo4j."""
	return generate_requirement_embeddings()

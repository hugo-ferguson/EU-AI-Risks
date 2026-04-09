"""
Various queries that can be performed on the EU AI Act graph.
"""

from eu_ai_risks.db import get_session


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
	Uses the 'CONTAINS' edge.

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
	Uses the 'CONTAINS' edge.

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


if __name__ == "__main__":
	"""
	Tests.
	"""

	print("=== Articles in Chapter III (first 8) ===")
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

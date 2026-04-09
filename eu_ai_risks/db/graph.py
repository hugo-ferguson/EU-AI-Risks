"""
Generic graph query operations on the Neo4j database.
"""

from eu_ai_risks.db.session import get_session


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

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
        # Articles can be in the chapter directly or via a section, so allow
        # one or two CONTAINS hops.
        query_result = session.run(
            """
			MATCH (c:Chapter {id: $chapter_id})-[:CONTAINS*1..2]->(a:Article)
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


def paragraph_details(paragraph_ids: list[str]) -> dict[str, dict]:
    """
    Load paragraph text and parent article details for a set of paragraph IDs.

    :param paragraph_ids: paragraph node ids.
    :return: dictionary keyed by paragraph id.
    """
    if not paragraph_ids:
        return {}

    with get_session() as session:
        query_result = session.run(
            """
			MATCH (a:Article)-[:HAS_PARAGRAPH]->(p:Paragraph)
			WHERE p.id IN $paragraph_ids
			RETURN
				p.id AS paragraph_id,
				p.num AS paragraph_num,
				p.text AS paragraph_text,
				a.id AS article_id,
				a.num AS article_num,
				a.title AS article_title
			""",
            paragraph_ids=paragraph_ids,
        )

        return {
            row["paragraph_id"]: {
                "paragraph_id": row["paragraph_id"],
                "paragraph_num": row["paragraph_num"],
                "paragraph_text": row["paragraph_text"],
                "article_id": row["article_id"],
                "article_num": row["article_num"],
                "article_title": row["article_title"],
            }
            for row in query_result
        }


def list_categories() -> list[dict]:
    """
    List all 14 RequirementCategory nodes with their anchor article IDs.

    :return: list of dicts with keys: key, name, article_ids.
    """
    with get_session() as session:
        query_result = session.run(
            """
			MATCH (a:Article)-[:IMPOSES]->(rc:RequirementCategory)
			RETURN rc.key AS key, rc.name AS name,
			       collect(a.id) AS article_ids
			ORDER BY rc.name
			"""
        )

        return [
            {
                "key": row["key"],
                "name": row["name"],
                "article_ids": row["article_ids"],
            }
            for row in query_result
        ]


def get_category_articles(
    category_key: str,
    obligation_types: list[str] | None = None,
) -> dict:
    """
    Return the anchor article(s) and their paragraphs for a requirement
    category.

    :param category_key: e.g. "risk_management", "human_oversight".
    :param obligation_types: filter paragraphs to these types
           (default: ["requirement"]).
    :return: dict with keys: category_key, category_name, articles.
    """
    if obligation_types is None:
        obligation_types = ["requirement"]

    with get_session() as session:
        query_result = session.run(
            """
			MATCH (a:Article)-[:IMPOSES]->(rc:RequirementCategory {key: $key})
			OPTIONAL MATCH (a)-[:HAS_PARAGRAPH]->(p:Paragraph)
			WHERE $filter_types = false
			   OR p.obligation_type IN $obligation_types
			RETURN rc.name AS category_name,
			       a.id AS article_id, a.num AS article_num,
			       a.title AS article_title, a.text AS article_text,
			       collect({
			           id: p.id, num: p.num, text: p.text,
			           obligation_type: p.obligation_type
			       }) AS paragraphs
			ORDER BY a.num
			""",
            key=category_key,
            obligation_types=obligation_types,
            filter_types=len(obligation_types) > 0,
        )

        articles = []
        category_name = category_key
        for row in query_result:
            category_name = row["category_name"]
            paragraphs = [para for para in row["paragraphs"] if para["id"] is not None]
            paragraphs.sort(key=lambda para: para["num"] or 0)
            articles.append({
                "article_id": row["article_id"],
                "article_num": row["article_num"],
                "article_title": row["article_title"],
                "article_text": row["article_text"],
                "paragraphs": paragraphs,
            })

        return {
            "category_key": category_key,
            "category_name": category_name,
            "articles": articles,
        }


def get_article(article_id: str) -> dict | None:
    """
    Return full article details: text, paragraphs, chapter context, and
    dimension tags.

    :param article_id: e.g. "art:9".
    :return: dict with article details, or None if not found.
    """
    with get_session() as session:
        article_result = session.run(
            """
			MATCH (a:Article {id: $article_id})
			OPTIONAL MATCH (c)-[:CONTAINS*1..2]->(a)
			WHERE c:Chapter
			OPTIONAL MATCH (a)-[:HAS_PARAGRAPH]->(p:Paragraph)
			RETURN a.id AS id, a.num AS num, a.title AS title,
			       a.text AS text,
			       c.id AS chapter_id, c.title AS chapter_title,
			       collect({
			           id: p.id, num: p.num, text: p.text,
			           obligation_type: p.obligation_type
			       }) AS paragraphs
			""",
            article_id=article_id,
        )

        record = article_result.single()
        if not record or record["id"] is None:
            return None

        paragraphs = [para for para in record["paragraphs"] if para["id"] is not None]
        paragraphs.sort(key=lambda para: para["num"] or 0)

        dim_result = session.run(
            """
			MATCH (a:Article {id: $article_id})
			OPTIONAL MATCH (a)-[:IMPOSES]->(rc:RequirementCategory)
			OPTIONAL MATCH (a)-[:ADDRESSES]->(rp:ResponsibleParty)
			OPTIONAL MATCH (a)-[:HAS_RISK]->(rk:RiskCategory)
			OPTIONAL MATCH (a)-[:CONCERNS]->(dc:DataCategory)
			RETURN collect(DISTINCT rc.key) AS requirement_categories,
			       collect(DISTINCT rp.key) AS responsible_parties,
			       collect(DISTINCT rk.key) AS risk_categories,
			       collect(DISTINCT dc.key) AS data_categories
			""",
            article_id=article_id,
        )

        dims = dim_result.single()
        dimensions = {}
        if dims:
            dimensions = {
                "requirement_categories": dims["requirement_categories"],
                "responsible_parties": dims["responsible_parties"],
                "risk_categories": dims["risk_categories"],
                "data_categories": dims["data_categories"],
            }

        return {
            "id": record["id"],
            "num": record["num"],
            "title": record["title"],
            "text": record["text"],
            "chapter_id": record["chapter_id"],
            "chapter_title": record["chapter_title"],
            "paragraphs": paragraphs,
            "dimensions": dimensions,
        }


def find_paragraphs(
    query_embedding: list[float],
    top_k: int = 8,
) -> list[dict]:
    """
    Vector search paragraphs and return results with full text, article
    context, and obligation type.

    :param query_embedding: the query embedding vector.
    :param top_k: number of results to return.
    :return: list of paragraph dicts with article context.
    """
    with get_session() as session:
        query_result = session.run(
            """
			CALL db.index.vector.queryNodes(
			    'paragraph_embedding', $top_k, $embedding
			)
			YIELD node, score
			MATCH (a:Article)-[:HAS_PARAGRAPH]->(node)
			OPTIONAL MATCH (c:Chapter)-[:CONTAINS*1..2]->(a)
			RETURN node.id AS paragraph_id,
			       node.num AS paragraph_num,
			       node.text AS paragraph_text,
			       node.obligation_type AS obligation_type,
			       a.id AS article_id, a.num AS article_num,
			       a.title AS article_title,
			       c.id AS chapter_id,
			       score
			ORDER BY score DESC
			""",
            top_k=top_k,
            embedding=query_embedding,
        )

        return [
            {
                "paragraph_id": row["paragraph_id"],
                "paragraph_num": row["paragraph_num"],
                "paragraph_text": row["paragraph_text"],
                "obligation_type": row["obligation_type"],
                "article_id": row["article_id"],
                "article_num": row["article_num"],
                "article_title": row["article_title"],
                "chapter_id": row["chapter_id"],
                "score": round(row["score"], 4),
            }
            for row in query_result
        ]


def text_search(
    keyword: str,
    obligation_types: list[str] | None = None,
    limit: int = 10,
) -> list[dict]:
    """
    Search paragraph text by keyword (case-insensitive substring match).

    :param keyword: the keyword or phrase to search for.
    :param obligation_types: optional filter for paragraph obligation types.
    :param limit: max results.
    :return: list of paragraph dicts with article context.
    """
    with get_session() as session:
        query_result = session.run(
            """
			MATCH (a:Article)-[:HAS_PARAGRAPH]->(p:Paragraph)
			WHERE toLower(p.text) CONTAINS toLower($keyword)
			  AND ($filter_types = false
			       OR p.obligation_type IN $obligation_types)
			RETURN p.id AS paragraph_id, p.num AS paragraph_num,
			       p.text AS paragraph_text,
			       p.obligation_type AS obligation_type,
			       a.id AS article_id, a.num AS article_num,
			       a.title AS article_title
			ORDER BY a.num, p.num
			LIMIT $limit
			""",
            keyword=keyword,
            obligation_types=obligation_types or [],
            filter_types=obligation_types is not None and len(
                obligation_types) > 0,
            limit=limit,
        )

        return [
            {
                "paragraph_id": row["paragraph_id"],
                "paragraph_num": row["paragraph_num"],
                "paragraph_text": row["paragraph_text"],
                "obligation_type": row["obligation_type"],
                "article_id": row["article_id"],
                "article_num": row["article_num"],
                "article_title": row["article_title"],
            }
            for row in query_result
        ]


def get_references(article_id: str) -> dict:
    """
    Return both outgoing and incoming references for an article.

    :param article_id: e.g. "art:9".
    :return: dict with references_to and referenced_by lists.
    """
    with get_session() as session:
        outgoing = session.run(
            """
			MATCH (a:Article {id: $article_id})-[:REFERENCES]->(b)
			RETURN b.id AS id, b.title AS title, labels(b)[0] AS type
			ORDER BY b.num
			""",
            article_id=article_id,
        )
        references_to = [
            {"id": row["id"], "title": row["title"], "type": row["type"]}
            for row in outgoing
        ]

        incoming = session.run(
            """
			MATCH (a)-[:REFERENCES]->(b:Article {id: $article_id})
			RETURN a.id AS id, a.title AS title, labels(a)[0] AS type
			ORDER BY a.num
			""",
            article_id=article_id,
        )
        referenced_by = [
            {"id": row["id"], "title": row["title"], "type": row["type"]}
            for row in incoming
        ]

        return {
            "article_id": article_id,
            "references_to": references_to,
            "referenced_by": referenced_by,
        }


def list_requirements() -> list[dict]:
    """
    List all Requirement nodes in the graph.

    :return: list of dicts with keys: id, text.
    """
    with get_session() as session:
        query_result = session.run(
            """
			MATCH (r:Requirement)
			RETURN r.id AS id, r.text AS text
			ORDER BY r.id
			"""
        )

        return [
            {"id": row["id"], "text": row["text"]}
            for row in query_result
        ]


def get_requirement(req_id: str) -> dict | None:
    """
    Return a requirement with its entity triples.

    :param req_id: the requirement ID, e.g. "REQ-001".
    :return: dict with requirement details and triples, or None.
    """
    with get_session() as session:
        query_result = session.run(
            """
			MATCH (r:Requirement {id: $req_id})
			OPTIONAL MATCH (r)-[:EXTRACTED_FROM]->(s:Entity)
			OPTIONAL MATCH (s)-[rel:RELATION]->(o:Entity)
			RETURN r.id AS id, r.text AS text,
			       collect({
			           subject: s.name,
			           predicate: rel.type,
			           object: o.name
			       }) AS triples
			""",
            req_id=req_id,
        )

        record = query_result.single()
        if not record or record["id"] is None:
            return None

        triples = [
            triple for triple in record["triples"]
            if triple["subject"] is not None
        ]

        return {
            "id": record["id"],
            "text": record["text"],
            "triples": triples,
        }


def get_related_requirements(req_id: str) -> list[dict]:
    """
    Find requirements that share entities with the given requirement.

    :param req_id: the requirement ID, e.g. "REQ-001".
    :return: list of related requirements with shared entity names.
    """
    with get_session() as session:
        query_result = session.run(
            """
			MATCH (r:Requirement {id: $req_id})-[:EXTRACTED_FROM]->(s:Entity)
			OPTIONAL MATCH (s)-[:RELATION*0..1]-(e:Entity)
			MATCH (other:Requirement)-[:EXTRACTED_FROM]->(e)
			WHERE other.id <> $req_id
			RETURN DISTINCT other.id AS id, other.text AS text,
			       collect(DISTINCT e.name) AS shared_entities
			ORDER BY size(collect(DISTINCT e.name)) DESC
			""",
            req_id=req_id,
        )

        return [
            {
                "id": row["id"],
                "text": row["text"],
                "shared_entities": row["shared_entities"],
            }
            for row in query_result
        ]


def search_entities(
    query_embedding: list[float],
    top_k: int = 8,
) -> list[dict]:
    """
    Vector search over Entity nodes from the requirements graph.

    :param query_embedding: the query embedding vector.
    :param top_k: number of results to return.
    :return: list of entity dicts with linked requirements.
    """
    with get_session() as session:
        query_result = session.run(
            """
			CALL db.index.vector.queryNodes(
			    'entity_embedding', $top_k, $embedding
			)
			YIELD node, score
			OPTIONAL MATCH (r:Requirement)-[:EXTRACTED_FROM]->(node)
			RETURN node.name AS entity_name,
			       score,
			       collect({id: r.id, text: r.text}) AS requirements
			ORDER BY score DESC
			""",
            top_k=top_k,
            embedding=query_embedding,
        )

        return [
            {
                "entity_name": row["entity_name"],
                "score": round(row["score"], 4),
                "requirements": [
                    req for req in row["requirements"]
                    if req["id"] is not None
                ],
            }
            for row in query_result
        ]

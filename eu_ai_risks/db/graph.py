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


def get_article_index() -> list[dict]:
    """
    Return the Act's table of contents: every article with its chapter and
    section, in article order.

    :return: list of dicts with keys: chapter_id, chapter_title, section_title,
        article_id, article_title.
    """
    with get_session() as session:
        query_result = session.run(
            """
			MATCH (c:Chapter)-[:CONTAINS*1..2]->(a:Article)
			OPTIONAL MATCH (s:Section)-[:CONTAINS]->(a)
			RETURN c.id AS chapter_id, c.title AS chapter_title,
			       s.title AS section_title, a.id AS article_id,
			       a.title AS article_title
			ORDER BY toInteger(a.num)
			"""
        )
        return query_result.data()


def binding_paragraphs_for_articles(
    article_ids: list[str],
    query_embedding: list[float],
    per_article: int = 2,
) -> list[dict]:
    """
    Return each article's binding paragraphs (requirements and prohibitions)
    most similar to the query, in the order the articles were given.

    A paragraph scores as its own similarity or its best-matching point's,
    whichever is higher, because one embedding of a long list of points
    (e.g. Article 5(1)) matches none of them well.

    :param article_ids: article node ids, e.g. ["art:10", "art:13"].
    :param query_embedding: the query embedding vector.
    :param per_article: maximum paragraphs to keep per article.
    :return: paragraph dicts in the same shape as find_paragraphs, plus
        best_point_id (None when the paragraph text itself matched best).
    """
    if not article_ids:
        return []

    with get_session() as session:
        rows = session.run(
            """
			UNWIND $article_ids AS article_id
			MATCH (a:Article {id: article_id})-[:HAS_PARAGRAPH]->(p:Paragraph)
			WHERE p.obligation_type IN ['requirement', 'prohibition']
			      AND p.embedding IS NOT NULL
			OPTIONAL MATCH (p)-[:HAS_POINT]->(pt:Point)
			WHERE pt.embedding IS NOT NULL
			WITH a, p, vector.similarity.cosine(p.embedding, $embedding) AS paragraph_score,
			     pt, vector.similarity.cosine(pt.embedding, $embedding) AS point_score
			ORDER BY point_score DESC
			WITH a, p, paragraph_score,
			     collect(pt.id)[0] AS best_point_id, max(point_score) AS best_point_score
			RETURN p.id AS paragraph_id, p.num AS paragraph_num,
			       p.text AS paragraph_text, p.obligation_type AS obligation_type,
			       a.id AS article_id, a.num AS article_num,
			       a.title AS article_title,
			       CASE WHEN best_point_score > paragraph_score THEN best_point_id END AS best_point_id,
			       CASE WHEN best_point_score > paragraph_score
			            THEN best_point_score ELSE paragraph_score END AS score
			""",
            article_ids=article_ids,
            embedding=query_embedding,
        ).data()

    by_article: dict[str, list[dict]] = {}
    for row in sorted(rows, key=lambda row: row["score"], reverse=True):
        kept = by_article.setdefault(row["article_id"], [])
        if len(kept) < per_article:
            row["score"] = round(row["score"], 4)
            kept.append(row)

    return [paragraph for article_id in article_ids for paragraph in by_article.get(article_id, [])]


def provision_label(node_id: str) -> str:
    """
    Format a provision node id the way the Act cites it.

    :param node_id: e.g. "art:10:p2:f", "art:3:p4", "annex:III:4:a".
    :return: e.g. "Article 10(2)(f)", "Article 3(4)", "Annex III point 4(a)".
    """
    parts = node_id.split(":")
    if parts[0] == "art" and len(parts) >= 2:
        label = f"Article {parts[1]}"
        if len(parts) >= 3 and parts[2].startswith("p"):
            label += f"({parts[2][1:]})"
        if len(parts) >= 4:
            label += f"({parts[3]})"
        return label
    if parts[0] == "annex" and len(parts) >= 2:
        label = f"Annex {parts[1]}"
        if len(parts) >= 3:
            label += f" point {parts[2]}"
        if len(parts) >= 4:
            label += f"({parts[3]})"
        return label
    return node_id


def get_annex_iii_points() -> list[dict]:
    """
    Return the points of Annex III (the high-risk areas and their use cases).

    :return: list of dicts with keys: id, text, ordered by id.
    """
    with get_session() as session:
        return session.run(
            """
			MATCH (:Annex {id: 'annex:III'})-[:HAS_POINT*1..2]->(p:Point)
			RETURN p.id AS id, p.text AS text
			ORDER BY p.id
			"""
        ).data()


def get_concepts() -> list[dict]:
    """
    Return the Article 3 concepts with the paragraph that defines each.

    :return: list of dicts with keys: name, description, definition_id,
        definition_text, article_count (articles that use the concept).
    """
    with get_session() as session:
        return session.run(
            """
			MATCH (definition:Paragraph)-[:DEFINES]->(c:Concept)
			OPTIONAL MATCH (a:Article)-[:USES]->(c)
			RETURN c.name AS name, c.description AS description,
			       definition.id AS definition_id, definition.text AS definition_text,
			       count(DISTINCT a) AS article_count
			"""
        ).data()


def get_requirement_concepts(requirement_id: str) -> list[dict]:
    """
    Return the Act concepts a requirement's entities were aligned to.

    :param requirement_id: the requirement ID, e.g. "FR-1".
    :return: list of dicts with keys: entity, concept.
    """
    with get_session() as session:
        return session.run(
            """
			MATCH (:Requirement {id: $requirement_id})-[:EXTRACTED_FROM]->(e:Entity)
			      -[:INSTANCE_OF]->(c:Concept)
			RETURN DISTINCT e.name AS entity, c.name AS concept
			""",
            requirement_id=requirement_id,
        ).data()


def get_articles_using_concepts(concept_names: list[str]) -> dict[str, list[str]]:
    """
    Return the articles that use each concept.

    :param concept_names: concept names, e.g. ["training data"].
    :return: dict of concept name to article ids.
    """
    if not concept_names:
        return {}
    with get_session() as session:
        rows = session.run(
            """
			MATCH (a:Article)-[:USES]->(c:Concept)
			WHERE c.name IN $names
			RETURN c.name AS concept, collect(a.id) AS article_ids
			""",
            names=concept_names,
        ).data()
    return {row["concept"]: row["article_ids"] for row in rows}


def get_referenced_provisions(paragraph_ids: list[str]) -> list[dict]:
    """
    Follow the precise references made by paragraphs (or their points).

    :param paragraph_ids: paragraph node ids, e.g. ["art:13:p3"].
    :return: list of dicts with keys: source_id (the referencing paragraph or
        point), target_id, target_label (Paragraph, Point, Article or Annex),
        target_text, and for targets inside an article the containing
        paragraph's fields (paragraph_id, paragraph_num, paragraph_text,
        obligation_type, article_id, article_num, article_title).
    """
    if not paragraph_ids:
        return []
    with get_session() as session:
        return session.run(
            """
			UNWIND $paragraph_ids AS paragraph_id
			MATCH (:Paragraph {id: paragraph_id})-[:HAS_POINT*0..1]->(source)
			      -[:REFERENCES]->(target)
			OPTIONAL MATCH (point_parent:Paragraph)-[:HAS_POINT]->(target)
			WITH source, target,
			     CASE WHEN target:Paragraph THEN target ELSE point_parent END AS paragraph
			OPTIONAL MATCH (article:Article)-[:HAS_PARAGRAPH]->(paragraph)
			RETURN DISTINCT source.id AS source_id, target.id AS target_id,
			       labels(target)[0] AS target_label, target.text AS target_text,
			       paragraph.id AS paragraph_id, paragraph.num AS paragraph_num,
			       paragraph.text AS paragraph_text,
			       paragraph.obligation_type AS obligation_type,
			       article.id AS article_id, article.num AS article_num,
			       article.title AS article_title
			""",
            paragraph_ids=paragraph_ids,
        ).data()


def get_provisions(node_ids: list[str]) -> dict[str, dict]:
    """
    Look up paragraphs and points by id, with their article context.

    :param node_ids: paragraph or point ids, e.g. ["art:10:p2", "art:10:p2:f"].
    :return: dict of id to a dict with keys: id, label (Paragraph or Point),
        text, article_id, article_num, article_title, paragraph_num,
        point_label (None for paragraphs).
    """
    if not node_ids:
        return {}
    with get_session() as session:
        rows = session.run(
            """
			MATCH (n) WHERE n.id IN $ids AND (n:Paragraph OR n:Point)
			OPTIONAL MATCH (point_parent:Paragraph)-[:HAS_POINT]->(n)
			WITH n, CASE WHEN n:Paragraph THEN n ELSE point_parent END AS paragraph
			OPTIONAL MATCH (article:Article)-[:HAS_PARAGRAPH]->(paragraph)
			RETURN n.id AS id, labels(n)[0] AS label, n.text AS text,
			       article.id AS article_id, article.num AS article_num,
			       article.title AS article_title, paragraph.num AS paragraph_num,
			       CASE WHEN n:Point THEN n.label END AS point_label
			""",
            ids=node_ids,
        ).data()
    return {row["id"]: row for row in rows}


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
            paragraphs = [paragraph for paragraph in row["paragraphs"]
                          if paragraph["id"] is not None]
            paragraphs.sort(key=lambda paragraph: paragraph["num"] or 0)
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

        paragraphs = [paragraph for paragraph in record["paragraphs"]
                      if paragraph["id"] is not None]
        paragraphs.sort(key=lambda paragraph: paragraph["num"] or 0)

        dimension_result = session.run(
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

        dimension_record = dimension_result.single()
        dimensions = {}
        if dimension_record:
            dimensions = {
                "requirement_categories": dimension_record["requirement_categories"],
                "responsible_parties": dimension_record["responsible_parties"],
                "risk_categories": dimension_record["risk_categories"],
                "data_categories": dimension_record["data_categories"],
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


def get_requirement(requirement_id: str) -> dict | None:
    """
    Return a requirement with its entity triples.

    :param requirement_id: the requirement ID, e.g. "REQ-001".
    :return: dict with requirement details and triples, or None.
    """
    with get_session() as session:
        query_result = session.run(
            """
			MATCH (r:Requirement {id: $requirement_id})
			OPTIONAL MATCH (r)-[:EXTRACTED_FROM]->(s:Entity)
			OPTIONAL MATCH (s)-[rel:RELATION]->(o:Entity)
			RETURN r.id AS id, r.text AS text,
			       collect({
			           subject: s.name,
			           predicate: rel.type,
			           object: o.name
			       }) AS triples
			""",
            requirement_id=requirement_id,
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


ENTITY_SIMILARITY_THRESHOLD = 0.75


def get_related_requirements(requirement_id: str, limit: int = 5) -> list[dict]:
    """
    Find requirements that share entities with the given requirement.

    Entities match when they are the same node or when their EDC definitions
    are similar (cosine at or above ENTITY_SIMILARITY_THRESHOLD). Each match is
    weighted by that similarity and by rarity (log of total requirements over
    requirements mentioning the entity), so an entity every requirement
    mentions, such as the system itself, carries no weight.

    :param requirement_id: the requirement ID, e.g. "REQ-001".
    :param limit: maximum number of related requirements to return.
    :return: related requirements, strongest first, with matched entity pairs
        and the related requirement's triples that involve them.
    """
    with get_session() as session:
        query_result = session.run(
            """
			MATCH (any:Requirement)
			WITH count(any) AS total
			MATCH (r:Requirement {id: $requirement_id})-[:EXTRACTED_FROM]->(own:Entity)
			MATCH (other:Requirement)-[:EXTRACTED_FROM]->(shared:Entity)
			WHERE other.id <> $requirement_id
			WITH total, other, own, shared,
			     CASE
			         WHEN own = shared THEN 1.0
			         WHEN own.definition_embedding IS NULL
			              OR shared.definition_embedding IS NULL THEN 0.0
			         // Neo4j rescales cosine to [0, 1]; convert back to raw cosine
			         ELSE 2 * vector.similarity.cosine(
			             own.definition_embedding, shared.definition_embedding) - 1
			     END AS similarity
			WHERE similarity >= $threshold
			MATCH (holder:Requirement)-[:EXTRACTED_FROM]->(shared)
			WITH total, other, own, shared, similarity, count(DISTINCT holder) AS frequency
			WITH other, own, shared, similarity * log(toFloat(total) / frequency) AS weight
			WHERE weight > 0
			// Count each of this requirement's entities once per related requirement
			ORDER BY weight DESC
			WITH other, own, collect(shared.name)[0] AS shared_name, max(weight) AS weight
			WITH other, collect([own.name, shared_name]) AS matches,
			     collect(shared_name) AS shared_entities, sum(weight) AS score
			OPTIONAL MATCH (s:Entity)-[rel:RELATION {requirement_id: other.id}]->(o:Entity)
			WHERE s.name IN shared_entities OR o.name IN shared_entities
			RETURN other.id AS id, other.text AS text, matches, shared_entities, score,
			       collect([s.name, rel.type, o.name]) AS triples
			ORDER BY score DESC, id
			LIMIT $limit
			""",
            requirement_id=requirement_id,
            threshold=ENTITY_SIMILARITY_THRESHOLD,
            limit=limit,
        )

        return [
            {
                "id": row["id"],
                "text": row["text"],
                "shared_entities": row["shared_entities"],
                # [this requirement's entity, the related requirement's entity]
                "matches": row["matches"],
                "score": row["score"],
                # OPTIONAL MATCH yields [null, null, null] when no triple matches
                "triples": [triple for triple in row["triples"] if triple[1] is not None],
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

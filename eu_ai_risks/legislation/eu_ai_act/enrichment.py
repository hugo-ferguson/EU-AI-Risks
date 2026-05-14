"""
Post-build enrichment passes that annotate the EU AI Act graph without
reparsing the source PDF.
"""

import re

from eu_ai_risks.db import get_session
from eu_ai_risks.llm import complete, complete_json

# Maps chapter number to the risk tier of its articles.
CHAPTER_RISK_TIERS: dict[int, str] = {
	1: "scope",
	2: "unacceptable",
	3: "high",
	4: "limited",
	5: "general_purpose",
}
# Chapters VI–XIII: governance, market surveillance, penalties, final provisions.
DEFAULT_RISK_TIER = "governance"


def add_risk_tiers() -> None:
	"""
	Write a risk_tier property to every Article node in Neo4j based on the
	chapter it belongs to.

	:return: None
	"""
	rows = [
		{"chapter_num": chapter_num, "risk_tier": tier}
		for chapter_num, tier in CHAPTER_RISK_TIERS.items()
	]

	with get_session() as session:
		session.run(
			"""
			UNWIND $rows AS row
			MATCH (c:Chapter {num: row.chapter_num})-[:CONTAINS]->(a:Article)
			SET a.risk_tier = row.risk_tier
			""",
			rows=rows,
		)
		session.run(
			"""
			MATCH (c:Chapter)-[:CONTAINS]->(a:Article)
			WHERE a.risk_tier IS NULL
			SET a.risk_tier = $risk_tier
			""",
			risk_tier=DEFAULT_RISK_TIER,
		)

	print("  Added risk_tier to article nodes.")


OBLIGATION_TYPES = (
	"requirement",
	"prohibition",
	"permission",
	"definition",
	"scope",
	"informational",
)

OBLIGATION_TYPE_SYSTEM_PROMPT = """You are a legal text classifier specialising in EU legislation.
Classify the obligation type of a paragraph from the EU AI Act.

Respond with exactly one word from this list:
- requirement: the text imposes a positive obligation ("shall", "must", "is required to")
- prohibition: the text forbids something ("shall not", "is prohibited", "are forbidden")
- permission: the text grants a discretionary right ("may", "is permitted to")
- definition: the text defines a term or concept ("means", "refers to", "for the purposes of")
- scope: the text states what the provision applies or does not apply to ("shall apply to", "shall not apply to")
- informational: the text is explanatory, transitional, or does not fit the above

Respond with only the single classification word. No explanation."""


def classify_obligation_type(
		paragraph_text: str,
		article_title: str,
		article_text: str
) -> str:
	"""
	Classify the obligation of a paragraph using the LLM.

	:param paragraph_text: the paragraph text to classify.
	:param article_title: the title of the parent article.
	:param article_text: the full text of the parent article.
	:return: one of the obligation type strings.
	"""
	prompt = f"""Article: {article_title}

Article text:
{article_text}

Paragraph to classify:
{paragraph_text}"""

	result = complete(
		prompt,
		system=OBLIGATION_TYPE_SYSTEM_PROMPT,
		max_tokens=10
	).strip().lower()

	# Prefer exact match, fall back to substring.
	for obligation_type in OBLIGATION_TYPES:
		if result == obligation_type:
			return obligation_type

	for obligation_type in OBLIGATION_TYPES:
		if obligation_type in result:
			return obligation_type

	return "informational"


def add_obligation_types() -> None:
	"""
	Classify and write an obligation_type property to every Paragraph node in
	Neo4j using the configured LLM.

	:return: None
	"""
	with get_session() as session:
		rows = session.run(
			"""
			MATCH (a:Article)-[:HAS_PARAGRAPH]->(p:Paragraph)
			WHERE p.obligation_type IS NULL
			RETURN p.id AS id, p.text AS text, a.title AS article_title, a.text AS article_text
			ORDER BY p.id
			"""
		).data()

	if not rows:
		print("  All paragraphs already classified.")
		return

	print(f"  Classifying {len(rows)} paragraphs ...")

	results = []
	for i, row in enumerate(rows, 1):
		try:
			obligation_type = classify_obligation_type(
				row["text"],
				row["article_title"] or "",
				row["article_text"] or "",
			)
		except Exception as e:
			print(f"  [{i}/{len(rows)}] {row['id']} FAILED: {e}")
			continue
		results.append({"id": row["id"], "obligation_type": obligation_type})
		print(f"  [{i}/{len(rows)}] {row['id']} is '{obligation_type}'")

	if results:
		with get_session() as session:
			session.run(
				"""
				UNWIND $rows AS row
				MATCH (p:Paragraph {id: row.id})
				SET p.obligation_type = row.obligation_type
				""",
				rows=results,
			)

	print(f"  Classified {len(results)} of {len(rows)} paragraphs.")


RE_CONCEPT_ID = re.compile(r'[^a-z0-9]+')

CONCEPT_EXTRACTION_SYSTEM_PROMPT = """You are a legal text extractor specialising in EU legislation.

Extract the formally defined term from this EU AI Act paragraph.
Article 3 is the definitions article — each paragraph defines exactly one term.

Respond with JSON only, no explanation:
{"name": "the defined term exactly as written", "description": "one sentence definition"}

If the paragraph does not define a term, respond with:
{"name": null, "description": null}"""

CONCEPT_USAGE_SYSTEM_PROMPT = """You are a legal text analyser specialising in EU legislation.

You will be given an article from the EU AI Act and a list of defined concepts.
Identify which concepts this article materially references or relies on.

Rules:
- Only return concepts from the provided list.
- Do not include concepts that appear only incidentally or in passing cross-references.
- Do not include concepts that are merely mentioned as an article number.

Respond with JSON only, no explanation:
{"concepts": ["concept one", "concept two"]}

If no concepts apply, respond with:
{"concepts": []}"""


def concept_id(name: str) -> str:
	"""
	Convert a concept name to a stable node id.

	:param name: the concept name.
	:return: a 'graph friendly' id string, e.g. "concept:high-risk-ai-system".
	"""
	return RE_CONCEPT_ID.sub('-', name.lower()).strip('-')


def extract_concept_from_paragraph(paragraph_text: str) -> dict | None:
	"""
	Ask the LLM to extract a defined concept from a single Art 3 paragraph.

	:param paragraph_text: the paragraph text.
	:return: dict with 'name' and 'description', or None if no concept found.
	"""
	try:
		parsed = complete_json(
			paragraph_text,
			system=CONCEPT_EXTRACTION_SYSTEM_PROMPT,
			max_tokens=150,
		)
	except ValueError:
		return None

	if isinstance(parsed, list):
		parsed = parsed[0] if parsed else None

	if not parsed or not parsed.get("name"):
		return None

	return {"name": parsed["name"], "description": parsed["description"] or ""}


def find_used_concepts(
		article_title: str,
		article_text: str,
		concept_names: list[str]
) -> list[str]:
	"""
	Ask the LLM which concepts from the seed list an article materially uses.

	:param article_title: the article title.
	:param article_text: the full article text.
	:param concept_names: the list of known concept names.
	:return: list of concept names used by the article.
	"""
	concept_list = "\n".join(f"- {name}" for name in concept_names)
	prompt = f"""Article: {article_title}

Text:
{article_text}

Concepts to check:
{concept_list}"""

	try:
		parsed = complete_json(
			prompt,
			system=CONCEPT_USAGE_SYSTEM_PROMPT,
			max_tokens=300,
		)
	except ValueError:
		return []

	concepts = parsed.get("concepts", []) if (
		isinstance(parsed, dict)
	) else parsed

	if not isinstance(concepts, list):
		return []

	valid = set(concept_names)
	return [name for name in concepts if
			isinstance(name, str) and name in valid]


def add_concepts() -> None:
	"""
	Extract Concept nodes from Article 3 and write DEFINES and USES edges
	linking them to the paragraphs and articles that define or reference them.
	Article 3 is unique as it contains the legal definitions section.

	:return: None
	"""
	# Skip extraction if concepts already exist in the graph.
	with get_session() as session:
		existing = session.run(
			"MATCH (c:Concept) RETURN c.id AS id, c.name AS name, c.description AS description"
		).data()

	if existing:
		print(f"  {len(existing)} concepts already exist, skipping extraction.")
		concept_nodes = existing
	else:
		with get_session() as session:
			article_three_paragraphs = session.run(
				"""
				MATCH (a:Article {id: 'art:3'})-[:HAS_PARAGRAPH]->(p:Paragraph)
				RETURN p.id AS id, p.text AS text
				ORDER BY p.num
				"""
			).data()

		print(f"  Extracting concepts from {len(article_three_paragraphs)} "
			  f"Article 3 paragraphs ...")

		concept_nodes = []
		defines_edges = []

		for i, row in enumerate(article_three_paragraphs, 1):
			try:
				concept = extract_concept_from_paragraph(row["text"])
			except Exception as e:
				print(f"  [{i}/{len(article_three_paragraphs)}] {row['id']} "
					  f"FAILED: {e}")
				continue

			if not concept:
				print(f"  [{i}/{len(article_three_paragraphs)}] {row['id']} "
					  f"(no concept found)")
				continue

			node_id = concept_id(concept["name"])
			concept_nodes.append({
				"id": node_id,
				"name": concept["name"],
				"description": concept["description"],
			})
			defines_edges.append({"src": row["id"], "dst": node_id})
			print(f"  [{i}/{len(article_three_paragraphs)}] {row['id']} "
				  f"defines concept '{concept['name']}'")

		if not concept_nodes:
			print("  No concepts extracted.")
			return

		with get_session() as session:
			session.run("CREATE CONSTRAINT concept_id IF NOT EXISTS FOR (n:Concept) REQUIRE n.id IS UNIQUE")
			session.run(
				"""
				UNWIND $rows AS row
				MERGE (c:Concept {id: row.id})
				SET c.name = row.name, c.description = row.description
				""",
				rows=concept_nodes,
			)
			session.run(
				"""
				UNWIND $rows AS row
				MATCH (p:Paragraph {id: row.src})
				MATCH (c:Concept {id: row.dst})
				MERGE (p)-[:DEFINES]->(c)
				""",
				rows=defines_edges,
			)

		print(f"  Wrote {len(concept_nodes)} Concept nodes and "
			  f"{len(defines_edges)} DEFINES edges.")

	with get_session() as session:
		articles = session.run(
			"""
			MATCH (a:Article)
			WHERE a.id <> 'art:3'
			RETURN a.id AS id, a.title AS title, a.text AS text
			ORDER BY a.num
			"""
		).data()

	concept_names = [node["name"] for node in concept_nodes]

	print(f"  Finding concept usage across {len(articles)} articles ...")

	uses_edges = []
	for i, row in enumerate(articles, 1):
		try:
			used = find_used_concepts(
				row["title"] or "",
				row["text"] or "",
				concept_names,
			)
		except Exception as e:
			print(f"  [{i}/{len(articles)}] {row['id']} FAILED: {e}")
			continue
		for name in used:
			uses_edges.append({"src": row["id"], "dst": concept_id(name)})
		print(f"  [{i}/{len(articles)}] {row['id']} uses '{used or '(none)'}'")

	if uses_edges:
		with get_session() as session:
			session.run(
				"""
				UNWIND $rows AS row
				MATCH (a:Article {id: row.src})
				MATCH (c:Concept {id: row.dst})
				MERGE (a)-[:USES]->(c)
				""",
				rows=uses_edges,
			)

	print(f"  Wrote {len(uses_edges)} USES edges.")

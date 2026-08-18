"""
Tag EU AI Act provisions with controlled-vocabulary dimension nodes.

This is quite a fixed process of matching AI act risks, systems, actors, etc.
to the text. This is quite AI Act specific - something else would be required
(without analysing using an LLM, anyway) for other texts.

This makes the graph more useful for analysis by an LLM.
"""

import re
from typing import cast, LiteralString

from eu_ai_risks.db import get_session

# Each dimension is a set list of words derived from the act.
# These are used to tag things like risks, systems, actors, etc. in the act.

RESPONSIBLE_PARTIES = {
	"provider": (r"\bproviders?\b", "Provider"),
	"deployer": (r"\bdeployers?\b", "Deployer"),
	"importer": (r"\bimporters?\b", "Importer"),
	"distributor": (r"\bdistributors?\b", "Distributor"),
	"authorised_representative": (r"\bauthorised representatives?\b", "Authorised representative"),
	"product_manufacturer": (r"\bproduct manufacturers?\b", "Product manufacturer"),
	"notified_body": (r"\bnotified bod(?:y|ies)\b", "Notified body"),
	"notifying_authority": (r"\bnotifying authorit(?:y|ies)\b", "Notifying authority"),
	"market_surveillance_authority": (r"\bmarket surveillance authorit(?:y|ies)\b", "Market surveillance authority"),
	"national_competent_authority": (r"\bnational competent authorit(?:y|ies)\b", "National competent authority"),
	"ai_office": (r"\bAI Office\b", "AI Office"),
	"commission": (r"\bCommission\b", "Commission"),
	"member_state": (r"\bMember States?\b", "Member State"),
}

REQUIREMENT_CATEGORIES = {
	"ai_literacy": "AI literacy",
	"risk_management": "Risk management system",
	"data_governance": "Data and data governance",
	"technical_documentation": "Technical documentation",
	"record_keeping": "Record-keeping and logging",
	"transparency": "Transparency and provision of information",
	"human_oversight": "Human oversight",
	"accuracy_robustness_cybersecurity": "Accuracy, robustness and cybersecurity",
	"quality_management": "Quality management system",
	"conformity_assessment": "Conformity assessment",
	"registration": "Registration",
	"post_market_monitoring": "Post-market monitoring",
	"serious_incident_reporting": "Serious incident reporting",
	"fundamental_rights_impact_assessment": "Fundamental rights impact assessment",
}

# Each article talks about a requirement, so map these here.
REQUIREMENT_ARTICLE_MAP = {
	"art:4": "ai_literacy",
	"art:9": "risk_management",
	"art:10": "data_governance",
	"art:11": "technical_documentation",
	"art:12": "record_keeping",
	"art:13": "transparency",
	"art:14": "human_oversight",
	"art:15": "accuracy_robustness_cybersecurity",
	"art:17": "quality_management",
	"art:18": "technical_documentation",
	"art:19": "record_keeping",
	"art:27": "fundamental_rights_impact_assessment",
	"art:43": "conformity_assessment",
	"art:49": "registration",
	"art:50": "transparency",
	"art:72": "post_market_monitoring",
	"art:73": "serious_incident_reporting",
}

# The four risk tiers plus the two general-purpose classes. 
RISK_CATEGORIES = {
	"prohibited": "Prohibited (unacceptable risk)",
	"high_risk": "High-risk",
	"transparency": "Limited risk (transparency)",
	"gpai": "General-purpose AI model",
	"gpai_systemic": "General-purpose AI model with systemic risk",
}

# The chapter each risk tier is defined in. 
RISK_CHAPTER_MAP = {
	"II": "prohibited",
	"III": "high_risk",
	"IV": "transparency",
}

GPAI_SYSTEMIC_ARTICLES = {"art:51", "art:55"}

# The eight high-risk areas in Annex III.
SYSTEM_CATEGORIES = {
	"biometrics": "Biometrics",
	"critical_infrastructure": "Critical infrastructure",
	"education_vocational_training": "Education and vocational training",
	"employment": "Employment and workers' management",
	"essential_services": "Access to essential private and public services",
	"law_enforcement": "Law enforcement",
	"migration_asylum_border": "Migration, asylum and border control",
	"justice_democracy": "Administration of justice and democratic processes",
}

# Data types defined in Article 3.
DATA_CATEGORIES = {
	"special_category_personal_data": (r"special categories of personal data", "Special categories of personal data"),
	"biometric_data": (r"\bbiometric data\b", "Biometric data"),
	"non_personal_data": (r"\bnon-personal data\b", "Non-personal data"),
	"personal_data": (r"(?<!non-)\bpersonal data\b", "Personal data"),
	"sensitive_operational_data": (r"\bsensitive operational data\b", "Sensitive operational data"),
	"training_data": (r"\btraining data\b", "Training data"),
	"validation_data": (r"\bvalidation data\b", "Validation data"),
	"testing_data": (r"\btesting data\b", "Testing data"),
	"input_data": (r"\binput data\b", "Input data"),
}


def _match_terms(text: str, vocabulary: dict[str, tuple[str, str]]) -> list[str]:
	"""
	Find which vocabulary keys have are present in text.

	:param text: the provision text to scan.
	:param vocabulary: a dimension vocabulary of key to (regex, name).
	:return: the keys whose regex matches.
	"""
	return [
		key for key, (pattern, _) in vocabulary.items()
		if re.search(pattern, text, re.I)
	]


def responsible_parties(text: str) -> list[str]:
	"""
	Find the responsible parties an article addresses.

	:param text: the article text.
	:return: the responsible-party keys present in the text.
	"""
	return _match_terms(text, RESPONSIBLE_PARTIES)


def data_categories(text: str) -> list[str]:
	"""
	Find the data categories an article concerns.

	:param text: the article text.
	:return: the data-category keys present in the text.
	"""
	return _match_terms(text, DATA_CATEGORIES)


def risk_category(article_id: str, chapter_roman: str) -> str | None:
	"""
	Find the risk tier of an article from the chapter it sits in.

	:param article_id: the article id.
	:param chapter_roman: the Roman numeral of the article's chapter.
	:return: the risk-category key, or None where the chapter carries no tier.
	"""
	if chapter_roman == "V":
		return "gpai_systemic" if article_id in GPAI_SYSTEMIC_ARTICLES else "gpai"

	return RISK_CHAPTER_MAP.get(chapter_roman)


def _write_dimension(
		dimension: str,
		label: str,
		edge: str,
		names: dict[str, str],
		assignments: list[tuple[str, list[str]]],
) -> None:
	"""
	Write dimension nodes and the edges linking provisions to them.

	:param dimension: the dimension name, used as the node id prefix and a property.
	:param label: the Neo4j node label for this dimension.
	:param edge: the relationship type from a provision to a dimension node.
	:param names: a map of dimension key to human-readable name.
	:param assignments: (provision id, dimension keys) pairs to write.
	"""
	node_rows = []
	edge_rows = []
	seen = set()

	for provision_id, keys in assignments:
		for key in keys:
			node_id = f"{dimension}:{key}"
			if node_id not in seen:
				seen.add(node_id)
				node_rows.append({
					"id": node_id, "key": key,
					"name": names[key], "dimension": dimension,
				})
			edge_rows.append({"src": provision_id, "dst": node_id})

	if not node_rows:
		print(f"  {dimension}: nothing to write.")
		return

	with get_session() as session:
		session.run(cast(LiteralString,
			f"CREATE CONSTRAINT {label.lower()}_id IF NOT EXISTS "
			f"FOR (n:{label}) REQUIRE n.id IS UNIQUE"
		))
		session.run(
			cast(LiteralString, f"""
				UNWIND $rows AS row
				MERGE (n:{label} {{id: row.id}})
				SET n.key = row.key, n.name = row.name, n.dimension = row.dimension
				"""),
			rows=node_rows,
		)
		session.run(
			cast(LiteralString, f"""
				UNWIND $rows AS row
				MATCH (p {{id: row.src}})
				MATCH (d:{label} {{id: row.dst}})
				MERGE (p)-[:{edge}]->(d)
				"""),
			rows=edge_rows,
		)

	print(f"  {dimension}: {len(node_rows)} {label} nodes, "
		  f"{len(edge_rows)} {edge} edges.")


def add_responsible_parties() -> None:
	"""
	Tag each Article with the responsible parties its text addresses.

	:return: None
	"""
	with get_session() as session:
		articles = session.run(
			"MATCH (a:Article) RETURN a.id AS id, a.text AS text"
		).data()

	assignments = [
		(row["id"], responsible_parties(row["text"] or ""))
		for row in articles
	]

	_write_dimension(
		"responsible_party", "ResponsibleParty", "ADDRESSES",
		{key: name for key, (_, name) in RESPONSIBLE_PARTIES.items()},
		assignments,
	)


def add_requirement_categories() -> None:
	"""
	Tag the requirement articles with the requirement theme they establish.

	:return: None
	"""
	with get_session() as session:
		existing = {
			row["id"] for row in session.run(
				"MATCH (a:Article) RETURN a.id AS id"
			).data()
		}

	assignments = [
		(article_id, [category])
		for article_id, category in REQUIREMENT_ARTICLE_MAP.items()
		if article_id in existing
	]

	_write_dimension(
		"requirement_category", "RequirementCategory", "IMPOSES",
		REQUIREMENT_CATEGORIES, assignments,
	)


def add_risk_categories() -> None:
	"""
	Tag each Article with its risk tier, derived from its chapter.

	:return: None
	"""
	with get_session() as session:
		rows = session.run(
			"""
			MATCH (c:Chapter)-[:CONTAINS*1..2]->(a:Article)
			RETURN a.id AS id, c.id AS chapter_id
			"""
		).data()

	assignments = []
	for row in rows:
		roman = row["chapter_id"].split(":")[1]
		category = risk_category(row["id"], roman)
		if category:
			assignments.append((row["id"], [category]))

	_write_dimension(
		"risk_category", "RiskCategory", "HAS_RISK",
		RISK_CATEGORIES, assignments,
	)


def add_system_categories() -> None:
	"""
	Create the Annex III high-risk area nodes and link Annex III to them.

	:return: None
	"""
	_write_dimension(
		"system_category", "SystemCategory", "COVERS",
		SYSTEM_CATEGORIES,
		[("annex:III", list(SYSTEM_CATEGORIES))],
	)


def add_data_categories() -> None:
	"""
	Tag each Article with the data categories its text concerns.

	:return: None
	"""
	with get_session() as session:
		articles = session.run(
			"MATCH (a:Article) RETURN a.id AS id, a.text AS text"
		).data()

	assignments = [
		(row["id"], data_categories(row["text"] or ""))
		for row in articles
	]

	_write_dimension(
		"data_category", "DataCategory", "CONCERNS",
		{key: name for key, (_, name) in DATA_CATEGORIES.items()},
		assignments,
	)


def add_dimensions() -> None:
	"""
	Run all dimension-tagging passes.

	:return: None
	"""
	add_responsible_parties()
	add_requirement_categories()
	add_risk_categories()
	add_system_categories()
	add_data_categories()

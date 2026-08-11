"""
LLM-driven mapping of requirements to legislation segments.
"""

from dataclasses import dataclass

from eu_ai_risks.db.graph import paragraph_details, vector_search_paragraphs
from eu_ai_risks.requirements.models import Requirement

RISK_SIGNALS = {
	"biometric_identification": {
		"keywords": {
			"biometric", "facial recognition", "face recognition",
			"emotion recognition", "remote identification",
		},
		"label": "Biometric identification or categorisation",
	},
	"automated_decision": {
		"keywords": {
			"automated decision", "decision support", "recommendation",
			"ranking", "score", "scoring", "classification", "prediction",
		},
		"label": "Automated decision-making",
	},
	"human_oversight": {
		"keywords": {
			"human review", "human oversight", "override", "appeal",
			"manual review", "operator",
		},
		"label": "Human oversight",
	},
	"transparency": {
		"keywords": {
			"explain", "explanation", "transparent", "notify", "disclose",
			"label", "user information",
		},
		"label": "Transparency and user information",
	},
	"logging": {
		"keywords": {
			"log", "logging", "audit", "trace", "record", "monitoring",
		},
		"label": "Logging and traceability",
	},
	"data_governance": {
		"keywords": {
			"personal data", "training data", "dataset", "data quality",
			"bias", "accuracy", "representative",
		},
		"label": "Data governance and quality",
	},
	"safety": {
		"keywords": {
			"safety", "security", "robustness", "fallback", "failure",
			"risk management", "harm",
		},
		"label": "Safety, robustness, and risk management",
	},
}


@dataclass
class LegislationMatch:
	paragraph_id: str
	paragraph_num: int
	paragraph_text: str
	article_id: str
	article_num: int
	article_title: str
	score: float

	def to_dict(self) -> dict:
		return {
			"paragraph_id": self.paragraph_id,
			"paragraph_num": self.paragraph_num,
			"paragraph_text": self.paragraph_text,
			"article_id": self.article_id,
			"article_num": self.article_num,
			"article_title": self.article_title,
			"score": self.score,
		}


@dataclass
class RiskMapping:
	requirement: Requirement
	matches: list[LegislationMatch]
	risk_signals: list[str]
	risk_level: str
	explanation: str

	def to_dict(self) -> dict:
		return {
			"requirement": self.requirement.to_dict(),
			"matches": [match.to_dict() for match in self.matches],
			"risk_signals": self.risk_signals,
			"risk_level": self.risk_level,
			"explanation": self.explanation,
		}


def map_requirements_to_legislation(
	requirements: list[Requirement],
	top_k: int = 5,
	min_score: float = 0.55,
) -> list[RiskMapping]:
	"""
	Map requirements to relevant EU AI Act paragraphs using vector search.

	:param requirements: requirements to map.
	:param top_k: number of paragraph candidates to retrieve per requirement.
	:param min_score: minimum vector score kept in the report.
	:return: risk mappings with matches and rule-based risk signals.
	"""
	from eu_ai_risks.embeddings import embed_text

	mappings = []
	for requirement in requirements:
		query_embedding = embed_text(requirement.text)
		search_results = vector_search_paragraphs(query_embedding, top_k)
		paragraph_ids = [paragraph_id for paragraph_id, _, _ in search_results]
		details_by_id = paragraph_details(paragraph_ids)

		matches = []
		for paragraph_id, paragraph_num, score in search_results:
			if score < min_score or paragraph_id not in details_by_id:
				continue

			details = details_by_id[paragraph_id]
			matches.append(LegislationMatch(
				paragraph_id=paragraph_id,
				paragraph_num=paragraph_num,
				paragraph_text=details["paragraph_text"],
				article_id=details["article_id"],
				article_num=details["article_num"],
				article_title=details["article_title"],
				score=score,
			))

		risk_signals = detect_risk_signals(requirement.text)
		risk_level = estimate_risk_level(matches, risk_signals)
		explanation = explain_mapping(requirement, matches, risk_signals, risk_level)
		mappings.append(RiskMapping(
			requirement=requirement,
			matches=matches,
			risk_signals=risk_signals,
			risk_level=risk_level,
			explanation=explanation,
		))

	return mappings


def detect_risk_signals(requirement_text: str) -> list[str]:
	text = requirement_text.lower()
	signals = []

	for signal_config in RISK_SIGNALS.values():
		if any(keyword in text for keyword in signal_config["keywords"]):
			signals.append(signal_config["label"])

	return signals


def estimate_risk_level(
	matches: list[LegislationMatch], risk_signals: list[str]
) -> str:
	if not matches:
		return "Unmapped"

	top_score = matches[0].score
	if top_score >= 0.78 and len(risk_signals) >= 2:
		return "High"
	if top_score >= 0.68 or risk_signals:
		return "Medium"
	return "Low"


def explain_mapping(
	requirement: Requirement,
	matches: list[LegislationMatch],
	risk_signals: list[str],
	risk_level: str,
) -> str:
	if not matches:
		return (
			"No EU AI Act paragraph exceeded the similarity threshold. "
			"This requirement should be manually reviewed if it describes AI "
			"functionality or processing of sensitive data."
		)

	top_match = matches[0]
	signal_text = (
		"; ".join(risk_signals)
		if risk_signals else
		"no explicit keyword risk signal"
	)

	return (
		f"Mapped to Article {top_match.article_num}, paragraph "
		f"{top_match.paragraph_num} with score {top_match.score:.3f}. "
		f"Detected signals: {signal_text}. "
		f"Estimated risk level: {risk_level}."
	)

"""
Semantic profiling for requirement-to-EU-AI-Act risk assessment.

Converts a software requirement into a structured profile (intent, obligation
categories, controls, gaps) then uses that to retrieve and rerank provisions.
"""

from __future__ import annotations

import os
from functools import lru_cache

from pydantic import BaseModel, ConfigDict, Field

from eu_ai_risks.llm import complete_json

PROFILE_MAX_TOKENS = int(os.environ.get(
    "EU_AI_RISKS_PROFILE_MAX_TOKENS", "700"))
PROFILE_MODE = os.environ.get(
    "EU_AI_RISKS_PROFILE_MODE", "semantic").strip().lower()
PROFILE_CONFIDENCE_SCORE = float(os.environ.get(
    "EU_AI_RISKS_PROFILE_CONFIDENCE_SCORE", "0.38"))
PROFILE_CONFIDENCE_MARGIN = float(os.environ.get(
    "EU_AI_RISKS_PROFILE_CONFIDENCE_MARGIN", "0.012"))

DEFAULT_CATEGORY_KEYS = {
    # Chapter I / Article 4
    "ai_literacy",

    # Chapter II / Article 5
    "prohibited_practice",

    # Article 6 + Annex III classification
    "high_risk_classification",
    "annex_iii_high_risk_domain",

    # Chapter III high-risk AI system requirements
    "risk_management",
    "data_governance",
    "technical_documentation",
    "annex_iv_technical_documentation",
    "record_keeping",
    "transparency",
    "human_oversight",
    "accuracy_robustness_cybersecurity",
    "quality_management",
    "fundamental_rights_impact_assessment",
    "conformity_assessment",
    "registration",

    # Chapter IV / Article 50 transparency obligations
    "general_transparency",
    "ai_interaction_disclosure",
    "synthetic_content_labelling",
    "deepfake_disclosure",
    "biometric_emotion_disclosure",

    # Chapter IX lifecycle obligations
    "post_market_monitoring",
    "serious_incident_reporting",
}

INTENT_VALUES = {
    "data_ingestion",
    "scoring_or_prediction",
    "ranking_or_prioritisation",
    "explanation_or_transparency",
    "notification_or_disclosure",
    "human_review_or_override",
    "logging_or_audit",
    "access_control_or_security",
    "monitoring_or_alerting",
    "rollback_or_corrective_action",
    "prohibited_feature_prevention",
    "prohibited_practice_use",
    "high_risk_domain_classification",
    "ai_interaction_disclosure",
    "synthetic_content_generation",
    "deepfake_generation",
    "biometric_emotion_disclosure",
    "post_market_monitoring",
    "serious_incident_reporting",
    "annex_iv_documentation",
    "data_validation_or_bias_testing",
    "protected_attribute_control",
    "technical_documentation",
    "risk_management_process",
    "ai_literacy_training",
    "conformity_or_registration",
    "other",
    "unknown",
}


# Additional provision anchors required for a stronger software-system checker.
# These keep the same category -> graph anchor design used by the Chapter III
# implementation, but broaden it to prohibited-practice screening, Article 50
# transparency duties, Annex III high-risk classification, Annex IV technical
# documentation detail, and Chapter IX lifecycle monitoring/incident reporting.
EXTENDED_REQUIREMENT_CATEGORIES = {
    "prohibited_practice": {
        "name": "Prohibited AI practice review",
        "article_ids": ["art:5"],
    },
    "high_risk_classification": {
        "name": "High-risk classification",
        "article_ids": ["art:6"],
    },
    "annex_iii_high_risk_domain": {
        "name": "Annex III high-risk domain",
        "article_ids": ["annex:III", "art:6"],
    },
    "annex_iv_technical_documentation": {
        "name": "Annex IV technical documentation detail",
        "article_ids": ["annex:IV", "art:11"],
    },
    "general_transparency": {
        "name": "General transparency obligations",
        "article_ids": ["art:50"],
    },
    "ai_interaction_disclosure": {
        "name": "AI interaction disclosure",
        "article_ids": ["art:50"],
    },
    "synthetic_content_labelling": {
        "name": "Synthetic content labelling",
        "article_ids": ["art:50"],
    },
    "deepfake_disclosure": {
        "name": "Deepfake disclosure",
        "article_ids": ["art:50"],
    },
    "biometric_emotion_disclosure": {
        "name": "Biometric/emotion-recognition disclosure",
        "article_ids": ["art:50"],
    },
}


def extend_requirement_categories(categories: list[dict] | None) -> list[dict]:
    """Return graph categories plus built-in extended mapping categories.

    The Neo4j graph may have been built before these broader EU AI Act
    categories were added. Merging them here makes the non-agent assessor
    immediately usable while still allowing a rebuilt graph to expose the same
    categories natively.
    """
    merged: dict[str, dict] = {}
    for category in categories or []:
        key = str(category.get("key", "")).strip()
        if key:
            merged[key] = {
                "key": key,
                "name": category.get("name", key),
                "article_ids": list(category.get("article_ids", [])),
            }

    for key, meta in EXTENDED_REQUIREMENT_CATEGORIES.items():
        existing = merged.get(key)
        if existing:
            article_ids = list(dict.fromkeys(
                list(existing.get("article_ids", []))
                + list(meta.get("article_ids", []))
            ))
            existing["article_ids"] = article_ids
            existing["name"] = existing.get("name") or meta["name"]
        else:
            merged[key] = {"key": key, **meta}

    return list(merged.values())

# Intent labels are stable software-engineering concepts. They are not
# requirement-specific keyword rules. The LLM extracts the intent, and this
# policy gives the risk assessor a maintainable default interpretation for
# that intent. This is what stops the report from drifting into unrelated
# categories such as human oversight for simple data ingestion.
INTENT_CATEGORY_POLICY = {
    "data_ingestion": {
        "primary": "data_governance",
        "secondary": ["technical_documentation"],
        "missing": ["data_governance"],
        "existing": [],
    },
    "scoring_or_prediction": {
        "primary": "data_governance",
        "secondary": [
            "transparency",
            "human_oversight",
            "accuracy_robustness_cybersecurity",
        ],
        "missing": [
            "data_governance",
            "transparency",
            "human_oversight",
            "accuracy_robustness_cybersecurity",
        ],
        "existing": [],
    },
    "ranking_or_prioritisation": {
        "primary": "transparency",
        "secondary": [
            "human_oversight",
            "accuracy_robustness_cybersecurity",
            "data_governance",
        ],
        "missing": [
            "transparency",
            "human_oversight",
            "accuracy_robustness_cybersecurity",
        ],
        "existing": [],
    },
    "explanation_or_transparency": {
        "primary": "transparency",
        "secondary": ["technical_documentation"],
        "missing": ["transparency"],
        "existing": ["transparency"],
    },
    "notification_or_disclosure": {
        "primary": "transparency",
        "secondary": [],
        "missing": ["transparency"],
        "existing": ["transparency"],
    },
    "human_review_or_override": {
        "primary": "human_oversight",
        "secondary": ["transparency"],
        "missing": ["human_oversight"],
        "existing": ["human_oversight"],
        "safeguard": True,
    },
    "logging_or_audit": {
        "primary": "record_keeping",
        "secondary": ["technical_documentation"],
        "missing": ["record_keeping"],
        "existing": ["record_keeping"],
        "safeguard": True,
    },
    "access_control_or_security": {
        "primary": "accuracy_robustness_cybersecurity",
        "secondary": ["data_governance"],
        "missing": ["accuracy_robustness_cybersecurity"],
        "existing": ["accuracy_robustness_cybersecurity"],
        "safeguard": True,
    },
    "monitoring_or_alerting": {
        "primary": "post_market_monitoring",
        "secondary": [
            "risk_management",
            "data_governance",
            "accuracy_robustness_cybersecurity",
        ],
        "missing": ["post_market_monitoring", "risk_management"],
        "existing": ["post_market_monitoring"],
        "safeguard": True,
    },
    "rollback_or_corrective_action": {
        "primary": "accuracy_robustness_cybersecurity",
        "secondary": ["risk_management", "post_market_monitoring"],
        "missing": ["accuracy_robustness_cybersecurity", "risk_management"],
        "existing": ["accuracy_robustness_cybersecurity"],
        "safeguard": True,
    },
    "prohibited_feature_prevention": {
        "primary": "",
        "secondary": [],
        "missing": [],
        "existing": [],
        "safeguard": True,
    },
    "data_validation_or_bias_testing": {
        "primary": "data_governance",
        "secondary": ["accuracy_robustness_cybersecurity", "risk_management"],
        "missing": ["data_governance"],
        "existing": ["data_governance"],
        "safeguard": True,
    },
    "protected_attribute_control": {
        "primary": "data_governance",
        "secondary": ["risk_management"],
        "missing": ["data_governance"],
        "existing": ["data_governance"],
        "safeguard": True,
    },
    "technical_documentation": {
        "primary": "technical_documentation",
        "secondary": [],
        "missing": ["technical_documentation"],
        "existing": ["technical_documentation"],
        "safeguard": True,
    },
    "risk_management_process": {
        "primary": "risk_management",
        "secondary": [],
        "missing": ["risk_management"],
        "existing": ["risk_management"],
        "safeguard": True,
    },
    "prohibited_practice_use": {
        "primary": "prohibited_practice",
        "secondary": [],
        "missing": ["prohibited_practice"],
        "existing": [],
    },
    "high_risk_domain_classification": {
        "primary": "high_risk_classification",
        "secondary": ["annex_iii_high_risk_domain"],
        "missing": ["high_risk_classification", "annex_iii_high_risk_domain"],
        "existing": [],
    },
    "ai_interaction_disclosure": {
        "primary": "ai_interaction_disclosure",
        "secondary": ["general_transparency"],
        "missing": ["ai_interaction_disclosure"],
        "existing": [],
    },
    "synthetic_content_generation": {
        "primary": "synthetic_content_labelling",
        "secondary": ["general_transparency"],
        "missing": ["synthetic_content_labelling"],
        "existing": [],
    },
    "deepfake_generation": {
        "primary": "deepfake_disclosure",
        "secondary": ["synthetic_content_labelling", "general_transparency"],
        "missing": ["deepfake_disclosure"],
        "existing": [],
    },
    "biometric_emotion_disclosure": {
        "primary": "biometric_emotion_disclosure",
        "secondary": ["general_transparency"],
        "missing": ["biometric_emotion_disclosure"],
        "existing": [],
    },
    "post_market_monitoring": {
        "primary": "post_market_monitoring",
        "secondary": ["risk_management", "technical_documentation"],
        "missing": ["post_market_monitoring"],
        "existing": ["post_market_monitoring"],
        "safeguard": True,
    },
    "serious_incident_reporting": {
        "primary": "serious_incident_reporting",
        "secondary": ["post_market_monitoring", "risk_management"],
        "missing": ["serious_incident_reporting"],
        "existing": ["serious_incident_reporting"],
        "safeguard": True,
    },
    "annex_iv_documentation": {
        "primary": "annex_iv_technical_documentation",
        "secondary": ["technical_documentation"],
        "missing": ["annex_iv_technical_documentation", "technical_documentation"],
        "existing": ["annex_iv_technical_documentation"],
        "safeguard": True,
    },
    "ai_literacy_training": {
        "primary": "ai_literacy",
        "secondary": [],
        "missing": ["ai_literacy"],
        "existing": ["ai_literacy"],
        "safeguard": True,
    },
    "conformity_or_registration": {
        "primary": "conformity_assessment",
        "secondary": ["registration", "technical_documentation"],
        "missing": ["conformity_assessment", "registration"],
        "existing": [],
    },
}

INTENT_SEMANTIC_DESCRIPTIONS = {
    "data_ingestion": "collecting, receiving, importing or storing application inputs, documents, records or user-submitted data",
    "scoring_or_prediction": "calculating a score, prediction, rating, suitability estimate, risk score or model-generated assessment",
    "ranking_or_prioritisation": "ordering, ranking, prioritising, shortlisting or sorting people, cases or items using model output",
    "explanation_or_transparency": "explaining model output, showing factors, giving reasons, making automated output understandable",
    "notification_or_disclosure": "notifying or informing a person that AI, automation or decision support was used",
    "human_review_or_override": "human review, manual approval, override, rejection, escalation or human decision-maker control",
    "logging_or_audit": "logging, audit trail, event records, retained evidence, traceability records or model version records",
    "access_control_or_security": "permissions, authorised access, confidentiality, security controls or restricting who can view data",
    "monitoring_or_alerting": "monitoring deployed performance, alerts, thresholds, drift, bias metrics or data-quality metrics",
    "rollback_or_corrective_action": "rollback, reverting model versions, corrective action, fail-safe response or recovery after failed checks",
    "prohibited_feature_prevention": "preventing or banning the use of biometric identification, emotion recognition or other disallowed features",
    "data_validation_or_bias_testing": "validating training, evaluation or testing datasets, checking missing values, duplicates, labels, representativeness, demographic performance, bias or fairness metrics",
    "protected_attribute_control": "preventing protected attributes such as race, religion, disability, political opinion, gender or age from being used as model inputs or ranking factors",
    "technical_documentation": "creating or maintaining technical documentation, system design records or compliance evidence",
    "risk_management_process": "risk assessment, risk management, risk review, mitigation planning or documenting harms",
    "prohibited_practice_use": "using or proposing manipulative AI, exploitative systems, social scoring, prohibited biometric categorisation, workplace or education emotion recognition, untargeted facial scraping, prohibited predictive policing or real-time remote biometric identification",
    "high_risk_domain_classification": "software requirement describing a use case in an Annex III high-risk domain, such as recruitment, education, essential services, law enforcement, migration, critical infrastructure, biometrics or justice",
    "ai_interaction_disclosure": "informing people that they are interacting with an AI system, chatbot, virtual assistant or conversational AI",
    "synthetic_content_generation": "generating synthetic text, audio, image or video content and labelling or marking it as AI-generated",
    "deepfake_generation": "generating or manipulating image, audio or video content that could appear to be a real person, event, place or object, including deepfakes",
    "biometric_emotion_disclosure": "notices or information for people exposed to biometric categorisation or emotion recognition systems",
    "post_market_monitoring": "monitoring deployed AI system performance, drift, accuracy, bias, risk, incidents or compliance after release",
    "serious_incident_reporting": "detecting, escalating, documenting or reporting serious incidents or fundamental-rights impacts to authorities or responsible teams",
    "annex_iv_documentation": "maintaining technical documentation contents such as intended purpose, design specifications, model architecture, training data, validation results, risk controls and monitoring plans",
    "ai_literacy_training": "training staff, deployers, users or operators so they understand AI system capabilities, limitations, risks and appropriate use",
    "conformity_or_registration": "conformity assessment, declaration of conformity, CE marking, registration or market-placement compliance workflow",
}

HIGH_RISK_DOMAIN_DESCRIPTIONS = {
    "biometrics": "remote biometric identification, biometric verification or biometric categorisation of natural persons",
    "critical_infrastructure": "AI system used as a safety component or management tool for critical digital infrastructure, road traffic, water, gas, heating or electricity",
    "education_vocational_training": "AI system used for education or vocational training access, admissions, grading, assessment, learning outcomes or monitoring prohibited behaviour during tests",
    "employment_recruitment": "AI system used for recruitment, candidate screening, employment decisions, worker management, hiring, selection, promotion, task allocation, performance monitoring or termination",
    "essential_private_public_services": "AI system used for access to public assistance, essential private services, credit scoring, health insurance or life insurance, emergency dispatch or priority services",
    "law_enforcement": "AI system used by or for law enforcement, criminal risk assessment, evidence evaluation, profiling, polygraphs, crime analytics or criminal investigation support",
    "migration_asylum_border": "AI system used for migration, asylum, visa, border control, security-risk assessment, document checking or border decision support",
    "justice_democratic_processes": "AI system used for judicial decision support, legal fact or law interpretation, dispute resolution, elections, voting behaviour or democratic-process influence",
}


@lru_cache(maxsize=1)
def _cached_high_risk_domain_embeddings() -> tuple[tuple[tuple[str, str], ...], tuple[tuple[float, ...], ...]]:
    from eu_ai_risks.embeddings import embed_batch

    items = tuple(HIGH_RISK_DOMAIN_DESCRIPTIONS.items())
    embeddings = embed_batch([description for _, description in items])
    return items, tuple(tuple(vector) for vector in embeddings)


def infer_high_risk_context_semantically(requirement_text: str) -> tuple[str, float]:
    """Infer broad Annex III-style context using embedding similarity.

    This is intentionally conservative and only used for context labels. It does
    not make a final legal classification.
    """
    try:
        from eu_ai_risks.embeddings import embed_text

        items, embeddings = _cached_high_risk_domain_embeddings()
        requirement_embedding = embed_text(requirement_text)
        scored = [
            (domain, _cosine_similarity(requirement_embedding, list(embedding)))
            for (domain, _), embedding in zip(items, embeddings)
        ]
        scored.sort(key=lambda item: item[1], reverse=True)
        return scored[0]
    except Exception:
        return "", 0.0


REQUIREMENT_PROFILE_PROMPT = """\
You extract structured software-engineering meaning from ONE requirement for an
EU AI Act compliance prototype.

Do not make final legal conclusions. Do not rely on exact keyword matching.
Infer cautiously from the requirement text and return ONLY JSON.

Critical rules:
- Profile the exact requirement, not the whole SRS or surrounding system.
- Do not add human_oversight just because the system is high-risk. Add it only
  if the requirement itself is about human review, override, decision-maker
  competence, monitoring by people, escalation, or review of automated outputs.
- Do not add data_governance just because data exists. Add it when the
  requirement is about data quality, datasets, inputs, protected attributes,
  bias/fairness, collection/origin, retention, or data management.
- Do not add transparency just because users exist. Add it when the requirement
  is about explanations, notification, instructions, understandability, or
  information provided to deployers/affected persons.
- Do not add record_keeping unless the requirement is about logs, audit trails,
  traceability records, retained evidence, model/version records, or event
  recording.
- If the requirement already describes a control/safeguard, put that category
  in existing_control_categories and set is_safeguard_or_control to true.
- Only put a category in missing_or_unclear_categories if the requirement
  appears to leave an obligation unclear or incomplete.
- If there is not enough information, use low confidence and explain the
  uncertainty briefly in notes.

Intent guidance:
- data ingestion/collection normally maps first to data_governance, not
  human_oversight or quality_management.
- scoring/prediction normally maps to data_governance, transparency, human
  oversight, and accuracy/robustness.
- ranking/prioritisation in a high-impact domain normally maps to human
  oversight, transparency, and accuracy/robustness.
- access controls normally map to cybersecurity/access-control style categories,
  not human oversight.
- rollback/alerts normally map to robustness, risk management, and monitoring.
- preventing a prohibited/sensitive feature is a safeguard/control; do not treat
  it as active use of that feature.
- dataset validation, demographic performance testing, and protected-attribute
  exclusion are controls/safeguards. They may still have remaining governance
  gaps, but they should not be treated as if no control exists.

Use only the obligation category keys listed in the user prompt.

Output JSON schema:
{
  "requirement_intent": "one of the allowed intent values",
  "domain": "short domain/use context or empty string",
  "intended_purpose": "what this requirement says the system should do",
  "system_functions": ["function 1", "function 2"],
  "decision_impact": "what decision/access/safety/monitoring outcome this exact requirement affects",
  "affected_stakeholders": ["stakeholder"],
  "data_types": ["data type"],
  "actors": ["provider", "deployer", "user", "affected person", "other"],
  "lifecycle_stage": "design | development | deployment | use | monitoring | other | unknown",
  "high_risk_context": true,
  "annex_iii_relevance": "possible Annex III area or empty string",
  "primary_obligation_category": "single best category key or empty string",
  "secondary_obligation_categories": ["category_key"],
  "existing_control_categories": ["category_key"],
  "missing_or_unclear_categories": ["category_key"],
  "relevant_obligation_categories": ["category_key"],
  "is_safeguard_or_control": false,
  "safeguards_or_controls": ["control already described by this requirement"],
  "retrieval_query": "one concise semantic search query for finding relevant EU AI Act provisions",
  "confidence": "high | medium | low",
  "notes": "short uncertainty note or empty string"
}

/no_think"""


class RequirementSemanticProfile(BaseModel):
    """Structured meaning extracted from a software requirement."""

    model_config = ConfigDict(extra="ignore")

    requirement_intent: str = "unknown"
    domain: str = ""
    intended_purpose: str = ""
    system_functions: list[str] = Field(default_factory=list)
    decision_impact: str = ""
    affected_stakeholders: list[str] = Field(default_factory=list)
    data_types: list[str] = Field(default_factory=list)
    actors: list[str] = Field(default_factory=list)
    lifecycle_stage: str = "unknown"
    high_risk_context: bool = False
    annex_iii_relevance: str = ""
    primary_obligation_category: str = ""
    secondary_obligation_categories: list[str] = Field(default_factory=list)
    existing_control_categories: list[str] = Field(default_factory=list)
    missing_or_unclear_categories: list[str] = Field(default_factory=list)
    relevant_obligation_categories: list[str] = Field(default_factory=list)
    is_safeguard_or_control: bool = False
    safeguards_or_controls: list[str] = Field(default_factory=list)
    retrieval_query: str = ""
    confidence: str = "medium"
    notes: str = ""

    def priority_categories(self) -> list[str]:
        """Categories to prioritise for retrieval and assessment."""
        ordered = []
        for category in (
            [self.primary_obligation_category]
            + self.missing_or_unclear_categories
            + self.secondary_obligation_categories
        ):
            if category and category not in ordered:
                ordered.append(category)
        return ordered

    def supported_categories(self) -> list[str]:
        """All categories the profile says are meaningfully connected."""
        ordered = []
        for category in (
            self.priority_categories()
            + self.existing_control_categories
            + self.relevant_obligation_categories
        ):
            if category and category not in ordered:
                ordered.append(category)
        return ordered


def _category_keys(categories: list[dict] | None) -> set[str]:
    merged = extend_requirement_categories(categories)
    if not merged:
        return set(DEFAULT_CATEGORY_KEYS)
    keys = {str(category.get("key", "")).strip() for category in merged}
    return {key for key in keys if key}


def _category_listing(categories: list[dict] | None) -> str:
    merged = extend_requirement_categories(categories)
    if not merged:
        return "\n".join(f"- {key}" for key in sorted(DEFAULT_CATEGORY_KEYS))

    lines = []
    for category in sorted(merged, key=lambda item: str(item.get("key", ""))):
        key = category.get("key", "")
        name = category.get("name", key)
        article_ids = ", ".join(category.get("article_ids", []))
        lines.append(f"- {key}: {name} ({article_ids})")
    return "\n".join(lines)


def _intent_listing() -> str:
    return "\n".join(f"- {value}" for value in sorted(INTENT_VALUES))


def normalise_category_key(value: str) -> str:
    return value.strip().lower().replace(" ", "_").replace("-", "_")


def _normalise_category_list(values: list[str], valid: set[str]) -> list[str]:
    normalised = []
    for value in values:
        key = normalise_category_key(str(value))
        if key in valid and key not in normalised:
            normalised.append(key)
    return normalised


def _cosine_similarity(left: list[float], right: list[float]) -> float:
    left_norm = sum(value * value for value in left) ** 0.5
    right_norm = sum(value * value for value in right) ** 0.5
    if not left_norm or not right_norm:
        return 0.0
    return sum(a * b for a, b in zip(left, right)) / (left_norm * right_norm)


@lru_cache(maxsize=1)
def _cached_intent_embeddings() -> tuple[tuple[tuple[str, str], ...], tuple[tuple[float, ...], ...]]:
    """Embed stable intent descriptions once per API process.

    This keeps the semantic-profile step semantic, but removes one repeated
    batch embedding call for every requirement. It is a reusable taxonomy, not
    requirement-ID or keyword matching.
    """
    from eu_ai_risks.embeddings import embed_batch

    intent_items = tuple(INTENT_SEMANTIC_DESCRIPTIONS.items())
    embeddings = embed_batch([description for _, description in intent_items])
    return intent_items, tuple(tuple(vector) for vector in embeddings)


def infer_requirement_intent_semantically(requirement_text: str) -> tuple[str, float, float]:
    """Infer requirement intent by embedding similarity to intent descriptions.

    This is semantic profiling without a profile-generation LLM call. It is
    faster for local Ollama models while still classifying by meaning rather
    than exact keywords. The return value is (best_intent, best_score, margin).
    """
    try:
        from eu_ai_risks.embeddings import embed_text

        intent_items, description_embeddings = _cached_intent_embeddings()
        requirement_embedding = embed_text(requirement_text)

        scored = [
            (intent, _cosine_similarity(requirement_embedding, list(embedding)))
            for (intent, _), embedding in zip(intent_items, description_embeddings)
        ]
        scored.sort(key=lambda item: item[1], reverse=True)
        best_intent, best_score = scored[0]
        second_score = scored[1][1] if len(scored) > 1 else 0.0
        return best_intent, best_score, best_score - second_score
    except Exception:
        return "unknown", 0.0, 0.0


def _merge_policy_categories(profile: RequirementSemanticProfile, valid: set[str]) -> RequirementSemanticProfile:
    policy = INTENT_CATEGORY_POLICY.get(profile.requirement_intent, {})
    if not policy:
        return profile

    primary = policy.get("primary", "")
    if primary and primary in valid:
        # Intent policy wins over broad categories such as quality_management
        # when the exact requirement intent is narrower.
        profile.primary_obligation_category = primary

    def merge(existing: list[str], defaults: list[str]) -> list[str]:
        merged: list[str] = []
        for value in existing + defaults:
            key = normalise_category_key(str(value))
            if key in valid and key not in merged:
                merged.append(key)
        return merged

    profile.secondary_obligation_categories = merge(
        profile.secondary_obligation_categories,
        list(policy.get("secondary", [])),
    )
    profile.existing_control_categories = merge(
        profile.existing_control_categories,
        list(policy.get("existing", [])),
    )
    profile.missing_or_unclear_categories = merge(
        profile.missing_or_unclear_categories,
        list(policy.get("missing", [])),
    )

    if policy.get("safeguard"):
        profile.is_safeguard_or_control = True

    # If the profile is a control/safeguard, do not remove all missing
    # categories. A control can still have a specific gap (for example, human
    # review exists but reviewer training/authority is unclear).
    profile.relevant_obligation_categories = profile.supported_categories()
    return profile




def _contains_any(text: str, patterns: tuple[str, ...]) -> bool:
    import re

    return any(re.search(pattern, text, re.I) for pattern in patterns)


def _looks_like_prevention_or_exclusion(text: str) -> bool:
    """Detect requirements that prohibit/prevent a sensitive practice.

    These should be treated as safeguards, not as active prohibited-practice
    use. Keep this deliberately conservative: it only fires where the sentence
    clearly says the system must not use, must prevent, block, reject, disable or
    exclude the practice/data.
    """
    return _contains_any(text, (
        r"\bshall not\b",
        r"\bmust not\b",
        r"\bwill not\b",
        r"\bprevent(s|ed|ing)?\b",
        r"\bblock(s|ed|ing)?\b",
        r"\breject(s|ed|ing)?\b",
        r"\bdisable(s|d)?\b",
        r"\bexclude(s|d)?\b",
        r"\bprohibit(s|ed|ing)?\b",
    ))


def _append_unique(values: list[str], *items: str) -> list[str]:
    result = list(values)
    for item in items:
        key = normalise_category_key(item)
        if key and key not in result:
            result.append(key)
    return result


def _route_profile_to_categories(
    profile: RequirementSemanticProfile,
    *,
    intent: str | None = None,
    primary: str | None = None,
    secondary: tuple[str, ...] = (),
    missing: tuple[str, ...] = (),
    existing: tuple[str, ...] = (),
    safeguard: bool | None = None,
    note: str = "",
) -> None:
    """Apply a high-confidence regulatory route to a profile in-place."""
    if intent:
        profile.requirement_intent = intent
    if primary:
        profile.primary_obligation_category = normalise_category_key(primary)
    if secondary:
        profile.secondary_obligation_categories = _append_unique(
            profile.secondary_obligation_categories, *secondary,
        )
    if missing:
        profile.missing_or_unclear_categories = _append_unique(
            profile.missing_or_unclear_categories, *missing,
        )
    if existing:
        profile.existing_control_categories = _append_unique(
            profile.existing_control_categories, *existing,
        )
    if safeguard is not None:
        profile.is_safeguard_or_control = safeguard
    if note:
        profile.notes = f"{profile.notes}; {note}".strip("; ")


def apply_regulatory_scope_guardrails(
    requirement_text: str,
    profile: RequirementSemanticProfile,
    categories: list[dict] | None,
) -> RequirementSemanticProfile:
    """Improve routing for non-Chapter-III modules using conservative signals.

    Embedding similarity is good for ordinary software intents, but some EU AI
    Act areas need high-precision legal routing. This pass adds deterministic
    guardrails for the Act areas we explicitly support beyond the existing
    Chapter III implementation: Article 5, Article 50, Annex III, Annex IV, and
    Articles 72-73. The guardrails affect retrieval/reranking only; the final
    output remains an engineering review finding, not a legal conclusion.
    """
    text = requirement_text.lower()
    valid = _category_keys(categories)
    prevention = _looks_like_prevention_or_exclusion(text)

    prohibited_active_patterns = (
        r"\bsocial scoring\b|\bsocial score\b|\bscore citizens\b",
        r"\bmanipulat\w*\b|\bsubliminal\b|\bdeceptive technique",
        r"\bexploit\w*\b.*\b(vulnerab|age|disab|social|economic)",
        r"\bbiometric categorisation\b.*\b(race|ethnic|political|religio|belief|sex life|sexual orientation|trade union)",
        r"\bemotion recognition\b.*\b(workplace|worker|employee|school|student|education|classroom)",
        r"\buntargeted\b.*\b(facial|face)\b.*\b(scrap|database|recognition)",
        r"\b(facial|face)\b.*\b(scrap|database)\b.*\b(recognition|identification)",
        r"\bpredictive policing\b|\bpredict\b.*\b(crime|criminal offence|offense)\b.*\b(person|individual)",
        r"\breal[- ]time remote biometric identification\b",
    )
    if _contains_any(text, prohibited_active_patterns):
        if prevention:
            _route_profile_to_categories(
                profile,
                intent="prohibited_feature_prevention",
                primary="prohibited_practice",
                existing=("prohibited_practice",),
                safeguard=True,
                note="regulatory guardrail: requirement appears to prevent a prohibited/sensitive practice",
            )
            if "prevention or exclusion of prohibited/sensitive AI practice" not in profile.safeguards_or_controls:
                profile.safeguards_or_controls.append(
                    "prevention or exclusion of prohibited/sensitive AI practice"
                )
        else:
            _route_profile_to_categories(
                profile,
                intent="prohibited_practice_use",
                primary="prohibited_practice",
                missing=("prohibited_practice",),
                safeguard=False,
                note="regulatory guardrail: potential Article 5 prohibited-practice review",
            )

    # Article 50 transparency obligations.
    if _contains_any(text, (
        r"\b(chatbot|virtual assistant|conversational ai|ai assistant)\b",
        r"\binteracting with (an )?ai\b|\busing ai\b.*\binform\b|\bdisclose\b.*\bai system\b",
    )):
        _route_profile_to_categories(
            profile,
            intent="ai_interaction_disclosure",
            primary="ai_interaction_disclosure",
            secondary=("general_transparency",),
            missing=("ai_interaction_disclosure",),
            note="regulatory guardrail: AI interaction disclosure route",
        )

    if _contains_any(text, (
        r"\bsynthetic\b.*\b(text|content|audio|image|video)\b",
        r"\b(ai[- ]generated|machine[- ]generated|generated by ai)\b",
        r"\bwatermark\b|\blabel\b.*\b(ai[- ]generated|synthetic)\b|\bmark\b.*\bsynthetic\b",
    )):
        _route_profile_to_categories(
            profile,
            intent="synthetic_content_generation",
            primary="synthetic_content_labelling",
            secondary=("general_transparency",),
            missing=("synthetic_content_labelling",),
            note="regulatory guardrail: synthetic-content labelling route",
        )

    if _contains_any(text, (r"\bdeepfake\b", r"\bmanipulat\w*\b.*\b(image|audio|video)\b.*\b(person|event|real)")):
        _route_profile_to_categories(
            profile,
            intent="deepfake_generation",
            primary="deepfake_disclosure",
            secondary=("synthetic_content_labelling", "general_transparency"),
            missing=("deepfake_disclosure",),
            note="regulatory guardrail: deepfake-disclosure route",
        )

    if _contains_any(text, (
        r"\bemotion recognition\b",
        r"\bbiometric categorisation\b",
    )) and not prevention:
        _route_profile_to_categories(
            profile,
            intent="biometric_emotion_disclosure",
            primary=(profile.primary_obligation_category or "biometric_emotion_disclosure"),
            secondary=("biometric_emotion_disclosure", "general_transparency"),
            missing=("biometric_emotion_disclosure",),
            note="regulatory guardrail: biometric/emotion-recognition notice route",
        )

    # Annex III + Article 6 high-risk classification signals.
    annex_domain_patterns = (
        r"\b(recruit|candidate|resume|cv|hiring|employment|worker|employee|promotion|termination|task allocation|performance monitoring)\b",
        r"\b(education|student|exam|admission|grading|vocational training|learning outcome)\b",
        r"\b(credit score|creditworthiness|loan|insurance premium|public benefit|social benefit|essential service|emergency dispatch)\b",
        r"\b(law enforcement|police|criminal|crime|evidence|offender|victim|witness|polygraph)\b",
        r"\b(migration|asylum|border|visa|residence permit)\b",
        r"\b(critical infrastructure|electricity|water supply|gas|heating|road traffic|digital infrastructure)\b",
        r"\b(judicial|court|judge|legal decision|election|voting|democratic process)\b",
        r"\b(remote biometric identification|biometric identification)\b",
    )
    if _contains_any(text, annex_domain_patterns):
        # Do not overwrite a more specific Article 5/50 route, but keep Annex
        # III classification as a secondary mapped area.
        if not profile.primary_obligation_category:
            profile.primary_obligation_category = "high_risk_classification"
        profile.secondary_obligation_categories = _append_unique(
            profile.secondary_obligation_categories,
            "high_risk_classification",
            "annex_iii_high_risk_domain",
        )
        profile.missing_or_unclear_categories = _append_unique(
            profile.missing_or_unclear_categories,
            "high_risk_classification",
        )
        profile.high_risk_context = True
        if not profile.annex_iii_relevance:
            profile.annex_iii_relevance = "possible Annex III high-risk domain"
        profile.notes = (
            f"{profile.notes}; regulatory guardrail: possible Article 6/Annex III high-risk classification context"
        ).strip("; ")

    # Annex IV technical documentation detail.
    if _contains_any(text, (
        r"\btechnical documentation\b|\bcompliance documentation\b|\bdesign documentation\b",
        r"\bintended purpose\b.*\bdocument",
        r"\b(model architecture|training data|validation data|testing data|performance metric|risk control)\b.*\bdocument",
    )):
        _route_profile_to_categories(
            profile,
            intent="annex_iv_documentation",
            primary="annex_iv_technical_documentation",
            secondary=("technical_documentation",),
            missing=("annex_iv_technical_documentation", "technical_documentation"),
            existing=("annex_iv_technical_documentation",),
            safeguard=True,
            note="regulatory guardrail: Annex IV technical-documentation route",
        )

    # Chapter IX lifecycle obligations.
    if _contains_any(text, (
        r"\bpost[- ]market\b",
        r"\bmonitor\w*\b.*\b(deployed|production|live|lifetime|after release|post deployment)\b",
        r"\b(drift|performance degradation|ongoing performance|continuous compliance)\b",
    )):
        _route_profile_to_categories(
            profile,
            intent="post_market_monitoring",
            primary="post_market_monitoring",
            secondary=("risk_management", "technical_documentation"),
            missing=("post_market_monitoring",),
            existing=("post_market_monitoring",),
            safeguard=True,
            note="regulatory guardrail: Article 72 post-market-monitoring route",
        )

    if _contains_any(text, (
        r"\bserious incident\b|\bincident reporting\b|\breport\w*\b.*\b(authorit|regulator|market surveillance)\b",
        r"\b(fundamental rights|death|serious harm|health and safety)\b.*\bincident\b",
    )):
        _route_profile_to_categories(
            profile,
            intent="serious_incident_reporting",
            primary="serious_incident_reporting",
            secondary=("post_market_monitoring", "risk_management"),
            missing=("serious_incident_reporting",),
            existing=("serious_incident_reporting",),
            safeguard=True,
            note="regulatory guardrail: Article 73 serious-incident-reporting route",
        )

    if _contains_any(text, (
        r"\b(ai literacy|training|trained users|trained operators|staff competence|operator competence)\b",
        r"\bunderstand\b.*\b(capabilities|limitations|risks)\b",
    )):
        _route_profile_to_categories(
            profile,
            intent="ai_literacy_training",
            primary=(profile.primary_obligation_category or "ai_literacy"),
            secondary=("ai_literacy",),
            missing=("ai_literacy",),
            existing=("ai_literacy",),
            safeguard=True,
            note="regulatory guardrail: Article 4 AI-literacy route",
        )

    # Remove categories that are not valid in this runtime. This keeps the
    # profile compatible with older graphs while extend_requirement_categories
    # supplies the new anchors at runtime.
    profile.primary_obligation_category = (
        profile.primary_obligation_category
        if normalise_category_key(profile.primary_obligation_category) in valid
        else ""
    )
    profile.secondary_obligation_categories = _normalise_category_list(
        profile.secondary_obligation_categories, valid,
    )
    profile.existing_control_categories = _normalise_category_list(
        profile.existing_control_categories, valid,
    )
    profile.missing_or_unclear_categories = _normalise_category_list(
        profile.missing_or_unclear_categories, valid,
    )
    profile.relevant_obligation_categories = profile.supported_categories()
    return _merge_policy_categories(profile, valid)


def stabilise_profile_with_semantic_intent(
    requirement_text: str,
    profile: RequirementSemanticProfile,
    categories: list[dict] | None,
) -> RequirementSemanticProfile:
    """Stabilise the LLM profile using embedding-based intent similarity.

    The risk assessor should be robust to one bad profiling call. We therefore
    compare the requirement to a small set of stable intent descriptions and
    use the result to choose a maintainable intent policy. This avoids
    requirement-specific keyword patches while fixing category drift such as
    simple data ingestion becoming a human-oversight issue.
    """
    valid = _category_keys(categories)
    inferred_intent, score, margin = infer_requirement_intent_semantically(
        requirement_text,
    )

    current_intent = profile.requirement_intent
    should_override = False
    if current_intent in {"unknown", "other"}:
        should_override = inferred_intent not in {"unknown", "other"}
    elif inferred_intent not in {"unknown", current_intent}:
        # Strong semantic evidence can override the LLM profile. Also allow a
        # narrower non-human intent to override accidental human_oversight drift.
        should_override = (
            (score >= 0.46 and margin >= 0.025)
            or (
                current_intent == "human_review_or_override"
                and inferred_intent in {
                    "data_ingestion",
                    "access_control_or_security",
                    "logging_or_audit",
                    "rollback_or_corrective_action",
                    "prohibited_feature_prevention",
                    "data_validation_or_bias_testing",
                    "protected_attribute_control",
                }
                and score >= 0.38
            )
        )

    if should_override:
        previous = profile.requirement_intent
        profile.requirement_intent = inferred_intent
        note = (
            f"intent stabilised from {previous} to {inferred_intent} "
            f"using semantic similarity (score={score:.3f}, margin={margin:.3f})"
        )
        profile.notes = f"{profile.notes}; {note}".strip("; ")

    return _merge_policy_categories(profile, valid)


def _normalise_profile_categories(
    profile: RequirementSemanticProfile,
    categories: list[dict] | None,
) -> RequirementSemanticProfile:
    valid = _category_keys(categories)

    primary = normalise_category_key(profile.primary_obligation_category)
    profile.primary_obligation_category = primary if primary in valid else ""

    profile.secondary_obligation_categories = _normalise_category_list(
        profile.secondary_obligation_categories, valid,
    )
    profile.existing_control_categories = _normalise_category_list(
        profile.existing_control_categories, valid,
    )
    profile.missing_or_unclear_categories = _normalise_category_list(
        profile.missing_or_unclear_categories, valid,
    )
    profile.relevant_obligation_categories = _normalise_category_list(
        profile.relevant_obligation_categories, valid,
    )

    intent = profile.requirement_intent.strip().lower().replace(" ", "_")
    profile.requirement_intent = intent if intent in INTENT_VALUES else "unknown"

    # Keep relevant categories consistent with the newer, stricter fields.
    merged = profile.supported_categories()
    profile.relevant_obligation_categories = merged
    return profile


def _unwrap_profile_payload(raw: dict | list) -> dict:
    if isinstance(raw, dict):
        for key in ("profile", "requirement_profile", "answer", "result", "data"):
            nested = raw.get(key)
            if isinstance(nested, dict):
                return nested
        return raw
    return {"notes": str(raw)}


def build_embedding_semantic_profile(
    requirement_id: str,
    requirement_text: str,
    categories: list[dict] | None = None,
) -> RequirementSemanticProfile:
    """Build a semantic profile using embeddings rather than an LLM call.

    This is the default path for local demo/API use because it reduces the
    pipeline from two LLM calls per requirement to one. It still uses semantic
    similarity over stable intent/domain descriptions, then applies the same
    obligation-category policy used by the full risk assessor.
    """
    intent, score, margin = infer_requirement_intent_semantically(
        requirement_text)
    domain, domain_score = infer_high_risk_context_semantically(
        requirement_text)

    confidence = "low"
    if score >= PROFILE_CONFIDENCE_SCORE and margin >= PROFILE_CONFIDENCE_MARGIN:
        confidence = "medium"
    if score >= PROFILE_CONFIDENCE_SCORE + 0.06 and margin >= PROFILE_CONFIDENCE_MARGIN + 0.02:
        confidence = "high"

    annex_relevance = ""
    high_risk_context = False
    if domain and domain_score >= 0.32:
        high_risk_context = True
        annex_relevance = domain.replace("_", " ")

    profile = RequirementSemanticProfile(
        requirement_intent=intent,
        domain=annex_relevance,
        intended_purpose=requirement_text,
        system_functions=[intent.replace("_", " ")] if intent not in {
            "unknown", "other"} else [],
        high_risk_context=high_risk_context,
        annex_iii_relevance=annex_relevance,
        retrieval_query=requirement_text,
        confidence=confidence,
        notes=(
            f"embedding semantic profile: intent={intent} "
            f"score={score:.3f}, margin={margin:.3f}, domain_score={domain_score:.3f}"
        ),
    )
    profile = _merge_policy_categories(profile, _category_keys(categories))
    profile = apply_regulatory_scope_guardrails(
        requirement_text, profile, categories,
    )
    profile.retrieval_query = build_profile_retrieval_query(
        profile, requirement_text)
    return profile


def extract_requirement_profile(
    requirement_id: str,
    requirement_text: str,
    categories: list[dict] | None = None,
) -> RequirementSemanticProfile:
    """Extract a semantic profile for one requirement.

    Default mode is embedding-based semantic profiling to reduce local Ollama
    latency. Set EU_AI_RISKS_PROFILE_MODE=llm for the older two-call pipeline,
    or hybrid to use embeddings first and only call the LLM when confidence is
    low.
    """
    embedding_profile = build_embedding_semantic_profile(
        requirement_id, requirement_text, categories,
    )

    if PROFILE_MODE in {"semantic", "embedding", "embedding_only"}:
        return embedding_profile
    if PROFILE_MODE == "hybrid" and embedding_profile.confidence in {"medium", "high"}:
        return embedding_profile

    prompt = f"""\
## Requirement
ID: {requirement_id}
Text: {requirement_text}

## Allowed requirement intent values
{_intent_listing()}

## Allowed obligation category keys
{_category_listing(categories)}

Extract the semantic profile for this requirement.
"""

    try:
        raw = complete_json(
            prompt=prompt,
            system=REQUIREMENT_PROFILE_PROMPT,
            max_tokens=PROFILE_MAX_TOKENS,
        )
        payload = _unwrap_profile_payload(raw)
        profile = RequirementSemanticProfile.model_validate(payload)
        profile = _normalise_profile_categories(profile, categories)
        profile = stabilise_profile_with_semantic_intent(
            requirement_text, profile, categories,
        )
        profile = apply_regulatory_scope_guardrails(
            requirement_text, profile, categories,
        )
        if not profile.retrieval_query:
            profile.retrieval_query = build_profile_retrieval_query(
                profile, requirement_text,
            )
        return profile
    except Exception as exc:  # keep assessment robust if profiling fails
        # Fallback remains semantic: it uses embedding intent classification, not
        # keyword or requirement-ID matching. Preserve the error in notes.
        embedding_profile.notes = f"{embedding_profile.notes}; LLM profile skipped/failed: {str(exc)[:160]}"
        return embedding_profile


def build_profile_retrieval_query(
    profile: RequirementSemanticProfile,
    requirement_text: str,
) -> str:
    """Build a semantic retrieval query from profile fields.

    The query is based on the structured meaning extracted by the LLM. It avoids
    maintaining a manual keyword list while keeping retrieval anchored to the
    specific requirement intent and primary obligation category.
    """
    parts = [requirement_text]

    for value in (
        profile.requirement_intent,
        profile.primary_obligation_category,
        profile.domain,
        profile.intended_purpose,
        profile.decision_impact,
        profile.annex_iii_relevance,
        profile.lifecycle_stage,
    ):
        if value and value not in {"unknown", "other"}:
            parts.append(value)

    parts.extend(profile.system_functions)
    parts.extend(profile.affected_stakeholders)
    parts.extend(profile.data_types)
    parts.extend(profile.actors)
    parts.extend(profile.missing_or_unclear_categories)
    parts.extend(profile.secondary_obligation_categories)
    parts.extend(profile.existing_control_categories)

    if profile.is_safeguard_or_control and profile.safeguards_or_controls:
        parts.append(
            "existing control or safeguard with remaining compliance gap")

    supported = set(profile.supported_categories())
    if "prohibited_practice" in supported:
        parts.append("EU AI Act Article 5 prohibited AI practices")
    if {"high_risk_classification", "annex_iii_high_risk_domain"} & supported:
        parts.append("EU AI Act Article 6 and Annex III high-risk AI system classification")
    if {
        "general_transparency",
        "ai_interaction_disclosure",
        "synthetic_content_labelling",
        "deepfake_disclosure",
        "biometric_emotion_disclosure",
    } & supported:
        parts.append("EU AI Act Article 50 transparency obligations")
    if "annex_iv_technical_documentation" in supported:
        parts.append("EU AI Act Annex IV technical documentation contents")
    if {"post_market_monitoring", "serious_incident_reporting"} & supported:
        parts.append("EU AI Act Articles 72 and 73 post-market monitoring and serious incident reporting")
    parts.append("EU AI Act software system compliance obligations")
    return "; ".join(dict.fromkeys(p.strip() for p in parts if p and p.strip()))


def _article_ids_for_categories(
    category_keys: list[str],
    categories: list[dict] | None,
) -> list[str]:
    merged = extend_requirement_categories(categories)
    if not merged:
        return []

    by_key = {
        str(category.get("key", "")): category.get("article_ids", [])
        for category in merged
    }

    article_ids: list[str] = []
    for category_key in category_keys:
        article_ids.extend(by_key.get(category_key, []))
    return list(dict.fromkeys(article_ids))


def article_ids_for_profile_categories(
    profile: RequirementSemanticProfile,
    categories: list[dict] | None,
) -> list[str]:
    """Return graph article IDs anchored to the profile's priority categories."""
    article_ids = _article_ids_for_categories(
        profile.priority_categories(), categories,
    )

    # Article 6 is the high-risk classification anchor. Add it only when the
    # profile says the exact requirement contributes to high-risk context.
    if profile.high_risk_context:
        article_ids.insert(0, "art:6")

    return list(dict.fromkeys(article_ids))


def rerank_paragraphs_by_profile(
    paragraphs: list[dict],
    profile: RequirementSemanticProfile,
    categories: list[dict] | None,
    limit: int,
) -> list[dict]:
    """Rerank vector results using semantic profile + graph metadata.

    This is not keyword matching. It uses:
    - the LLM-extracted primary/secondary/missing obligation categories;
    - the graph's RequirementCategory article anchors;
    - chapter/obligation metadata already stored on graph results.
    """
    primary_articles = set(_article_ids_for_categories(
        [profile.primary_obligation_category], categories,
    ))
    missing_articles = set(_article_ids_for_categories(
        profile.missing_or_unclear_categories, categories,
    ))
    secondary_articles = set(_article_ids_for_categories(
        profile.secondary_obligation_categories, categories,
    ))
    existing_control_articles = set(_article_ids_for_categories(
        profile.existing_control_categories, categories,
    ))
    priority_articles = (
        primary_articles | missing_articles | secondary_articles
        | {"art:6" if profile.high_risk_context else ""}
    )

    ranked: list[dict] = []
    for paragraph in paragraphs:
        score = float(paragraph.get("score", 0.0))
        article_id = paragraph.get("article_id", "")
        chapter_id = paragraph.get("chapter_id", "")
        obligation_type = paragraph.get("obligation_type", "")

        # The original vector score remains dominant. These boosts express the
        # semantic profile's structured interpretation.
        if article_id in primary_articles:
            score += 0.18
        if article_id in missing_articles:
            score += 0.14
        if article_id in secondary_articles:
            score += 0.08
        if article_id in existing_control_articles:
            score += 0.04
        if profile.high_risk_context and chapter_id == "ch:III":
            score += 0.03
        if obligation_type in {"requirement", "prohibition"}:
            score += 0.02

        # Lightly prefer profile-supported articles when candidates tie. Do not
        # remove other articles: Article 5/72/73 can still be relevant when the
        # semantic query retrieves them strongly.
        if priority_articles and article_id not in priority_articles:
            score -= 0.015

        updated = dict(paragraph)
        updated["adjusted_score"] = round(score, 4)
        ranked.append(updated)

    ranked.sort(
        key=lambda item: item.get("adjusted_score", item.get("score", 0)),
        reverse=True,
    )
    return ranked[:limit]


def format_semantic_profile(profile: RequirementSemanticProfile) -> str:
    """Format the profile for inclusion in the risk-assessment prompt."""
    lines = ["## Requirement semantic profile"]
    lines.append(f"- Requirement intent: {profile.requirement_intent}")
    lines.append(f"- Domain/use context: {profile.domain or 'not explicit'}")
    lines.append(
        f"- Intended purpose: {profile.intended_purpose or 'not explicit'}")
    lines.append(
        "- System functions: "
        + (", ".join(profile.system_functions) or "not explicit")
    )
    lines.append(
        "- Decision impact: " + (profile.decision_impact or "not explicit")
    )
    lines.append(
        "- Affected stakeholders: "
        + (", ".join(profile.affected_stakeholders) or "not explicit")
    )
    lines.append(
        "- Data types: " + (", ".join(profile.data_types) or "not explicit")
    )
    lines.append("- Actors: " + (", ".join(profile.actors) or "not explicit"))
    lines.append(f"- Lifecycle stage: {profile.lifecycle_stage or 'unknown'}")
    lines.append(
        f"- Possible high-risk context: {'yes' if profile.high_risk_context else 'no'}"
    )
    lines.append(
        "- Annex III relevance: " +
        (profile.annex_iii_relevance or "not explicit")
    )
    lines.append(
        "- Primary obligation category: "
        + (profile.primary_obligation_category or "none explicit")
    )
    lines.append(
        "- Secondary obligation categories: "
        + (", ".join(profile.secondary_obligation_categories) or "none explicit")
    )
    lines.append(
        "- Existing control categories: "
        + (", ".join(profile.existing_control_categories) or "none explicit")
    )
    lines.append(
        "- Missing/unclear categories: "
        + (", ".join(profile.missing_or_unclear_categories) or "none explicit")
    )
    lines.append(
        "- Safeguard/control already present: "
        + ("yes" if profile.is_safeguard_or_control else "no")
    )
    lines.append(
        "- Safeguards/controls described: "
        + (", ".join(profile.safeguards_or_controls) or "none explicit")
    )
    lines.append(f"- Profile confidence: {profile.confidence}")
    if profile.notes:
        lines.append(f"- Notes: {profile.notes}")

    lines.append(
        "Assessment rule: evaluate the exact requirement intent first. Use the "
        "primary and missing/unclear categories as the main assessment scope. "
        "Treat existing control categories as controls or partial mitigations, "
        "not as missing risks unless the remaining gap is specific."
    )
    return "\n".join(lines)

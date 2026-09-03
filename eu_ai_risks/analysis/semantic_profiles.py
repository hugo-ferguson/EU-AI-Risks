"""
Semantic profiling helpers for requirement-to-EU-AI-Act risk assessment.

This module avoids maintaining large keyword lists. It asks the LLM to convert
one software requirement into a structured semantic profile, then uses that
profile to retrieve and rerank relevant EU AI Act provisions.

The intent-aware version is stricter than the initial semantic-profile layer:
- it profiles the exact requirement rather than the whole SRS;
- it separates requirement intent, primary obligation category, secondary
  categories, existing controls, and remaining gaps;
- it avoids treating every high-risk requirement as a human-oversight issue.
"""

from __future__ import annotations

import os
from functools import lru_cache

from pydantic import BaseModel, ConfigDict, Field

from eu_ai_risks.llm import complete_json

PROFILE_MAX_TOKENS = int(os.environ.get("EU_AI_RISKS_PROFILE_MAX_TOKENS", "700"))
PROFILE_MODE = os.environ.get("EU_AI_RISKS_PROFILE_MODE", "semantic").strip().lower()
PROFILE_CONFIDENCE_SCORE = float(os.environ.get("EU_AI_RISKS_PROFILE_CONFIDENCE_SCORE", "0.38"))
PROFILE_CONFIDENCE_MARGIN = float(os.environ.get("EU_AI_RISKS_PROFILE_CONFIDENCE_MARGIN", "0.012"))

DEFAULT_CATEGORY_KEYS = {
    "ai_literacy",
    "risk_management",
    "data_governance",
    "technical_documentation",
    "record_keeping",
    "transparency",
    "human_oversight",
    "accuracy_robustness_cybersecurity",
    "quality_management",
    "fundamental_rights_impact_assessment",
    "conformity_assessment",
    "registration",
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
    "data_validation_or_bias_testing",
    "protected_attribute_control",
    "technical_documentation",
    "risk_management_process",
    "other",
    "unknown",
}

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
}

HIGH_RISK_DOMAIN_DESCRIPTIONS = {
    "employment_recruitment": "AI system used for recruitment, candidate screening, employment decisions, worker management, hiring, selection or promotion",
    "education_training": "AI system used for access to education, assessment, grading, admissions, learning evaluation or vocational training",
    "healthcare_safety": "AI system used in health, medical triage, safety-critical decisions, patient support or clinical assessment",
    "public_services": "AI system used for public assistance, social benefits, essential private services, credit, insurance or access to services",
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
    if not categories:
        return set(DEFAULT_CATEGORY_KEYS)
    keys = {str(category.get("key", "")).strip() for category in categories}
    return {key for key in keys if key}


def _category_listing(categories: list[dict] | None) -> str:
    if not categories:
        return "\n".join(f"- {key}" for key in sorted(DEFAULT_CATEGORY_KEYS))

    lines = []
    for category in categories:
        key = category.get("key", "")
        name = category.get("name", key)
        article_ids = ", ".join(category.get("article_ids", []))
        lines.append(f"- {key}: {name} ({article_ids})")
    return "\n".join(lines)


def _intent_listing() -> str:
    return "\n".join(f"- {value}" for value in sorted(INTENT_VALUES))


def _normalise_category_key(value: str) -> str:
    return value.strip().lower().replace(" ", "_").replace("-", "_")


def _normalise_category_list(values: list[str], valid: set[str]) -> list[str]:
    normalised = []
    for value in values:
        key = _normalise_category_key(str(value))
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
            key = _normalise_category_key(str(value))
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

    primary = _normalise_category_key(profile.primary_obligation_category)
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


def fallback_requirement_profile(
    requirement_text: str,
    reason: str = "Semantic profile extraction failed.",
) -> RequirementSemanticProfile:
    """Return a safe profile that preserves the original requirement text."""
    return RequirementSemanticProfile(
        intended_purpose=requirement_text,
        retrieval_query=requirement_text,
        confidence="low",
        notes=reason,
    )


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
    intent, score, margin = infer_requirement_intent_semantically(requirement_text)
    domain, domain_score = infer_high_risk_context_semantically(requirement_text)

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
        system_functions=[intent.replace("_", " ")] if intent not in {"unknown", "other"} else [],
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
    if not profile.retrieval_query:
        profile.retrieval_query = build_profile_retrieval_query(profile, requirement_text)
    else:
        profile.retrieval_query = build_profile_retrieval_query(profile, requirement_text)
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
        parts.append("existing control or safeguard with remaining compliance gap")

    parts.append("EU AI Act high-risk AI system obligations")
    return "; ".join(dict.fromkeys(p.strip() for p in parts if p and p.strip()))


def _article_ids_for_categories(
    category_keys: list[str],
    categories: list[dict] | None,
) -> list[str]:
    if not categories:
        return []

    by_key = {
        str(category.get("key", "")): category.get("article_ids", [])
        for category in categories
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
    lines.append(f"- Intended purpose: {profile.intended_purpose or 'not explicit'}")
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
        "- Annex III relevance: " + (profile.annex_iii_relevance or "not explicit")
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

"""
Deterministic risk assessment pipeline.

Pre-fetches context from the Neo4j knowledge graph, builds a semantic
profile for each requirement, then uses a single LLM call per requirement
to synthesise a risk assessment.
"""

from functools import lru_cache

from eu_ai_risks.analysis.models import RequirementRisk, RiskItem
from eu_ai_risks.analysis.prompts import RISK_ASSESSMENT_PROMPT
from eu_ai_risks.analysis.semantic_profiles import (
    article_ids_for_profile_categories,
    build_profile_retrieval_query,
    extract_requirement_profile,
    format_semantic_profile,
    rerank_paragraphs_by_profile,
    RequirementSemanticProfile,
)
from eu_ai_risks.db.graph import (
    find_paragraphs, list_categories, get_article,
    get_references, get_related_requirements,
)
from eu_ai_risks.embeddings import embed_text
from eu_ai_risks.llm import complete_json

TOP_K_PARAGRAPH_CANDIDATES = 8
TOP_K_PARAGRAPHS = 3
TOP_K_ARTICLES = 3
MAX_PARAGRAPHS_PER_ARTICLE = 2
MAX_CROSS_REFERENCES = 2
MAX_RELATED_REQUIREMENTS = 1
MAX_SHARED_ENTITIES = 3
MAX_TOKENS = 2048

# Intents that represent existing safeguards; cap their severity
LOW_RISK_CONTROL_INTENTS = {
    "logging_or_audit",
    "prohibited_feature_prevention",
    "data_validation_or_bias_testing",
    "protected_attribute_control",
    "monitoring_or_alerting",
    "rollback_or_corrective_action",
}

MEDIUM_MAX_CONTROL_INTENTS = {
    "human_review_or_override",
    "access_control_or_security",
}

# Fallback article anchors per category when the LLM returns no risks
# but the profile says an obligation gap remains
CATEGORY_FALLBACK_RISKS = {
    "risk_management": {
        "article_id": "art:9",
        "paragraph_num": 1,
        "provision": "Article 9(1)",
        "description": "Risk management expectations not fully specified",
        "action": "Add risk identification, mitigation, and review criteria.",
    },
    "data_governance": {
        "article_id": "art:10",
        "paragraph_num": 2,
        "provision": "Article 10(2)",
        "description": "Data governance expectations not fully specified",
        "action": "Define data source, quality, bias, and validation checks.",
    },
    "technical_documentation": {
        "article_id": "art:11",
        "paragraph_num": 1,
        "provision": "Article 11(1)",
        "description": "Technical documentation expectations not fully specified",
        "action": "Document design decisions, evidence, and compliance rationale.",
    },
    "record_keeping": {
        "article_id": "art:12",
        "paragraph_num": 1,
        "provision": "Article 12(1)",
        "description": "Record-keeping expectations not fully specified",
        "action": "Specify log fields, retention, access controls, and audit review.",
    },
    "transparency": {
        "article_id": "art:13",
        "paragraph_num": 1,
        "provision": "Article 13(1)",
        "description": "Transparency expectations not fully specified",
        "action": "Define explanation detail, user information, and instructions for use.",
    },
    "human_oversight": {
        "article_id": "art:14",
        "paragraph_num": 1,
        "provision": "Article 14(1)",
        "description": "Human oversight expectations not fully specified",
        "action": "Define reviewer authority, training, escalation, and monitoring.",
    },
    "accuracy_robustness_cybersecurity": {
        "article_id": "art:15",
        "paragraph_num": 1,
        "provision": "Article 15(1)",
        "description": "Accuracy, robustness, or cybersecurity expectations not fully specified",
        "action": "Add performance, robustness, security, and failure-handling criteria.",
    },
    "quality_management": {
        "article_id": "art:17",
        "paragraph_num": 1,
        "provision": "Article 17(1)",
        "description": "Quality management expectations not fully specified",
        "action": "Record the relevant quality-management procedure and owner.",
    },
    "post_market_monitoring": {
        "article_id": "art:72",
        "paragraph_num": 1,
        "provision": "Article 72(1)",
        "description": "Post-market monitoring expectations not fully specified",
        "action": "Define monitoring metrics, thresholds, review cadence, and corrective actions.",
    },
}

CATEGORY_ANCHORS = {
    key: (value["article_id"], value["paragraph_num"], value["provision"])
    for key, value in CATEGORY_FALLBACK_RISKS.items()
}

# Core Chapter 3 articles that can always be cited even if not pre-fetched
CORE_ARTICLE_IDS = {
    "art:9", "art:10", "art:11", "art:12", "art:13",
    "art:14", "art:15", "art:72",
}


@lru_cache(maxsize=128)
def _cached_article(article_id: str) -> dict:
    return get_article(article_id) or {}


@lru_cache(maxsize=128)
def _cached_references(article_id: str) -> dict:
    return get_references(article_id) or {}


def _normalise_category(value: str) -> str:
    return value.strip().lower().replace(" ", "_").replace("-", "_")


def _build_prompt(
    requirement_id: str,
    requirement_text: str,
    paragraphs: list[dict],
    articles: dict[str, dict],
    referenced_articles: set[tuple[str, str]],
    related_requirements: list[dict],
    categories: list[dict],
    semantic_profile_text: str = "",
) -> str:
    parts = [
        f"## Requirement {requirement_id}\n",
        f"{requirement_text}\n",
    ]

    if semantic_profile_text:
        parts.extend(["\n", semantic_profile_text, "\n"])

    parts.append("\n## Matching provisions (semantic retrieval + vector search)\n")
    for paragraph in paragraphs:
        adjusted = paragraph.get("adjusted_score", paragraph.get("score"))
        parts.append(
            f"- **{paragraph['article_id']} "
            f"({paragraph['article_title']})** "
            f"paragraph {paragraph['paragraph_num']} "
            f"[{paragraph['obligation_type']}]: "
            f"{str(paragraph['paragraph_text'])[:320]} "
            f"(score={adjusted})\n"
        )

    if articles:
        parts.append("\n## Key article obligations\n")
        for article_id, article in articles.items():
            parts.append(f"### {article['title']} ({article_id})\n")

            dimensions = article.get("dimensions", {}) or {}
            requirement_categories = dimensions.get("requirement_categories", [])
            if requirement_categories:
                parts.append(
                    f"- Categories: {', '.join(requirement_categories)}\n"
                )

            binding = [
                paragraph for paragraph in article.get("paragraphs", [])
                if paragraph.get("obligation_type") in ("requirement", "prohibition")
            ][:MAX_PARAGRAPHS_PER_ARTICLE]
            for article_paragraph in binding:
                parts.append(
                    f"- ({article_paragraph['num']}) "
                    f"{article_paragraph['text'][:180]}\n"
                )

    if referenced_articles:
        parts.append("\n## Cross-referenced articles\n")
        for reference_id, reference_title in list(referenced_articles)[:MAX_CROSS_REFERENCES]:
            parts.append(f"- {reference_id}: {reference_title}\n")

    if related_requirements:
        parts.append("\n## Related requirements (shared entities)\n")
        for related in related_requirements:
            shared = ", ".join(related["shared_entities"][:MAX_SHARED_ENTITIES])
            parts.append(
                f"- **{related['id']}**: {related['text']} "
                f"(shared: {shared})\n"
            )

    parts.append("\nIdentify the compliance risks for this requirement "
                 "based on the provisions above.")

    return "\n".join(parts)


# -- Post-processing pipeline ------------------------------------------------

def _normalise_risk_provision(risk: RiskItem) -> None:
    """Redirect weak classification articles to the category's anchor."""
    category = _normalise_category(risk.obligation_category)
    anchor = CATEGORY_ANCHORS.get(category)
    if not anchor:
        return

    weak_for_category = {
        "art:6", "art:7", "art:43", "art:74", "art:79",
        "art:81", "art:92", "art:93", "art:112", "art:113",
    }
    if risk.article_id in weak_for_category:
        risk.article_id, risk.paragraph_num, risk.provision = anchor


def _apply_control_severity_policy(
    assessment: RequirementRisk,
    profile: RequirementSemanticProfile,
) -> RequirementRisk:
    """Cap severity for requirements that already describe controls."""
    intent = profile.requirement_intent

    if intent == "prohibited_feature_prevention":
        assessment.risks = []
        assessment.risk_level = "low"
        assessment.summary = (
            "No requirement-level risk retained; the requirement prevents "
            "a sensitive or prohibited feature."
        )
        assessment.recommendations = []
        return assessment

    if intent in LOW_RISK_CONTROL_INTENTS:
        for risk in assessment.risks:
            _normalise_risk_provision(risk)
            if risk.severity in {"high", "medium"}:
                risk.severity = "low"
        if assessment.risks:
            assessment.risk_level = "low"
            assessment.summary = (
                "The requirement describes a control/safeguard. A low "
                "remaining clarification risk is retained for manual review."
            )
        return assessment

    if intent in MEDIUM_MAX_CONTROL_INTENTS or profile.is_safeguard_or_control:
        for risk in assessment.risks:
            _normalise_risk_provision(risk)
            if risk.severity == "high":
                risk.severity = "medium"
        if assessment.risk_level == "high":
            assessment.risk_level = "medium"
        return assessment

    for risk in assessment.risks:
        _normalise_risk_provision(risk)
    return assessment


def _apply_profile_gap_fallback(
    assessment: RequirementRisk,
    profile: RequirementSemanticProfile,
    articles: dict[str, dict],
) -> RequirementRisk:
    """Add a conservative risk when the profile says gaps exist but LLM returned none."""
    if assessment.risks:
        return assessment

    category_order = []
    for category in (
        [profile.primary_obligation_category]
        + profile.missing_or_unclear_categories
        + profile.secondary_obligation_categories
    ):
        key = _normalise_category(category)
        if key and key not in category_order:
            category_order.append(key)

    if not category_order:
        assessment.risk_level = "low"
        return assessment

    # Explicit safeguard with no missing categories: keep low
    if profile.is_safeguard_or_control and not profile.missing_or_unclear_categories:
        assessment.risk_level = "low"
        assessment.summary = (
            "No requirement-level risk retained; the requirement describes "
            "an existing safeguard/control."
        )
        return assessment

    fallback_risks: list[RiskItem] = []
    for category in category_order:
        fallback = CATEGORY_FALLBACK_RISKS.get(category)
        if not fallback:
            continue
        article_id = fallback["article_id"]
        if articles and article_id not in articles and article_id not in CORE_ARTICLE_IDS:
            continue

        severity = "low" if profile.is_safeguard_or_control else "medium"
        fallback_risks.append(RiskItem(
            description=fallback["description"],
            severity=severity,
            article_id=article_id,
            paragraph_num=fallback["paragraph_num"],
            provision=fallback["provision"],
            obligation_category=category,
            engineering_action=fallback["action"],
        ))
        if len(fallback_risks) >= 2:
            break

    if fallback_risks:
        assessment.risks = fallback_risks
        assessment.risk_level = (
            "low" if all(risk.severity == "low" for risk in fallback_risks)
            else "medium"
        )
        categories_text = ", ".join(
            risk.obligation_category for risk in fallback_risks
        )
        assessment.summary = (
            f"Semantic profile indicates a remaining {categories_text} gap. "
            "Conservative risk retained for manual review."
        )
        assessment.recommendations = [
            risk.engineering_action for risk in fallback_risks
            if risk.engineering_action
        ]
    else:
        assessment.risk_level = "low"

    return assessment


def _profile_assessment_scope(
    profile: RequirementSemanticProfile,
) -> set[str]:
    """Categories that should drive the final assessment."""
    scope = {
        _normalise_category(category)
        for category in (
            [profile.primary_obligation_category]
            + profile.missing_or_unclear_categories
            + profile.existing_control_categories
        )
        if category
    }
    return {category for category in scope if category}


def _align_assessment_with_profile(
    assessment: RequirementRisk,
    profile: RequirementSemanticProfile,
) -> RequirementRisk:
    """Remove risks outside the profile's assessment scope."""
    supported = _profile_assessment_scope(profile)
    if not supported:
        supported = {
            _normalise_category(category)
            for category in profile.supported_categories()
        }
    if not supported:
        return assessment

    filtered = [
        risk for risk in assessment.risks
        if not risk.obligation_category
        or _normalise_category(risk.obligation_category) in supported
    ]

    if filtered == assessment.risks:
        return assessment

    assessment.risks = filtered
    if not filtered:
        assessment.risk_level = "low"
        assessment.summary = (
            "No requirement-level risk retained after aligning with "
            "the semantic profile."
        )
        assessment.recommendations = []
    elif assessment.risk_level == "high" and all(
        risk.severity != "high" for risk in filtered
    ):
        assessment.risk_level = "medium"

    return assessment


def _remove_duplicate_risks(assessment: RequirementRisk) -> RequirementRisk:
    seen: set[tuple[str, str, int | None, str]] = set()
    unique: list[RiskItem] = []
    for risk in assessment.risks:
        key = (
            risk.description.strip().lower(),
            risk.article_id,
            risk.paragraph_num,
            _normalise_category(risk.obligation_category),
        )
        if key in seen:
            continue
        seen.add(key)
        unique.append(risk)
    assessment.risks = unique
    return assessment


# -- Main entry point --------------------------------------------------------

def assess_requirement(
    requirement_id: str,
    requirement_text: str,
    categories: list[dict] | None = None,
) -> tuple[RequirementRisk, dict[str, dict], dict | list]:
    """Assess a single requirement against the EU AI Act graph."""
    if categories is None:
        categories = list_categories()

    profile = extract_requirement_profile(
        requirement_id=requirement_id,
        requirement_text=requirement_text,
        categories=categories,
    )
    retrieval_query = build_profile_retrieval_query(profile, requirement_text)
    embedding = embed_text(retrieval_query)

    paragraph_candidates = find_paragraphs(
        embedding, top_k=TOP_K_PARAGRAPH_CANDIDATES,
    )
    paragraphs = rerank_paragraphs_by_profile(
        paragraph_candidates, profile, categories, limit=TOP_K_PARAGRAPHS,
    )

    priority_article_ids = article_ids_for_profile_categories(profile, categories)
    hit_article_ids = list(dict.fromkeys(
        [paragraph["article_id"] for paragraph in paragraphs]
        + priority_article_ids
    ))

    articles = {}
    for article_id in hit_article_ids[:TOP_K_ARTICLES]:
        article = _cached_article(article_id)
        if article:
            articles[article_id] = article

    referenced_articles: set[tuple[str, str]] = set()
    for article_id in hit_article_ids[:TOP_K_ARTICLES]:
        refs = _cached_references(article_id)
        for ref in refs.get("references_to", []):
            referenced_articles.add((ref["id"], ref.get("title", "")))
        for ref in refs.get("referenced_by", []):
            referenced_articles.add((ref["id"], ref.get("title", "")))

    related_requirements: list[dict] = []
    try:
        related_requirements = get_related_requirements(
            requirement_id)[:MAX_RELATED_REQUIREMENTS]
    except (KeyError, ValueError):
        pass

    prompt = _build_prompt(
        requirement_id, requirement_text, paragraphs, articles,
        referenced_articles, related_requirements, categories,
        semantic_profile_text=format_semantic_profile(profile),
    )

    try:
        raw = complete_json(
            prompt=prompt,
            system=RISK_ASSESSMENT_PROMPT,
            max_tokens=MAX_TOKENS,
        )
        assessment = _parse_assessment(raw)
    except ValueError:
        raw = {"fallback_used": True}
        assessment = RequirementRisk(
            summary="Model returned invalid JSON; semantic-profile fallback used.",
            risks=[],
            risk_level="low",
            recommendations=[],
        )

    assessment = _align_assessment_with_profile(assessment, profile)
    assessment = _apply_profile_gap_fallback(assessment, profile, articles)
    assessment = _apply_control_severity_policy(assessment, profile)
    assessment = _remove_duplicate_risks(assessment)
    return assessment, articles, raw


def _parse_assessment(raw: dict | list) -> RequirementRisk:
    if not isinstance(raw, dict):
        return RequirementRisk(summary=str(raw))

    try:
        return RequirementRisk.model_validate(raw)
    except Exception:
        pass

    for key in ("answer", "response", "result", "assessment", "data"):
        nested = raw.get(key)
        if isinstance(nested, dict) and "summary" in nested:
            try:
                return RequirementRisk.model_validate(nested)
            except Exception:
                pass

    summary = raw.get("summary", "")
    if not summary:
        for value in raw.values():
            if isinstance(value, str) and len(value) > 20:
                summary = value
                break

    risk_level = raw.get("risk_level", "medium")
    if risk_level not in ("high", "medium", "low"):
        risk_level = "medium"

    return RequirementRisk(
        summary=summary or "Model did not produce a valid risk assessment.",
        risk_level=risk_level,
    )

"""
Deterministic risk assessment pipeline.

Pre-fetches context from the Neo4j knowledge graph, then uses LLM-supported
semantic profiling and one final LLM call per requirement to synthesise a risk
assessment.
"""

from eu_ai_risks.analysis.models import RequirementRisk, RiskItem
from eu_ai_risks.analysis.prompts import RISK_ASSESSMENT_PROMPT
from eu_ai_risks.analysis.semantic_profiles import (
    article_ids_for_profile_categories,
    build_profile_retrieval_query,
    extract_requirement_profile,
    format_semantic_profile,
    rerank_paragraphs_by_profile,
)
from eu_ai_risks.db.graph import (
    find_paragraphs, list_categories, get_article,
    get_references, get_related_requirements,
)
from eu_ai_risks.embeddings import embed_text
from eu_ai_risks.llm import complete_json

TOP_K_PARAGRAPHS = 5
TOP_K_PARAGRAPH_CANDIDATES = 12
TOP_K_ARTICLES = 4
MAX_PARAGRAPHS_PER_ARTICLE = 4
MAX_CROSS_REFERENCES = 5
MAX_RELATED_REQUIREMENTS = 3
MAX_SHARED_ENTITIES = 3
MAX_TOKENS = 1200

# Generic fallbacks by obligation category. These are not requirement-specific
# patches; they provide a safe article anchor when the LLM returns no retained
# risk even though the semantic profile says a requirement-level obligation
# remains unclear.
CATEGORY_FALLBACK_RISKS = {
    "risk_management": {
        "article_id": "art:9",
        "paragraph_num": 1,
        "provision": "Article 9(1)",
        "description": "Risk management expectations for this requirement are not fully specified",
        "action": "Add risk identification, mitigation, and review criteria for this requirement.",
    },
    "data_governance": {
        "article_id": "art:10",
        "paragraph_num": 2,
        "provision": "Article 10(2)",
        "description": "Data governance, data quality, or data-management expectations are not fully specified",
        "action": "Define data source, quality, bias, and validation checks for this requirement.",
    },
    "technical_documentation": {
        "article_id": "art:11",
        "paragraph_num": 1,
        "provision": "Article 11(1)",
        "description": "Technical documentation expectations for this requirement are not fully specified",
        "action": "Document the design decision, evidence, and compliance rationale for this requirement.",
    },
    "record_keeping": {
        "article_id": "art:12",
        "paragraph_num": 1,
        "provision": "Article 12(1)",
        "description": "Record-keeping or logging expectations are not fully specified",
        "action": "Add logging and audit-trail acceptance criteria for this requirement.",
    },
    "transparency": {
        "article_id": "art:13",
        "paragraph_num": 1,
        "provision": "Article 13(1)",
        "description": "Transparency or explanation expectations are not fully specified",
        "action": "Add explanation, notification, or instruction requirements for deployers or affected users.",
    },
    "human_oversight": {
        "article_id": "art:14",
        "paragraph_num": 1,
        "provision": "Article 14(1)",
        "description": "Human oversight expectations are not fully specified",
        "action": "Add human review, override, authority, training, and escalation criteria.",
    },
    "accuracy_robustness_cybersecurity": {
        "article_id": "art:15",
        "paragraph_num": 1,
        "provision": "Article 15(1)",
        "description": "Accuracy, robustness, or cybersecurity expectations are not fully specified",
        "action": "Add performance, robustness, security, and failure-handling acceptance criteria.",
    },
    "quality_management": {
        "article_id": "art:17",
        "paragraph_num": 1,
        "provision": "Article 17(1)",
        "description": "Quality management expectations are not fully specified",
        "action": "Record the relevant quality-management procedure and owner.",
    },
    "fundamental_rights_impact_assessment": {
        "article_id": "art:27",
        "paragraph_num": 1,
        "provision": "Article 27(1)",
        "description": "Fundamental-rights impact assessment responsibilities may need review",
        "action": "Confirm whether a fundamental-rights impact assessment is required for this deployment context.",
    },
    "post_market_monitoring": {
        "article_id": "art:72",
        "paragraph_num": 1,
        "provision": "Article 72(1)",
        "description": "Post-market monitoring expectations are not fully specified",
        "action": "Define deployment monitoring metrics, review cadence, and incident follow-up steps.",
    },
}

# Intents that should be treated primarily as safeguards/controls. These are
# generic software-engineering intents, not requirement-ID patches. They prevent
# the assessor from escalating requirements that already specify a control.
LOW_RISK_CONTROL_INTENTS = {
    "logging_or_audit",
    "prohibited_feature_prevention",
}

MEDIUM_MAX_CONTROL_INTENTS = {
    "data_validation_or_bias_testing",
    "protected_attribute_control",
}

# Some categories have a clear Chapter 3 anchor. If the LLM returns the right
# category but cites a weak classification/admin article, normalise it back to
# the category anchor so the report remains useful at requirement level.
CATEGORY_ANCHORS = {
    key: (value["article_id"], value["paragraph_num"], value["provision"])
    for key, value in CATEGORY_FALLBACK_RISKS.items()
}


def _downgrade_risk(risk: RiskItem, severity: str) -> None:
    risk.severity = severity


def _normalise_risk_provision_to_category(risk: RiskItem) -> None:
    category = _normalise_category(risk.obligation_category)
    anchor = CATEGORY_ANCHORS.get(category)
    if not anchor:
        return

    # Article 6 is useful as classification context, but when a risk is labelled
    # as data_governance/transparency/etc. the cited article should be the
    # obligation article, not the classification exception.
    weak_for_category = {"art:6", "art:7", "art:43", "art:74", "art:79",
                         "art:81", "art:92", "art:93", "art:112", "art:113"}
    if risk.article_id in weak_for_category:
        risk.article_id, risk.paragraph_num, risk.provision = anchor


def _apply_control_severity_policy(
    assessment: RequirementRisk,
    profile,
) -> RequirementRisk:
    """Calibrate severity for requirements that already describe controls.

    This is deliberately intent/category-based rather than requirement-specific.
    Logging, audit, and prohibited-feature-prevention requirements should usually
    be low risk unless a clear unsupported gap remains. Dataset validation and
    protected-attribute controls can retain a medium remaining governance gap,
    but should not be escalated to high simply because broader Article 10 duties
    exist.
    """
    intent = getattr(profile, "requirement_intent", "")

    if intent == "prohibited_feature_prevention":
        assessment.risks = []
        assessment.risk_level = "low"
        assessment.summary = (
            "No requirement-level risk was retained because the requirement is "
            "framed as an existing safeguard/control that prevents a sensitive "
            "or prohibited feature. Manual review may still confirm how the "
            "control is implemented."
        )
        assessment.recommendations = []
        return assessment

    if intent in LOW_RISK_CONTROL_INTENTS:
        for risk in assessment.risks:
            _normalise_risk_provision_to_category(risk)
            if risk.severity in {"high", "medium"}:
                _downgrade_risk(risk, "low")
        if assessment.risks:
            assessment.risk_level = "low"
            assessment.summary = (
                "The requirement already describes a control/safeguard. A low "
                "remaining clarification risk is retained for manual review."
            )
        return assessment

    if intent in MEDIUM_MAX_CONTROL_INTENTS or getattr(profile, "is_safeguard_or_control", False):
        for risk in assessment.risks:
            _normalise_risk_provision_to_category(risk)
            if risk.severity == "high":
                _downgrade_risk(risk, "medium")
        if assessment.risk_level == "high":
            assessment.risk_level = "medium"
        return assessment

    for risk in assessment.risks:
        _normalise_risk_provision_to_category(risk)
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

    parts.append("\n## Matching provisions (semantic-profile retrieval + vector search)\n")
    for paragraph in paragraphs:
        parts.append(
            f"- **{paragraph['article_id']} "
            f"({paragraph['article_title']})** "
            f"paragraph {paragraph['paragraph_num']} "
            f"[{paragraph['obligation_type']}]: "
            f"{str(paragraph['paragraph_text'])[:500]} "
            f"(vector score={paragraph.get('score')}, "
            f"adjusted score={paragraph.get('adjusted_score', paragraph.get('score'))})\n"
        )

    if articles:
        parts.append("\n## Key article obligations\n")
        for article_id, article in articles.items():
            dimensions = article.get("dimensions", {}) or {}
            requirement_categories = dimensions.get("requirement_categories", [])
            parties = dimensions.get("responsible_parties", [])

            parts.append(f"### {article['title']} ({article_id})\n")
            if requirement_categories:
                parts.append(
                    f"- Graph requirement categories: "
                    f"{', '.join(requirement_categories)}\n"
                )
            if parties:
                parts.append(
                    f"- Graph responsible parties: {', '.join(parties)}\n"
                )

            binding = [
                ap for ap in article.get("paragraphs", [])
                if ap.get("obligation_type") in ("requirement", "prohibition")
            ][:MAX_PARAGRAPHS_PER_ARTICLE]
            for article_paragraph in binding:
                parts.append(
                    f"- ({article_paragraph['num']}) "
                    f"{article_paragraph['text'][:220]}\n"
                )

    if referenced_articles:
        parts.append("\n## Cross-referenced articles\n")
        for ref_id, ref_title in list(referenced_articles)[:MAX_CROSS_REFERENCES]:
            parts.append(f"- {ref_id}: {ref_title}\n")

    if related_requirements:
        parts.append("\n## Related requirements (shared entities)\n")
        for related in related_requirements:
            parts.append(
                f"- **{related['id']}**: {related['text']} "
                f"(shared: {', '.join(related['shared_entities'][:MAX_SHARED_ENTITIES])})\n"
            )

    parts.append("\n## Available requirement categories\n")
    for category in categories:
        parts.append(
            f"- {category['key']} → "
            f"{', '.join(category['article_ids'])}\n"
        )

    parts.append("\n## Assessment instructions for this requirement\n")
    parts.append(
        "- Assess the exact requirement text and semantic profile, not the whole SRS.\n"
    )
    parts.append(
        "- Prioritise the profile's primary and missing/unclear obligation "
        "categories. Do not force unrelated categories just because the system "
        "is high-risk.\n"
    )
    parts.append(
        "- If the requirement already describes a safeguard/control, treat it as "
        "addressed or partially addressed and only flag the specific remaining "
        "gap.\n"
    )
    parts.append(
        "- If the supplied provisions do not support a risk for this requirement, "
        "return no risks instead of using a weak article match.\n"
    )
    parts.append(
        "\nIdentify the compliance risks for this requirement based on the "
        "semantic profile and the graph provisions above."
    )

    return "\n".join(parts)



def _normalise_category(value: str) -> str:
    return value.strip().lower().replace(" ", "_").replace("-", "_")


def _article_available(article_id: str, articles: dict[str, dict]) -> bool:
    return article_id in articles


def _fallback_category_order(profile) -> list[str]:
    ordered: list[str] = []
    for category in (
        profile.missing_or_unclear_categories
        + [profile.primary_obligation_category]
        + profile.secondary_obligation_categories
    ):
        key = _normalise_category(category)
        if key and key not in ordered:
            ordered.append(key)
    return ordered


def _apply_profile_gap_fallback(
    assessment: RequirementRisk,
    profile,
    articles: dict[str, dict],
) -> RequirementRisk:
    """Add one safe risk when profile scope is clear but LLM retained none.

    This keeps the pipeline robust without hardcoding individual requirements.
    The fallback only uses structured profile categories and generic article
    anchors. Safeguards with no remaining missing categories stay low/no-risk.
    """
    if assessment.risks:
        return assessment

    category_order = _fallback_category_order(profile)
    if not category_order:
        assessment.risk_level = "low"
        return assessment

    # If this is an explicit safeguard and the profile has no missing/unclear
    # categories, keep it as a low-risk retained control.
    if profile.is_safeguard_or_control and not profile.missing_or_unclear_categories:
        assessment.risk_level = "low"
        assessment.summary = (
            "No requirement-level risk was retained because the requirement is "
            "framed as an existing safeguard/control. Manual review may still "
            "be useful to confirm implementation details."
        )
        return assessment

    for category in category_order:
        fallback = CATEGORY_FALLBACK_RISKS.get(category)
        if not fallback:
            continue
        # Prefer article anchors that were already fetched, but do not require
        # that for core Chapter 3 categories because report citation collection
        # can fetch the article by ID later.
        article_id = fallback["article_id"]
        if articles and not _article_available(article_id, articles):
            core = {"art:9", "art:10", "art:11", "art:12", "art:13", "art:14", "art:15"}
            if article_id not in core:
                continue

        assessment.risks = [RiskItem(
            description=fallback["description"],
            severity="medium",
            article_id=article_id,
            paragraph_num=fallback["paragraph_num"],
            provision=fallback["provision"],
            obligation_category=category,
            engineering_action=fallback["action"],
        )]
        assessment.risk_level = "medium"
        assessment.summary = (
            f"The semantic profile indicates a remaining {category} gap for "
            "this exact requirement. A conservative requirement-level risk has "
            "been retained for manual review."
        )
        assessment.recommendations = [fallback["action"]]
        return assessment

    assessment.risk_level = "low"
    return assessment


def _align_assessment_with_profile(assessment: RequirementRisk, profile) -> RequirementRisk:
    """Light post-processing guard against category drift.

    The final LLM sometimes overgeneralises high-risk AI obligations. This
    guard does not invent new risks; it only removes risks that are outside the
    semantic profile's stated assessment scope when the profile is confident
    enough to provide that scope.
    """
    supported = {_normalise_category(c) for c in profile.supported_categories()}
    if not supported:
        return assessment

    filtered = []
    for risk in assessment.risks:
        risk_category = _normalise_category(risk.obligation_category)
        if not risk_category or risk_category in supported:
            filtered.append(risk)

    if filtered == assessment.risks:
        return assessment

    assessment.risks = filtered
    if not filtered:
        assessment.risk_level = "low"
        assessment.summary = (
            "No requirement-level risk was retained after aligning the output "
            "with the semantic profile. The generated provisions may need "
            "manual review."
        )
        assessment.recommendations = []
    elif assessment.risk_level == "high" and all(r.severity != "high" for r in filtered):
        assessment.risk_level = "medium"

    return assessment

def assess_requirement(
    requirement_id: str,
    requirement_text: str,
    categories: list[dict] | None = None,
) -> tuple[RequirementRisk, dict[str, dict], dict | list]:
    """Assess a single requirement against the EU AI Act graph.

    Returns (parsed assessment, fetched articles, raw LLM output).
    """
    if categories is None:
        categories = list_categories()

    # Instead of keyword triggers, first create a semantic profile. The profile
    # expands the retrieval query and identifies likely obligation categories.
    profile = extract_requirement_profile(
        requirement_id=requirement_id,
        requirement_text=requirement_text,
        categories=categories,
    )
    retrieval_query = build_profile_retrieval_query(profile, requirement_text)
    embedding = embed_text(retrieval_query)

    paragraph_candidates = find_paragraphs(
        embedding,
        top_k=TOP_K_PARAGRAPH_CANDIDATES,
    )
    paragraphs = rerank_paragraphs_by_profile(
        paragraph_candidates,
        profile,
        categories,
        limit=TOP_K_PARAGRAPHS,
    )

    priority_article_ids = article_ids_for_profile_categories(profile, categories)
    hit_article_ids = list(dict.fromkeys(
        [paragraph["article_id"] for paragraph in paragraphs]
        + priority_article_ids
    ))

    articles = {}
    for article_id in hit_article_ids[:TOP_K_ARTICLES]:
        article = get_article(article_id)
        if article:
            articles[article_id] = article

    referenced_articles: set[tuple[str, str]] = set()
    for article_id in hit_article_ids[:TOP_K_ARTICLES]:
        refs = get_references(article_id)
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
        requirement_id,
        requirement_text,
        paragraphs,
        articles,
        referenced_articles,
        related_requirements,
        categories,
        semantic_profile_text=format_semantic_profile(profile),
    )

    try:
        raw = complete_json(
            prompt=prompt,
            system=RISK_ASSESSMENT_PROMPT,
            max_tokens=MAX_TOKENS,
        )
        assessment = _parse_assessment(raw)
    except ValueError as exc:
        # Local/small LLMs occasionally return truncated or repetitive JSON.
        # Do not crash the full batch; fall back to the deterministic semantic
        # profile/category policy so the report can still be generated and
        # manually reviewed.
        raw = {
            "fallback_used": True,
            "error": str(exc)[:500],
        }
        assessment = RequirementRisk(
            summary=(
                "The model returned invalid JSON, so a deterministic "
                "semantic-profile fallback was used for manual review."
            ),
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

    # Try direct validation first.
    try:
        return RequirementRisk.model_validate(raw)
    except Exception:
        pass

    # Model may wrap the response in a key like "answer", "response",
    # "result", or "assessment".
    for key in ("answer", "response", "result", "assessment", "data"):
        nested = raw.get(key)
        if isinstance(nested, dict) and "summary" in nested:
            try:
                return RequirementRisk.model_validate(nested)
            except Exception:
                pass

    # Extract whatever text we can find.
    summary = raw.get("summary", "")
    if not summary:
        for value in raw.values():
            if isinstance(value, str) and len(value) > 20:
                summary = value
                break

    risk_level = raw.get("risk_level", "medium")
    if risk_level not in ("high", "medium", "low"):
        risk_level = "medium"

    if not summary:
        summary = "Model did not produce a valid risk assessment."

    return RequirementRisk(summary=summary, risk_level=risk_level)

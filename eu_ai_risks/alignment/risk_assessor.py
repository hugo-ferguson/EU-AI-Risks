"""
Deterministic risk assessment pipeline.

Pre-fetches context from the Neo4j knowledge graph, then uses a single
LLM call per requirement to synthesise a risk assessment.
"""

from eu_ai_risks.alignment.models import RequirementRisk
from eu_ai_risks.alignment.prompts import RISK_ASSESSMENT_PROMPT
from eu_ai_risks.db.graph import (
    find_paragraphs, list_categories, get_article,
    get_references, get_related_requirements,
)
from eu_ai_risks.embeddings import embed_text
from eu_ai_risks.llm import complete_json

TOP_K_PARAGRAPHS = 5
TOP_K_ARTICLES = 2
MAX_PARAGRAPHS_PER_ARTICLE = 4
MAX_CROSS_REFERENCES = 5
MAX_RELATED_REQUIREMENTS = 3
MAX_SHARED_ENTITIES = 3
MAX_TOKENS = 2048


def _build_prompt(
    requirement_id: str,
    requirement_text: str,
    paragraphs: list[dict],
    articles: dict[str, dict],
    referenced_articles: set[tuple[str, str]],
    related_requirements: list[dict],
    categories: list[dict],
) -> str:
    parts = [
        f"## Requirement {requirement_id}\n",
        f"{requirement_text}\n",
        "\n## Matching provisions (vector search)\n",
    ]
    for paragraph in paragraphs:
        parts.append(
            f"- **{paragraph['article_id']} "
            f"({paragraph['article_title']})** "
            f"paragraph {paragraph['paragraph_num']} "
            f"[{paragraph['obligation_type']}]: "
            f"{paragraph['paragraph_text']}\n"
        )

    if articles:
        parts.append("\n## Key article obligations\n")
        for article_id, article in articles.items():
            parts.append(f"### {article['title']} ({article_id})\n")
            binding = [
                ap for ap in article.get("paragraphs", [])
                if ap.get("obligation_type") in ("requirement", "prohibition")
            ][:MAX_PARAGRAPHS_PER_ARTICLE]
            for article_paragraph in binding:
                parts.append(
                    f"- ({article_paragraph['num']}) "
                    f"{article_paragraph['text'][:300]}\n"
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

    parts.append("\n## Requirement categories\n")
    for category in categories:
        parts.append(
            f"- {category['key']} → "
            f"{', '.join(category['article_ids'])}\n"
        )

    parts.append(
        "\nIdentify the compliance risks for this requirement "
        "based on the provisions above."
    )

    return "\n".join(parts)


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

    embedding = embed_text(requirement_text)
    paragraphs = find_paragraphs(embedding, top_k=TOP_K_PARAGRAPHS)

    hit_article_ids = list(dict.fromkeys(
        paragraph["article_id"] for paragraph in paragraphs
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
        requirement_id, requirement_text, paragraphs, articles,
        referenced_articles, related_requirements, categories,
    )

    raw = complete_json(
        prompt=prompt,
        system=RISK_ASSESSMENT_PROMPT,
        max_tokens=MAX_TOKENS,
    )

    assessment = _parse_assessment(raw)
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

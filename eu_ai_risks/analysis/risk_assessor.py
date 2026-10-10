"""
Deterministic (single-call) risk assessment against the Neo4j
knowledge graph, with every cited provision traced back through the graph.
"""

import os
import re
from dataclasses import dataclass, field
from functools import lru_cache

from eu_ai_risks.analysis.models import RequirementRisk, RiskItem
from eu_ai_risks.analysis.prompts import (
    ARTICLE_ROUTING_ANNEX_PARTS, ARTICLE_ROUTING_PROMPT, RISK_ASSESSMENT_PROMPT,
)
from eu_ai_risks.db.graph import (
    binding_paragraphs_for_articles, find_paragraphs, get_annex_iii_points,
    get_article_index, get_articles_using_concepts, get_concepts,
    get_provisions, get_referenced_provisions, get_related_requirements,
    get_requirement_concepts, provision_label,
)
from eu_ai_risks.embeddings import embed_text
from eu_ai_risks.llm import complete_json

# "graph" routes through the Act's article index, concepts and references;
# "vector" is plain paragraph vector search, kept as a baseline to compare
RETRIEVAL_MODE = os.environ.get("EU_AI_RISKS_RETRIEVAL", "graph").strip().lower()

ROUTED_ARTICLES = 5
PARAGRAPHS_PER_ROUTED_ARTICLE = 2
CONCEPT_PARAGRAPHS = 3
REFERENCED_PARAGRAPHS = 3
MAX_DEFINITIONS = 8
VECTOR_PARAGRAPHS = 3
VECTOR_CANDIDATES = 15
MAX_RELATED_REQUIREMENTS = 5
MAX_SHARED_ENTITIES = 3
MAX_RELATED_TRIPLES = 4
MAX_TOKENS = 2048
BINDING_OBLIGATION_TYPES = {"requirement", "prohibition"}

RE_PROVISION_ID = re.compile(r"art:\d+:p\d+(?::[a-z])?")


@dataclass
class _Retrieval:
    """The provisions supplied for one requirement, and how each was reached."""
    paragraphs: dict[str, dict] = field(default_factory=dict)
    via: dict[str, list[str]] = field(default_factory=dict)
    definitions: dict[str, dict] = field(default_factory=dict)
    # Paragraph id -> Annex III points it refers to, for scope checks
    scope: dict[str, list[str]] = field(default_factory=dict)
    # Concept name -> how the requirement itself connects to that defined term
    requirement_concepts: dict[str, str] = field(default_factory=dict)
    routed_articles: list[str] = field(default_factory=list)
    annex_iii_points: list[str] = field(default_factory=list)

    def add(self, paragraph: dict, via: str) -> bool:
        """Add a paragraph (or another route to it); return True if it is new."""
        paragraph_id = paragraph["paragraph_id"]
        routes = self.via.setdefault(paragraph_id, [])
        if via not in routes:
            routes.append(via)
        if paragraph_id in self.paragraphs:
            return False
        self.paragraphs[paragraph_id] = paragraph
        return True


def _annex_point_summary(point_id: str, text: str) -> str:
    # Numbered points (annex:III:4) contain their lettered points, so keep the heading only
    return text.split(":")[0] if point_id.count(":") == 2 else text


@lru_cache(maxsize=1)
def _act_index() -> tuple[str, dict[str, str], str, dict[str, str], dict[str, str]]:
    """
    Render the Act's table of contents and Annex III once.

    :return: (article index text, article id -> chapter/section heading,
        Annex III index text, Annex III point id -> text, article id -> title).
    """
    lines: list[str] = []
    headings: dict[str, str] = {}
    titles: dict[str, str] = {}
    current_heading = None
    for row in get_article_index():
        heading = f"{row['chapter_id']} {row['chapter_title'] or ''}".strip()
        if row["section_title"]:
            heading += f" / {row['section_title']}"
        if heading != current_heading:
            lines.append(f"\n{heading}")
            current_heading = heading
        lines.append(f"- {row['article_id']}: {row['article_title']}")
        headings[row["article_id"]] = heading
        titles[row["article_id"]] = row["article_title"]

    annex_texts = {row["id"]: row["text"] for row in get_annex_iii_points()}
    annex_lines = [
        f"- {point_id}: {_annex_point_summary(point_id, text)[:200]}"
        for point_id, text in annex_texts.items()
    ]
    return "\n".join(lines), headings, "\n".join(annex_lines), annex_texts, titles


@lru_cache(maxsize=1)
def _concepts() -> dict[str, dict]:
    return {concept["name"]: concept for concept in get_concepts()}


@lru_cache(maxsize=1)
def _concept_patterns() -> dict[str, re.Pattern]:
    # Whole-word, case-insensitive, allowing a plural 's'
    return {
        name: re.compile(rf"(?<!\w){re.escape(name)}s?(?!\w)", re.IGNORECASE)
        for name in _concepts()
    }


def _concepts_in(text: str) -> list[str]:
    return [name for name, pattern in _concept_patterns().items() if pattern.search(text)]


def _route(requirement_text: str) -> tuple[list[str], list[str]]:
    """Ask the LLM which articles, and which Annex III points, apply to the requirement."""
    index_text, headings, annex_index, annex_texts, _ = _act_index()
    # Without Annex III points in the graph the model tends to explain its
    # guesses in prose, so that part of the prompt is left out entirely
    annex_parts = {
        "annex_task": ARTICLE_ROUTING_ANNEX_PARTS["annex_task"],
        "annex_section": ARTICLE_ROUTING_ANNEX_PARTS["annex_section"].format(annex_index=annex_index),
        "annex_instruction": ARTICLE_ROUTING_ANNEX_PARTS["annex_instruction"],
    } if annex_index else {
        "annex_task": "", "annex_section": "", "annex_instruction": " Give an empty list for annex_iii_points.",
    }
    system = ARTICLE_ROUTING_PROMPT.format(index=index_text, limit=ROUTED_ARTICLES, **annex_parts)

    # One retry: the model occasionally answers in prose instead of JSON
    for _ in range(2):
        try:
            result = complete_json(
                prompt=f"Requirement: {requirement_text}",
                system=system,
                max_tokens=300,
            )
        except ValueError:
            continue
        if not isinstance(result, dict):
            return [], []
        articles = [
            article_id for article_id in dict.fromkeys(result.get("articles", []))
            if article_id in headings
        ][:ROUTED_ARTICLES]
        annex_points = [
            point_id for point_id in dict.fromkeys(result.get("annex_iii_points", []))
            if point_id in annex_texts
        ]
        return articles, annex_points
    return [], []


def _add_concept_provisions(
    retrieval: _Retrieval, requirement_id: str, embedding: list[float],
) -> list[dict]:
    """Add provisions reached through the requirement's Act concepts; return the links used."""
    links = get_requirement_concepts(requirement_id)
    if not links:
        return []

    articles_by_concept = get_articles_using_concepts(
        sorted({link["concept"] for link in links}))
    article_ids = list(dict.fromkeys(
        article_id for article_ids in articles_by_concept.values() for article_id in article_ids))
    candidates = binding_paragraphs_for_articles(article_ids, embedding, per_article=1)

    added = 0
    for paragraph in sorted(candidates, key=lambda p: p["score"], reverse=True):
        link = next(
            (link for link in links
             if paragraph["article_id"] in articles_by_concept.get(link["concept"], [])),
            None,
        )
        if not link:
            continue
        definition = _concepts().get(link["concept"], {})
        via = (
            f"requirement term '{link['entity']}' is an instance of the defined term "
            f"'{link['concept']}' ({provision_label(definition.get('definition_id', 'art:3'))}), "
            f"which Article {paragraph['article_num']} uses"
        )
        # Extra routes to an existing provision are kept as further evidence
        if paragraph["paragraph_id"] in retrieval.paragraphs:
            retrieval.add(paragraph, via)
        elif added < CONCEPT_PARAGRAPHS:
            retrieval.add(paragraph, via)
            added += 1
    return links


def _add_referenced_provisions(retrieval: _Retrieval) -> None:
    """Follow references from the supplied provisions, and record Annex III scope."""
    added = 0
    for reference in get_referenced_provisions(list(retrieval.paragraphs)):
        source_id = reference["source_id"]
        source_paragraph = ":".join(source_id.split(":")[:3])
        target_id = reference["target_id"]

        if target_id.startswith("annex:III:"):
            scope = retrieval.scope.setdefault(source_paragraph, [])
            if target_id not in scope:
                scope.append(target_id)
            continue

        if not reference["paragraph_id"] or not reference["article_id"]:
            continue
        if reference["paragraph_id"] in retrieval.paragraphs or added >= REFERENCED_PARAGRAPHS:
            continue
        retrieval.add(
            {key: reference[key] for key in (
                "paragraph_id", "paragraph_num", "paragraph_text", "obligation_type",
                "article_id", "article_num", "article_title")},
            f"referenced by {provision_label(source_id)} ({provision_label(target_id)})",
        )
        added += 1


def _select_definitions(
    retrieval: _Retrieval, requirement_text: str, links: list[dict],
) -> None:
    """Supply the Article 3 definitions of terms the requirement or provisions use."""
    concepts = _concepts()
    for link in links:
        retrieval.requirement_concepts.setdefault(
            link["concept"],
            f"requirement term '{link['entity']}' is the defined term '{link['concept']}'",
        )
    for name in _concepts_in(requirement_text):
        retrieval.requirement_concepts.setdefault(
            name, f"requirement uses the defined term '{name}'")

    mentioned = [
        name for paragraph in retrieval.paragraphs.values()
        for name in _concepts_in(paragraph["paragraph_text"] or "")
    ]
    # The requirement's own terms first, then the most specific (least used) terms
    ranked = list(retrieval.requirement_concepts) + sorted(
        set(mentioned) - set(retrieval.requirement_concepts),
        key=lambda name: int(concepts[name]["article_count"] or 0),
    )
    retrieval.definitions = {
        name: concepts[name] for name in ranked[:MAX_DEFINITIONS] if name in concepts
    }


def _retrieve(requirement_id: str, requirement_text: str) -> _Retrieval:
    """Collect the provisions for a requirement, recording how each was reached."""
    embedding = embed_text(requirement_text)
    retrieval = _Retrieval()

    if RETRIEVAL_MODE == "vector":
        for paragraph in find_paragraphs(embedding, top_k=VECTOR_PARAGRAPHS):
            retrieval.add(paragraph, "vector similarity to the requirement")
        return retrieval

    articles, annex_points = _route(requirement_text)
    retrieval.routed_articles, retrieval.annex_iii_points = articles, annex_points
    headings = _act_index()[1]
    for paragraph in binding_paragraphs_for_articles(
            articles, embedding, per_article=PARAGRAPHS_PER_ROUTED_ARTICLE):
        closest_point = paragraph.get("best_point_id")
        retrieval.add(
            paragraph,
            f"selected from the Act's index: {headings.get(paragraph['article_id'], '')} "
            f"> Article {paragraph['article_num']} {paragraph['article_title']}"
            + (f" (closest match: {provision_label(closest_point)})" if closest_point else ""),
        )

    links = _add_concept_provisions(retrieval, requirement_id, embedding)

    # Vector search only when the graph routes found nothing
    if not retrieval.paragraphs:
        for paragraph in [
            paragraph for paragraph in find_paragraphs(embedding, top_k=VECTOR_CANDIDATES)
            if paragraph["obligation_type"] in BINDING_OBLIGATION_TYPES
        ][:VECTOR_PARAGRAPHS]:
            retrieval.add(paragraph, "vector similarity to the requirement (fallback)")

    _add_referenced_provisions(retrieval)
    _select_definitions(retrieval, requirement_text, links)
    return retrieval


def _normalise_category(value: str) -> str:
    return value.strip().lower().replace(" ", "_").replace("-", "_")


def _build_prompt(
    requirement_id: str,
    requirement_text: str,
    retrieval: _Retrieval,
    related_requirements: list[dict],
) -> str:
    parts = [
        f"## Requirement {requirement_id}\n",
        f"{requirement_text}\n",
    ]

    if retrieval.annex_iii_points:
        annex_texts = _act_index()[3]
        parts.append("\n## Annex III classification of this requirement's system\n")
        for point_id in retrieval.annex_iii_points:
            parts.append(f"- [{point_id}] {provision_label(point_id)}: {annex_texts.get(point_id, '')}\n")

    parts.append("\n## Provisions from the EU AI Act graph\n")
    by_article: dict[str, list[dict]] = {}
    for paragraph in retrieval.paragraphs.values():
        by_article.setdefault(paragraph["article_id"], []).append(paragraph)
    for article_id, article_paragraphs in by_article.items():
        first = article_paragraphs[0]
        parts.append(
            f"### Article {first['article_num']}: {first['article_title']} ({article_id})\n")
        for paragraph in sorted(article_paragraphs, key=lambda p: p["paragraph_num"] or 0):
            parts.append(
                f"- [{paragraph['paragraph_id']}] paragraph {paragraph['paragraph_num']} "
                f"[{paragraph['obligation_type']}]: {paragraph['paragraph_text']}\n"
            )
            scope = retrieval.scope.get(paragraph["paragraph_id"])
            if scope:
                parts.append(
                    f"  Scope: refers to {', '.join(provision_label(point_id) for point_id in scope)}\n")

    if retrieval.definitions:
        parts.append("\n## Definitions (Article 3)\n")
        for name, concept in retrieval.definitions.items():
            parts.append(f"- [{concept['definition_id']}] '{name}': {concept['definition_text']}\n")

    if related_requirements:
        parts.append("\n## Related requirements in this SRS (shared entities)\n")
        for related in related_requirements:
            # Show similar-but-different entities as "ours ≈ theirs"
            shared = ", ".join(
                own if own == theirs else f"{own} ≈ {theirs}"
                for own, theirs in related["matches"][:MAX_SHARED_ENTITIES])
            parts.append(
                f"- **{related['id']}**: {related['text']} "
                f"(shared: {shared})\n"
            )
            for subject, relation, obj in related.get("triples", [])[:MAX_RELATED_TRIPLES]:
                parts.append(f"  - {subject} → {relation} → {obj}\n")

    parts.append("\nIdentify the compliance risks for this requirement "
                 "based on the provisions above.")

    return "\n".join(parts)


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


def _scopes_overlap(point_a: str, point_b: str) -> bool:
    # annex:III:4 covers annex:III:4:a and vice versa
    return point_a == point_b or point_a.startswith(f"{point_b}:") or point_b.startswith(f"{point_a}:")


def _trace_citations(assessment: RequirementRisk, retrieval: _Retrieval) -> RequirementRisk:
    """Resolve each risk's citation to a graph node and record how it was reached."""
    for risk in assessment.risks:
        found = RE_PROVISION_ID.search(risk.provision_id or "")
        if found:
            risk.provision_id = found.group(0)
        elif risk.article_id and risk.paragraph_num is not None:
            risk.provision_id = f"{risk.article_id}:p{risk.paragraph_num}"

    cited = {risk.provision_id for risk in assessment.risks if risk.provision_id}
    provisions = get_provisions(sorted(cited | {
        ":".join(node_id.split(":")[:3]) for node_id in cited}))
    definitions_by_id = {
        concept["definition_id"]: name for name, concept in retrieval.definitions.items()}
    supplied = set(retrieval.paragraphs) | set(definitions_by_id)

    for risk in assessment.risks:
        if not risk.provision_id:
            risk.citation_supplied = False
            risk.trace = ["no provision id was given for this risk"]
            continue

        paragraph_id = ":".join(risk.provision_id.split(":")[:3])
        # A point the graph doesn't have (e.g. before a rebuild) falls back to its paragraph
        if risk.provision_id not in provisions and paragraph_id in provisions:
            risk.provision_id = paragraph_id
        node = provisions.get(risk.provision_id)
        if node:
            risk.article_id = node["article_id"]
            risk.paragraph_num = node["paragraph_num"]
            risk.provision = provision_label(risk.provision_id)

        risk.citation_supplied = paragraph_id in supplied
        if paragraph_id in definitions_by_id:
            risk.trace = [f"definition of '{definitions_by_id[paragraph_id]}' supplied from Article 3"]
        else:
            risk.trace = list(retrieval.via.get(paragraph_id, []))
        # Only defined terms that link the requirement's wording to this provision
        text = (node or {}).get("text") or retrieval.paragraphs.get(paragraph_id, {}).get("paragraph_text", "")
        for name in _concepts_in(text):
            if name in retrieval.requirement_concepts and name in _concepts():
                definition_id = _concepts()[name]["definition_id"]
                risk.trace.append(
                    f"{retrieval.requirement_concepts[name]} ({provision_label(definition_id)}), "
                    f"which this provision uses")

        scope = retrieval.scope.get(paragraph_id, [])
        if scope and retrieval.annex_iii_points and not any(
                _scopes_overlap(point_id, classified)
                for point_id in scope for classified in retrieval.annex_iii_points):
            risk.scope_warning = (
                f"{provision_label(paragraph_id)} refers to "
                f"{', '.join(provision_label(point_id) for point_id in scope)}, but this "
                f"requirement's system was classified under "
                f"{', '.join(provision_label(point_id) for point_id in retrieval.annex_iii_points)}."
            )
    return assessment


def assess_requirement(
    requirement_id: str,
    requirement_text: str,
) -> tuple[RequirementRisk, dict[str, dict], dict | list]:
    """Assess a single requirement against the EU AI Act graph."""
    retrieval = _retrieve(requirement_id, requirement_text)

    # With nothing retrieved the model can only say "no gap"; report that as
    # not assessed so a broken or unenriched graph can't pass as low risk
    if not retrieval.paragraphs:
        assessment = RequirementRisk(
            summary=(
                "Not assessed: no EU AI Act provisions were retrieved from the graph for "
                "this requirement. Check that the graph is built and enriched "
                "(paragraph obligation types are needed to find binding provisions)."
            ),
            risks=[],
            risk_level="unknown",
            recommendations=[],
        )
        _record_retrieval_steps(assessment, retrieval)
        return assessment, {}, {"retrieval": {
            "mode": RETRIEVAL_MODE,
            "routed_articles": retrieval.routed_articles,
            "annex_iii_points": retrieval.annex_iii_points,
            "provisions": {},
        }, "not_assessed": True}

    related_requirements: list[dict] = []
    try:
        related_requirements = get_related_requirements(
            requirement_id, limit=MAX_RELATED_REQUIREMENTS)
    except (KeyError, ValueError):
        pass

    prompt = _build_prompt(
        requirement_id, requirement_text, retrieval, related_requirements,
    )

    # Recorded alongside the model output so each assessment is traceable
    retrieval_record = {
        "mode": RETRIEVAL_MODE,
        "routed_articles": retrieval.routed_articles,
        "annex_iii_points": retrieval.annex_iii_points,
        "provisions": {paragraph_id: routes for paragraph_id, routes in retrieval.via.items()},
        "definitions": [concept["definition_id"] for concept in retrieval.definitions.values()],
        "scope": retrieval.scope,
    }

    try:
        raw = complete_json(
            prompt=prompt,
            system=RISK_ASSESSMENT_PROMPT,
            max_tokens=MAX_TOKENS,
        )
        assessment = _parse_assessment(raw)
    except ValueError:
        # Report the failure as such rather than as a low-risk finding
        assessment = RequirementRisk(
            summary=(
                "Assessment failed: the model did not return valid JSON, "
                "so this requirement was not assessed."
            ),
            risks=[],
            risk_level="unknown",
            recommendations=[],
        )
        _record_retrieval_steps(assessment, retrieval)
        return assessment, {}, {"retrieval": retrieval_record, "fallback_used": True}

    assessment = _remove_duplicate_risks(assessment)
    assessment = _trace_citations(assessment, retrieval)
    _record_retrieval_steps(assessment, retrieval)
    raw = {"retrieval": retrieval_record, **raw} if isinstance(raw, dict) else raw
    return assessment, {}, raw


def _record_retrieval_steps(assessment: RequirementRisk, retrieval: _Retrieval) -> None:
    """Attach the classification and article selection, where every trace starts."""
    annex_texts, titles = _act_index()[3], _act_index()[4]
    assessment.classification = [
        f"{provision_label(point_id)} ({point_id}): "
        f"{_annex_point_summary(point_id, annex_texts.get(point_id, ''))}"
        for point_id in retrieval.annex_iii_points
    ]
    assessment.selected_articles = [
        f"{provision_label(article_id)} {titles.get(article_id, '')} ({article_id})"
        for article_id in retrieval.routed_articles
    ]


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

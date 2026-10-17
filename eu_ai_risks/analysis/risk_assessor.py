"""
Deterministic (single-call) risk assessment against the Neo4j
knowledge graph, with every cited provision traced back through the graph.
"""

import os
import re
from dataclasses import dataclass, field
from functools import lru_cache
from typing import NamedTuple

from pydantic import ValidationError

from eu_ai_risks.analysis.models import RequirementRisk, RiskItem
from eu_ai_risks.analysis.prompts import (
    ARTICLE_ROUTING_PROMPT, RISK_ASSESSMENT_PROMPT, SYSTEM_CLASSIFICATION_PROMPT,
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
# All of them: the router chose the article, so similarity only orders its
# paragraphs. A cap here dropped e.g. Article 26(11) from notification requirements
PARAGRAPHS_PER_ROUTED_ARTICLE: int | None = None
CONCEPT_PARAGRAPHS = 3
REFERENCED_PARAGRAPHS = 3
MAX_DEFINITIONS = 8
VECTOR_PARAGRAPHS = 3
VECTOR_CANDIDATES = 15
MAX_RELATED_REQUIREMENTS = 5
MAX_SHARED_ENTITIES = 3
MAX_RELATED_TRIPLES = 4
# Beyond this the rest of the SRS is left out and only related requirements are shown
MAX_SRS_REQUIREMENTS = 80
MAX_TOKENS = 2048
ROUTING_MAX_TOKENS = 300
CLASSIFICATION_MAX_TOKENS = 400
BINDING_OBLIGATION_TYPES = {"requirement", "prohibition"}
RISK_LEVELS = ("high", "medium", "low")

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

    def record(self) -> dict:
        """Recorded alongside the model output so each assessment is traceable."""
        return {
            "mode": RETRIEVAL_MODE,
            "routed_articles": self.routed_articles,
            "annex_iii_points": self.annex_iii_points,
            "provisions": dict(self.via),
            "definitions": [concept["definition_id"] for concept in self.definitions.values()],
            "scope": self.scope,
        }


@dataclass(frozen=True)
class SystemContext:
    """What every requirement's assessment needs to know about the system as a whole."""
    requirements: tuple[tuple[str, str], ...]  # (id, text) in SRS order
    intended_purpose: str = ""
    annex_iii_points: tuple[str, ...] = ()


class _ActIndex(NamedTuple):
    article_index: str
    headings: dict[str, str]  # article id -> chapter/section heading
    titles: dict[str, str]  # article id -> title
    annex_index: str
    annex_texts: dict[str, str]  # Annex III point id -> text


def _paragraph_of(node_id: str) -> str:
    """art:10:p2:f -> art:10:p2"""
    return ":".join(node_id.split(":")[:3])


def _annex_point_summary(point_id: str, text: str) -> str:
    # Numbered points (annex:III:4) contain their lettered points, so keep the heading only
    return text.split(":")[0] if point_id.count(":") == 2 else text


@lru_cache(maxsize=1)
def _act_index() -> _ActIndex:
    """Render the Act's table of contents and Annex III once."""
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
    return _ActIndex("\n".join(lines), headings, titles, "\n".join(annex_lines), annex_texts)


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


def _complete_json_dict(prompt: str, system: str, max_tokens: int) -> dict | None:
    # One retry: the model occasionally answers in prose instead of JSON
    for _ in range(2):
        try:
            result = complete_json(prompt=prompt, system=system, max_tokens=max_tokens)
        except ValueError:
            continue
        return result if isinstance(result, dict) else None
    return None


def classify_system(requirements: list[tuple[str, str]]) -> SystemContext:
    """
    Classify the system once from all its requirements, so that every
    requirement is assessed as part of the same (possibly high-risk) system.

    :param requirements: (id, text) pairs in SRS order.
    """
    index = _act_index()
    srs = "\n".join(f"- {requirement_id}: {text}" for requirement_id, text in requirements)
    result = _complete_json_dict(
        f"Requirements:\n{srs}",
        SYSTEM_CLASSIFICATION_PROMPT.format(
            annex_index=index.annex_index or "(none in the graph; give an empty list)"),
        CLASSIFICATION_MAX_TOKENS,
    ) or {}
    purpose = result.get("intended_purpose")
    return SystemContext(
        requirements=tuple(requirements),
        intended_purpose=purpose.strip() if isinstance(purpose, str) else "",
        annex_iii_points=tuple(
            point_id for point_id in dict.fromkeys(result.get("annex_iii_points") or [])
            if point_id in index.annex_texts
        ),
    )


def _system_lines(system: SystemContext) -> list[str]:
    annex_texts = _act_index().annex_texts
    lines = []
    if system.intended_purpose:
        lines.append(f"Intended purpose (inferred from the SRS): {system.intended_purpose}")
    if system.annex_iii_points:
        lines.append("Annex III classification:")
        lines.extend(
            f"- [{point_id}] {provision_label(point_id)}: {annex_texts.get(point_id, '')}"
            for point_id in system.annex_iii_points)
    else:
        lines.append("Annex III classification: none (no Annex III point clearly applies)")
    return lines


def _route(requirement_text: str, system: SystemContext) -> list[str]:
    """Ask the LLM which articles apply to the requirement, given the system it is part of."""
    index = _act_index()
    result = _complete_json_dict(
        "\n".join([*_system_lines(system), "", f"Requirement: {requirement_text}"]),
        ARTICLE_ROUTING_PROMPT.format(index=index.article_index, limit=ROUTED_ARTICLES),
        ROUTING_MAX_TOKENS,
    ) or {}
    return [
        article_id for article_id in dict.fromkeys(result.get("articles") or [])
        if article_id in index.headings
    ][:ROUTED_ARTICLES]


def _add_routed_provisions(retrieval: _Retrieval, embedding: list[float]) -> None:
    """Add the binding paragraphs of the articles the LLM picked from the Act's index."""
    headings = _act_index().headings
    for paragraph in binding_paragraphs_for_articles(
            retrieval.routed_articles, embedding, per_article=PARAGRAPHS_PER_ROUTED_ARTICLE):
        closest_point = paragraph.get("best_point_id")
        retrieval.add(
            paragraph,
            f"selected from the Act's index: {headings.get(paragraph['article_id'], '')} "
            f"> Article {paragraph['article_num']} {paragraph['article_title']}"
            + (f" (closest match: {provision_label(closest_point)})" if closest_point else ""),
        )


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
        # Extra routes to an existing provision are kept as further evidence,
        # so the cap only limits new provisions
        if paragraph["paragraph_id"] not in retrieval.paragraphs and added >= CONCEPT_PARAGRAPHS:
            continue
        definition = _concepts().get(link["concept"], {})
        via = (
            f"requirement term '{link['entity']}' is an instance of the defined term "
            f"'{link['concept']}' ({provision_label(definition.get('definition_id', 'art:3'))}), "
            f"which Article {paragraph['article_num']} uses"
        )
        added += retrieval.add(paragraph, via)
    return links


def _add_vector_provisions(retrieval: _Retrieval, embedding: list[float], via: str) -> None:
    paragraphs = find_paragraphs(embedding, top_k=VECTOR_CANDIDATES)
    binding = [p for p in paragraphs if p["obligation_type"] in BINDING_OBLIGATION_TYPES]
    for paragraph in binding[:VECTOR_PARAGRAPHS]:
        retrieval.add(paragraph, via)


def _add_referenced_provisions(retrieval: _Retrieval) -> None:
    """Follow references from the supplied provisions, and record Annex III scope."""
    # Most relevant sources first: with every paragraph of the routed articles
    # supplied, query order would let incidental references take the slots
    references = sorted(
        get_referenced_provisions(list(retrieval.paragraphs)),
        key=lambda reference: retrieval.paragraphs.get(
            _paragraph_of(reference["source_id"]), {}).get("score") or 0,
        reverse=True,
    )
    added = 0
    for reference in references:
        source_id = reference["source_id"]
        target_id = reference["target_id"]

        if target_id.startswith("annex:III:"):
            scope = retrieval.scope.setdefault(_paragraph_of(source_id), [])
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

    mentioned = {
        name for paragraph in retrieval.paragraphs.values()
        for name in _concepts_in(paragraph["paragraph_text"] or "")
    }
    # The requirement's own terms first, then the most specific (least used) terms
    ranked = list(retrieval.requirement_concepts) + sorted(
        mentioned - set(retrieval.requirement_concepts),
        key=lambda name: int(concepts[name]["article_count"] or 0),
    )
    retrieval.definitions = {
        name: concepts[name] for name in ranked[:MAX_DEFINITIONS] if name in concepts
    }


def _retrieve(requirement_id: str, requirement_text: str, system: SystemContext) -> _Retrieval:
    """Collect the provisions for a requirement, recording how each was reached."""
    embedding = embed_text(requirement_text)
    retrieval = _Retrieval(annex_iii_points=list(system.annex_iii_points))

    if RETRIEVAL_MODE == "vector":
        for paragraph in find_paragraphs(embedding, top_k=VECTOR_PARAGRAPHS):
            retrieval.add(paragraph, "vector similarity to the requirement")
        return retrieval

    retrieval.routed_articles = _route(requirement_text, system)
    _add_routed_provisions(retrieval, embedding)
    links = _add_concept_provisions(retrieval, requirement_id, embedding)

    # Vector search only when the graph routes found nothing
    if not retrieval.paragraphs:
        _add_vector_provisions(
            retrieval, embedding, "vector similarity to the requirement (fallback)")

    _add_referenced_provisions(retrieval)
    _select_definitions(retrieval, requirement_text, links)
    return retrieval


def _build_prompt(
    requirement_id: str,
    requirement_text: str,
    retrieval: _Retrieval,
    related_requirements: list[dict],
    system: SystemContext,
) -> str:
    parts = [
        f"## Requirement {requirement_id}\n",
        f"{requirement_text}\n",
        "\n## System this requirement belongs to\n",
        *(f"{line}\n" for line in _system_lines(system)),
    ]

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
                parts.append(f"  Scope: refers to {_labels(scope)}\n")

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

    # The whole SRS, so a gap another requirement already covers isn't flagged
    # as missing, and severity can reflect whether anything addresses it
    shown = {requirement_id} | {related["id"] for related in related_requirements}
    rest = [(other_id, text) for other_id, text in system.requirements if other_id not in shown]
    if rest and len(system.requirements) <= MAX_SRS_REQUIREMENTS:
        parts.append("\n## Rest of the SRS\n")
        parts.extend(f"- **{other_id}**: {text}\n" for other_id, text in rest)

    parts.append("\nIdentify the compliance risks for this requirement "
                 "based on the provisions above.")

    return "".join(parts)


def _labels(node_ids: list[str]) -> str:
    return ", ".join(provision_label(node_id) for node_id in node_ids)


def _normalise_category(value: str) -> str:
    return value.strip().lower().replace(" ", "_").replace("-", "_")


def _parse_assessment(raw: dict | list) -> RequirementRisk:
    """Validate the model's JSON, salvaging what it can from malformed output."""
    if not isinstance(raw, dict):
        return RequirementRisk(summary=str(raw))

    try:
        return RequirementRisk.model_validate(raw)
    except ValidationError:
        pass

    for key in ("answer", "response", "result", "assessment", "data"):
        nested = raw.get(key)
        if isinstance(nested, dict) and "summary" in nested:
            try:
                return RequirementRisk.model_validate(nested)
            except ValidationError:
                pass

    summary = raw.get("summary", "")
    if not isinstance(summary, str) or not summary:
        summary = next(
            (value for value in raw.values() if isinstance(value, str) and len(value) > 20), "")

    # One malformed risk shouldn't discard the others
    risks = []
    for item in raw.get("risks", []) if isinstance(raw.get("risks"), list) else []:
        try:
            risks.append(RiskItem.model_validate(item))
        except ValidationError:
            pass
    recommendations = raw.get("recommendations", [])
    if not isinstance(recommendations, list):
        recommendations = []

    risk_level = raw.get("risk_level", "medium")
    if risk_level not in RISK_LEVELS:
        risk_level = "medium"

    return RequirementRisk(
        summary=summary or "Model did not produce a valid risk assessment.",
        risks=risks,
        risk_level=risk_level,
        recommendations=[str(item) for item in recommendations],
    )


def _remove_duplicate_risks(assessment: RequirementRisk) -> None:
    seen: set[tuple[str, str, int | None, str]] = set()
    unique: list[RiskItem] = []
    for risk in assessment.risks:
        key = (
            risk.description.strip().lower(),
            risk.article_id,
            risk.paragraph_num,
            _normalise_category(risk.obligation_category),
        )
        if key not in seen:
            seen.add(key)
            unique.append(risk)
    assessment.risks = unique


def _scopes_overlap(point_a: str, point_b: str) -> bool:
    # annex:III:4 covers annex:III:4:a and vice versa
    return point_a == point_b or point_a.startswith(f"{point_b}:") or point_b.startswith(f"{point_a}:")


def _trace_citations(assessment: RequirementRisk, retrieval: _Retrieval) -> None:
    """Resolve each risk's citation to a graph node and record how it was reached."""
    for risk in assessment.risks:
        found = RE_PROVISION_ID.search(risk.provision_id or "")
        if found:
            risk.provision_id = found.group(0)
        elif risk.article_id and risk.paragraph_num is not None:
            risk.provision_id = f"{risk.article_id}:p{risk.paragraph_num}"

    cited = {risk.provision_id for risk in assessment.risks if risk.provision_id}
    provisions = get_provisions(sorted(cited | {_paragraph_of(node_id) for node_id in cited}))
    definitions_by_id = {
        concept["definition_id"]: name for name, concept in retrieval.definitions.items()}
    supplied = set(retrieval.paragraphs) | set(definitions_by_id)
    concepts = _concepts()

    for risk in assessment.risks:
        if not risk.provision_id:
            risk.citation_supplied = False
            risk.trace = ["no provision id was given for this risk"]
            continue

        paragraph_id = _paragraph_of(risk.provision_id)
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
            # Skip terms the concept route above already explains
            if name in retrieval.requirement_concepts and not any(
                    f"'{name}'" in step for step in risk.trace):
                risk.trace.append(
                    f"{retrieval.requirement_concepts[name]} "
                    f"({provision_label(concepts[name]['definition_id'])}), "
                    f"which this provision uses")

        scope = retrieval.scope.get(paragraph_id, [])
        if scope and retrieval.annex_iii_points and not any(
                _scopes_overlap(point_id, classified)
                for point_id in scope for classified in retrieval.annex_iii_points):
            risk.scope_warning = (
                f"{provision_label(paragraph_id)} refers to {_labels(scope)}, but this "
                f"requirement's system was classified under "
                f"{_labels(retrieval.annex_iii_points)}."
            )


def _record_retrieval_steps(assessment: RequirementRisk, retrieval: _Retrieval) -> None:
    """Attach the classification and article selection, where every trace starts."""
    index = _act_index()
    assessment.classification = [
        f"{provision_label(point_id)} ({point_id}): "
        f"{_annex_point_summary(point_id, index.annex_texts.get(point_id, ''))}"
        for point_id in retrieval.annex_iii_points
    ]
    assessment.selected_articles = [
        f"{provision_label(article_id)} {index.titles.get(article_id, '')} ({article_id})"
        for article_id in retrieval.routed_articles
    ]


def _not_assessed(summary: str, retrieval: _Retrieval) -> RequirementRisk:
    # "unknown" rather than "low", so a failure can't pass as a clean result
    assessment = RequirementRisk(summary=summary, risk_level="unknown")
    _record_retrieval_steps(assessment, retrieval)
    return assessment


def assess_requirement(
    requirement_id: str,
    requirement_text: str,
    system: SystemContext | None = None,
) -> tuple[RequirementRisk, dict]:
    """
    Assess a single requirement against the EU AI Act graph.

    :param system: from classify_system over the whole SRS; without it the
        requirement is classified, and assessed, on its own.
    :return: (assessment, raw model output plus the retrieval record).
    """
    system = system or classify_system([(requirement_id, requirement_text)])
    retrieval = _retrieve(requirement_id, requirement_text, system)

    # With nothing retrieved the model can only say "no gap"; report that as
    # not assessed so a broken or unenriched graph can't pass as low risk
    if not retrieval.paragraphs:
        assessment = _not_assessed(
            "Not assessed: no EU AI Act provisions were retrieved from the graph for "
            "this requirement. Check that the graph is built and enriched "
            "(paragraph obligation types are needed to find binding provisions).",
            retrieval,
        )
        return assessment, {"retrieval": retrieval.record(), "not_assessed": True}

    try:
        related_requirements = get_related_requirements(
            requirement_id, limit=MAX_RELATED_REQUIREMENTS)
    except (KeyError, ValueError):
        related_requirements = []

    prompt = _build_prompt(
        requirement_id, requirement_text, retrieval, related_requirements, system)

    try:
        raw = complete_json(prompt=prompt, system=RISK_ASSESSMENT_PROMPT, max_tokens=MAX_TOKENS)
    except ValueError:
        assessment = _not_assessed(
            "Assessment failed: the model did not return valid JSON, "
            "so this requirement was not assessed.",
            retrieval,
        )
        return assessment, {"retrieval": retrieval.record(), "fallback_used": True}

    assessment = _parse_assessment(raw)
    _remove_duplicate_risks(assessment)
    _trace_citations(assessment, retrieval)
    _record_retrieval_steps(assessment, retrieval)
    return assessment, {"retrieval": retrieval.record(), "response": raw}

"""
CLI entry point for eu-ai-risks.
"""

import json
import os
from pathlib import Path

import typer
from dotenv import load_dotenv

load_dotenv()

app = typer.Typer(help="Parse the EU AI Act into a Neo4j graph and query it.")


def _parse_and_build() -> tuple[dict, list]:
    """Parse the PDF and build the in-memory graph."""
    from eu_ai_risks.legislation.eu_ai_act.parser import extract_segments
    from eu_ai_risks.legislation.eu_ai_act.graph_builder import (
        build_in_memory_graph,
        SEGMENT_TYPES,
    )

    pdf_path = Path(os.environ["PDF_PATH"])
    print(f"Parsing {pdf_path} ...")
    segments = extract_segments(pdf_path)

    nodes, edges = build_in_memory_graph(segments)

    for segment_type, type_config in SEGMENT_TYPES.items():
        node_count = sum(
            1 for node_properties in nodes.values() if
            node_properties["type"] == segment_type
        )
        print(f"  {node_count} {type_config['label']} nodes.")
    print(f"  {len(edges)} edges total.")

    return nodes, edges


@app.command()
def reset(confirm: bool = typer.Option(
        False,
        "--confirm",
        help="Required to prevent accidental deletion."
)):
    """Delete all nodes and relationships from the Neo4j database."""
    if not confirm:
        typer.echo("Pass --confirm to reset the graph.")
        raise typer.Exit(1)

    from eu_ai_risks.db import get_session
    with get_session() as session:
        session.run("MATCH (n) DETACH DELETE n")
    print("Graph cleared.")


@app.command()
def build():
    """Parse the EU AI Act PDF and write the graph to Neo4j."""
    from eu_ai_risks.db import NEO4J_URI
    from eu_ai_risks.legislation.eu_ai_act.graph_builder import write_to_neo4j

    nodes, edges = _parse_and_build()

    print(f"\nWriting graph to Neo4j at {NEO4J_URI} ...")
    write_to_neo4j(nodes, edges)


@app.command()
def embed():
    """Generate embeddings and write them to Neo4j."""
    from eu_ai_risks.legislation.eu_ai_act.graph_builder import (
        generate_and_write_embeddings,
    )

    nodes, _ = _parse_and_build()

    print("\nGenerating embeddings ...")
    generate_and_write_embeddings(nodes)


@app.command("obligation-types")
def obligation_types():
    """Classify and annotate Paragraph nodes with an obligation_type
    property."""
    from eu_ai_risks.legislation.eu_ai_act.enrichment import add_obligation_types

    print("Classifying paragraph obligation types ...")
    add_obligation_types()


@app.command()
def concepts():
    """Extract Concept nodes from Art 3 and write DEFINES/USES edges to
    all articles."""
    from eu_ai_risks.legislation.eu_ai_act.enrichment import add_concepts

    print("Extracting concepts ...")
    add_concepts()


@app.command()
def dimensions():
    """Tag provisions with responsible-party, requirement, risk, system, and
    data dimension nodes."""
    from eu_ai_risks.legislation.eu_ai_act.dimensions import add_dimensions

    print("Tagging provisions with dimensions ...")
    add_dimensions()


@app.command()
def enrich():
    """Run all enrichment passes: obligation-types, concepts, dimensions."""
    obligation_types()
    concepts()
    dimensions()


@app.command("all")
def run_all():
    """Build the graph, generate embeddings, and run all enrichment passes."""
    from eu_ai_risks.db import NEO4J_URI
    from eu_ai_risks.legislation.eu_ai_act.graph_builder import (
        write_to_neo4j, generate_and_write_embeddings,
    )

    nodes, edges = _parse_and_build()

    print(f"\nWriting graph to Neo4j at {NEO4J_URI} ...")
    write_to_neo4j(nodes, edges)

    print("\nGenerating embeddings ...")
    generate_and_write_embeddings(nodes)

    print("\nEnriching ...")
    enrich()


@app.command()
def chapter(chapter_id: str = typer.Argument(help="e.g. ch:III")):
    """List articles in a chapter."""
    from eu_ai_risks.db.graph import articles_in_chapter

    for article_id, title in articles_in_chapter(chapter_id):
        print(f"  {article_id}: {title}")


@app.command()
def refs(article_id: str = typer.Argument(help="e.g. art:6")):
    """List articles that reference the given article."""
    from eu_ai_risks.db.graph import referenced_by

    for ref_id, title in referenced_by(article_id):
        print(f"  {ref_id}: {title}")


@app.command("refs-from")
def refs_from(article_id: str = typer.Argument(help="e.g. art:5")):
    """List articles that the given article references."""
    from eu_ai_risks.db.graph import references_from

    for ref_id, title in references_from(article_id):
        print(f"  {ref_id}: {title}")


@app.command()
def path(
        source: str = typer.Argument(help="e.g. art:5"),
        target: str = typer.Argument(help="e.g. art:85"),
):
    """Find the shortest reference path between two articles."""
    from eu_ai_risks.db.graph import shortest_path

    reference_path = shortest_path(source, target)
    if reference_path:
        print(" -> ".join(reference_path))
    else:
        print("No path found.")


@app.command()
def search(
        query: str = typer.Argument(help="Natural language search query"),
        top_k: int = typer.Option(5, help="Number of results"),
        paragraphs: bool = typer.Option(
            False,
            "--paragraphs", "-p",
            help="Search paragraphs instead of articles"
        ),
):
    """Semantic search over articles or paragraphs."""
    from eu_ai_risks.db.graph import (
        vector_search_articles,
        vector_search_paragraphs,
    )
    from eu_ai_risks.embeddings import embed_text

    query_embedding = embed_text(query)

    if paragraphs:
        results = vector_search_paragraphs(query_embedding, top_k)
        for para_id, num, score in results:
            print(f"  {para_id} (para {num})  score: {score:.4f}")
    else:
        results = vector_search_articles(query_embedding, top_k)
        for article_id, title, score in results:
            print(f"  {article_id}: {title}  score: {score:.4f}")


@app.command("load-requirements")
def load_requirements(
        document_path: Path = typer.Argument(
            help="Path to a .txt, .md, .pdf, or .docx SRS"),
):
    """Extract requirements, split into triples, and write to Neo4j."""
    from eu_ai_risks.requirements.loader import write_triples

    print(f"Loading requirements from {document_path} ...")
    write_triples(document_path)
    print("Done.")


@app.command("assess-risks")
def assess_risks(
    document_path: Path = typer.Argument(
        help="Path to a requirements document (.txt, .md, .pdf, .docx)",
    ),
    output: Path = typer.Option(
        Path("risk-assessment.md"),
        "--output", "-o",
        help="Markdown report output path",
    ),
    agent: bool = typer.Option(
        False, "--agent",
        help="Use multi-turn agent loop (slower, more thorough)",
    ),
    skip_load: bool = typer.Option(
        False, "--skip-load",
        help="Skip loading requirements to graph (use if already loaded)",
    ),
    verbose: bool = typer.Option(
        False, "--verbose", "-v",
        help="Print raw LLM output for each requirement",
    ),
):
    """Load requirements into the graph and assess EU AI Act compliance risks."""
    if verbose:
        import logging
        logging.basicConfig(level=logging.DEBUG, format="%(name)s: %(message)s")

    from eu_ai_risks.requirements.loader import write_triples
    from eu_ai_risks.db.graph import list_requirements, list_categories
    from eu_ai_risks.analysis.risk_report import (
        collect_citations, entries_from_assessments,
        write_markdown_report,
    )

    if not skip_load:
        print(f"Loading requirements from {document_path} ...")
        write_triples(document_path)

    requirements = list_requirements()
    if not requirements:
        print("No requirements found in the graph.")
        raise typer.Exit(1)

    print(f"Found {len(requirements)} requirements in graph.")

    if agent:
        from eu_ai_risks.analysis.risk_assessor_agent import assess_requirement
    else:
        from eu_ai_risks.analysis.risk_assessor import assess_requirement

    categories = list_categories()
    article_cache: dict[str, dict] = {}

    assessment_entries: list[dict] = []
    for i, requirement in enumerate(requirements, 1):
        req_id = requirement["id"]
        req_text = requirement["text"]
        print(f"  [{i}/{len(requirements)}] {req_id}...")

        assessment, fetched_articles, raw = assess_requirement(
            req_id, req_text, categories=categories,
        )
        article_cache.update(fetched_articles)
        citations = collect_citations(assessment.risks, article_cache)

        if verbose:
            print(f"    Raw: {json.dumps(raw, indent=2)}")
            print()

        assessment_entries.append({
            "requirement": requirement,
            "assessment": assessment,
            "citations": citations,
        })

    entries = entries_from_assessments(assessment_entries)
    write_markdown_report(entries, output)
    print(f"Wrote {output}")


@app.command("ask")
def ask(
        query: str = typer.Argument(help="Question about the EU AI Act"),
        verbose: bool = typer.Option(
            False, "--verbose", "-v",
            help="Show tool calls and iteration count",
        ),
):
    """Ask a question about the EU AI Act using the knowledge graph."""
    from eu_ai_risks.analysis.agent import AgentLoop
    from eu_ai_risks.analysis.tools import TOOL_DEFINITIONS, execute_tool
    from eu_ai_risks.analysis.prompts import GRAPH_READER_PROMPT

    agent = AgentLoop(
        system_prompt=GRAPH_READER_PROMPT,
        tools=TOOL_DEFINITIONS,
        tool_executor=execute_tool,
    )

    if verbose:
        print("Running agent...")

    result = agent.run(query)

    if verbose:
        print(
            f"\n[{result.iterations} iterations, "
            f"{result.tool_calls_made} tool calls]\n"
        )

    print(result.answer.summary)

    if result.answer.citations:
        print("\nCitations:")
        for citation in result.answer.citations:
            label = citation.article_title or citation.article_id
            if citation.paragraph_num:
                label += f"({citation.paragraph_num})"
            print(f"  - {label}")

    if verbose:
        print(f"\nConfidence: {result.answer.confidence}")
        print(f"\nRaw output: {result.raw_content}")


def main():
    app()


if __name__ == "__main__":
    main()

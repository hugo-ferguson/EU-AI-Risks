# EU AI Risks

Parse the [EU AI Act](https://eur-lex.europa.eu/eli/reg/2024/1689/oj) into a Neo4j knowledge graph, then assess software requirements against it for compliance risks.

The tool builds a graph of the full regulation (chapters, articles, paragraphs, annexes, cross-references) and layers on semantic embeddings, obligation types, and controlled-vocabulary dimensions. You can then feed in a software requirements document and get back a report of where each requirement might fall short of the Act.

## Setup

**You'll need:**

- Python 3.12+
- A Neo4j instance ([Neo4j Aura Free](https://neo4j.com/cloud/aura-free/) works)
- A copy of the [EU AI Act PDF](https://eur-lex.europa.eu/eli/reg/2024/1689/oj)
- An LLM endpoint: Ollama, Anthropic, OpenAI, or any [LiteLLM](https://docs.litellm.ai/)-compatible provider

```bash
pip install -e .
```

Copy `.env.example` to `.env` and fill in your values:

```
PDF_PATH=~/path/to/eu_ai_act.pdf

NEO4J_URI=bolt://localhost:7687
NEO4J_USERNAME=neo4j
NEO4J_PASSWORD=password

HF_TOKEN=token

LLM_MODEL=ollama_chat/qwen3:32b
LLM_API_BASE=http://localhost:11434
```

`HF_TOKEN` speeds up the first embedding model download. `LLM_MODEL` is needed for enrichment, risk assessment, and the `ask` command. Any [LiteLLM](https://docs.litellm.ai/)-compatible model string works (e.g. `anthropic/claude-sonnet-4-20250514`, `ollama_chat/qwen3:32b`). Anthropic models get automatic prompt caching.

## Building the graph

Build, embed, and enrich in one go:

```bash
eu-ai-risks all
```

Or run the steps individually:

```bash
eu-ai-risks build       # Parse the PDF into a Neo4j graph
eu-ai-risks embed       # Generate vector embeddings
eu-ai-risks enrich      # Tag obligation types, concepts, dimensions
```

`enrich` runs three sub-passes: `obligation-types` and `concepts` (need the LLM) and `dimensions` (deterministic). Each can be run on its own.

To start fresh: `eu-ai-risks reset --confirm`

## Querying the graph

```bash
eu-ai-risks chapter ch:III                    # Articles in a chapter
eu-ai-risks refs art:6                        # What references this article
eu-ai-risks refs-from art:5                   # What this article references
eu-ai-risks path art:5 art:85                 # Shortest reference path
eu-ai-risks search "human oversight"          # Semantic search over articles
eu-ai-risks search -p "biometric data" -k 10  # Search paragraphs instead
```

## Asking questions

The `ask` command runs an LLM agent that reads the knowledge graph with tool calls. It can search, follow cross-references, and read articles to answer questions about the Act:

```bash
eu-ai-risks ask "What obligations exist for logging in high-risk AI systems?"
eu-ai-risks ask "How does Article 14 relate to Article 9?" --verbose
```

## Risk assessment

Point `assess-risks` at a requirements document. It extracts requirements, loads them into the graph as semantic triples, then assesses each one against the Act:

```bash
eu-ai-risks assess-risks ./examples/requirements/sample-srs.md
```

This outputs a Markdown report (`risk-assessment.md` by default) with specific risks, cited provisions, and recommendations per requirement.

**Options:**

```bash
eu-ai-risks assess-risks ./my-srs.pdf -o report.md      # Custom output path
eu-ai-risks assess-risks ./my-srs.md --agent             # Multi-turn agent loop
eu-ai-risks assess-risks ./my-srs.md --skip-load         # Skip if requirements already in graph
eu-ai-risks assess-risks ./my-srs.md --verbose           # Print raw LLM output
```

Supported input formats: `.txt`, `.md`, `.pdf`, `.docx`.

### Deterministic vs agent

By default, `assess-risks` uses a **deterministic pipeline**: it pre-fetches context from the graph (vector search, article text, cross-references), then makes a single LLM call per requirement. This is faster and works well with smaller models.

Pass `--agent` to use the **multi-turn agent loop** instead, where the LLM decides which tools to call and can explore the graph iteratively. More thorough but slower and needs a capable model (qwen3:32b or better, or an Anthropic/OpenAI model).

### Loading requirements separately

If you just want to load requirements into the graph without running the assessment:

```bash
eu-ai-risks load-requirements ./my-srs.md
```

Then run the assessment later with `--skip-load`:

```bash
eu-ai-risks assess-risks ./my-srs.md --skip-load
```

## Graph structure

The knowledge graph contains:

- **Chapters** (13), **Sections**, **Articles** (113), **Paragraphs** (574)
- **Annexes** (13), cross-referenced by articles
- **Concepts** (68), defined in Article 3
- **14 RequirementCategory nodes**: the backbone of the Act's obligations (risk management, human oversight, data governance, etc.), each linked to its anchor articles
- **Dimension nodes**: ResponsibleParty, RiskCategory, SystemCategory, DataCategory

Node IDs follow the pattern `ch:III`, `sec:III:2`, `art:6`, `art:6:p2`, `annex:III`.

Each paragraph is tagged with an `obligation_type`: requirement, prohibition, permission, definition, scope, or informational.

When requirements are loaded, the graph also gets Requirement and Entity nodes with semantic triple edges, so related requirements can be found through shared entities.

## Project structure

```
eu_ai_risks/
  cli.py                              # CLI entry point (Typer)
  db/
    session.py                        # Neo4j driver
    graph.py                          # Graph queries
  embeddings/
    client.py                         # Sentence-transformers (bge-base-en-v1.5)
  llm/
    client.py                         # LiteLLM wrapper with prompt caching
  legislation/
    eu_ai_act/
      models.py                       # Segment data structure
      parser.py                       # PDF parsing
      graph_builder.py                # Graph construction and Neo4j writes
      enrichment.py                   # Obligation types, Article 3 concepts
      dimensions.py                   # Controlled-vocabulary dimension tagging
  requirements/
    models.py                         # Requirement data structure
    loader.py                         # Document parsing, triple extraction
  analysis/
    models.py                         # Assessment and agent data structures
    agent.py                          # Tool-calling agent loop
    tools.py                          # Graph tool definitions and dispatch
    prompts.py                        # System prompts
    risk_assessor.py                  # Deterministic assessment pipeline
    risk_assessor_agent.py            # Agent-based assessment pipeline
    risk_report.py                    # Markdown report generation
```

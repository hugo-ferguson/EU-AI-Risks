# EU AI Risks

Parse the [EU AI Act](https://eur-lex.europa.eu/eli/reg/2024/1689/oj) into a Neo4j graph database, generate semantic embeddings, and query the legislation structure.

## Overview

The tool parses the EU AI Act PDF into a graph of **chapters**, **sections**, **articles**, **paragraphs**, and **annexes**, with edges for containment (`CONTAINS`, `HAS_PARAGRAPH`) and cross-references (`REFERENCES`). Articles and paragraphs are then tagged with a semantic layer: Article 3 concepts, paragraph obligation types, and five controlled-vocabulary dimensions (responsible party, requirement, risk, system, and data category). Embeddings are generated using [sentence-transformers](https://www.sbert.net/) (`BAAI/bge-base-en-v1.5`) for semantic search over the legislation.

## Graph structure

Node labels: `Chapter`, `Section`, `Article`, `Paragraph`, `Annex`, `Concept`, and the five dimension labels `ResponsibleParty`, `RequirementCategory`, `RiskCategory`, `SystemCategory`, `DataCategory`.

Edges:

- `CONTAINS`: chapter to section, section to article, chapter to article
- `HAS_PARAGRAPH`: article to paragraph
- `REFERENCES`: article or annex to the articles and annexes it cites
- `DEFINES` / `USES`: a paragraph defines an Article 3 concept, an article uses one
- `ADDRESSES`, `IMPOSES`, `HAS_RISK`, `COVERS`, `CONCERNS`: a provision to its dimension nodes

Node IDs follow the pattern `ch:III`, `sec:III:2`, `art:6`, `art:6:p2`, `annex:III`.

Each dimension is a closed vocabulary drawn from the Act (Article 3 definitions, the Article 9-15 requirement titles, the chapter and Annex III scheme). Tagging is deterministic.

## Setup

### Requirements

- Python 3.12+
- A Neo4j instance (e.g. [Neo4j Aura](https://neo4j.com/cloud/aura-free/))
- A copy of the EU AI Act PDF
- (Optional) A [Hugging Face token](https://huggingface.co/settings/tokens) for faster model downloads

### Installation

```bash
pip install -e .
```

### Configuration

Copy `.env.example` to `.env` and fill in your values:

```
PDF_PATH=~/path/to/eu_ai_act.pdf

NEO4J_URI=bolt://localhost:7687
NEO4J_USERNAME=neo4j
NEO4J_PASSWORD=password

HF_TOKEN=token

LLM_MODEL=ollama/llama3.2
LLM_API_BASE=http://localhost:11434
```

`LLM_MODEL` and `LLM_API_BASE` are only needed for the LLM enrichment passes (obligation types and concepts). Any [LiteLLM](https://docs.litellm.ai/)-compatible model works.

## Usage

### Build everything

Run build, embed, and enrich in one step:

```bash
eu-ai-risks all
```

The individual steps are also available:

### Build the graph

Parse the PDF and write chapters, sections, articles, paragraphs, annexes, and their relationships to Neo4j:

```bash
eu-ai-risks build
```

### Generate embeddings

Generate and store vector embeddings for articles, paragraphs, and annexes:

```bash
eu-ai-risks embed
```

### Enrich the graph

Tag the graph with risk tiers, obligation types, Article 3 concepts, and the five dimensions:

```bash
eu-ai-risks enrich
```

The individual passes `tiers`, `obligation-types`, `concepts`, and `dimensions` can be run on their own. `dimensions` is deterministic and needs no LLM; `obligation-types` and `concepts` require `LLM_MODEL`.

### Query the graph

List articles in a chapter:

```bash
eu-ai-risks chapter ch:III
```

Find articles that reference a given article:

```bash
eu-ai-risks refs art:6
```

Find articles that a given article references:

```bash
eu-ai-risks refs-from art:5
```

Find the shortest reference path between two articles:

```bash
eu-ai-risks path art:5 art:85
```

### Semantic search

Search for articles relevant to a natural language query:

```bash
eu-ai-risks search "prohibited artificial intelligence practices"
```

Search paragraphs instead:

```bash
eu-ai-risks search -p "biometric identification" --top-k 10
```

This can be used to find legislation relevant to a given requirement, e.g.:

```bash
eu-ai-risks search "The system shall log all automated decisions for human review"
```

## Project structure

```
eu_ai_risks/
  cli.py                              # CLI entry point (typer)
  models.py                           # Shared data structures
  db/
    session.py                        # Neo4j connection management
    graph.py                          # Graph query operations
  embeddings/
    client.py                         # Sentence-transformers wrapper
  llm/
    client.py                         # LiteLLM wrapper for enrichment
  legislation/
    eu_ai_act/
      parser.py                       # PDF parsing into segments
      graph_builder.py                # Graph construction and Neo4j writes
      enrichment.py                   # Risk tiers, obligation types, concepts
      dimensions.py                   # Controlled-vocabulary dimension tagging
  requirements/                       # (planned) Requirement parsing
  analysis/                           # (planned) Requirement-to-legislation mapping
```

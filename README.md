# EU AI Risks

Parse the [EU AI Act](https://eur-lex.europa.eu/eli/reg/2024/1689/oj) into a Neo4j graph database, generate semantic embeddings, query the legislation structure, and map software requirements documents to candidate EU AI Act compliance risks.

## Overview

The tool parses the EU AI Act PDF into a graph of **chapters**, **articles**, and **paragraphs**, with edges representing containment (`CONTAINS`, `HAS_PARAGRAPH`) and cross-references (`REFERENCES`) between articles. Embeddings are generated using [sentence-transformers](https://www.sbert.net/) (`BAAI/bge-base-en-v1.5`) to enable semantic search over the legislation.

The requirements analysis pipeline extracts candidate software requirements from an SRS document, embeds each requirement, retrieves similar EU AI Act paragraphs from Neo4j, classifies likely risk themes, and writes a traceable Markdown/JSON report.

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
```

## Usage

### Build the graph

Parse the PDF and write chapters, articles, paragraphs, and their relationships to Neo4j:

```bash
eu-ai-risks build
```

### Generate embeddings

Generate and store vector embeddings for articles and paragraphs:

```bash
eu-ai-risks embed
```

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

### Requirements analysis

Extract candidate requirements from a software requirements document:

```bash
eu-ai-risks parse-requirements ./sample-srs.pdf
```

Save extracted requirements as JSON:

```bash
eu-ai-risks parse-requirements ./sample-srs.pdf --output extracted-requirements.json
```

Generate a traceable EU AI Act risk report:

```bash
eu-ai-risks analyze-requirements ./sample-srs.pdf --output risk-report.md --json-output risk-report.json
```

The analysis command expects the EU AI Act graph and paragraph embeddings to already exist in Neo4j:

```bash
eu-ai-risks build
eu-ai-risks embed
eu-ai-risks analyze-requirements ./sample-srs.pdf
```

Supported requirements document formats are `.txt`, `.md`, `.pdf`, and `.docx`.

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
  legislation/
    eu_ai_act/
      parser.py                       # PDF parsing into segments
      graph_builder.py                # Graph construction and Neo4j writes
  requirements/
    loader.py                         # Requirement document parsing
    models.py                         # Requirement data structures
  analysis/
    risk_mapper.py                    # Requirement-to-legislation mapping
    risk_report.py                    # Markdown/JSON report generation
```

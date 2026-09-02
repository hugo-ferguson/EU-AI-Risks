# Contribution summary: semantic profile risk assessment + frontend/API

This branch improves the proof-of-concept risk assessment flow for Chapter 3 high-risk AI obligations.

## Main contribution

The risk assessment now uses an intent-aware semantic profile before mapping a software requirement to EU AI Act provisions.

The intended flow is:

```text
requirement -> semantic profile -> obligation category -> graph retrieval -> LLM risk assessment -> report
```

This helps the system avoid relying only on raw semantic similarity between a requirement and legal paragraphs.

## Mapping improvements

The profile layer separates common requirement intents such as:

- data ingestion
- scoring or prediction
- ranking or prioritisation
- explanation/transparency
- human review/override
- logging/audit records
- dataset validation and bias testing
- protected-attribute control
- monitoring/alerts
- rollback/corrective action
- prohibited-feature prevention

These intents guide mapping toward Chapter 3 obligation areas such as Article 10 data governance, Article 12 record-keeping, Article 13 transparency, Article 14 human oversight, Article 15 accuracy/robustness/cybersecurity, Article 9 risk management, and Article 72 post-market monitoring.

The branch also distinguishes missing risks from requirements that already describe safeguards or controls.

## Speed/quality optimisation

The latest update keeps the semantic-profile + retrieval + LLM approach, but reduces local Ollama latency by:

- using embedding-based semantic profiling by default instead of an extra LLM profile call for every requirement;
- caching intent/domain embeddings, category anchors, article reads, and cross-reference reads;
- limiting retrieved context sent to the final LLM call;
- aligning the LLM's output back to the semantic profile scope to reduce category drift;
- keeping invalid-JSON fallback handling so one local model response does not crash the full report.

This is not a keyword-only fast mapper and does not hardcode individual FR/NFR IDs.

## Frontend/API work

The branch also adds a minimal React/Vite frontend and FastAPI endpoint for uploading requirements documents, running the assessment through the existing backend, and viewing results in a dashboard.

The frontend includes:

- requirements document upload;
- risk summary cards including High/Medium/Low counts;
- requirement finding list;
- risk/category filtering;
- mapped obligation details;
- recommended engineering actions;
- demo mode for backup presentations.

## Scope

This contribution is mainly Chapter 3/high-risk AI focused. It does not claim full legal-grade coverage of the entire EU AI Act. Wider Act coverage should be added later by expanding the semantic profile taxonomy and validation set.

# Semantic profile optimisation

This update keeps the full assessment approach:

```text
requirement -> semantic profile -> graph retrieval -> LLM risk assessment -> report
```

It does **not** replace the main mapping with keyword rules or requirement-ID patches. The optimisation focuses on reducing unnecessary local LLM calls while preserving the semantic profile and Chapter 3 obligation-category mapping.

## What changed

### 1. Embedding-based semantic profile by default

The profile step now defaults to `EU_AI_RISKS_PROFILE_MODE=semantic`.

In this mode, the system compares the requirement against stable semantic descriptions of requirement intents, such as scoring, ranking, explanation, human review, logging, dataset validation, protected-attribute control, monitoring, rollback, and prohibited-feature prevention.

This is faster than asking the local LLM to write a full profile for every requirement, but it still profiles by semantic similarity rather than keyword matching.

### 2. One main LLM call per requirement

The old richer path could use one LLM call for profile extraction and another for final risk assessment. The default path now uses embeddings for the semantic profile and keeps the LLM for the final risk explanation.

This reduces latency for Ollama models while keeping the final report natural and useful.

### 3. Cached semantic/profile components

The intent-description embeddings and broad high-risk-domain embeddings are cached for the life of the API process. Article reads, cross-reference reads, and category anchors are also cached where appropriate.

### 4. Smaller, cleaner LLM context

The risk assessment prompt now sends fewer retrieved paragraphs, fewer article paragraphs, and shorter snippets. This helps smaller local models avoid repetitive or invalid JSON responses while still keeping the strongest graph evidence.

### 5. Stronger profile-alignment guard

The final LLM output is aligned back to the semantic profile's assessment scope. This reduces category drift, for example explanation requirements drifting to data governance or monitoring requirements drifting away from post-market monitoring.

## Recommended local settings

For fast local testing with a small Qwen model:

```env
LLM_MODEL=ollama/qwen3:4b
LLM_API_BASE=http://localhost:11434
LLM_TEMPERATURE=0.1
LLM_NUM_RETRIES=1
LLM_TIMEOUT=300

EU_AI_RISKS_PROFILE_MODE=semantic
EU_AI_RISKS_TOP_K_PARAGRAPH_CANDIDATES=8
EU_AI_RISKS_TOP_K_PARAGRAPHS=3
EU_AI_RISKS_TOP_K_ARTICLES=3
EU_AI_RISKS_MAX_PARAGRAPHS_PER_ARTICLE=2
EU_AI_RISKS_RISK_MAX_TOKENS=900
EU_AI_RISKS_WARMUP=true
```

If mapping quality is more important than speed for a final report, use:

```env
EU_AI_RISKS_PROFILE_MODE=hybrid
```

Hybrid mode uses embedding profiling first and only asks the LLM for a richer semantic profile when the embedding profile has low confidence.

## Scope

This optimisation is mainly for Chapter 3/high-risk AI requirement mapping. It improves mappings for obligation areas such as data governance, transparency, human oversight, record-keeping, accuracy/robustness/cybersecurity, risk management, and post-market monitoring.

It does not claim complete coverage of the entire EU AI Act. Wider EU AI Act coverage can be added later by expanding the semantic profile taxonomy and validation set.

# Contribution Summary: Semantic Profile Risk Assessment + Frontend/API

This branch improves the proof-of-concept risk assessment flow for mapping software requirements against the EU AI Act, mainly focused on Chapter 3 high-risk AI obligations.

The goal of this contribution is to make the output more useful as an engineering review aid by improving requirement-to-obligation mapping, reducing over-reliance on raw semantic similarity, and adding a minimal frontend/API flow for demo and testing.

---

## Main Contribution

The risk assessment now uses an intent-aware semantic profile before mapping a software requirement to EU AI Act provisions.

The intended flow is:

```text
requirement -> semantic profile -> obligation category -> graph retrieval -> LLM risk assessment -> report
```

This helps the system avoid relying only on raw semantic similarity between a requirement and legal paragraphs.

Instead of only asking “which EU AI Act paragraph sounds similar to this requirement?”, the system first considers what the requirement is actually doing, then uses that profile to guide the mapping.

---

## Mapping Improvements

The semantic profile layer separates common requirement intents such as:

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

These intents guide mapping toward relevant Chapter 3 obligation areas, including:

- Article 9 — risk management
- Article 10 — data governance
- Article 11 — technical documentation
- Article 12 — record-keeping/logging
- Article 13 — transparency
- Article 14 — human oversight
- Article 15 — accuracy, robustness, and cybersecurity
- Article 72 — post-market monitoring

The branch also distinguishes missing risks from requirements that already describe safeguards or controls.

For example:

```text
logging/audit requirement -> record-keeping control -> low remaining clarification risk
human override requirement -> human oversight safeguard -> remaining reviewer competency gap
biometric prevention requirement -> prohibited-feature safeguard -> no retained requirement-level risk
monitoring alert requirement -> post-market monitoring / risk management
```

---

## Speed and Quality Optimisation

The latest update keeps the full assessment approach:

```text
requirement -> semantic profile -> graph retrieval -> LLM risk assessment -> report
```

It does **not** replace the main mapping with keyword-only rules or requirement-ID patches.

The optimisation focuses on reducing unnecessary local LLM calls while preserving semantic profiling and Chapter 3 obligation-category mapping.

### What changed

1. **Embedding-based semantic profiling by default**

   The profile step now defaults to:

   ```env
   EU_AI_RISKS_PROFILE_MODE=semantic
   ```

   In this mode, the system compares each requirement against stable semantic descriptions of requirement intents. This is faster than asking the local LLM to write a full profile for every requirement, while still being more flexible than simple keyword matching.

2. **One main LLM call per requirement**

   The previous richer path could use one LLM call for profile extraction and another for final risk assessment.

   The default path now uses embeddings for the semantic profile and keeps the LLM for the final risk explanation.

3. **Cached semantic/profile components**

   The system caches intent/domain embeddings, category anchors, article reads, and cross-reference reads where appropriate.

4. **Smaller, cleaner LLM context**

   The risk assessment prompt now sends fewer retrieved paragraphs, fewer article paragraphs, and shorter snippets. This helps smaller local models avoid repetitive or invalid JSON responses while still keeping the strongest graph evidence.

5. **Profile-alignment guard**

   The final LLM output is aligned back to the semantic profile’s assessment scope. This reduces category drift, such as explanation requirements drifting to data governance or monitoring requirements drifting away from post-market monitoring.

6. **Invalid JSON fallback**

   If the local model returns invalid JSON, the assessment does not crash the full report. A conservative fallback is used so the pipeline can continue.

---

## Frontend/API Work

This branch also adds a minimal React/Vite frontend and FastAPI endpoint for uploading requirements documents, running the assessment through the backend, and viewing results in a dashboard.

The frontend includes:

- requirements document upload
- risk summary cards, including High/Medium/Low counts
- requirement finding list
- risk/category filtering
- mapped obligation details
- recommended engineering actions
- demo mode for backup presentations

---

## Running the API

From the repo root:

```bash
pip install -e .
uvicorn eu_ai_risks.api:app --reload --host 0.0.0.0 --port 8000
```

The API exposes:

```text
POST /api/assess-risks
GET  /api/health
```

Open the API docs at:

```text
http://localhost:8000/docs
```

---

## Running the Frontend

From the repo root:

```bash
cd frontend
npm install
npm run dev
```

The frontend runs on:

```text
http://localhost:5174
```

The frontend should have this in `frontend/.env`:

```env
VITE_API_URL=http://localhost:8000
```

---

## Requirements Upload Flow

The frontend accepts requirements files in:

```text
.json, .txt, .md, .markdown, .pdf, .docx
```

Recommended fastest testing format is JSON:

```json
[
  {
    "id": "FR-1",
    "text": "The system shall explain automated decisions to users in plain language."
  }
]
```

The API extracts requirements, runs the semantic-profile risk assessment, and returns frontend-ready findings.

---

## Qwen3 / Ollama Setup

Use Qwen3 for local testing.

Recommended demo balance:

```env
LLM_MODEL=ollama/qwen3:4b
LLM_API_BASE=http://localhost:11434
LLM_TEMPERATURE=0.1
LLM_JSON_NO_THINK=true
LLM_NUM_RETRIES=1
LLM_TIMEOUT=300

EU_AI_RISKS_PROFILE_MODE=semantic
EU_AI_RISKS_WARMUP=true
```

Pull and test the model:

```powershell
ollama pull qwen3:4b
ollama run qwen3:4b
```

Then type:

```text
/bye
```

Speed/quality options:

```env
# Fastest smoke test, weaker mapping
LLM_MODEL=ollama/qwen3:1.7b

# Recommended demo balance
LLM_MODEL=ollama/qwen3:4b

# Better quality, slower
LLM_MODEL=ollama/qwen3:8b
```

There is not usually an Ollama tag called `qwen3:3b` or `qwen3:3.2`. The closest Qwen3 option for this use case is `qwen3:4b`.

---

## Recommended Local Settings

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

For higher quality on difficult examples, use:

```env
EU_AI_RISKS_PROFILE_MODE=hybrid
```

Hybrid mode uses embedding profiling first and only asks the LLM for a richer semantic profile when the embedding profile has low confidence.

---

## Demo Advice

For a live supervisor demo, use a small 3–4 requirement JSON first.

Do not rely on running a full 16-requirement assessment live unless the local model is responding quickly.

Recommended demo plan:

```text
1. Start the API
2. Start the frontend
3. Upload a small requirements JSON
4. Run assessment
5. Review the mapped findings in the dashboard
6. Keep demo mode available as a backup
```

---

## Scope and Limitations

This contribution is mainly Chapter 3/high-risk AI focused.

It improves mappings for obligation areas such as:

- data governance
- transparency
- human oversight
- record-keeping
- accuracy, robustness, and cybersecurity
- risk management
- post-market monitoring

It does **not** claim complete legal-grade coverage of the entire EU AI Act.

Wider EU AI Act coverage should be added later by expanding the semantic profile taxonomy, validation set, and obligation mapping beyond Chapter 3/high-risk AI requirements.

The output should be treated as an engineering review aid, not legal advice.

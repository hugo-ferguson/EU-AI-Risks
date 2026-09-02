# Frontend + API flow

The frontend can upload a requirements document and call the FastAPI backend to run the EU AI Act risk assessment.

## Run the API

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

## Run the frontend

```bash
cd frontend
npm install
npm run dev
```

The frontend runs on:

```text
http://localhost:5174
```

## Upload flow

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

## Performance settings

For local Ollama testing, use the root `.env` settings from `.env.example`. The fastest useful setup is:

```env
LLM_MODEL=ollama/qwen3:4b
EU_AI_RISKS_PROFILE_MODE=semantic
EU_AI_RISKS_WARMUP=true
```

`EU_AI_RISKS_PROFILE_MODE=semantic` reduces latency by using embedding-based semantic profiling and keeping one final LLM call per requirement. For higher quality on difficult examples, switch to:

```env
EU_AI_RISKS_PROFILE_MODE=hybrid
```

## Demo advice

For a live supervisor demo, use a small 3-4 requirement JSON first. Keep demo mode available as a backup because local LLM responses can still be slow on CPU.

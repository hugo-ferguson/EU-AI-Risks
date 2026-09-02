# Frontend + API demo integration

This adds a lightweight API and frontend flow for the proof of concept.

## What changed

- Added `eu_ai_risks/api.py`.
- Added a FastAPI endpoint at `POST /api/assess-risks`.
- The endpoint accepts an uploaded requirements document.
- Supported uploads: `.json`, `.txt`, `.md`, `.pdf`, `.docx`.
- The API extracts requirement-like statements and runs the existing semantic-profile risk assessment pipeline.
- The frontend now uploads a requirements document instead of requiring JSON copy/paste.
- The frontend still supports uploading a generated Markdown report for viewing only.

## Run backend

From the project root:

```bash
uvicorn eu_ai_risks.api:app --reload --host 0.0.0.0 --port 8000
```

The backend requires the same environment as the CLI pipeline, including Neo4j and LLM configuration.

## Run frontend

```bash
cd frontend
npm install
```

Create `frontend/.env`:

```bash
VITE_API_URL=http://localhost:8000
```

Then run:

```bash
npm run dev
```

Open:

```text
http://localhost:5174/
```

## Current demo limitation

The API runs the assessment in the request/response cycle. For a small requirements file this is fine for the POC, but a full production version should use a background job queue with progress updates.


## Qwen3 / faster local model option

For a faster local model, pull Qwen3 with Ollama and update `.env`:

```bash
ollama pull qwen3:8b
```

```env
LLM_MODEL=ollama/qwen3:8b
LLM_API_BASE=http://localhost:11434
LLM_TEMPERATURE=0.2
LLM_JSON_NO_THINK=true
```

Restart the Python API after changing `.env`. If 8B is still too slow, try `ollama/qwen3:4b` for demo testing.

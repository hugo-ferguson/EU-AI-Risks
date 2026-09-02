# Using Qwen3 with the EU AI Risks pipeline

This project uses LiteLLM, so switching models is mainly an `.env` change. For a faster local demo, Qwen3 8B is a good first option; Qwen3 4B is faster but may be less accurate.

## 1. Pull/run the model in Ollama

```bash
ollama pull qwen3:8b
ollama run qwen3:8b
```

Keep Ollama running. If Ollama is on another team member's machine, keep their existing IP in `LLM_API_BASE` instead of using localhost.

## 2. Update `.env`

```env
LLM_MODEL=ollama/qwen3:8b
LLM_API_BASE=http://localhost:11434
LLM_TEMPERATURE=0.2
LLM_JSON_NO_THINK=true
```

If 8B is still too slow for the frontend demo, try:

```env
LLM_MODEL=ollama/qwen3:4b
```

## 3. Restart the API

```bash
uvicorn eu_ai_risks.api:app --reload --host 0.0.0.0 --port 8000
```

The LLM client now strips Qwen-style `<think>...</think>` blocks and tries to extract valid JSON from fenced or slightly wrapped responses. This is mainly to make local Qwen/Ollama runs less likely to crash the assessment pipeline.

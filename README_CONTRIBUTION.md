# UI polish + Qwen3 support bundle

This bundle updates the frontend/API demo layer with the following changes:

- Removes the top-level **Upload generated report** button so the main demo flow is now requirements document upload -> run assessment -> review dashboard.
- Keeps **Load demo** for quick supervisor/demo viewing.
- Adds a visible **High = 0** summary card instead of hiding high risk when there are no high findings.
- Replaces the star-style logo with a cleaner compliance/checklist icon using the existing Lucide icon set.
- Updates frontend README wording so it matches the new requirements-document upload flow.
- Adds Qwen3/Ollama configuration notes in `README_QWEN3.md`.
- Improves the LLM JSON parsing path so Qwen-style `<think>...</think>` blocks, markdown fences, or wrapped JSON are less likely to crash the pipeline.

## Files changed

```text
frontend/src/App.jsx
frontend/src/styles.css
frontend/README.md
eu_ai_risks/llm/client.py
.env.example
README_QWEN3.md
README_FRONTEND_API.md
```

## Suggested commit message

```bash
git commit -m "Polish frontend flow and add Qwen3 JSON handling"
```

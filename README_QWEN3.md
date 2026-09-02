# Qwen3 / Ollama setup

Use Qwen3 for local testing. For this semantic optimised branch, the recommended balance is `qwen3:4b`. It should be faster than `qwen3:8b` while giving better mapping quality than `qwen3:1.7b`.

## Pull and test the model

```powershell
ollama pull qwen3:4b
ollama run qwen3:4b
```

Then type `/bye` to exit the chat.

## Root `.env`

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

## Speed/quality options

```env
# Fastest smoke test, weaker mapping
LLM_MODEL=ollama/qwen3:1.7b

# Recommended demo balance
LLM_MODEL=ollama/qwen3:4b

# Better quality, slower
LLM_MODEL=ollama/qwen3:8b
```

There is not usually an Ollama tag called `qwen3:3b` or `qwen3:3.2`. The closest Qwen3 option for your use case is `qwen3:4b`.

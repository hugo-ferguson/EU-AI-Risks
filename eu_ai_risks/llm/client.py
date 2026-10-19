"""
LiteLLM wrapper for text completion.
"""

import json
import os
import re
import threading
from collections.abc import Iterator
from contextlib import contextmanager
from typing import cast

import litellm
from litellm import ModelResponse

RE_THINK_BLOCK = re.compile(r"<think>.*?</think>\s*", flags=re.DOTALL)
RE_MD_JSON_FENCE = re.compile(
    r"^```(?:json)?\s*\n(.*?)```\s*$", flags=re.DOTALL)
RE_MD_FENCE_OPEN = re.compile(r"^```(?:json)?\s*\n", flags=re.DOTALL)


def strip_llm_wrapping(text: str) -> str:
    """Remove <think> blocks and markdown JSON fences."""
    text = RE_THINK_BLOCK.sub("", text).strip()
    match = RE_MD_JSON_FENCE.match(text)
    if match:
        text = match.group(1).strip()
    else:
        # Truncated output: opening fence without closing fence
        text = RE_MD_FENCE_OPEN.sub("", text).strip()
    return text


litellm.suppress_debug_info = True

USAGE_FIELDS = ("calls", "input", "output", "cache_read", "cache_write")
# Token totals being kept by track_usage, per thread so parallel callers don't mix
_tracking = threading.local()


@contextmanager
def track_usage() -> Iterator[dict]:
    """Total the tokens of every LLM call this thread makes inside the block."""
    totals = dict.fromkeys(USAGE_FIELDS, 0)
    stack = _tracking.__dict__.setdefault("stack", [])
    stack.append(totals)
    try:
        yield totals
    finally:
        stack.remove(totals)


def _completion(**kwargs) -> tuple[ModelResponse, dict]:
    """litellm.completion, returning its token use and adding it to any track_usage totals."""
    response = cast(ModelResponse, litellm.completion(**kwargs))
    usage = response.usage
    details = getattr(usage, "prompt_tokens_details", None)
    cache_read = (getattr(usage, "cache_read_input_tokens", 0)
                  or getattr(details, "cached_tokens", 0) or 0)
    cache_write = getattr(usage, "cache_creation_input_tokens", 0) or 0
    token_usage = {
        "calls": 1,
        # prompt_tokens includes cached tokens, which are billed differently
        "input": max(usage.prompt_tokens - cache_read - cache_write, 0),
        "output": usage.completion_tokens,
        "cache_read": cache_read,
        "cache_write": cache_write,
    }
    for totals in getattr(_tracking, "stack", []):
        for field in USAGE_FIELDS:
            totals[field] += token_usage[field]
    return response, token_usage

LLM_MODEL: str = os.environ.get("LLM_MODEL", "")
LLM_API_BASE: str | None = os.environ.get("LLM_API_BASE")
LLM_NUM_CTX: int = int(os.environ.get("LLM_NUM_CTX", "16384"))


def _is_anthropic() -> bool:
    return LLM_MODEL.startswith("anthropic/")


def _base_kwargs(max_tokens: int, model: str | None = None) -> dict:
    """Provider-aware base kwargs for litellm.completion."""
    model = model or LLM_MODEL
    kwargs: dict = {"model": model,
                    "max_tokens": max_tokens, "num_retries": 3}
    # The API base belongs to LLM_MODEL; another model (e.g. a judge) uses its provider's default
    if LLM_API_BASE and model == LLM_MODEL:
        kwargs["api_base"] = LLM_API_BASE
    if model.startswith("ollama"):
        kwargs["api_key"] = "ollama"
        kwargs["num_ctx"] = LLM_NUM_CTX
    return kwargs


def _cacheable_system_message(content: str) -> dict:
    """Wrap a system message for Anthropic prompt caching."""
    return {
        "role": "system",
        "content": [{
            "type": "text",
            "text": content,
            "cache_control": {"type": "ephemeral"},
        }],
    }


def _cacheable_tools(tools: list[dict]) -> list[dict]:
    """Mark the last tool for Anthropic prompt caching."""
    result = tools[:-1] + \
        [{**tools[-1], "cache_control": {"type": "ephemeral"}}]
    return result


class LLMClient:
    """Singleton wrapper around LiteLLM."""

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            if not LLM_MODEL:
                raise RuntimeError(
                    "LLM_MODEL environment variable is not set. "
                    "Set it in .env (e.g. LLM_MODEL=anthropic/claude-sonnet-5)"
                )
            cls._instance = super().__new__(cls)
        return cls._instance

    def complete(
        self,
        prompt: str,
        system: str | None = None,
        max_tokens: int = 1024,
    ) -> str:
        messages: list[dict] = []
        if system:
            messages.append({"role": "system", "content": system})
        messages.append({"role": "user", "content": prompt})

        kwargs = _base_kwargs(max_tokens)
        kwargs["messages"] = messages
        response, _ = _completion(**kwargs)

        return strip_llm_wrapping(str(response.choices[0].message.content or ""))

    def complete_json(
        self,
        prompt: str,
        system: str | None = None,
        max_tokens: int = 1024,
    ) -> dict | list:
        messages: list[dict] = []
        if system:
            messages.append({"role": "system", "content": system})
        messages.append({"role": "user", "content": prompt})

        kwargs = _base_kwargs(max_tokens)
        kwargs["messages"] = messages
        kwargs["response_format"] = {"type": "json_object"}
        response, _ = _completion(**kwargs)

        content = strip_llm_wrapping(
            str(response.choices[0].message.content or ""))
        # A model sometimes writes its reasoning before the JSON
        parsed = _parse_json(content)
        if parsed is None:
            raise ValueError(f"Model returned invalid JSON: {content!r}")
        return parsed

    def complete_json_cached(
        self,
        prompt: str,
        system: str,
        shared: str = "",
        max_tokens: int = 1024,
        model: str | None = None,
        schema: dict | None = None,
        **options,
    ) -> tuple[dict | list, dict]:
        """
        JSON completion whose system prompt and shared context are cached, for
        many requests that differ only in the prompt.

        :param shared: context common to a run of requests (e.g. an SRS), sent
            before the prompt so it is part of the cached prefix.
        :param model: a litellm model string, defaulting to LLM_MODEL.
        :param schema: a JSON schema the response must follow, as a structured
            output; without it the model is only asked for a JSON object.
        :param options: further litellm.completion arguments, e.g. reasoning_effort.
        :return: (parsed JSON, token usage).
        """
        model = model or LLM_MODEL
        user_blocks = [{"type": "text", "text": text} for text in (shared, prompt) if text]
        # Anthropic caches up to explicit breakpoints; OpenAI caches long prefixes by itself
        if model.startswith("anthropic/"):
            messages = [_cacheable_system_message(system)]
            if shared:
                user_blocks[0]["cache_control"] = {"type": "ephemeral"}
            messages.append({"role": "user", "content": user_blocks})
        else:
            # Plain text, which every provider accepts; OpenAI still caches the long prefix
            messages = [{"role": "system", "content": system},
                        {"role": "user", "content": "\n\n".join(b["text"] for b in user_blocks)}]

        kwargs = _base_kwargs(max_tokens, model)
        # Asking for a JSON object doesn't stop some models reasoning in prose first; a schema does
        response_format = (
            {"type": "json_schema",
             "json_schema": {"name": "response", "schema": schema, "strict": True}}
            if schema else {"type": "json_object"})
        kwargs.update(options, messages=messages, response_format=response_format)
        response, token_usage = _completion(**kwargs)

        content = strip_llm_wrapping(str(response.choices[0].message.content or ""))
        parsed = _parse_json(content)
        if parsed is None:
            raise ValueError(f"Model returned invalid JSON: {content!r}")
        return parsed, token_usage

    def complete_with_tools(
        self,
        messages: list[dict],
        tools: list[dict] | None = None,
        max_tokens: int = 4096,
    ) -> ModelResponse:
        kwargs = _base_kwargs(max_tokens)

        if _is_anthropic():
            kwargs["messages"] = _apply_system_caching(messages)
            if tools:
                kwargs["tools"] = _cacheable_tools(tools)
        else:
            kwargs["messages"] = messages
            if tools:
                kwargs["tools"] = tools

        response, _ = _completion(**kwargs)
        return response


def _parse_json(text: str) -> dict | list | None:
    """The text as JSON, or else the last JSON object in it, after any prose the model wrote first."""
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        pass
    decoder = json.JSONDecoder()
    for start in reversed([index for index, char in enumerate(text) if char == "{"]):
        try:
            parsed, _ = decoder.raw_decode(text, start)
        except json.JSONDecodeError:
            continue
        if isinstance(parsed, dict):
            return parsed
    return None


def _apply_system_caching(messages: list[dict]) -> list[dict]:
    """Convert system messages to the cached content-block format."""
    result = []
    for message in messages:
        if message["role"] == "system" and isinstance(message["content"], str):
            result.append(_cacheable_system_message(message["content"]))
        else:
            result.append(message)
    return result


def complete(
    prompt: str,
    system: str | None = None,
    max_tokens: int = 1024,
) -> str:
    return LLMClient().complete(prompt, system=system, max_tokens=max_tokens)


def complete_json(
    prompt: str,
    system: str | None = None,
    max_tokens: int = 1024,
) -> dict | list:
    return LLMClient().complete_json(prompt, system=system, max_tokens=max_tokens)


def complete_json_cached(
    prompt: str,
    system: str,
    shared: str = "",
    max_tokens: int = 1024,
    model: str | None = None,
    schema: dict | None = None,
    **options,
) -> tuple[dict | list, dict]:
    return LLMClient().complete_json_cached(
        prompt, system, shared=shared, max_tokens=max_tokens, model=model, schema=schema,
        **options)


def complete_with_tools(
    messages: list[dict],
    tools: list[dict] | None = None,
    max_tokens: int = 4096,
) -> ModelResponse:
    return LLMClient().complete_with_tools(
        messages, tools=tools, max_tokens=max_tokens
    )

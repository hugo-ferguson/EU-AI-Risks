"""
LiteLLM wrapper for text completion.
"""

import json
import os
import re
from typing import cast

import litellm
from litellm import ModelResponse

RE_THINK_BLOCK = re.compile(r"<think>.*?</think>\s*", flags=re.DOTALL)
RE_MD_JSON_FENCE = re.compile(r"^```(?:json)?\s*\n(.*?)```\s*$", flags=re.DOTALL)


def strip_llm_wrapping(text: str) -> str:
    """Remove <think> blocks and markdown JSON fences."""
    text = RE_THINK_BLOCK.sub("", text).strip()
    match = RE_MD_JSON_FENCE.match(text)
    if match:
        text = match.group(1).strip()
    return text


litellm.suppress_debug_info = True

LLM_MODEL: str = os.environ.get("LLM_MODEL", "")
LLM_API_BASE: str | None = os.environ.get("LLM_API_BASE")
LLM_NUM_CTX: int = int(os.environ.get("LLM_NUM_CTX", "16384"))


def _is_anthropic() -> bool:
    return LLM_MODEL.startswith("anthropic/")


def _base_kwargs(max_tokens: int) -> dict:
    """Provider-aware base kwargs for litellm.completion."""
    kwargs: dict = {"model": LLM_MODEL, "max_tokens": max_tokens, "num_retries": 3}
    if LLM_API_BASE:
        kwargs["api_base"] = LLM_API_BASE
    if LLM_MODEL.startswith("ollama"):
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
    result = tools[:-1] + [{**tools[-1], "cache_control": {"type": "ephemeral"}}]
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
        response = cast(ModelResponse, litellm.completion(**kwargs))

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
        response = cast(ModelResponse, litellm.completion(**kwargs))

        content = strip_llm_wrapping(
            str(response.choices[0].message.content or ""))
        try:
            return json.loads(content)
        except json.JSONDecodeError as exc:
            raise ValueError(
                f"Model returned invalid JSON: {content!r}") from exc

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

        return cast(ModelResponse, litellm.completion(**kwargs))


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


def complete_with_tools(
    messages: list[dict],
    tools: list[dict] | None = None,
    max_tokens: int = 4096,
) -> ModelResponse:
    return LLMClient().complete_with_tools(
        messages, tools=tools, max_tokens=max_tokens
    )

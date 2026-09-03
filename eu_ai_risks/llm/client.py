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
    """Remove <think> blocks and markdown JSON fences from model output."""
    text = RE_THINK_BLOCK.sub("", text).strip()
    m = RE_MD_JSON_FENCE.match(text)
    if m:
        text = m.group(1).strip()
    return text

litellm.suppress_debug_info = True

# Configured via .env. Supports any LiteLLM-compatible model string and API.
LLM_MODEL: str = os.environ.get("LLM_MODEL", "")
LLM_API_BASE: str | None = os.environ.get("LLM_API_BASE")
LLM_NUM_CTX: int = int(os.environ.get("LLM_NUM_CTX", "16384"))


def _base_kwargs(max_tokens: int) -> dict:
    """Build provider-aware kwargs for litellm.completion."""
    kwargs: dict = {"model": LLM_MODEL, "max_tokens": max_tokens, "num_retries": 3}
    if LLM_API_BASE:
        kwargs["api_base"] = LLM_API_BASE
    if LLM_MODEL.startswith("ollama"):
        kwargs["api_key"] = "ollama"
        kwargs["num_ctx"] = LLM_NUM_CTX
    return kwargs


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
        except json.JSONDecodeError as e:
            raise ValueError(
                f"Model returned invalid JSON: {content!r}") from e

    def complete_with_tools(
        self,
        messages: list[dict],
        tools: list[dict] | None = None,
        max_tokens: int = 4096,
    ) -> ModelResponse:
        kwargs = _base_kwargs(max_tokens)
        kwargs["messages"] = messages
        if tools:
            kwargs["tools"] = tools
        return cast(ModelResponse, litellm.completion(**kwargs))


def complete(
    prompt: str,
    system: str | None = None,
    max_tokens: int = 1024,
) -> str:
    """Send a completion request and return the response text."""
    return LLMClient().complete(prompt, system=system, max_tokens=max_tokens)


def complete_json(
    prompt: str,
    system: str | None = None,
    max_tokens: int = 1024,
) -> dict | list:
    """Send a completion request with JSON output enforced."""
    return LLMClient().complete_json(prompt, system=system, max_tokens=max_tokens)


def complete_with_tools(
    messages: list[dict],
    tools: list[dict] | None = None,
    max_tokens: int = 4096,
) -> ModelResponse:
    """Send a chat completion request with tool definitions."""
    return LLMClient().complete_with_tools(
        messages, tools=tools, max_tokens=max_tokens
    )

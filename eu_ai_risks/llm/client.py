"""
LiteLLM wrapper for text completion.
"""

import json
import os
from typing import cast

import litellm
from litellm import ModelResponse

# Configured via .env. Supports any LiteLLM-compatible model string and API.
LLM_MODEL: str = os.environ.get("LLM_MODEL", "")
LLM_API_BASE: str | None = os.environ.get("LLM_API_BASE")


class LLMClient:
    """Singleton wrapper around LiteLLM."""

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            if not LLM_MODEL:
                raise RuntimeError(
                    "LLM_MODEL environment variable is not set. "
                    "Set it in .env (e.g. LLM_MODEL=ollama/qwen2.5:14b)"
                )
            cls._instance = super().__new__(cls)
        return cls._instance

    def complete(
        self,
        prompt: str,
        system: str | None = None,
        max_tokens: int = 1024,
    ) -> str:
        """
        Send a completion request and return the response text.

        :param prompt: the user message.
        :param system: optional system prompt.
        :param max_tokens: maximum tokens to generate.
        :return: the model's response text.
        """
        messages: list[dict] = []
        if system:
            messages.append({"role": "system", "content": system})
        messages.append({"role": "user", "content": prompt})

        response = cast(ModelResponse, litellm.completion(
            model=LLM_MODEL,
            messages=messages,
            max_tokens=max_tokens,
            api_base=LLM_API_BASE,
            num_retries=3,
        ))

        return str(response.choices[0].message.content or "")

    def complete_json(
        self,
        prompt: str,
        system: str | None = None,
        max_tokens: int = 1024,
    ) -> dict | list:
        """
        Send a completion request with JSON output enforced and return the
        parsed result. Uses the model's native JSON mode.

        :param prompt: the user message.
        :param system: optional system prompt.
        :param max_tokens: maximum tokens to generate.
        :return: parsed JSON as a dict or list.
        :raises ValueError: if the response cannot be parsed as JSON.
        """
        messages: list[dict] = []
        if system:
            messages.append({"role": "system", "content": system})
        messages.append({"role": "user", "content": prompt})

        response = cast(ModelResponse, litellm.completion(
            model=LLM_MODEL,
            messages=messages,
            max_tokens=max_tokens,
            api_base=LLM_API_BASE,
            response_format={"type": "json_object"},
            num_retries=3,
        ))

        content = response.choices[0].message.content
        try:
            return json.loads(content)  # type: ignore[arg-type]
        except json.JSONDecodeError as e:
            raise ValueError(
                f"Model returned invalid JSON: {content!r}") from e

    def complete_with_tools(
        self,
        messages: list[dict],
        tools: list[dict] | None = None,
        max_tokens: int = 4096,
    ) -> ModelResponse:
        """
        Send a chat completion request with tool definitions.

        :param messages: full conversation history.
        :param tools: OpenAI-format tool definitions.
        :param max_tokens: maximum tokens to generate.
        :return: the full model response.
        """
        if tools:
            return cast(ModelResponse, litellm.completion(
                model=LLM_MODEL,
                messages=messages,
                tools=tools,
                max_tokens=max_tokens,
                api_base=LLM_API_BASE,
                num_retries=3,
            ))

        return cast(ModelResponse, litellm.completion(
            model=LLM_MODEL,
            messages=messages,
            max_tokens=max_tokens,
            api_base=LLM_API_BASE,
            num_retries=3,
        ))


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

"""
LiteLLM wrapper for text completion.
"""

import json
import os
import re
from typing import cast

import litellm
from litellm import ModelResponse

litellm.suppress_debug_info = True

# Configured via .env. Supports any LiteLLM-compatible model string and API.
LLM_MODEL: str = os.environ.get("LLM_MODEL", "")
LLM_API_BASE: str | None = os.environ.get("LLM_API_BASE")
LLM_TEMPERATURE: float = float(os.environ.get("LLM_TEMPERATURE", "0.2"))
LLM_JSON_NO_THINK: bool = os.environ.get("LLM_JSON_NO_THINK", "true").lower() not in {"0", "false", "no"}


def _with_no_think(prompt: str) -> str:
    """Ask Qwen3-style reasoning models to skip visible thinking for JSON calls."""
    if LLM_JSON_NO_THINK and "qwen3" in LLM_MODEL.lower() and "/no_think" not in prompt:
        return f"/no_think\n{prompt}"
    return prompt


def _strip_thinking_blocks(content: str) -> str:
    """Remove Qwen/DeepSeek style thinking blocks before JSON parsing."""
    return re.sub(r"<think>[\s\S]*?</think>", "", content, flags=re.IGNORECASE).strip()


def _strip_code_fence(content: str) -> str:
    content = content.strip()
    if content.startswith("```"):
        content = re.sub(r"^```(?:json)?\s*", "", content, flags=re.IGNORECASE)
        content = re.sub(r"\s*```$", "", content)
    return content.strip()


def _extract_balanced_json(content: str) -> str | None:
    """Extract the first balanced JSON object/array from surrounding text."""
    starts = [(idx, char) for idx, char in ((content.find("{"), "{"), (content.find("["), "[")) if idx != -1]
    if not starts:
        return None

    start, first = min(starts, key=lambda item: item[0])
    expected_close = {"{": "}", "[": "]"}
    stack = [expected_close[first]]
    in_string = False
    escaped = False

    for index in range(start + 1, len(content)):
        char = content[index]
        if in_string:
            if escaped:
                escaped = False
            elif char == "\\":
                escaped = True
            elif char == '"':
                in_string = False
            continue

        if char == '"':
            in_string = True
        elif char in expected_close:
            stack.append(expected_close[char])
        elif stack and char == stack[-1]:
            stack.pop()
            if not stack:
                return content[start:index + 1]

    return None


def parse_json_response(content: str | None) -> dict | list:
    """Parse JSON even if a local model adds thinking text or markdown fences."""
    if content is None:
        raise ValueError("Model returned an empty response")

    cleaned = _strip_code_fence(_strip_thinking_blocks(str(content)))
    try:
        return json.loads(cleaned)
    except json.JSONDecodeError:
        extracted = _extract_balanced_json(cleaned)
        if extracted:
            return json.loads(extracted)
        raise


class LLMClient:
    """Singleton wrapper around LiteLLM."""

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            if not LLM_MODEL:
                raise RuntimeError(
                    "LLM_MODEL environment variable is not set. "
                    "Set it in .env (e.g. LLM_MODEL=ollama/qwen3:8b)"
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
            temperature=LLM_TEMPERATURE,
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
        messages.append({"role": "user", "content": _with_no_think(prompt)})

        response = cast(ModelResponse, litellm.completion(
            model=LLM_MODEL,
            messages=messages,
            max_tokens=max_tokens,
            api_base=LLM_API_BASE,
            response_format={"type": "json_object"},
            temperature=LLM_TEMPERATURE,
            num_retries=3,
        ))

        content = response.choices[0].message.content
        try:
            return parse_json_response(content)
        except (json.JSONDecodeError, ValueError) as e:
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
                temperature=LLM_TEMPERATURE,
                num_retries=3,
            ))

        return cast(ModelResponse, litellm.completion(
            model=LLM_MODEL,
            messages=messages,
            max_tokens=max_tokens,
            api_base=LLM_API_BASE,
            temperature=LLM_TEMPERATURE,
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

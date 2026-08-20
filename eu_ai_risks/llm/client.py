"""
LiteLLM wrapper for text completion.
"""

import json
import os

import litellm

# Configured via .env. Supports any LiteLLM-compatible model string and API.
LLM_MODEL = os.environ.get("LLM_MODEL")
LLM_API_BASE = os.environ.get("LLM_API_BASE")


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
		messages = []
		if system:
			messages.append({"role": "system", "content": system})
		messages.append({"role": "user", "content": prompt})

		response = litellm.completion(
			model=LLM_MODEL,
			messages=messages,
			max_tokens=max_tokens,
			api_base=LLM_API_BASE,
			num_retries=3,
		)

		return response.choices[0].message.content

	def complete_json(
			self,
			prompt: str,
			system: str | None = None,
			max_tokens: int = 1024,
	) -> dict | list:
		"""
		Send a completion request with JSON output enforced and return the
		parsed result.

		Uses the model's native JSON mode (grammar-constrained decoding where
		supported) to guarantee valid JSON, eliminating parse errors from
		freeform output.

		:param prompt: the user message.
		:param system: optional system prompt.
		:param max_tokens: maximum tokens to generate.
		:return: parsed JSON as a dict or list.
		:raises ValueError: if the response cannot be parsed as JSON.
		"""
		messages = []
		if system:
			messages.append({"role": "system", "content": system})
		messages.append({"role": "user", "content": prompt})

		response = litellm.completion(
			model=LLM_MODEL,
			messages=messages,
			max_tokens=max_tokens,
			api_base=LLM_API_BASE,
			response_format={"type": "json_object"},
			num_retries=3,
		)

		content = response.choices[0].message.content
		try:
			return json.loads(content)
		except json.JSONDecodeError as e:
			raise ValueError(f"Model returned invalid JSON: {content!r}") from e


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
	"""Send a completion request with JSON output enforced and return the parsed result."""
	return LLMClient().complete_json(prompt, system=system, max_tokens=max_tokens)

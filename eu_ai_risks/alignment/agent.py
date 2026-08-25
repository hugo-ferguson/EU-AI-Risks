"""
LLM agent loop with tool calling.
"""

import json
import uuid
from collections.abc import Callable
from eu_ai_risks.alignment.models import AgentAnswer, AgentResult
from eu_ai_risks.llm import complete_with_tools


def _parse_answer(raw_content: str) -> AgentAnswer:
    try:
        return AgentAnswer.model_validate_json(raw_content)
    except (json.JSONDecodeError, ValueError):
        return AgentAnswer(summary=raw_content)


def _extract_text_tool_calls(content: str) -> list[dict] | None:
    try:
        parsed = json.loads(content.strip())
    except (json.JSONDecodeError, ValueError):
        return None

    items = [parsed] if isinstance(parsed, dict) else parsed
    if not isinstance(items, list):
        return None

    tool_calls = []
    for item in items:
        func = item.get("function") if isinstance(item, dict) else None
        if isinstance(func, dict) and "name" in func:
            args = func.get("arguments", {})
            tool_calls.append({
                "id": item.get("id", f"call_{uuid.uuid4().hex[:12]}"),
                "type": "function",
                "function": {
                    "name": func["name"],
                    "arguments": args if isinstance(args, str) else json.dumps(args),
                },
            })

    return tool_calls or None


def _serialize_tool_call(tc) -> dict:
    return {
        "id": tc.id,
        "type": "function",
        "function": {
            "name": tc.function.name,
            "arguments": tc.function.arguments,
        },
    }


def _execute_tool_call(tc_dict: dict, executor: Callable) -> tuple[str, str]:
    tool_name = tc_dict["function"]["name"] or ""
    try:
        arguments = json.loads(tc_dict["function"]["arguments"] or "{}")
    except json.JSONDecodeError:
        arguments = {}
    return tool_name, executor(tool_name, arguments)


class AgentLoop:

    def __init__(
        self,
        system_prompt: str,
        tools: list[dict],
        tool_executor: Callable[[str, dict], str],
        max_iterations: int = 15,
        max_tokens: int = 4096,
    ):
        self.system_prompt = system_prompt
        self.tools = tools
        self.tool_executor = tool_executor
        self.max_iterations = max_iterations
        self.max_tokens = max_tokens

    def run(self, user_message: str) -> AgentResult:
        messages = [
            {"role": "system", "content": self.system_prompt},
            {"role": "user", "content": user_message},
        ]

        total_tool_calls = 0

        for iteration in range(1, self.max_iterations + 1):
            response = complete_with_tools(
                messages, tools=self.tools, max_tokens=self.max_tokens,
            )

            message = response.choices[0].message
            assistant_msg: dict = {"role": "assistant"}
            if message.content:
                assistant_msg["content"] = message.content

            tool_calls = (
                [_serialize_tool_call(tc) for tc in message.tool_calls]
                if message.tool_calls
                else _extract_text_tool_calls(message.content or "")
            )

            if not tool_calls:
                messages.append(assistant_msg)
                raw = message.content or ""
                return AgentResult(
                    answer=_parse_answer(raw),
                    raw_content=raw,
                    messages=messages,
                    tool_calls_made=total_tool_calls,
                    iterations=iteration,
                )

            assistant_msg["tool_calls"] = tool_calls
            messages.append(assistant_msg)

            for tc_dict in tool_calls:
                _, result = _execute_tool_call(tc_dict, self.tool_executor)
                total_tool_calls += 1
                messages.append({
                    "role": "tool",
                    "tool_call_id": tc_dict["id"],
                    "content": result,
                })

        raw = next(
            (m["content"] for m in reversed(messages)
             if m["role"] == "assistant" and m.get("content")),
            "",
        )

        return AgentResult(
            answer=_parse_answer(raw),
            raw_content=raw,
            messages=messages,
            tool_calls_made=total_tool_calls,
            iterations=self.max_iterations,
        )

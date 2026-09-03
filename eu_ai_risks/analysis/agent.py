"""
LLM agent loop with tool calling.
"""

import json
import logging
import uuid
from collections.abc import Callable
from eu_ai_risks.analysis.models import AgentAnswer, AgentResult
from eu_ai_risks.llm import complete_with_tools, strip_llm_wrapping

log = logging.getLogger(__name__)

MAX_TOOL_RESULT_CHARS = 2000


def _parse_answer(raw_content: str) -> AgentAnswer:
    raw_content = strip_llm_wrapping(raw_content)
    try:
        return AgentAnswer.model_validate_json(raw_content)
    except (json.JSONDecodeError, ValueError):
        return AgentAnswer(summary=raw_content)


def _extract_text_tool_calls(content: str) -> list[dict] | None:
    """Parse tool calls embedded as JSON text (for models without native tool support)."""
    try:
        parsed = json.loads(content.strip())
    except (json.JSONDecodeError, ValueError):
        return None

    items = [parsed] if isinstance(parsed, dict) else parsed
    if not isinstance(items, list):
        return None

    tool_calls = []
    for item in items:
        function = item.get("function") if isinstance(item, dict) else None
        if isinstance(function, dict) and "name" in function:
            arguments = function.get("arguments", {})
            tool_calls.append({
                "id": item.get("id", f"call_{uuid.uuid4().hex[:12]}"),
                "type": "function",
                "function": {
                    "name": function["name"],
                    "arguments": arguments if isinstance(arguments, str) else json.dumps(arguments),
                },
            })

    return tool_calls or None


def _serialise_tool_call(tool_call) -> dict:
    return {
        "id": tool_call.id,
        "type": "function",
        "function": {
            "name": tool_call.function.name,
            "arguments": tool_call.function.arguments,
        },
    }


def _execute_tool_call(tool_call_dict: dict, executor: Callable) -> tuple[str, str]:
    tool_name = tool_call_dict["function"]["name"] or ""
    try:
        arguments = json.loads(tool_call_dict["function"]["arguments"] or "{}")
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
            is_final_iteration = iteration == self.max_iterations

            if is_final_iteration:
                messages.append({
                    "role": "user",
                    "content": (
                        "You have one turn left. Stop using tools and "
                        "produce your final JSON answer now."
                    ),
                })

            log.debug(
                "iter %d/%d | %d messages | roles=%s",
                iteration, self.max_iterations,
                len(messages),
                [msg["role"] for msg in messages],
            )

            tools_for_call = None if is_final_iteration else self.tools
            response = complete_with_tools(
                messages, tools=tools_for_call, max_tokens=self.max_tokens,
            )

            message = response.choices[0].message
            raw_content = message.content or ""
            content = strip_llm_wrapping(raw_content)
            assistant_message: dict = {"role": "assistant"}
            if content:
                assistant_message["content"] = content

            log.debug(
                "iter %d | content[:200]=%r | tool_calls=%s",
                iteration,
                content[:200],
                [tool_call.function.name for tool_call in message.tool_calls]
                if message.tool_calls else None,
            )

            tool_calls = (
                [_serialise_tool_call(tool_call) for tool_call in message.tool_calls]
                if message.tool_calls
                else _extract_text_tool_calls(content)
            )

            if not tool_calls and not content:
                messages.append({"role": "assistant", "content": "(no output)"})
                messages.append({
                    "role": "user",
                    "content": (
                        "You did not produce any output. Use the tools "
                        "to research the question, then give your answer."
                    ),
                })
                continue

            if not tool_calls:
                messages.append(assistant_message)
                return AgentResult(
                    answer=_parse_answer(content),
                    raw_content=content,
                    messages=messages,
                    tool_calls_made=total_tool_calls,
                    iterations=iteration,
                )

            assistant_message["tool_calls"] = tool_calls
            messages.append(assistant_message)

            for tool_call_dict in tool_calls:
                _, result = _execute_tool_call(tool_call_dict, self.tool_executor)
                if len(result) > MAX_TOOL_RESULT_CHARS:
                    result = result[:MAX_TOOL_RESULT_CHARS] + "\n...(truncated)"
                total_tool_calls += 1
                messages.append({
                    "role": "tool",
                    "tool_call_id": tool_call_dict["id"],
                    "content": result,
                })

        final_content = next(
            (msg["content"] for msg in reversed(messages)
             if msg["role"] == "assistant" and msg.get("content")),
            "",
        )

        return AgentResult(
            answer=_parse_answer(final_content),
            raw_content=final_content,
            messages=messages,
            tool_calls_made=total_tool_calls,
            iterations=self.max_iterations,
        )

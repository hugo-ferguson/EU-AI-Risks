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


def _parse_answer(raw_content: str) -> AgentAnswer:
    raw_content = strip_llm_wrapping(raw_content)
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


MAX_TOOL_RESULT_CHARS = 2000


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
            if iteration == self.max_iterations:
                messages.append({
                    "role": "user",
                    "content": (
                        "You have one turn left. Stop using tools and "
                        "produce your final JSON answer now."
                    ),
                })

            log.debug(
                "SENDING iter %d | %d msgs | roles=%s",
                iteration,
                len(messages),
                [m["role"] for m in messages],
            )
            tools_to_send = (
                self.tools if iteration < self.max_iterations else None
            )
            response = complete_with_tools(
                messages, tools=tools_to_send, max_tokens=self.max_tokens,
            )

            message = response.choices[0].message
            raw_content = message.content or ""
            content = strip_llm_wrapping(raw_content)
            assistant_msg: dict = {"role": "assistant"}
            if content:
                assistant_msg["content"] = content

            log.debug(
                "iter %d | raw_content[:200]=%r | "
                "content[:200]=%r | tool_calls=%s",
                iteration,
                raw_content[:200],
                content[:200],
                [tc.function.name for tc in message.tool_calls]
                if message.tool_calls else None,
            )

            tool_calls = (
                [_serialize_tool_call(tc) for tc in message.tool_calls]
                if message.tool_calls
                else _extract_text_tool_calls(content)
            )

            # If the model returned only thinking tags (no real content
            # and no tool calls), nudge it to actually act.
            if not tool_calls and not content:
                messages.append({
                    "role": "assistant",
                    "content": "(no output)",
                })
                messages.append({
                    "role": "user",
                    "content": (
                        "You did not produce any output. Use the tools "
                        "to research the question, then give your answer."
                    ),
                })
                continue

            if not tool_calls:
                messages.append(assistant_msg)
                raw = content
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
                if len(result) > MAX_TOOL_RESULT_CHARS:
                    result = result[:MAX_TOOL_RESULT_CHARS] + "\n...(truncated)"
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

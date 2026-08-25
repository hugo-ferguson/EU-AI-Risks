"""
LLM agent loop with tool calling.
"""

import json
from collections.abc import Callable
from eu_ai_risks.alignment.models import AgentAnswer, AgentResult
from eu_ai_risks.llm import complete_json, complete_with_tools


def _format_answer(raw_content: str) -> AgentAnswer:
    """
    Structure raw agent output into an AgentAnswer using an LLM call.
    """
    schema = json.dumps(AgentAnswer.model_json_schema(), indent="\t")
    try:
        result = complete_json(
            f"Structure this into valid JSON matool_callhing the schema. "
            f"Extract citations from any article/paragraph references. Write a "
            f"clear natural language summary.\n\n"
            f"Schema:\n{schema}\n\n"
            f"Raw answer:\n{raw_content}",
            max_tokens=2048,
        )
        return AgentAnswer.model_validate(result)
    except Exception:
        return AgentAnswer(summary=raw_content)


class AgentLoop:
    """
    A generic tool-calling agent loop.
    """

    def __init__(
            self,
            system_prompt: str,
            tools: list[dict],
            tool_executor: Callable[[str, dict], str],
            max_iterations: int = 15,
            max_tokens: int = 4096,
            format_response: bool = True,
    ):
        self.system_prompt = system_prompt
        self.tools = tools
        self.tool_executor = tool_executor
        self.max_iterations = max_iterations
        self.max_tokens = max_tokens
        self.format_response = format_response

    def run(self, user_message: str) -> AgentResult:
        """
        Run the agent loop to completion.

        :param user_message: the user's question or instruction.
        :return: AgentResult with structured answer and conversation history.
        """
        messages = [
            {"role": "system", "content": self.system_prompt},
            {"role": "user", "content": user_message},
        ]

        total_tool_calls = 0
        raw_content = ""

        for iteration in range(1, self.max_iterations + 1):
            response = complete_with_tools(
                messages,
                tools=self.tools,
                max_tokens=self.max_tokens,
            )

            message = response.choices[0].message
            assistant_msg: dict = {"role": "assistant"}

            if message.content:
                assistant_msg["content"] = message.content

            if not message.tool_calls:
                if "content" not in assistant_msg:
                    assistant_msg["content"] = ""
                messages.append(assistant_msg)
                raw_content = message.content or ""

                answer = (
                    _format_answer(raw_content)
                    if self.format_response
                    else AgentAnswer(summary=raw_content)
                )

                return AgentResult(
                    answer=answer,
                    raw_content=raw_content,
                    messages=messages,
                    tool_calls_made=total_tool_calls,
                    iterations=iteration,
                )

            assistant_msg["tool_calls"] = [
                {
                    "id": tool_call.id,
                    "type": "function",
                            "function": {
                                "name": tool_call.function.name,
                                "arguments": tool_call.function.arguments,
                            },
                }
                for tool_call in message.tool_calls
            ]

            messages.append(assistant_msg)

            for tool_call in message.tool_calls:
                tool_name = tool_call.function.name or ""
                try:
                    arguments = json.loads(
                        tool_call.function.arguments or "{}")
                except json.JSONDecodeError:
                    arguments = {}

                result = self.tool_executor(tool_name, arguments)
                total_tool_calls += 1

                messages.append({
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "content": result,
                })

        last_content = ""

        for msg in reversed(messages):
            if msg["role"] == "assistant" and msg.get("content"):
                last_content = msg["content"]
                break

        answer = (
            _format_answer(last_content)
            if self.format_response
            else AgentAnswer(summary=last_content)
        )

        return AgentResult(
            answer=answer,
            raw_content=last_content,
            messages=messages,
            tool_calls_made=total_tool_calls,
            iterations=self.max_iterations,
        )

"""
Agent-based risk assessment pipeline.

Uses multi-turn tool calling to explore the Neo4j knowledge graph
before synthesising a risk assessment for each requirement.
"""

import json
import re

from eu_ai_risks.analysis.agent import AgentLoop
from eu_ai_risks.analysis.models import RequirementRisk
from eu_ai_risks.analysis.prompts import RISK_ASSESSMENT_AGENT_PROMPT
from eu_ai_risks.analysis.tools import TOOL_DEFINITIONS, execute_tool

# Extracts known fields from truncated/malformed JSON
_RE_SUMMARY = re.compile(r'"summary"\s*:\s*"((?:[^"\\]|\\.)*)"')
_RE_RISK_LEVEL = re.compile(r'"risk_level"\s*:\s*"(high|medium|low)"')

MAX_AGENT_ITERATIONS = 8
MAX_AGENT_TOKENS = 4096


def _extract_first_json_object(text: str) -> str | None:
    """Walk brace depth to extract the outermost JSON object."""
    start = text.find("{")
    if start == -1:
        return None
    depth = 0
    in_string = False
    escape = False
    for i in range(start, len(text)):
        character = text[i]
        if escape:
            escape = False
            continue
        if character == "\\":
            escape = True
            continue
        if character == '"':
            in_string = not in_string
            continue
        if in_string:
            continue
        if character == "{":
            depth += 1
        elif character == "}":
            depth -= 1
            if depth == 0:
                return text[start:i + 1]
    return None


def _parse_result(raw_content: str) -> RequirementRisk:
    """Parse agent output with layered fallbacks."""
    content = raw_content.strip()
    if not content:
        return RequirementRisk(
            summary="Model did not produce a valid risk assessment.",
        )

    try:
        return RequirementRisk.model_validate_json(content)
    except Exception:
        pass

    extracted = _extract_first_json_object(content)
    if extracted:
        try:
            return RequirementRisk.model_validate_json(extracted)
        except Exception:
            pass
        try:
            data = json.loads(extracted)
            if isinstance(data, dict):
                return RequirementRisk.model_validate(data)
        except Exception:
            pass

    # Last resort: regex-extract fields from truncated JSON
    summary_match = _RE_SUMMARY.search(content)
    if summary_match:
        summary = summary_match.group(1).replace('\\"', '"')
        level_match = _RE_RISK_LEVEL.search(content)
        return RequirementRisk(
            summary=summary,
            risk_level=level_match.group(1) if level_match else "medium",
        )

    return RequirementRisk(
        summary=content[:2000] if len(content) > 2000 else content,
    )


def assess_requirement(
    requirement_id: str,
    requirement_text: str,
    categories: list[dict] | None = None,
) -> tuple[RequirementRisk, dict[str, dict], dict]:
    """Assess a single requirement using the agent loop."""
    agent = AgentLoop(
        system_prompt=RISK_ASSESSMENT_AGENT_PROMPT,
        tools=TOOL_DEFINITIONS,
        tool_executor=execute_tool,
        max_iterations=MAX_AGENT_ITERATIONS,
        max_tokens=MAX_AGENT_TOKENS,
    )

    user_message = (
        f"Assess this software requirement for EU AI Act compliance risks.\n\n"
        f"Requirement ID: {requirement_id}\n"
        f"Requirement: {requirement_text}\n\n"
        f"Use the tools to find relevant provisions, then identify "
        f"specific compliance gaps."
    )

    result = agent.run(user_message)
    assessment = _parse_result(result.raw_content)

    metadata = {
        "iterations": result.iterations,
        "tool_calls_made": result.tool_calls_made,
        "raw_content": result.raw_content,
    }

    return assessment, {}, metadata

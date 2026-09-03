"""
Agent-based risk assessment pipeline.

Uses multi-turn tool calling to explore the Neo4j knowledge graph
before synthesising a risk assessment for each requirement.
"""

from eu_ai_risks.analysis.agent import AgentLoop
from eu_ai_risks.analysis.models import RequirementRisk
from eu_ai_risks.analysis.prompts import RISK_ASSESSMENT_AGENT_PROMPT
from eu_ai_risks.analysis.tools import TOOL_DEFINITIONS, execute_tool

MAX_AGENT_ITERATIONS = 8
MAX_AGENT_TOKENS = 4096


def assess_requirement(
    requirement_id: str,
    requirement_text: str,
    categories: list[dict] | None = None,
) -> tuple[RequirementRisk, dict[str, dict], dict]:
    """Assess a single requirement using the agent loop.

    Returns (parsed assessment, article cache, raw metadata).
    The article cache is empty — collect_citations fetches as needed.
    """
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

    try:
        assessment = RequirementRisk.model_validate_json(result.raw_content)
    except Exception:
        assessment = RequirementRisk(
            summary=result.raw_content or "Model did not produce a valid risk assessment.",
        )

    metadata = {
        "iterations": result.iterations,
        "tool_calls_made": result.tool_calls_made,
        "raw_content": result.raw_content,
    }

    return assessment, {}, metadata

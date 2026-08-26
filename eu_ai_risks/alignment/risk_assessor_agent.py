"""
Agent-based risk assessment pipeline.

Uses multi-turn tool calling to explore the Neo4j knowledge graph
before synthesising a risk assessment for each requirement.
"""

import json

from eu_ai_risks.alignment.agent import AgentLoop
from eu_ai_risks.alignment.models import RequirementRisk, RiskItem
from eu_ai_risks.alignment.prompts import RISK_ASSESSMENT_AGENT_PROMPT
from eu_ai_risks.alignment.tools import TOOL_DEFINITIONS, execute_tool

MAX_AGENT_ITERATIONS = 10
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
    assessment = _convert_agent_result(result)

    metadata = {
        "iterations": result.iterations,
        "tool_calls_made": result.tool_calls_made,
        "raw_content": result.raw_content,
    }

    return assessment, {}, metadata


def _convert_agent_result(result) -> RequirementRisk:
    """Convert an AgentResult to RequirementRisk."""
    try:
        parsed = json.loads(result.raw_content)
        if isinstance(parsed, dict):
            try:
                return RequirementRisk.model_validate(parsed)
            except Exception:
                pass
            for key in ("answer", "response", "result", "assessment", "data"):
                nested = parsed.get(key)
                if isinstance(nested, dict) and "summary" in nested:
                    try:
                        return RequirementRisk.model_validate(nested)
                    except Exception:
                        pass
    except (json.JSONDecodeError, ValueError):
        pass

    answer = result.answer
    risks = []
    for citation in answer.citations:
        risks.append(RiskItem(
            description=f"See {citation.article_title or citation.article_id}",
            article_id=citation.article_id,
            paragraph_num=citation.paragraph_num,
            provision=_format_provision(citation),
        ))

    return RequirementRisk(
        summary=answer.summary or "Model did not produce a valid risk assessment.",
        risks=risks,
        risk_level="medium",
    )


def _format_provision(citation) -> str:
    if citation.paragraph_num and ":" in citation.article_id:
        num = citation.article_id.split(":")[-1]
        return f"Article {num}({citation.paragraph_num})"
    return citation.article_title or citation.article_id

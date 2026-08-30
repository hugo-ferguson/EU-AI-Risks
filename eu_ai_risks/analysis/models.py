"""
Data structures for the agent layer.
"""

from pydantic import BaseModel, Field


class Citation(BaseModel):
    """A reference to a specific provision in the EU AI Act."""

    article_id: str = Field(description="e.g. 'art:14'")
    article_title: str = ""
    paragraph_num: int | None = Field(
        default=None, description="e.g. 1 for Article 14(1)"
    )
    text: str = Field(
        default="", description="The relevant text from the provision"
    )


class AgentAnswer(BaseModel):
    """Structured response from the graph-reading agent."""

    summary: str = Field(description="Natural language answer to the question")
    citations: list[Citation] = Field(default_factory=list)
    confidence: str = Field(
        default="medium",
        description="How confident the answer is: high, medium, low",
    )


class AgentResult(BaseModel):
    """Full result of an agent loop run, including metadata."""

    answer: AgentAnswer
    raw_content: str = Field(
        default="", description="The raw LLM output before structuring"
    )
    tool_calls_made: int = 0
    iterations: int = 0
    messages: list[dict] = Field(
        default_factory=list, description="Full conversation history"
    )


class RiskItem(BaseModel):
    """A single compliance risk identified for a requirement."""

    description: str = Field(description="What the risk is")
    severity: str = Field(
        default="medium", description="high, medium, or low"
    )
    article_id: str = Field(
        default="", description="Graph node ID, e.g. art:14"
    )
    paragraph_num: int | None = Field(
        default=None, description="e.g. 1 for paragraph (1)"
    )
    provision: str = Field(
        default="", description="Human-readable, e.g. Article 14(1)"
    )
    obligation_category: str = Field(
        default="",
        description=(
            "RequirementCategory key such as transparency, human_oversight, "
            "data_governance, or risk_management"
        ),
    )
    engineering_action: str = Field(
        default="",
        description="Practical software-engineering action suggested for this risk",
    )



class RequirementRisk(BaseModel):
    """Risk assessment result for a single requirement."""

    summary: str = Field(description="Overall compliance analysis")
    risks: list[RiskItem] = Field(default_factory=list)
    risk_level: str = Field(
        default="medium", description="Overall risk level: high, medium, low"
    )
    recommendations: list[str] = Field(default_factory=list)

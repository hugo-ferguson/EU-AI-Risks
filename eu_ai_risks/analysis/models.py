"""
Data models for the agent and risk assessment layers.
"""

from pydantic import BaseModel, Field


class Citation(BaseModel):
    article_id: str = Field(description="e.g. 'art:14'")
    article_title: str = ""
    paragraph_num: int | None = Field(
        default=None, description="e.g. 1 for Article 14(1)"
    )
    text: str = ""


class AgentAnswer(BaseModel):
    summary: str = Field(description="Natural language answer")
    citations: list[Citation] = Field(default_factory=list)
    confidence: str = Field(default="medium")


class AgentResult(BaseModel):
    answer: AgentAnswer
    raw_content: str = ""
    tool_calls_made: int = 0
    iterations: int = 0
    messages: list[dict] = Field(default_factory=list)


class RiskItem(BaseModel):
    description: str = Field(description="What the risk is")
    severity: str = Field(default="medium")
    article_id: str = Field(default="", description="Graph node ID, e.g. art:14")
    paragraph_num: int | None = Field(default=None)
    provision: str = Field(default="", description="e.g. Article 14(1)")


class RequirementRisk(BaseModel):
    summary: str = Field(description="Overall compliance analysis")
    risks: list[RiskItem] = Field(default_factory=list)
    risk_level: str = Field(default="medium")
    recommendations: list[str] = Field(default_factory=list)

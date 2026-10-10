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
    article_id: str = Field(
        default="", description="Graph node ID, e.g. art:14")
    paragraph_num: int | None = Field(default=None)
    provision: str = Field(default="", description="e.g. Article 14(1)")
    provision_id: str = Field(
        default="",
        description="Graph node id of the cited paragraph or point, e.g. art:10:p2:f",
    )
    obligation_category: str = Field(
        default="",
        description="RequirementCategory key, e.g. data_governance",
    )
    engineering_action: str = Field(
        default="",
        description="Practical engineering action for this risk",
    )
    citation_supplied: bool = Field(
        default=True,
        description="Whether the cited provision was among those retrieved for the assessment",
    )
    trace: list[str] = Field(
        default_factory=list,
        description="How the cited provision was reached in the graph, step by step",
    )
    scope_warning: str = Field(
        default="",
        description="Set when the cited provision's scope may exclude this system",
    )


class RequirementRisk(BaseModel):
    summary: str = Field(description="Overall compliance analysis")
    risks: list[RiskItem] = Field(default_factory=list)
    risk_level: str = Field(default="medium")
    recommendations: list[str] = Field(default_factory=list)
    # Filled by the assessor, not the model: the first step of every trace
    classification: list[str] = Field(
        default_factory=list,
        description="Annex III points the system was classified under",
    )
    selected_articles: list[str] = Field(
        default_factory=list,
        description="Articles chosen from the Act's index for this requirement",
    )

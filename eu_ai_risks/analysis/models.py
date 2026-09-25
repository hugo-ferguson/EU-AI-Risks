"""
Data models for the agent and risk assessment layers.
"""

from __future__ import annotations

from enum import Enum
from typing import Any
from pydantic import BaseModel, Field, field_validator


class AssessmentStatus(str, Enum):
    COMPLETE = "complete"
    INCOMPLETE = "incomplete"
    FAILED = "failed"


class RiskLevel(str, Enum):
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"
    UNKNOWN = "unknown"


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
    obligation_category: str = Field(
        default="",
        description="RequirementCategory key, e.g. data_governance",
    )
    engineering_action: str = Field(
        default="",
        description="Practical engineering action for this risk",
    )

    @field_validator("severity", mode="before")
    @classmethod
    def normalise_severity(cls, v: Any) -> str:
        if isinstance(v, RiskLevel):
            return v.value
        s = str(v or "medium").strip().lower()
        if s in ("high", "medium", "low", "unknown"):
            return s
        if s == "critical":
            return "high"
        return "medium"


class RequirementRisk(BaseModel):
    summary: str = Field(description="Overall compliance analysis")
    risks: list[RiskItem] = Field(default_factory=list)
    risk_level: str = Field(default="medium")
    recommendations: list[str] = Field(default_factory=list)
    status: AssessmentStatus = Field(default=AssessmentStatus.COMPLETE)
    validation_issues: list[str] = Field(default_factory=list)

    @field_validator("risk_level", mode="before")
    @classmethod
    def normalise_risk_level(cls, v: Any) -> str:
        if isinstance(v, RiskLevel):
            return v.value
        s = str(v or "medium").strip().lower()
        if s in ("high", "medium", "low", "unknown"):
            return s
        if s == "critical":
            return "high"
        return "medium"

"""
Data models for TypeSafe/Jev decision adapters and candidate evaluations.
"""

from __future__ import annotations

from enum import Enum
from typing import Any
from pydantic import BaseModel, Field


class DecisionStatus(str, Enum):
    SUCCEEDED = "succeeded"
    UNAVAILABLE = "unavailable"
    INVALID = "invalid"
    INSUFFICIENT_EVIDENCE = "insufficient_evidence"


class CandidateJudgment(BaseModel):
    """Judgment for a single provision candidate against a requirement."""
    candidate_id: str
    relevance: str = Field(
        default="uncertain",
        description="Choice outcome: 'direct', 'context', 'unrelated', 'uncertain'",
    )
    confidence: float | None = None
    probabilities: dict[str, float] = Field(default_factory=dict)
    rationale: str | None = None


class DecisionResult(BaseModel):
    """Structured result from a Jev decision task."""
    task: str = "provision_reranking"
    status: DecisionStatus = DecisionStatus.SUCCEEDED
    model: str = "jev-1.13.0"
    mode: str = "shadow"
    judgments: list[CandidateJudgment] = Field(default_factory=list)
    raw_response: dict[str, Any] = Field(default_factory=dict)
    error: str | None = None
    duration_ms: float = 0.0

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

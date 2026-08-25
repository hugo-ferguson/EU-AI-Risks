"""
Data structures for parsed requirements.
"""

from dataclasses import dataclass, field


@dataclass
class Requirement:
    """
    A single software requirement extracted from a requirements document.
    """

    id: str
    text: str
    source: str
    section: str | None = None
    title: str | None = None
    page: int | None = None
    metadata: dict[str, str] = field(default_factory=dict)
    triples: str | None = None

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "text": self.text,
            "source": self.source,
            "section": self.section,
            "title": self.title,
            "page": self.page,
            "metadata": self.metadata,
            "triples": self.triples,
        }

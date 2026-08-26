"""
Data structures for parsed requirements.
"""

import json
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

    def parsed_triples(self) -> list[dict]:
        if not self.triples:
            return []
        try:
            data = json.loads(self.triples)
            if isinstance(data, list):
                return [t for t in data if "subject" in t]
            if isinstance(data, dict) and "subject" in data:
                return [data]
            return []
        except (json.JSONDecodeError, ValueError):
            return []

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "text": self.text,
            "source": self.source,
            "section": self.section,
            "title": self.title,
            "page": self.page,
            "metadata": self.metadata,
            "triples": self.parsed_triples(),
        }

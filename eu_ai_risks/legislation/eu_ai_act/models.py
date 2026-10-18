"""
Shared data structures used across the project.
"""

from dataclasses import dataclass, field


@dataclass
class Segment:
    """
    type: chapter/section/article/paragraph/annex/point
    id: a unique identifier
    num: the chapter/article/paragraph/point number from the Act
    title: the chapter/article title, or a point's letter or number
            (paragraphs aren't titled)
    parent_id: the id of the parent node (chapter, article, paragraph, annex
            or point id)
    body: the text following the title of a chapter/article, or a paragraph's
            text.
    """

    type: str
    id: str
    num: int
    title: str | None = None
    body: list[str] = field(default_factory=list)
    parent_id: str | None = None

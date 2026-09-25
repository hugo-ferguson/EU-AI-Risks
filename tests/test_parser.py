"""
Unit tests for legislation parser and unnumbered article bodies (R09).
"""

from eu_ai_risks.legislation.eu_ai_act.models import Segment
from eu_ai_risks.legislation.eu_ai_act.parser import extract_paragraphs


def test_extract_paragraphs_numbered():
    """Numbered articles should extract their numbered paragraphs."""
    article = Segment(
        type="article",
        id="art:14",
        num=14,
        parent_id="ch:III",
        title="Human oversight",
        body=[
            "1. High-risk AI systems shall be designed...",
            "They shall be overseen by natural persons.",
            "2. The oversight measures shall...",
        ],
    )
    paragraphs = extract_paragraphs(article)
    assert len(paragraphs) == 2
    assert paragraphs[0].id == "art:14:p1"
    assert paragraphs[0].num == 1
    assert len(paragraphs[0].body) == 2
    assert paragraphs[1].id == "art:14:p2"
    assert paragraphs[1].num == 2


def test_extract_paragraphs_unnumbered():
    """Unnumbered articles (like Article 4) must extract a p0 provision segment (R09)."""
    article = Segment(
        type="article",
        id="art:4",
        num=4,
        parent_id="ch:I",
        title="AI literacy",
        body=[
            "Providers and deployers of AI systems shall take measures to ensure",
            "to their best extent a sufficient level of AI literacy of their staff.",
        ],
    )
    paragraphs = extract_paragraphs(article)
    assert len(paragraphs) == 1
    assert paragraphs[0].id == "art:4:p0"
    assert paragraphs[0].num == 0
    assert len(paragraphs[0].body) == 2

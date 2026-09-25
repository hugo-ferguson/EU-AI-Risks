"""
Unit tests for report generation, summary counts, and status indicators (R05, R08).
"""

from eu_ai_risks.analysis.models import AssessmentStatus, RequirementRisk, RiskItem
from eu_ai_risks.analysis.risk_report import entries_from_assessments, render_markdown_report


def test_render_markdown_report_with_failures():
    """Report must dynamically count all risk levels and explicitly highlight failures."""
    assessment_entries = [
        {
            "requirement": {"id": "REQ-1", "text": "Authenticate users"},
            "assessment": RequirementRisk(
                summary="Passed with high risk",
                risk_level="high",
                status=AssessmentStatus.COMPLETE,
                risks=[RiskItem(description="Risk", severity="high")],
            ),
            "citations": [],
        },
        {
            "requirement": {"id": "REQ-2", "text": "Log audit records"},
            "assessment": RequirementRisk(
                summary="Model failed to produce valid JSON",
                risk_level="unknown",
                status=AssessmentStatus.FAILED,
                validation_issues=["JSON parse error"],
            ),
            "citations": [],
        },
    ]

    entries = entries_from_assessments(assessment_entries)
    report = render_markdown_report(entries)

    assert "- High: 1" in report
    assert "- Unknown: 1" in report
    assert "- Failed: 1" in report
    assert "REQ-1" in report
    assert "REQ-2" in report

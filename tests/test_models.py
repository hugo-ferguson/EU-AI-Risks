"""
Unit tests for data models, risk normalization, and assessment status enums (R05, R08).
"""

from eu_ai_risks.analysis.models import (
    AssessmentStatus,
    RequirementRisk,
    RiskItem,
    RiskLevel,
)


def test_risk_level_normalization():
    """Risk levels must normalize case, whitespace, and unsupported labels (R08)."""
    item1 = RiskItem(description="Risk 1", severity="HIGH")
    assert item1.severity == "high"

    item2 = RiskItem(description="Risk 2", severity="  critical ")
    assert item2.severity == "high"

    item3 = RiskItem(description="Risk 3", severity="unsupported_label")
    assert item3.severity == "medium"

    risk = RequirementRisk(summary="Test", risk_level=" LOW ")
    assert risk.risk_level == "low"


def test_assessment_status_enum():
    """RequirementRisk must support AssessmentStatus enums (R05)."""
    risk_complete = RequirementRisk(summary="All good", status=AssessmentStatus.COMPLETE)
    assert risk_complete.status == AssessmentStatus.COMPLETE

    risk_failed = RequirementRisk(
        summary="Model failure",
        status=AssessmentStatus.FAILED,
        risk_level=RiskLevel.UNKNOWN,
        validation_issues=["Timeout connecting to model"],
    )
    assert risk_failed.status == AssessmentStatus.FAILED
    assert risk_failed.risk_level == "unknown"
    assert "Timeout" in risk_failed.validation_issues[0]

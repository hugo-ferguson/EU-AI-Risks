"""
Unit tests for risk assessment failure handling and status reporting (R05).
"""

from eu_ai_risks.analysis.models import AssessmentStatus
from eu_ai_risks.analysis.risk_assessor import _parse_assessment


def test_parse_assessment_invalid_types():
    """Non-dict model responses must result in FAILED status, not low risk."""
    assessment1 = _parse_assessment("some raw unparseable string")
    assert assessment1.status == AssessmentStatus.FAILED
    assert assessment1.risk_level == "unknown"

    assessment2 = _parse_assessment(["list", "of", "items"])
    assert assessment2.status == AssessmentStatus.FAILED
    assert assessment2.risk_level == "unknown"


def test_parse_assessment_valid_dict():
    """Valid dict response produces COMPLETE status."""
    valid_data = {
        "summary": "Compliance analysis successful.",
        "risk_level": "high",
        "risks": [
            {
                "description": "High risk of bias in data",
                "severity": "high",
                "obligation_category": "data_governance",
            }
        ],
        "recommendations": ["Implement bias audit"],
    }
    assessment = _parse_assessment(valid_data)
    assert assessment.status == AssessmentStatus.COMPLETE
    assert assessment.risk_level == "high"
    assert len(assessment.risks) == 1

"""
Unit tests for TypeSafe / Jev decision adapter and candidate reranker (J1, J2).
"""

from eu_ai_risks.decisions import (
    DecisionStatus,
    TypeSafeConfig,
    TypeSafeDecisionClient,
)
from eu_ai_risks.analysis.jev_reranker import rerank_candidates_with_jev


def test_typesafe_client_disabled_mode():
    """In 'off' mode, judge_candidates must return UNAVAILABLE status without network calls."""
    config = TypeSafeConfig(mode="off")
    client = TypeSafeDecisionClient(config=config)
    assert not client.is_enabled

    result = client.judge_candidates(
        "The system shall log access.",
        [{"id": "art:12:p1", "text": "Record keeping requirement"}],
    )
    assert result.status == DecisionStatus.UNAVAILABLE
    assert "off" in result.error


def test_jev_reranker_shadow_mode(monkeypatch):
    """In shadow mode, candidate order must remain unchanged while recording decision result."""
    candidates = [
        {"id": "art:10:p1", "text": "Data governance"},
        {"id": "art:14:p1", "text": "Human oversight"},
    ]

    # Mock client simulating successful Jev responses
    class MockClient:
        is_enabled = True

        def judge_candidates(self, req_text, cands):
            from eu_ai_risks.decisions.models import CandidateJudgment, DecisionResult
            return DecisionResult(
                task="provision_reranking",
                status=DecisionStatus.SUCCEEDED,
                mode="shadow",
                judgments=[
                    CandidateJudgment(candidate_id="art:14:p1", relevance="direct", confidence=0.9),
                    CandidateJudgment(candidate_id="art:10:p1", relevance="context", confidence=0.7),
                ],
            )

    reranked, decision = rerank_candidates_with_jev(
        "Operator must be able to intervene.",
        candidates,
        client=MockClient(),
    )

    # In shadow mode, returned candidates retain exact initial order
    assert reranked[0]["id"] == "art:10:p1"
    assert reranked[1]["id"] == "art:14:p1"
    assert decision is not None
    assert decision.status == DecisionStatus.SUCCEEDED
    assert len(decision.judgments) == 2


def test_jev_reranker_active_mode(monkeypatch):
    """In active rerank mode, direct relevance candidates must be sorted first."""
    candidates = [
        {"id": "art:10:p1", "text": "Data governance"},
        {"id": "art:14:p1", "text": "Human oversight"},
    ]

    class MockClient:
        is_enabled = True

        def judge_candidates(self, req_text, cands):
            from eu_ai_risks.decisions.models import CandidateJudgment, DecisionResult
            return DecisionResult(
                task="provision_reranking",
                status=DecisionStatus.SUCCEEDED,
                mode="rerank",
                judgments=[
                    CandidateJudgment(candidate_id="art:10:p1", relevance="context", confidence=0.7),
                    CandidateJudgment(candidate_id="art:14:p1", relevance="direct", confidence=0.9),
                ],
            )

    reranked, decision = rerank_candidates_with_jev(
        "Operator must be able to intervene.",
        candidates,
        client=MockClient(),
    )

    # In active rerank mode, 'direct' candidate is moved to front
    assert reranked[0]["id"] == "art:14:p1"
    assert reranked[1]["id"] == "art:10:p1"

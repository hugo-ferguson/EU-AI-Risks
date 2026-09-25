"""
Jev decision adapter hook for regulatory provision reranking (shadow and active modes).
"""

from __future__ import annotations

import logging
from typing import Any

from eu_ai_risks.decisions import (
    DecisionResult,
    DecisionStatus,
    TypeSafeDecisionClient,
)

logger = logging.getLogger("eu_ai_risks.analysis.jev_reranker")

# Priority map for Jev relevance categories in rerank mode
_RELEVANCE_PRIORITY = {
    "direct": 0,
    "context": 1,
    "uncertain": 2,
    "unrelated": 3,
}


def rerank_candidates_with_jev(
    requirement_text: str,
    candidates: list[dict[str, Any]],
    client: TypeSafeDecisionClient | None = None,
) -> tuple[list[dict[str, Any]], DecisionResult | None]:
    """
    Evaluate candidate paragraphs with TypeSafe Jev.
    In 'shadow' mode: records evaluation without altering candidate ordering.
    In 'rerank' mode: sorts candidate paragraphs based on Jev relevance judgments.
    """
    decision_client = client or TypeSafeDecisionClient()
    if not decision_client.is_enabled:
        return candidates, None

    decision = decision_client.judge_candidates(requirement_text, candidates)
    if decision.status != DecisionStatus.SUCCEEDED or not decision.judgments:
        logger.debug("Jev decision returned non-success (%s); preserving baseline candidates.", decision.status)
        return candidates, decision

    logger.info(
        "Jev completed %s mode judgment for %d candidates (duration: %.1fms)",
        decision.mode,
        len(decision.judgments),
        decision.duration_ms,
    )

    if decision.mode == "shadow":
        # Shadow mode: evaluate and record, but preserve exact baseline ordering
        return candidates, decision

    # Active rerank mode: sort by Jev relevance priority, preserving baseline ties
    judgment_map = {j.candidate_id: j for j in decision.judgments}

    def _sort_key(candidate: dict[str, Any]) -> tuple[int, float]:
        cid = candidate.get("id", "")
        judgment = judgment_map.get(cid)
        if judgment:
            priority = _RELEVANCE_PRIORITY.get(judgment.relevance, 2)
            # Higher confidence is better within the same category
            conf = -(judgment.confidence or 0.0)
            return priority, conf
        return 2, 0.0

    reranked = sorted(candidates, key=_sort_key)
    return reranked, decision

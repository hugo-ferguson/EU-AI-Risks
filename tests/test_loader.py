"""
Unit tests for requirements ingestion, multi-line assembly, and triple validation (R04, R06, R07, R19).
"""

import json
from pathlib import Path

from eu_ai_risks.requirements.loader import (
    _assemble_logical_blocks,
    _extract_requirement_id,
    _strip_requirement_prefix,
    _split_requirement,
    load_requirements,
)


def test_assemble_logical_blocks_continuation():
    """Wrapped requirement continuation lines must be joined into one block (R04)."""
    raw_lines = [
        {"text": "REQ-001 The system shall retain audit records for", "page": 1},
        {"text": "five years after the final decision.", "page": 1},
        {"text": "REQ-002 The model must not use biometric data.", "page": 2},
    ]

    blocks = _assemble_logical_blocks(raw_lines)
    assert len(blocks) == 2
    assert blocks[0]["text"] == "REQ-001 The system shall retain audit records for five years after the final decision."
    assert blocks[0]["page"] == 1
    assert blocks[1]["text"] == "REQ-002 The model must not use biometric data."
    assert blocks[1]["page"] == 2


def test_prefix_regex_embedded_id_preservation():
    """Prefix regex must only strip IDs at the start, preserving embedded IDs (R19)."""
    # At start: should extract and strip
    text1 = "REQ-001 The system shall log security events."
    assert _extract_requirement_id(text1) == "REQ-001"
    assert _strip_requirement_prefix(text1) == "The system shall log security events."

    # Mid-sentence: should NOT strip embedded requirement ID
    text2 = "The system shall interface with REQ-100 before launch."
    assert _strip_requirement_prefix(text2) == "The system shall interface with REQ-100 before launch."


def test_split_requirement_triple_validation(monkeypatch):
    """Triple extraction must strictly validate subject, predicate, and object (R07)."""
    # Mock complete_json to return one valid triple and one invalid triple (missing predicate)
    mock_response = [
        {"subject": "the system", "predicate": "logs", "object": "audit events"},
        {"subject": "the system"},  # Malformed: missing predicate and object
        "not a dict",
    ]
    import eu_ai_risks.requirements.loader as loader
    monkeypatch.setattr(loader, "complete_json", lambda **kwargs: mock_response)

    triples = _split_requirement("Some requirement")
    assert len(triples) == 1
    assert triples[0] == {
        "subject": "the system",
        "predicate": "logs",
        "object": "audit events",
    }


def test_load_json_without_triples(tmp_path):
    """JSON requirements must be loaded and assessable even without triples (R06)."""
    json_file = tmp_path / "reqs.json"
    data = [
        {"id": "FR-01", "text": "The system shall authenticate users."},
        {"id": "FR-02", "text": "The system shall encrypt data at rest."},
    ]
    json_file.write_text(json.dumps(data), encoding="utf-8")

    reqs = load_requirements(json_file, with_triples=False)
    assert len(reqs) == 2
    assert reqs[0].id == "FR-01"
    assert reqs[0].text == "The system shall authenticate users."
    assert reqs[1].id == "FR-02"
    assert reqs[1].text == "The system shall encrypt data at rest."

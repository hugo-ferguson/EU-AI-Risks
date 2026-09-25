"""
Unit tests for web storage, token resolution, and containment boundaries (R01, R15).
"""

import tempfile
from pathlib import Path
from fastapi import HTTPException
import pytest

from eu_ai_risks.web_app import (
    OUTPUT_DIR,
    UPLOAD_PREFIX,
    _resolve_upload_token,
    download_report,
)


def test_resolve_upload_token_valid():
    """A valid upload token pointing to an existing file in tempdir resolves properly."""
    temp_base = Path(tempfile.gettempdir())
    upload_dir = temp_base / f"{UPLOAD_PREFIX}valid123"
    upload_dir.mkdir(parents=True, exist_ok=True)
    test_file = upload_dir / "uploaded.txt"
    test_file.write_text("dummy requirements")

    try:
        resolved = _resolve_upload_token(f"{UPLOAD_PREFIX}valid123")
        assert resolved is not None
        assert resolved.resolve() == test_file.resolve()
    finally:
        if test_file.exists():
            test_file.unlink()
        if upload_dir.exists():
            upload_dir.rmdir()


def test_resolve_upload_token_traversal_rejected():
    """Path traversal attempts with '..' or path separators must return None."""
    assert _resolve_upload_token(f"{UPLOAD_PREFIX}../../etc") is None
    assert _resolve_upload_token(f"{UPLOAD_PREFIX}../") is None
    assert _resolve_upload_token(f"../{UPLOAD_PREFIX}test") is None
    assert _resolve_upload_token("invalid_prefix_123") is None
    assert _resolve_upload_token("") is None


def test_download_report_security_and_404():
    """Download route must reject non-markdown files, traversal, and missing reports."""
    # Attempt to download state JSON file
    with pytest.raises(HTTPException) as exc_info:
        download_report("results-1234567890abcdef1234567890abcdef.json")
    assert exc_info.value.status_code == 404

    # Traversal attempt
    with pytest.raises(HTTPException) as exc_info:
        download_report("../../../etc/passwd")
    assert exc_info.value.status_code == 404

    # Non-existent report
    with pytest.raises(HTTPException) as exc_info:
        download_report("risk-assessment-00000000000000000000000000000000.md")
    assert exc_info.value.status_code == 404


def test_download_report_valid():
    """Valid markdown report file downloads with 200 OK."""
    token = "risk-assessment-11112222333344445555666677778888.md"
    report_file = OUTPUT_DIR / token
    report_file.write_text("# Report", encoding="utf-8")

    try:
        response = download_report(token)
        assert response.status_code == 200
        assert response.media_type == "text/markdown"
    finally:
        if report_file.exists():
            report_file.unlink()

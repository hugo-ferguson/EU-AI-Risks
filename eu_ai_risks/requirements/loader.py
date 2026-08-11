"""
Load and parse requirement documents (PDF, docx, etc.) into structured data.
"""

import re
from pathlib import Path

import pdfplumber

from eu_ai_risks.requirements.models import Requirement

RE_REQUIREMENT_ID = re.compile(
	r'\b((?:FR|NFR|REQ|R|UC|SR|SYS|SRS)[-_ ]?\d+(?:\.\d+)*)\b',
	re.IGNORECASE,
)
RE_NUMBERED_ITEM = re.compile(r'^(\d+(?:\.\d+)*|[A-Z]\d+)[.)]\s+(.+)$')
RE_HEADING = re.compile(r'^(\d+(?:\.\d+)*)\s+([A-Z][^\n]{2,120})$')
RE_REQUIREMENT_VERB = re.compile(
	r'\b(shall|should|must|needs to|is required to|may not|must not)\b',
	re.IGNORECASE,
)

SUPPORTED_EXTENSIONS = {".txt", ".md", ".markdown", ".pdf", ".docx"}


def load_requirements(document_path: Path) -> list[Requirement]:
	"""
	Load a requirements document and extract candidate requirements.

	:param document_path: path to a .txt, .md, .pdf, or .docx document.
	:return: extracted requirements with source traceability.
	"""

	document_path = document_path.expanduser()
	if not document_path.exists():
		raise FileNotFoundError(f"Requirements document not found: {document_path}")

	extension = document_path.suffix.lower()
	if extension not in SUPPORTED_EXTENSIONS:
		raise ValueError(
			f"Unsupported requirements document type '{extension}'. "
			f"Supported types: {', '.join(sorted(SUPPORTED_EXTENSIONS))}"
		)

	if extension == ".pdf":
		blocks = _read_pdf_blocks(document_path)
	elif extension == ".docx":
		blocks = _read_docx_blocks(document_path)
	else:
		blocks = _read_text_blocks(document_path)

	return _extract_requirements(blocks, document_path)


def _read_text_blocks(document_path: Path) -> list[dict]:
	text = document_path.read_text(encoding="utf-8")
	return [
		{"text": line.strip(), "page": None}
		for line in text.splitlines()
		if line.strip()
	]


def _read_pdf_blocks(document_path: Path) -> list[dict]:
	blocks = []
	with pdfplumber.open(document_path) as pdf:
		for page_number, page in enumerate(pdf.pages, start=1):
			text = page.extract_text() or ""
			for line in text.splitlines():
				if line.strip():
					blocks.append({"text": line.strip(), "page": page_number})
	return blocks


def _read_docx_blocks(document_path: Path) -> list[dict]:
	try:
		from docx import Document
	except ImportError as exc:
		raise ImportError(
			"Reading .docx files requires python-docx. Install the project "
			"with its current dependencies, or convert the document to PDF/text."
		) from exc

	document = Document(document_path)
	return [
		{"text": paragraph.text.strip(), "page": None}
		for paragraph in document.paragraphs
		if paragraph.text.strip()
	]


def _extract_requirements(
	blocks: list[dict], document_path: Path
) -> list[Requirement]:
	requirements = []
	current_section = None
	current_title = None
	next_id = 1

	for block in blocks:
		text = _normalize_text(block["text"])
		if not text:
			continue

		heading_match = RE_HEADING.match(text)
		if heading_match and not _looks_like_requirement(text):
			current_section = heading_match.group(1)
			current_title = heading_match.group(2)
			continue

		if not _looks_like_requirement(text):
			continue

		explicit_id = _extract_requirement_id(text)
		requirement_id = explicit_id or f"REQ-{next_id:03d}"
		next_id += 1

		requirements.append(Requirement(
			id=requirement_id,
			text=_strip_requirement_prefix(text),
			source=str(document_path),
			section=current_section,
			title=current_title,
			page=block.get("page"),
		))

	return _deduplicate_requirements(requirements)


def _normalize_text(text: str) -> str:
	return re.sub(r'\s+', ' ', text).strip()


def _looks_like_requirement(text: str) -> bool:
	if RE_REQUIREMENT_ID.search(text) and len(text.split()) >= 4:
		return True
	if RE_REQUIREMENT_VERB.search(text) and len(text.split()) >= 5:
		return True
	numbered_match = RE_NUMBERED_ITEM.match(text)
	return bool(numbered_match and RE_REQUIREMENT_VERB.search(numbered_match.group(2)))


def _extract_requirement_id(text: str) -> str | None:
	match = RE_REQUIREMENT_ID.search(text)
	if not match:
		return None
	return re.sub(r'\s+', '-', match.group(1).upper())


def _strip_requirement_prefix(text: str) -> str:
	text = RE_REQUIREMENT_ID.sub('', text, count=1).strip(" :-\t")
	numbered_match = RE_NUMBERED_ITEM.match(text)
	if numbered_match:
		return numbered_match.group(2).strip()
	return text


def _deduplicate_requirements(
	requirements: list[Requirement],
) -> list[Requirement]:
	seen = set()
	unique_requirements = []

	for requirement in requirements:
		key = requirement.text.lower()
		if key in seen:
			continue
		seen.add(key)
		unique_requirements.append(requirement)

	return unique_requirements

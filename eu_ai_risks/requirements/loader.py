"""
Load and parse requirement documents (PDF, docx, etc.) into structured data.
"""

from __future__ import annotations

import json
import re
from pathlib import Path

from eu_ai_risks.db import get_session
from eu_ai_risks.embeddings import embed_batch
from eu_ai_risks.embeddings.client import EMBEDDING_DIMENSIONS
from eu_ai_risks.llm import complete_json
from eu_ai_risks.requirements.models import Requirement

RE_REQUIREMENT_ID = re.compile(
    r'\b((?:CH3-FR|CH3-NFR|FR|NFR|REQ|R|UC|SR|SYS|SRS)[-_ ]?\d+(?:\.\d+)*)\b',
    re.IGNORECASE,
)
# Anchored to line/block start for accurate prefix detection without mangling mid-sentence IDs
RE_PREFIX_REQUIREMENT_ID = re.compile(
    r'^\s*((?:CH3-FR|CH3-NFR|FR|NFR|REQ|R|UC|SR|SYS|SRS)[-_ ]?\d+(?:\.\d+)*)\b\s*[:\-\.]?\s*',
    re.IGNORECASE,
)
RE_NUMBERED_ITEM = re.compile(r'^(\d+(?:\.\d+)*|[A-Z]\d+)[.)]\s+(.+)$')
RE_HEADING = re.compile(r'^(\d+(?:\.\d+)*)\s+([A-Z][^\n]{2,120})$')
RE_REQUIREMENT_VERB = re.compile(
    r'\b(shall|should|must|needs to|is required to|may not|must not)\b',
    re.IGNORECASE,
)

SUPPORTED_EXTENSIONS = {".json", ".txt", ".md", ".markdown", ".pdf", ".docx"}


def load_requirements(
    document_path: Path,
    *,
    with_triples: bool = True,
    document_id: str | None = None,
) -> list[Requirement]:
    """Load a requirements document and extract candidate requirements."""
    document_path = document_path.expanduser()
    if not document_path.exists():
        raise FileNotFoundError(
            f"Requirements document not found: {document_path}")

    extension = document_path.suffix.lower()
    if extension not in SUPPORTED_EXTENSIONS:
        raise ValueError(
            f"Unsupported requirements document type '{extension}'. "
            f"Supported types: {', '.join(sorted(SUPPORTED_EXTENSIONS))}"
        )

    doc_id = document_id or document_path.stem

    if extension == ".json":
        return _requirements_from_json(document_path, with_triples=with_triples, document_id=doc_id)
    if extension == ".pdf":
        raw_lines = _read_pdf_blocks(document_path)
    elif extension == ".docx":
        raw_lines = _read_docx_blocks(document_path)
    else:
        raw_lines = _read_text_blocks(document_path)

    # Assemble logical multi-line blocks before requirement detection
    blocks = _assemble_logical_blocks(raw_lines)
    return _extract_requirements(blocks, document_path, with_triples=with_triples, document_id=doc_id)


def parse_requirements(document_path: Path, document_id: str | None = None) -> list[Requirement]:
    """Load requirements without LLM triple extraction."""
    return load_requirements(document_path, with_triples=False, document_id=document_id)


def _read_text_blocks(document_path: Path) -> list[dict]:
    text = document_path.read_text(encoding="utf-8")
    return [
        {"text": line.strip(), "page": None}
        for line in text.splitlines()
        if line.strip()
    ]


def _read_pdf_blocks(document_path: Path) -> list[dict]:
    try:
        import pdfplumber
    except ImportError as exc:
        raise ImportError("Reading .pdf requires pdfplumber.") from exc

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

    document = Document(str(document_path))

    blocks = [
        {"text": paragraph.text.strip(), "page": None}
        for paragraph in document.paragraphs
        if paragraph.text.strip()
    ]

    # Include table cells if present
    for table in document.tables:
        for row in table.rows:
            for cell in row.cells:
                text = cell.text.strip()
                if text:
                    blocks.append({"text": text, "page": None})

    return blocks


def _assemble_logical_blocks(raw_lines: list[dict]) -> list[dict]:
    """
    Assemble physical lines into coherent logical requirement/heading blocks.
    Preserves continuation lines in wrapped text while respecting new headings or IDs.
    """
    blocks: list[dict] = []
    current_block: dict | None = None

    for item in raw_lines:
        text = item["text"].strip()
        page = item.get("page")
        if not text:
            continue

        is_heading = bool(RE_HEADING.match(text) and not _looks_like_requirement(text))
        is_new_item = bool(
            RE_PREFIX_REQUIREMENT_ID.match(text)
            or RE_NUMBERED_ITEM.match(text)
            or is_heading
        )

        if current_block is None:
            current_block = {"text": text, "page": page}
        elif is_new_item:
            blocks.append(current_block)
            current_block = {"text": text, "page": page}
        else:
            # Continuation line
            current_text = current_block["text"]
            if current_text.endswith("-"):
                current_block["text"] = current_text[:-1] + text
            else:
                current_block["text"] = current_text + " " + text

    if current_block:
        blocks.append(current_block)

    return blocks


def _extract_requirements(
    blocks: list[dict],
    document_path: Path,
    *,
    with_triples: bool = True,
    document_id: str | None = None,
) -> list[Requirement]:
    requirements = []
    current_section = None
    current_title = None
    next_id = 1
    doc_id = document_id or document_path.stem

    for block in blocks:
        text = _normalise_text(block["text"])
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

        requirement_text = _strip_requirement_prefix(text)
        triples = _split_requirement(requirement_text) if with_triples else []

        requirements.append(Requirement(
            id=requirement_id,
            text=requirement_text,
            source=str(document_path),
            section=current_section,
            title=current_title,
            page=block.get("page"),
            document_id=doc_id,
            triples=triples
        ))

    return _deduplicate_requirements(requirements)


def _requirements_from_json(
    document_path: Path,
    *,
    with_triples: bool = True,
    document_id: str | None = None,
) -> list[Requirement]:
    data = json.loads(document_path.read_text(encoding="utf-8"))
    if isinstance(data, dict):
        for key in ("requirements", "items", "data"):
            if isinstance(data.get(key), list):
                data = data[key]
                break

    if not isinstance(data, list):
        raise ValueError(
            "JSON requirements file must contain a list of requirement objects.")

    doc_id = document_id or document_path.stem
    requirements: list[Requirement] = []
    for index, item in enumerate(data, start=1):
        if isinstance(item, str):
            text = re.sub(r"\s+", " ", item).strip()
            requirement_id = f"REQ-{index:03d}"
        elif isinstance(item, dict):
            text = re.sub(
                r"\s+", " ",
                str(item.get("text") or item.get("requirement")
                    or item.get("description") or ""),
            ).strip()
            requirement_id = str(item.get("id") or item.get(
                "requirement_id") or f"REQ-{index:03d}")
        else:
            continue
        if text:
            triples = _split_requirement(text) if with_triples else []
            requirements.append(Requirement(
                id=requirement_id,
                text=text,
                source=str(document_path),
                document_id=doc_id,
                triples=triples,
            ))
    return _deduplicate_requirements(requirements)


def _normalise_text(text: str) -> str:
    return re.sub(r'\s+', ' ', text).strip()


def _looks_like_requirement(text: str) -> bool:
    if RE_PREFIX_REQUIREMENT_ID.match(text) and len(text.split()) >= 4:
        return True
    if RE_REQUIREMENT_ID.search(text) and len(text.split()) >= 4:
        return True
    if RE_REQUIREMENT_VERB.search(text) and len(text.split()) >= 5:
        return True
    numbered_match = RE_NUMBERED_ITEM.match(text)
    return bool(numbered_match and RE_REQUIREMENT_VERB.search(numbered_match.group(2)))


def _extract_requirement_id(text: str) -> str | None:
    match = RE_PREFIX_REQUIREMENT_ID.match(text)
    if not match:
        match = RE_REQUIREMENT_ID.search(text)
        if not match or match.start() > 10:
            return None
    return re.sub(r'\s+', '-', match.group(1).upper())


def _strip_requirement_prefix(text: str) -> str:
    match = RE_PREFIX_REQUIREMENT_ID.match(text)
    if match:
        text = text[match.end():].strip(" :-\t")
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


_TRIPLE_EXTRACTION_SYSTEM = """\
You are a requirements analysis assistant. Extract semantic triples from \
a software requirement.

A triple consists of:
- Subject: the entity or system performing or being described
- Predicate: the relationship, action, or constraint
- Object: what the action is performed on or the constraint applies to

Rules:
- Extract only what is explicitly stated
- A single requirement may contain multiple triples
- Use concise, normalised terms (e.g. "the system" not "it")
- Split compound objects into separate triples
- Each triple must have exactly one subject, predicate, and object
- Respond with a JSON array of triple objects, nothing else"""


def _split_requirement(requirement_text: str) -> list[dict]:
    try:
        result = complete_json(
            prompt=f'Extract triples from: "{requirement_text}"',
            system=_TRIPLE_EXTRACTION_SYSTEM,
        )
    except Exception:
        return []
    if isinstance(result, dict):
        for value in result.values():
            if isinstance(value, list):
                result = value
                break
    if not isinstance(result, list):
        result = [result] if isinstance(result, dict) else []

    # Strictly validate that all three components (subject, predicate, object) are non-empty strings
    valid_triples = []
    for item in result:
        if not isinstance(item, dict):
            continue
        subj = str(item.get("subject", "")).strip()
        pred = str(item.get("predicate", "")).strip()
        obj = str(item.get("object", "")).strip()
        if subj and pred and obj:
            valid_triples.append({
                "subject": subj,
                "predicate": pred,
                "object": obj,
            })
    return valid_triples


def write_triples(document_path: Path, document_id: str | None = None) -> None:
    """
    Persist Requirement nodes and scoped Assertion triples to Neo4j.
    Ensures requirements are persisted even when zero triples exist.
    """
    document_path = Path(document_path).expanduser()
    doc_id = document_id or document_path.stem
    requirements = load_requirements(document_path, with_triples=True, document_id=doc_id)

    if not requirements:
        print(f"No requirements found in {document_path}.")
        return

    # 1. Persist all Requirement nodes linked to Document node
    req_rows = [
        {
            "id": f"{doc_id}:{r.id}" if not r.id.startswith(f"{doc_id}:") else r.id,
            "raw_id": r.id,
            "text": r.text,
            "document_id": doc_id,
            "source": str(document_path),
            "section": r.section or "",
            "title": r.title or "",
            "page": r.page or 0,
        }
        for r in requirements
    ]

    with get_session() as session:
        session.run("""
            UNWIND $rows AS row
            MERGE (d:Document {id: row.document_id})
            MERGE (req:Requirement {id: row.id})
            SET req.raw_id = row.raw_id,
                req.text = row.text,
                req.document_id = row.document_id,
                req.source = row.source,
                req.section = row.section,
                req.title = row.title,
                req.page = row.page
            MERGE (d)-[:CONTAINS_REQUIREMENT]->(req)
        """, rows=req_rows)

    print(f"  Wrote {len(req_rows)} Requirement nodes for document '{doc_id}'.")

    # 2. Persist requirement-scoped assertions
    assertion_rows = []
    for r in requirements:
        scoped_req_id = f"{doc_id}:{r.id}" if not r.id.startswith(f"{doc_id}:") else r.id
        for idx, triple in enumerate(r.triples):
            assertion_rows.append({
                "assertion_id": f"{scoped_req_id}:a{idx}",
                "requirement_id": scoped_req_id,
                "subject": triple["subject"],
                "predicate": triple["predicate"],
                "object": triple["object"],
            })

    if not assertion_rows:
        print(f"  No triples extracted to persist for document '{doc_id}'.")
        return

    batch_size = 500
    for i in range(0, len(assertion_rows), batch_size):
        batch = assertion_rows[i:i + batch_size]
        with get_session() as session:
            session.run("""
                UNWIND $rows AS row
                MATCH (req:Requirement {id: row.requirement_id})

                MERGE (s:Entity {name: row.subject})
                MERGE (o:Entity {name: row.object})

                // Requirement-scoped Assertion node
                MERGE (a:Assertion {id: row.assertion_id})
                SET a.predicate = row.predicate
                MERGE (req)-[:ASSERTS]->(a)
                MERGE (a)-[:HAS_SUBJECT]->(s)
                MERGE (a)-[:HAS_OBJECT]->(o)

                // Shared graph discovery relationship
                MERGE (s)-[:RELATION {type: row.predicate}]->(o)
                MERGE (req)-[:EXTRACTED_FROM]->(s)
            """, rows=batch)
            print(f"  Wrote {i + len(batch)}/{len(assertion_rows)} assertion triples")

            generate_and_write_triple_embeddings(session, batch)


def generate_and_write_triple_embeddings(session, all_triples: list[dict]) -> None:
    entities = {}
    for triple in all_triples:
        for key in ("subject", "object"):
            name = triple[key]
            if name not in entities:
                entities[name] = name
    if entities:
        entity_ids = list(entities.keys())
        entity_texts = list(entities.values())

        print(f"  Generating embeddings for {len(entity_texts)} Entity nodes...")
        entity_embeddings = embed_batch(entity_texts)

        entity_rows = [
            {"name": name, "embedding": embedding}
            for name, embedding in zip(entity_ids, entity_embeddings)
        ]

        session.run("""
            UNWIND $rows AS row
            MATCH (n:Entity {name: row.name})
            SET n.embedding = row.embedding
            """,
            rows=entity_rows
        )
        print(f"  Wrote embeddings for {len(entity_rows)} Entity nodes.")

    for label in ("Entity",):
        session.run(f"""
            CREATE VECTOR INDEX {label.lower()}_embedding IF NOT EXISTS
            FOR (n:{label}) ON (n.embedding)
            OPTIONS {{indexConfig: {{
                `vector.dimensions`: {EMBEDDING_DIMENSIONS},
                `vector.similarity_function`: 'cosine'
            }}}}
        """)
        print(f"  Created vector index for {label}.")


if __name__ == "__main__":
    doc = Path("./examples/sample-srs.md")
    write_triples(doc)

"""
Load and parse requirement documents (PDF, docx, etc.) into structured data.
"""

import re
from pathlib import Path

import pdfplumber
import json

from eu_ai_risks.requirements.models import Requirement
from eu_ai_risks.embeddings import embed_batch
from eu_ai_risks.embeddings.client import EMBEDDING_DIMENSIONS
from eu_ai_risks.db import get_session
from eu_ai_risks.llm import complete_json

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
        raise FileNotFoundError(
            f"Requirements document not found: {document_path}")

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

    document = Document(str(document_path))

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

        requirement_text = _strip_requirement_prefix(text)
        triples = _split_requirement(requirement_text)

        requirements.append(Requirement(
            id=requirement_id,
            text=requirement_text,
            source=str(document_path),
            section=current_section,
            title=current_title,
            page=block.get("page"),
            triples=triples
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
- Respond with a JSON array of triple objects, nothing else

/no_think"""


def _split_requirement(requirement_text: str) -> list[dict]:
    result = complete_json(
        prompt=f'Extract triples from: "{requirement_text}"',
        system=_TRIPLE_EXTRACTION_SYSTEM,
    )
    if isinstance(result, dict):
        for value in result.values():
            if isinstance(value, list):
                result = value
                break
    if not isinstance(result, list):
        result = [result] if isinstance(result, dict) else []
    return [t for t in result if isinstance(t, dict) and "subject" in t]


def write_triples(document_path: Path):
    requirements = load_requirements(document_path)

    # Collect all triples from all requirements into a flat list
    all_triples = []
    for req in requirements:
        for triple in req.triples:
            all_triples.append({
                "subject":   triple["subject"],
                "predicate": triple["predicate"],
                "object":    triple["object"],
                "req_id":    req.id,
                "req_text":  req.text,
            })

    if not all_triples:
        print("No triples to write.")
        return

    # Write in batches of 500
    batch_size = 500
    for i in range(0, len(all_triples), batch_size):
        batch = all_triples[i:i + batch_size]

        with get_session() as session:
            session.run("""
                UNWIND $rows AS row

                // Merge subject node
                MERGE (s:Entity {name: row.subject})

                // Merge object node
                MERGE (o:Entity {name: row.object})

                // Merge the relationship between them
                MERGE (s)-[r:RELATION {type: row.predicate}]->(o)

                // Merge the requirement node
                MERGE (req:Requirement {id: row.req_id})
                SET req.text = row.req_text

                // Link requirement to its subject entity
                MERGE (req)-[:EXTRACTED_FROM]->(s)
                """,
                        rows=batch
                        )

            print(f"  Wrote {i + len(batch)}/{len(all_triples)} triples")

            generate_and_write_triple_embeddings(session, batch)


def generate_and_write_triple_embeddings(session, all_triples: list[dict]) -> None:
    # Collect unique entities to embed
    # Use dict to deduplicate by name/id
    entities = {}

    for triple in all_triples:
        # Entity nodes - embed the entity name as text
        for key in ("subject", "object"):
            name = triple[key]
            if name not in entities:
                entities[name] = name  # text to embed is just the entity name

    # Embed and write Entity nodes
    if entities:
        entity_ids = list(entities.keys())
        entity_texts = list(entities.values())

        print(
            f"  Generating embeddings for {len(entity_texts)} Entity nodes...")
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

    # Create vector indexes
    for label in ("Entity",):
        session.run(f"""
            CREATE VECTOR INDEX {label.lower()}_embedding IF NOT EXISTS
            FOR (n:{label}) ON (n.embedding)
            OPTIONS {{indexConfig: {{
                `vector.dimensions`: {EMBEDDING_DIMENSIONS},
                `vector.similarity_function`: 'cosine'
            }}}}
            """
                    )
        print(f"  Created vector index for {label}.")


if __name__ == "__main__":
    doc = Path("./examples/sample-srs.md")

    write_triples(doc)

"""
Load and parse requirement documents (PDF, docx, etc.) into structured data.
"""

import re
from pathlib import Path

import pdfplumber
import json

from eu_ai_risks.requirements.models import Requirement
from eu_ai_risks.embeddings import embed_batch, embed_text, cosine_similarity
from eu_ai_risks.embeddings.client import EMBEDDING_DIMENSIONS
from eu_ai_risks.db import get_session
from eu_ai_risks.llm import complete_json

RE_REQUIREMENT_ID = re.compile(
    r'\b((?:CH3-FR|CH3-NFR|FR|NFR|REQ|R|UC|SR|SYS|SRS)[-_ ]?\d+(?:\.\d+)*)\b',
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
    document_path: Path, *, with_triples: bool = True,
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

    if extension == ".json":
        return _requirements_from_json(document_path)
    if extension == ".pdf":
        blocks = _read_pdf_blocks(document_path)
    elif extension == ".docx":
        blocks = _read_docx_blocks(document_path)
    else:
        blocks = _read_text_blocks(document_path)

    return _extract_requirements(blocks, document_path, with_triples=with_triples)


def parse_requirements(document_path: Path) -> list[Requirement]:
    """Load requirements without LLM triple extraction."""
    return load_requirements(document_path, with_triples=False)


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
    blocks: list[dict], document_path: Path, *, with_triples: bool = True,
) -> list[Requirement]:
    requirements = []
    current_section = None
    current_title = None
    next_id = 1

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
        triples = _open_information_extraction_triple(requirement_text) if with_triples else []

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


def _requirements_from_json(document_path: Path) -> list[Requirement]:
    data = json.loads(document_path.read_text(encoding="utf-8"))
    if isinstance(data, dict):
        for key in ("requirements", "items", "data"):
            if isinstance(data.get(key), list):
                data = data[key]
                break
    if not isinstance(data, list):
        raise ValueError(
            "JSON requirements file must contain a list of requirement objects.")

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
            requirements.append(Requirement(
                id=requirement_id, text=text, source=str(document_path)))
    return _deduplicate_requirements(requirements)


def _normalise_text(text: str) -> str:
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


_TRIPLE_EXTRACTION_SYSTEM = """
    You are a requirements analysis assistant. Extract semantic triples from
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
"""

_OPEN_INFORMATION_EXTRACTION_SYSTEM = """
    Given a piece of text, extract relational triplets in
    the form of [Subject, Relation, Object] from it. Respond with a JSON array of triple objects, nothing else.
    
    Here are some examples:
    Text: The 17068.8 millimeter long ALCO RS-3 has a diesel-electric transmission.
    Triplets: [['ALCO RS-3', 'powerType', 'Dieselelectric transmission'], ['ALCO RS-3', 'length', '17068.8 (millimetres)']] 
"""

_SCHEMA_DEFINITON_SYSTEM = """
    Given a piece of text and a list of relational triplets
    extracted from it, write a definition for each relation present. Respond with a JSON dictionary with key 
    as the relationship and value as the definition, nothing else.
    Example 1:
    Text: The 17068.8 millimeter long ALCO RS-3 has a diesel-electric transmission.
    Triplets: [['ALCO RS-3', 'powerType', 'Dieselelectric transmission'], ['ALCO RS-3', 'length', '17068.8 (millimetres)']]
    Definitions:
    powerType: The subject entity uses the type ofpower or energy source specified by the object entity.
"""

_CANONICALISATION_SYSTEM = """
    Given a piece of text, a relational triplet extracted from it, and the definition of the relation in it,
    choose the most appropriate relation to replace it in this context if there is any. Respond with a JSON 
    dictionary with the key as the relationship and value as the definition. If none of the relations are 
    suitable or if the choices are empty, return the original relation and definition. 
"""

def _split_requirement(requirement_text: str) -> list[dict]:
    try:
        result = complete_json(
            prompt=f'Extract triples from: "{requirement_text}"',
            system=_TRIPLE_EXTRACTION_SYSTEM,
        )
    except ValueError:
        return []
    if isinstance(result, dict):
        for value in result.values():
            if isinstance(value, list):
                result = value
                break
    if not isinstance(result, list):
        result = [result] if isinstance(result, dict) else []
    return [triple for triple in result if isinstance(triple, dict) and "subject" in triple]


def _open_information_extraction_triple(requirement_text: str) -> list[list[str]]:
    try:
        result = complete_json(
            prompt = f"Now please extract triplets from the following text: {requirement_text}",
            system = _OPEN_INFORMATION_EXTRACTION_SYSTEM
        )
        print(result)
    except ValueError:
        return []
    if isinstance(result, dict):
        for value in result.values():
            if isinstance(value, list):
                result = value
                break
    if not isinstance(result, list):
        result = [result] if isinstance(result, dict) else []
    return result

    
def _schema_definition(requirement_text: str, triples: list[list[str]]):
    try:
        result = complete_json(
            prompt = f"Now write a definition for each relation present in the triplets extracted from the following text: Text: {requirement_text} Triplets: {triples}",
            system = _SCHEMA_DEFINITON_SYSTEM
        )
        print(result)
    except ValueError:  
        return {}
    if isinstance(result, list):
        for value in result:
            if isinstance(value, dict):
                result = value
                break
    return result


def _canonicalisation(requirement_text: str, triple: list[str], relation_def: str, relations: dict) -> dict:
    relation_embed = embed_text(relation_def)
    relation_choices = []

    for key in relations:
        embed = relations[key][1]

        if cosine_similarity(relation_embed, embed) > 0.95:
            relation_choices.append({key: relations[key]})

    print(relation_choices)

    try:
        result = complete_json(
            prompt = f"Text: {requirement_text} Triplet: {triple} Definition of {triple[1]}: {relation_def} Choices: {relation_choices}",
            system = _CANONICALISATION_SYSTEM
        )
        print(result)
    except ValueError:
        return {}
    if isinstance(result, list):
        for value in result:
            if isinstance(value, dict):
                result = value
                break

    for key in result:
        if key not in relations:
            new_embed = embed_text(result[key])
            relations[key] = [result[key],new_embed]

    return result


def write_triples(document_path: Path, save_json: bool = False):
    requirements = load_requirements(document_path)
    relation_definitions = {}
    all_triples = []
    
    for requirement in requirements:
        req_text = requirement.text
        triples = requirement.triples
        schema_definiton = _schema_definition(req_text, triples)

        for triple in triples:
            canonicalisation = _canonicalisation(req_text, triple, schema_definiton[triple[1]], relation_definitions)

            relation, _ = canonicalisation.popitem()

            triple[1] = relation

            all_triples.append({
                "subject":        triple[0],
                "predicate":      triple[1],
                "object":         triple[2],
                "requirement_id":   requirement.id,
                "requirement_text": requirement.text,
            })

    if not all_triples:
        print("No triples to write.")
        return

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
                MERGE (req:Requirement {id: row.requirement_id})
                SET req.text = row.requirement_text

                // Link requirement to its subject entity
                MERGE (req)-[:EXTRACTED_FROM]->(s)
                """,
                        rows=batch
                        )

            print(f"  Wrote {i + len(batch)}/{len(all_triples)} triples")

            _generate_and_write_triple_embeddings(session, batch)

    if save_json:
        _save_to_json(document_path, requirements)

def _generate_and_write_triple_embeddings(session, all_triples: list[dict]) -> None:
    entities = {}
    for triple in all_triples:
        for key in ("subject", "object"):
            name = triple[key]
            if name not in entities:
                entities[name] = name
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


def reset_requirements(session, batch_size: int = 5000) -> None:
    # delete Requirement nodes and EXTRACTED_FROM relationships
    deleted_requirements = 0
    while True:
        result = session.run(
            """
            MATCH (r:Requirement)
            WITH r LIMIT $batch_size
            DETACH DELETE r
            RETURN count(r) AS deleted
            """,
            batch_size=batch_size,
        )
        deleted = result.single()["deleted"]
        deleted_requirements += deleted
        if deleted < batch_size:
            break
    print(f"  Deleted {deleted_requirements} Requirement nodes.")

    # delete Entity nodes and RELATION relationships
    deleted_entities = 0
    while True:
        result = session.run(
            """
            MATCH (e:Entity)
            WITH e LIMIT $batch_size
            DETACH DELETE e
            RETURN count(e) AS deleted
            """,
            batch_size=batch_size,
        )
        deleted = result.single()["deleted"]
        deleted_entities += deleted
        if deleted < batch_size:
            break
        
    print(f"  Deleted {deleted_entities} Entity nodes.")

    print("Requirements, entities, and relations cleared.")


def _save_to_json(doc_path: Path, requirements: list[Requirement]):
    out_path = doc_path.with_name(f"{doc_path.stem}_req.json")
    out_path.write_text(json.dumps([req.__dict__ for req in requirements], indent=4))
    print(f"  Wrote {len(requirements)} to {out_path}")


if __name__ == "__main__":
    # doc = Path("./examples/sample-srs.md")

    # write_triples(doc)
    
    pass

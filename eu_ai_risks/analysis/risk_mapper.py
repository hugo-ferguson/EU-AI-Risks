from eu_ai_risks.db import get_session
from eu_ai_risks.embeddings import embed_batch

# Define all requirements and their text for embedding
REQUIREMENTS = [
    {
        "var": "r1",
        "title": "User Registration",
        "description": "Allow new users to create an account.",
    },
    {
        "var": "r2",
        "title": "User Login",
        "description": "Authenticate returning users.",
    },
    {
        "var": "r3",
        "title": "Story Project Creation",
        "description": "Enable users to create new writing projects.",
    },
    {
        "var": "r4",
        "title": "Generative-AI Name Generator",
        "description": "Generate names for characters, places, or objects.",
    },
    {
        "var": "r5",
        "title": "Generative-AI Storyline Idea Generator",
        "description": "Provide creative prompts and plot ideas.",
    },
]

PROCESSES = [
    {"title": "User Registration", "name": "Account Setup",           "details": "Validate email format, hash password, store user profile"},
    {"title": "User Login",        "name": "Credential Verification", "details": "Verify credentials against stored records"},
    {"title": "Story Project Creation", "name": "Metadata Storage",   "details": "Store project metadata"},
    {"title": "Generative-AI Name Generator", "name": "LLM Name Generation", "details": "Generative-AI model produces names"},
    {"title": "Generative-AI Storyline Idea Generator", "name": "LLM Plot Generation", "details": "Generative-AI model creates storyline concepts"},
]


def build_query_with_embeddings() -> str:
    """Generate embeddings and inject them directly into the Cypher query."""

    # Build and embed all texts in one batch
    req_texts  = [f"Requirement: {r['title']}. Description: {r['description']}" for r in REQUIREMENTS]
    proc_texts = [f"Process: {p['name']}. Details: {p['details']}" for p in PROCESSES]

    all_texts       = req_texts + proc_texts
    all_embeddings  = embed_batch(all_texts)

    req_embeddings  = all_embeddings[:len(REQUIREMENTS)]
    proc_embeddings = all_embeddings[len(REQUIREMENTS):]

    # Attach embeddings to their respective dicts
    for req, emb in zip(REQUIREMENTS, req_embeddings):
        req["embedding"] = emb
    for proc, emb in zip(PROCESSES, proc_embeddings):
        proc["embedding"] = emb

    # Build the Cypher query with embeddings inline
    query = ""

    query += "// ===== Requirements =====\n"
    for r in REQUIREMENTS:
        query += f"""
MERGE (r:RequirementTest {{title: "{r['title']}"}})
SET r.description = "{r['description']}",
    r.embedding = {r['embedding']};
"""

    query += "\n// ===== Processes =====\n"
    for p in PROCESSES:
        query += f"""
MERGE (p:Process {{name: "{p['name']}"}})
SET p.details = "{p['details']}",
    p.embedding = {p['embedding']};
"""

    query += """
// ===== Relationships =====
MERGE (in1:Data {name: "Registration Credentials",  details: "Email, password, display name"})
MERGE (out1:Data {name: "Registration Confirmation", details: "Confirmation of successful registration"})
MERGE (err1:Action {name: "Registration Fallback",  details: "Notify user if email already exists or validation fails"})
MERGE (r1:RequirementTest {title: "User Registration"})
MERGE (proc1:Process {name: "Account Setup"})
MERGE (r1)-[:ACCEPTS_INPUT]->(in1)
MERGE (r1)-[:PERFORMS_PROCESS]->(proc1)
MERGE (r1)-[:PRODUCES_OUTPUT]->(out1)
MERGE (r1)-[:TRIGGERS_ERROR_HANDLING]->(err1);

MERGE (in2:Data {name: "Login Credentials",  details: "Email, password"})
MERGE (out2:Data {name: "Workspace Access",  details: "Access to user dashboard"})
MERGE (err2:Action {name: "Auth Warning",    details: "Display incorrect credentials message"})
MERGE (r2:RequirementTest {title: "User Login"})
MERGE (proc2:Process {name: "Credential Verification"})
MERGE (r2)-[:ACCEPTS_INPUT]->(in2)
MERGE (r2)-[:PERFORMS_PROCESS]->(proc2)
MERGE (r2)-[:PRODUCES_OUTPUT]->(out2)
MERGE (r2)-[:TRIGGERS_ERROR_HANDLING]->(err2);

MERGE (in3:Data {name: "Project Metadata Input", details: "Project title, optional description"})
MERGE (out3:Data {name: "Project Node",          details: "New project added to user workspace"})
MERGE (err3:Action {name: "Creation Alert",      details: "Notify user if project cannot be created"})
MERGE (r3:RequirementTest {title: "Story Project Creation"})
MERGE (proc3:Process {name: "Metadata Storage"})
MERGE (r3)-[:ACCEPTS_INPUT]->(in3)
MERGE (r3)-[:PERFORMS_PROCESS]->(proc3)
MERGE (r3)-[:PRODUCES_OUTPUT]->(out3)
MERGE (r3)-[:TRIGGERS_ERROR_HANDLING]->(err3);

MERGE (in4:Data {name: "Naming Parameters", details: "Category (person/place/object), optional style tags"})
MERGE (out4:Data {name: "Name Lists",       details: "List of suggested names"})
MERGE (err4:Action {name: "Static Fallback Names", details: "Provide fallback generic names if AI fails"})
MERGE (r4:RequirementTest {title: "Generative-AI Name Generator"})
MERGE (proc4:Process {name: "LLM Name Generation"})
MERGE (r4)-[:ACCEPTS_INPUT]->(in4)
MERGE (r4)-[:PERFORMS_PROCESS]->(proc4)
MERGE (r4)-[:PRODUCES_OUTPUT]->(out4)
MERGE (r4)-[:TRIGGERS_ERROR_HANDLING]->(err4);

MERGE (in5:Data {name: "Creative Constraints", details: "Genre, tone, optional keywords"})
MERGE (out5:Data {name: "Storyline Array",     details: "3-10 storyline ideas"})
MERGE (err5:Action {name: "Generation Failure UI", details: "Display message if generation fails"})
MERGE (r5:RequirementTest {title: "Generative-AI Storyline Idea Generator"})
MERGE (proc5:Process {name: "LLM Plot Generation"})
MERGE (r5)-[:ACCEPTS_INPUT]->(in5)
MERGE (r5)-[:PERFORMS_PROCESS]->(proc5)
MERGE (r5)-[:PRODUCES_OUTPUT]->(out5)
MERGE (r5)-[:TRIGGERS_ERROR_HANDLING]->(err5);
"""
    return query


def create_nodes_test():
    query = build_query_with_embeddings()
    statements = [s.strip() for s in query.split(";") if s.strip()]
    with get_session() as session:
        def create_test(tx):
            for statement in statements:
                tx.run(statement)
        session.execute_write(create_test)

def create_affected_by_relationships(top_k: int = 10) -> int:
    """Create affected by relationships from RequirementTest and Process nodes to similar Paragraph nodes."""
    total = 0
    total += _create_relationships_for_label(
        label="RequirementTest",
        match_key="title",
        top_k=top_k,
    )
    total += _create_relationships_for_label(
        label="Process",
        match_key="name",
        top_k=top_k,
    )
    return total


def _create_relationships_for_label(label: str, match_key: str, top_k: int) -> int:
    """Generic helper to create affected_by relationships for any node type."""
    with get_session() as session:
        result = session.run(
            f"""
            MATCH (r:{label})
            WHERE r.embedding IS NOT NULL
            WITH r
            MATCH (node)
            SEARCH node IN (
                VECTOR INDEX paragraph_embedding
                FOR r.embedding
                LIMIT $top_k
            ) SCORE AS score
            WHERE score > 0.799
            RETURN r.{match_key} AS identifier, node.id AS paragraph_id, score
            """,
            top_k=top_k,
        )

        rows = sanitize_affected_by_rows([
            {"identifier": record.get("identifier"), "paragraph_id": record.get("paragraph_id")}
            for record in result
        ])

        if not rows:
            return 0

        session.run(
            f"""
            UNWIND $rows AS row
            MATCH (r:{label} {{{match_key}: row.identifier}})
            MATCH (p:Paragraph {{id: row.paragraph_id}})
            MERGE (r)-[:`AFFECTED_TEST`]->(p)
            """,
            rows=rows,
        )

        return len(rows)


def sanitize_affected_by_rows(records: list[dict[str, str | None]]) -> list[dict[str, str]]:
    """Filter and deduplicate node-to-paragraph rows."""
    rows = []
    seen = set()

    for record in records:
        identifier = str(record.get("identifier") or "").strip()
        paragraph_id = str(record.get("paragraph_id") or "").strip()
        if not identifier or not paragraph_id:
            continue

        key = (identifier, paragraph_id)
        if key in seen:
            continue

        seen.add(key)
        rows.append({"identifier": identifier, "paragraph_id": paragraph_id})

    return rows

def create_requirement_embedding_index_test() -> None:
	"""Create the Requirement vector index if it does not already exist."""
	with get_session() as session:
		session.run(
			f"""
			CREATE VECTOR INDEX requirement_embedding IF NOT EXISTS
			FOR (n:RequirementTest) ON (n.embedding)
			OPTIONS {{indexConfig: {{
				`vector.dimensions`: {768},
				`vector.similarity_function`: 'cosine'
			}}}}
			""",
		)

def create_process_embedding_index_test() -> None:
	"""Create the Requirement vector index if it does not already exist."""
	with get_session() as session:
		session.run(
			f"""
			CREATE VECTOR INDEX requirement_embedding IF NOT EXISTS
			FOR (n:Process) ON (n.embedding)
			OPTIONS {{indexConfig: {{
				`vector.dimensions`: {768},
				`vector.similarity_function`: 'cosine'
			}}}}
			""",
		)

if __name__ == "__main__":
    # Step 1 - Create nodes with embeddings already injected
    print("Creating nodes...")
    create_nodes_test()
    print("Nodes created.")

    # Step 2 - Create vector indexes for similarity search
    print("Creating vector indexes...")
    create_requirement_embedding_index_test()
    create_process_embedding_index_test()
    print("Indexes created.")

    # Step 3 - Link nodes to relevant paragraphs via similarity
    print("Creating affected_by relationships...")
    total = create_affected_by_relationships(top_k=10)
    print(f"Created {total} affected_by relationships.")
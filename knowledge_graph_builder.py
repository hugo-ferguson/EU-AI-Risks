import re
from neo4j import GraphDatabase
import PyPDF2

# Connection details for Neo4j Aura
URI = "neo4j+s://065e0bc1.databases.neo4j.io"
AUTH = ("065e0bc1", "65r_h9wvgNKtrUYRDlONVT4s3283PbxcEH2v7fLTwqM")

def extract_text_from_pdf(file_path):
    text = ""
    with open(file_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        # Iterate through all pages in the document [cite: 1, 25, 51, 77, 104, 131, 157, 183, 209, 236]
        for page in reader.pages:
            text += page.extract_text()
    return text

def parse_requirements(text):
    # Regex to capture each requirement block
    req_blocks = re.split(r'Requirement \d+', text)[1:]
    requirements = []
    
    for block in req_blocks:
        req = {
            "title": re.search(r"Title:\s*(.*)", block).group(1).strip(),
            "description": re.search(r"Description:\s*(.*)", block).group(1).strip(),
            "input": re.search(r"Input:\s*(.*)", block).group(1).strip(),
            "processing": re.search(r"Processing:\s*(.*)", block).group(1).strip()
        }
        requirements.append(req)
    return requirements

def create_graph(tx, req):
    # 1. Create Requirement Node
    query = """

    MERGE (r:Requirement {title: $title})
    SET r.description = $desc, r.processing = $proc, r.input = $input
    
    // 2. Link to Target Audience
    WITH r
    UNWIND (
        CASE 
        WHEN toLower($desc) CONTAINS 'super-admin' THEN ['User', 'Admin', 'Super-Admin']
        WHEN toLower($desc) CONTAINS 'admin' THEN ['User', 'Admin']
        ELSE ['User']
        END
    ) AS role
    MERGE (a:Audience {name: role})
    MERGE (r)-[:TARGETS]->(a)

    // 3. Link to Keywords (Extracting from title/input)
    WITH r
    UNWIND split(toLower($title), ' ') AS word
    WITH r, word
    WHERE word CONTAINS 'ai'
    MERGE (k:Keyword {name: word})
    MERGE (r)-[:HAS_KEYWORD]->(k)
    
    """
    tx.run(query, title=req['title'], desc=req['description'], 
           proc=req['processing'], input=req['input'])

# Execution
if __name__ == "__main__":
    file_name = "the_story_web_requirements_document.pdf"
    raw_text = extract_text_from_pdf(file_name)
    with GraphDatabase.driver(URI, auth=AUTH) as driver:
        with driver.session() as session:
            parsed_data = parse_requirements(raw_text)
                # Now pass 'parsed_data' to your Neo4j session functions
            print(f"Successfully parsed {len(parsed_data)} requirements.")
            print(parsed_data)
            for r in parsed_data:
                session.execute_write(create_graph, r)
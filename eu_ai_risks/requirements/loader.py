"""
Load and parse requirement documents (PDF, docx, etc.) into structured data.
"""

from ollama import generate
import pymupdf as pymu
from pathlib import Path
import chonkie as ch
import json

EXTRACT_TRIPLETS_PROMPT = """
    You are a knowledge graph extraction engine. Your sole task is to extract all RDF triplets from the given text.

    ## Output Format
    Return ONLY a valid JSON object. No preamble, no explanation, no markdown backticks.

    {{
        "triplets": [
            {{
                "subject": "entity that the statement is about",
                "predicate": "relationship or property linking subject to object",
                "object": "entity or value the predicate points to"
            }}
        ]
    }}

    ## Extraction Rules
    1. Extract EVERY meaningful relationship present in the text — do not skip any.
    2. Subjects and objects must be named entities, noun phrases, or concrete values (not pronouns).
    3. Predicates must be concise and descriptive (e.g. "founded_by", "located_in", "is_a").
    4. Use snake_case for predicates.
    5. If the object is a literal value (date, number, string), include it as-is.
    6. Do not infer or hallucinate relationships that are not explicitly stated in the text.
    7. If no triplets can be extracted, return: {{"triplets": []}}

    ## Example
    Input: "Apple was founded by Steve Jobs in 1976 and is headquartered in Cupertino."
    Output:
    {{
        "triplets": [
            {{"subject": "Apple", "predicate": "founded_by", "object": "Steve Jobs"}},
            {{"subject": "Apple", "predicate": "founded_in", "object": "1976"}},
            {{"subject": "Apple", "predicate": "headquartered_in", "object": "Cupertino"}}
        ]
    }}

    ## Text to Process
    {chunk}
"""

def main(pdf):
    pdf_text = read_pdf(pdf)

    # Chunk PDF text using chonkie SemanticChunker
    chunker = ch.SemanticChunker(
        embedding_model="minishlab/potion-base-32M",
        threshold=0.8,
        similarity_window=3,
        chunk_size=4096,
    )

    chunks = chunker.chunk(pdf_text)

    triplets = []

    count = 1
    for chunk in chunks:
        print(f"Currently processing chunk {count}/{len(chunks)}")
        response = analyse_chunk(chunk.text)
        count += 1

        triplets + parse_triplets(response)
    
    return triplets


def analyse_chunk(textChunk):
    response = generate(
        model="qwen3",
        prompt=EXTRACT_TRIPLETS_PROMPT.format(chunk=textChunk),
        think=False,
        stream=False
    )

    return response.response

def read_pdf(pdf):
    # Parse PDF with pymupdf
    print("Currently parsing: " + str(pdf))
    document = pymu.open(pdf)
    
    text = ""
    for pg in document:
        text += pg.get_text("text",delimiters="\n\r")
    
    return ' '.join(text.split())

def parse_triplets(llm_response: str) -> list[dict]:
    try:
        clean = llm_response.strip().replace("```json", "").replace("```", "")
        data = json.loads(clean)
        return data.get("triplets", [])
    except json.JSONDecodeError as e:
        print(f"Failed to parse response: {e}")
        return []

if __name__ == "__main__":
    path = Path("./sample_SRS.pdf")

    main(path)
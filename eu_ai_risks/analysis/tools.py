"""
Tool definitions and dispatch for the graph-reading agent.
"""

import json

from eu_ai_risks.db.graph import (
    list_categories,
    get_category_articles,
    get_article,
    find_paragraphs,
    text_search,
    get_references,
    list_requirements,
    get_requirement,
    get_related_requirements,
    search_entities,
)
from eu_ai_risks.embeddings import embed_text


TOOL_DEFINITIONS = [
    {
        "type": "function",
        "function": {
            "name": "list_categories",
            "description": "List the 14 requirement categories with their anchor article IDs.",
            "parameters": {"type": "object", "properties": {}, "required": []},
        },
    },
    {
        "type": "function",
        "function": {
            "name": "get_category_articles",
            "description": "Get anchor article text and binding paragraphs for a category.",
            "parameters": {
                "type": "object",
                "properties": {
                    "category_key": {
                        "type": "string",
                        "description": "e.g. 'human_oversight', 'data_governance'.",
                    },
                    "include_all_types": {
                        "type": "boolean",
                        "description": "Include non-binding paragraphs too. Default false.",
                    },
                },
                "required": ["category_key"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "search",
            "description": "Semantic search over EU AI Act paragraphs. Use regulatory vocabulary.",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "Search query in regulatory language.",
                    },
                    "top_k": {
                        "type": "integer",
                        "description": "Number of results (default 8, max 15).",
                    },
                },
                "required": ["query"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "text_search",
            "description": "Exact keyword search in paragraph text.",
            "parameters": {
                "type": "object",
                "properties": {
                    "keyword": {
                        "type": "string",
                        "description": "Keyword or phrase to find.",
                    },
                    "obligation_types": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "Filter: requirement, prohibition, permission, definition, scope, informational.",
                    },
                },
                "required": ["keyword"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "read_article",
            "description": "Full article text with paragraphs, chapter context, and dimension tags.",
            "parameters": {
                "type": "object",
                "properties": {
                    "article_id": {
                        "type": "string",
                        "description": "e.g. 'art:9'.",
                    },
                },
                "required": ["article_id"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "get_references",
            "description": "Outgoing and incoming cross-references for an article.",
            "parameters": {
                "type": "object",
                "properties": {
                    "article_id": {
                        "type": "string",
                        "description": "e.g. 'art:9'.",
                    },
                },
                "required": ["article_id"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "list_requirements",
            "description": "List all software requirements loaded into the graph.",
            "parameters": {"type": "object", "properties": {}, "required": []},
        },
    },
    {
        "type": "function",
        "function": {
            "name": "get_requirement",
            "description": "Read a requirement with its semantic triples.",
            "parameters": {
                "type": "object",
                "properties": {
                    "requirement_id": {
                        "type": "string",
                        "description": "e.g. 'FR-1'.",
                    },
                },
                "required": ["requirement_id"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "get_related_requirements",
            "description": "Find requirements sharing entities with the given one.",
            "parameters": {
                "type": "object",
                "properties": {
                    "requirement_id": {
                        "type": "string",
                        "description": "e.g. 'FR-1'.",
                    },
                },
                "required": ["requirement_id"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "search_requirement_entities",
            "description": "Semantic search over entities from the requirements graph.",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "Search query for entity names.",
                    },
                    "top_k": {
                        "type": "integer",
                        "description": "Number of results (default 8, max 15).",
                    },
                },
                "required": ["query"],
            },
        },
    },
]


_DISPATCH = {
    "list_categories": lambda args: list_categories(),
    "get_category_articles": lambda args: get_category_articles(
        args["category_key"],
        obligation_types=[] if args.get("include_all_types") else None,
    ),
    "search": lambda args: find_paragraphs(
        embed_text(args["query"]),
        top_k=min(args.get("top_k", 8), 15),
    ),
    "text_search": lambda args: text_search(
        args["keyword"],
        obligation_types=args.get("obligation_types"),
        limit=10,
    ),
    "read_article": lambda args: get_article(args["article_id"]),
    "get_references": lambda args: get_references(args["article_id"]),
    "list_requirements": lambda args: list_requirements(),
    "get_requirement": lambda args: get_requirement(
        args["requirement_id"],
    ),
    "get_related_requirements": lambda args: get_related_requirements(
        args["requirement_id"],
    ),
    "search_requirement_entities": lambda args: search_entities(
        embed_text(args["query"]),
        top_k=min(args.get("top_k", 8), 15),
    ),
}


def execute_tool(tool_name: str, arguments: dict) -> str:
    handler = _DISPATCH.get(tool_name)
    if not handler:
        return json.dumps({"error": f"Unknown tool: {tool_name}"})

    try:
        result = handler(arguments)
        return json.dumps(result, default=str, ensure_ascii=False)
    except Exception as exc:
        return json.dumps({"error": str(exc)})

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
)
from eu_ai_risks.embeddings import embed_text


TOOL_DEFINITIONS = [
    {
        "type": "function",
        "function": {
            "name": "list_categories",
            "description": (
                "List all 14 requirement categories from the EU AI Act "
                "(e.g. risk_management, human_oversight, data_governance) "
                "with their names and anchor article IDs."
            ),
            "parameters": {
                "type": "object",
                "properties": {},
                "required": [],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "get_category_articles",
            "description": (
                "Get the anchor article text and binding paragraphs for a "
                "requirement category. Use after identifying which category "
                "is relevant."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "category_key": {
                        "type": "string",
                        "description": (
                            "One of the 14 category keys, e.g. "
                            "'human_oversight', 'risk_management'."
                        ),
                    },
                    "include_all_types": {
                        "type": "boolean",
                        "description": (
                            "If true, include all paragraph types, not "
                            "just binding requirements. Default false."
                        ),
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
            "description": (
                "Semantic search over EU AI Act paragraphs. Returns "
                "paragraphs ranked by relevance with full text and article "
                "context. Use EU AI Act vocabulary for best results "
                "(e.g. 'human oversight measures' not 'a person reviews "
                "the output')."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": (
                            "Search query. Use regulatory vocabulary."
                        ),
                    },
                    "top_k": {
                        "type": "integer",
                        "description": (
                            "Number of results (default 8, max 15)."
                        ),
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
            "description": (
                "Search for an exact keyword or phrase in paragraph text. "
                "More precise than semantic search for known regulatory "
                "terms (e.g. 'conformity assessment', 'high-risk AI system')."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "keyword": {
                        "type": "string",
                        "description": "The keyword or phrase to find.",
                    },
                    "obligation_types": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": (
                            "Filter by type: requirement, prohibition, "
                            "permission, definition, scope, informational."
                        ),
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
            "description": (
                "Read the full text of a specific article with all its "
                "paragraphs, chapter context, and dimension tags "
                "(responsible parties, risk category, data categories)."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "article_id": {
                        "type": "string",
                        "description": "The article ID, e.g. 'art:9'.",
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
            "description": (
                "Get articles that a given article cites and articles that "
                "cite it. Use to follow the cross-reference network."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "article_id": {
                        "type": "string",
                        "description": "The article ID, e.g. 'art:9'.",
                    },
                },
                "required": ["article_id"],
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
}


def execute_tool(tool_name: str, arguments: dict) -> str:
    """
    Execute a tool call and return the result as a JSON string.

    :param tool_name: the function name from the tool call.
    :param arguments: the parsed arguments dict.
    :return: JSON string of the result.
    """
    handler = _DISPATCH.get(tool_name)
    if not handler:
        return json.dumps({"error": f"Unknown tool: {tool_name}"})

    try:
        result = handler(arguments)
        return json.dumps(result, default=str, ensure_ascii=False)
    except Exception as e:
        return json.dumps({"error": str(e)})

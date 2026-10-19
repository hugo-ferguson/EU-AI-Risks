"""
Write a blinded spreadsheet of every risk for manual judging, and a separate
key that maps each row back to the setup that produced it.

Judge each row in judging.csv by filling in:
  correct    y/n  the gap the risk describes really exists in the requirement
  supported  y/n  the cited provision imposes the obligation the risk says is missing
"""

import argparse
import csv
import json
import random
import re
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

from eu_ai_risks.db.graph import get_article, get_provisions  # noqa: E402

SHEET_FIELDS = ["row_id", "requirement_id", "requirement", "risk", "cited",
                "provision_exists", "provision_text", "correct", "supported", "notes"]
KEY_FIELDS = ["row_id", "setup", "run", "requirement_id", "risk_index", "provision_id",
              "paragraph_id", "granularity", "exists", "quote_match", "quote_match_loose",
              "supplied", "trace"]

RE_POINT = re.compile(r"^(?:art:\d+:p\d+:[a-z]|annex:[IVX]+:\d+:[a-z])$")
RE_PARAGRAPH = re.compile(r"^(?:art:\d+:p\d+|annex:[IVX]+:\d+)$")


def _paragraph_of(node_id: str) -> str:
    return ":".join(node_id.split(":")[:3])


def _granularity(provision_id: str, article_id: str) -> str:
    if RE_POINT.match(provision_id):
        return "point"
    if RE_PARAGRAPH.match(provision_id):
        return "paragraph"
    return "article" if article_id else "none"


def _normalise(text: str) -> str:
    # Quotes are compared ignoring case, spacing and quotation mark style
    text = text.lower().replace("’", "'").replace("“", '"').replace("”", '"')
    return re.sub(r"\s+", " ", text).strip(" .\"'")


def _quote_matches(quote: str, provision_text: str) -> bool:
    # Models mark omissions with an ellipsis, so each part must match on its own
    parts = [_normalise(part) for part in re.split(r"\.\.\.|…", quote)]
    parts = [part for part in parts if part]
    text = _normalise(provision_text)
    return bool(parts) and all(part in text for part in parts)


def load_assessments(results: Path, run: int) -> list[dict]:
    """The rows run.py saved for one run, in the order they were assessed."""
    with (results / "assessments.jsonl").open(encoding="utf-8") as file:
        return [row for row in map(json.loads, file) if row["run"] == run]


def collect_risks(rows: list[dict]) -> list[dict]:
    """
    Every risk in the rows, with its cited provision's text and the checks
    that need no judgement (whether it exists, how specific it is, whether
    its quote matches), so human and LLM judging score the same thing.
    """
    risks = [(row, index, risk) for row in rows
             for index, risk in enumerate(row["assessment"]["risks"])]
    cited = {risk["provision_id"] for _, _, risk in risks if risk["provision_id"]}
    provisions = get_provisions(sorted(cited | {_paragraph_of(node_id) for node_id in cited}))
    articles = {article_id: get_article(article_id)
                for article_id in {risk["article_id"] for _, _, risk in risks if risk["article_id"]}}

    collected = []
    for row, index, risk in risks:
        provision_id = risk["provision_id"] or ""
        granularity = _granularity(provision_id, risk["article_id"])
        article = articles.get(risk["article_id"])
        if granularity == "article":
            exists = article is not None
            provision_text = (article or {}).get("text") or ""
        # A point is judged with its paragraph, which holds the point's lead-in
        elif provision_id.startswith("art:") and _paragraph_of(provision_id) in provisions:
            exists = provision_id in provisions
            provision_text = provisions[_paragraph_of(provision_id)]["text"] if exists else ""
        else:
            exists = provision_id in provisions
            provision_text = provisions.get(provision_id, {}).get("text", "")
        collected.append({
            "setup": row["setup"],
            "run": row["run"],
            "requirement_id": row["requirement_id"],
            "requirement_text": row["requirement_text"],
            "risk_index": index,
            "risk": risk["description"],
            "cited": provision_id or risk["provision"] or risk["article_id"] or "(none)",
            "provision_id": provision_id,
            "paragraph_id": _paragraph_of(provision_id) if provision_id else risk["article_id"],
            "granularity": granularity,
            "exists": exists,
            "provision_text": provision_text,
            "quote": risk.get("quote", ""),
            "quote_match": _quote_matches(risk.get("quote", ""), provision_text),
            "quote_match_loose": _quote_matches_loose(risk.get("quote", ""), provision_text),
            "supplied": risk["citation_supplied"],
            "trace": " | ".join(risk["trace"]),
        })
    return collected


def _quote_matches_loose(quote: str, provision_text: str) -> bool:
    """Like _quote_matches, but a quote that differs only in punctuation still matches."""
    def words(text: str) -> str:
        return re.sub(r"\s+", " ", re.sub(r"[^\w\s]", " ", text.lower())).strip()
    parts = [words(part) for part in re.split(r"\.\.\.|\u2026", quote)]
    parts = [part for part in parts if part]
    text = words(provision_text)
    return bool(parts) and all(part in text for part in parts)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("results", type=Path, help="Results folder written by run.py")
    parser.add_argument("--run", type=int, default=0, help="Which run to judge")
    parser.add_argument("--seed", type=int, default=0)
    parser.add_argument("--force", action="store_true",
                        help="Overwrite an existing judging.csv, losing any judgements in it")
    parser.add_argument("--key-only", action="store_true",
                        help="Only rewrite key.csv (e.g. to add new checks), keeping judging.csv")
    args = parser.parse_args()

    sheet_path = args.results / "judging.csv"
    key_path = args.results / "key.csv"
    if sheet_path.exists() and not args.force and not args.key_only:
        raise SystemExit(f"{sheet_path} exists; pass --force to overwrite it.")

    rows = load_assessments(args.results, args.run)
    risks = collect_risks(rows)
    order = {row["requirement_id"]: position for position, row in enumerate(rows)}
    random.Random(args.seed).shuffle(risks)
    # Grouped by requirement, then by provision, so each provision is read once per requirement
    risks.sort(key=lambda risk: (order[risk["requirement_id"]], risk["provision_id"]))

    sheet, key = [], []
    for number, risk in enumerate(risks, 1):
        row_id = f"R{number:04d}"
        sheet.append({
            "row_id": row_id,
            "requirement_id": risk["requirement_id"],
            "requirement": risk["requirement_text"],
            "risk": risk["risk"],
            "cited": risk["cited"],
            "provision_exists": "y" if risk["exists"] else "n",
            "provision_text": risk["provision_text"],
            "correct": "",
            # A provision that doesn't exist can't support anything
            "supported": "" if risk["exists"] else "n",
            "notes": "",
        })
        key.append({"row_id": row_id, **{field: risk[field] for field in KEY_FIELDS[1:]}})

    if args.key_only:
        # Row ids follow from the seed and the assessments, so they must name the same risks as before
        with key_path.open(newline="", encoding="utf-8") as file:
            old = {row["row_id"]: (row["setup"], row["requirement_id"], row["risk_index"])
                   for row in csv.DictReader(file)}
        new = {row["row_id"]: (row["setup"], row["requirement_id"], str(row["risk_index"]))
               for row in key}
        if old != new:
            raise SystemExit("The rows no longer match key.csv, so judging.csv would be "
                             "misread; key.csv was not changed.")
        outputs = ((key_path, KEY_FIELDS, key),)
    else:
        outputs = ((sheet_path, SHEET_FIELDS, sheet), (key_path, KEY_FIELDS, key))
    for path, fields, data in outputs:
        with path.open("w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=fields)
            writer.writeheader()
            writer.writerows(data)
    print(f"Wrote {key_path}" if args.key_only else
          f"Wrote {len(sheet)} risks to {sheet_path} (key: {key_path})")


if __name__ == "__main__":
    main()

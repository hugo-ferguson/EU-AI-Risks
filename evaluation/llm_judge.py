"""
Score every risk in a results folder against rubric.md with an LLM judge.

The rubric and the SRS are the same for every risk, so they are sent first
and cached; each request adds only the risk and its cited provision. Scores
are written to llm_scores_<model>.jsonl for metrics.py --llm.
"""

import argparse
import json
import os
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

from dotenv import load_dotenv
from pydantic import BaseModel, Field

load_dotenv()

from eu_ai_risks.llm import complete_json_cached  # noqa: E402
from evaluation.judging import collect_risks, load_assessments  # noqa: E402

RUBRIC = (Path(__file__).parent / "rubric.md").read_text(encoding="utf-8")


class JudgeScores(BaseModel):
    """The judge's scores for one risk against rubric.md, one criterion per RQ."""
    gap_validity: int = Field(ge=0, le=10, description="RQ1: the gap really exists")
    provision_support: int = Field(ge=0, le=10, description="RQ2: the provision imposes it")
    citation_precision: int = Field(ge=0, le=10, description="RQ3: the citation leads to it")


CRITERIA = tuple(JudgeScores.model_fields)
# The response format sent to the API. Ranges are left to JudgeScores, as not
# every provider's structured outputs accept minimum and maximum
SCHEMA = {
    "type": "object",
    "properties": {criterion: {"type": "integer"} for criterion in CRITERIA},
    "required": list(CRITERIA),
    "additionalProperties": False,
}
DEFAULT_MODEL = "anthropic/claude-sonnet-5-5"
# Fields of each risk worth keeping next to its scores; the rest can be rebuilt
KEPT = ("setup", "run", "requirement_id", "risk_index", "risk", "cited", "provision_id",
        "paragraph_id", "granularity", "exists", "quote_match", "supplied", "trace")


def scores_path(results: Path, model: str) -> Path:
    return results / f"llm_scores_{model.replace('/', '_')}.jsonl"


def _key(risk: dict) -> tuple:
    return risk["setup"], risk["run"], risk["requirement_id"], risk["risk_index"]


def _srs(rows: list[dict]) -> str:
    requirements = dict.fromkeys((row["requirement_id"], row["requirement_text"]) for row in rows)
    return "## SRS\n" + "\n".join(f"- {rid}: {text}" for rid, text in requirements)


def _prompt(risk: dict) -> str:
    provision = risk["provision_text"] or (
        "The cited provision does not exist in the Act." if not risk["exists"]
        else "(The whole article is cited.)")
    return (
        f"## Requirement {risk['requirement_id']}\n{risk['requirement_text']}\n\n"
        f"## Risk\n{risk['risk']}\n\n"
        f"Cited provision: {risk['cited']}\n"
        f"Quoted words: {risk['quote'] or '(none)'}\n\n"
        f"## Text of the cited provision\n{provision}\n"
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("results", type=Path, help="Results folder written by run.py")
    parser.add_argument("--run", type=int, default=0, help="Which run to score")
    parser.add_argument("--model", default=os.environ.get("JUDGE_MODEL", DEFAULT_MODEL),
                        help=f"litellm model string (default: JUDGE_MODEL or {DEFAULT_MODEL})")
    parser.add_argument("--effort", choices=["low", "medium", "high"],
                        help="Reasoning effort, passed as litellm's reasoning_effort")
    parser.add_argument("--workers", type=int, default=4, help="Requests in parallel")
    parser.add_argument("--max-tokens", type=int, default=4000,
                        help="Includes any thinking, so a low limit can cut the answer off")
    parser.add_argument("--limit", type=int, help="Only score the first N unscored risks")
    args = parser.parse_args()

    rows = load_assessments(args.results, args.run)
    risks = collect_risks(rows)
    srs = _srs(rows)
    out = scores_path(args.results, args.model)
    done = set()
    if out.exists():
        with out.open(encoding="utf-8") as file:
            done = {_key(row) for row in map(json.loads, file)}
    todo = [risk for risk in risks if _key(risk) not in done][:args.limit]
    print(f"{len(risks)} risks, {len(done)} already scored, scoring {len(todo)} with {args.model}")

    options = {"reasoning_effort": args.effort} if args.effort else {}
    totals = {"input": 0, "output": 0, "cache_read": 0, "cache_write": 0}
    lock = threading.Lock()

    def judge(risk: dict) -> dict:
        raw, usage = complete_json_cached(
            _prompt(risk), RUBRIC, shared=srs, max_tokens=args.max_tokens,
            model=args.model, schema=SCHEMA, **options)
        # A missing, out-of-range or non-integer score fails validation, so the risk is retried
        scores = JudgeScores.model_validate(raw).model_dump()
        if not risk["exists"]:
            # Nothing that doesn't exist can support or locate an obligation
            scores["provision_support"] = scores["citation_precision"] = 0
        return {**{field: risk[field] for field in KEPT}, **scores,
                "judge_model": args.model, "usage": usage}

    failed = 0
    with ThreadPoolExecutor(max_workers=args.workers) as pool, \
            out.open("a", encoding="utf-8") as file:
        futures = {}
        if todo:
            # One request first writes the cache, so the parallel ones read it instead of each writing it
            first = pool.submit(judge, todo[0])
            futures[first] = todo[0]
            next(as_completed([first]))
        futures.update({pool.submit(judge, risk): risk for risk in todo[1:]})
        for number, future in enumerate(as_completed(futures), 1):
            risk = futures[future]
            try:
                record = future.result()
            except Exception as error:  # noqa: BLE001
                # Left unscored, so rerunning the command retries it
                failed += 1
                print(f"[{number}/{len(todo)}] {risk['setup']} {risk['requirement_id']} "
                      f"#{risk['risk_index']} failed: {error}")
                continue
            with lock:
                file.write(json.dumps(record) + "\n")
                file.flush()
                for field in totals:
                    totals[field] += record["usage"][field]
            print(f"[{number}/{len(todo)}] {risk['setup']} {risk['requirement_id']} "
                  f"#{risk['risk_index']}: " + ", ".join(f"{c}={record[c]}" for c in CRITERIA))

    print(f"\nWrote {out}" + (f" ({failed} failed; rerun to retry)" if failed else ""))
    print("Tokens: " + ", ".join(f"{field} {value:,}" for field, value in totals.items()))


if __name__ == "__main__":
    main()

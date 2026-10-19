"""
Score each setup from human judgements (judging.csv) or LLM scores
(llm_scores_<model>.jsonl), answering:

  RQ1  precision (risks judged correct) and recall against the pool of risks
       judged correct and supported across all setups; for the KG setup, which
       retrieval routes found the provisions of those risks
  RQ2  citations that exist in the Act, and risks judged supported by them
  RQ3  citations of a paragraph or point rather than a whole article, and
       quotes that match the cited provision's text
  RQ4  tokens per requirement and per risk judged correct and supported, and
       the KG setup's one-off tokens for building the requirements KG

With --llm, a score at or above --threshold counts as a yes, and if
judging.csv has human judgements, the LLM's agreement with them is reported.
"""

import argparse
import csv
import json
from collections import Counter
from pathlib import Path

SETUP_NAMES = {"kg": "KG (ours)", "llm-only": "LLM-only", "full-act": "Full-Act",
               "chunk-rag": "Chunk-RAG"}
CRITERIA = ("gap_validity", "provision_support", "citation_precision")
# The start of each trace step, as risk_assessor writes it -> route name
ROUTES = {
    "selected from the Act's index": "table of contents",
    "requirement term": "concept links",
    "referenced by": "reference expansion",
    "vector similarity to the requirement (fallback)": "vector fallback",
    "definition of": "Article 3 definition",
}


def _answer(value: str) -> bool | None:
    value = (value or "").strip().lower()
    if value in {"y", "yes", "1", "true"}:
        return True
    if value in {"n", "no", "0", "false"}:
        return False
    return None


def _read_csv(path: Path) -> list[dict]:
    with path.open(newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))


def _key(row: dict) -> tuple:
    return row["setup"], int(row["run"]), row["requirement_id"], int(row["risk_index"])


def _rate(count: int, total: int) -> float | None:
    return round(count / total, 3) if total else None


def _routes(trace: str) -> set[str]:
    return {route for step in trace.split(" | ") for prefix, route in ROUTES.items()
            if step.startswith(prefix)}


def _kappa(pairs: list[tuple[bool, bool]]) -> float | None:
    """Cohen's kappa for two judges' yes/no answers."""
    if not pairs:
        return None
    observed = sum(a == b for a, b in pairs) / len(pairs)
    yes_a = sum(a for a, _ in pairs) / len(pairs)
    yes_b = sum(b for _, b in pairs) / len(pairs)
    expected = yes_a * yes_b + (1 - yes_a) * (1 - yes_b)
    return round((observed - expected) / (1 - expected), 3) if expected < 1 else 1.0


def human_rows(results: Path) -> list[dict]:
    """key.csv joined with the judgements in judging.csv."""
    judged = {row["row_id"]: row for row in _read_csv(results / "judging.csv")}
    rows = []
    for row in _read_csv(results / "key.csv"):
        judgement = judged[row["row_id"]]
        rows.append({**row, "run": int(row["run"]), "risk_index": int(row["risk_index"]),
                     "exists": row["exists"] == "True",
                     "quote_match": row["quote_match"] == "True",
                     "correct": _answer(judgement["correct"]),
                     "supported": _answer(judgement["supported"])})
    return rows


def llm_rows(path: Path, threshold: int) -> list[dict]:
    with path.open(encoding="utf-8") as file:
        rows = [json.loads(line) for line in file if line.strip()]
    for row in rows:
        row["correct"] = row["gap_validity"] >= threshold
        row["supported"] = row["provision_support"] >= threshold
    return rows


def _tokens_in(usage: dict) -> int:
    # Cached input still has to be read by the model, so it counts towards input
    return usage["input"] + usage["cache_read"] + usage["cache_write"]


def one_off_usage(results: Path) -> dict | None:
    """Tokens the KG setup spends once per SRS: building the requirements KG and classifying the system."""
    usage = {}
    for name, path in (("load", results / "load_usage.json"),
                       ("classification", results / "system.json")):
        if path.exists() and (saved := json.loads(path.read_text(encoding="utf-8"))).get("usage"):
            usage[name] = {"input": _tokens_in(saved["usage"]), "output": saved["usage"]["output"]}
    return usage or None


def setup_metrics(rows: list[dict], assessments: list[dict]) -> tuple[dict, int]:
    def good(row: dict) -> bool:
        return bool(row["correct"] and row["supported"])

    # Recall is against every (requirement, provision) that any setup got right
    pool = {(row["requirement_id"], row["paragraph_id"]) for row in rows if good(row)}
    runs = {row["run"] for row in rows}
    metrics = {}
    # From the assessments, so a setup that raised no risks is still reported
    for setup in [s for s in SETUP_NAMES
                  if any(row["setup"] == s and row["run"] in runs for row in assessments)]:
        own = [row for row in rows if row["setup"] == setup]
        assessed = [row for row in assessments if row["setup"] == setup and row["run"] in runs]
        correct = [row for row in own if row["correct"] is not None]
        supported = [row for row in own if row["supported"] is not None]
        found = {(row["requirement_id"], row["paragraph_id"]) for row in own if good(row)}
        provisions = [len((row["retrieval"] or {}).get("provisions", {})) for row in assessed]
        # Results from before token use was recorded have no usage
        usages = [row["usage"] for row in assessed if row.get("usage")]
        tokens = sum(_tokens_in(usage) + usage["output"] for usage in usages)
        good_risks = sum(good(row) for row in own)
        values = {
            "requirements": len(assessed),
            "not_assessed": sum(row["not_assessed"] for row in assessed),
            "risks": len(own),
            "provisions_supplied_mean": _rate(sum(provisions), len(provisions)),
            "rq1_precision": _rate(sum(row["correct"] for row in correct), len(correct)),
            "rq1_recall": _rate(len(found & pool), len(pool)),
            "rq2_exists": _rate(sum(row["exists"] for row in own), len(own)),
            "rq2_supported": _rate(sum(row["supported"] for row in supported), len(supported)),
            "rq3_specific": _rate(
                sum(row["granularity"] in {"paragraph", "point"} for row in own), len(own)),
            "rq3_quote_match": _rate(sum(row["quote_match"] for row in own), len(own)),
            "rq4_input_tokens_mean": _rate(sum(map(_tokens_in, usages)), len(usages)),
            "rq4_output_tokens_mean": _rate(sum(u["output"] for u in usages), len(usages)),
            "rq4_tokens_per_good_risk": (round(tokens / good_risks) if usages and good_risks
                                         else None),
        }
        # Mean rubric scores, when an LLM judged
        for criterion in CRITERIA:
            if own and criterion in own[0]:
                values[f"mean_{criterion}"] = round(
                    sum(row[criterion] for row in own) / len(own), 2)
        metrics[setup] = values
    return metrics, len(pool)


def kg_routes(rows: list[dict]) -> dict:
    """Which routes retrieved the provisions of the KG setup's good risks."""
    good = [row for row in rows if row["setup"] == "kg" and row["correct"] and row["supported"]]
    found = Counter(route for row in good for route in _routes(row["trace"]))
    only = Counter(next(iter(routes)) for row in good if len(routes := _routes(row["trace"])) == 1)
    return {route: {"found": found[route], "only_route": only[route]} for route in ROUTES.values()}


def agreement(rows_a: list[dict], rows_b: list[dict]) -> dict:
    """Cohen's kappa between two judges on the risks both judged."""
    by_key = {_key(row): row for row in rows_b}
    result = {}
    for field in ("correct", "supported"):
        pairs = [(row[field], other[field]) for row in rows_a
                 if (other := by_key.get(_key(row))) is not None
                 and row[field] is not None and other[field] is not None]
        result[field] = {"risks": len(pairs), "kappa": _kappa(pairs),
                         "agree": _rate(sum(a == b for a, b in pairs), len(pairs))}
    return result


def _percent(value: float | None) -> str:
    return "--" if value is None else f"{round(value * 100)}\\%"


def _thousands(value: float | None) -> str:
    return "--" if value is None else f"{value / 1000:.1f}k"


def latex_table(metrics: dict, caption: str, label: str) -> str:
    """One column per setup and one row per measure, so it fits a single IEEE column."""
    groups = [
        (None, [("risks", "Risks")]),
        ("RQ1", [("rq1_precision", "Correct"), ("rq1_recall", "Recall")]),
        ("RQ2", [("rq2_exists", "Exists"), ("rq2_supported", "Supported")]),
        ("RQ3", [("rq3_specific", "Specific"), ("rq3_quote_match", "Quote")]),
        ("RQ4", [("rq4_input_tokens_mean", "Input tokens"),
                 ("rq4_output_tokens_mean", "Output tokens"),
                 ("rq4_tokens_per_good_risk", "Tokens per supported risk")]),
    ]
    setups = list(metrics)
    lines = [
        "\\begin{table}[t]", "\\centering", "\\footnotesize", "\\setlength{\\tabcolsep}{4pt}",
        f"\\caption{{{caption}}}", f"\\label{{{label}}}",
        "\\begin{tabular}{l" + "r" * len(setups) + "}", "\\hline",
        "Measure & " + " & ".join(SETUP_NAMES[setup] for setup in setups) + " \\\\", "\\hline",
    ]
    for group, rows in groups:
        if group:
            lines.append(f"\\multicolumn{{{len(setups) + 1}}}{{l}}{{\\textit{{{group}}}}} \\\\")
        for field, name in rows:
            if field == "risks":
                cells = [str(metrics[setup]["risks"]) for setup in setups]
            elif field.startswith("rq4"):
                cells = [_thousands(metrics[setup][field]) for setup in setups]
            else:
                cells = [_percent(metrics[setup][field]) for setup in setups]
            lines.append(("\\quad " if group else "") + f"{name} & " + " & ".join(cells) + " \\\\")
    lines += ["\\hline", "\\end{tabular}", "\\end{table}"]
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("results", type=Path, help="Results folder written by run.py")
    parser.add_argument("--llm", type=Path,
                        help="An llm_scores_<model>.jsonl to score from, instead of judging.csv")
    parser.add_argument("--threshold", type=int, default=7,
                        help="With --llm, the lowest score that counts as a yes (default 7)")
    parser.add_argument("--second-judge", type=Path,
                        help="A copy of judging.csv judged independently, for Cohen's kappa")
    args = parser.parse_args()

    has_human = (args.results / "judging.csv").exists() and (args.results / "key.csv").exists()
    human = human_rows(args.results) if has_human else []
    if args.llm:
        rows = llm_rows(args.llm, args.threshold)
        model = rows[0]["judge_model"].split("/")[-1] if rows else args.llm.stem
        source = f"llm_{model}"
        judge = f"{model} (a score of {args.threshold} or more counts as yes)"
    elif human:
        rows, source, judge = human, "human", "hand"
    else:
        raise SystemExit("No judgements: run judging.py and fill in judging.csv, or pass --llm.")

    unjudged = sum(row["correct"] is None or row["supported"] is None for row in rows)
    if unjudged:
        print(f"Warning: {unjudged} of {len(rows)} risks are not fully judged and are left out.\n")

    with (args.results / "assessments.jsonl").open(encoding="utf-8") as file:
        assessments = [json.loads(line) for line in file]
    metrics, pool_size = setup_metrics(rows, assessments)
    routes = kg_routes(rows)
    one_off = one_off_usage(args.results)

    agreements = {}
    if args.llm and any(row["correct"] is not None for row in human):
        agreements["llm_vs_human"] = agreement(rows, human)
    if args.second_judge and human:
        second = {row["row_id"]: row for row in _read_csv(args.second_judge)}
        second_rows = [{**row, "correct": _answer(second[row["row_id"]]["correct"]),
                        "supported": _answer(second[row["row_id"]]["supported"])}
                       for row in _read_csv(args.results / "key.csv") if row["row_id"] in second]
        agreements["human_vs_second_judge"] = agreement(human, second_rows)

    columns = list(next(iter(metrics.values())).keys())
    print("| setup | " + " | ".join(columns) + " |")
    print("|---" * (len(columns) + 1) + "|")
    for setup, values in metrics.items():
        print(f"| {setup} | " + " | ".join(
            "-" if values[column] is None else str(values[column]) for column in columns) + " |")
    print(f"\nPool of correct and supported (requirement, provision) pairs: {pool_size}")
    print("\nKG routes behind its correct and supported risks:")
    for route, counts in routes.items():
        print(f"  {route}: {counts['found']} ({counts['only_route']} found by this route only)")
    if one_off:
        requirements = metrics.get("kg", {}).get("requirements") or 1
        total = sum(usage["input"] + usage["output"] for usage in one_off.values())
        print("\nKG one-off tokens for this SRS: " + ", ".join(
            f"{name} {usage['input']:,} in / {usage['output']:,} out"
            for name, usage in one_off.items())
              + f" ({total / requirements:,.0f} per requirement assessed)")
    for name, result in agreements.items():
        print(f"\nAgreement, {name.replace('_', ' ')}:")
        for field, values in result.items():
            print(f"  {field}: kappa {values['kappa']}, {_percent(values['agree'])} agree, "
                  f"over {values['risks']} risks".replace("\\", ""))

    table = latex_table(
        metrics, (f"Results per setup, judged by {judge}. Tokens are per requirement, "
                  "except the last row.").replace("_", "\\_"), "tab:results")
    (args.results / f"metrics_{source}.json").write_text(json.dumps({
        "source": source, "threshold": args.threshold if args.llm else None,
        "setups": metrics, "pool_size": pool_size, "kg_routes": routes, "kg_one_off": one_off,
        "agreement": agreements,
    }, indent=2), encoding="utf-8")
    (args.results / f"results_{source}.tex").write_text(table + "\n", encoding="utf-8")
    print(f"\nWrote {args.results / f'metrics_{source}.json'} and "
          f"{args.results / f'results_{source}.tex'}")


if __name__ == "__main__":
    main()

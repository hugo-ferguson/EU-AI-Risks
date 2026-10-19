"""
Split an EU AI Act use-case JSON file into one file per data item.

For each item in "data" this writes:
  <index>_<role>_<domain>.json  - the item exactly as it appears in the source
  <index>_<role>_<domain>.md    - a one-line requirements file for load_requirements()
"""


import csv
import json
import re
import time
import traceback
from dataclasses import dataclass, field
from pathlib import Path

def _load_json(path: Path) -> dict | list:
    raw = path.read_text(encoding="utf-8")
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        # Handle a truncated file (e.g. cut off after a trailing "},")
        repaired = raw.rstrip().rstrip(",")
        for suffix in ("]}", "}]}", "]", ""):
            try:
                data = json.loads(repaired + suffix)
                print(f"Warning: {path.name} was truncated; repaired it.")
                return data
            except json.JSONDecodeError:
                continue
        raise


def _slug(text: str, max_len: int = 40) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return slug[:max_len].rstrip("-") or "item"


def _to_requirement_text(intended_use: str) -> str:
    text = re.sub(r"\s+", " ", intended_use).strip().rstrip(".")
    text = text[0].lower() + text[1:]
    return f"The system shall {text}."


def split_items(
    input_path: Path,
    output_dir: Path,
    formats: tuple[str, ...] = ("json", "md"),
) -> int:
    data = _load_json(input_path)
    items = data["data"] if isinstance(data, dict) else data

    output_dir.mkdir(parents=True, exist_ok=True)

    written = 0
    for index, item in enumerate(items, start=1):
        name = f"{index:03d}_{_slug(item.get('role', ''))}_{_slug(item.get('domain', ''))}"

        if "json" in formats:
            (output_dir / f"{name}.json").write_text(
                json.dumps(item, indent=4, ensure_ascii=False), encoding="utf-8")

        if "md" in formats:
            intended_use = (item.get("intended_use") or "").strip()
            if intended_use:
                # Use the item's global index so IDs stay unique if several
                # files are loaded into the same graph.
                content = (
                    "# Requirements\n\n"
                    f"REQ-{index:03d}: {_to_requirement_text(intended_use)}\n"
                )
                (output_dir / f"{name}.md").write_text(content, encoding="utf-8")

        written += 1

    return written


def _reset_requirements():
    """Delete all nodes and relationships from the Neo4j database."""
    from eu_ai_risks.requirements.loader import reset_requirements
    from eu_ai_risks.db import get_session
    
    with get_session() as session:
        reset_requirements(session)
    print("Requirements cleared.")


def _load_requirements(
        document_path: Path,
        save_to_json: bool,
):
    """Extract requirements, split into triples, and write to Neo4j."""
    from eu_ai_risks.requirements.loader import write_triples

    print(f"Loading requirements from {document_path} ...")
    write_triples(document_path, save_to_json)
    print("Done.")


def _assess_risks(
    document_path: Path,
    output: Path ,
):
    """Load requirements into the graph and assess EU AI Act compliance risks."""
    from functools import partial
    from eu_ai_risks.db.graph import list_requirements
    from eu_ai_risks.analysis.risk_report import (
        collect_citations, entries_from_assessments,
        write_markdown_report,
    )

    requirements = list_requirements()
    if not requirements:
        raise ValueError("  No requirements found in graph.")

    print(f"Found {len(requirements)} requirements in graph.")


    from eu_ai_risks.analysis.risk_assessor import assess_requirement, classify_system
    system = classify_system([(r["id"], r["text"]) for r in requirements])
    print(f"System classified under: {', '.join(system.annex_iii_points) or 'no Annex III point'}")
    assess_requirement = partial(assess_requirement, system=system)

    article_cache: dict[str, dict] = {}

    assessment_entries: list[dict] = []
    for i, requirement in enumerate(requirements, 1):
        requirement_id = requirement["id"]
        requirement_text = requirement["text"]
        print(f"  [{i}/{len(requirements)}] {requirement_id}...")

        assessment, raw = assess_requirement(requirement_id, requirement_text)
        citations = collect_citations(assessment.risks, article_cache)

        assessment_entries.append({
            "requirement": requirement,
            "assessment": assessment,
            "citations": citations,
        })

    entries = entries_from_assessments(assessment_entries)
    write_markdown_report(entries, output)
    print(f"Wrote {output}")


def run_scenarios(
    scenarios_dir: Path,
    save_to_json: bool = False,
    skip_existing: bool = False,
    suffix: str = "_report",
) -> dict[str, list[str]]:
    """
    For every requirements .md file in `scenarios_dir`, run:
        reset -> load requirements -> assess risks
    and write the report next to it as <name><suffix>.md
    (e.g. 001_provider_retail_report.md).

    Returns a dict with "succeeded", "failed" and "skipped" file names.
    """
    scenarios_dir = Path(scenarios_dir)
    if not scenarios_dir.is_dir():
        raise FileNotFoundError(f"Scenarios folder not found: {scenarios_dir}")

    # Exclude previously generated reports so reruns don't treat them as inputs.
    md_files = sorted(
        p for p in scenarios_dir.glob("*.md") if not p.stem.endswith(suffix)
    )
    if not md_files:
        print(f"No .md scenario files found in {scenarios_dir}")
        return {"succeeded": [], "failed": [], "skipped": []}

    results: dict[str, list[str]] = {"succeeded": [], "failed": [], "skipped": []}

    for n, md_path in enumerate(md_files, 1):
        report_path = md_path.with_name(f"{md_path.stem}{suffix}.md")
        print(f"\n=== [{n}/{len(md_files)}] {md_path.name} ===")

        if skip_existing and report_path.exists():
            print(f"  Report already exists, skipping: {report_path.name}")
            results["skipped"].append(md_path.name)
            continue

        start = time.perf_counter()
        try:
            _reset_requirements()
            _load_requirements(md_path, save_to_json)
            _assess_risks(md_path, report_path)
            print(f"  Finished in {time.perf_counter() - start:.1f}s")
            results["succeeded"].append(md_path.name)
        except Exception as exc:
            print(f"  FAILED: {type(exc).__name__}: {exc}")
            traceback.print_exc()
            results["failed"].append(md_path.name)

    print("\n=== Summary ===")
    print(f"  Succeeded: {len(results['succeeded'])}")
    print(f"  Skipped:   {len(results['skipped'])}")
    print(f"  Failed:    {len(results['failed'])}")
    for name in results["failed"]:
        print(f"    - {name}")

    return results

DEFAULT_WEIGHT = 1.0
RISKS_FACTOR = 1.0      # article appears in a **Risks:** block
SELECTED_FACTOR = 0.10 # article appears only on an "Articles selected from the index" line

_PROHIBITED_LOW = (
    set(range(6, 30))
    | {40, 41, 42, 43, 44, 45, 46, 47, 49, 60, 71, 72, 73, 80, 86}
)

RISK_WEIGHTS: dict[str, dict] = {
    "prohibited": {
        "general": {"5": 5.0, "99": 3.0},
        "low": {str(a) for a in _PROHIBITED_LOW},
        "low_weight": 0.10,
    },
    "high": {
        "general": {"6": 3.0, "annex_3": 3.0},
        "low": set(),
        "low_weight": 0.25,
    },
    "limited": {
        "general": set(),
        "low": {"6","annex_3"},
        "low_weight": 0.1,
    },
    "minimal": {
        "general": set(),
        "low": {"6","annex_3"},
        "low_weight": 0.1,
    },
}

_ROMAN = {"i": 1, "ii": 2, "iii": 3, "iv": 4, "v": 5, "vi": 6, "vii": 7, "viii": 8, "ix": 9, "x": 10, "xi": 11, "xii": 12, "xiii": 13}

# Matches art:5, art:5:p1:a  ->  "5"
_ART_RE = re.compile(r"\bart:(\d+)", re.I)
# Matches annex:III, annex:III:5:b  ->  "III"  (later normalised to "annex_3")
_ANNEX_RE = re.compile(r"\bannex:([ivxlc]+|\d+)", re.I)

_SELECTED_PREFIX = "**Articles selected from the index:**"


def _ids_in(text: str) -> set[str]:
    found = set(_ART_RE.findall(text))
    found.update(_normalise_annex(m) for m in _ANNEX_RE.findall(text))
    return found


def _normalise_level(value: str) -> str:
    v = (value or "").lower()
    if "prohib" in v:
        return "prohibited"
    if "high" in v:
        return "high"
    if "limited" in v or "transparen" in v:
        return "limited"
    return "minimal"


def _normalise_annex(token: str) -> str:
    token = token.strip().lower()
    num = int(token) if token.isdigit() else _ROMAN.get(token)
    return f"annex_{num}" if num else f"annex_{token}"


def _weight(article: str, level: str) -> float:
    cfg = RISK_WEIGHTS[level]
    if article in cfg["general"]:
        return cfg["general"][article]
    if article in cfg["low"]:
        return cfg["low_weight"]
    return DEFAULT_WEIGHT


def _risks_text(report_text: str) -> str:
    """Return only the text inside **Risks:** blocks (up to the next bold heading, ---, or ### heading)."""
    kept, capturing = [], False
    for line in report_text.splitlines():
        s = line.strip()
        if s.startswith("**Risks:**"):
            capturing = True
            continue
        if capturing and (s.startswith("**") or s == "---" or s.startswith("### ")):
            capturing = False
        if capturing:
            kept.append(line)
    return "\n".join(kept)


def extract_report_articles(
    report_text: str,
    risks_factor: float = RISKS_FACTOR,
    selected_factor: float = SELECTED_FACTOR,
) -> dict[str, float]:
    """
    Return {article_id: source_factor} for every article the report lists.
    Ids are matched in any form: art:5, (art:5), `art:5:p1:a`, (annex:III:5:b).
    Risks-block articles get risks_factor; selected-only articles get selected_factor.
    """
    selected_lines = "\n".join(
        l for l in report_text.splitlines() if l.startswith(_SELECTED_PREFIX)
    )
    found = {a: selected_factor for a in _ids_in(selected_lines)}
    found.update({a: risks_factor for a in _ids_in(_risks_text(report_text))})
    return found


def _expected_articles(item: dict, level: str) -> set[str]:
    expected = set(RISK_WEIGHTS[level]["general"])
    for a in item.get("related_articles", []):
        s = str(a).strip().lower()
        m = re.match(r"annex\s*([ivxlc\d]+)", s)
        expected.add(_normalise_annex(m.group(1)) if m else re.sub(r"\D", "", s) or s)
    return expected


@dataclass
class EvalResult:
    name: str
    risk_level: str
    precision: float
    recall: float
    f1: float
    true_positives: list[str] = field(default_factory=list)
    false_positives: list[str] = field(default_factory=list)
    false_negatives: list[str] = field(default_factory=list)


def evaluate_report(
    report_path: Path,
    json_path: Path | None = None,
    risks_factor: float = RISKS_FACTOR,
    selected_factor: float = SELECTED_FACTOR,
) -> EvalResult:
    """
    Each predicted article's credit = level weight * source factor.

        credit(TP)  = sum(weight * factor)          for TP articles
        precision   = credit(TP) / sum(weight * factor for all predicted)
        recall      = credit(TP) / sum(weight for all expected)

    An expected article found only via the index therefore earns partial recall,
    and a stray index-only article costs little precision.
    """
    report_path = Path(report_path)
    if json_path is None:
        stem = report_path.stem.removesuffix("_report")
        json_path = report_path.with_name(f"{stem}.json")

    item = json.loads(Path(json_path).read_text(encoding="utf-8"))
    level = _normalise_level(item.get("risk_level", ""))

    expected = _expected_articles(item, level)
    factors = extract_report_articles(
        report_path.read_text(encoding="utf-8"), risks_factor, selected_factor
    )
    predicted = set(factors)

    tp = expected & predicted
    fp = predicted - expected
    fn = expected - predicted

    credit = lambda arts: sum(_weight(a, level) * factors[a] for a in arts)
    exp_weight = sum(_weight(a, level) for a in expected)

    precision = credit(tp) / credit(predicted) if predicted else (1.0 if not expected else 0.0)
    recall = credit(tp) / exp_weight if expected else 1.0
    f1 = 2 * precision * recall / (precision + recall) if (precision + recall) else 0.0

    key = lambda a: (not a.isdigit(), int(a) if a.isdigit() else 0, a)
    return EvalResult(
        name=report_path.stem.removesuffix("_report"),
        risk_level=level,
        precision=precision,
        recall=recall,
        f1=f1,
        true_positives=sorted(tp, key=key),
        false_positives=sorted(fp, key=key),
        false_negatives=sorted(fn, key=key),
    )


def evaluate_scenarios(
    scenarios_dir: Path,
    suffix: str = "_report",
    csv_path: Path | None = None,
    risks_factor: float = RISKS_FACTOR,
    selected_factor: float = SELECTED_FACTOR,
) -> list[EvalResult]:
    """Evaluate every <name>_report.md in the folder against <name>.json."""
    scenarios_dir = Path(scenarios_dir)
    results = []
    for report in sorted(scenarios_dir.glob(f"*{suffix}.md")):
        json_path = report.with_name(f"{report.stem.removesuffix(suffix)}.json")
        if not json_path.exists():
            print(f"Skipping {report.name}: no matching {json_path.name}")
            continue
        results.append(evaluate_report(report, json_path, risks_factor, selected_factor))

    print(f"{'scenario':<55}{'level':<11}{'P':>6}{'R':>6}{'F1':>6}  FP / FN")
    for r in results:
        print(f"{r.name[:54]:<55}{r.risk_level:<11}{r.precision:6.2f}{r.recall:6.2f}{r.f1:6.2f}"
              f"  +{r.false_positives} -{r.false_negatives}")

    if results:
        n = len(results)
        print(f"{'MACRO AVERAGE':<66}{sum(r.precision for r in results)/n:6.2f}"
              f"{sum(r.recall for r in results)/n:6.2f}{sum(r.f1 for r in results)/n:6.2f}")

    if csv_path and results:
        with open(csv_path, "w", newline="", encoding="utf-8") as f:
            wr = csv.writer(f)
            wr.writerow(["scenario", "risk_level", "precision", "recall", "f1", "tp", "fp", "fn"])
            for r in results:
                wr.writerow([r.name, r.risk_level, f"{r.precision:.3f}", f"{r.recall:.3f}", f"{r.f1:.3f}",
                             " ".join(r.true_positives), " ".join(r.false_positives), " ".join(r.false_negatives)])
    return results


if __name__ == "__main__":
    test_path = Path("eu_ai_risks/tests/scenarios")
    result_path = Path("eu_ai_risks/tests/results.csv")
    # run_scenarios(Path("eu_ai_risks/tests/scenarios"), True, True)
    evaluate_scenarios(test_path, csv_path=result_path)
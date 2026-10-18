"""
Run the system and the three baselines over an SRS, saving every assessment
for judging (judging.py) and scoring (metrics.py).
"""

import argparse
import json
import time
from pathlib import Path

from dotenv import load_dotenv

# The package reads its LLM and Neo4j settings at import
load_dotenv()

from eu_ai_risks.analysis.risk_assessor import (  # noqa: E402
    SystemContext, assess_requirement, classify_system,
)
from eu_ai_risks.db import get_session  # noqa: E402
from eu_ai_risks.db.graph import list_requirements  # noqa: E402
from eu_ai_risks.requirements.loader import reset_requirements, write_triples  # noqa: E402

# Setup name -> retrieval mode in risk_assessor
SETUPS = {"kg": "graph", "llm-only": "none", "full-act": "full", "chunk-rag": "chunk"}


def _completed(path: Path) -> set[tuple[str, int, str]]:
    """(setup, run, requirement id) already saved, so an interrupted run can resume."""
    if not path.exists():
        return set()
    with path.open(encoding="utf-8") as file:
        rows = [json.loads(line) for line in file if line.strip()]
    return {(row["setup"], row["run"], row["requirement_id"]) for row in rows}


def _system_context(requirements: list[tuple[str, str]], path: Path) -> SystemContext:
    """Classify the system once and reuse it, so every run of the KG setup shares it."""
    if path.exists():
        saved = json.loads(path.read_text(encoding="utf-8"))
        return SystemContext(
            requirements=tuple(requirements),
            intended_purpose=saved["intended_purpose"],
            annex_iii_points=tuple(saved["annex_iii_points"]),
        )
    system = classify_system(requirements)
    path.write_text(json.dumps({
        "intended_purpose": system.intended_purpose,
        "annex_iii_points": list(system.annex_iii_points),
    }, indent=2), encoding="utf-8")
    return system


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("srs", type=Path,
                        help="SRS to evaluate on; it should not have been used during development")
    parser.add_argument("--out", type=Path, default=Path("evaluation/results"),
                        help="Results are written to OUT/<SRS file name>/")
    parser.add_argument("--setups", default=",".join(SETUPS),
                        help=f"Comma-separated, from: {', '.join(SETUPS)}")
    parser.add_argument("--runs", type=int, default=1, help="Times to assess each requirement")
    parser.add_argument("--limit", type=int,
                        help="Only assess the first N requirements, for a quick check")
    parser.add_argument("--skip-load", action="store_true",
                        help="The SRS is already loaded into the graph")
    args = parser.parse_args()

    setups = [setup.strip() for setup in args.setups.split(",") if setup.strip()]
    unknown = sorted(set(setups) - set(SETUPS))
    if unknown:
        parser.error(f"unknown setups: {', '.join(unknown)}")

    out = args.out / args.srs.stem
    out.mkdir(parents=True, exist_ok=True)
    results_path = out / "assessments.jsonl"

    if not args.skip_load:
        # Requirements left from another SRS would otherwise be assessed too
        with get_session() as session:
            reset_requirements(session)
        print(f"Loading requirements from {args.srs} ...")
        write_triples(args.srs)

    requirements = [(row["id"], row["text"]) for row in list_requirements()]
    if not requirements:
        raise SystemExit("No requirements in the graph.")
    # The whole SRS is still the system's context when only some are assessed
    system = _system_context(requirements, out / "system.json")
    baseline_system = SystemContext(requirements=tuple(requirements))
    assessed = requirements[:args.limit] if args.limit else requirements
    print(f"System classified under: {', '.join(system.annex_iii_points) or 'no Annex III point'}")

    completed = _completed(results_path)
    total = args.runs * len(setups) * len(assessed)
    done = 0
    with results_path.open("a", encoding="utf-8") as results:
        for run in range(args.runs):
            for setup in setups:
                mode = SETUPS[setup]
                for requirement_id, text in assessed:
                    done += 1
                    if (setup, run, requirement_id) in completed:
                        continue
                    print(f"[{done}/{total}] run {run} {setup} {requirement_id}")
                    started = time.monotonic()
                    try:
                        assessment, raw = assess_requirement(
                            requirement_id, text,
                            system=system if mode == "graph" else baseline_system,
                            mode=mode)
                    except Exception as error:  # noqa: BLE001
                        # Skipped rather than saved, so rerunning the command retries it
                        print(f"  failed: {error}")
                        continue
                    if raw.get("fallback_used"):
                        print("  failed: the model did not return valid JSON")
                        continue
                    results.write(json.dumps({
                        "setup": setup,
                        "mode": mode,
                        "run": run,
                        "requirement_id": requirement_id,
                        "requirement_text": text,
                        "assessment": assessment.model_dump(),
                        "retrieval": raw.get("retrieval"),
                        "not_assessed": bool(raw.get("not_assessed")),
                        "seconds": round(time.monotonic() - started, 1),
                    }) + "\n")
                    results.flush()

    print(f"Wrote {results_path}")


if __name__ == "__main__":
    main()

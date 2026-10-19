# Evaluation

Compares the system (`kg`) with three baselines that use the same LLM, instructions,
requirement, SRS and output format, but differ in what they are given from the EU AI Act:

| Setup | Given from the Act | Retrieval mode |
|---|---|---|
| `kg` | Provisions retrieved through the KGs, plus the system classification, definitions and related requirements | `graph` |
| `llm-only` | Nothing; cites from the LLM's own knowledge of the Act | `none` |
| `full-act` | Every article paragraph and annex | `full` |
| `chunk-rag` | The 10 paragraphs most similar to the requirement | `chunk` |

## Before running

- Build and enrich the Act graph (`eu-ai-risks all`).
- Use one `LLM_MODEL` for every setup. `full-act` sends about 121k tokens per requirement
  (measured on Haiku 5.5), so the model needs a context window of at least 200k tokens. On
  Haiku 5.5 this is above the 100K-token price threshold, so each full-act call costs about $0.06.
- Evaluate on an SRS that was not used during development, so the results do not reflect
  changes made to suit its requirements.

## Steps

1. **Run** every setup over the SRS. This clears the requirements in the graph and loads the SRS:

   ```bash
   python -m evaluation.run path/to/srs.md
   ```

   Results are appended to `evaluation/results/<srs>/assessments.jsonl`. Rerunning the same
   command skips what is already saved, so an interrupted run resumes. Add `--limit 2` for a
   quick check first.

2. **Judge** every risk, by hand, by an LLM, or both. Both judge the same three things,
   set out in [rubric.md](rubric.md): whether the gap is real (RQ1), whether the cited provision
   supports it (RQ2), and whether the citation leads to the operative words of the Act (RQ3).

   **By an LLM** (default Sonnet 5.5; set `JUDGE_MODEL` or `--model` to change it, e.g.
   `openai/gpt-5`). It scores each risk 0-10 per criterion and only returns the scores. The
   rubric and the SRS are cached, so each request only adds the risk and its provision:

   ```bash
   python -m evaluation.llm_judge evaluation/results/<srs> [--effort low]
   ```

   Scores go to `llm_scores_<model>.jsonl`. Rerunning skips risks already scored.

   **By hand**:

   ```bash
   python -m evaluation.judging evaluation/results/<srs>
   ```

   This writes `judging.csv`, with every risk shuffled and its setup hidden, and `key.csv`,
   which maps rows back to setups (don't open it until judging is done). Fill in `correct`
   and `supported` with `y` or `n`, following the rubric's first two criteria. Rows citing a
   provision that does not exist are already marked unsupported. Judging even a sample by hand
   lets `metrics.py` report how far the LLM judge agrees with you.

3. **Score**:

   ```bash
   python -m evaluation.metrics evaluation/results/<srs>                       # from judging.csv
   python -m evaluation.metrics evaluation/results/<srs> --llm <scores.jsonl>  # from LLM scores
   ```

   With `--llm`, a score of 7 or more counts as a yes (`--threshold` changes it), and the mean
   score per criterion is reported too. Each prints a table per setup and writes
   `metrics_<judge>.json` and `results_<judge>.tex`, a LaTeX table for the report.

## Metrics

| RQ | Metric | Meaning |
|---|---|---|
| RQ1 | `rq1_precision` | Share of risks judged correct |
| RQ1 | `rq1_recall` | Share of the pool found, where the pool is every (requirement, provision) pair that any setup got correct and supported |
| RQ1 | KG routes | Which retrieval routes found the provisions of the KG setup's correct and supported risks, and how many only one route found |
| RQ2 | `rq2_exists` | Share of citations that refer to a provision or article in the Act |
| RQ2 | `rq2_supported` | Share of risks judged supported by their cited provision |
| RQ3 | `rq3_specific` | Share of citations of a paragraph or point rather than a whole article |
| RQ3 | `rq3_quote_match` | Share of risks whose quote appears in the cited provision's text |
| RQ3 | `rq3_quote_match_loose` | The same, ignoring punctuation (needs a `key.csv` from `judging.py --key-only` or later) |
| RQ4 | `rq4_input_tokens_mean`, `rq4_output_tokens_mean` | Mean tokens per requirement over every LLM call of the assessment (for the KG setup, its article selection too); cached input counts as input |
| RQ4 | `rq4_tokens_per_good_risk` | All tokens the setup used, divided by its risks judged correct and supported |
| RQ4 | KG one-off tokens | Building the requirements KG (`load_usage.json`) and classifying the system (`system.json`), once per SRS |
| All | `mean_gap_validity`, `mean_provision_support`, `mean_citation_precision` | With `--llm`, the mean 0-10 rubric score for RQ1, RQ2 and RQ3 |

Token use is recorded from runs made after it was added; older results show `-` for RQ4.
Tokens are reported rather than prices, which change; they are specific to the model's tokenizer,
so compare setups run on the same model.

`provisions_supplied_mean` is the mean number of provisions given to the LLM per requirement.
Recall is relative to the pool, so a risk that no setup found is not counted.

Precision and support are also given with 95% Wilson intervals (`rq1_precision_ci`,
`rq2_supported_ci`), and the KG setup's difference in recall from each baseline with a 95% interval
from 4,000 resamples of the requirements, drawn with replacement and a fixed seed
(`recall_differences` in `metrics_<judge>.json`). An interval that excludes 0 means the difference
is larger than chance.

To add a new check to an SRS that has already been judged, rewrite only its key with
`python -m evaluation.judging evaluation/results/<srs> --key-only`. It refuses to run if the rows
no longer match the existing `judging.csv`.

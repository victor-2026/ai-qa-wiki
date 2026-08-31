# How to Run LLM Evals in CI/CD

**Source:** https://getautonoma.com/blog/how-to-run-llm-evals-in-ci-cd
**Date:** 2026-07-27
**Tags:** #autonoma #llm-evals #cicd #threshold-gating
**Raw:** [autonoma-llm-evals-ci-cd-2026.md](../raw/autonoma-llm-evals-ci-cd-2026.md)

---

## What It Is (3-5 bullets)

- **LLM eval = score vs threshold, not exact match**: correctness, faithfulness, tone scored by a function (semantic similarity, groundedness, LLM-as-judge rubric) and gated on whether the score clears a bar — what separates it from a unit test (Tom Piaggio, Autonoma, 2026-07-27, repo `Autonoma-Tools/how-to-run-llm-evals-in-ci-cd`).
- **Two-speed pipeline pattern**: deterministic tests (prompt building, parsing, retries, schema) on every commit/PR — free, ms; eval tests only on merge to `main` + nightly cron — paid tokens, seconds per case. Running full evals on every commit burns a month's API budget in a week.
- **Runnable scoring + gating**: `src/scorer.py` folds semantic similarity + groundedness into one float; `tests/test_evals.py` runs each dataset case N times, averages, asserts average ≥ baseline − tolerance; `scripts/run_evals.py` summarizes aggregated regression, not just pytest pass/fail.
- **Versioned JSONL dataset** `data/eval_dataset.jsonl` (id, input, reference/grounding, tags) owned and reviewed like a migration — one case per line, diffable; fed from both design-time query types and production failures (escalation becomes a new row).

## Key Patterns / Techniques (table or bullets)

| Pattern | How it works (from raw) | File in repo |
|---------|-------------------------|--------------|
| **Deterministic vs eval split** | Deterministic asserts fact (same input → exact output); eval asserts graded quality via scoring function; eval cannot use string equality ("refund was processed" vs "I've processed your refund" = both correct) | Deterministic suite vs `tests/test_evals.py` |
| **Two triggers, two jobs** | `deterministic-tests` on every push/PR; `llm-evals` on push to main + `schedule:` nightly + `workflow_dispatch` manual | `.github/workflows/evals.yml` |
| **N-run averaging for noise** | Same case N times (floor 3, default 5), average score, compare average to stored baseline minus tolerance 0.05-0.1 on 0-1 scale; single outlier does not fail build; consistent 5-low = real regression | `tests/test_evals.py` + `src/scorer.py` |
| **Scorer composition** | One float from semantic similarity + groundedness/faithfulness so downstream gate has single number | `src/scorer.py` |
| **Baseline + tolerance gate** | Compare per-case averaged score to stored baseline file; reporting script fails job when any case regresses past tolerance even if still above individual threshold | `scripts/run_evals.py` |
| **Dataset schema** | JSON Lines: id, input, reference answer or grounding context, tags (query type, regression it catches); add case = one-line diff | `data/eval_dataset.jsonl` |
| **Why nightly is non-optional** | Merge hook catches deliberate prompt/model changes; nightly catches silent provider rollout behind same alias with no PR — skip either and one drift class sits undetected | Workflow schedule |

> DeepEval's `LLMTestCase`/`assert_test` and its averaging-3-plus-runs recommendation are explicitly called closest to correct; this guide adds the pipeline around them (dataset versioning, workflow file, aggregation).

## Relevance to QA/QE (table QA Action)

| QA Concern | Action |
|------------|--------|
| **"We run evals" = manual script + eyeballed spreadsheet** | Promote to CI gate with `evals.yml`: required job on merge + nightly, with `run_evals.py` that exits non-zero on aggregated regression |
| **Full evals on every commit burns budget** | Keep deterministic on every commit; reserve evals for merge/nightly; use `workflow_dispatch` before release instead of per-push |
| **Single-run flake → team ignores red** | Average N=5 per case; gate on average vs baseline−tolerance, never on one run; tolerance 0.05-0.1 absorbs sampling noise, not a 5-low drop |
| **Reference answers drifting stale** | Assign dataset owner; review cadence matching fixture cadence; treat "is reference still true after product copy change?" as checklist item |
| **Dataset only from design phase** | Mine cases from production: support escalations, confusing transcripts, confident-wrong answers — suite must grow from real traffic, not imagination |
| **Regression looks like flake** | Semantic/judge scoring, not exact string; if case still flakes at N=5, assertion too strict or prompt ambiguous — fix, not retry |

## Critical Analysis (Strengths/Gaps)

**Strengths:**
- Two-speed scheduling is priced in real token cost and wait time, not theory — the merge+nightly pattern directly maps to two distinct drift sources (team change vs provider change).
- Averaging + baseline−tolerance is a practical noise gate that prevents single-outlier red while still catching consistent drops.
- JSONL dataset discipline (reviewable, diffable, owned) and dual sourcing (design + prod) keep evals honest over time.

**Gaps:**
- Scorer aggregation (similarity + groundedness → one float) weight choice not justified — trade-off between correctness and faithfulness left implicit.
- N=5 and tolerance 0.05-0.1 given as comfortable defaults without quantifying detection power (what drop size is reliably caught, false-fence rate).
- DeepEval docs already recommend averaging; novelty is pipeline wiring, but workflow file excerpt not fully shown in article body — requires repo read to reproduce exactly.
- No guidance on handling new-model adoption after baseline regression (when to re-baseline vs block) or on tracking token/latency alongside score.

## Worked Example (from raw)

- **Anti-pattern:** eval job on every commit with six small PR pushes in an afternoon burns monthly token budget — scheduling, not smarter model, fixed it.
- **Scoring:** "refund was processed" vs "I've processed your refund" — string equality fails, embedding/judge passes — illustrates why evals need scoring.
- **Averaging gate:** Case averages 0.88 vs baseline 0.90 with tolerance 0.05 = pass (single 0.72 outlier absorbed); five runs at 0.70-0.73 = fail, consistent drop caught.
- **Silent drift:** provider rolls new weights behind same alias Thursday night — no PR triggers merge job, but Friday 2am nightly eval run fails and flags before customers do.
- **Dataset growth:** beta transcript where model was confidently wrong about refund policy → new JSONL row with correct reference + tag `regression: refund-policy` → future drift blocked.

## FAQ Highlights (from raw)

- Pipeline = two lanes: deterministic every commit (free/fast), evals at merge + nightly (paid, seconds per case).
- Eval tests scored quality (correctness, faithfulness, tone) via scoring function vs threshold; unit test asserts exact output.
- Reproducibility via averaging N runs (3 floor, 5 default) vs baseline ± tolerance, not identical strings.
- Custom eval needs dataset + scorer + N-run runner + CI job on merges/nightly; do not run eval suite on every commit.

## Reuse Checklist

- Fork `Autonoma-Tools/how-to-run-llm-evals-in-ci-cd`; point `data/eval_dataset.jsonl` at your feature; keep schema id/input/reference/tags.
- Implement `src/scorer.py` pattern: `score = w1*similarity + w2*groundedness` (tune weights, record rationale) and document embedding/judge model pinned.
- Set `tests/test_evals.py` to N=5 per case; assert `avg >= baseline[name] - 0.07`; store baselines in `baselines/eval_scores.json`.
- Wire `.github/workflows/evals.yml` two-job split; make `llm-evals` required on `push: branches: [main]` + `schedule: cron: '0 2 * * *'` + `workflow_dispatch`.
- Add dataset PR checklist: new case source, reference still true, tag added, baseline updated only on intentional change (not to make a failing eval pass).

## Cross-links

- Prompt unit layer: [LLM Unit Testing](autonoma-llm-unit-testing-2026.md) — assertions this lane gates every commit; [Non-Deterministic Outputs](autonoma-non-deterministic-outputs-2026.md) — sampling and threshold details
- Tool/agent regression: [Testing Tool Calls](autonoma-testing-tool-calls-2026.md) — K-of-N for trajectories; [Agent Regression Testing](https://getautonoma.com/blog/agent-regression-testing) — golden trajectory variant
- Feature gate: [QA a Generative AI Feature](autonoma-qa-ai-feature-2026.md) — consumes this pipeline as its eval + red-team lane
- Streaming: [Streaming Responses](autonoma-streaming-responses-2026.md) — same two-speed split (fake-server every commit, browser on PR)
- Guardrails/injection: `how-to-test-for-prompt-injection` + `how-to-test-ai-guardrails` — guardrail pass alongside eval lane referenced in next pillar
- Behavioral outcome: [How to Test an AI Agent E2E](autonoma-how-to-test-ai-agent-e2e-2026.md) — eval proves text clears bar, behavioral proves action landed; Autonoma PreviewKit sits after eval gate
- Evidence: [AI QA Evidence Layer](ai-qa-evidence-layer-validation-evals-guardrails-telemetry.md) — eval = model eval, app effect = downstream validation
- Repo: [Autonoma-Tools/how-to-run-llm-evals-in-ci-cd](https://github.com/Autonoma-Tools/how-to-run-llm-evals-in-ci-cd)

## Reuse Notes

- Log tokens and p95 latency per eval case alongside score — cost drift is a separate regression signal from quality.

---
*Ingested: 2026-08-31*

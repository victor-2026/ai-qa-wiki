# How to Test a RAG Pipeline: Two Surfaces, Not One Score

**Source:** https://getautonoma.com/blog/how-to-test-a-rag-pipeline
**Date:** 2026-07-28
**Tags:** #autonoma #rag-testing #rag-pipeline #ragas #deepeval
**Raw:** [autonoma-rag-pipeline-2026.md](../raw/autonoma-rag-pipeline-2026.md)

---

## What It Is (3-5 bullets)

- **Two-surface RAG test split**: retrieval and generation tested as independent gates — retriever output (which chunks returned) vs generator output (faithfulness to those chunks) — so a "confidently wrong" answer is localized to the stage that broke (Tom Piaggio, Autonoma, 2026-07-28, repo `Autonoma-Tools/how-to-test-a-rag-pipeline`).
- **Runnable harness with eval-set builder**: `scripts/build_eval_set.py` samples own index, LLM-drafts Q+A pairs, mines real user logs, and adds adversarial unanswerable questions; `eval_set/eval_set.json` is the reviewed, tagged corpus the tests consume.
- **Library-agnostic metric gates**: retrieval via hit-rate/MRR/precision-recall offline; generation via Ragas `tests/test_generation_ragas.py` and DeepEval `tests/test_generation_deepeval.py` (faithfulness, answer relevancy, context precision) — both aggregated as mean across eval set and threshold-gated in CI.
- **CI gate on aggregate, not single example**: `.github/workflows/rag-tests.yml` fails PR when mean drops; `lib/repeat_and_threshold.py` handles N-run variance for generation; Autonoma behavioral E2E sits above pipeline to verify rendered feature still works.

## Key Patterns / Techniques (table or bullets)

| Pattern | How it works (from raw) | File in repo |
|---------|-------------------------|--------------|
| **Retrieval Assertion Gate** | After retriever: check known-correct chunk in top-k, rank, context precision (relevant / retrieved) and recall (relevant retrieved / all relevant) | `tests/test_retrieval.py` |
| **Generation Assertion Gate** | Given fixed context: faithfulness (claims entailed by chunks) + answer relevancy (does answer address question); claim-level decomposition then aggregate | `tests/test_generation_ragas.py`, `tests/test_generation_deepeval.py` |
| **Refusal gate** | Adversarial subset: corpus truly cannot answer → assert generator refuses/hedges instead of inventing | `eval_set/eval_set.json` (tagged `adversarial`) + retrieval/generation tests |
| **Eval-set construction loop** | Sample own index → LLM draft Q+A → human review (mandatory) → deduplicate real user queries → add unanswerable set; 20-50 curated > 500 synthetic | `scripts/build_eval_set.py` |
| **Shared fixture layer** | One corpus, one eval-set, one retriever instance for all test files | `tests/conftest.py` |
| **Mean-gated thresholds** | Mean across eval set vs threshold; 5 runs / 4-pass floor for generation; single-example failure never fails build alone | `lib/repeat_and_threshold.py` |
| **CI as pipeline gate only** | PR gate scores pipeline (grounded, relevant); product surface (citation link, streaming truncation, fallback UI) out of scope — explicit boundary | `.github/workflows/rag-tests.yml` |

> Retrieval is deterministic (fixed index → same chunks); generation is sampled — that determinism split is why two gates, not one score, are required.

## Relevance to QA/QE (table QA Action)

| QA Concern | Action |
|------------|--------|
| **Wrong RAG answer, unknown culprit** | Gate retrieval and generation separately; route retrieval red to chunking/embeddings/top-k/reranking, generation red to prompt/threshold/refusal |
| **End-to-end score hides root cause** | Replace single pass/fail with two aggregates; keep retrieval gate offline/fast, generation gate N-run/LLM-judge |
| **No eval set / benchmark drift** | Build eval set from own docs + logs via `build_eval_set.py`; keep 20-50 reviewed; stale set = silent pass — assign owner |
| **Flaky faithfulness in CI** | Never gate on single generation verdict; N=5, threshold on mean; pin judge model version, temperature 0, treat judge disagreement as rubric signal |
| **Green pipeline, broken feature** | Add behavioral E2E above pipeline: citation resolves, answer renders, fallback shown, follow-up keeps context — Autonoma Planner/Executor layer |
| **Threshold guessing** | Measure baseline on trusted version; set floor below it; "did this change make it worse" not "is it perfect" |

## Critical Analysis (Strengths/Gaps)

**Strengths:**
- Two-surface framing is immediately actionable — table of fix levers (chunking vs prompt) prevents the common "tune prompt when retriever is wrong" loop.
- Eval-set builder closes the gap most RAG guides skip; script + reviewed-set shape + adversarial subset make "build your own" reproducible, not hand-wavy.
- Dual-library coverage (Ragas dataset-level + DeepEval case-level) lets teams pick workflow shape without rewriting assertion logic.
- Explicit boundary statement (pipeline gate vs feature gate) avoids green-harness/false-confidence confusion.

**Gaps:**
- Mean-only gating can hide per-query regression (one critical question drops while mean holds) — no per-critical-query floor suggested.
- Claim-decomposition rubric details and judge calibration delegated to linked hallucination guide; not self-contained for generation gate setup.
- No guidance on chunk-ID pinning after re-index or embedding-model version pinning beyond "fixed index" note — silent vector-space split undetected if not enforced.
- Diffs Agent upkeep for behavioral layer described at product level, not as portable harness for own pipeline.

## Worked Example (from raw)

- **Refund-window Slack screenshot**: bot wrong with confident tone — without two gates, team cannot tell if retriever returned wrong chunk or generator ignored correct one.
- **Retrieval failure**: right question, wrong chunks → fix chunking/embeddings/top-k/reranking; generation failure: right chunks, unsupported claim → fix prompt/threshold/refusal.
- **Small trusted set**: 20-50 reviewed examples where every red is investigated beats 500 synthetic where red is shrugged off as noise.
- **N-run generation gate**: mean across set, thresholded; single ungrounded sentence inside solid answer caught by claim-level split, missed by whole-answer score.
- **Pipeline vs feature**: 100% faithfulness can still ship citation 404, truncated streaming, blank fallback div, or lost follow-up context — behavioral layer's catch.

## FAQ Highlights (from raw)

- Test retrieval and generation separately; aggregate mean vs threshold; build eval set from own docs (20-50 curated > 500 synthetic).
- Retrieval deterministic (same index + query → same chunks); generation non-deterministic → N-run gate.
- 20-50 reviewed examples is enough to start; each must be defensible individually.
- Reference-free faithfulness needs only retrieved context + answer (scales to live traffic); precision/recall needs labeled chunk IDs.
- CI gate proves grounded answer; behavioral E2E proves answer rendered correctly in product — neither substitutes for the other.

## Reuse Checklist

- Clone `Autonoma-Tools/how-to-test-a-rag-pipeline`; run `scripts/build_eval_set.py` sampling own index; review every entry; tag adversarial.
- Keep `tests/conftest.py` fixture layer so retrieval and both generation suites share one corpus/eval-set/retriever.
- Wire `tests/test_retrieval.py` offline (no LLM) and `tests/test_generation_*.py` with N=5; gate on mean, not single example.
- Add `.github/workflows/rag-tests.yml` on every PR; set separate thresholds for retrieval vs generation; pin judge model.
- When gate fails, check retrieval first (index rebuild, chunking, embedding bump, top-k) before touching prompt.

## Cross-links

- Retrieval deep dive: [RAG Retrieval](autonoma-rag-retrieval-2026.md) — hit-rate, MRR, vector-search accuracy, labeled set
- Metrics deep dive: [RAG Evaluation Metrics](autonoma-rag-evaluation-metrics-2026.md) — 4 metrics (faithfulness, relevancy, precision, recall) split by surface
- Hallucinations: [How to Test for AI Hallucinations](autonoma-hallucinations-2026.md) — claim decomposition + reference vs reference-free + judge
- Non-determinism: [Non-Deterministic Outputs](autonoma-non-deterministic-outputs-2026.md) — N-run, threshold, practitioner rule
- CI wiring: [LLM Evals in CI/CD](autonoma-llm-evals-cicd-2026.md) — two-speed pipeline, baseline±tolerance, nightly silent-drift catch
- Feature gate: [QA a Generative AI Feature](autonoma-qa-ai-feature-2026.md) — pipeline gate + behavioral E2E + rollout
- Tool/agent: [Testing Tool Calls](autonoma-testing-tool-calls-2026.md) — trajectory vs outcome gap mirrors pipeline vs feature gap
- Evidence layer: [AI QA Evidence Layer](ai-qa-evidence-layer-validation-evals-guardrails-telemetry.md) — pipeline eval = model eval, rendering = downstream validation
- Repo: [Autonoma-Tools/how-to-test-a-rag-pipeline](https://github.com/Autonoma-Tools/how-to-test-a-rag-pipeline)

## Reuse Notes

- Start behavioral probe on one rendered field (citation href resolves, answer not truncated) alongside pipeline gate — fastest proof that grounded text actually helps user.

---
*Ingested: 2026-08-31*

# How to Build a RAG Evaluation Framework in 4 Metrics

**Source:** https://getautonoma.com/blog/rag-evaluation-metrics
**Date:** 2026-07-28
**Tags:** #autonoma #rag-evaluation #rag-testing #ragas #deepeval
**Raw:** [autonoma-rag-evaluation-metrics-2026.md](../raw/autonoma-rag-evaluation-metrics-2026.md)

---

## What It Is (3-5 bullets)

- **4-metric RAG framework for app builders**: faithfulness + answer relevancy (generation side) and context precision + context recall (retrieval side) — the minimal set that actually changes a ship decision, replacing 18-20-item catalogs (Tom Piaggio, Autonoma, 2026-07-28, repo `Autonoma-Tools/rag-evaluation-metrics`).
- **Benchmark built from own corpus, not leaderboards**: 30-50 question-answer pairs sourced from support tickets/sales transcripts/chat logs with chunk-ID-grounded ground truth, versioned alongside code; public benchmarks never predict refund-policy/rate-limit/onboarding performance.
- **Runnable dual-library scoring**: `ragas_eval.py` (dataset-level batch) and `deepeval_eval.py` (case-level pytest) compute same four metrics via LLM-judge claim decomposition; choice is workflow shape, not correctness.
- **Per-metric, repeated-run CI gate**: `tests/test_rag_gate.py` thresholds per metric (faithfulness/recall stricter), 4-of-5 pass rate across reruns to absorb judge variance; `.github/workflows/rag-eval-gate.yml` fails PR when any metric regresses.

## Key Patterns / Techniques (table or bullets)

| Pattern | How it works (from raw) | File in repo |
|---------|-------------------------|--------------|
| **4-metric split by pipeline half** | Precision/recall = retriever handed right chunks; faithfulness/relevancy = generator used them correctly — tells which half to fix | Metric table + diagram |
| **Context recall** | Ground-truth chunk ID appears in retrieved set? Miss = unfixable by prompt; fix is retriever | `ragas_eval.py` / `deepeval_eval.py` |
| **Context precision** | Relevant / retrieved — buries right chunk under noise → generator blends irrelevant details | Same |
| **Faithfulness** | Every claim entailed by retrieved chunks? Catches hallucination-on-top-of-retrieval even when retriever was correct | Same, via claim decomposition |
| **Answer relevancy** | Grounded but off-question? Faithful non-answer passes faithfulness, fails relevancy — why single-metric gating lets complaints through | Same |
| **Own-document benchmark** | Mine tickets/logs for Qs (question-mark heuristic), write ground truth + supporting chunk IDs, dedup, version file with docs | `scripts/extract_questions.py`, `benchmark/rag_benchmark_v3.jsonl` |
| **Per-metric N-run gate** | Separate threshold per metric (no blended average); 4-of-5 across reruns; judge non-determinism treated as pass rate, not noise | `tests/test_rag_gate.py`, `.github/workflows/rag-eval-gate.yml` |

> Blended aggregate hides the failure you need: 95% faithful + 60% relevant → average "fine" while users fail on relevancy.

## Relevance to QA/QE (table QA Action)

| QA Concern | Action |
|------------|--------|
| **Catalog overwhelm (20 metrics, zero gating guidance)** | Start with 4; add 5th only on observed product failure, not blog-list pressure |
| **Demo passes, user phrasing fails** | Source questions from tickets/logs, not team imagination; weirder/shorter/ambiguous real phrasing is the regression |
| **Wrong fix (prompt tweak when retrieval missed chunk)** | Read metric half: precision/recall red → fix retriever (chunking, embeddings, top-k, rerank); faithfulness/relevancy red → fix prompt/refusal |
| **Stale benchmark vs changing corpus** | Commit benchmark into pipeline repo; bump version when source doc edited/removed; treat stale ground truth as benchmark bug |
| **Dashboard nobody checks** | Make gate fail the build on PR, not a chart; per-metric threshold + repeated-run pass rate; disabled gate worse than none |
| **Retrieval vs generation conflation** | Keep two halves distinct: context precision/recall needs chunk IDs; faithfulness/relevancy need only context+answer (reference-free, scales to live traffic) |

## Critical Analysis (Strengths/Gaps)

**Strengths:**
- Scope correction is decisive — narrows research-grade catalogs to app-builder decision surface and gives "add fifth only on observed failure" rule.
- Benchmark construction is the most-prescriptive section across RAG guides: log-mining heuristic, chunk-ID grounding requirement, versioning discipline, and size guidance (30-50 > 0 while waiting for perfect).
- Per-metric threshold + 4-of-5 rerun insight directly addresses why gates get disabled (blended average hides relevancy, single-run variance disables gate within a sprint).
- Dual-library stance (Ragas vs DeepEval = batch vs case shape) saves rewrite anxiety; switching cost framed as afternoon, not rewrite.

**Gaps:**
- 4-metric threshold numbers not prescribed beyond "faithfulness/recall stricter" — team must still derive own bars empirically without starter defaults shown in prose (only retrieval doc gives numbers).
- Benchmark size 30-50 asserted as sufficient without power analysis; coverage of tail queries (adversarial/unanswerable) only hinted, not wired into this framework's gate.
- Token cost/latency of repeated judge calls not quantified; no split between fast pre-merge vs nightly re-score.
- Behavioral gap (citation link, field wiring, fallback rendering) correctly scoped out but example of how Autonoma plugs in is product-level, not portable recipe.

## Worked Example (from raw)

- **Demo vs reality**: 3 demo questions cited correctly; one off-script user question → fluent confident answer citing doc that never said claimed fact → prompt tweak loop fails because eval never had 4-metric benchmark to show it wasn't a prompt problem.
- **Contrast pair**: retriever correct + generator invented fact = faithfulness fail; retriever correct + grounded off-topic answer = relevancy fail (passes faithfulness) — gating only one leaks the other.
- **Mining**: week's support tickets with `?` → dedup/skim → stronger seed set in an afternoon than team brainstorm in a week; plus LLM-generated Qs per chunk with human confirm.
- **Grounding record**: per question, record supporting chunk IDs — without it, precision/recall uncomputable; with it, both retrieval and generation halves testable.
- **Gate math**: aggregate blended score hides failure; per-metric gate would fail PR on relevancy alone; 4-of-5 absorbs judge variance while 2-of-5 over a week signals real prompt/model/context drift.

## FAQ Highlights (from raw)

- Framework = 4 metrics + own-document benchmark + per-metric thresholds wired into CI on every PR (not one-off report).
- Ragas = dataset/batch shape, DeepEval = pytest/case shape; both use claim-decomposition judge — workflow shape decides.
- 30-50 curated pairs beats 100 debated for six weeks and beats zero while waiting for "proper" dataset — extend as gaps show.
- Benchmark without chunk IDs loses retrieval half — still can score faithfulness/relevancy reference-free.
- Gate on separate thresholds, repeated runs (4-of-5), fail build per metric; a gate failing on normal variance gets disabled within a sprint.

## Reuse Checklist

- Fork `Autonoma-Tools/rag-evaluation-metrics`; point `benchmark/rag_benchmark_v3.jsonl` at own docs; keep schema Q + ground truth + chunk IDs.
- Run `scripts/extract_questions.py` on exported support logs; human-review each before grading; add 10-20% adversarial if guardrail-relevant.
- Copy `ragas_eval.py` or `deepeval_eval.py` pattern; pin judge model, temperature 0 where allowed; calibrate thresholds per metric on measured baseline.
- Wire `tests/test_rag_gate.py` (per-metric thresholds + 4-of-5) into `.github/workflows/rag-eval-gate.yml` on PR path; block merge when any metric < floor.
- Version benchmark file with pipeline code; on doc edit, update ground truth + bump version; treat stale answer as benchmark bug.

## Cross-links

- Hub: [RAG Pipeline](autonoma-rag-pipeline-2026.md) — two-surface harness that consumes these 4 metrics; Ragas/DeepEval suites + eval-set builder
- Retrieval layer: [RAG Retrieval](autonoma-rag-retrieval-2026.md) — hit-rate, MRR, vector-search accuracy, labeled set for precision/recall
- Hallucinations: [How to Test for AI Hallucinations](autonoma-hallucinations-2026.md) — claim decomposition + judge rubric behind faithfulness
- Non-determinism: [Non-Deterministic Outputs](autonoma-non-deterministic-outputs-2026.md) — N-run sampling, threshold calibration, strict-vs-ambiguous rule
- CI wiring: [LLM Evals in CI/CD](autonoma-llm-evals-cicd-2026.md) — two-speed scheduling, baseline±tolerance, nightly silent-provider catch
- Feature gate: [QA a Generative AI Feature](autonoma-qa-ai-feature-2026.md) — 6-step gate that composes eval + red-team + behavioral
- E2E arc: [How to Test an AI Agent E2E](autonoma-how-to-test-ai-agent-e2e-2026.md) — pipeline score vs product outcome
- Evidence: [AI QA Evidence Layer](ai-qa-evidence-layer-validation-evals-guardrails-telemetry.md) — metric = model eval, citation/field = downstream validation
- Repo: [Autonoma-Tools/rag-evaluation-metrics](https://github.com/Autonoma-Tools/rag-evaluation-metrics)

## Reuse Notes

- Start with 30 benchmark rows covering top sales/support questions; gate deterministically — forensically add rows only after observed failure; smallest trusted set that fails build on real regression wins.

---
*Ingested: 2026-08-31*

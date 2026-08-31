# How to Test for AI Hallucinations: A Code-First Guide

**Source:** https://getautonoma.com/blog/how-to-test-for-ai-hallucinations
**Date:** 2026-07-27
**Tags:** #autonoma #hallucinations #faithfulness #llm-as-judge #rag-testing
**Raw:** [autonoma-hallucinations-2026.md](../raw/autonoma-hallucinations-2026.md)

---

## What It Is (3-5 bullets)

- **Two complementary hallucination checks**: reference-based (semantic similarity vs labeled golden answer, curated regression set) and reference-free (groundedness/faithfulness vs retrieved context, scales to live traffic) — each catches what the other cannot (Tom Piaggio, Autonoma, 2026-07-27, repo `Autonoma-Tools/how-to-test-for-ai-hallucinations`).
- **Claim-decomposition faithfulness harness**: split answer into atomic, independently checkable claims → per-claim entailment against retrieved chunks → aggregate fraction entailed; ships as hand-rolled `lib/faithfulness.py` plus DeepEval `FaithfulnessMetric` and Ragas dataset equivalents.
- **LLM-as-judge factuality rubric**: judge forced to binary entailment per claim with cited supporting chunk, not vague 1-5 "is accurate"; includes calibration and bias notes (verbosity/confidence, same-family blind spot).
- **Repeat-and-threshold + incident-fed regression**: `lib/repeat_and_threshold.py` N-run pass-rate gate (5 runs / 4-pass floor, never single verdict); `fixtures/hallucination_incidents.json` turns every prod miss into a permanent gate; `.github/workflows/hallucination-tests.yml` blocks merge on recurrence.

## Key Patterns / Techniques (table or bullets)

| Pattern | How it works (from raw) | File in repo |
|---------|-------------------------|--------------|
| **Reference-based check** | Compare answer to golden via semantic similarity (not exact match — "refund processed" = "I've processed your refund"), threshold-gated | `tests/test_reference_based_check.py` |
| **Reference-free groundedness** | No label needed: is answer supported by context actually given? Viable on open-ended/live traffic | `tests/test_reference_free_groundedness.py` |
| **Claim decomposition** | No pronouns, no compound "and" — one atomic claim per check; prevents single invented sentence hiding in solid answer | `lib/faithfulness.py` |
| **Faithfulness assertion** | Decompose → per-claim entailment vs chunks → gate on fraction entailed, not unanimous | `tests/test_rag_faithfulness.py` |
| **DeepEval / Ragas shims** | Same entailment behind single call: DeepEval case-level, Ragas batch-level | `tests/test_faithfulness_deepeval.py`, `tests/test_faithfulness_ragas.py` |
| **LLM-as-judge rubric** | Per-claim binary verdict + cited chunk; captures faithfulness and, with rubric care, unsupported extrapolation | `lib/factuality_judge.py`, `tests/test_llm_judge_factuality.py` |
| **N-run pass-rate gate** | 5 runs, 4-pass floor; 5/5→2/5 over week = signal (prompt/model/context drift), not noise; single-run gate = untrustworthy within month | `lib/repeat_and_threshold.py` |
| **Incident regression set** | Each prod hallucination → (question, context, wrong claim, why) as permanent case | `fixtures/hallucination_incidents.json`, `tests/test_hallucination_regression.py` |

> Faithfulness asks "does the context support this?" not "is the context itself correct" — a grounded answer built on wrong retrieved chunk is still a failure, just at retrieval layer.

## Relevance to QA/QE (table QA Action)

| QA Concern | Action |
|------------|--------|
| **Hallucination = vague "AI said wrong thing"** | Classify: ungrounded claim vs factually false vs unsupported extrapolation — choose groundedness vs reference vs judge rubric accordingly |
| **Reference set doesn't scale to prod traffic** | Keep reference-based on high-stakes curated set; add reference-free faithfulness for everything else (needs only context+answer) |
| **Whole-answer score misses buried invention** | Decompose to atomic claims; gate fraction entailed — single ungrounded sentence must fail gate |
| **Vague judge prompt drifts run-to-run** | Enforce binary entailment + cited chunk per claim; calibrate judge against human-labeled set before trusting threshold |
| **Same check passes then fails** | Never gate on single run; N=5, pass-rate threshold; treat judge non-determinism, verbosity bias, same-family blind spot as monitored components |
| **Same hallucination ships twice** | Turn every prod incident into `hallucination_incidents.json` row; gate blocks recurrence — regression set compounds over months |
| **Grounded words, wrong app outcome** | Pair hallucination score with behavioral E2E: did grounded text land correctly (DB row, screen, wrong field/routing) — Autonoma Planner/Executor layer |

## Critical Analysis (Strengths/Gaps)

**Strengths:**
- Reference vs reference-free split is the clearest "when to use which" in Autonoma RAG cluster; scalability table prevents over-investing in labeled set where groundedness suffices.
- Claim-level mechanism is runnable, not named — decomposition + entailment + threshold wired through hand-rolled, DeepEval, and Ragas variants; team can pick without ideology.
- Judge section goes beyond "use LLM-as-judge" to rubric design + calibration + bias catalog — treats judge as component to monitor, not ground truth.
- Regression-set compounding argument ("every incident makes next release harder to break") reframes prod failure as durable asset; CI wiring closes "laptop-only before release" gap.

**Gaps:**
- Ungrounded vs factually-false vs extrapolation taxonomy useful but mapping to threshold choice not quantified — where to set fraction-entailed floor per class.
- Judge bias mitigation (verbosity, confidence, same-family) flagged but no de-bias pattern (e.g., shorten, strip confidence markers, cross-family judge) shown in code.
- Repeated-run cost (5x judge + generator calls per case) not budgeted; no guidance on sampling subset vs full set on per-PR vs nightly.
- Factually-false-yet-grounded case (context itself wrong) acknowledged as out-of-scope for faithfulness but no upstream truth-source check suggested.

## Worked Example (from raw)

- **Restocking-fee bot**: quotes refund policy correctly + invents "$10 restocking fee" nowhere in policy/context/reality — passes tone/latency/JSON checks; only claim-level faithfulness catches it.
- **Metric**: answer with 4 grounded claims + 1 invented → whole-answer score may pass; 4/5 fraction entailed fails threshold if floor 0.9 — demonstrates decomposition value.
- **Judge rubric**: "rate 1-5 accurate" drifts; binary per-claim verdict citing chunk ID produces thresholdable signal — excerpt shown in `lib/factuality_judge.py`.
- **Flake decision tree**: 5 runs, same check intermittently fails → if judge disagreement near boundary, rubric signal not noise — calibrate; if consistent 2/5 after prompt edit, real drift.
- **Compounding set**: prod miss (question + retrieved chunks + wrong "$10 fee" claim) added to `hallucination_incidents.json` → future model bump reintroducing same invention blocks merge automatically.

## FAQ Highlights (from raw)

- Two checks: reference-based (vs golden, semantic similarity) + reference-free (grounded in given context, claim-decomposed faithfulness).
- RAG hallucinations need faithfulness (generation grounded?) separate from retrieval quality (right chunk at all?) — faithful on wrong chunk still fails user.
- Best tools: DeepEval and Ragas both do claim-level faithfulness; rubric > tool choice — forced chunk citation matters more than library.
- Catch before prod: continuous CI with N-run pass rate + incident-fed regression; reference-free scales to live-like inputs without labels.
- Judge reliable only with per-claim binary + cited chunk, calibrated on human labels, run N times with pass-rate — vague 1-5 unreliable, biased to verbose/confident.

## Reuse Checklist

- Clone `Autonoma-Tools/how-to-test-for-ai-hallucinations`; start with `lib/faithfulness.py` decomposition pattern on own domain.
- Implement both `test_reference_based_check.py` (golden set, high-stakes) and `test_reference_free_groundedness.py` (context-only, broad).
- Add `lib/factuality_judge.py` with binary per-claim rubric requiring `chunk_id` citation; calibrate against ~20 human-labeled triples before CI.
- Wrap with `lib/repeat_and_threshold.py` N=5, 4/5 floor; gate on fraction entailed, not single verdict; pin judge version.
- On each prod hallucination, append to `fixtures/hallucination_incidents.json`; wire `tests/test_hallucination_regression.py` + `.github/workflows/hallucination-tests.yml` as required PR check.

## Cross-links

- RAG hub: [RAG Pipeline](autonoma-rag-pipeline-2026.md) — two-surface split where faithfulness is the generation gate
- Retrieval: [RAG Retrieval](autonoma-rag-retrieval-2026.md) — "right chunk" half; faithful on wrong chunk is retrieval failure, not model invention
- Metrics: [RAG Evaluation Metrics](autonoma-rag-evaluation-metrics-2026.md) — faithfulness + relevancy as the generation pair
- Non-determinism: [Non-Deterministic Outputs](autonoma-non-deterministic-outputs-2026.md) — N-run sampling, practitioner rule (strict vs ambiguous), threshold gating
- CI wiring: [LLM Evals in CI/CD](autonoma-llm-evals-cicd-2026.md) — dataset versioning, two-speed pipeline for paid judge calls
- Tool calls: [Testing Tool Calls](autonoma-testing-tool-calls-2026.md) — trajectory vs outcome gap analogous to text-grounded vs app-state-correct
- Feature gate: [QA a Generative AI Feature](autonoma-qa-ai-feature-2026.md) — faithfulness inside 6-step ship sequence
- Guardrails: [Testing Guardrails](https://getautonoma.com/blog/how-to-test-ai-guardrails) — refusal/grounding-adjacent
- Repo: [Autonoma-Tools/how-to-test-for-ai-hallucinations](https://github.com/Autonoma-Tools/how-to-test-for-ai-hallucinations)

## Reuse Notes

- Keep one judge call per claim, not per answer, and log per-claim verdict + cited chunk — makes threshold tuning and failure triage trivial compared to single-score debugging.

---
*Ingested: 2026-08-31*

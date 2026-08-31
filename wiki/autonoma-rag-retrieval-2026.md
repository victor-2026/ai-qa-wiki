# How to Test if RAG Is Retrieving the Right Context

**Source:** https://getautonoma.com/blog/how-to-test-rag-retrieval
**Date:** 2026-07-28
**Tags:** #autonoma #rag-retrieval #rag-testing #information-retrieval
**Raw:** [autonoma-rag-retrieval-2026.md](../raw/autonoma-rag-retrieval-2026.md)

---

## What It Is (3-5 bullets)

- **Retrieval isolated from generation**: pure IR test — query → ranked chunk IDs, no LLM call — fast, deterministic, ms on every commit; generation's fluent summary of wrong chunk no longer masks retriever bug (Tom Piaggio, Autonoma, 2026-07-28, repo `Autonoma-Tools/how-to-test-rag-retrieval`).
- **Four IR metrics with distinct catch**: hit rate/recall@k (chunk in top-k?), MRR (how high?), context precision (relevant / retrieved, noise dilution), context recall (needed info actually retrieved, partial-answer catch) — each maps to a different fix.
- **Labeled test-set mining, not labeling team**: `tests/fixtures/labeled_queries.json` with 44 query→expected-chunk-ID pairs mined from production logs, support tickets (linked doc = label), and LLM-draft Qs confirmed by human — 30-50 is enough to gate.
- **CI regression gate with ratchet**: `tests/test_retrieval_regression.py` aggregates across set, thresholds per metric set below measured baseline then ratcheted; `.github/workflows/retrieval-regression.yml` fails build before wrong chunk becomes confident answer.

## Key Patterns / Techniques (table or bullets)

| Pattern | How it works (from raw) | File in repo |
|---------|-------------------------|--------------|
| **Isolation wrapper** | `retrieve(query) -> List[chunk_id]` ranked — thin shim over any vector store, no prompt/generator/parsing | `src/retriever.py` |
| **Hit rate / recall@k** | Binary per query (chunk in top-k?), averaged; k=5 starting floor 0.80; "hit at 9 but window fits 3" still functionally invisible | `src/metrics/hit_rate.py` |
| **MRR** | Mean of 1/rank of first relevant; 1.0 at rank 1, ~0.11 at rank 9; catches "technically hit, practically buried" | `src/metrics/mrr.py`, origin TREC QA track |
| **Context precision + recall** | Precision = share retrieved that is relevant (8 noise + 2 relevant = dilution + blending risk); recall = share needed that was retrieved (1/3 paragraphs = partial confident answer) | `src/metrics/context_precision_recall.py` |
| **Vector-search accuracy checks** | Same query, same top-k, direct ID set comparison; surfaces embedding-version mismatch, chunk split, ANN approximation, metadata-filter exclusion | `src/retriever.py` + metrics |
| **Exact-ID blind spot** | Semantic search bad at `invoice #48291` — nearby language clusters, literal ID has no weight; needs hybrid/keyword layer, tested via exact-match queries | Labeled set design note |
| **Labeled set mining** | Logs > tickets > LLM-draft+human-confirm (30s each, avoids circular retriever≅generator agreement) | `tests/fixtures/labeled_queries.json` |

> Hit rate tells you the chunk existed. MRR tells you whether it mattered. Precision/recall tell you whether the set was clean and complete.

## Relevance to QA/QE (table QA Action)

| QA Concern | Action |
|------------|--------|
| **Prompt-tuning loop on retrieval bug** | Isolate retrieval first; if gate red, fix retriever (chunking, embeddings, top-k/reranking) — do not touch prompt |
| **"Seemed fine when I tried it"** | Replace anecdotal probe with labeled set + 4-metric gate on every commit; ms cost, no API key |
| **Hit-rate green but answer wrong** | Add MRR + precision/recall: buried rank, noisy context, or partial answer each passes hit-rate alone |
| **Exact-ID query returns wrong doc** | Add keyword/hybrid path; include exact-ID queries (order/invoice/account numbers) in labeled set on purpose |
| **Threshold never green → gate disabled** | Measure current baseline honestly; set floor a few points below it; ratchet up over time — regression gate, not perfection gate |
| **Green retrieval, broken feature** | Retrieval correct ≠ user saw correct thing (wrong panel, 404 citation, truncated stream, missing empty state) → behavioral E2E above metrics (Autonoma Planner/Executor) |
| **Labeled data never started** | Mine 30-50 from logs/tickets today; grow by adding a case on every prod miss — do not wait for labeling team |

## Critical Analysis (Strengths/Gaps)

**Strengths:**
- Reframing retrieval as classic IR (decades-old metrics, TREC provenance) is clarifying — legitimizes deterministic, cheap assertions and explains why LLM-judge is unnecessary here.
- MRR vs hit-rate diagram plus exact-ID invoice example makes rank-awareness concrete; team stops treating "in top-10" as success.
- Labeled-set mining playbook removes the common blocker ("need labeling team") with three ranked sources and human-confirm guardrail against circularity.
- Regression-threshold philosophy (baseline minus a few points, ratchet) plus non-determinism handling (pin embedding version, ANN caveat) prevents permanently-red gate.

**Gaps:**
- Threshold table (0.80/0.60/0.70/0.75) flagged as opinionated but no calibration guidance per domain/query difficulty — team still guesses.
- ANN index ceiling (<100% by design) and re-index atomicity not paired with a concrete double-index or shadow-score recipe.
- Hybrid/keyword layer for exact-ID recommended but not scaffolded — no hybrid scorer or query-classifier stub shown in repo.
- Transport from retrieval success to UI rendering failure delegated to Autonoma product; no generic behavioral-assertion sketch for retriever-only teams.

## Worked Example (from raw)

- **Misdiagnosed layer**: RAG wrong answer → team rewrites system prompt 3x; retriever pulled wrong chunk, generator faithfully summarized garbage — retrieval test would have failed before prompt loop started.
- **Metric routing**: low hit rate → embedding/chunking/index; low MRR + decent hit rate → ranking/reranking; low precision + fine recall → tighten k/reranker; low recall + fine precision → chunk boundaries split answer.
- **Isolation payoff**: strip generator → deterministic comparison of ranked chunk IDs vs expected set; no temperature, no judge drift, no cents-per-run.
- **Vector failure cases**: index-time vs query-time embedding version split (half index in different space); chunk split across two pieces; ANN (HNSW/IVF) approximate by design; tenant metadata filter silently excludes correct chunk.
- **Red-build triage**: retrieval metric failure = upstream of generator; check index rebuild, embedding bump, chunking change, new-doc metadata tags before looking at generation.

## FAQ Highlights (from raw)

- 30-50 labeled query→chunk pairs enough to gate CI; grow by adding case on each prod failure.
- Starting bars: hit rate 0.80+ at k=5, MRR 0.60+, precision 0.70+, recall 0.75+ — floors, then replace with measured baseline.
- Test retrieval separately first (fast/deterministic, no LLM), then layer end-to-end pipeline tests for faithfulness/relevancy.
- Dense vectors unreliable for exact-ID/keyword queries — add keyword/hybrid layer and test it with literal-ID queries.
- Without labeled set, mine logs/tickets or LLM-draft+human-confirm; unlabeled eval cannot compute precision/recall that needs chunk IDs.
- Mismatched embedding versions most common wrong-chunk cause; chunk splits, ANN trade-off, bad metadata tags follow.

## Reuse Checklist

- Clone `Autonoma-Tools/how-to-test-rag-retrieval`; adapt `src/retriever.py` wrapper to own vector store to return ranked `chunk_id` list.
- Build `tests/fixtures/labeled_queries.json` with 30-50 entries: query, expected chunk ID(s), source tag (log/ticket/llm-confirmed); include 5+ exact-ID queries.
- Implement `src/metrics/hit_rate.py`, `mrr.py`, `context_precision_recall.py` and `tests/test_retrieval_regression.py` aggregating per metric; assert vs floor below baseline.
- Add `.github/workflows/retrieval-regression.yml` on every push/PR; pin embedding model version in test config; fail build on any metric below floor.
- On red, route by metric: hit rate→embeddings/chunking/index; MRR→reranker; precision→k/noise; recall→chunk splits/metadata; check re-index completeness.

## Cross-links

- Hub: [RAG Pipeline](autonoma-rag-pipeline-2026.md) — two-surface harness where this retriever gate is the left half
- Metrics: [RAG Evaluation Metrics](autonoma-rag-evaluation-metrics-2026.md) — 4-metric app-builder framework (this page's metrics in context)
- Hallucinations: [How to Test for AI Hallucinations](autonoma-hallucinations-2026.md) — faithfulness layer when generator drifts from correct chunk
- Non-determinism: [Non-Deterministic Outputs](autonoma-non-deterministic-outputs-2026.md) — sampling/threshold handling for generation side (retrieval stays deterministic)
- CI wiring: [LLM Evals in CI/CD](autonoma-llm-evals-cicd-2026.md) — same ratchet-the-floor pattern applied to generation evals
- Feature gate: [QA a Generative AI Feature](autonoma-qa-ai-feature-2026.md) — where retrieval gate sits in 6-step ship sequence
- Vector DB: [Vector Databases in Fintech](vector-databases-fintech-2026.md) — HNSW/IVF and retrieval trade-offs
- RAGAS: [RAG Evaluation Using Ragas](rag-evaluation-ragas.md) — Ragas scoring context
- Repo: [Autonoma-Tools/how-to-test-rag-retrieval](https://github.com/Autonoma-Tools/how-to-test-rag-retrieval)

## Reuse Notes

- Keep a pinned "golden index snapshot" for retrieval CI so re-index or embedding bump shows as metric regression, not as flaky generation.

---
*Ingested: 2026-08-31*

# Amazon Science: Ground Truth Is a Process, Not a Dataset (2026-06-03)

**Author:** Venkatesh Saligrama (Amazon Scholar, Boston University professor, IEEE Fellow); ack: Yukun Huang, Leonardo F. R. Ribeiro, Momchil Hardalov, Markus Dreyer
**Source:** https://www.amazon.science/blog/ground-truth-is-a-process-not-a-dataset
**Paper:** arXiv:2603.05912 + DeepFact-Bench (shared test set) + DeepFact-Eval (fact-checking system)
**Context:** Benchmark methodology for factuality of long AI-generated research reports. Core result: PhD experts as one-shot labelers reach only 60.8% on hidden known answers; the SAME experts as auditors in audit-then-score loop reach 90.9% across 4 rounds. Direct hit for our golden-dataset design (labels must be debatable artifacts, not frozen truth) and attestor role (human audits disputed claims, doesn't label from blank page). Pairs with judges-agree piece (who judges the judges) and CIGE evidence rules.
**Fetched:** 2026-09-23 via webfetch, substance below (nav/footer stripped).

---

## Problem

Deep-research reports synthesize many sources per sentence; claims depend on surrounding context and compare assertions no single source makes. Existing fact-checkers match claim-to-quote and break here. Amazon AGI first tried building a stronger checker - then discovered building the BENCHMARK was at least as hard: PhD specialists (CS, control theory, education, public health, environmental eng.) scored 60.8% unassisted on hidden known-answer claims. Cause is task difficulty (long-context reading, cross-document synthesis), not expertise. Lesson: model-vs-benchmark disagreement must not default to model failure - sometimes the benchmark is ambiguous, incomplete, or wrong.

## Protocol: audit-then-score

Disagreeing checker becomes a CHALLENGER: submits concrete evidence + written rationale why the human answer is wrong. An AUDITOR (human expert) compares challenger evidence directly against the benchmark's original rationale - no labeling from scratch. Stronger case wins; benchmark revised BEFORE scoring. DeepFact-Eval: reads full report context, plans literature searches, summarizes retrieved docs, asks follow-ups on missing details, outputs verdict + written explanation.

## Results

4 audit rounds: hidden-set accuracy 60.8% → 90.9%. DeepFact-Eval (GPT-4.1) on DeepFact-Bench: 83.4% vs 58.5% best traditional fact-checker vs 69.1% strong prior deep-research system.

## Thesis: evaluation as evolving infrastructure

As AI approaches human expertise, one-shot human answers stop sufficing. Benchmarks need auditing, revision, calibration, periodic revalidation - ongoing collaboration of humans, models, and surfaced evidence. Ground truth is a process.

## Use for us

- Golden-dataset doctrine: seed labels are version 0, challenger evidence + auditor ruling is the update mechanism; store rationale per label (benchmark's "original rationale" = our evidence artifact).
- Attestor economics: auditing disputes is far more reliable (90.9%) than labeling from blank (60.8%) - staff the human gate as AUDITOR, not labeler.
- DeepFact-Eval architecture (context read → search plan → summarize → follow-up → verdict+explanation) = template for verdict-agent loop.
- Cross-links: judges-agree (judge dependence), CIGE (evidence bar for pass), building-trust (model-breaking datasets need the same audit loop).

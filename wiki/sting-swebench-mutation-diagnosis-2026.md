---
source: "sting-swebench-2026.md"
ingested: "2026-10-01"
title: "STING: Mutation-Guided Diagnosis of SWE-bench Regression Suites"
type: article
tags: [mutation-testing, benchmark, swebench, diagnosis]
---

## Summary

STING diagnoses behavioral gaps in SWE-bench Verified through surviving program variants. 77% of 500 instances contain at least one surviving variant, showing under-constrained tests are widespread. Augmented tests significantly change repair agent rankings.

## Key Findings

| Metric | Value |
|--------|-------|
| SWE-bench instances with survivors | 77% (385/500) |
| LLM-based mutation instances | 380 (1915 variants) |
| Coverage drop with stronger tests | 6-9% |
| Agent ranking changes | Significant |

## Method

1. Apply operator-based and LLM-based mutation to 500 instances
2. Identify surviving variants (behavioral gaps)
3. Generate targeted tests to kill survivors
4. Compare original vs augmented test suites
5. Evaluate impact on repair agent rankings

## Key Insights

- SWE-bench tests are systematically under-constrained
- 77% of accepted patches are behaviorally incorrect
- Mutation-guided augmentation reveals hidden gaps
- Stronger tests change agent rankings significantly
- LLM-based mutation finds more gaps than operator-based alone

## See also

- [[wiki/mutgen-mutation-guided-test-generation-2025]] - Mutation-guided generation
- [[meta-ach-mutation-guided-llm-2025]] - Meta ACH
- [[witness-predictive-mutation-testing-2026]] - Predictive MT
- [[llmorpheus-llm-mutation-testing-2025]] - LLM-based mutation

---
*Source: [raw/sting-swebench-mutation-diagnosis-2026.md](../raw/sting-swebench-mutation-diagnosis-2026.md) · 2026*

# STING: Mutation-Guided Diagnosis and Augmentation of Regression Suites

**Source:** https://arxiv.org/html/2604.01518v1
**Published:** 2026

## Summary

STING is a variant-guided framework that diagnoses behavioral gaps through surviving program variants and synthesizes targeted tests to eliminate those gaps. Applied to SWE-bench Verified, it reveals that 77% of instances contain at least one surviving program variant, showing under-constrained tests are widespread.

## Key Results

- **77% of 500 SWE-bench Verified instances** contain at least one surviving variant
- **LLM-based mutation** accounts for the majority (380 instances, 1915 variants)
- **Operator-based mutation** adapted from mutmut, MutPy, Cosmic Ray
- **Augmented tests** provide more reliable comparison between repair agents
- **Coverage drop:** Atlassian Rovo Dev 76.80% -> 68.80% (-8%) with stronger tests
- **Agent ranking changes:** Significant reordering when evaluated with augmented tests

## Method

1. Apply operator-based and LLM-based mutation to all 500 SWE-bench instances
2. Identify surviving variants (behavioral gaps)
3. Generate targeted tests to kill survivors
4. Compare original vs augmented test suites
5. Evaluate impact on repair agent rankings

## Key Insights

- SWE-bench tests are systematically under-constrained
- 77% of patches accepted on SWE-bench Verified are behaviorally incorrect
- Mutation-guided augmentation reveals hidden behavioral gaps
- Stronger tests change agent rankings significantly
- LLM-based mutation finds more gaps than operator-based alone

## Implications

- Benchmark contamination is measurable via mutation testing
- Mutation-guided test augmentation improves benchmark quality
- Current AI repair evaluations may be unreliable due to weak tests
- Mutation testing can diagnose and fix benchmark weaknesses

## Related

- Mutation testing for benchmark evaluation
- LLM-based mutation (LLMorpheus)
- SWE-bench Verified quality assessment
- Mutation-guided test generation (MUTGEN, Meta ACH)
- Property-Based Mutation Testing

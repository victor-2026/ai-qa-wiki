---
source: "mutgen-2025.md"
ingested: "2026-10-01"
title: "MUTGEN: Mutation-Guided Unit Test Generation with LLM"
type: article
tags: [mutation-testing, llm, ai, test-generation]
---

## Summary

MUTGEN incorporates mutation feedback directly into LLM prompts for test generation. Evaluated on 204 subjects, it significantly outperforms EvoSuite and vanilla prompt-based strategies in mutation score. Key insight: LLMs need mutation feedback to generate boundary-value tests.

## Key Results

| Metric | Value |
|--------|-------|
| Subjects | 204 |
| Baselines | EvoSuite, vanilla LLM |
| Finding | 100% coverage can yield 4% mutation score |
| Fixing mechanism | +13% mutation score increase |

## Method

1. Extract mutation feedback (live and uncovered mutants)
2. Integrate with source code in prompt
3. Iterative generation with refinement
4. Automatic fixing of failing tests

## Key Insights

- LLMs focus on representative invalid inputs, miss boundary values
- Mutation feedback guides toward boundary testing
- Iterative refinement is key to high-quality test generation
- Mutation score is more reliable than coverage for LLM-generated tests

## See also

- [[meta-ach-mutation-guided-llm-2025]] - Meta's industrial deployment
- [[llmorpheus-llm-mutation-testing-2025]] - LLM-based mutant generation
- [[intent-based-mutation-testing-2025]] - Mutating programming intents
- [[sting-swebench-mutation-diagnosis-2026]] - Mutation-guided diagnosis

---
*Source: [raw/mutgen-2025.md](raw/mutgen-mutation-guided-test-generation-2025.md) · 2025*

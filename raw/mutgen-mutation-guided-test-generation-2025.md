# MUTGEN: Mutation-Guided Unit Test Generation with a Large Language Model

**Source:** https://arxiv.org/abs/2506.02954
**Authors:** Guancheng Wang, Qinghua Xu, Lionel C. Briand, Kui Liu
**Published:** 2025 (revised August 2025)

## Summary

MUTGEN is a mutation-guided, LLM-based test generation approach that incorporates mutation feedback directly into the prompt. Evaluated on 204 subjects from two benchmarks, MUTGEN significantly outperforms both EvoSuite and vanilla prompt-based strategies in terms of mutation score.

## Key Results

- **Subjects:** 204 from two benchmarks
- **Baselines:** EvoSuite (search-based), vanilla prompt-based LLM generation
- **Metric:** Mutation score (primary), code coverage, execution success rate
- **Finding:** Some test suites achieve 100% coverage but only 4% mutation score

## Method

1. **Mutation feedback extraction:** Before generation, MUTGEN extracts mutation feedback from mutation reports (live and uncovered mutants)
2. **Prompt construction:** Mutation feedback integrated with source code to guide LLM
3. **Iterative generation:** Tests generated, executed against mutants, feedback refines next iteration
4. **Fixing mechanism:** Automatically repairs failing test cases by invoking LLM with error context

## Key Insights

- LLM-generated tests tend to focus on representative invalid inputs and valid values far from boundaries
- Example: LLM generates `assertFalse(validDate("04-00-2025"))` but misses `assertTrue(validDate("04-01-2025"))` needed to kill boundary mutant
- Mutation feedback guides LLM toward boundary values and edge cases
- Fixing mechanism resulted in 13% mutation score increase in one example

## Implications

- Mutation score is a more reliable quality signal than coverage for LLM-generated tests
- Iterative refinement with mutation feedback is key to high-quality test generation
- LLMs need guidance to generate boundary-value tests (mutation feedback provides this)

## Related

- Meta ACH (FSE 2025) - mutation-guided test generation at Meta
- LLMorpheus (TSE 2025) - LLM-based mutant generation
- Intent-Based MT (Mutation 2025) - mutating programming intents
- "Does mutation testing improve testing practices?" (Just et al., ICSE 2021)

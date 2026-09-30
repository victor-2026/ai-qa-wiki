# Intent-Based Mutation Testing: From Naturally Written Programming Intents to Mutants

**Source:** https://conf.researchr.org/details/icst-2025/mutation-2025-papers/5/Intent-Based-Mutation-Testing-From-Naturally-Written-Programming-Intents-to-Mutants
**Authors:** Asma Hamidi, Ahmed Khanfir, Mike Papadakis (University of Luxembourg)
**Published:** Mutation 2025 (ICST 2025 Workshop), April 1, 2025

## Summary

Intent-based mutation testing generates mutations by changing the programming intents implemented in programs under test. Unlike traditional mutation testing which changes how programs are written (syntax), intent mutation changes the behavior of programs by producing mutations that implement slightly different intents than the original program.

## Key Results

- **Subjects:** 29 programs
- **Method:** LLMs mutate programming intents and transform them into mutants
- **Finding:** 55% of intent-based mutations are not subsumed by traditional mutations
- **Quality:** Syntactically complex, semantically diverse, quite different from traditional mutations

## Method

1. Identify programming intents in source code
2. LLM generates alternative intents (corner cases, misunderstandings of specifications)
3. Alternative intents transformed into executable mutants
4. Traditional test suite executed against intent-mutants

## Key Insights

- Programming intents represent possible corner cases and misunderstandings of program behavior (specifications)
- Intent-based mutations capture different fault classes than syntax-based mutation
- Since intents can be implemented in different ways, intent-based MT generates diverse and complex mutations
- Directs testing toward intent variants of program behavior/specifications
- Powerful complement to traditional (syntax-based) mutation testing

## Implications

- Bridges gap between specification-level and code-level mutation testing
- LLMs understand intent, not just syntax
- 55% non-subsumption rate shows traditional operators miss entire fault classes
- Can be combined with traditional mutation for comprehensive coverage

## Related

- LLMorpheus (TSE 2025) - LLM-based mutant generation
- Meta ACH (FSE 2025) - mutation-guided LLM test generation
- MUTGEN (2025) - mutation feedback in prompts
- Property-Based Mutation Testing (2023) - mutation against properties/specifications

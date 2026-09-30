---
source: "intent-based-mt-2025.md"
ingested: "2026-10-01"
title: "Intent-Based Mutation Testing: Mutating Programming Intents via LLM"
type: article
tags: [mutation-testing, llm, ai, intent]
---

## Summary

Intent-based mutation testing generates mutations by changing the programming intents implemented in programs. Unlike traditional mutation (syntax changes), intent mutation changes behavior by producing mutations that implement slightly different intents. 55% of intent-based mutations are not subsumed by traditional mutations.

## Key Results

| Metric | Value |
|--------|-------|
| Programs | 29 |
| Non-subsumed by traditional | 55% |
| Quality | Syntactically complex, semantically diverse |

## Method

1. Identify programming intents in source code
2. LLM generates alternative intents (corner cases, misunderstandings)
3. Transform alternative intents into executable mutants
4. Execute traditional test suite against intent-mutants

## Key Insights

- Programming intents represent corner cases and specification misunderstandings
- Captures different fault classes than syntax-based mutation
- LLMs understand intent, not just syntax
- Powerful complement to traditional mutation testing

## See also

- [[llmorpheus-llm-mutation-testing-2025]] - LLM-based mutant generation
- [[meta-ach-mutation-guided-llm-2025]] - Meta's industrial deployment
- [[wiki/mutgen-mutation-guided-test-generation-2025]] - Mutation feedback in prompts
- [[pytation-python-mutation-operators-2026]] - Python-specific operators

---
*Source: [raw/intent-based-mutation-testing-2025.md](../raw/intent-based-mutation-testing-2025.md) · Mutation 2025 (ICST)*

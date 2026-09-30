---
source: "llmorpheus-tse-2025.md"
ingested: "2026-10-01"
title: "LLMorpheus: Mutation Testing Using Large Language Models"
type: article
tags: [mutation-testing, llm, ai, javascript]
---

## Summary

LLMorpheus is a mutation testing tool for JavaScript that uses Large Language Models to generate mutants instead of relying on a fixed set of mutation operators. Introduced placeholders in source code are replaced by LLM-suggested code fragments, producing mutants that resemble real bugs beyond what traditional tools can generate.

## Key Findings

| Metric | Value |
|--------|-------|
| Cost | $3.62 for 13 npm packages |
| Surviving mutants (not equivalent) | 63.2% |
| Equivalent mutants | 8.5% |
| Near-equivalent | 9.7% |
| Stability (temp 0.0) | 89-99% across 5 runs |

## Method

1. Placeholders introduced at designated locations in source code
2. LLM prompted to suggest replacements
3. Modified StrykerJS executes mutants
4. Interactive web report for inspection

## Implications

- LLMs generate diverse, realistic mutants beyond fixed operator sets
- Cost is practical for real-world use
- Complements traditional mutation testing by covering different fault classes
- Opens door to intent-based mutation testing

## See also

- [[meta-ach-mutation-guided-llm-2025]] - Meta's industrial deployment
- [[wiki/mutgen-mutation-guided-test-generation-2025]] - Mutation feedback in prompts
- [[intent-based-mutation-testing-2025]] - Mutating programming intents
- [[mutation-testing-vs-code-coverage-autonoma]] - General mutation testing concepts

---
*Source: [raw/llmorpheus-llm-mutation-testing-2025.md](../raw/llmorpheus-llm-mutation-testing-2025.md) · IEEE TSE 2025*

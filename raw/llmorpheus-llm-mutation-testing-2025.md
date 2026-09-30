# LLMorpheus: Mutation Testing Using Large Language Models

**Source:** https://arxiv.org/abs/2404.09952
**Authors:** Frank Tip, Jonathan Bell, Max Schaefer
**Published:** IEEE Transactions on Software Engineering, Vol. 51, June 2025, pp. 1645-1665
**DOI:** 10.1109/TSE.2025.3562025

## Summary

LLMorpheus is a mutation testing tool for JavaScript that uses Large Language Models to generate mutants instead of relying on a fixed set of mutation operators. The technique introduces placeholders at designated locations in a program's source code and prompts an LLM to suggest what they could be replaced with.

## Key Findings

- **Cost:** $3.62 total for running LLMorpheus on all 13 subject applications (using octo.ai service, codellama-34b-instruct at $0.50/1M input tokens, $1.00/1M output tokens)
- **Mutant quality:** 63.2% of surviving mutants are "not equivalent" (real behavioral differences), 8.5% equivalent, 9.7% near-equivalent, 18.6% unknown
- **Comparison to StrykerJS:** LLMorpheus produces mutants that resemble existing bugs that cannot be produced by StrykerJS (state-of-the-art traditional tool)
- **Stability:** At temperature 0.0, 89.29%-98.89% of mutants observed across 5 runs
- **LLMs tested:** codellama-34b-instruct, mixtral-8x7b-instruct, and others

## Method

1. Placeholders introduced at designated locations in source code
2. LLM prompted to suggest replacements for placeholders
3. StrykerJS (modified) executes mutants and determines killed/survived/timeout
4. Interactive web site for inspecting results

## Implications

- LLMs can generate diverse, realistic mutants beyond fixed operator sets
- Cost is practical for real-world use ($3.62 for 13 packages)
- Complements traditional mutation testing by covering different fault classes
- Opens door to "intent-based" mutation testing (see Intent-Based MT, Mutation 2025)

## Related

- Meta ACH (FSE 2025) - industrial deployment of mutation-guided LLM test generation
- MUTGEN (2025) - mutation feedback in LLM prompts for test generation
- Intent-Based Mutation Testing (Mutation 2025) - mutating programming intents via LLM

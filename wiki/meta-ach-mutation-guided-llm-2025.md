---
source: "meta-ach-fse-2025.md"
ingested: "2026-10-01"
title: "Meta ACH: Mutation-Guided LLM Test Generation at Meta"
type: article
tags: [mutation-testing, llm, ai, industry, meta]
---

## Summary

ACH (Automated Compliance Hardening) is Meta's system for mutation-guided LLM-based test generation. It generates few, highly specific mutants targeting currently undetected faults, then uses these as prompts for LLM test generation. First industrial deployment of LLM-based mutation testing at scale.

## Key Results

| Metric | Value |
|--------|-------|
| Kotlin classes | 10,795 |
| Mutants generated | 9,095 |
| Tests generated | 571 |
| Engineer acceptance | 73% |
| Privacy-relevant | 36% |
| Equivalent detection precision | 0.79 (0.95 with pre-processing) |
| Coverage side-benefit | 51% of tests raise coverage |

## Method

1. Generate mutants specific to a concern (e.g., privacy)
2. Filter for currently undetected faults
3. Use as prompts for LLM test generation
4. Engineers review and accept/reject

## Key Insights

- Mutation testing goes beyond structural coverage
- "Mutation-as-RAG" - mutation feedback as retrieval-augmented generation
- Equivalent mutant problem less critical when engineers review tests
- Tests useful even when not directly tackling the specific concern

## Just-in-Time (JiT) Testing (2026)

Meta перешла на Just-in-Time Testing — динамическую генерацию тестов во время code review с опорой на мутационные проверки. Привело к 4x увеличению обнаружения багов по сравнению с поддержкой долгоживущих статических наборов тестов.

| Source | Date | Link |
|--------|------|------|
| InfoQ | Jan 2026 | [infoq.com](https://www.infoq.com/news/2026/01/meta-llm-mutation-testing/) |
| Meta Engineering | Feb 2026 | [engineering.fb.com](https://engineering.fb.com/2026/02/11/developer-tools/the-death-of-traditional-testing-agentic-development-jit-testing-revival/) |
| arXiv | 2026 | [2601.22832](https://arxiv.org/abs/2601.22832) |

## See also

- [[llmorpheus-llm-mutation-testing-2025]] - LLM-based mutant generation
- [[wiki/mutgen-mutation-guided-test-generation-2025]] - Mutation feedback in prompts
- [[intent-based-mutation-testing-2025]] - Mutating programming intents
- [[mutation-testing-vs-code-coverage-autonoma]] - General concepts

---
*Source: [raw/meta-ach-mutation-guided-llm-2025.md](../raw/meta-ach-mutation-guided-llm-2025.md) · FSE 2025*

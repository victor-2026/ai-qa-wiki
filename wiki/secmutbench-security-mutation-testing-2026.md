---
source: "secmutbench-2026.md"
ingested: "2026-10-01"
title: "SecMutBench: Security Mutation Testing for LLM Test Evaluation"
type: article
tags: [mutation-testing, security, llm, cwe]
---

## Summary

SecMutBench evaluates LLM-generated security tests using 25 security-specific mutation operators spanning 30 CWE categories. Traditional mutation scores overstate LLM security testing capability by 2.2x; the best LLM achieves only 19.7% vs 47.6% for expert-written tests.

## Key Findings

| Metric | Value |
|--------|-------|
| Mutation operators | 25 (30 CWE categories) |
| LLM overstatement | 2.2x |
| Best LLM | 19.7% |
| Expert-written | 47.6% |
| Functional kills | 15-36% (not crashes) |

## Security Mutation Score (SMS)

Classifies mutant kills into:
- **Semantic:** Genuine security awareness
- **Functional:** Behavioral side-effects
- **Incidental:** Coincidental detection
- **Crash:** Non-security failures

**Effective SMS (EffSMS)** = SMS x Secure-Pass Rate

## Implications

- LLM security tests appear stronger than they are with traditional metrics
- Need security-specific metrics distinguishing semantic understanding
- Significant gap between LLM and expert security tests
- Mutation testing essential for security test quality evaluation

## See also

- [[pytation-python-mutation-operators-2026]] - Python-specific operators
- [[llmorpheus-llm-mutation-testing-2025]] - LLM-based mutation
- [[meta-ach-mutation-guided-llm-2025]] - Meta ACH
- [[mutation-testing-vs-code-coverage-autonoma]] - General concepts

---
*Source: [raw/secmutbench-security-mutation-testing-2026.md](../raw/secmutbench-security-mutation-testing-2026.md) · AI-Powered Software 2026*

# SecMutBench: Evaluating LLM-Generated Security Tests via Mutation-Based Vulnerability Detection

**Source:** https://dl.acm.org/doi/10.1145/3805760.3814933
**Published:** AI-Powered Software Engineering (AI-Powered Software 2026)
**DOI:** 10.1145/3805760.3814933

## Summary

SecMutBench evaluates LLM-generated security tests using mutation-based vulnerability detection. It introduces 25 security-specific mutation operators spanning 30 CWE categories that transform secure Python code into realistic vulnerable variants.

## Key Findings

- **Security Mutation Score (SMS):** Classifies mutant kills into semantic, functional, incidental, and crash categories
- **Effective SMS (EffSMS):** SMS x Secure-Pass Rate to account for test validity
- **LLM overstatement:** Traditional mutation scores overstate LLM security testing capability by 2.2x on average
- **Best LLM:** 19.7% vs 47.6% for expert-written tests (2.4x gap)
- **Functional kills:** Not crashes, dominate non-semantic failures (15-36%)
- **22 new operators:** Extending prior security mutation frameworks to Python

## Method

1. Design 25 security-specific mutation operators for 30 CWE categories
2. Transform secure Python code into vulnerable variants
3. Evaluate LLM-generated security tests against mutants
4. Classify kills: semantic (genuine security awareness), functional (behavioral side-effects), incidental, crash

## Implications

- LLM security tests appear stronger than they are when measured by traditional mutation score
- Need security-specific metrics (SMS) that distinguish semantic understanding from coincidental detection
- Significant gap between LLM and expert-written security tests
- Mutation testing is essential for evaluating security test quality

## Related

- Mutation testing for AI/LLM evaluation
- Security testing quality metrics
- LLM-generated test validation

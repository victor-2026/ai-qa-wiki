# Mutation-Guided LLM-based Test Generation at Meta (ACH)

**Source:** https://arxiv.org/abs/2501.12862
**Authors:** Christopher Foster, Abhishek Gulati, Mark Harman, Inna Harper, Ke Mao, Jillian Ritchey, Herve Robert, Shubho Sengupta
**Published:** FSE 2025 (33rd ACM International Conference on the Foundations of Software Engineering), Industry Track
**DOI:** 10.1145/3696630.3728544

## Summary

ACH (Automated Compliance Hardening) is Meta's system for mutation-guided LLM-based test generation. It generates relatively few mutants compared to traditional mutation testing, focusing on generating currently undetected faults that are specific to an issue of concern. From these uncaught faults, ACH generates tests that catch them, thereby "killing" the mutants and hardening the platform against regressions.

## Key Results

- **Scale:** 10,795 Android Kotlin classes across 7 software platforms
- **Mutants generated:** 9,095
- **Tests generated:** 571 privacy-hardening test cases
- **Engineer acceptance:** 73% of ACH tests accepted, 36% judged privacy-relevant
- **Equivalent mutant detection:** LLM-based agent with precision 0.79, recall 0.47 (rising to 0.95 and 0.96 with simple pre-processing)
- **Coverage side-benefit:** 51% of ACH tests also raise coverage
- **Unkilled mutants:** 70% of mutants left unkilled by TestGen-LLM reside in classes without any TestGen-LLM test

## Method

1. Generate mutants specific to a concern (e.g., privacy)
2. Filter for currently undetected faults (not killed by existing tests)
3. Use these as prompts for LLM-based test generation
4. LLM generates tests that kill the mutants
5. Engineers review and accept/reject tests

## Key Insights

- Mutation testing goes beyond structural coverage (line coverage)
- "Mutation-as-RAG" - using mutation feedback as retrieval-augmented generation for test generation
- Equivalent mutant problem is less critical when engineers review tests (not mutants)
- First industrial deployment of LLM-based mutation testing at scale

## Deployment

- Used by Messenger and WhatsApp test-a-thons
- Engineers accepted 73% of generated tests
- Tests useful even when not directly tackling the specific concern

## Related

- LLMorpheus (TSE 2025) - LLM-based mutant generation
- MUTGEN (2025) - mutation feedback in prompts
- Google "Practical Mutation Testing at Scale" - diff-based mutation at code review
- "Does mutation testing improve testing practices?" (Just et al., ICSE 2021) - 14M mutants study

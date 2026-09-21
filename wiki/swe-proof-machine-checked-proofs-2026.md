# SWE-Proof: Machine-Checked Proofs for LLM Code (2026-09-18)

**Source:** https://arxiv.org/abs/2609.21190 (Ma, Mikek, Li, Erata, Zhang, Shui, Tehrani, Huan, Ramanathan, Sojoudi, Zhou, Deoras — 2026-09-18)

**Relevance:** ★★★★★ — Article 26/27/28: independent academic evidence that a green test suite is not correctness. Direct numerical backup for the mutation-matrix thesis: "verification catches what tests miss."

## Premise

Benchmarks for agentic code generation check correctness with **held-out test suites**, which are (1) inherently incomplete and (2) increasingly susceptible to memorization. Formal verification avoids both — but existing work only covers standalone tasks with specs given as input, not real issues (large repos, vague natural language intent).

## SWE-Proof pipeline (Benchproofer)

Turns a coding task with a known correct patch into a **formally verified** one:

1. Write a specification for the new code
2. Summarize the existing functions that code calls into axioms
3. Admit an instance only after **mechanical and adversarial gates agree**

Result: **SWE-Proof** = 500 real issues from SWE-bench Verified whose correctness is formally verified rather than tested. Extends to SWE-bench Pro.

## Key findings (numbers for articles)

- **"A quarter to a half of test-passing patches admit counterexamples"** — verification catches what test suites miss. This is the "green run while missing seeded breaks" claim, sourced with frontier models.
- **Structured natural-language specification does NOT fix it** — informal specs still admit the counterexamples.
- **Correct formal spec lifts resolution from 85% to 95%** for Opus 4.8 (only when the spec is written correctly).
- **Writing the spec is the hard part:** models that must write their own spec gain *nothing* over an unaided baseline, and only **62%** of their specs pass the audit.
- **Commonest failure = faithfulness:** a spec that constrains part of the required behavior and leaves the rest free — silent partial coverage, exactly analogous to a test that asserts the happy path only.
- Specification quality tracks outcome: fails on **89%** of unresolved instances vs 47% of resolved ones. Faithful spec synthesis = stated open problem.

## QA interpretation

- **Independent academic confirmation of Article 27's core argument:** the verifier itself must be verified. A suite passing does not establish correctness — here a quarter to a half of passing patches are provably wrong.
- **Mutation matrix / Verdictgate framing:** SWE-Proof seeds "breaks" the same way we do, but at the spec-axiom level (mechanical + adversarial gates = our assertion-kind + relevance gate). Their "faithfulness" failure = our warn about assertions that anchor the happy path only (testRigor M3/M6: suite green, break submitted → silent green).
- **For vendor evals (Article 26):** "62% of self-authored specs pass audit" is a calibration point — if even frontier models can't faithfully write their own verification intent, a vendor's self-reported "95% accurate" AI assertions carry the same unverified-intent risk.
- **Practical lift for our methodology:** spec/axiom summarization of called functions = the boundary-mapping step in per-risk-tier framework (what the change *touches*), operationalized for agentic codegen.

## Open questions for our A/B
- Can the same mechanical+adversarial double gate be applied to *test assertions* (not code specs) → strengthens the mutation-matrix design (assertion faithfulness gate)?
- Merging: SWE-Proof = formal-proof layer, Verdictgate = empirical-mutation layer. Both answer "did the verifier bite" from opposite ends.

## Cross-links
- [[mutation-testing-without-code]] / [[ai-qa-tool-evaluation-mutation-matrix]] — break the verifier, measure sensitivity
- [[ai-productivity-paradox-verification-layer-2026]] — verification layer argument
- [[testing-ai-book-evidence-foundations]] — evidence vs claims, oracle problem
- Article 26/27 (Articles project) — green-dashboard trap, silent false negative
- [[jason-arbon-how-ai-tests-software-2026]] — AI confidence, verifier sensitivity
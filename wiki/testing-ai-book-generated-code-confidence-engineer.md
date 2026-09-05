# Testing AI: Generated Code and the Confidence Engineer

This page summarizes Chapters 9-11 and the public brief on AI review loops with coding agents.

## Chapter 9: Generated Code Changes the Job

**Official source:** https://www.testingaibook.com/knowledge/chapter-09.html

### Core idea

Generated code can look clean, compile and still be wrong in integration, API usage, security, privacy, permissions or deployment behavior. Generated tests can increase coverage while missing the behavior that matters. The solution is not more trust in the generator; it is an independent verification path.

### Practical QA interpretation

- Review AI patches for behavior, not just syntax or style.
- Verify integration contracts, permissions, data handling and deployment assumptions.
- Inspect AI-generated tests for string assertions, tautologies, happy-path bias and over-mocking.
- Use a second agent or deterministic validator as a skeptical review path.
- Run meaningful behavior, integration, security and mutation checks.

### Useful artifacts

- Generated-code risk review.
- Patch-specific test plan.
- Security and privacy checklist.
- AI-generated-test critique.
- Trace from generated change to failing or passing evidence.

### Relation to Article 16

This chapter provides the conceptual basis for the claim that code generation can become cheap while understanding, verification and maintenance remain expensive.

## Chapter 10: Anti-Patterns That Create False Confidence

**Official source:** https://www.testingaibook.com/knowledge/chapter-10.html

### Core idea

False confidence is often a measurement or process failure, not a model failure. The chapter names traps such as Boolean pass/fail theater, percentage-passed worship, over-specific cases, golden-answer fixation, one-run demos, static test plans, aggregate-score blindness, final-answer-only testing and treating an LLM judge as truth.

### Practical QA interpretation

- Diagnose the confidence trap before tuning the prompt.
- Replace pass/fail with distributions, blockers, slices and representative examples.
- Treat surviving mutants as evidence that a test may not protect behavior.
- Do not patch one visible failure without checking nearby regressions.
- Evaluate agent trajectories, tool calls and side effects, not only the final response.
- Do not mistake refusal frequency for safety.

### Useful artifacts

- Anti-pattern diagnosis.
- Replacement measurement plan.
- False-confidence risk list.
- Release-policy rewrite.

### Relation to current wiki

This is closely related to mutation testing, Goodhart's Law, the AI QA evidence layer and the "agent found a bug but invented four" failure pattern.

## Chapter 11: The Confidence Engineer

**Official source:** https://www.testingaibook.com/knowledge/chapter-11.html

### Core idea

The Confidence Engineer connects product intent, code, tests, evals, traces, rollout and business consequences. The role is not simply a renamed tester. It combines building, testing, product judgment, risk analysis and evidence communication.

### Practical QA interpretation

- Define what the product is allowed to do and what evidence supports release.
- Connect technical findings to ship, hold, canary, rollback or collect-more-evidence decisions.
- Make known, unknown, risky and next-step states explicit.
- Keep role boundaries clear: product and engineering define intent; Quality Engineering makes evaluation and correction observable, testable and proportionate to risk.

### Useful artifacts

- Confidence report.
- Responsibility map.
- Quality decision narrative.
- Evidence-backed recommendation.

### Relation to current work

This is the closest book concept to the user's AI Quality Engineering leadership positioning, Article 16 and the Quality Operating Model series.

## Public Brief: Testing AI Review Loops With Coding Agents

**Official source:** https://www.testingaibook.com/knowledge/ch192-review-loops-coding-agents.html

### Core idea

A coding agent should not be the only judge of its own work. Add a fast, skeptical, evidence-oriented review path that challenges the generated patch and returns actionable findings before human approval.

### Practical QA interpretation

- Separate generation from evaluation and correction.
- Give the reviewer the task, diff, tests and relevant constraints.
- Require findings to cite behavior and evidence, not just style preferences.
- Keep a human approval boundary for high-risk changes.
- Validate the review loop with seeded faults and surviving-mutant analysis.

### Useful artifacts

- Direct -> Evaluate -> Correct loop.
- Reviewer prompt and policy.
- Finding classification.
- Confidence threshold and escalation rule.
- Human approval record.

### Relation to current work

This matches the Article 16 middle loop, QAEverest's locator versus step-change gates and the local 34/34 mutation result.

## Cross-Chapter Pattern

Chapters 9-11 change the unit of QA from "did the generated code compile?" to "what evidence justifies trusting this generated change?" The resulting system has four independent concerns:

1. Behavior and integration correctness.
2. Security, privacy and permission safety.
3. Test adequacy and anti-overfit protection.
4. Human decision rights for release.

## Sources

- [Official Knowledge Edition index](https://www.testingaibook.com/knowledge/index.html)
- [Full author draft preview](https://icebergqa.com/book/draft.html)
- [Testing AI book index in this wiki](testing-ai-book-index.md)





<!-- backlinks-start -->
### Backlinks
- [Apparently We Need a Testing Mindset After All (Klain)](wiki/keith-klain-testing-mindset-after-all-2026.md)
<!-- backlinks-end -->

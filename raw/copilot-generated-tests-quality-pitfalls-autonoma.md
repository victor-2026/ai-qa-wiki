# Copilot-Generated Tests: Quality Pitfalls and How to Fix Them

- **Source:** https://getautonoma.com/blog/copilot-generated-tests-quality-pitfalls
- **Author:** Tom Piaggio, Co-Founder at Autonoma
- **Date:** June 2026

## Key thesis

Copilot-generated tests share one root quality failure: Copilot infers expected values from the code it sees, so when asked to generate tests it asserts what the code already does rather than what the code should do. Result: hundreds of green tests, coverage looks strong, business-logic bugs still reach staging. Tests are real; protection is not as strong as the green checkmarks suggest.

## The 4 Pitfalls

All four start when Copilot derives expected behavior from the implementation.

1. **Tautological assertions** — test asserts the code's own output as the expected value. Discount example: Gold tier copy-paste bug applies 15% instead of 25%; Copilot test captures the wrong 85.00 output and asserts it, test passes. Fix: write expected value yourself from the spec before generating; drop it in a comment above the assertion.
2. **Mock everything, verify the mock** — when every dependency is mocked the test verifies the mock setup, not the component behavior. Declined-card integration bug never caught. Fix: mock at the boundary you care about (external HTTP, I/O), not the internal domain classes. Assert on observable outcome (order status = payment_failed, inventory restored).
3. **Snapshot / echo assertions that re-bless any change** — Copilot captures current output and asserts output equals itself. On change, update command re-captures and re-blesses the change, whether intentional or regression. Fix: snapshot baseline from a known-good state, not first run; for non-UI tests avoid snapshot-style assertions, assert specific values from spec.
4. **Happy-path-only coverage** — default output is valid inputs + success case; edge cases, boundaries, error paths missing. Fix: happy path = one test case, not the suite; ask separately for edge/error tests.

## Prompts That Improve Assertion Quality

- **Anchor to the business rule first** — write rule as comment before the test: `// Gold tier: 25% discount. A $100 order should return $75.00.` Highest-leverage edit.
- **Ask for falsifiability** — "What would make this test fail if the behavior were wrong?"
- **Paste acceptance criteria as context** — verbatim from ticket/spec.
- **Request edge cases as a separate pass** — second prompt after happy path.

## The Ceiling: What Better Prompting Still Can't Fix

Structural problem: when Copilot writes both the feature code and the test in the same/adjacent context windows, any bug in the logic becomes the expected value. Test stays green because expected value was derived from buggy code. This is an **independence problem**, not a prompt engineering one. AI verification is only as trustworthy as its independence from the thing being verified. A green test proves consistency, not correctness.

Better prompting addresses unit-level spec anchoring. It cannot give access to what the app is supposed to do at the user-flow level (product requirements, user stories, running app behavior) — that knowledge is not in function signatures Copilot can see.

## Autonoma's Positioning (vendor angle)

Autonoma covers the behavioral layer: Planner derives test cases from what the app is supposed to do (routes, components, API contracts, user flows) + DB state setup; Executor runs against per-PR preview asserting observable outcomes (UI, API, DB state); Reviewer classifies real bug vs agent error vs test/plan mismatch; Diffs Agent keeps tests healthy. Independence argument: "we are not the same model that wrote your feature asserting that feature back to itself."

Two layers complementary: Copilot unit tests = structural coverage (null handling, type safety, method call contracts); Autonoma = independent behavioral layer.

## Relevance to QA / resonance with our work

- Matches our mutation-testing findings: AI-generated tests give low mutation score (20-40%) vs human (60-80%) — same root cause: model-derived expected values.
- Matches DevAssure O2 experiment: agent found real bug but also false positives (JS-injection artifact) → Reviewer/classification layer is essential.
- Tautological-assertion pitfall = exactly what mutation testing exposes: test asserts buggy behavior as correct, survives mutant.
- Aider `--test-cmd` lesson: feedback loop from real test failures is more valuable than blind generation.

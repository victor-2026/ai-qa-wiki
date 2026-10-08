# Bas Dijkstra: Claude Code Guardrails + Mutation Check (Feb-Mar 2026, Surfaced 08.10)

**Sources (both full text read 08.10, via digest 08.10):** "Refactoring the RestAssured.Net code with Claude Code" (27.02.2026) https://www.ontestautomation.com/refactoring-the-rest-assured-net-code-with-claude-code/ + "Writing tests with Claude Code - part 1 - initial results" (09.03.2026) https://www.ontestautomation.com/writing-tests-with-claude-code-part-1-initial-results/. Author: Bas Dijkstra (Tier-1 peer watch). Code: https://github.com/basdijkstra/writing-tests-with-claude-code.

## Guardrails first (refactor post)

Three rules before letting the agent loose: (1) Claude does NOT touch tests (handwritten acceptance suite = safety net proving behavior-preserving refactor); (2) thorough review of EVERY change before version control ("I am responsible for the code, not Claude"; no outsourcing thinking — Fiona Charles; no offloading test runs + commits); (3) small steps (no hours-long unsupervised runs). Result: RequestBodyFactory extraction incl. 9-arg smell fixed via settings object, StyleCop-nuclear clean, tests green, committed. Doctrine: "slightly slower, a lot safer"; tests-and-review stay human until trust is earned.

## Mutation check on generated tests (part 1)

Setup honesty: API of his own (knows intent + what good looks like) — flags that without this, "looks good to me" approval is the risk. Claude: 23 tests, all passing, minutes of work. PITest: 95% line (tells nothing), **91% mutation (50/55 killed)**. Survivors: HTTP 500 path, HTTP 204 empty-GET path, savings-overdraw + interest boundaries. Dead weight: 4/23 (17%) removed with zero coverage impact (duplicate paths). Warnings: "productivity theater" (23 passing tests that can't fail = nothing); "moral obligation to closely watch LLM output"; single-run luck caveat (n=1); follow-up planned (feedback loop into Claude + mutation in generation loop).

## QA interpretation

- Independent practitioner replication of our mutation-verdict doctrine with numbers: line coverage dismissed explicitly, mutation + dead-weight analysis as the real measures.
- Guardrails post = accountability doctrine in matching words (responsibility stays human; tests as safety net, not oracle).
- "Looks good to me without understanding what you're approving" = examiner-author gap, pairs with Jason's held-out validation demand.
- Dead-weight 17% metric belongs in verdict-economics (W2 lane): generated tests cost maintenance + attention, not just tokens.

## See also

- [[llm-testing-6-approaches]] — judge calibration, contracts
- [[jason-arbon-book-v1-v2-audit-2026]] — held-out validation, TestBucks honesty
- [[testmuai-agentic-regression-testing-2026]] — recall metric, TDAD

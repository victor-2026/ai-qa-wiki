# Are My Tests Actually Testing Anything? 5 Ways to Know

- **Source:** https://getautonoma.com/blog/how-to-tell-if-tests-are-testing-anything
- **Author:** Tom Piaggio, Co-Founder at Autonoma
- **Date:** June 2026

## Thesis

"The fastest way to tell if your tests are testing anything: break the code on purpose. Comment out a line, flip a boolean, change a return value. If no test goes red, that test is theater, not protection."

## The 5 Checks (10 minutes, no special tooling)

### Check 1: Comment out a line. Does a test fail?

- Pick critical function, comment out one line of business logic
- **PASS:** At least one test goes red
- **FAIL:** Suite stays green → that line is "covered" but never verified

### Check 2: Break the function intentionally. Does it go red?

- Flip comparison (`>` → `>=`), swap `true`/`false`, change return value
- **PASS:** Test catches it → assertion derived from requirement, not output
- **FAIL:** Green → tautological test. Expected value = whatever function returned

### Check 3: Do assertions check observable behavior or implementation detail?

- Read each assertion. Is it checking a return value / rendered UI / API response? Or a private variable / mock call count / intermediate value?
- **PASS:** Assertions on outputs and observable state
- **FAIL:** Assertions mirror implementation back to itself. Tests that assert on mocks configured in the same test file are confirming the mock, not real behavior.

### Check 4: Would the test survive a mutation?

- Run Stryker/PIT/mutmut. Each surviving mutant = gap in verification.
- **PASS:** Mutation score >70% on critical paths
- **FAIL:** High line coverage (85%) + low mutation score (30%) → blind spot

### Check 5: Does removing the test drop meaningful coverage, or just line coverage?

- Pick a test. Delete it. Re-run. Did line coverage drop? Is any behavior now unverified?
- **PASS:** Removing it leaves a real gap
- **FAIL:** Line coverage drops a few points, but all behavior is still verified (or was never verified) → hollow test. Common in AI suites that target coverage %, not behavioral targets.

## Why AI-generated suites fail

Structural: same model writes code + test → bug in function becomes expected value in assertion. Model also optimizes for producing a test that PASSES, gaming line coverage by touching lines without asserting outcomes.

## Connection to Autonoma

Four-agent workflow structurally prevents this: Planner (reads codebase, plans from structure) → Executor (tests against running preview) → Reviewer (evaluates failures) → Diffs (keeps suite aligned). Independence is structural — expected behavior comes from user flow, not function output.

## Relevance to our stack

- **Buzzhive fault injection** = Check 1+2 automated (34/34 pass)
- **k6 URL bug** (`/` vs `auth/login`) = Check 2 FAIL — test passed 9 checks but URL was broken
- **Article 8 "big-pickle evaluates itself"** = Check 3 FAIL — assertion mirrors implementation
- **Article 7 0% lift** = Checks 4+5 — skills as generators produce hollow coverage
- **Quality Gates (W26 plan)** = Checks 3+5 automated as pre-commit lint

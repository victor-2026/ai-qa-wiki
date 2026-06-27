# Writing Tests with Claude Code — Part 1

**Author:** Bas Dijkstra
**Source:** [ontestautomation.com](https://www.ontestautomation.com/writing-tests-with-claude-code-part-1-initial-results/)
**Date:** March 9, 2026

---

## Overview

Bas Dijkstra experiment: asked Claude Code to write tests for a new Spring Boot API. This is part 1 — initial results.

---

## Experiment Setup

**Prompt used:**
> "Add acceptance tests for the endpoints exposed by the AccountController to this project. Cover all the logic in the AccountService class. Use REST Assured as the tool to interact with the API. Use JUnit 5 as the test runner. Both libraries are already part of the project, see the pom.xml. Assert status codes and relevant response body elements as part of the tests. Extract common request properties into a RequestSpecification."

**Result:** 23 tests, all passing, in ~2 minutes

---

## Results: Coverage

| Metric | Value |
|--------|-------|
| Line Coverage | **95%** |
| Mutation Coverage | **91%** (50/55 mutants killed) |

---

## Quality Assessment

### What Claude Did Well ✅

- Fast (2 min vs human hours)
- Good line + mutation coverage
- Covered most endpoints
- Readable code structure

### What Claude Missed ❌

| Missing Path | Impact |
|-------------|--------|
| HTTP 500 exception path | High |
| HTTP 204 (no accounts) | Medium |
| Boundary conditions | Medium |

---

## Dead Weight Analysis

**4 out of 23 tests (17%)** were dead weight — same code paths covered by other tests.

After removal: **0% impact on coverage** — tests could be safely removed.

---

## Key Insights

1. **Mutation testing is essential** — don't trust AI tests blindly
2. **17% dead weight** is common in AI-generated tests
3. **Need human review** — AI misses edge cases
4. **Same prompt = different results** — need iteration

---

## Bas Advice

> "It is my moral obligation to closely watch the output of an LLM."

---

## Related

- [[Test-Automation-Quadrant]] — Bas model for value vs efficiency
- [[wiki/mas-risks]] — AI testing risks (Groupthink, etc.)
- [[wiki/mutation-testing]] — PITest for mutation testing

---

*See Part 2 for improvement process*
*GitHub: https://github.com/basdijkstra/writing-tests-with-claude-code*
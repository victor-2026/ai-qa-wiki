# Mutation Matrix Template — Independent Quality Signal for AI-Generated Tests

**Purpose:** Measure whether your AI-generated tests actually catch deliberate defects (regressions), not just whether they pass on green code.

**How it works:** Introduce a small, controlled defect (mutant) into the code under test. Run your test suite against it. If tests still pass → the mutant "survived" → your tests have a blind spot.

**Key principle:** Not every test must catch every mutation. A login test should not be expected to catch a price-calculation boundary flip. Track `Expected to catch` separately from `Actual result`.

### "Expected to catch" checklist
A test is marked `Expected to catch = Yes` only if ALL hold:
- The mutation changes behavior in the area the test claims to verify
- The mutation is on the same layer (UI/API/logic) the test covers
- The mutation is NOT equivalent (it changes observable behavior for user/system)

If any fails → mark `Expected = No` (or `Equivalent`). This removes subjectivity and keeps the survival rate denominator meaningful.

---

## Step 1: Select tests
Pick 5-10 AI-assisted tests from your pilot. Note what each one claims to verify and its risk level.

| # | Test name | What it claims to check | Risk level (H/M/L) |
|---|-----------|------------------------|-------------------|
| 1 | | | |
| 2 | | | |
| ... | | | |

---

## Step 2: Define mutations
For each test, introduce ONE deliberate defect. Keep mutations small and isolated.

### UI-level mutations (manual DOM / fixture change)
| Mutation type | Example | What it simulates |
|---------------|---------|-------------------|
| Locator drift | `id="loginBtn"` → `id="login-button"` | UI/selector change between versions |
| Selector broadening | Remove `id`, use bare `button` | Test becomes less specific |
| Element removed | Delete a button/handler | Missing functionality |
| Wrong element | Swap two buttons' actions | Logic error |
| Duplicate target ambiguity | Two identical buttons, matcher picks first | Text matcher picks wrong occurrence |
| Validation removed | Remove required-field check | Business rule bypass |
| Navigation mutation | Wrong redirect target | Routing error |

### API-level mutations (mock server with mutated responses)
| Mutation type | Example | What it simulates |
|---------------|---------|-------------------|
| Status flip | `200` → `500` | Backend failure |
| Missing field | Response drops `balance` | Schema drift |
| Wrong type | `amount: "abc"` | Contract violation |
| Permission/role | User sees admin function | Authz bypass |

### Data mutations
| Mutation type | Example | What it simulates |
|---------------|---------|-------------------|
| Value change | `price = 100` → `price = 0` | Boundary / calculation error |
| Date shift | `expiry +1d` → `expiry -1d` | Time logic bug |
| Text corruption | Localized string broken | i18n regression |

### Logic / state mutations
| Mutation type | Example | What it simulates |
|---------------|---------|-------------------|
| Boundary flip | `>=` → `>` | Off-by-one / edge case |
| Race condition | Reorder async calls | Concurrency bug |
| Session expiry | Valid session → expired | Auth state bug |
| State mutation | Concurrent user edit | Shared-state conflict |

---

## Step 3: Run and record
For each mutation, run the associated test in an **ephemeral/sandbox environment only**. Record the result.

| Mutation ID | Date | Env | Layer (UI/API/DB/Logic) | Test | Mutation applied | Expected to catch? | Test result | Verdict | Assertion quality |
|-------------|------|-----|------------------------|------|-----------------|---------------|-------------|---------|------------------|
| M1 | | | UI | login | id drift | Yes | PASS | ❌ Survived | clear timeout |
| M2 | | | Logic | calc | `>=`→`>` | No | PASS | n/a | not applicable |
| M3 | | | UI | submit | validation removed | Yes | FAIL | ✅ Caught | clear message |
| ... | | | | | | | | | |

### Verdict values (not binary)
- **Caught** — test failed on the mutant, as expected
- **Survived** — test passed on the mutant (blind spot)
- **Flaky** — test intermittently passes/fails
- **False alert** — test failed, but for the wrong reason (wrong assertion fired)
- **Equivalent** — mutation does not change observable behavior; excluded from survival rate
- **n/a** — mutation not expected to be caught by this test

### Equivalent mutants
A mutant is **equivalent** when it changes the code but not the observable behavior (e.g., `if (x > 0)` → `if (x >= 1)` when x is integer). These must be marked `Equivalent` and excluded from the denominator of survival rate — otherwise the metric is artificially inflated.

### Assertion quality
- **High** — message explicitly points to the mutation (e.g., "balance field missing", "validation error expected")
- **Medium** — test failed but message is generic ("element not visible", "timeout")
- **Low** — unclear timeout/error requiring debug; prioritize fixing `Survived + Low` tests first

---

## Step 4: Calculate rates
```
Survival rate (FN) = (mutants expected-to-catch that PASSED) / (mutants expected-to-catch) × 100%
False positive rate (FP) = (tests that FAIL on clean code) / (total tests run) × 100%

Formula (explicit):
  Survival rate (FN) = Survived (Expected=Yes, Verdict≠Equivalent) / Total (Expected=Yes, Verdict≠Equivalent) × 100%

Note: FP rate is measured BEFORE any mutation is introduced — run the same tests on unmodified code in the same environment. This prevents accidentally counting mutant-caused failures as false positives.

Example from a commercial AI-QA platform run (M6-M9):
- M6 locator drift: PASSED, expected=Yes → Survived
- M7 selector broadening: PASSED, expected=Yes → Survived
- M8 element removed: FAILED, expected=Yes → Caught
- M9 wrong element: FAILED, expected=Yes → Caught

Survival rate = 2/4 = 50%
Pattern: functional failures caught, structural fragility missed
```

> Note: Track BOTH survival rate (FN) and FP rate. A test suite that catches everything but also fails on clean code is itself a liability.

---

## Step 5: Interpret
| Survival rate | Meaning | Action |
|---------------|---------|--------|
| 0% | Tests catch every expected defect | Strong — trust the signal |
| <20% | Minor blind spots | Target the missed mutation types |
| 20-50% | Structural gaps | Add mutation testing to CI as a gate |
| >50% | Tests are weak | Don't trust green dashboard |

---

## Step 6: Map to risk level (concrete actions)
Cross-reference survival rate with risk level from Step 1:

| Risk | Survival rate | Concrete human gate |
|------|--------------|---------------------|
| High | >0% | Full manual re-review by senior QA; sign-off required before merge; artifact = reviewed diff + note |
| High | 0% | Lightweight spot-check; artifact = mutation report attached to PR |
| Medium | 20-50% | Targeted review of the missed mutation type; 30 min per flow |
| Low | any | No gate; rely on mutation trend |

**Human gate = a named person reviews the mutation report and approves before the PR merges. Time cost scales with risk × survival rate.**

---

## Step 7: Regression / trend
Survival rate is a point-in-time metric. Re-run the matrix every iteration and track the trend.

### Minimum fields for aggregation
| Sprint | Risk | Layer | Survival rate | FP rate |
|--------|------|-------|---------------|---------|
| S1 | High | UI | 45% | 2% |
| S2 | High | UI | 30% | 1% |

- Falling survival rate = tests improving
- Rising survival rate = test debt accumulating
- Plot per-risk-level to see where quality erodes first

---

## Tooling notes
| Level | Tools | What they mutate |
|-------|-------|------------------|
| Code-level | Stryker (TS/JS), MutPy (Python) | Source code — runs many mutants per execution |
| UI-level | Manual DOM edit / test fixture mutation | Live UI elements (as described above) |
| API-level | Mock server (WireMock, MSW) | Response status, fields, types |

> "One mutation per test-target pair" — for UI/API manual mutations, isolate one defect per run. For code-level tools (Stryker), the tool auto-mutates many points in a single execution; review its report per mutant.

---

## Meta-data for audit trail
Every mutation record should carry: `Mutation ID`, `Date`, `Environment`, `Layer`, `Owner`, `Status`. This enables repeatable runs, trend analysis, and shows which mutants are still open.

| Mutation ID | Date | Env | Layer | Test | Owner | Status |
|-------------|------|-----|-------|------|-------|--------|
| M1 | 2026-09-01 | sandbox-1 | UI | login | QA-1 | Open |

Status values: `Open` / `Fixed` / `Accepted risk`.

---

## Appendix: Filled example (7 rows)

| Mutation ID | Date | Env | Layer | Test | Mutation applied | Expected to catch? | Test result | Verdict | Assertion quality |
|-------------|------|-----|-------|------|-----------------|-------------------|-------------|---------|------------------|
| M1 | 2026-09-01 | sandbox-1 | UI | login | id loginBtn → login-button | Yes | PASS | ❌ Survived | timeout (low) |
| M2 | 2026-09-01 | sandbox-1 | Logic | price-calc | `>=` → `>` | Yes | FAIL | ✅ Caught | clear message |
| M3 | 2026-09-01 | sandbox-1 | UI | submit | validation removed | Yes | FAIL | ✅ Caught | clear message |
| M4 | 2026-09-01 | sandbox-1 | UI | login | swap buttons | Yes | FAIL | ✅ Caught | clear message |
| M5 | 2026-09-01 | sandbox-1 | API | fetch-balance | 200 → 500 | Yes | FAIL | ✅ Caught | clear message |
| M6 | 2026-09-01 | sandbox-1 | Logic | price-calc | `x>0` → `x>=1` | Yes | PASS | Equivalent | n/a (excluded) |
| M7 | 2026-09-01 | sandbox-1 | UI | nav | wrong redirect | No | PASS | n/a | not applicable |

### Calculation
```
Expected-to-catch mutants (non-equivalent): M1, M2, M3, M4, M5 = 5  (M7 excluded: Expected=No)
Survived (expected=Yes, non-equivalent): M1 = 1
Survival rate (FN) = 1/5 = 20%

FP rate: tests that fail on clean code = 0 / 7 = 0%
```

Interpretation: 20% survival rate = minor blind spots. M1 (locator drift) is the gap - strengthen the login test's locator assertion. M6 excluded as equivalent. M7 not expected to catch (nav test, different scope).

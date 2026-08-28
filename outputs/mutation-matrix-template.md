# Mutation Matrix Template — Independent Quality Signal for AI-Generated Tests

**Purpose:** Measure whether your AI-generated tests actually catch deliberate defects (regressions), not just whether they pass on green code.

**How it works:** Introduce a small, controlled defect (mutant) into the code under test. Run your test suite against it. If tests still pass → the mutant "survived" → your tests have a blind spot.

---

## Step 1: Select tests
Pick 5-10 AI-assisted tests (or AI-generated tests) from your pilot. Note what each one claims to verify.

| # | Test name | What it claims to check | Risk level (H/M/L) |
|---|-----------|------------------------|-------------------|
| 1 | | | |
| 2 | | | |
| ... | | | |

---

## Step 2: Define mutations
For each test, introduce ONE deliberate defect. Keep mutations small and isolated.

| Mutation type | Example | What it simulates |
|---------------|---------|-------------------|
| **Locator drift** | `id="loginBtn"` → `id="login-button"` | UI/selector change between versions |
| **Selector broadening** | Remove `id`, use bare `button` | Test becomes less specific |
| **Element removed** | Delete a button/handler | Missing functionality |
| **Wrong element** | Swap two buttons' actions | Logic error |
| **Validation removed** | Remove required-field check | Business rule bypass |
| **Boundary flip** | `>=` → `>` | Off-by-one / edge case |

---

## Step 3: Run and record
For each mutation, run the associated test. Record the result.

| # | Test | Mutation applied | Test result | Verdict |
|---|------|-----------------|-------------|---------|
| 1 | login test | id loginBtn → login-button | PASS | ❌ Mutant survived (blind spot) |
| 2 | submit test | removed validation | FAIL | ✅ Caught |
| ... | | | | |

---

## Step 4: Calculate survival rate
```
Survival rate = (mutants that passed) / (total mutants) × 100%

Example from my QAEverest run (M6-M9):
- M6 locator drift: PASSED (survived)
- M7 selector broadening: PASSED (survived)
- M8 element removed: FAILED (caught)
- M9 wrong element: FAILED (caught)

Survival rate = 2/4 = 50%
Pattern: functional failures caught, structural fragility missed
```

---

## Step 5: Interpret
| Survival rate | Meaning | Action |
|---------------|---------|--------|
| 0% | Tests catch every defect | Strong — trust the signal |
| <20% | Minor blind spots | Target the missed mutation types |
| 20-50% | Structural gaps | Add mutation testing to CI as a gate |
| >50% | Tests are weak | Don't trust green dashboard |

---

## Step 6: Map to risk level
Cross-reference survival rate with the risk level from Step 1:
- High-risk flow + high survival rate = **human gate mandatory**
- Low-risk flow + low survival rate = lighter touch OK

This gives you a measurable, independent signal alongside execution results and QA review — without a person rechecking everything.

---

## Notes
- Run mutants in ephemeral/sandbox environments only. Never on production.
- One mutation per run (isolate the variable).
- Automate if possible (tools: Stryker, MutPy, or manual for small sets).
- Re-run after test fixes to confirm the blind spot is closed.

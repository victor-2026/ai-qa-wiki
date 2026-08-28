# Mutation Matrix Lite

## Purpose
Measure whether your AI-generated tests actually catch deliberate defects (regressions), not just whether they pass on green code.

## How it works
Introduce a small, controlled defect (mutant) into the code under test. Run your test suite against it.

- If tests still **pass** → the mutant **"survived"** → your tests have a blind spot.
- If tests **fail** → the mutant was **"caught"** → your tests are sensitive to this type of defect.

## Key principle
Not every test must catch every mutation. A login test should not be expected to catch a price-calculation boundary flip. Track **Expected to catch** separately from **Actual result**.

**Simple rule for Lite:**
Mark `Expected = Yes` only if:

- the mutation changes behavior in the area the test checks, and
- the mutation is on the same layer (UI/API/logic) that the test covers.

If not → mark `Expected = No` and use verdict `n/a`.

---

## Step 1: Select tests
Pick 5–10 AI-assisted tests from your pilot. Note the test name and risk level.

| # | Test name | Risk (H/M/L) |
|---|-----------|--------------|
| 1 |           |              |
| 2 |           |              |
| 3 |           |              |
| 4 |           |              |
| 5 |           |              |

---

## Step 2: Define mutations
For each test, introduce **ONE** deliberate defect. Keep mutations small and isolated.

Use this minimal set for the pilot:

### UI mutations
| Mutation type       | Example                              | What it simulates                          |
|---------------------|--------------------------------------|--------------------------------------------|
| Locator drift       | `id="loginBtn"` → `id="login-button"` | UI/selector change between versions        |
| Validation removed  | Remove required-field check          | Business rule bypass                       |

### API mutations
| Mutation type       | Example                     | What it simulates           |
|---------------------|-----------------------------|-----------------------------|
| Status flip         | `200` → `500`               | Backend failure             |
| Missing field       | Response drops `balance`    | Schema drift                |

### Logic mutations
| Mutation type       | Example       | What it simulates                  |
|---------------------|---------------|------------------------------------|
| Boundary flip       | `>=` → `>`    | Off-by-one / edge case             |

Pick one mutation type per test from this list.

---

## Step 3: Run and record
For each mutation, run the associated test in an **ephemeral/sandbox environment only**. Record the result.

| Mutation ID | Test        | Mutation type      | Expected? (Y/N) | Result (PASS/FAIL) | Verdict (Caught/Survived/n/a) |
|-------------|-------------|--------------------|-----------------|--------------------|-------------------------------|
| M1          | login       | id drift           | Y               | PASS               | Survived                      |
| M2          | login       | validation removed | Y               | FAIL               | Caught                        |
| M3          | fetch-balance | 200→500           | Y               | FAIL               | Caught                        |
| M4          | price-calc  | `>=`→`>`           | N               | PASS               | n/a                           |
| M5          | nav         | wrong redirect     | N               | PASS               | n/a                           |

**Verdict values:**
- **Caught** — test failed on the mutant, as expected
- **Survived** — test passed on the mutant (blind spot)
- **n/a** — mutation not expected to be caught by this test

---

## Step 4: Calculate survival rate
```
Survival rate = (Survived (Expected=Yes)) / (Total Expected=Yes) × 100%
```

**Example:**
- Expected=Yes: M1, M2, M3 = 3
- Survived (Expected=Yes): M1 = 1
- Survival rate = 1/3 = 33% → some blind spots

---

## Step 5: Interpret
| Survival rate | Meaning                     | Action                              |
|---------------|-----------------------------|-------------------------------------|
| 0%            | Tests catch every expected defect | Strong — trust the signal          |
| <50%          | Some blind spots            | Strengthen assertions/locators      |
| ≥50%          | Tests are weak              | Don't trust green dashboard         |

---

## Mini example
5 tests, 5 mutations, 3 expected=Yes.
1 survived → survival rate = 1/3 = 33% → minor blind spots. Focus on strengthening the test that let the mutation survive (e.g., improve locator assertion).

---

## Quick pilot checklist (1 page)
Can be used as a standalone document / Notion page:

1. **Pick 5–10 AI tests** (login / payments / calculations).
2. **For each test, pick 1 mutation** from the list:
   - UI: `Locator drift`, `Validation removed`
   - API: `Status flip (200→500)`, `Missing field`
   - Logic: `Boundary flip (>= → >)`
3. **Apply the mutation in a sandbox** and run the test.
4. **Fill the table**:

   | Mutation ID | Test | Mutation type | Expected? (Y/N) | Result (PASS/FAIL) | Verdict |
   |-------------|------|---------------|-----------------|--------------------|---------|
   |             |      |               |                 |                    |         |

5. **Calculate survival rate**:
   ```
   Survival rate = (Survived (Expected=Yes)) / (Total Expected=Yes) × 100%
   ```

6. **Draw a conclusion** from the interpretation table and note 1–2 actions:
   - which tests to strengthen (locators, assertions, field checks);
   - which mutations to add in the next round.

# Login Mutation Set (Lite pilot) 

A ready-to-use set of **5 mutations** for a typical login flow. Each mutation takes ~5–10 minutes to apply manually and run.

## Typical login tests
| # | Test name | What it claims to check | Risk |
|---|-----------|------------------------|------|
| 1 | login_success | Valid credentials → redirect to dashboard | High |
| 2 | login_invalid_password | Invalid password → error message shown | High |
| 3 | login_empty_fields | Empty email/password → validation error | Medium |
| 4 | login_locked_account | Locked account → specific error | Medium |
| 5 | login_redirect_after | After login, correct page URL | Low |

## Mutations for Lite pilot

### M1: Locator drift (UI)
- **Test:** `login_success`
- **Mutation:** Change `id="loginBtn"` → `id="login-button"` on the login button.
- **Expected:** Test should fail (cannot find button by old locator).
- **What it checks:** How sensitive the test is to selector changes.

### M2: Validation removed (UI)
- **Test:** `login_empty_fields`
- **Mutation:** Remove the `required` check from email or password field (or disable form-level validation).
- **Expected:** Test should fail (form submits without validation, but test expects an error).
- **What it checks:** Whether the test catches missing mandatory validation.

### M3: Status flip (API)
- **Test:** `login_invalid_password`
- **Mutation:** In the mock server, change response from `200` → `500` on wrong password.
- **Expected:** Test should fail (expects 200 + error message, gets 500).
- **What it checks:** Whether the test reacts to backend errors.

### M4: Wrong element (UI)
- **Test:** `login_locked_account`
- **Mutation:** Swap the actions of "Login" and "Cancel" buttons (or make clicking "Login" trigger cancel).
- **Expected:** Test should fail (logic broken).
- **What it checks:** Whether the test catches UI-level logic swap.

### M5: Boundary flip (Logic)
- **Test:** `login_locked_account`
- **Mutation:** Change lockout condition: `attempts >= 5` → `attempts > 5`.
- **Expected:** Test should fail (account unlocks on 5th attempt instead of 6th).
- **What it checks:** Sensitivity to off-by-one errors in lockout logic.

## Results table
| Mutation ID | Test | Mutation type | Expected? (Y/N) | Result (PASS/FAIL) | Verdict (Caught/Survived/n/a) | Notes |
|-------------|------|---------------|-----------------|--------------------|-------------------------------|-------|
| M1 | login_success | id drift | Y | | | |
| M2 | login_empty_fields | validation removed | Y | | | |
| M3 | login_invalid_password | 200→500 | Y | | | |
| M4 | login_locked_account | swap buttons | Y | | | |
| M5 | login_locked_account | >=→> | Y | | | |

### Calculation
- Total Expected=Yes: 5
- Survived (Expected=Yes): count after run
- Survival rate = Survived / 5 × 100%

**Pilot goal:** achieve survival rate <50% and at least 1–2 concrete insights (e.g., "login tests don't catch locator drift" or "don't react to 500 from backend").

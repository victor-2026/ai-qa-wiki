# Payments — mutation set for Lite pilot 

A ready-to-use set of **5 mutations** for the payments scenario. Each mutation takes ~5–10 minutes to apply manually and run.

## Typical payment tests
| # | Test name | What it claims to check | Risk |
|---|-----------|------------------------|------|
| 1 | payment_success | Valid card → payment processed, success message | High |
| 2 | payment_insufficient_funds | Insufficient balance → payment declined | High |
| 3 | payment_invalid_card | Invalid card number → validation error | Medium |
| 4 | payment_duplicate_prevention | Double-click → only one charge | High |
| 5 | payment_refund_success | Refund request → balance updated | Medium |

## Mutations for Lite pilot

### M1: Status flip (API)
- **Test:** `payment_success`
- **Mutation:** In the mock server, change the payment gateway response from `200` → `500`.
- **Expected:** Test should fail (expects successful payment, gets error).
- **What it checks:** Whether the test reacts to backend/gateway errors.

### M2: Missing field (API)
- **Test:** `payment_success`
- **Mutation:** Remove the `transactionId` field from the payment gateway response.
- **Expected:** Test should fail (expects `transactionId` to be present).
- **What it checks:** Whether the test checks response completeness, not just status 200.

### M3: Value change (Data/Logic)
- **Test:** `payment_insufficient_funds`
- **Mutation:** Change the user balance: `balance = 100` → `balance = 0` before the payment attempt.
- **Expected:** Test should fail (payment goes through although balance is 0).
- **What it checks:** Whether the test catches missing balance validation.

### M4: Validation removed (UI/API)
- **Test:** `payment_invalid_card`
- **Mutation:** Disable card-number validation at form or API level (accept any format).
- **Expected:** Test should fail (invalid card accepted, but test expects an error).
- **What it checks:** Presence and behavior of input validation.

### M5: Duplicate allowed (Logic)
- **Test:** `payment_duplicate_prevention`
- **Mutation:** Remove the `isProcessing` or `deduplicationKey` check, allow two identical requests in a row.
- **Expected:** Test should fail (two payments go through instead of one).
- **What it checks:** Protection against duplicate payments.

## Results table
| Mutation ID | Test | Mutation type | Expected? (Y/N) | Result (PASS/FAIL) | Verdict (Caught/Survived/n/a) | Notes |
|-------------|------|---------------|-----------------|--------------------|-------------------------------|-------|
| M1 | payment_success | 200→500 | Y | | | |
| M2 | payment_success | missing transactionId | Y | | | |
| M3 | payment_insufficient_funds | balance 100→0 | Y | | | |
| M4 | payment_invalid_card | validation removed | Y | | | |
| M5 | payment_duplicate_prevention | duplicate allowed | Y | | | |

### Calculation
- Total Expected=Yes: 5
- Survived (Expected=Yes): count after run
- Survival rate = Survived / 5 × 100%

**Target insights:** e.g., "tests don't catch missing transactionId" or "let duplicate payments through".

# Calculations — mutation set for Lite pilot 

A ready-to-use set of **5 mutations** for the calculations scenario. Each mutation takes ~5–10 minutes to apply manually and run.

## Typical calculation tests
| # | Test name | What it claims to check | Risk |
|---|-----------|------------------------|------|
| 1 | calc_total_price | Correct total with tax and discount | High |
| 2 | calc_boundary_discount | Discount applied at boundary (>=1000) | Medium |
| 3 | calc_rounding | Correct rounding to 2 decimals | Medium |
| 4 | calc_negative_input | Negative quantity → error | Low |
| 5 | calc_tax_rate_change | Tax rate update → new total | Medium |

## Mutations for Lite pilot

### M1: Boundary flip (Logic)
- **Test:** `calc_boundary_discount`
- **Mutation:** Change the discount condition: `amount >= 1000` → `amount > 1000`.
- **Expected:** Test should fail (discount not applied at 1000, but should be).
- **What it checks:** Sensitivity to off-by-one errors at boundaries.

### M2: Value change (Logic)
- **Test:** `calc_total_price`
- **Mutation:** Change the formula: `total = price * qty + tax` → `total = price * qty` (drop tax).
- **Expected:** Test should fail (total without tax).
- **What it checks:** Whether the test checks the full calculation formula.

### M3: Rounding removed (Logic)
- **Test:** `calc_rounding`
- **Mutation:** Disable rounding: `round(total, 2)` → `total` (returns 10.999999 instead of 11.00).
- **Expected:** Test should fail (expects 2 decimal places).
- **What it checks:** Presence and behavior of rounding.

### M4: Validation removed (Logic/UI)
- **Test:** `calc_negative_input`
- **Mutation:** Remove the `qty > 0` check, allow negative quantity.
- **Expected:** Test should fail (calculation runs with negative qty, but test expects an error).
- **What it checks:** Input validation.

### M5: Tax rate change (Data/Config)
- **Test:** `calc_tax_rate_change`
- **Mutation:** Change the tax rate in config: `taxRate = 0.20` → `taxRate = 0.15`, but the test expects the old rate.
- **Expected:** Test should fail (total doesn't match expected).
- **What it checks:** Whether the test reacts to config changes.

## Results table
| Mutation ID | Test | Mutation type | Expected? (Y/N) | Result (PASS/FAIL) | Verdict (Caught/Survived/n/a) | Notes |
|-------------|------|---------------|-----------------|--------------------|-------------------------------|-------|
| M1 | calc_boundary_discount | >=→> | Y | | | |
| M2 | calc_total_price | remove tax | Y | | | |
| M3 | calc_rounding | rounding removed | Y | | | |
| M4 | calc_negative_input | validation removed | Y | | | |
| M5 | calc_tax_rate_change | tax 20%→15% | Y | | | |

### Calculation
- Total Expected=Yes: 5
- Survived (Expected=Yes): count after run
- Survival rate = Survived / 5 × 100%

**Target insights:** e.g., "tests don't catch off-by-one at boundaries" or "let missing rounding through".

# Сводная таблица для пилота (логин + платежи + расчёты)

Единый пилот на 15 тестах (5 на сценарий). Соберите всё в одну таблицу:

| Mutation ID | Scenario | Test | Mutation type | Expected? (Y/N) | Result (PASS/FAIL) | Verdict | Notes |
|-------------|----------|------|---------------|-----------------|--------------------|---------|-------|
| L1 | Login | login_success | id drift | Y | | | |
| L2 | Login | login_empty_fields | validation removed | Y | | | |
| L3 | Login | login_invalid_password | 200→500 | Y | | | |
| L4 | Login | login_locked_account | swap buttons | Y | | | |
| L5 | Login | login_locked_account | >=→> | Y | | | |
| P1 | Payments | payment_success | 200→500 | Y | | | |
| P2 | Payments | payment_success | missing transactionId | Y | | | |
| P3 | Payments | payment_insufficient_funds | balance 100→0 | Y | | | |
| P4 | Payments | payment_invalid_card | validation removed | Y | | | |
| P5 | Payments | payment_duplicate_prevention | duplicate allowed | Y | | | |
| C1 | Calculations | calc_boundary_discount | >=→> | Y | | | |
| C2 | Calculations | calc_total_price | remove tax | Y | | | |
| C3 | Calculations | calc_rounding | rounding removed | Y | | | |
| C4 | Calculations | calc_negative_input | validation removed | Y | | | |
| C5 | Calculations | calc_tax_rate_change | tax 20%→15% | Y | | | |

## Общий расчёт
- Total Expected=Yes: 15
- Survived (Expected=Yes): посчитать
- Survival rate = Survived / 15 × 100%

Отдельно по сценариям:
- Login survival rate = Survived_L / 5
- Payments survival rate = Survived_P / 5
- Calculations survival rate = Survived_C / 5

Это покажет, где качество тестов хуже.

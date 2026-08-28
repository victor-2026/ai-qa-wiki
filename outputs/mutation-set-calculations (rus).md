# Расчёты (Calculations) — набор мутаций для Lite-пилота

Готовый набор из **5 мутаций** для сценария «расчёты». Каждая мутация рассчитана на 5–10 минут ручного внесения и прогона.

## Типовые тесты для расчётов
| # | Test name | What it claims to check | Risk |
|---|-----------|------------------------|------|
| 1 | calc_total_price | Correct total with tax and discount | High |
| 2 | calc_boundary_discount | Discount applied at boundary (>=1000) | Medium |
| 3 | calc_rounding | Correct rounding to 2 decimals | Medium |
| 4 | calc_negative_input | Negative quantity → error | Low |
| 5 | calc_tax_rate_change | Tax rate update → new total | Medium |

## Мутации для Lite-пилота

### M1: Boundary flip (Logic)
- **Test:** `calc_boundary_discount`
- **Mutation:** Изменить условие применения скидки: `amount >= 1000` → `amount > 1000`.
- **Ожидаемое поведение:** Тест должен упасть (скидка не применяется при 1000, хотя должна).
- **Что проверяет:** Чувствительность к off-by-one ошибкам на границах.

### M2: Value change (Logic)
- **Test:** `calc_total_price`
- **Mutation:** Изменить формулу: `total = price * qty + tax` → `total = price * qty` (убрать налог).
- **Ожидаемое поведение:** Тест должен упасть (итоговая сумма без налога).
- **Что проверяет:** Проверяет ли тест полную формулу расчёта.

### M3: Rounding removed (Logic)
- **Test:** `calc_rounding`
- **Mutation:** Отключить округление: `round(total, 2)` → `total` (возвращает 10.999999 вместо 11.00).
- **Ожидаемое поведение:** Тест должен упасть (ожидает 2 знака после запятой).
- **Что проверяет:** Наличие и работу округления.

### M4: Validation removed (Logic/UI)
- **Test:** `calc_negative_input`
- **Mutation:** Удалить проверку `qty > 0`, разрешить отрицательное количество.
- **Ожидаемое поведение:** Тест должен упасть (расчёт проходит с отрицательным qty, но тест ожидает ошибку).
- **Что проверяет:** Валидацию входных данных.

### M5: Tax rate change (Data/Config)
- **Test:** `calc_tax_rate_change`
- **Mutation:** Изменить ставку налога в конфиге: `taxRate = 0.20` → `taxRate = 0.15`, но тест ожидает старую ставку.
- **Ожидаемое поведение:** Тест должен упасть (итоговая сумма не совпадает с ожидаемой).
- **Что проверяет:** Реагирует ли тест на изменения конфигурации.

## Таблица для записи результатов
| Mutation ID | Test | Mutation type | Expected? (Y/N) | Result (PASS/FAIL) | Verdict (Caught/Survived/n/a) | Notes |
|-------------|------|---------------|-----------------|--------------------|-------------------------------|-------|
| M1 | calc_boundary_discount | >=→> | Y | | | |
| M2 | calc_total_price | remove tax | Y | | | |
| M3 | calc_rounding | rounding removed | Y | | | |
| M4 | calc_negative_input | validation removed | Y | | | |
| M5 | calc_tax_rate_change | tax 20%→15% | Y | | | |

### Расчёт
- Total Expected=Yes: 5
- Survived (Expected=Yes): посчитать после прогона
- Survival rate = Survived / 5 × 100%

**Целевые инсайты:** например, «тесты не ловят off-by-one на границах» или «пропускают отсутствие округления».

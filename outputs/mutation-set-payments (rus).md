# Платежи (Payments) — набор мутаций для Lite-пилота

Готовый набор из **5 мутаций** для сценария «платежи». Каждая мутация рассчитана на 5–10 минут ручного внесения и прогона.

## Типовые тесты для платежей
| # | Test name | What it claims to check | Risk |
|---|-----------|------------------------|------|
| 1 | payment_success | Valid card → payment processed, success message | High |
| 2 | payment_insufficient_funds | Insufficient balance → payment declined | High |
| 3 | payment_invalid_card | Invalid card number → validation error | Medium |
| 4 | payment_duplicate_prevention | Double-click → only one charge | High |
| 5 | payment_refund_success | Refund request → balance updated | Medium |

## Мутации для Lite-пилота

### M1: Status flip (API)
- **Test:** `payment_success`
- **Mutation:** В мок-сервере изменить ответ платёжного шлюза с `200` → `500`.
- **Ожидаемое поведение:** Тест должен упасть (ожидает успешный платёж, получает ошибку).
- **Что проверяет:** Реагирует ли тест на ошибки бэкенда/шлюза.

### M2: Missing field (API)
- **Test:** `payment_success`
- **Mutation:** Удалить поле `transactionId` из ответа платёжного шлюза.
- **Ожидаемое поведение:** Тест должен упасть (ожидает наличие `transactionId`).
- **Что проверяет:** Проверяет ли тест полноту ответа, а не только статус 200.

### M3: Value change (Data/Logic)
- **Test:** `payment_insufficient_funds`
- **Mutation:** Изменить баланс пользователя: `balance = 100` → `balance = 0` перед попыткой платежа.
- **Ожидаемое поведение:** Тест должен упасть (платёж проходит, хотя баланс 0).
- **Что проверяет:** Ловит ли тест отсутствие проверки баланса.

### M4: Validation removed (UI/API)
- **Test:** `payment_invalid_card`
- **Mutation:** Отключить валидацию номера карты на уровне формы или API (принимает любой формат).
- **Ожидаемое поведение:** Тест должен упасть (невалидная карта принимается, но тест ожидает ошибку).
- **Что проверяет:** Наличие и работу валидации входных данных.

### M5: Duplicate allowed (Logic)
- **Test:** `payment_duplicate_prevention`
- **Mutation:** Удалить проверку `isProcessing` или `deduplicationKey`, разрешить два одинаковых запроса подряд.
- **Ожидаемое поведение:** Тест должен упасть (проходят два платежа вместо одного).
- **Что проверяет:** Защиту от дублирования платежей.

## Таблица для записи результатов
| Mutation ID | Test | Mutation type | Expected? (Y/N) | Result (PASS/FAIL) | Verdict (Caught/Survived/n/a) | Notes |
|-------------|------|---------------|-----------------|--------------------|-------------------------------|-------|
| M1 | payment_success | 200→500 | Y | | | |
| M2 | payment_success | missing transactionId | Y | | | |
| M3 | payment_insufficient_funds | balance 100→0 | Y | | | |
| M4 | payment_invalid_card | validation removed | Y | | | |
| M5 | payment_duplicate_prevention | duplicate allowed | Y | | | |

### Расчёт
- Total Expected=Yes: 5
- Survived (Expected=Yes): посчитать после прогона
- Survival rate = Survived / 5 × 100%

**Целевые инсайты:** например, «тесты не ловят отсутствие transactionId» или «пропускают дубли платежей».

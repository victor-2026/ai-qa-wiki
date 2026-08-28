# Конкретный набор мутаций для сценария «Логин» (Lite-пилот)

Готовый набор из **5 мутаций** для типового flow «логин». Каждая мутация рассчитана на 5–10 минут ручного внесения и прогона.

## Типовые тесты для логина
| # | Test name | What it claims to check | Risk |
|---|-----------|------------------------|------|
| 1 | login_success | Valid credentials → redirect to dashboard | High |
| 2 | login_invalid_password | Invalid password → error message shown | High |
| 3 | login_empty_fields | Empty email/password → validation error | Medium |
| 4 | login_locked_account | Locked account → specific error | Medium |
| 5 | login_redirect_after | After login, correct page URL | Low |

## Мутации для Lite-пилота

### M1: Locator drift (UI)
- **Test:** `login_success`
- **Mutation:** Изменить `id="loginBtn"` → `id="login-button"` в кнопке входа.
- **Ожидаемое поведение:** Тест должен упасть (не находит кнопку по старому локатору).
- **Что проверяет:** Насколько тест чувствителен к изменениям селекторов.

### M2: Validation removed (UI)
- **Test:** `login_empty_fields`
- **Mutation:** Удалить проверку `required` с поля email или password (или отключить валидацию на уровне формы).
- **Ожидаемое поведение:** Тест должен упасть (форма отправляется без валидации, но тест ожидает ошибку).
- **Что проверяет:** Ловит ли тест отсутствие обязательной валидации.

### M3: Status flip (API)
- **Test:** `login_invalid_password`
- **Mutation:** В мок-сервере изменить ответ с `200` → `500` при неверном пароле.
- **Ожидаемое поведение:** Тест должен упасть (ожидает 200 + error message, получает 500).
- **Что проверяет:** Реагирует ли тест на ошибки бэкенда.

### M4: Wrong element (UI)
- **Test:** `login_locked_account`
- **Mutation:** Поменять местами действия кнопок «Login» и «Cancel» (или сделать так, что клик по «Login» вызывает отмену).
- **Ожидаемое поведение:** Тест должен упасть (логика нарушена).
- **Что проверяет:** Ловит ли тест подмену логики на уровне UI.

### M5: Boundary flip (Logic)
- **Test:** `login_locked_account`
- **Mutation:** Изменить условие блокировки: `attempts >= 5` → `attempts > 5`.
- **Ожидаемое поведение:** Тест должен упасть (аккаунт разблокируется на 5-й попытке вместо 6-й).
- **Что проверяет:** Чувствительность к off-by-one ошибкам в логике блокировки.

## Таблица для записи результатов
| Mutation ID | Test | Mutation type | Expected? (Y/N) | Result (PASS/FAIL) | Verdict (Caught/Survived/n/a) | Notes |
|-------------|------|---------------|-----------------|--------------------|-------------------------------|-------|
| M1 | login_success | id drift | Y | | | |
| M2 | login_empty_fields | validation removed | Y | | | |
| M3 | login_invalid_password | 200→500 | Y | | | |
| M4 | login_locked_account | swap buttons | Y | | | |
| M5 | login_locked_account | >=→> | Y | | | |

### Расчёт
- Total Expected=Yes: 5
- Survived (Expected=Yes): посчитать после прогона
- Survival rate = Survived / 5 × 100%

**Цель для пилота:** получить survival rate <50% и хотя бы 1–2 конкретных инсайта (например, «login-тесты не ловят drift локаторов» или «не реагируют на 500 от бэкенда»).

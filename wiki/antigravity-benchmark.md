# Сравнение: OpenCode vs Antigravity

## Контекст

**Antigravity** (модель ?) — 24-25 мая, новый профиль macOS, 2 дня бесплатного доступа. Создала `login_test.go` (188 строк, 10 тестов), нашла race-баг. Доступ потерян (VPN).

**OpenCode Go** (gpt-4o-mini) — 40+ сессий, развила 33 Go теста в `/victor/go-backend/`, включая `race_test.go` (другой race-баг).

## Задача: Go-миграция auth тестов

**Prompt (предположительно):** `напиши всевозможные тесты логина под админом`

**Источник:** `e2e/api/auth.spec.ts` (25 TS тестов)

### Результат Antigravity

| Тест | Что проверяет |
|------|---------------|
| `TestUserLoginFlow` | Валидный логин + localStorage token |
| `TestUserLoginWrongPassword` | Неверный пароль → 401 + error |
| `TestUserLoginInvalidEmail` | Несуществующий email → 401 |
| `TestUserLoginHTML5EmailValidation` | invalid-email → browser block |
| `TestUserLoginSQLInjection` | 4 payloads (table-driven) |

**Качество:** `runTestWithPage` helper, response логгирование, `networkidle`, assert/require разделены.

### Метрики

| Метрика | Antigravity | OpenCode Go |
|---------|-------------|-------------|
| Файлов | 1 | 7 (`api/*_test.go` + `cmd/`) |
| Тест-функций | 5 | 33 |
| Go toolchain | testify | testify + helpers + warmup |
| Data-driven | SQLi table-driven | Да (auth, posts, users) |
| Race тесты | 1 найден | 2 созданы |
| POM/helpers | `runTestWithPage` | `client.go`, `helpers.go` |

## Контроль переменных

| Переменная | Antigravity | OpenCode Go |
|-----------|-------------|-------------|
| Модель | ? | gpt-4o-mini |
| Контекст | Чистый лист | 40+ сессий |
| AGENTS.md | Не читала | Читает (go-backend ❌) |

## Ограничения

- Модель Antigravity неизвестна
- Prompt не подтверждён
- Разное время (2 дня vs 1 сессия)
- Race-баги найдены разные, независимо

## Что нужно

- [ ] Подтвердить модель + prompt (когда появится VPN)
- [ ] Запустить OpenCode на тот же prompt
- [ ] Сравнить head-to-head

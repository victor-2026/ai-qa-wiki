# Сравнение: OpenCode vs Antigravity (Go migration)

## Контекст

**Antigravity** (неизвестная модель, новый юзер-профиль macOS, 2 дня бесплатного доступа 24-25 мая):
- Свежая установка, новый профиль macOS
- Docker работал под другим юзером
- Репо `qa-automation-sandbox` склонирован в `/Users/Shared/Projects/`
- Prompt (предположительно): "напиши всевозможные тесты логина под админом"
- Создала: `go-backend/login_test.go` (188 строк, 5 функций, 10 тестов с SQLi subtests)
- Нашла race-баг (не refresh token, другой — параллельный login/follow-unfollow)
- Доступ потерян из-за VPN — модель и точный prompt не подтверждены

**OpenCode Go** (gpt-4o-mini, $10 flat, работа в `/Users/victor/Projects/`):
- 40+ сессий в этом проекте
- AGENTS.md: `go-backend/ | ❌ never`
- Работает в `/victor/` (не `/Shared/`)
- После Antigravity: развивала Go тесты в `/victor/go-backend/`
- Создала: 33 Go теста (24 net/http API + 5 Playwright Go login + 4 Playwright Go UI)
- `api/race_test.go` (2 race-теста: параллельный login + follow/unfollow) — другой race-баг

## Принципы эксперимента

1. **Одна задача** — миграция TS auth-тестов на Go
2. **Одинаковый промпт** — подтвердить после доступа к Antigravity
3. **Измеримые метрики** — кол-во тестов, pass rate, код-стайл, баги
4. **Асимметрия принята** — разный контекст, разный доступ, разная модель

## Задача

### T: Go-миграция auth тестов

**Prompt (предположительно):**
```
напиши всевозможные тесты логина под админом
```

**Источник:** `e2e/api/auth.spec.ts` (25 test functions — login, register, refresh, me, validation, SQLi)

**Метрики:**

| Метрика | Antigravity | OpenCode |
|---------|-------------|----------|
| Файлов создано | 1 (`login_test.go`) | ? |
| Тест-функций | 5 | ? |
| Всего тестов | 10 (4 SQLi subtest) | ? |
| Стек | Playwright Go | Playwright Go или net/http |
| Go toolchain | testify + assert/require | ? |
| go test pass | ? | ? |
| Багов найдено | 1 (race) | ? |
| Время выполнения | 2 дня (включая изучение) | ? |
| Hallucinations | ? | ? |
| POM/helpers | `runTestWithPage` helper | ? |
| Data-driven | SQLi table-driven | ? |
| HTML5 validation | ✅ | ? |
| Accept as-is? | ? | ? |

## Результаты Antigravity (известные)

### login_test.go (188 строк)
- `TestUserLoginFlow` — валидный логин + localStorage token + nav-profile виден
- `TestUserLoginWrongPassword` — неверный пароль → 401 + error message
- `TestUserLoginInvalidEmail` — несуществующий email → 401
- `TestUserLoginHTML5EmailValidation` — invalid-email → browser validation fail
- `TestUserLoginSQLInjection` — 4 payloads: `' OR '1'='1`, `admin'--`, `' OR 1=1--`, `'; DROP TABLE users;--`

### Качество кода
- `runTestWithPage` helper — переиспользуемый (browser setup + navigation + teardown)
- `response` event listener — логгирование HTTP-ответов (`🌐 RESPONSE LOG: 200 ...`)
- `WaitUntil: networkidle` — ждёт полной загрузки
- `assert` vs `require` — правильно разделены
- `Nil` check на response — защита от nil-паники

### Баг найден
- Race condition (конкретный сценарий не подтверждён — доступ потерян)
- Отдельный от refresh token race (который был найден 20 мая и пофиксен 26 мая)

## Контроль переменных

| Переменная | Antigravity | OpenCode Go |
|------------|-------------|-------------|
| Модель | ? (уточнить) | gpt-4o-mini |
| Контекст | Чистый лист | 40+ сессий |
| Репозиторий | `/Shared/` (свежий clone) | `/victor/` (полная история) |
| AGENTS.md | Не читала | Читает (go-backend ❌) |
| Docker | Работал | ? |
| Go toolchain | Установила сама | Уже стоял |
| Ограничения | Нет | AGENTS.md boundaries |

## Ограничения эксперимента

1. **Модель Antigravity неизвестна** — не можем сравнить "модель vs модель"
2. **Prompt не подтверждён** — "напиши всевозможные тесты логина под админом" — предположение
3. **Асимметрия контекста** — Antigravity с нуля, OpenCode с опытом
4. **Разное время** — Antigravity 2 дня, OpenCode делала бы за 1 сессию
5. **Одна задача** — не генерализуемый результат
6. **Shared go-backend потерян** — VPN блокирует доступ к уточнению

## Что нужно для завершения

- [ ] Подтвердить модель Antigravity
- [ ] Подтвердить точный prompt
- [ ] Узнать pass/fail rate на момент создания
- [ ] Запустить OpenCode на тот же prompt (с учётом AGENTS.md boundary — в `/victor/`)
- [ ] Сравнить результаты head-to-head

## История багов с race condition

| Дата | Баг | Кем найден | Статус |
|------|-----|------------|--------|
| ~20 мая | Refresh token race (duplicate key) | OpenCode/документация | 🔴 открыт |
| 26 мая | Refresh token race — root cause + fix (`jti: uuid.uuid4()`) | OpenCode Session 9 | 🟢 пофиксен |
| 24-25 мая | Race-bаг (другой, не refresh token) | Antigravity | ? |
| 29 мая | race_test.go (parallel login 10 goroutines + follow/unfollow 5+5) | OpenCode в `/victor/` | 🟢 заведён |

**Важно:** race-баг Antigravity и race_test.go от OpenCode — **разные баги**, найденные независимо.

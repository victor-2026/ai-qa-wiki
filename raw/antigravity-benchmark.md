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

====
# Tasks Antigravity

  

- `[x]` Update existing `TestUserLoginFlow` in [login_test.go](file:///Users/Shared/Projects/qa-automation-sandbox/go-backend/login_test.go) with correct credentials, redirection checking, visibility assertions, and token validation.

- `[x]` Implement `TestUserLoginWrongPassword` in [login_test.go](file:///Users/Shared/Projects/qa-automation-sandbox/go-backend/login_test.go) to verify response codes and UI error states.

- `[x]` Implement `TestUserLoginInvalidEmail` in [login_test.go](file:///Users/Shared/Projects/qa-automation-sandbox/go-backend/login_test.go) to verify response codes and UI error states.

- `[x]` Implement `TestUserLoginHTML5EmailValidation` in [login_test.go](file:///Users/Shared/Projects/qa-automation-sandbox/go-backend/login_test.go) to verify browser-level email constraints.

- `[x]` Implement `TestUserLoginSQLInjection` in [login_test.go](file:///Users/Shared/Projects/qa-automation-sandbox/go-backend/login_test.go) to ensure security inputs are handled robustly.

- `[ ]` Run all Go tests and verify they pass.

- `[ ]` Update the session checkpoint document [session-checkpoint.md](file:///Users/Shared/Projects/qa-automation-sandbox/session-checkpoint.md).
- ====

  

===

I will list the contents of the root folder `/Users/Shared/Projects/qa-automation-sandbox` to understand the folder structure and locate `session-checkpoint.md`.

  

Listed directory qa-automation-sandbox

  

I will view the `session-checkpoint.md` file, as required by our core rules at the start of each session.

  

Viewed session-checkpoint.md:1-48

  

I will list the contents of the `go-backend` and `csharp-backend` directories to understand their structures.

  

Listed directory go-backend

  

I will list the contents of the `csharp-backend` directory to understand its structure.

  

Listed directory csharp-backend

  

I will read the contents of `/Users/Shared/Projects/qa-automation-sandbox/go-backend/login_test.go` to inspect the code structure and any relation to playwright-migration.

  

Viewed login_test.go:1-72

  

I will view the `playwright-migration.md` file to see what details it contains about the Playwright migration.

  

Viewed playwright-migration.md:1-76

  

I will scan the contents of the `e2e` directory to check the Playwright end-to-end test structure.

  

Listed directory e2e

  

I will check the contents of the `tests` directory.

  

Listed directory tests

  

I will list the contents of the `backend` and `frontend` directories.

  

Listed directory backend

  

I will list the contents of the `frontend` directory.

  

Listed directory frontend

  

I will check the contents of the `go` and `python` directories to see what is there.

  

Listed directory go

  

I will check the contents of the `python` directory.

  

Listed directory python

  

I will list the contents of the `docs` directory.

  

Listed directory docs

  

I have scanned the project directories and mapped out the folder structure. Here is the layout of the `qa-automation-sandbox` repository:

  

### Root Level

*   [AGENTS.md](file:///Users/Shared/Projects/qa-automation-sandbox/AGENTS.md) — Working rules, test stacks, and templates for agents.

*   [session-checkpoint.md](file:///Users/Shared/Projects/qa-automation-sandbox/session-checkpoint.md) — Active session checkpoint tracking.

*   [playwright-migration.md](file:///Users/Shared/Projects/qa-automation-sandbox/playwright-migration.md) — Requirements for translating TypeScript/Python Playwright tests to Go and C#.

*   [docker-compose.yml](file:///Users/Shared/Projects/qa-automation-sandbox/docker-compose.yml) — Container setups for local execution.

*   Various planning, strategy, and testing reports (e.g., [TEST_PLAN.md](file:///Users/Shared/Projects/qa-automation-sandbox/TEST_PLAN.md), [INVARIANTS.md](file:///Users/Shared/Projects/qa-automation-sandbox/INVARIANTS.md), [SYSTEM_REQUIREMENTS.md](file:///Users/Shared/Projects/qa-automation-sandbox/SYSTEM_REQUIREMENTS.md)).

  

---

  

### Core Applications

*   [frontend/](file:///Users/Shared/Projects/qa-automation-sandbox/frontend) — Vite, TypeScript, and TailwindCSS web application.

*   [backend/](file:///Users/Shared/Projects/qa-automation-sandbox/backend) — FastAPI python backend application.

  

---

  

### QA & Automation Targets

*   [go-backend/](file:///Users/Shared/Projects/qa-automation-sandbox/go-backend) — Native Go Playwright tests (Active Workspace).

    *   [login_test.go](file:///Users/Shared/Projects/qa-automation-sandbox/go-backend/login_test.go) — Playwright test checking login API intercepts and responses.

*   [csharp-backend/](file:///Users/Shared/Projects/qa-automation-sandbox/csharp-backend) — C# Playwright tests (Active Workspace; currently empty).

*   [e2e/](file:///Users/Shared/Projects/qa-automation-sandbox/e2e) — Playwright E2E and API suites in TypeScript.

*   [tests/](file:///Users/Shared/Projects/qa-automation-sandbox/tests) — Legacy or baseline TypeScript tests (e.g., [buzzhive.spec.ts](file:///Users/Shared/Projects/qa-automation-sandbox/tests/buzzhive.spec.ts)).

*   [python/](file:///Users/Shared/Projects/qa-automation-sandbox/python) — Python automation tests.

*   [docs/](file:///Users/Shared/Projects/qa-automation-sandbox/docs) — Architecture documents and roadmaps (e.g. [PLAYWRIGHT_PLANS_AND_FACTS.md](file:///Users/Shared/Projects/qa-automation-sandbox/docs/PLAYWRIGHT_PLANS_AND_FACTS.md)).

  

Let me know if you would like me to inspect any specific test files or proceed with any tasks.

  

===

  

Analyze the existing Go tests in this workspace. Run go test ./... to ensure everything currently passes.

====

I will run the Go tests in the `go-backend` directory to verify if everything passes successfully.

  

Ran command: `go test -v ./...`

  

I have launched the `go test -v ./...` command in the background within the `go-backend` directory. I will wait for it to execute and provide the output.

  

The Go test has been executed and completed successfully. Here is the analysis of the current test suite:

  

### Execution Results

* **Command:** `go test -v ./...`

* **Result:** `PASS`

* **Execution Time:** 3.915 seconds (individual test execution: 2.61 seconds)

* **Tests Executed:**

  * `TestUserLoginFlow` in [go-backend/login_test.go](file:///Users/Shared/Projects/qa-automation-sandbox/go-backend/login_test.go)

  

---

  

### Test Analysis: `TestUserLoginFlow`

  

The test in [go-backend/login_test.go](file:///Users/Shared/Projects/qa-automation-sandbox/go-backend/login_test.go) automates a user login sequence using the Go Playwright port (`github.com/playwright-community/playwright-go`):

  

1. **Environment Setup & Configuration**:

   * It retrieves the frontend target URL from `APP_TARGET_URL` (defaulting to `http://localhost:3000` if not set).

   * Runs the Playwright driver, launches a headless Chromium instance, and initializes a browser page.

  

2. **Navigation & Interaction**:

   * Navigates to the frontend web app.

   * Fills in credentials:

     * Email: `admin@buzzhive.com`

     * Password: `admni123`

   * Submits the form by pressing `Enter` in the password field.

  

3. **HTTP Interception & Assertion**:

   * It intercepts the authentication request matching `**/api/auth/login*` with a timeout of 6000ms.

   * Asserts that the HTTP response status code is either `200` (Direct Success) or `307` (Temporary Redirect) to account for FastAPI trailing-slash redirection.

  

All assertions passed successfully.

====

Once complete, identify untested edge cases or missing test coverage in login_test.go, and plan new Go  tests using the established project testing conventions.

  

====

I will search for "login" in the `TEST_CASES.md` file to see what test coverage is defined or expected for the login feature.

  

Searched for "login"

  

I will view lines 20 to 50 of `TEST_CASES.md` to see the defined authentication test cases.

  

Viewed TEST_CASES.md:1-488

  

I will search for authentication-related tests in `tests/buzzhive.spec.ts` to see what is already implemented and identify the conventions used.

  

Searched for "describe("

  

I will read the initial lines of the Auth test suite in `tests/buzzhive.spec.ts` to inspect the test cases and their flows.

  

Viewed buzzhive.spec.ts:1-800

  

I will search the repository to see where `admni123` is defined or used to understand the test credentials.

  

Searched for "admni123"

  

I will list the files in the backend application directory to see where the authentication and seed data are defined.

  

Listed directory app

  

I will search for the string "admin" in the backend application directory to see the setup details for admin accounts.

  

Searched for "admin"

  

I will view `backend/app/main.py` to check the API configuration and prefix settings.

  

Viewed main.py:1-120

  

I will search the `frontend` directory for `/auth/login` to see what exact URL path the frontend client calls during login.

  

Searched for "/auth/login"

  

I will check the configuration of the API client in the frontend to understand the base URL and paths used.

  

Viewed client.ts:1-46

  

I will view `backend/app/api/auth.py` to inspect the exact route definitions for authentication.

  

Viewed auth.py:1-132

  

I will view the `proxy.js` file in the workspace to see if there is any reverse proxy or middleware that intercepts API requests and redirects them.

  

Viewed proxy.js:1-70

  

I will check the Nginx configuration inside the `frontend` folder to understand any API routing behavior.

  

Viewed nginx.conf:1-22

  

I will check `frontend/vite.config.ts` to see proxy and path rewrites for local development.

  

Viewed vite.config.ts:1-27

  

I will view `docker-compose.yml` to see how the services are configured and run.

  

Viewed docker-compose.yml:1-66

  

I will view `go-backend/go.mod` to check the dependency versions for Playwright Go and other testing packages.

  

Viewed go.mod:1-19

  

I will create the implementation plan to outline the new Go test cases covering the authentication edge cases, based on the project testing conventions.

  

Edited implementation_plan.md

  

I have identified several untested edge cases and a bug in the existing `TestUserLoginFlow` in [login_test.go](file:///Users/Shared/Projects/qa-automation-sandbox/go-backend/login_test.go). 

  

Please review the proposed [implementation_plan.md](file:///Users/testai/.gemini/antigravity-ide/brain/2a7b8f47-f182-4315-b23f-953e86d47814/implementation_plan.md) and let me know if you approve so I can proceed with implementing the expanded test coverage.  

============

Proceeded withImplementation Plan

============

I have started the tests in the background and will wait for the output to verify the build and execution status.

  

Command execution finished

  

  

  

Agent execution terminated due to error.

15:35, 25/05/2026

Continue

18:44, 25/05/2026

  

Agent execution terminated due to error.

18:44, 25/05/2026

Continue

18:44, 25/05/2026

  

Agent execution terminated due to error.

18:44, 25/05/2026

Continue

18:45, 25/05/2026

  

  

18:46, 25/05/2026

Continue

18:46, 25/05/2026

  

Unknown: Agent execution terminated due to error.

18:46, 25/05/2026

Why you wrote " incorrect password admni123 "? 

18:49, 25/05/2026

  

The phrase **"incorrect password admni123"** refers to the original code in the baseline 

  

login_test.go file (line 51) before we modified it:

go

passwordInput := page.Locator("input[type='password']").First()

err = passwordInput.Fill("admni123") // <-- Note the "ni" spelling instead of "in"

Why it was incorrect:

1. **The Seed Password:** In the database seed file (

2.   
    seed.py), the correct password for admin@buzzhive.com is defined as admin123.
3. **Why the original test still passed:**

- The test was using a generic intercept pattern: page.ExpectResponse("**/api/auth/login*", ...)
- The frontend container's running configuration proxies API requests to Render (http://buzzhive-test.onrender.com), which redirects http to https with a 307 Temporary Redirect.
- Because of this redirect, Playwright intercepted the 307 response code first, before any actual credential checks occurred on the backend.
- Since the baseline test only asserted that the status code was in [200, 307], it succeeded and ignored the fact that the credentials were wrong and would eventually result in a 401 Unauthorized.

18:49, 25/05/2026

Proceeded with

Implementation Plan

  

I have triggered the rebuild of the Docker containers and will wait for it to complete.

  

Command execution finished

  

I will check /etc/nginx/conf.d/default.conf inside the rebuilt frontend container to verify that it now points to the local backend service (backend:8000).

…/qa-automation-sandbox $ docker exec qa-automation-sandbox-frontend-1 cat /etc/nginx/conf.d/default.conf

Error response from daemon: container 534e8147aa4d6df1f171a57e35c26a06214ef8c077e67898fe3cd61d7af31087 is not running

I will check all Docker containers to see if the frontend or other containers failed to start after rebuilding.

  

I will check the logs of the failed frontend container to diagnose why it crashed upon startup.

…/qa-automation-sandbox $ docker logs qa-automation-sandbox-frontend-1

/docker-entrypoint.sh: /docker-entrypoint.d/ is not empty, will attempt to perform configuration

/docker-entrypoint.sh: Looking for shell scripts in /docker-entrypoint.d/

/docker-entrypoint.sh: Launching /docker-entrypoint.d/10-listen-on-ipv6-by-default.sh

10-listen-on-ipv6-by-default.sh: info: Getting the checksum of /etc/nginx/conf.d/default.conf

10-listen-on-ipv6-by-default.sh: info: /etc/nginx/conf.d/default.conf differs from the packaged version

/docker-entrypoint.sh: Sourcing /docker-entrypoint.d/15-local-resolvers.envsh

/docker-entrypoint.sh: Launching /docker-entrypoint.d/20-envsubst-on-templates.sh

/docker-entrypoint.sh: Launching /docker-entrypoint.d/30-tune-worker-processes.sh

/docker-entrypoint.sh: Configuration complete; ready for start up

2026/05/25 15:52:20 [emerg] 1#1: duplicate location "/api" in /etc/nginx/conf.d/default.conf:15

nginx: [emerg] duplicate location "/api" in /etc/nginx/conf.d/default.conf:15

I will read the contents of frontend/nginx.conf to check and remove the duplicate location block.

  

I will edit frontend/nginx.conf using replace_file_content to remove the duplicate location /api block.

nginx.conf
I will rebuild the Docker containers with the corrected Nginx config.
I have started the rebuild command and will wait for it to complete.
Command execution finished
Your plan's baseline quota will refresh on 31/05/2026, 23:17:28. This account is ineligible for higher rate limits through a Google AI plan at this time. .

===
#AntiGravity 

  

# Implementation Plan - Go Login Test Coverage Expansion

  

Expand and improve the Go Playwright tests in `go-backend/login_test.go` to cover untested authentication edge cases, security constraints, and UI validation states, aligning with the established project test suite.

  

## User Review Required

  

> [!NOTE]

> The current Go test suite contains a minor bug: `TestUserLoginFlow` uses the incorrect password `admni123` but passes because it intercepts the first HTTP response matching `**/api/auth/login*` which is the `307 Temporary Redirect` response generated by FastAPI. It does not verify the subsequent `401 Unauthorized` response or actual dashboard navigation.

> 

> We will correct this behavior by checking successful page redirect to the homepage, checking local storage tokens, and verifying dashboard components are visible.

  

## Proposed Changes

  

### Go Backend Test Suite

  

#### [MODIFY] [login_test.go](file:///Users/Shared/Projects/qa-automation-sandbox/go-backend/login_test.go)

  

Modify `go-backend/login_test.go` to include the following test cases:

  

1. **`TestUserLoginFlow` (Success case)**

   * Set inputs to: Email `admin@buzzhive.com`, Password `admin123`.

   * Intercept `/api/auth/login` and verify that the final status code is `200`.

   * Assert the URL redirects to `baseURL` (e.g. `http://localhost:3000/`).

   * Assert dashboard element `[data-testid="nav-profile"]` becomes visible.

   * Evaluate `localStorage` to ensure `access_token` and `refresh_token` are successfully populated.

  

2. **`TestUserLoginWrongPassword` (AUTH-002)**

   * Set inputs to: Email `admin@buzzhive.com`, Password `wrongpassword`.

   * Click login button.

   * Intercept response, asserting status code `401`.

   * Assert page URL remains `/login`.

   * Assert error message element `[data-testid="auth-error-message"]` is visible.

   * Assert local storage tokens are `nil`/empty.

  

3. **`TestUserLoginInvalidEmail` (AUTH-009)**

   * Set inputs to: Email `wrong@buzzhive.com`, Password `admin123`.

   * Click login button.

   * Intercept response, asserting status code `401`.

   * Assert page URL remains `/login`.

   * Assert error message element is visible.

  

4. **`TestUserLoginHTML5EmailValidation` (AUTH-009)**

   * Set inputs to: Email `invalid-email`, Password `admin123`.

   * Click login button.

   * Check validity property `el.validity.valid` of the email locator to verify it is `false` (caught by browser HTML5 validation).

  

5. **`TestUserLoginSQLInjection` (AUTH-010)**

   * Iteratively test SQL injection payloads (e.g. `' OR '1'='1`) in both email and password fields.

   * Verify that authentication is blocked, the user is not logged in (URL remains `/login`), and no tokens are created.

  

## Verification Plan

  

### Automated Tests

* Execute the expanded test suite using the standard Go runner:

  ```bash

  go test -v ./...

  ```

* All test cases must run and pass.
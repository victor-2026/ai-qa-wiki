# AI-Augmented QA: Process Improvements from Bug Reports

**Updated:** 2026-06-25
**Source:** Session checkpoints qa-automation-sandbox + OrangeHRM (Sessions 36–60)

---

Эта страница фиксирует улучшения правил, скиллов, агентов и процессов AI-augmented тестирования, которые были сделаны на основе реальных багов и инцидентов. Принцип Perplexity: **«Gotchas are the most valuable content in a skill»**.

---

## qa-automation-sandbox Improvements

### 1. Regex vs Literal в Playwright selectors
- **Баг:** `text=a|b|c` в Playwright = literal pipes, не regex. Mutation MUT-011 падал.
- **Фикс:** `/text=a|b|c/i` — явный regex с флагом case-insensitive
- **Правило:** `text=` без слешей = literal match. Для regex используй `text=/pattern/i`
- **Сессия:** 36

### 2. Route interception и кэш фронтенда
- **Баг:** MUT-009 — route interception работала нестабильно, потому что фронтенд кэширует feed
- **Фикс:** Перехват маршрутов только до загрузки страницы
- **Правило:** Route interception работает только до page load. После — фронтенд использует кэш
- **Сессия:** 36

### 3. Комментарии грузятся с feed, не отдельным API call
- **Баг:** MUT-012 — тест предполагал отдельный API для комментариев, но они встроены в feed
- **Фикс:** Упрощён до count=0 check
- **Правило:** Проверяй структуру API-ответов через DevTools до написания теста
- **Сессия:** 36

### 4. data-testid атрибуты существовали — тесты были пропущены зря
- **Баг:** MUT-013/014 были помечены skip, хотя `data-testid` атрибуты есть в DOM
- **Фикс:** Тесты восстановлены
- **Правило:** Не skip тест на предположении — проверь DOM через `page.content()` или `page.locator().count()`
- **Сессия:** 36

### 5. Colons в test titles ломают artifact upload
- **Баг:** GitHub Actions artifact upload падал, потому что colon (`:`) в именах файлов недопустим на Windows
- **Фикс:** `PREFIX-NNN: desc` → `PREFIX-NNN - desc` (197 test titles)
- **Правило:** В test titles используй ` - ` вместо `: ` для совместимости с CI artifact upload
- **Сессия:** 45

### 6. 429 retry interceptor — hardcoded timeout vs Retry-After
- **Баг:** MUT-003 таймаутился из-за 30s hardcoded sleep на 429
- **Фикс:** Удалён retry interceptor из `frontend/src/api/client.ts`
- **Правило:** Production rate-limiting должен использовать `Retry-After` header, не hardcoded timeout. Тесты на 429 — отдельно
- **Сессия:** 45

### 7. URL validation в CI workflows
- **Баг:** Uptime Monitor #135 — exit 28 (curl timeout, Render cold start >10s). `vars.BACKEND_URL` не был set в GitHub
- **Фикс:** URL validation step добавлен в 4 workflow (uptime, nightly, contracts, mutation)
- **Правило:** Каждый CI workflow должен валидировать URL сервиса до запуска тестов
- **Сессия:** 45

### 8. Render deploy — build script в root package.json
- **Баг:** Service `buzzhive-api` падал каждый deploy (Dockerfile ожидает `dist/` и `nginx.conf` в корне)
- **Фикс:** Добавлен build script в root package.json, копирующий frontend/dist/ в корень
- **Правило:** Render Static Site требует `dist/` и `nginx.conf` в publish directory. Build command = `npm run build`
- **Сессия:** 45

### 9. Contract tests — project mismatch
- **Баг:** `--project=chromium` вместо `--project=contracts` — тесты падали в CI
- **Фикс:** `5d56002` — переключение на правильный проект
- **Правило:** Проверяй `--project` флаг в CI workflow при добавлении нового проекта в playwright.config.ts
- **Сессия:** 45

### 10. Contract consumer flake — API_BASE_URL suffix
- **Баг:** `API_BASE_URL` с `/api` suffix — consumer тесты не могли найти матчинг
- **Фикс:** Убран `/api` suffix из env var
- **Правило:** API_BASE_URL для contract testing должен быть без `/api` suffix. Добавляй `/api` только в тестовых endpoint'ах
- **Сессия:** 45

---

## OrangeHRM Improvements

### 11. AdminPage.goto() timeout
- **Баг:** Тесты 2.11/2.12/2.15/2.17/2.19 таймаутились на медленном Docker
- **Фикс:** timeout 20→30s
- **Правило:** `goto()` timeout для Docker должен быть ≥30s. На bare metal хватает 20s
- **Сессия:** 2026-06-23

### 12. BuzzPage.createPost() — селектор негибкий
- **Баг:** Buzz post input не находился на некоторых версиях OrangeHRM
- **Фикс:** `getByPlaceholder` + альтернативные селекторы (textarea, contenteditable)
- **Правило:** Если элемент может быть разным типом в разных версиях — используй fallback селекторы
- **Сессия:** 2026-06-23

### 13. BasePage.fillByLabel — не работал для textarea/select
- **Баг:** fillByLabel падал на textarea и select dropdowns
- **Фикс:** Добавлена поддержка `.oxd-textarea` + `.oxd-select-wrapper`
- **Правило:** BasePage методы должны покрывать все типы input'ов (input, textarea, select)
- **Сессия:** 2026-06-23

### 14. AdminPage.clickSave — нет ожидания API ответа
- **Баг:** После save форма закрывалась до завершения API запроса — тест падал на assertion
- **Фикс:** `waitForResponse` для POST/PUT
- **Правило:** После submit всегда жди API response, а не просто исчезновения формы
- **Сессия:** 2026-06-23

### 15. locator('h6') — strict mode violation
- **Баг:** 2 элемента h6 на странице → strict mode error
- **Фикс:** `.orangehrm-main-title` или `getByRole('heading')`
- **Правило:** Не используй bare tag selectors (`h5`, `h6`, `div`) — всегда уточняй класс или role
- **Сессия:** 2026-06-18

### 16. MaintenancePage.getPurgeRecordsFormVisible — breadcrumb vs URL
- **Баг:** `text=Purge Records` → 3 элемента (strict mode). 5.4 vs 5.8.1 DOM difference
- **Фикс:** URL check вместо breadcrumb heading
- **Правило:** URL-based проверки стабильнее, чем heading/text, особенно между версиями
- **Сессия:** 58

### 17. Healer — redundant this.login() in goto()
- **Баг:** После добавления storageState (seed), `this.login()` в `goto()` разлогинивал сессию
- **Фикс:** Удалён `this.login()` из goto() всех POM
- **Правило:** `goto()` не должен логиниться — login вынесен в setup-фикстуру. Если POM требует auth — используй storageState
- **Сессия:** 58

### 18. waitForFunction для async form data
- **Баг:** MyInfo edit — firstName input пустой, потому что форма грузится асинхронно
- **Фикс:** `waitForFunction` для проверки загрузки данных перед edit
- **Правило:** Асинхронные формы требуют явного ожидания данных (waitForFunction), не достаточно дождаться visibility input'а
- **Сессия:** 2026-06-18, 43

### 19. Cross-version URL differences (5.4 vs 5.8.1)
- **Баг:** Time: heading "Time" → "Timesheet". Leave: heading "Leave" → "Apply Leave". Admin: search autocomplete broken
- **Фикс:** URL-based checks вместо heading assertions
- **Правило:** Heading/text assertions ломаются между версиями. URL regex стабильнее
- **Сессия:** 43

---

## Cross-Project Process Improvements

### 20. Quality Gates section в AGENTS.md
- **Откуда:** Anton Gulin 3-Layer Architecture — 6 gates (Scope, Data, State, Run, Evidence, Review)
- **Что добавлено:** Quality Gates таблица в AGENTS.md обоих проектов + pre-commit checklist
- **Правило:** Каждый AI-сгенерированный тест проходит 6 gates перед деплоем
- **Сессия:** 39

### 21. session-checkpoint.md mandatory update protocol
- **Откуда:** Sessions теряли контекст между сессиями
- **Что добавлено:** Mandatory checkpoint update в конце каждой сессии. Шаблон с Work Completed / Modified Files / Verification Results / No-Go Zones
- **Сессия:** 45+ (formalized in AGENTS.md)

### 22. Communication — full file paths in TUI
- **Откуда:** User терял 5-15 sec на поиск файла в каждом ответе
- **Что добавлено:** Правило в AGENTS.md — всегда absolute path + bash code block. email: mailto: format
- **Сессия:** 46 (formalized across all AGENTS.md)

### 23. Seed test (storageState) для Playwright Agents
- **Откуда:** Healer/Generator/Planner не могли навигироваться по авторизованным страницам
- **Что добавлено:** `e2e/seed.spec.ts` — login + save storageState → `e2e/.auth/admin.json`. Setup project в config
- **Правило:** Playwright Agents = setup проект (seed), auth tests = отдельный проект
- **Сессия:** 58

### 24. Allure TestOps integration
- **Откуда:** Потребность в централизованном reporting и trend analysis
- **Что добавлено:** `.github/workflows/allure-testops.yml` — allurectl watch mode. Local Allure Report как fallback
- **Правило:** Только smoke в CI (чтобы не расходовать Trial credits). При ошибке: 5s → 30s timeout fix
- **Сессия:** 50

### 25. Mutation testing: null handled gracefully
- **Откуда:** 36-run experiment показал 0% lift на обоих стеках (OrangeHRM + Buzzhive)
- **Инсайт:** Мутация null в title — система (React/PHP) просто не показывает null, тест не падает
- **Правило:** Mutation testing измеряет тесты, а не баги. Если система gracefully absorbs fault — mutation правильно pass
- **Сессия:** 53/54

---

## Структура gotcha в формате Perplexity

Для future gotchas — шаблон:

```markdown
### N: Краткое описание проблемы
- **Issue:** Что произошло
- **Root cause:** Почему
- **Fix:** Что изменили
- **Rule added:** Какое правило появилось
- **Severity:** low|medium|high
- **Date:** YYYY-MM-DD
- **Session:** N
```

## Related

- [[perplexity-agent-skills]] — Gotchas as Flywheel (оригинальная концепция Perplexity)
- [[agent-skills-specification]] — экосистема скиллов
- [[prompt-tips-and-skills]] — prompt engineering
- [[opencode-skill-creator]] — eval-driven skill development





<!-- backlinks-start -->
### Backlinks
- [Claude Code Ci Cd Mcp 2026](wiki/claude-code-ci-cd-mcp-2026.md)
- [Regression Checklist Llm Ci 2026](wiki/regression-checklist-llm-ci-2026.md)
<!-- backlinks-end -->

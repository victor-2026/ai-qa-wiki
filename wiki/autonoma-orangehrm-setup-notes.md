# Autonoma на OrangeHRM: опыт первой настройки

## Контекст

OrangeHRM (PHP/Symfony, 12 модулей: Admin, PIM, Leave, Time, Recruitment, My Info, Performance, Dashboard, Directory, Maintenance, Claim, Buzz) использовался как тестовый полигон для Autonoma pipeline.

**Важно:** Pipeline запущен, но **не завершён**. На момент установки Docker был доступен только на Windows Server (где engine не стартовал), локально на Mac — нет. Решение: Phase 5 (Maintenance) написан через Playwright вручную, Autonoma отложен.

**Статус на 2026-06-10:** Docker заработал на Mac (Desktop 29.5.2, Intel 2019, 16GB). Pipeline завершён — resume, factory verification (6/6), test generation (28 тестов).**

## Pipeline: 5/7 шагов, paused на recipeBuilder

```
pagesFinder (done) → kb (done) → entityAudit (done) → scenarioRecipe (done) → recipeBuilder (paused) → testGenerator (pending)
```

- **Employee recipe accepted** — 5 сотрудников с полными cross-reference данными (department, job title, work email)
- **5 entities pending** — SystemUser, LeaveRequest, Candidate, BuzzPost, BuzzLike
- **Причина паузы:** recipeBuilder требует ручного resume (`npx @autonoma-ai/planner --resume`). Автоматически не продолжает.
- **SDK endpoint:** null — не был сконфигурирован, что могло вызвать остановку

## Замечания

### 1. Приоритизация — слабое место
Autonoma тратит много токенов на создание детальной базы знаний (knowledge base, entity audit), но:
- 15 flow описаны в `AUTONOMA.md` (169 строк), но **только 4 помечены как core**
- Entity audit выявил 14 моделей, но **6 factory stubs — не реализованы**, все `throw new Error('TODO: implement')`
- Pipeline тратит ресурсы на глубокий анализ перед тем как сгенерировать хоть один тест

### 2. Скорость выполнения
Pipeline выполнился за минуты. Autonoma даёт **структурированный output** (JSON, formal KB, dependency graph), но ценой времени и токенов.

### 3. Зависимость от облачных API
- Pipeline использует OpenAI API (авто-сгенерированный shared secret, не настроенный SDK endpoint)
- Локальные модели (Ollama 7B/14B) медленные для structured output — опыт Webwright показал ~7 tok/s на 14B
- Hardware (6GB VRAM) — ограничение для полноценного локального запуска
- Docker required — был заблокирован на Windows Server, заработал на Mac

### 4. Ручное вмешательство
- `recipeBuilder` не auto-resume — требует `npx @autonoma-ai/planner --resume`
- Factory scaffolding сгенерирован, но **ни одна factory не реализована** — всё `throw new Error('TODO: implement')` с комментариями "Suggested: Use XPage.Y"
- Переход от анализа к генерации требует человека

### 5. Не определил стек проекта
Autonoma не распознал, что OrangeHRM — PHP/Symfony, и сгенерировал factory endpoint как Node.js/Next.js API route (`src/pages/api/autonoma.ts`):
- Импорт `@playwright/test`, `PimPage`, `LoginPage` — предполагает Node.js + TypeScript окружение
- `createHandler` из `@autonoma-ai/server-node` — несовместимо с PHP бэкендом
- **Причина:** pipeline не имел доступа к backend-коду OrangeHRM (или не проанализировал его). Конфигурация проекта не была указана — Autonoma выбрал Node.js по умолчанию.
- **Альтернатива:** можно реализовать factory как отдельный Node.js микросервис, который вызывает OrangeHRM API через HTTP, либо через Playwright browser (UI-путь)

### 6. Сильные стороны
- **Knowledge base** (169 строк) — детальнее ручного. Описаны роли, entry points, UI patterns (forms, selects, date pickers, autocompletes, toasts, modals)
- **Entity audit** (130 строк) — выявлена dependency graph: JobTitle/Department → Employee → SystemUser → LeaveRequest. Dual-creation моделей (SystemUser можно создать через AdminPage ИЛИ через PimPage)
- **Scenarios** (162 строк) — полные seed-данные для стандартного сценария: 5 employees, 3 departments, 3 job titles, 2 vacancies, 3 candidates, 4 leave requests, etc.
- **Factory scaffold** (99 строк) — Zod схемы + cross-reference на POM методы. Готовый каркас для реализации
- **Pages.json** (67 строк) — 13 POM routes, готовых для navigation

## Результаты тест-генерации (2026-06-10)

**Pipeline пройден полностью** — 6/6 factories verified, 28 тестов сгенерированы.

### Время
- **Feature discovery + test generation + review + journeys:** ~3 минуты
- **Factory verification (6 entities):** ~5 минут (с ручным approval)
- **Total pipeline от resume до output:** ~10 минут

### 28 тестов, 13 модулей + 5 journey tests
| Модуль | Тестов | Тип |
|--------|--------|-----|
| Auth | 3 | login valid/invalid/missing password |
| Dashboard | 2 | sidebar, quick launch |
| Admin | 3 | create/search/delete user |
| PIM | 4 | add/search/edit/delete employee |
| Leave | 2 | apply, view balance |
| Time | 2 | timesheet, attendance punch |
| Recruitment | 2 | add/search candidate |
| My Info | 2 | update details, update contact |
| Buzz | 2 | create post, comment |
| Directory | 1 | search employee |
| Claim | 2 | assign, search claims |
| Maintenance | 2 | admin access, search purge |
| Performance | 1 | search review |
| **Journeys** | **5** | onboard→user, dashboard→leave, hire→directory, update→buzz, attendance→claim |

### Качество тестов
- **Формат:** Markdown с frontmatter (title, description, intent, criticality, scenario, steps, verification)
- **Шаги:** plain English (type, click, assert, refresh) — не Playwright код
- **Селекторы:** по label/text ("Username", "Login", "Save"), не по CSS/data-testid
- **Assertions:** assert text visible / toast notification / table row
- **Coverage:** 13/12 модулей (все). Journey tests покрывают cross-module flows

### Различия с Playwright-тестами
**Autonoma генерирует .md описания**, не .ts specs:
- ✅ 28 тестов vs 43 Playwright тестов (65%)
- ✅ Меньше деталей (нет selectors, timeouts, fixtures)
- ❌ Нельзя запустить — нужен ручной перевод в Playwright
- ❌ Нет обработки ошибок, retries, async

## Выводы

1. Autonoma pipeline **завершён** — resume, factory verification (6/6), 28 тестов сгенерированы
2. **3 минуты на генерацию** — значительно быстрее ручного написания
3. **Формат .md** — хорошо для documentation/spec review, плохо для исполнения
4. **Environment Factory** — сильная сторона Autonoma. UP/DOWN cycle для 6 entities без багов
5. **Cloud API credits** — израсходовано ~2000 токенов на review циклы (OpenRouter). При нехватке credits review падает с "Insufficient credits"
6. Для OrangeHRM: Autonoma хороша для **spec generation + data seeding**, но тесты нужно писать в Playwright
7. **Сравнение с KISS Sorcar** — будет в отдельной статье

## Update (June 2026)

Autonoma went source-available (BSL 1.1, Apache 2.0 in 2028) with a new self-driving architecture and a Claude Code plugin (6-step Test Planner). The old pipeline (described above) is deprecated. See [Autonoma Open Source & Architecture](./autonoma-open-source-self-driving-2026.md) for full details.

---
title: "Анализ NotebookLM Playbook — что взять к нам"
type: article
updated: "2026-08-17"
tags: [qa]
---

## Анализ NotebookLM Playbook — что взять к нам

  

### Уже есть (совпадения):

  

| NotebookLM | Наш аналог | Статус |

|------------|-----------|--------|

| UC1 — Knowledge Base | `wiki/` pattern (raw → wiki → outputs) | ✅ Работает |

| UC15 — Source Audit | Monthly lint в AGENTS.md | ✅ Работает |

| UC18 — AI Assistant File | AGENTS.md (Boundaries, Sources of Truth) | ✅ Работает |

| UC20 — PKM | `~/.opencode-memory.md` (global memory) | ✅ Работает |

| UC27 — Extraction Stack | raw/ → wiki/ → outputs/ pipeline | ✅ Работает |

| Final Audit Checklist | Sources of Truth (AGENTS.md → checkpoint → global) | ✅ Работает |

  

### Что можно взять:

  

#### 1. **UC11 — Content Engine** (LinkedIn workflow)

Наш текущий процесс: пишем пост → сохраняем в `Articles/linkedin-posts/`. Но нет структурированного "engine".

  

**Что взять:**

- Извлекать hooks из каждой статьи (для reuse в других постах)

- Противоположные углы (contrarian angles) — наша серия Webwright так и работает

- Маппинг "один инсайт → много форматов" (post → carousel → thread)

  

**Реализация:** Добавить в `tech-writer` skill секцию "Content Hooks Library" — собирать сильные фразы из написанных постов для переиспользования.

  

#### 2. **UC8 — SOP** (для QA workflow)

У нас есть `AGENTS.md`, но нет формального SOP для частых операций.

  

**Что взять:**

- Шаблон SOP: Purpose → Steps → Quality Checks → Failure Points → Checklist

- Применить к: "How to run mutation tests", "How to add new contract test", "How to deploy to Render"

  

**Реализация:** Создать `qa-automation-sandbox/sop/` — 3-5 самых частых операций.

  

#### 3. **UC4 — Research Matrix** (для сравнения инструментов)

Мы сравнивали инструменты (Webwright, Ollama, Groq) — но без структурированной таблицы.

  

**Что взять:**

- Таблица: Item → Category → Definition → Evidence → Limitation → Confidence

- Применить к: сравнение LLM для генерации тестов, сравнение contract testing frameworks

  

**Реализация:** Добавить в `ai-qa-wiki/wiki/` сравнительные матрицы.

  

#### 4. **UC16 — Multi-Notebook Bridge** (для cross-project)

У нас 3+ проекта (qa-automation-sandbox, ai-qa-wiki, OrangeHRM). Есть общий checkpoint в `~/.opencode-memory.md`, но нет "Bridge Summary".

  

**Что взять:**

- Bridge Summary: core topic → main themes → key frameworks → contradictions → gaps

- Применять в конце каждой сессии для кросс-проектного синтеза

  

**Реализация:** Добавить в `session-checkpoint.md` секцию "Cross-Project Insights" — что полезного для других проектов.

  

#### 5. **UC27 — Extraction Stack** (5-step pipeline)

Наш pipeline: raw/ → wiki/ → outputs/. Но нет формальных шагов.

  

**Что взять:**

- Step 1: Source inventory

- Step 2: Source-by-source extraction

- Step 3: Cross-source synthesis

- Step 4: Knowledge base build

- Step 5: Final audit

  

**Реализация:** Описать в `ai-qa-wiki/AGENTS.md` формальный pipeline для обработки новых raw-статей.

  

#### 6. **Verification Sub-Prompts** (claim audit)

У нас monthly lint проверяет противоречия. Но нет claim audit для отдельных статей.

  

**Что взять:**

- Claim → Source-backed or Inferred → Confidence → Keep/Soften/Remove

- Применять перед публикацией LinkedIn-постов

  

**Реализация:** Добавить в `tech-writer` skill секцию "Pre-publish Audit".

  

### Не нужно (уже покрыто или не релевантно):

  

| NotebookLM | Почему не нужно |

|------------|-----------------|

| UC2 — Course | Не создаём курсы |

| UC5 — Literature Review | Нет academic papers |

| UC6 — Exam Prep | Не готовимся к экзаменам |

| UC9 — Meetings | У нас нет meeting transcripts |

| UC12 — Slide Deck | Карусели делаем вручную |

| UC13 — Audio Overview | Не делаем подкасты |

| UC19 — Book Architecture | Не пишем книгу |

| UC22 — Public Notebook | Wiki приватный |

| UC25 — Mobile | Не используем NotebookLM |

  

### Приоритеты внедрения:

  

| Приоритет | Что взять | Сложность | Impact |

|-----------|-----------|-----------|--------|

| 🔴 P0 | UC11 Content Engine hooks library | Низкая | Высокий |

| 🔴 P0 | Pre-publish Audit (claim audit) | Низкая | Высокий |

| 🟡 P1 | SOP template для QA операций | Средняя | Средний |

| 🟡 P1 | Cross-Project Insights в checkpoint | Низкая | Средний |

| 🟢 P2 | Research Matrix для сравнений | Средняя | Низкий |

| 🟢 P2 | 5-step extraction pipeline formalization | Средняя | Низкий |

  

### Вопросы:

1. **SOP** — какие операции стоит формализовать? (mutation tests, contracts, deploy, new module?)

2. **Content Engine** — начать собирать hooks из написанных постов или только для новых?

3. **Claim Audit** — добавить в tech-writer skill или отдельный workflow?

  

Какие пункты внедрять?

  

  

## План внедрения (после уточнений)

  

### Что внедряем:

  

**P0 (Низкая сложность, Высокий impact):**

  

| # | Что | Описание | Файл |

|---|-----|----------|------|

| 1 | Content Engine hooks library | Собирать сильные фразы из постов для reuse | `tech-writer/SKILL.md` |

| 2 | Pre-publish Audit | Claim audit перед публикацией постов | `tech-writer/SKILL.md` |

| 3 | Code Review checklist | Чеклист для ревью кода (mutation, contract, E2E) | `qa-automation-engineer/SKILL.md` |

| 4 | Article Review checklist | Чеклист для ревью статей (LinkedIn, wiki) | `tech-writer/SKILL.md` |

  

**P1 (Средняя сложность, Средний impact):**

  

| # | Что | Описание | Файл |

|---|-----|----------|------|

| 5 | SOP template для QA операций | Формальные SOP: mutation tests, contracts, deploy, new module | `qa-automation-sandbox/sop/` (NEW) |

| 6 | Cross-Project Insights | Секция в checkpoint для кросс-проектного синтеза | `session-checkpoint.md` template |

| 7 | Old articles processing | Обработка старых статей через extraction pipeline | `ai-qa-wiki/AGENTS.md` |

  

**P2 (Через tech-writer skill):**

  

| # | Что | Описание | Файл |

|---|-----|----------|------|

| 8 | Research Matrix template | Таблица сравнения инструментов | `tech-writer/SKILL.md` |

| 9 | 5-step extraction pipeline | Формализация raw → wiki → outputs | `ai-qa-wiki/AGENTS.md` |

  

---

  

### Детали по каждому пункту:

  

#### 1. Content Engine hooks library

  

**Где:** `tech-writer/SKILL.md` — новая секция "Content Hooks Library"

  

**Что делать:**

- После каждого написанного поста — извлекать 3-5 сильных фраз

- Сохранять в `Articles/linkedin-posts/hooks-library.md`

- Переиспользовать в следующих постах

  

**Формат:**

```markdown

## Hooks Library

  

| Hook | Source Post | Reuse For |

|------|-------------|-----------|

| "20% coverage with a traceability matrix beats 80% without one" | 0-orangehrm-phase0 | Coverage discussions |

| "taught me more than 1000 passing tests on a project I already know" | 1-orangehrm-phase1 | Learning/contrast |

```

  

#### 2. Pre-publish Audit

  

**Где:** `tech-writer/SKILL.md` — новая секция "Pre-publish Audit"

  

**Что делать:**

- Перед публикацией каждого поста — проверять:

  - [ ] Все цифры source-backed

  - [ ] Нет unsupported claims

  - [ ] Нет повторов из предыдущих постов (если серия — OK)

  - [ ] CTA присутствует

  - [ ] ≤1200 chars

  - [ ] Author line в конце

  - [ ] Hashtags (3-5)

  

**Формат:** Чеклист в skill file

  

#### 3. Code Review checklist

  

**Где:** `qa-automation-engineer/SKILL.md` — новая секция "Code Review Checklist"

  

**Что делать:**

- При ревью тестов проверять:

  - [ ] Types: нет `any` (page: Page, not page: any)

  - [ ] URLs: нет hardcoded (baseURL в config)

  - [ ] Waits: нет waitForTimeout (explicit waits)

  - [ ] Selectors: data-testid (не text= или CSS)

  - [ ] Assertions: сильные (toHaveText, toHaveCount, не toBeVisible)

  - [ ] Imports: из fixtures (не @playwright/test)

  - [ ] Cleanup: afterEach/unrouteAll

  

**Формат:** Чеклист в skill file

  

#### 4. Article Review checklist

  

**Где:** `tech-writer/SKILL.md` — новая секция "Article Review Checklist"

  

**Что делать:**

- При ревью статей проверять:

  - [ ] Hook — конкретный (числа, контраст)

  - [ ] Money paragraph — сильный claim

  - [ ] Длина ≤1200 chars (или carousel если длиннее)

  - [ ] CTA — вопрос к аудитории

  - [ ] Авторская подпись

  - [ ] Эмодзи ≤9

  - [ ] Нет клише ("In today's world...", "As we all know...")

  - [ ] Нет повторов из предыдущих постов

  

**Формат:** Чеклист в skill file

  

#### 5. SOP template

  

**Где:** `qa-automation-sandbox/sop/` — NEW directory

  

**Файлы:**

- `mutation-testing.md` — как запускать mutation tests

- `contract-testing.md` — как добавлять contract tests

- `deploy-render.md` — как деплоить на Render

- `new-module.md` — как добавлять новый модуль (OrangeHRM)

  

**Формат SOP:**

```markdown

# SOP: Mutation Testing

  

## Purpose

Запуск и анализ mutation tests для Buzzhive.

  

## When to Use

- Перед каждым PR

- После изменения API endpoints

- Раз в неделю (nightly)

  

## Steps

1. `docker-compose up --build -d`

2. `npx playwright test e2e/mutation/ --project=chromium`

3. Анализ results: killed / survived / skipped

4. Если survived > 0 — исправить assertions

  

## Quality Checks

- Все mutation tests pass (34/34)

- Нет skipped без причин

- Assertions使用ильные (не toBeVisible)

  

## Failure Points

- Docker не запущен → ECONNREFUSED

- Backend не healthy → timeout

- Flaky tests → retries=2

  

## Checklist

- [ ] Docker running

- [ ] Backend healthy

- [ ] All 34 tests pass

```

  

#### 6. Cross-Project Insights

  

**Где:** `session-checkpoint.md` template — новая секция

  

**Что делать:**

- В конце каждой сессии добавлять:

```markdown

## Cross-Project Insights

- **Для qa-automation-sandbox:** ... (что полезного из этого проекта)

- **Для ai-qa-wiki:** ... (что полезного)

- **Для OrangeHRM:** ... (что полезного)

```

  

#### 7. Old articles processing

  

**Где:** `ai-qa-wiki/AGENTS.md` — новая секция "Processing Old Articles"

  

**Что делать:**

- Для каждой старой статьи в `raw/`:

  1. Source inventory (UC27 step 1)

  2. Extraction (UC27 step 2)

  3. Synthesis (UC27 step 3)

  4. Сохранить в `wiki/`

  

**Приоритет:** Статьи по mutation testing, chaos engineering, LLM testing

  

#### 8. Research Matrix template

  

**Где:** `tech-writer/SKILL.md` — новая секция "Research Matrix"

  

**Формат:**

```markdown

## Research Matrix: [Topic]

  

| Tool/Approach | Category | Strengths | Weaknesses | Confidence | Source |

|---------------|----------|-----------|------------|------------|--------|

| Playwright | E2E | Multi-browser, fast | No API testing | High | docs |

| Jest | Unit | Fast, simple | No browser | High | docs |

```

  

#### 9. 5-step extraction pipeline

  

**Где:** `ai-qa-wiki/AGENTS.md` — новая секция "Extraction Pipeline"

  

**Формализация:**

```

1. Source inventory → что есть в raw/

2. Source-by-source extraction → ключевые идеи из каждой статьи

3. Cross-source synthesis → общие темы, противоречия

4. Knowledge base build → organized wiki/

5. Final audit → проверка покрытия

```

  

---

  

### Порядок внедрения:

  

| Шаг | Что | Время |

|-----|-----|-------|

| 1 | tech-writer: hooks library + pre-publish audit + article review | 15 мин |

| 2 | qa-automation-engineer: code review checklist | 10 мин |

| 3 | qa-automation-sandbox: 4 SOP файла | 20 мин |

| 4 | session-checkpoint: cross-project insights template | 5 мин |

| 5 | ai-qa-wiki: old articles processing + extraction pipeline | 15 мин |

  

**Итого:** ~65 мин

  

---

  

### Вопросы:

1. **SOP** — 4 файла достаточно или нужно больше? (auth testing, UI testing?)

2. **Old articles** — начать с mutation testing статей или с других?

3. **Research Matrix** — какой первый сравнительный анализ сделать? (LLM для тестов? Contract frameworks?)

  

## Research Matrix — приоритеты

  

### Варианты сравнения:

  

| # | Тема | Релевантность | Покрытие | Impact |

|---|------|---------------|----------|--------|

| 1 | **LLM для генерации тестов** | 🔴 Высокая | Уже тестировали 5 моделей | Высокий |

| 2 | **Contract testing frameworks** | 🟡 Средняя | Уже используем Hybrid | Средний |

| 3 | **Test runners (Playwright vs Jest vs Vitest)** | 🟡 Средняя | Playwright основной | Средний |

| 4 | **Mutation testing tools** | 🟢 Низкая | Наш подход уникален | Низкий |

  

### Рекомендация: **Вариант 1 — LLM для генерации тестов**

  

**Почему:**

- Уже есть данные: Ollama (qwen2.5:3b, 7b, 14b, 32b), Groq (llama-3.3-70b), Webwright (5 моделей)

- Результат: 34/34 mutation tests pass с 7B custom model

- Практический impact: можно повторить для OrangeHRM

- LinkedIn серия: это третий пост в серии (0: Phase 0, 1: Phase 1 skeleton, 2: LLM story)

  

**Формат матрицы:**

  

| Model | Speed | Format Quality | Cost | Best For | Source |

|-------|-------|----------------|------|----------|--------|

| qwen2.5-coder:7b (custom) | 30 tok/s | 90% JSON | $0 | Playwright tests | Ollama local |

| Groq llama-3.3-70b | 500 tok/s | 98% JSON | $0 (limited) | Quick prototypes | API |

| Webwright (GPT-5.4) | ~50 tok/s | 85% JSON | $2.37/run | CLI tools | Webwright |

| Ollama 14B | 7 tok/s | 90% JSON | $0 | Too slow | Ollama local |

| Ollama 32B | 3 tok/s | 60% JSON (broken) | $0 | Doesn't fit VRAM | Ollama local |

  

**Инсайты для поста:**

- "Custom 7B model beats default 32B on structured JSON output"

- "30 tok/s vs 3 tok/s — speed matters more than size for test generation"

- "96% mutation score with AI-generated tests — but only with right temperature (0.1)"

  

### Альтернатива: **Вариант 2 — Contract testing frameworks**

  

Если нужно для wiki, а не для поста:

  

| Framework | Type | Setup | Maintenance | Best For |

|-----------|------|-------|-------------|----------|

| OpenAPI Schema | Structural | Medium | Low | API validation |

| Pact (PactV4) | Behavioral | High | High | Consumer-driven |

| Hybrid (наш) | Both | Medium | Medium | Full coverage |

  

### Вопрос:

1. **LLM comparison** — начать с матрицы для wiki или сразу для LinkedIn поста?

2. **Другие данные** — нужно ли добавить Claude Code / OpenCode в сравнение? (мы их не тестировали для генерации тестов)
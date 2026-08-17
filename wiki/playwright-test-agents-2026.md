---
title: "Playwright Test Agents (2026)"
type: article
updated: "2026-08-17"
tags: [playwright, agents, microsoft]
---

# Playwright Test Agents (2026)

## Три агента

Microsoft встроил трёх специализированных Playwright-агентов прямо в `@playwright/test`:

### 🎭 Planner
- Исследует приложение: кликает, заполняет формы, ходит по страницам
- На вход: задача (например, "Generate a plan for guest checkout")
- На выход: Markdown-план в `specs/*.md` — шаги, ожидаемые результаты, тестовые данные
- Использует `seed.spec.ts` для bootstrap контекста (фикстуры, глобальный setup)
- План человекочитаемый, но достаточно точный для генерации тестов

### 🎭 Generator
- Берёт Markdown-план из `specs/`
- Трансформирует в Playwright `.ts` тесты
- Верифицирует селекторы и assertions live — пока генерирует, проверяет что элементы существуют
- На выход: `tests/*.spec.ts` — один тест на один scenario
- Может содержать ошибки (Healer их чинит)

### 🎭 Healer
- Запускает сгенерированные тесты
- Если тест падает:
  1. Replay упавших шагов
  2. Inspect UI — находит эквивалентные элементы
  3. Suggests patch (locator update, wait adjustment, data fix)
  4. Re-run до pass или guardrails
- На выход: passing test или skip (если функциональность сломана)

## Архитектура

```
repo/
  .github/           # agent definitions (MCP tools + instructions)
  specs/             # human-readable test plans
    basic-operations.md
  tests/
    seed.spec.ts     # seed test for context
    create/add-valid-todo.spec.ts
  playwright.config.ts
```

Агент-дефиниции — коллекция инструкций и MCP tools. Обновляются через `npx playwright init-agents`.

## Сравнение с MAS-пайплайном

| Этап | MAS (Model-AI-Schema) | Playwright Agents |
|------|----------------------|-------------------|
| Exploration | Model → known_patterns.json | 🎭 Planner → specs/*.md |
| Generation | AI + REJECT → learned_patterns.json | 🎭 Generator → tests/*.ts |
| Validation | Schema check + Human review | 🎭 Healer (auto-fix loop) |
| Feedback loop | `learned_patterns.json` (память) | Нет памяти между сессиями |
| Human gate | Обязателен (AGENTS.md) | Опционален |
| Scope | Любые типы тестов, код | Только Playwright E2E |

**Общее:** трёхшаговый пайплайн с валидационным циклом.

**Различия:**
- MAS копит знания (`known_patterns.json` → `learned_patterns.json`)
- Playwright Healer чинит selenoid-зависящие проблемы, но не учится
- MAS требует человека как gate — Healer пытается автопочинить

## Сравнение с Autonoma

| | Autonoma | Playwright Agents |
|---|---------|-------------------|
| Exploration | ✅ Codebase-first (routes, components, data models) | ✅ Smoke-first (ходит по приложению) |
| Test generation | ✅ Env Factory + specs | ✅ Plan → .ts |
| Data seeding | ✅ Environment Factory (REST API) | ❌ Seed test (ручной контекст) |
| Auto-heal | ❌ | ✅ Healer |
| CI/CD | ✅ Pipeline | ❌ Только в IDE |
| Цена | Free self-host / $499/mo cloud | Бесплатно (open-source) |
| Платформы | Web + Mobile | Web (Mobile через эмуляцию) |

**Ключевое преимущество Autonoma:** Environment Factory — сидирование данных через API. Playwright Agents полагаются на seed test, который нужно писать руками.

**Ключевое преимущество Playwright Agents:** Healer — автопочинка flaky тестов. Этого нет в Autonoma.

## Совместимость с текущим стеком

Playwright Agents интегрируются с OpenCode:

```bash
npx playwright init-agents --loop=opencode
```

Флаг `--loop` определяет, для какого AI-ассистента генерировать дефиниции:
- `opencode` — OpenCode (наш стек)
- `claude` — Claude Code
- `vscode` — VS Code (v1.105+)

## Вывод

Playwright Test Agents — это MAS-пайплайн родной для Playwright. Не заменяет Autonoma (нет data seeding), но закрывает две дыры: генерация планов из exploration и автопочинка упавших тестов.

Наш комбинированный стек:
1. **Autonoma** — data seeding (Environment Factory)
2. **Playwright Planner** — exploration + test plan
3. **Playwright Generator** → .ts код
4. **Playwright Healer** — авто-починка flaky
5. **Человек** — review + critical decisions

Источник: https://playwright.dev/docs/test-agents

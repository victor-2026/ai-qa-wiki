# KISS Sorcar — Open-Source AI Coding Agent

**Repo:** [github.com/ksenxx/kiss_ai](https://github.com/ksenxx/kiss_ai) (515 ★, Apache 2.0)
**Author:** Koushik Sen (Berkeley)
**Stack:** Python, ~3,270 LOC, VS Code extension + CLI + Web/Mobile

## Что такое KISS Sorcar

Open-source AI software engineering agent, который бьёт Cursor и Claude Code на Terminal Bench 2.0 (62.2% vs 61.7% vs 58%). Бесплатный, локальный, model-agnostic. Работает как расширение VS Code и как CLI-инструмент.

Назван в честь P.C. Sorcar — бенгальского иллюзиониста.

## Ключевые возможности

| Фича                       | Детали                                                                 |
| -------------------------- | ---------------------------------------------------------------------- |
| **Browser Automation**     | Chromium + Playwright из коробки                                       |
| **Git Worktree Isolation** | Каждая задача в своей ветке, main untouched                            |
| **fix-run-verify loop**    | Пишет код → запускает линтер/typecheck/test → чинит ошибки → повторяет |
| **Model-agnostic**         | 533 модели через OpenRouter/Anthropic/OpenAI/Together AI/локальные     |
| **Budget tracking**        | Real-time токены + стоимость + hard budget ceilings                    |
| **Cross-session learning** | USER_PREFS.md — запоминает конвенции проекта                           |
| **Multimodal**             | Читает скриншоты, изображения                                          |
| **Docker sandbox**         | Изолированное выполнение                                               |
| **23 third-party агента**  | Slack, Discord, Teams, WhatsApp, Telegram, Gmail...                    |

## Архитектура (5 слоёв)

| Layer | Назначение | LOC |
|-------|-----------|:---:|
| L1 — KISS Agent | Budget-tracked ReAct loop с function calling | 483 |
| L2 — Relentless Agent | Auto-summarization, continuation между сессиями | 514 |
| L3 — Sorcar Agent | Coding tools + browser automation + parallel sub-agents | 912 |
| L4 — Chat Sorcar Agent | Многошаговые chat-сессии | 443 |
| L5 — Worktree Sorcar Agent | Git worktree изоляция | 916 |

## Бенчмарки

| Бенчмарк | KISS Sorcar | Claude Code | Cursor |
|----------|:---:|:---:|:---:|
| **Terminal Bench 2.0** | **62.2%** 🥇 | 58% | 61.7% |
| SWE-bench (Python) | — | 80.8% 🥇 | — |

## Сравнение с Webwright для QA

| | Webwright | KISS Sorcar |
|---|:---:|:---:|
| Playwright встроен | ❌ через отдельный браузер | ✅ Chromium + Playwright |
| Git safety | ❌ правит напрямую | ✅ Git Worktree |
| Запускает тесты | ❌ только генерирует | ✅ fix-run-verify loop |
| Format errors | Высокий (>30%) | Низкий (инструкции жёстче) |
| Model | Только Anthropic | Model-agnostic |
| VS Code | ❌ Terminal-only | ✅ Расширение VS Code |

## Установка

```bash
# Full install
curl -fsSL https://raw.githubusercontent.com/ksenxx/kiss_ai/main/scripts/install.sh | bash

# VS Code только расширение
# Marketplace → "KISS Sorcar" → Install
```

## Модели для QA-задач

```bash
# OpenRouter (нужен ключ: openrouter.ai/keys)
export OPENROUTER_API_KEY="sk-or-v1-..."

# Платные (с function calling)
sorcar -m "openrouter/deepseek/deepseek-v3.2" -t "task"

# Бесплатные (через OpenRouter, rate-limited)
sorcar -m "openrouter/nvidia/nemotron-3-super-120b-a12b:free" -t "task"
sorcar -m "openrouter/google/gemma-4-31b-it:free" -t "task"

# Groq (500 tok/s)
sorcar -e "https://api.groq.com/openai/v1" \
       --header "Authorization: Bearer $GROQ_API_KEY" \
       -m "llama-3.3-70b-versatile" -t "task"

# Локальный Ollama
sorcar -e "http://localhost:11434/v1" \
       -m "qwen2.5-coder:7b" -t "task"
```

## Project Conventions (SORCAR.md)

KISS Sorcar первым делом читает `SORCAR.md` в рабочей директории. Формат — Markdown с конвенциями проекта (POM структура, тестовые команды, импорты, no-go зоны).

См. пример: `OrangeHRM/SORCAR.md`

## Сценарии для QA

| Сценарий                                 | Риск | Промпт                                                                 |
| ---------------------------------------- | :--: | ---------------------------------------------------------------------- |
| Новый POM + spec (модуль без тестов)     |  🟢  | "Create pom/XPage.ts + e2e/x.spec.ts following SORCAR.md. Run tests."  |
| Code review существующих тестов          |  🟢  | "Review e2e/*.spec.ts for assert strength, flake patterns, selectors"  |
| Миграция waitForTimeout → explicit waits |  🟡  | "Find all waitForTimeout calls in e2e/. Replace with explicit waits."  |
| Генерация mutation-тестов                |  🟡  | "Add 3 API mutation tests to e2e/mutation/. Follow existing patterns." |
| CI/CD pipeline debug                     |  🟡  | "Read playwright.yml. Fix failed job from logs."                       |

## Ограничения

- Free-модели Nemotron/Gemma склонны к пошаговому выполнению (type_text по буквам) — для code-gen лучше давать задачу без browser exploration
- DeepSeek V4 Pro через OpenRouter без function calling — только для чата, не для агентных задач
- Git Worktree требует git-репозиторий — иначе падает в direct mode
- Rate limits на бесплатных моделях OpenRouter — троттлинг при частых запросах
- Может залипнуть на логине (ждёт steer) — не ошибка, ждёт подтверждения

## FAQ
## Когда что использовать

| Задача | OpenCode (я) | KISS + Nemotron (free) | KISS + DeepSeek ($) |
|--------|:---:|:---:|:---:|
| Анализ вакансий, CV, cover letter | ✅ | ❌ | ❌ |
| LinkedIn статья + ревью | ✅ | ❌ | ❌ |
| Обновление TEST_CASES.md (цифры) | ✅ | ✅ | ✅ |
| SORCAR.md обновление | ✅ | ✅ | ✅ |
| Новый POM по паттерну | ❌ | ✅ | ✅ |
| Новый spec по паттерну | ❌ | ✅ | ✅ |
| Регистрация в fixtures | ✅ | ⚠️ (баг рендеринга) | ✅ |
| Запуск тестов + fix failures | ❌ | ✅ | ✅ |
| Рефакторинг 8+ файлов | ✅ | ❌ | ✅ |
| Code review с контекстом проекта | ✅ | ❌ | ⚠️ |
| Простой rename/cleanup | ✅ | ✅ | ✅ |
| Browser exploration | ❌ | ❌ | ✅ |
| Mutation/contract тесты | ✅ | ❌ | ⚠️ |

### Правило

- **Я (OpenCode)** — для задач где нужен **контекст и понимание**: анализ, review, статьи, стратегия. Бесплатно (включено).
- **KISS + Nemotron (free)** — для простых **паттерн-копирующих** задач: один новый POM, одна правка текста. Бесплатно.
- **KISS + DeepSeek ($)** — для автономных **генерация + run + fix** циклов: новый spec с нуля, browser exploration, рефакторинг. $0.23/M tok.

**Текущая задача (fix TypeScript errors)** — для KISS. Это ровно то что он делает лучше меня: находит ошибки, чинит, запускает проверку. Мне пришлось бы читать 8 файлов, тыкать вручную.
















<!-- backlinks-start -->
### Backlinks
- [3 Ai Test Tools Orangehrm Comparison 2026](wiki/3-ai-test-tools-orangehrm-comparison-2026.md)
- [Ai In Qa Issue 17 Butch Mayhew 2026 07 06](wiki/ai-in-qa-issue-17-butch-mayhew-2026-07-06.md)
- [Claude Code Ci Cd Mcp 2026](wiki/claude-code-ci-cd-mcp-2026.md)
<!-- backlinks-end -->

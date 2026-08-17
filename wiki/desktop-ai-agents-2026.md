---
title: "Десктопные AI-агенты для кода (2026)"
type: article
updated: "2026-08-17"
tags: [agents]
---

# Десктопные AI-агенты для кода (2026)

**Источник:** `raw/desktop-ai-agents-2026.md` (полный обзор)

---

## Tier 1 — Мейнстрим (6 инструментов)

| Инструмент | Тип | Модели | Цена | Уникальная фича |
|-----------|-----|--------|------|----------------|
| **Cursor** | IDE (VS Code fork) | Claude, GPT, Gemini | $20/mo Pro | Лучшее Tab completion |
| **Claude Code** | Terminal CLI | Claude (только) | $20-200/mo | #1 SWE-bench 80.8% |
| **Google Antigravity** | Platform (Desktop + CLI + SDK + API) | Gemini 3.5 Flash, Claude Sonnet, GPT-OSS | $20-200/mo | Browser Sub-agent, Multi-agent DAG |
| **OpenCode** | TUI + Desktop + VS Code | BYOK, 75+ providers | $0 (MIT) + API | #1 open source, приватность |
| **GitHub Copilot** | VS Code extension | GPT-4o/Codex | $10-39/mo | 26M+ пользователей |
| **Windsurf** | IDE (VS Code fork) | Claude, GPT, SWE-1.5 | $15/mo Pro | Лучший free tier |

## Tier 2 — Нишевые

Augment Code ($30/mo), Sourcegraph Cody ($9/mo), Aider (open source), Cline (open source), Devin ($500/mo), Kiro ($0), JetBrains Junie, Gemini CLI (умирает 18 июня 2026).

---

## Наши результаты апробаций

### OpenCode — ежедневный драйвер (80+ сессий)

**Проекты:** qa-automation-sandbox, OrangeHRM, ai-qa-wiki, Articles, Positions-CV-CL, Test-Dora-Plus, DYI-Building, Hire-me

**Что делали:** E2E-тесты (Playwright), API-тесты (Go), POM-рефакторинг, CI/CD, генерация контента, анализ кода.

**Затраты:**
- OpenCode Go (gpt-4o-mini): ~$10/mo
- OpenCode Free (deepseek): $0
- Deepseek-v3.2: ~$4 за сессию Autonoma pipeline (4/6 шагов)
- Groq (llama-3.3-70b): $0 (free tier, ~500 tok/s)

**Ключевые выводы:**
- 131K контекста достаточно для POM-рефакторинга и E2E-тестов, но не для entityAudit (требует >131K)
- Deepseek справляется с E2E-генерацией, но уступает gpt-4o по качеству entity resolution
- Смена модели на ходу (без спроса) — реальный risk для бюджета (Session 48)
- Groq free tier идеален для RAG и анализа (digest, regression-advice)

### Devin ($500/mo) — OrangeHRM POM

**Сессия 76b (2026-07-13):** Devin сгенерировал MaintenancePage POM + 7 тестов из spec-файла.

**Результат:**
- POM: 4 метода, 1 spec-файл, 7 тестов
- Селекторы угаданы (нет DOM-доступа) — часть нерабочих
- Без CI feedback loop — ошибки не фиксились
- Время: ~15 мин на генерацию

**Вердикт:** Быстро, но без гарантий. Требует ручной доработки.

### Aider (open source) — OrangeHRM Maintenance

**Тот же spec, сравнение apples-to-apples** (Session 76b):

| Параметр | Devin | Aider |
|----------|-------|-------|
| POM-методы | 4 | 10 |
| Тестов | 7 | 1 |
| CI feedback | Нет | `--test-cmd` авто-фикс |
| Первый PASS | Нет | 2/2 за 15.4с |
| Цена | $500/mo | $0 |

**Ключевая фича Aider:** `--test-cmd` — запускает тест, читает ошибку Playwright, фиксит локатор, повторяет. Devin так не умеет.

**Вывод:** На одинаковом spec Aider не хуже Devin, а с auto-fix — надёжнее.

### Autonoma — полный pipeline (6 шагов)

**Сессии 47-48 (2026-06-15):** Попытка запустить полный pipeline (pageFinder → kb → entityAudit → scenarioRecipe → testGenerator → review).

**Результаты:**
- Шаги 1-2 (pageFinder, kb): ✅ прошли, 131K хватило
- Шаг 3 (entityAudit): ❌ overflow 274K → fix (skip POMs) → 59 entities
- Шаг 4 (scenarioRecipe): ❌ timeout 191K → auto-switch модели без спроса
- Остановлены на 4/6 из-за budget $4.99

**Проблемы:**
- Context overflow при включении POM-файлов (>131K)
- Timeout (191K): причина неясна — контекст или нагрузка провайдера
- Auto-switch модели: deepseek-v3.2 → kimi-k2.6 → deepseek/v4-pro → gpt-5.4-nano
- **Старая архитектура deprecated** — Autonoma перешла на Claude Code plugin

### Kiro ($0) — Virto Commerce codebase analysis

**Сессия 79 (2026-07-21):** 30 мин анализа vc-platform.

**Результаты:**
- 36 untested security-файлов (auth, OAuth, permissions, SSO, certificates)
- 89/109 endpoints untested (81.65%), 82 [Authorize] — 0 тестов 401/403
- 4 модуля нулевого покрытия (127 файлов)
- Breaking change: limited_permissions removal — CI не поймает

**Вердикт:** PBT-first философия даёт глубину, которой нет у Devin/Windsurf.

### Google Antigravity — login_test.go

**Сессия 47 (2026-06-14):** Free preview, написал `login_test.go` (188 строк, 10 тестов).

**Результат:**
- Go-тест для API-логина: корректные assertion'ы, table-driven
- Нашёл race condition в хендлере логина
- Доступ потерян через 2 дня (VPN блокировка региона)
- Quota: 4 сокращения за 4 месяца — доверие подорвано

### Claude Code — CI/CD + MCP integration

**Что оценили через wiki-анализ** (claude-code-ci-cd-mcp-2026.md):
- CI/CD пайплайн: Docker → Playwright → Computer Use → MCP (Jira/Slack)
- Self-healing при падении тестов
- Skill ecosystem — 14 QA skills от Anton Gulin (pw-kit)

**На проектах не использовали** (нет прямого доступа к Claude).

---

## Сводное сравнение

| Инструмент | Цена | Тесты | POM | CI/CD | Feedback | Проект |
|-----------|------|-------|-----|-------|----------|--------|
| OpenCode | ~$10/mo | ✅ 600+ | ✅ 13 POM | ✅ 10 workflows | 🔄 ручной | Daily driver |
| Devin | $500/mo | ✅ 7 | ⚠️ 4 метода | ❌ | ❌ | OrangeHRM |
| Aider | $0 | ✅ 1 | ✅ 10 методов | ✅ --test-cmd | ✅ авто-фикс | OrangeHRM |
| Autonoma | ~$5/session | ❌ 4/6 шагов | overflow | ❌ | ❌ | Sandbox |
| Kiro | $0 | analysis | analysis | ❌ | ✅ PBT | Virto |
| Antigravity | free→$20 | ✅ 10 Go | N/A | ❌ | ❌ | Sandbox |
| Claude Code | $20-200 | analysis | analysis | ✅ MCP | ✅ self-heal | Wiki only |

## Комбинации

- **Antigravity + Cursor** ($40/mo) — параллельные задачи + точное редактирование
- **Cursor + Claude Code** ($120-220/mo) — стандартный choice у CTO (Oleg из Virto использует Claude Code)
- **Cursor + OpenCode** ($30-70/mo) — multi-model
- **OpenCode + Groq** ($10/mo) — RAG + анализ + дешёвые задачи

## Ключевые тренды 2026

1. Все major labs теперь имеют вертикальный stack: Anthropic → Claude Code, Google → Antigravity, OpenAI → Codex CLI
2. Browser Sub-agent (Antigravity) — уникальная фича, никто больше не умеет
3. Quota crisis — Antigravity 4 сокращения за 4 месяца, доверие подорвано
4. **Open source побеждает**: Aider = Devin по качеству, OpenCode = Claude Code по возможностям, Kiro = уникальная ниша
5. Agentic IDE против Terminal CLI — Antigravity выбрал "и то и то"
6. Race bugs — разные инструменты находят разные проблемы (Antigravity vs OpenCode)
7. **Self-healing** — единственный real gap у open source (есть только у Claude Code + Playwright Agents)








<!-- backlinks-start -->
### Backlinks
- [Autonoma Open Source & Architecture (June 2026)](wiki/autonoma-open-source-self-driving-2026.md)
- [Google Antigravity Qa 2026](wiki/google-antigravity-qa-2026.md)
- [Kiro.dev — AWS Agentic AI IDE (2026)](wiki/kiro-dev-aws-ai-ide-2026.md)
<!-- backlinks-end -->

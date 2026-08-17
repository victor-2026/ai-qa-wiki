# Session Checkpoint — 2026-07-26 (Session 81 — Wiki Ingest)

## Session 81 (2026-07-26)

### Что сделано
1. **Ingested:** `raw/6 AI Concepts You Must Master to Build Production-Ready AI Systems.md` → `wiki/6aiconceptsyoumustmastertobuildproduction-readyaisystems.md` (52 строки, таблица 6 концепций + практические применения)
2. **wiki index updated** — 185 topics, 101 raw sources

### Next
- Следующий raw файл для ингеста по запросу

---

## Что сделано

### Новые wiki статьи (6)
1. `wiki/claude-code-qa-testing-2026.md` — Claude Code, Computer Use, Skills, MCP
2. `wiki/claude-code-skill-examples-2026.md` — 2 SKILL.md: Playwright + Hybrid Computer Use
3. `wiki/claude-code-ci-cd-mcp-2026.md` — Docker + GitHub Actions + MCP Slack/Jira + closed-loop assignee
4. `wiki/opencode-openrouter-qa-2026.md` — OSS стек, цены, AGENTS.md
5. `wiki/google-antigravity-qa-2026.md` — Agent-First, multi-agent, Browser-in-loop
6. `wiki/kiro-dev-aws-ai-ide-2026.md` — обновлена: coverage gap analysis, security audit, Devin/Windsurf сравнение

### 6 raw files ingested (все новые)
Все новые raw → wiki: claude-code-skill-examples, claude-code-ci-cd-mcp, opencode-openrouter, google-antigravity. Обновлены cross-links.

### Структура
```
wiki/
├── claude-code-qa-testing-2026.md           # Claude Code обзор
├── claude-code-skill-examples-2026.md       # SKILL.md примеры
├── claude-code-ci-cd-mcp-2026.md            # CI/CD + MCP pipeline
├── opencode-openrouter-qa-2026.md           # OSS альтернатива
├── google-antigravity-qa-2026.md            # Antigravity (с ценами)
└── kiro-dev-aws-ai-ide-2026.md              # Kiro обновлённый
```

### wiki-topics
~170 topics (было 164, +6 новых статей с cross-links)

---

## Session 89 (2026-08-17) — AI QA Evidence Layer reference

### Что сделано
- Added `wiki/ai-qa-evidence-layer-validation-evals-guardrails-telemetry.md`.
- Documented downstream QA validation vs model/agent evals, including trajectory and outcome boundaries.
- Added the distinction between mutation testing as an anti-overfit guardrail and a complete risk-based AI safety guardrail layer.
- Added model, tool, and agent telemetry fields, privacy controls, OpenTelemetry GenAI reference, and correlation with Allure/DORA.
- Cross-linked offline trajectories, tool-call testing, mutation testing, monitoring/observability, Claude Code MCP, and Alex Barady wiki pages.
- Updated `wiki-topics.json` to 192 topics; raw source count remains unchanged because no raw file was modified.

## Session 90 (2026-08-17) — Autonoma pipeline steps + CARBON harness

### Autonoma pipeline (ingest)
- Ingested `raw/Autonoma - шаги в пайплайне.md` → `wiki/autonoma-шагивпайплайне.md` (RU): 6 шагов pagesFinder → KB → entityAudit → scenarioRecipe → testGenerator → environmentFactory; интерактивная пауза + Confirmation перед testGenerator; правки entity-audit.md/features.json.
- Исправлено противоречие в `wiki/autonoma-open-source-self-driving-2026.md` (строка old pipeline): `recipeBuilder → testGenerator` → `testGenerator → environmentFactory` (по GitHub-источнику), добавлен Flag для human review (наблюдаемый лог Phase 3 от 2026-06-10 показывал промежуточный recipeBuilder).
- Broken See also link исправлен.

### CARBON (ingest + review)
- Пользователь перенёс LinkedIn-пост в `raw/CARBON, AI Agentic Verification Harnes.md` → ingested → `wiki/carbon-ai-agentic-verification-harness.md` (имя исправлено с Harnes → Harness).
- Добавлены: vendor-caveat (private beta marketing, не верифицировано), секция Community Discussion (Anton Gulin: failing trace vs green run + ответ Arbon; Vikash Soni: verification bottleneck), Sources (Jason Arbon, LinkedIn urn, testers.ai).
- See also: anton-gulin-3-layer, evidence-layer, tool-calls, agents-review, offline-eval.
- Backlinks synced (194 pages), wiki-topics.json: **194 topics, 110 raw sources**.

### Git
- Коммит не делался (по договорённости: чекпоинт позже).

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

Augment Code ($30/mo), Sourcegraph Cody ($9/mo), Aider (open source), Cline (open source), Devin ($500/mo), JetBrains Junie, Gemini CLI (умирает 18 июня 2026).

## Antigravity — наш опыт

**Google Antigravity** (free preview 24-25 мая). Сделал `login_test.go` (188 строк, 10 тестов), нашёл race-баг. Доступ потерян из-за VPN.

## Комбинации

- **Antigravity + Cursor** ($40/mo) — параллельные задачи + точное редактирование
- **Cursor + Claude Code** ($120-220/mo) — стандартный choice
- **Cursor + OpenCode** ($30-70/mo) — multi-model

## Ключевые тренды 2026

1. Все major labs теперь имеют вертикальный stack: Anthropic → Claude Code, Google → Antigravity, OpenAI → Codex CLI
2. Browser Sub-agent (Antigravity) — уникальная фича, никто больше не умеет
3. Quota crisis — Antigravity 4 сокращения за 4 месяца, доверие подорвано
4. Agentic IDE против Terminal CLI — Antigravity выбрал "и то и то"
5. Race bugs — разные инструменты находят разные проблемы

# Vibe Wipe Coding Guide

**Last Updated:** 2026-04-18
**Sources:** raw/vibe-coding-*, raw/hidden-costs-vibe-coded-apps, raw/spec-driven, raw/pipeline-triad

---

## What is Vibe Coding

Building software from natural language prompts using AI assistants. Named after the "vibe" of describing what you want rather than specifying how.

**Problem:** Works great for prototyping, falls short for production systems.

## The Hidden Costs

| What's Built (80%) | What's Missing (20%) |
|--------------------|----------------------|
| UI, features, logic | Security hardening |
| Happy path works | CI/CD pipelines |
| Demo-ready | Monitoring & alerts |
| | Compliance & backups |

> "Good enough to demo" ≠ "Safe to run in production"

### Security Gaps
- Exposed API keys in frontend
- Broken authentication (no rate limiting)
- IDOR vulnerabilities
- SQL injection, XSS

### Operational Gaps
- No CI/CD = no safety net
- No monitoring = discover problems from users, not alerts
- No compliance documentation

## Vibe vs Spec-Driven Development

| Aspect | Vibe Coding | Spec-Driven |
|--------|-------------|-------------|
| Nature | Speculative, exploratory | Structured, intentional |
| Artifacts | Ephemeral prompts | Living documents |
| Collaboration | Dev + AI only | Wider team |
| Context | Lost in chat history | Captured in specs |
| For | Prototyping | Production |

**Key insight:** Specs are "source of **intention**" not just source of truth.

## When to Use Each

| Use Vibe Coding | Use Spec-Driven |
|-----------------|-----------------|
| Early exploration | Production systems |
| MVP/prototypes | Team collaboration |
| Testing ideas | Compliance requirements |
| Getting unstuck | Long-term maintenance |

## Pipeline Triad Pattern

Agentic approach for production AI development:

```
Creator → Critic → Arbiter
   ↑_________|_________|
```

**14 Steps:**
1. Human creates task
2. Triad: Requirements → Tech spec
3. Human Gate
4. Triad: Development + Code review
5. Triad: Testing (unit, integration, PBT, fuzz)
6. Human Gate
7. Auto: Deploy to staging
8. Human Gate
9. Auto: Deploy to production

**Economics:** ~1 hour human time, ~$6-12 API cost per task

## Best Practices

1. **Start with vibe coding** — spark ideas, get unstuck
2. **Migrate to spec-driven** — when moving to production
3. **Always add monitoring** — before shipping
4. **Security audit** — before public release
5. **CI/CD from day one** — or face technical debt

## The Middle Path

> "Not either/or — Yes And"

Both have value:
- **Vibe coding** — unlocks momentum, spark, test ideas
- **Spec-driven** — slows down to think clearly, creates artifacts

Use vibe coding for prototyping. Spec-driven for production.

## Related

- [[wiki/testing-strategies]] — Testing vibe-coded apps
- [[wiki/agentic-patterns]] — Agentic development patterns
- [[wiki/monitoring-observability]] — What vibe-coded apps need

## Sources

- raw/vibe-coding-vs-spec-driven.md
- raw/hidden-costs-vibe-coded-apps.md
- raw/pipeline-triad-pattern.md
- raw/comprehension-debt.md

---

## Wipe-Coding (Flow-State Coding)

### What is Wipe-Coding

Wipe-coding (или Flow-state coding) — это стиль разработки, при котором программист перестает писать код «руками» построчно.

**Key idea:** AI «стирает» старые абстракции и «накатывает» (wipe) новые слои кода сразу во многих файлах.

### Autonomous AI Agents

Появление автономных AI-агентов (Windsurf, Cursor, Claude Code, Bolt) знаменует переход от «чата с подсказками» к полноценному AI-напарнику с «руками» в системе:

| Traditional AI | Autonomous Agent |
|----------------|------------------|
| Пишет текст кода | Видит весь контекст проекта |
| Предлагает изменения | Индексирует все файлы |
| Требует копирования | Имеет доступ к терминалу |
| | Сам запускает npm install, pytest |
| | Самостоятельно исправляет ошибки |

### How It Works

1. **Give high-level task** — e.g., "Add user profile page with avatar upload"
2. **AI executes** — Creates/edits files across the project
3. **You review** — Approve (Accept) or reject changes
4. **Loop** — AI iterates until tests pass

### Buzzhive Sandbox Example

В проекте Buzzhive Sandbox уже использовались элементы wipe-coding:
- Параллельные агенты для разведки API
- Генерация документации
- Ускорение процесса в **3 раза**

### Economics

- ~1 hour human time per task
- ~$6-12 API cost

### When to Use

- Rapid prototyping
- Feature exploration
- Getting unstuck
- MVP development

### Best Practices for Wipe-Coding

1. **Set clear boundaries** — What can/cannot be changed
2. **Review every change** — Don't let AI run wild
3. **Test-driven** — Let AI fix until tests pass
4. **Keep artifacts** — Document decisions for future

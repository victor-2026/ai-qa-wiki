---
title: "rmorison: Six-Layer AI Architecture for AI-Forward Engineering"
source: https://github.com/rmorison/engineering-standards (MIT, 7 stars)
date: 2026-09-21
tags: [ai-architecture, engineering-standards, spec-driven, context-engineering, agent-transcripts]
---

# rmorison: Six-Layer AI Architecture

**Source:** https://github.com/rmorison/engineering-standards (MIT, 7 stars) — AI forward engineering standards

## The Six Layers

1. **Rules** — global constraints (AGENTS.md)
2. **Workflow Skills** — reusable skills
3. **Persona Agents** — specialized agents (Pi subagents)
4. **References** — context docs (wiki, raw)
5. **Compound/Learnings** — accumulated knowledge (session-checkpoints, memory)
6. **Hooks** — automation triggers (LaunchAgent, hooks)

Principle: **context is expensive, load only what you need.**

## Spec-Driven Development

Specification = source of truth, "code implements the spec". Matches our principle "spec first, no vendor-written spec".

## Agent Transcripts

Logs of AI decisions for history (why-so). Dogfooded: standards prescribe AI review workflow that checks themselves.

## Mapping to Victor's Stack

| Layer | rmorison | Victor |
|-------|----------|--------|
| Rules | Rules | AGENTS.md |
| Workflow Skills | Skills | Pi skills + opencode skills |
| Persona Agents | Persona | Pi subagents (scout, researcher, worker) |
| References | References | wiki/raw, outputs |
| Compound | Compound | session-checkpoints, .opencode-memory.md |
| Hooks | Hooks | LaunchAgent, hooks |

Validates our current layering — same architecture, different names.

## Takeaway for Process

Adopt explicit six-layer naming in docs? Already have it implicitly. The value: **transcripts** (why-so logs) — we have session-checkpoints but not per-decision transcripts. Could add `reviews/` decision logs (as in compound plugin) to compound knowledge.

## Links
- Repo: https://github.com/rmorison/engineering-standards
- Compound: https://github.com/EveryInc/compound-engineering-plugin

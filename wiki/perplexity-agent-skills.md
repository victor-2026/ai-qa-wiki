# Perplexity Agent Skills Guide

## Overview

Perplexity published their internal guide for designing Agent Skills — modular capabilities that power their AI agents. This represents a new discipline: **Skill Engineering**.

## Key Insight

> If you write a skill for an agent the same way you write code for developers, the result will be poor. Good documentation for humans is almost always bad documentation for models.

---

## Zen of Skills: Five Principles Inverted

| Python Principle | → | Agent Skills Principle |
|------------------|---|------------------------|
| Simple is better than complex | → | A skill is a **folder**, not a file. Inside: `SKILL.md`, `scripts/`, `references/`, `assets/`, `config.json` |
| Explicit is better than implicit | → | Skill activation = implicit pattern matching. Agent decides when to load based on short description |
| Sparse is better than dense | → | Context costs tokens. Maximum signal per token is the real quality metric |
| Special cases aren't special enough to break the rules | → | **Gotchas** (failure records) are the most valuable content in a skill |
| If the implementation is easy to explain, it may be good | → | If easy to explain, the model already knows it from training data. Delete such lines |

### Real Example

When Perplexity built skills for US tax law (1,945 sections):
- Flat structure → worse than no skill at all
- Three-level hierarchy with navigation guides → success

---

## Context Tax: Three Cost Levels

Every skill in Perplexity Computer passes through three levels, each costing differently:

| Level | Cost | When Paid |
|-------|------|-----------|
| **Index** | ~100 tokens per skill | Always (in system prompt for every user) |
| **Load** | ~5,000 tokens | When agent decides to activate the skill |
| **Runtime** | unlimited | Only on-demand (scripts, references) |

**Rule:** If a sentence in a skill doesn't change agent behavior — it doesn't belong there.

### Index Quality Requirements

- Maximum 50 words
- Start with "Load when..." — not describing what the skill does
- Should trigger based on user intent, not internal logic

---

## Skill Description = Trigger, Not Documentation

### Bad Description
> "Tracks pull request status"

### Good Description
> "Load when user says: babysit my PR, watch CI, make sure this lands"

The description is a routing trigger, not documentation. Build it from real user queries, not internal logic.

---

## Gotchas as Flywheel

The most practical pattern from the guide. Skills grow not from new instructions but from failure records:

```
Agent failed on task → Add gotcha
Skill loaded incorrectly → Tighten description, add negative tests
Skill didn't load when it should → Add keywords to description
```

The longer a skill lives in production, the more accurate it becomes. The skill body barely changes — only the gotcha section grows.

### Gotcha Structure

```markdown
### N: Issue Title
- **Issue:** What happened
- **Impact:** Test behavior
- **Severity:** low|medium|high
- **Date:** YYYY-MM-DD
```

---

## LLM Limitation

Perplexity emphasizes: **LLMs cannot write skills that benefit them**. Self-generation doesn't work. A skill is engineering with opinion, experience, and iterations — not a one-shot prompt.

---

## Our Implementation

Applied to qa-automation-sandbox skills:

### Structure Added
```
.opencode/skills/
├── skill-name/
│   ├── SKILL.md           # Instructions
│   ├── references/        # Links to docs
│   │   └── links.md
│   ├── gotchas.md         # Failure records
│   └── config.json        # Triggers, priority
```

### Config.json Format
```json
{
  "name": "rest-api-qa",
  "triggers": ["api testing", "rest api", "http requests"],
  "priority": "high",
  "load_when": "user asks about API testing, endpoints, assertions"
}
```

### MAS Integration
MAS reports now include `gotchas` field:
```json
{
  "gotchas": [
    {"issue": "...", "severity": "medium", "line": 42, "date": "2026-05-10"}
  ]
}
```

---

## Related

- [[agent-skills-specification]]
- [[vibe-coding-links]]
- [[wipe-coding-transition]]
- [[prompt-tips-and-skills]]

---

**Tags:** #agent-skills #perplexity #skill-engineering #prompt-engineering #ai-agents  
**Source:** Perplexity internal guide (2026)  
**Updated:** 2026-05-10
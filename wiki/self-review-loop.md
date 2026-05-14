# Self-Review Loop — Make AI Verify Its Own Work

## The Technique

Add to system prompt or task description:

```
You are 100% confident in this strategy? If not — find all possible holes,
propose fixes, and repeat this cycle until you are 100% confident.
```

## What It Does

Transforms agent from answer-generator to self-reviewer:

```
Without: First acceptable answer → stop
With:    Answer → Review → Fix → Review → 100% confident
```

## Results

- Catches edge cases that normally slip through
- Especially effective for:
  - Architecture decisions
  - Refactoring
  - Complex logic
  - Code reviews

---

## Important Nuance

| Model | Effect |
|-------|--------|
| **GPT-5.5 (Codex)** | ✅ Works well — actively finds holes |
| **Claude Opus** | ⚠️ Limited — tends to agree with itself |
| **Groq 70B** | ⚠️ Untested — may need adjustment |

**For Claude:** Use external reviewer agent instead of self-review.

---

## Our Implementation

### MAS Quality Check

Can add this to `AGENTS.md` and `scripts/mas-quality-check.py`:

```
Before generation: Review prompt → find gaps → fix → generate
```

### Perplexity Agent Skills

Add to SKILL.md descriptions:

```markdown
You are 100% confident in your answer? If not — 
find all possible issues, propose fixes, repeat until confident.
```

### QA Sandbox AGENTS.md

Add to core rules:

```markdown
## Self-Review Rule

After generating code/tests:
1. Ask: "Am I 100% confident?"
2. If not — find all possible holes
3. Fix them
4. Repeat until confident
```

---

## Example Usage

### In Code Generation
```
Write API tests for /posts endpoint.
You are 100% confident? If not — find all possible edge cases,
propose fixes, repeat until 100% confident.
```

### In MAS Analysis
```
Analyze test quality and give score.
You are 100% confident in this score? If not — 
find all issues, propose fixes, repeat.
```

---

## Related

- [[agent-teams-architecture]] — Agent A checks Agent B
- [[perplexity-agent-skills]] — Skill engineering best practices
- [[mas-testing-framework]] — Our current MAS implementation

---

**Tags:** #self-review #prompt-engineering #ai-agents #codex #claude
**Source:** Twitter/X thread (2026-05-14)
**Updated:** 2026-05-14
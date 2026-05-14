# Self-Review Loop for AI Agents

Source: Twitter/X thread
Date: 2026-05-14

## The Technique

Add to prompt:
```
You are 100% confident in this strategy? If not — find all possible holes,
propose fixes, and repeat this cycle until you are 100% confident.
```

## What It Does

Transforms agent from answer-generator to self-reviewer.

## Results

- Catches edge cases
- Especially for architecture, refactoring
- Works with GPT-5.5/Codex
- Limited effect with Claude Opus

## Implementation

Added to AGENTS.md self-review rule.

---

Tags: #self-review #prompt-engineering #ai-agents
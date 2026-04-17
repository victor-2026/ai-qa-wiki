# Passmark - AI Regression Testing Engine

**Source:** [bug0inc/passmark](https://github.com/bug0inc/passmark)  
**Type:** Open Source  
**License:** MIT  
**Added:** 2026-04-17

---

## Overview

Passmark is an open-source AI-powered regression testing framework built on Playwright by [Bug0](https://bug0.io/). Tests are written in natural language, and AI handles locator adaptation when UI changes.

## Key Features

### Natural Language Test Definition

```typescript
import { Passmark } from 'passmark';

const passmark = new Passmark({ provider: 'openai' });

await passmark.test('login, open users table, sort by date, verify records display');
```

### How It Works

1. **First run:** LLM executes steps → results stored in Redis
2. **Subsequent runs:** Playwright runner uses cached steps (no LLM calls)
3. **On failure:** AI identifies failing steps, finds new locators, updates cache

### Auto-Healing Locators

When UI changes:
- Passmark detects which step failed
- AI suggests new locators
- Only that step is updated, not the whole test
- Cache is refreshed for future runs

**Result:** ~60% fewer regressions during active frontend refactoring.

### Consensus Validation

Each assertion is verified by multiple models:
- Claude
- Gemini  
- Arbiter model (tie-breaker)

Final result determined by majority vote → fewer false positives.

## Architecture

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│  Natural    │────▶│   Passmark  │────▶│   Redis     │
│   Language  │     │   Engine    │     │   Cache     │
│   Tests     │     └──────┬──────┘     └─────────────┘
└─────────────┘            │
                           ▼
                   ┌─────────────┐
                   │  Playwright  │
                   │   Runner     │
                   └─────────────┘
```

### Flow

1. User writes test in natural language
2. First run: LLM interprets and executes
3. Steps cached in Redis
4. Normal runs: Playwright runner (fast, no LLM)
5. Failure: AI auto-heals failing steps

## Comparison with Other Tools

| Feature | Passmark | Traditional Playwright | SaaS AI Tools |
|---------|----------|------------------------|---------------|
| Natural language tests | ✅ | ❌ | ✅ |
| Open source | ✅ | ✅ | ❌ |
| Self-healing | ✅ (cached) | ❌ | ✅ |
| No LLM on reruns | ✅ | ✅ | ❌ |
| Multi-model consensus | ✅ | ❌ | Varies |
| Self-hosted | ✅ | ✅ | ❌ |

## Benefits

- **60% fewer regressions** during frontend refactoring
- **Cost efficient:** No LLM calls on normal runs
- **Open source:** No vendor lock-in
- **Consensus validation:** Reduced false positives
- **Easy migration:** Drop-in for existing Playwright tests

## Installation

```bash
npm install passmark
# or
pnpm add passmark
```

## Requirements

- Node.js 18+
- Redis (for caching)
- Playwright (peer dependency)
- LLM API key (OpenAI, Anthropic, or Google)

## Related

- [[wiki/testing-strategies]] — Testing approaches overview
- [[wiki/testing-stability]] — Anti-flakiness patterns
- [[wiki/agentic-patterns]] — AI agent patterns

## Tags

`open-source` `playwright` `ai-testing` `regression` `self-healing` `passmark`

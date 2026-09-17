# Anton Gulin — Save Clues from a Failed Playwright Test (2026)

**Source:** https://www.anton.qa/blog/posts/save-failed-playwright-test
**Author:** Anton Gulin (AI QA Architect, former Apple SDET)
**Date:** 2026-09-16
**Runnable project:** https://github.com/antongulin/anton-qa-resources/tree/main/posts/save-failed-playwright-test

---

## Core Problem

Test fails, then passes on retry. You open the recording — see only the successful run. Original failure evidence is gone.

---

## Two Recording Settings

| Setting | What It Records | What You Get |
|---------|----------------|--------------|
| `on-first-retry` | Records the retry attempt | Successful second attempt (original failure LOST) |
| `retain-on-failure` | Records each attempt, keeps failed ones | Original failed attempt (evidence PRESERVED) |

Config in `playwright.config.ts`:

```typescript
{ use: { trace: 'on-first-retry' } }   // default: only retry
{ use: { trace: 'retain-on-failure' } } // keeps failures
```

---

## The Comparison

Practice project: test fills order note, presses Save. Route handler supplies response.

| Attempt | Response | Message |
|---------|----------|---------|
| Original (0) | 503 | "Injected first-attempt save failure" |
| Retry (1) | 200 | "Saved on retry by synthetic fixture" |

**`on-first-retry`:** opens retry → sees 200, success message. No evidence of 503.
**`retain-on-failure`:** opens original → sees 503, error message, failed check. Evidence chain complete.

---

## Why This Matters

- **Flaky tests:** if you only record retries, you lose the failure context
- **Debugging:** you need the original failure, not the successful retry
- **Evidence chain:** which response did the browser ACTUALLY receive on the failed attempt?
- **Trade-off:** more recordings = more storage + potential PII in saved pages

---

## Connections to Our Work

- **Evidence retention = Article 27:** the recording setting determines what evidence survives. If you don't capture it, you can't verify it.
- **`retain-on-failure` = our mutation testing philosophy:** keep the failing evidence, not just the passing score
- **Trace = audit trail:** actions, page views, requests — the full run record (like TestMu's "grade the run, not the response")
- **Config rot (Osmani):** default setting loses evidence. Teams discover too late.
- **Tornhill's double-entry bookkeeping:** same principle — don't let the passing retry overwrite the failing evidence

---

## Related

- `raw/adamtornhill-practices-abandoned-agents-2026.md` — double-entry bookkeeping
- `raw/testmuai-llm-evaluation-vs-e2e-agent-testing-2026.md` — grade the run, not the response
- Article 27: "QA Didn't Get Replaced. It Got Promoted." — evidence chain governance

# Your Regression Suite Is a Museum: 5 Questions That Decide Delete vs Keep

**Source:** https://www.anton.qa/blog/posts/regression-suite-museum (Anton Gulin, AI QA Architect, ex-Apple SDET)
**Date:** August 19, 2026 (DEV cross-post Aug 22)
**Tags:** #regression-suite #mutation-testing #test-maintenance #playwright
**Raw:** [software-testing-weekly-newsletter-2026.md](software-testing-weekly-newsletter-2026.md) (#325 #4)

---

## What It Is

Every sprint adds tests. Almost no sprint deletes one. Result: museum. Cheaper fix than rewriting suite: audit oldest third with 5 questions. On author's last inherited suite, third retired — nothing they "guarded" ever broke. Connected to Yaron Assa "The dust your test suite is kicking up is blocking the light" — always-green tests.

## The 5 Questions (with Playwright Code)

**1. When did this test last fail for a real reason?**
CI history (server test runs) already knows. If never failed on real bug → candidate. Check: `npx playwright test --project=chromium --grep @museum-candidate` history.

**2. What user risk does it guard?**
Write risk in one sentence naming a user: "Guest checkout with expired coupon still charges correctly." If you can't → museum piece.

**3. Would anyone notice if it vanished?**
Experiment, not debate: in branch, skip suspect, run everything else.
```bash
npx playwright test --grep-invert "@museum-candidate"
```
If suite still signals same risk → delete.

**4. Does it check results or steps?**
Tour vs test:
```js
// tour: asserts step happened
await page.getByRole('button', {name: 'Pay'}).click();
await expect(page).toHaveURL(/confirmation/);
// test: asserts outcome
await expect(page.getByTestId('invoice-total')).toHaveText('34.2');
await expect(page.getByTestId('invoice-number')).not.toBeEmpty();
```
Click + URL = tour. Invoice total/number = outcome.

**5. Can it fail at all?**
Flip condition and run — must fail. If passes, test dead:
```js
// original
await expect(status).toBe('paid');
// flipped: this MUST fail. If passes, test is dead.
await expect(status).not.toBe('paid');
```

## What You Get Back

One afternoon on oldest third → one-third retired, signal improved, maintenance down. When agent starts writing tests into suite, this audit is the contract you hold its work against: generated test enters only if it survives same 5.

Also referenced: Gulin's **7 Checks Before You Trust a Green Checkmark** (name risk → break product → check result → change data → read failure → run twice → release decision) and **Playwright v1.60 evidence-first** (scoped HAR, locator.drop(), ARIA boxes).

## Connection to Yaron Assa Dust

Assa: dust (always-green tests) blocks light (real failures). Gulin: 5 questions catch dust. Same theme — green ≠ good.

## Relevance to QA/QE

| Question | Museum Detector | Action |
|----------|-----------------|--------|
| Last real failure? | Never failed | Quarantine / delete |
| User risk? | No named risk | Require risk sentence in test docstring |
| Vanish unnoticed? | Suite still same signal | Branch experiment, delete if silent |
| Results vs steps? | Only steps | Refactor to outcome assertions |
| Can fail? | Flip still passes | Fix or delete dead test |

## Critical Analysis

**Strengths:**
- Actionable, code-backed (Playwright snippets), one-afternoon scope.
- Works as gate for AI-generated tests — not opinion, experiment.

**Gaps:**
- Assumes CI history available; new suites lack signal → need synthetic fault injection as proxy.
- "User risk" sentence is subjective; needs risk taxonomy to be consistent across team.

## Cross-links

- Related: [Anton Gulin 7 Checks](https://www.anton.qa/blog/posts/review-ai-generated-tests-seven-checks)
- Related: [Mutation testing as always-green detector](../wiki/Mutation-testing-advanced-playwright.md)
- Related: [Rick Crawford structural problem](rick-crawford-qe-structural-problem-2026.md) — museum is symptom of test rot (#3)
- Newsletter: [Software Testing Weekly #325](software-testing-weekly-newsletter-2026.md)

---


## One-Afternoon Runbook
1. Take oldest third of suite.
2. Run 5 questions in order; skip debate.
3. For Q1 use CI history; Q2 require one-sentence risk; Q3 branch experiment; Q4 inspect assertions; Q5 flip check.
4. Retire third; measure signal change.

*Ingested: 2026-09-01*

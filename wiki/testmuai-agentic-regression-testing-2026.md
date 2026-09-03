# Agentic Regression Testing: What to Delegate, What to Verify

**Source:** https://www.testmuai.com/blog/agentic-regression-testing/ (TestMu AI, formerly LambdaTest)
**Date:** August 27, 2026
**Authors:** Saurabh Prakash (Engineering Manager, TestMu AI), Reviewer Sai Krishna (Director of Engineering, Appium core)
**Tags:** #agentic-regression #test-selection #self-healing #KaneAI #risk-based
**Raw:** [testmuai-agentic-regression-testing-2026.md](../raw/testmuai-agentic-regression-testing-2026.md)

---

## What It Is

Agentic regression testing moves 3 decisions from script to agent: **which tests run, in what order, what happens to ones that break**. Classic regression answers all three same way every time — predictable but wasteful. Classic AI regression (self-healing locators, visual) = smarter features; agentic = **decision authority moves**. Agent reasons over diff + dependency graph + failure history; run adapts per commit.

Mechanic: TestMu AI **KaneAI** resolves element by intent/context, not single selector; when DOM shifts, re-anchors step and surfaces change for reviewer approval — approval is the design.

## The Delegation Problem

Delegating selection is harder than authoring: bad authoring is visible, bad selection produces **no output**. Developer sentiment (Stack Overflow 2025): 66% frustrated by AI "almost right, but not quite," 45.2% say debugging AI-generated code takes longer. Almost-right selection = plausible, fast, wrong, and nothing surfaces.

Design goal: highest autonomy where mistake still produces visible signal.

## Four Autonomy Levels (Ladder)

| Level | Agent May | Human Still | Failure Visible Because |
|-------|-----------|-------------|-------------------------|
| **1. Advisory** | Rank/recommend subset, flag unaffected | Runs full suite, reads recommendation as report | Everything executes → bad recommendation costs nothing |
| **2. Selective** | Choose which run on PR | Runs full nightly as safety net | Nightly catches miss within day |
| **3. Self-repairing** | Re-anchor locators, retry non-deterministic | Approves each repair before commit | Wrong re-anchor fails loudly, not silently |
| **4. Autonomous** | Rewrite assertions, retire redundant | Audits coverage deltas (nothing else will) | **Not visible** — coverage disappears silently |

1-3 safe in order. 4 worth arguing — edits assertion can make failing test green without fixing defect.

## The Three Decisions

- **Selection:** walks dependency/call graph from changed files → tests that reach them; drops no-path tests; weighted by failure history + business impact. Failure = untracked dependency (shared fixture, config not in graph).
- **Ordering:** ranked by recent failure history + business impact (risk-based per commit). Low risk — everything selected still runs.
- **Maintenance:** repairs broken steps, retries unstable. **Dangerous** if assertion changed — removes coverage without removing test.

**Signal prerequisite:** suite stability. Agent learning from flaky suite learns noise. TestMu AI **Test Insights** ranks by failure frequency: >75% high, 50-75% medium, <50% low; detection = product, fix = human.

## Verifying a Skipped Test (Only Metric That Matters)

Not time saved — **recall on skipped tests**: of faults full suite would catch, what share does subset still catch?

Bar: Facebook **Predictive Test Selection** (Machalica et al., arXiv 1810.05286): cut infra cost **2×** while reporting **95%** test failures and **99.9%** faulty changes. Gap is insight: missing individual failure tolerable if another test catches same fault; missing faulty change is not → change-level held 100× tighter.

**Your measurement loop:**
1. Record subset selected per commit, including dropped tests
2. Run full nightly against same commits regardless
3. For every nightly failure, check was test in selected subset?
4. Count miss when dropped test failed and no selected test failed for same change
5. Track misses per 100 faulty changes; upward trend → drop autonomy level

Teams skipping this loop run smaller suite and hope.

## Why Naive Prompts Backfire

Alonso et al. **TDAD: Test-Driven Agentic Development** (arXiv 2603.17973) on SWE-bench Verified:
- Baseline agent regressions **6.08%**
- +TDD instructions without context → **9.94%** (worse than nothing)
- +pre-change impact analysis (code→tests map) → **1.82%**; second model resolution **24%→32%**

Mechanism: vague "run tests" expands search space → agent satisfies cheaply with non-covering tests. Dependency map narrows to tests that matter. **Impact analysis is not optimization after selection works — it's input that makes selection safe.**

## Real Selection Run (Illustration, Not Benchmark)

5 checks by area on **Selenium Playground** via TestMu AI cloud (Chrome/Win11):

```js
CHECKS = [
 {id:'T01', area:'forms',    url:'.../simple-form-demo', sel:'#user-message'},
 {id:'T02', area:'forms',    url:'.../input-form-demo',  sel:'#name'},
 {id:'T03', area:'dropdown', url:'.../select-dropdown-demo', sel:'#select-demo'},
 {id:'T04', area:'sliders',  url:'.../drag-drop-range-sliders-demo', sel:'input[type=range]'},
 {id:'T05', area:'checkbox', url:'.../checkbox-demo', sel:'input[type=checkbox]'}];
selected = CHECKS.filter(c => changedAreas.has(c.area)); // area==='forms'
```

Console:
```
FULL SUITE      : 5 checks, 4300ms
IMPACT-SELECTED : 2 checks (area=forms), 2050ms
SKIPPED         : 3 checks, 2250ms not spent
```
Honest reading: shape, not scale. Saving is 2,050ms/4,300ms. Whether to keep setting depends on whether skipped 3 would ever have caught fault in `forms` — only full nightly answers.

Cloud config: `LT:Options` (platform Windows 11, build "Agentic Regression Testing") via `hub.lambdatest.com/wd/hub`; selection logic stays independent of execution grid. Every decision as trustworthy as failure history behind it.

## Guardrails Worth Keeping

- **Pin floor suite:** auth/payment/data-integrity always run regardless of diff (blast radius ≠ diff size)
- **Separate repair permissions:** locator re-anchoring auto, assertion edits → review (look similar in diff, differ completely in consequence)
- **Keep nightly full run:** only instrument measuring recall; dropping to save compute removes evidence
- **Model non-code dependencies:** feature flags, config, shared fixtures need explicit mapping
- **Treat root cause as lead:** agentic analysis localizes probable cause for engineer to confirm
- **Review coverage deltas, not just pass rates:** retiring tests can raise pass rate while coverage falls — no red build warns; see **Agentic Test Management** for release-readiness view

## Where to Start

Log ten slowest regression tests for 2 weeks: which failed, what changed in breaking commits. That's input agent needs; building log costs nothing and tests dependency mapping quality. If suite not automated yet → prerequisite (**Automated Regression Testing** guide). Adopt ladder: advisory → selective with nightly → self-repairing with approval per heal. Stop before assertion rewrites until escaped-fault zero for full quarter. KaneAI authors/heals from plain English and exports to Selenium/Playwright/Cypress/Appium.

## Relevance to QA/QE

| Delegation | Action |
|------------|--------|
| Selection via graph | Build dependency graph + failure history; floor suite always runs |
| Locator repair | Delegate — fails loudly, safe |
| Assertion rewrite | Keep human — silent coverage loss |
| Ordering | Delegate — low risk, risk-based sort |
| Skip audit | Measure recall on skipped (Facebook 99.9% change-level bar) |

## Critical Analysis

**Strengths:**
- Explicit ladder with visibility column — correct framing: autonomy where mistake visible.
- Quantified bars: Facebook 2× cost, 99.9%; TDAD 6.08%→1.82% with impact analysis; Stack Overflow 66%/45.2%.
- Concrete run (5 checks, 4300ms→2050ms) + KaneAI intent re-anchoring.

**Gaps:**
- 5-check demo is illustration, not scale; no large-suite data from TestMu AI.
- Requires mature failure history + graph — flaky suite breaks signal.

## Cross-links

- Related: [Zalando agentic snapshot](zalando-agentic-engineering-snapshot-2026.md) (risk-based gate + Identity Broker)
- Related: [Kiro root cause 33s](kiro-root-cause-33s-2026.md) (agent RCA pattern)
- Related: [Autonoma agent regression](autonoma-agent-regression-2026.md) (drift without deploy)
- QA evidence layer: [ai-qa-evidence-layer-validation-evals-guardrails-telemetry.md](ai-qa-evidence-layer-validation-evals-guardrails-telemetry.md)

---

*Ingested: 2026-09-03*

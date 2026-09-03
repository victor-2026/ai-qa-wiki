# Agentic Regression Testing: What to Delegate, What to Verify

**Source:** https://www.testmuai.com/blog/agentic-regression-testing/
**Authors:** Saurabh Prakash (Engineering Manager), Reviewer Sai Krishna (Director of Engineering, TestMu AI / Appium contributor)
**Date:** August 27, 2026 (last updated)
**Fetched:** 2026-09-03

---

Agentic regression testing lets AI agents select, run, and repair regression tests. Learn what to delegate, what to verify, and how to audit any skipped test.

TL;DR: agent chooses which regression tests to run after code change, executes, repairs. Human owns standard of proof for anything skipped.
- Test selection: delegate (graph work)
- Locator repair: delegate (fails loudly)
- Assertion changes: keep human (can turn defect into passing)
- Skip auditing: keep human (nightly full run)
- Autonomy ladder: advisory → selective with nightly safety net → self-repairing with approval
- Signal quality: TestMu AI ranks tests by failure frequency

What Is Agentic Regression Testing? Moves 3 decisions from script to agent: which tests run, in what order, what happens to ones that break. Distinction: AI regression testing = capabilities (self-healing, visual), agentic = who decides. KaneAI resolves by intent/context, re-anchors, approval required.

Delegation Problem: bad authoring visible, bad selection invisible (no output). 66% Stack Overflow Survey 2025: AI almost right but not quite; 45.2% debugging AI-generated code more time-consuming.

Four Levels:
1 Advisory — rank/recommend, human still runs full suite (bad recommendation costs nothing)
2 Selective — choose which run on PR, human runs full nightly (catches within day)
3 Self-repairing — re-anchor locators, retry non-deterministic, human approves each repair (wrong fails loudly)
4 Autonomous — rewrite assertions, retire tests — not safe, coverage disappears silently

Three Decisions:
- Selection: walk dependency/call graph from changed files, drop no-path tests; failure = untracked dependency (shared fixture/config)
- Ordering: ranked by recent failure history + business impact (risk-based per commit); low risk
- Maintenance: repair broken steps, retry unstable; dangerous if assertion changed

Failure history signal: suite stability prerequisite; TestMu Test Insights ranks by failure frequency (flake >75% high, 50-75% medium, <50% low).

Verifying a Skipped Test: metric recall on skipped tests — of faults full suite would catch, what share selected subset still catches. Facebook Predictive Test Selection: cut infra cost 2x, still 95% test failures, 99.9% faulty changes. Track misses per hundred faulty changes via nightly full vs selected subset.

Why Naive Prompts Backfire: Alonso et al. TDAD on SWE-bench Verified: baseline regressions 6.08%, +TDD instructions without context 9.94% worse, +pre-change impact analysis 1.82%, second model 24%→32% resolution. Vague test instruction expands search, invites cheap satisfaction; dependency map narrows.

Real Selection Run: 5 checks tagged by area (forms, dropdown, sliders, checkbox) on Selenium Playground via TestMu AI cloud Chrome/Win11: FULL 5 checks 4300ms, IMPACT-SELECTED area=forms 2 checks 2050ms, SKIPPED 3 checks 2250ms not spent. Need full nightly to know if skipped would have caught fault.

Guardrails: pin floor suite (auth/payment/data-integrity always run), separate repair permissions (locator auto, assertion review), keep nightly full run, model non-code dependencies, treat root cause as lead, review coverage deltas not just pass rates.

Where to Start: log ten slowest regression tests for 2 weeks (failures vs commits that broke them) → dependency mapping quality test. Adopt ladder advisory → selective with nightly → self-repairing with approval. Stop before assertion rewrites until escaped-fault zero for quarter. KaneAI exports to Selenium/Playwright/Cypress/Appium.


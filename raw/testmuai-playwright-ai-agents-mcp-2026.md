# TestMu AI: Playwright AI Agents, MCP, Self-Healing (Parth Mistry, 2026-09-23)

**Author:** Parth Mistry (TestMu AI, SmartUI); reviewer Sri Harsha (Selenium TLC, Appium committer). TestMu AI = ex-LambdaTest.
**Source:** https://www.testmuai.com/learning-hub/playwright-ai/ (fetched 2026-09-25, full text; updated Sep 23 2026).
**Context:** Superset of existing wiki/playwright-test-agents-2026.md (which covers only built-in Planner/Generator/Healer): adds MCP doctrine, KaneAI/Kane CLI, SSO/storageState, reviewable-unit ownership, determinism split, ZeroStep death. Vendor page (TestMu grid pitch inside) but doctrines are vendor-neutral and strong.
**Captured:** 2026-09-25 from webfetch.

---

## Core doctrines (vendor-neutral, keep)

- **Determinism split:** Playwright deterministic (same script, same actions) vs OpenAI API reasoning (varies). Model OUT of regression execution path; model IN authoring/diagnosis. "Generate code once, run deterministically" - per-execution model resolution multiplies latency×cost×browsers×locales.
- **Healer local-only caveat:** heals against local browsers; healed suite MUST rerun on real grid (Safari/old Edge) before trust.
- **SSO/storageState:** bot-protection stops MCP agents by design; seed authenticated session/storageState or non-prod credential flag. Auth = design problem, not agent limit. (Matches our OrangeHRM/FlowScout practice.)
- **Reviewable unit = committed code:** engineer opening the PR must explain every locator/wait/assertion. Silent self-heal (rewriting locators without human approval) REMOVES the review step that keeps suite trustworthy. = attestation-adjacent rule.
- **Durable context:** AGENTS.md + reusable agent skills > per-prompt pasting; coding-agent familiarity matters more than any single product.

## KaneAI / Kane CLI (vendor layer, factual)

- KaneAI: NL→executable steps with assertions, intent-based element resolution (not emitted selectors), multi-framework export, two-way NL/code editing, self-heal surfaced for APPROVAL, RCA + auto bug ticket, API/DB/WCAG/visual in one run, PRD/Jira/PDF/recording/PR-diff inputs.
- Kane CLI: natural-language objective in real Chrome (DevTools), user- reachable-actions only (no JS injection to force pass); agent mode NDJSON + run_end; POSIX exits (0/1/2/3) for CI gating; Playwright export; autoheal rejects low-confidence matches upfront (anti-quiet-pass).
- Grid: 3,000+ browser/OS combos rerun for healed suites.

## Ecosystem notes

- ZeroStep DEAD (DNS gone 08.2026) - suites on it need replacement authoring layer.
- SO Survey 2025: 46% distrust AI accuracy vs 33% trust; only 27.5% use AI even partially for testing.
- Third-party: auto-playwright (844⭐, experimental), ChatGPT/Claude drafting (no execution - validate selectors), Codegen (deterministic, no AI).

## Cross-links

- pilots/TestMu/ (W3 catalog dir) - vendor side; this page = methodology side.
- Existing wiki/playwright-test-agents-2026.md - built-in agents subset (RU); keep both, link.
- SSO/storageState practice ↔ OrangeHRM/FlowScout runs; reviewable-unit rule ↔ attestation doctrine.

## Use for us

- Determinism-split + reviewable-unit doctrines are quotable for Articles (26/27) and the W3 Jev-comparison framing (model in authoring, never in execution path).
- Kane CLI POSIX-gate + export pattern = reference design for CLI-first verification steps.
- Healer-local caveat justifies grid-rerun requirement in our own pilot acceptance criteria.

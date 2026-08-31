# Property-Based Testing Caught a Security Bug I Never Would Have Found

**Source:** https://kiro.dev/blog/property-based-testing-fixed-security-bug/
**Date:** December 18, 2025
**Author:** Krishiv Dakwala (SDE)
**Tags:** #pbt #fast-check #security #spec-driven #kiro
**Raw:** [kiro-property-based-testing-security-bug-2026.md](../raw/kiro-property-based-testing-security-bug-2026.md)

---

## What It Is

Real Kiro SDD (spec-driven development) case where Property-Based Testing with fast-check found a prototype-pollution-adjacent bug on trial #75 that human review and unit tests missed.

**Spec:** storage service for chat app, localStorage for API keys by provider name. Requirement acceptance criteria #2 → round-trip property: for any `provider` and `key`, `save(provider,key)` then `load(provider)` == `key`.

**Implementation (LLM-generated):**
```ts
const apiKeys = {};
function saveApiKey(provider, key) { apiKeys[provider] = key; JSON.stringify(apiKeys); }
function loadApiKey(provider) { return apiKeys[provider]; }
```
Looks solid. Code review would pass.

**PBT:** 100 iterations, random strings. Counterexample: `provider="__proto__"`, `apiKey=" "`. Save then load returns `{}` (empty object, the prototype) instead of `" "`. Failure Shrunk to minimal value (`" "`), proving provider is the culprit.

## Root Cause

JavaScript prototype-based inheritance: every object has `__proto__` pointing to parent. `apiKeys["__proto__"] = " "` doesn't set a property — engine rejects string as prototype, keeps original prototype. `load` returns that prototype (`{}`).

With attacker-controlled strings, non-string `apiKey` could inject into prototype (prototype pollution), poisoning future reads. Here not directly exploitable (`apiKeys` short-lived, `JSON.stringify` skips `__proto__`, not global prototype), but refactor could widen impact.

## The Fix (MITRE CWE-1321)

1. **Safe storage:** `const apiKeys = Object.create(null)` — null prototype, `__proto__` becomes regular key.
2. **Safe retrieval:** defensive load with `Object.prototype.hasOwnProperty` style checks.

## Why PBT Found It

- **Bias injection:** Humans/LLMs test happy paths they imagined; PBT injects institutional wisdom via generators. `__proto__` is a built-in edge string in fast-check's corpus — collective knowledge, not model guesswork.
- **Shrinking:** minimal counterexample isolates cause.
- **Configurable runs:** `numRuns: 100` (Kiro default) — raise for confidence, lower for speed. Executable specification: property is requirement you can run, bridging spec → evidence.

## Bigger Picture (Kiro SDD + PBT)

1. Properties map directly to requirements (round-trip = requirement).
2. Random generation explores space humans skip.
3. Tight feedback loop: failing property → minimal counterexample → fix.
4. Catches bugs code review / hand-picked unit tests / integration tests miss.

## Relevance to QA/QE

| Pattern | Action |
|---------|--------|
| Round-trip property | Template for storage/config APIs: `save(x) → load(x) == x` for arbitrary x |
| Built-in edge corpus (`__proto__`, `constructor`, etc.) | Don't hand-pick edges; use fast-check/Hypothesis generators |
| Executable spec | Make acceptance criteria testable before coding |
| 75th trial failure | Run 100+ iterations in CI; deterministic seed for repro |

## Critical Analysis

**Strengths:**
- Real production-adjacent bug, not toy; shows LLM-generated code not immune.
- Clear SDD flow: requirement → property → code → PBT → fix.

**Gaps:**
- Fix addresses prototype but broader pollution (e.g., `constructor`) not discussed; need allow-list or Map.
- 100 runs is heuristic — false confidence if input space huge; seed not mentioned.

## Cross-links

- Related: [Does your code match your spec? (PBT)](https://kiro.dev/blog/property-based-testing/) — tutorial companion
- Related: [Bug fix paradox](kiro-bug-fix-paradox-2026.md) — same SDD property mindset
- Related: [Diagnostics over time](kiro-diagnostics-over-time-agent-quality-2026.md) — static vs dynamic signals
- PBT in wiki: [pbt-llm-code-generation.md](pbt-llm-code-generation.md)

---


## Lessons for QA: LLM-Generated Code Is Not Bias-Free
- Same entity (human or model) that writes code also writes unit tests → shares blind spots.
- PBT breaks that symmetry by pulling edge corpus from community (fast-check maintainers encoded `__proto__`, `constructor`, `0`, `NaN`, empty strings).
- Kiro's SDD makes property first-class: requirement → property → code → PBT → shrinking → fix → re-run. Evidence loop closed before human review.
- 100 runs is cheap; failure on run 75 shows why hand-picked 5-10 examples miss rare but critical paths.
- Map vs plain object: using `Map` would avoid prototype issue entirely — PBT pushes toward safer abstractions.


## Checklist for Your Codebase
- Replace plain objects for dynamic keys with `Map` or `Object.create(null)`.
- Add fast-check to CI with 100 runs default, 1000 on PR for storage/security modules.
- Encode requirement as property in spec doc — makes hypothesis and test co-evolve.

*Ingested: 2026-08-30*

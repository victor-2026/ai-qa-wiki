# Root Cause in 33 Seconds: How Kiro CLI Saved 4 Years of Build Time

**Source:** https://kiro.dev/blog/root-cause-in-33s/
**Date:** April 16, 2026
**Authors:** Cameron Conradt, Sameer Bansal
**Tags:** #kiro-cli #root-cause #performance #autonomous #subagents
**Raw:** [kiro-root-cause-33s-2026.md](../raw/kiro-root-cause-33s-2026.md)

---

## What It Is

Kiro CLI investigated a performance bottleneck in 33 seconds, identified root cause, and implemented fix saving ~4 years of compute per month. Context: internal config build packages, P99 build 25-30 min, 381 packages built 550K times/month across EC2 and AWS teams.

**Prompt:** single instruction with structured `perf` report. Agent did 10 autonomous turns.

## Root Cause

Config file parser re-initialized on **every function call** across multiple subroutines — each call created new parser instance, re-read/re-parsed same config files from disk. Parser accounted for ~79-80% CPU (perf call tree). Fix: shared cache keyed on config params (parse once, reuse).

Result: P99 30 min → <1 min. Kiro implemented 80-90% of code changes; engineers reviewed, built, validated.

## How Kiro Investigated (10 Turns)

1. **Orient:** `generate_codebase_overview` + `search_codebase_map` + `fs_read` (directory) — build mental model of unfamiliar repo without reading every file.
2. **Read profiling data:** `fs_read` (line mode) on `perf` report — parsed call tree, hottest path = parser core + token parsing + I/O.
3. **Delegate:** `use_subagent` — specialized code-analyzer subagent queried: "find build tool locations for perf optimization" — keeps main context clean, runs parallel.
4. **Locate code:** `glob` + `fs_read` on plugin/config modules — found repeated `new Parser(...)` with identical params.
5. **Implement:** `fs_write str_replace` — added hash cache + helper `getParser()` checking cache before instantiation + refactored all call sites to use cache. Surgically preserved behavior, eliminated redundant init.

## Tools That Made It Possible

- **Code intelligence:** `generate_codebase_overview`, `search_codebase_map` — fast orientation in unfamiliar codebase
- **File system:** `fs_read`, `fs_write`, `glob` — reading perf data, inspecting code, writing fix
- **Subagent delegation:** `use_subagent` — focused analysis without polluting main context

## Lessons

- **Generalist agent for investigation** — open-ended "why slow?" needs cross-file reasoning, not just code generation. Kiro chains tools autonomously.
- **Trust but verify** — agent did majority autonomously; humans still built and validated before ship.
- **ROI compounds at scale** — 30 min feels personal; ×550K builds/month = infra cost. Fix surfaced only in aggregate.
- **Chaining, not single tool, is the differentiator** — context building → hypothesis → validation → fix.

## Relevance to QA/QE

| Pattern | QA Application |
|---------|----------------|
| Single prompt + structured perf input | Provide agent with structured logs/metrics/report as context for RCA |
| Orient before dive (`overview` + `map`) | Use codebase overview tools before deep debugging unfamiliar services |
| Subagent delegation | Isolate focused subtasks (log analysis, code search) to keep main agent context clean |
| Cache vs re-init pattern | Classic perf anti-pattern — add to review checklist: repeated expensive init in hot path |
| 33s investigation, human validation | Automate RCA draft, keep human gate for correctness/safety |

## Critical Analysis

**Strengths:**
- Concrete impact metric (4 years/month) and before/after (30m → 1m).
- Shows Kiro beyond code gen — generalist investigation.
- Clear tool trace (10 turns) — auditable.

**Gaps:**
- Requires well-structured `perf` reformatting (step called out as "this matters" but details light).
- 80-90% autonomy still needs human validation — not full auto-merge.
- Single anecdote; no stats on failure rate or false hypotheses.

## Cross-links

- Related: [Kiro diagnostics over time](kiro-diagnostics-over-time-agent-quality-2026.md) — diagnostics as verification after fix
- Related: [Trust agent triage](kiro-trust-agent-triage-2026.md) — same CLI harness, ticket pipeline
- Related: [How We Learned to Trust](kiro-trust-agent-triage-2026.md) — same authorship team patterns

---


## Engineering Takeaways (Expanded)
- **Structure your perf input:** raw `perf` is noisy; reformatting call tree + percentages into markdown table made LLM reasoning tractable. Invest once in perf formatter.
- **Subagent keeps main clean:** delegating code search prevented context bloat — main agent stayed in 10-turn budget.
- **Fix is cache, not rewrite:** cheapest correct fix (shared instance) beats re-architecting parser. Agent chose minimal preservation-preserving change.
- **Validate with build:** 80-90% auto still required `./build` run — gate remains mandatory.
- **Scale reveals ROI:** single-user pain invisible; aggregate build-count reveals infra cost → prioritize fixes by total compute saved.


## Anti-Pattern to Watch
Repeated `new ExpensiveService(config)` in loop/hot path is common agent-generated pattern — agent favors correctness over reuse. Add lint rule or review prompt: "reuse parser/client/connection; do not re-init in loop" — steering prevents recurrence.

Additional note: combine with mutation testing — C/¬C partition becomes mutant kill/preserve oracle.

Note: 33s wall-clock excludes human build/validation — end-to-end with review ~5-10m, still order-of-magnitude faster than manual days.

*Ingested: 2026-08-30*

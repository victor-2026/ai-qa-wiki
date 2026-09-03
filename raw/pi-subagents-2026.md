# pi-subagents

**Source:** https://github.com/nicobailon/pi-subagents
**Fetched:** 2026-09-03

---

pi-subagents lets Pi delegate work to focused child agents. Use it for code review, scouting, implementation, parallel audits, saved workflows, background jobs, and anything else that benefits from a second or third set of model eyes.

Install: pi install npm:pi-subagents

Try this first: Use reviewer to review this diff. Ask oracle for second opinion. Use scout to understand code, then ask clarification. Run parallel reviewers: one for correctness, one for tests, and one for unnecessary complexity.

How it works: Pi is parent session. Subagent is focused child Pi session with own job. Foreground streams, background keeps working. Installing does not start automatic reviewer, gives delegation tool. If you want every implementation reviewed, say so in prompt.

Builtin agents: scout (recon), researcher (web/docs), worker (implementation), reviewer (code review), oracle (second opinion), delegate (general).

Common workflows: council, parallel reviewers, implement then review, review loop, scout before planning, background, saved workflows.

Where running work shows up: FleetView below editor, /subagents-fleet inspector, machine-readable artifacts.

Bounded orchestration: maxSubagentSpawnsPerRun defaults to 64.

[Full README truncated — see wiki for structured summary; fetched via raw GitHub README 2026-09-03]


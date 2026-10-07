# Self-diagnostics protocol (DRAFT for review, 07.10, W5)

Status: proposal. Implementation (hooks/scripts) = W2 territory if accepted. Patient in mind: context-heavy windows showing degradation (self-corrections) — healthy windows ignore.

## Triggers

- Session start.
- Every ~20 tool calls.
- Before commit/push.
- After any provider error or blocked call.

## Checks (read-only, cheap)

1. **Tree:** bare `git status --short`. Dirt in foreign files = stop, investigate, never commit.
2. **Lint cache:** broken links must be 0; topics growth sane. Full lint only if wiki touched.
3. **Read verification:** after blocked calls — grep, not tail (shared checkout interleaves). Claim without path:line = draft.
4. **Error counter:** 2 identical failures in a row = stop and change method. No third retry.
5. **Context proxy:** % is not visible to the agent. Proxy for owner: turn count + volume read. On degradation signs (typos, self-corrections, repeated reads) — report to bus, no heroics.

## Report format

5 lines max, hyphen-only, to checkpoint or bus on demand:
`diag: tree [clean/dirty:X] / lint [broken N] / verify [grep-ok] / errors [count] / context [turns ~N, reads ~K]`

## Non-goals

- No auto-fix of anything destructive.
- No new hooks by this file (text only).
- No diagnosis of other windows — each window self-reports.

---
*Scope (fixed 07.10 per W2 review): text protocol, ai-qa-wiki ops lane, maintainer W5. No hooks, no cross-window infra. Numbers below are owner-reported 07.10 (bus), not measured — treat as triggers, not metrics.*

# Executor/Evaluator Split: Radik Zagirov (Agentiqa) Architecture Post (2026-09-09)

**Source:** Radik Zagirov (Co-Founder & CEO, Agentiqa) LinkedIn post, 2026-09-09 (~33m before capture). Thesis: same model family writing code AND tests automates a shared blind spot.
**Why in wiki:** general verifier-architecture pattern (executor ≠ evaluator), not vendor news. Directly testable — mapped against our Agentiqa pilot (M0-M6) below.

## The 4 mechanisms (vendor claims)

1. **Codebase-blind execution** — testing agent has zero repo/mocks/test-files access; interacts with deployed preview via Chrome CDP as external observer. Cannot edit assertions to force green.
2. **Heterogeneous cross-model audit** — Model A (driver, one family) executes; Model B (different family) audits WITHOUT seeing A's scratchpad — only raw artifacts (DOM mutations, HAR, viewport frames) vs initial product intent. Different weights → catches what A missed.
3. **Terminal-state assertion** — browser session stays alive past endpoint 200/202; verifies RENDERED terminal state (catches dropped background payloads that exit-code CI misses).
4. **Append-only evidence logs** — network payloads, console events, frame recordings per run; green checkmark = lossy compression, they keep history.

## Mapping against our pilot evidence (M0-M6, 2026-09-08)

- **Consistent (1):** agent never touched code, healed via UI only (M1 label, M3 position) — blind execution holds.
- **Consistent (3):** valid login judged by Dashboard render, not POST 200 (baseline 3/3, M5 screenshots) — terminal-state holds.
- **Consistent (4):** per-run video + screenshots + runUrl/batchUrl artifacts — evidence trail holds (HAR not inspected — minor gap).
- **TENSION (2):** M3 textless button → 0 issues; M4 duplicate field → misattributed to credentials. If Model B audits raw artifacts vs intent, why no UI-root-cause flag? Fair reading: auditor is INTENT-scoped (login works → no flag), not UI-complete. Silence is then by design, not a miss — but the boundary is undocumented.
- **"Weaken assertion to exit 0" warning:** our M1/M3 passes adapted (found the control) rather than weakened (no assertions exist to weaken — plan steps are NL). No contradiction observed.

## Follow-up question for vendor (when thread resumes)

Is the auditor's silence on UI-level defects (missing button text, duplicate fields) INTENT-scoped by design — and if so, where is that boundary documented for users reading green reports? (Feeds Article 26 red-flag list: confidence without methodology.)

## Links

- Pilot: Agentiqa pilot-log rows 26-39 (`company/pilots/Agentiqa/` in Positions-CV-CL vault — cross-vault, open by path)
- Method: [[ai-qa-tool-evaluation-mutation-matrix]]
- Qase deterministic gates: https://www.qase.io/blog/test-management-for-ai-coding-agents/
- Article 26 (playbook, unpublished — link after 14.09 release); DevAssure Antigravity post (URL TBD)





<!-- backlinks-start -->
### Backlinks
- [Boris Cherny Claude Maintains Apps 2026](wiki/boris-cherny-claude-maintains-apps-2026.md)
- [Ilya Kabanov Cybersecurity Ai Cost 2026](wiki/ilya-kabanov-cybersecurity-ai-cost-2026.md)
- [Ishan Anand Llm Persona Feedback Failure Modes 2026](wiki/ishan-anand-llm-persona-feedback-failure-modes-2026.md)
<!-- backlinks-end -->

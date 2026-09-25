# Addy Osmani — Agentic Autonomy Levels (2026)

**Source:** https://addyo.substack.com/p/agentic-autonomy-levels
**Author:** Addy Osmani (Member of Technical Staff, Anthropic)
**Date:** 2026-07-03
**Engagement:** 103 likes, 11 comments, 11 restacks

---

## Core Thesis

> The core question about an action is always: what level does this task deserve, and what verification makes that level defensible?

Two axes, not one ladder: **agency** (how far from yourself you let a single agent go) and **orchestration** (your skill at coordinating many agents). Yegge's single-axis ladder conflates them.

---

## The Six Levels

| Level | Name | Description | Verification |
|-------|------|-------------|--------------|
| L0 | **Assist** | Suggestions, you decide | Local verification |
| L1 | **Supervised action** | Agent edits/runs, asks before executing | Approval fatigue risk; Codex Auto-review delegates final approval to separate reviewer agent |
| L2 | **Scoped task delegation** | Bounded task with clear goal + constraints | Shifts from you to evidence: tests, types, lint, screenshots |
| L3 | **Goal-driven autonomy** | Agent does whatever it takes to meet measurable stopping condition | Plan→act→test→review cycle; goal must be automated/measurable |
| L4 | **Parallel delegation** | Many agents in parallel, isolated slices | Decomposition is bottleneck; false parallelism = merge conflicts |
| L5 | **Managed-by-exception** | Manager agent dispatches, monitors, verifies, escalates | Issue tracker as input, PRs as output; independent verification critical |

Three eras: L0-L1 (driver's seat), L2-L3 (agent takes bounded charge), L4-L5 (orchestration, management by exception).

---

## Risk & Reversibility Set the Ceiling

Three questions to determine true high autonomy:
1. How quickly will we know we're wrong about what it's doing?
2. How cleanly can we undo what it's doing?
3. What would prove we're right about what it's doing?

If answers are "not quickly, great difficulty, trusting the summary" → it's NOT high autonomy.

---

## Agent Contract (Pre-Run)

Every run needs: goal, scope, non-goals, tools/permissions, stopping condition, evidence, escalation, budget.

---

## Four Anti-Patterns

1. **Autonomy as status** — higher autonomy treated as capability proof, not safety
2. **Permission laundering** — approval fatigue → grant overly broad access
3. **Summary substitution** — agent summary replaces review
4. **Fleet cosplay** — many agents run, human still orchestrates every dependency manually

---

## Key Metrics

Mean time between interventions, longest successful unattended run, sandbox vs escalated ratio, auto-approved vs rejected %, agent actions per human instruction, review time per change, rework rate, defect escape rate, token cost per accepted change.

---

## Connections to Our Work

- **Six levels ≈ our zones (Green/Yellow/Red) + B0–B3 tiers:** both map autonomy to verification confidence. Osmani's L0-L5 is agency axis; our B0-B3 is risk axis. Complementary.
- **"Verification will always be the bottleneck"** = Article 27 core thesis. QA role IS the verification bottleneck by design.
- **Agent contract ≈ per-risk-tier step 0 (relevance gate):** define goal, scope, evidence BEFORE execution.
- **Anti-pattern "summary substitution"** = what VerdictGate detects: score without evidence.
- **Calibrated autonomy** = staged ramp §8 v0.3 (trivial → realistic → industry pool).

---

## Related Wiki

- `wiki/addy-osmani-brownfield-agentic-engineering-2026.md` — zones as practical autonomy mapping
- `wiki/addy-osmani-human-judgment-software-factory-2026.md` — where humans go in the factory
- `wiki/addy-osmani-own-the-outer-loop-2026.md` — accountability at the boundary

## See also

- [Addy Osmani — Agentic Code Quality (2026)](wiki/addy-osmani-agentic-code-quality-2026.md)

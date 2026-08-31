# The Bug Fix Paradox: Why AI Agents Keep Breaking Working Code

**Source:** https://kiro.dev/blog/bug-fix-paradox/
**Date:** February 19, 2026
**Author:** Jatin Arora (Applied Science)
**Tags:** #bugfix #property-aware #pbt #hypothesis #differential-testing
**Raw:** [kiro-bug-fix-paradox-2026.md](../raw/kiro-bug-fix-paradox-2026.md)

---

## What It Is

Problem: agent fixing a bug refactors unrelated helpers, adds defensive null checks (agents 2x more likely than humans to add guard clauses), invents edge cases, breaks working code — sledgehammer vs scalpel. Drift worsens with iteration.

Solution: **Property-aware code evolution** — make the boundary between "fix" and "preserve" explicit and testable.

## Core Model: Bug Condition + Postcondition

- **Bug condition C** = input partition where bug triggers.
  - C holds → buggy (want change)
  - ¬C → working (want preservation)
  - Example BST delete crash: `node has two children AND node.right.left is None`

Without explicit C: agent drifts, invents boundary, can't check preservation.

- **Postcondition P** = what "fixed" means for C inputs (e.g., delete doesn't crash, removes node, preserves BST invariant). Without P, agent can `try/except` and call it fixed.

**Two properties (partition entire input space):**
- **Fix property:** `C ⟹ P` — patched code satisfies P when C holds
- **Preservation property:** `¬C ⟹ unchanged` — patched code behaves identically to original when C doesn't hold

## Kiro Bugfix Workflow (BST Example)

Bug: `BST delete crashes when right child has no left subtree`.

1. **Bugfix doc (requirements):** Kiro analyzes report → categories: defective behavior (crash on C), expected fix (P), unchanged behavior (all ¬C). Mirrors C partition.
2. **Design:** Formalize `C` and `P` in code, trace root cause hypothesis:
   - Hypothesis: `_find_min(node.right.left)` called instead of `_find_min(node.right)`; when C holds, `node.right.left is None` → crash `None.left`.
   - **Checkpoint:** Review C/P/hypothesis before any code/tests. Hypothesis falsifiable: fix-property tests should fail on unfixed code with `AttributeError`; if different failure / no failure → hypothesis refuted, re-analyze.
3. **Task plan (red-green + differential):**
   - Task 1: bug-condition tests (PBT Hypothesis) for C → run on unfixed code → fail (confirms bug at predicted boundary)
   - Task 2: preservation tests for ¬C — record unfixed behavior, assert identity → pass on unfixed (baseline)
   - Task 3: patch (one line: `_find_min(node.right)`), rerun both suites → bug tests now pass, preservation still pass. If preservation flips → side effect, narrow patch.
4. **Testing:** Property-based (Hypothesis) — generates hundreds of trees covering combinatorial structure vs hand-crafting.
5. **Scale example:** RocketMQ HeartbeatSyncer leak — map key mismatch (`consumerGroup + channel` on insert vs channel only on remove → never matches, every unregister leaks). Same workflow: 5 preservation paths (null args, non-ClientChannelInfo, multi-group, etc.) each captured before fix; fix one line.

## Why PBT Here

Structure-dependent bug (tree shape) — combinatorial. Unit tests miss combinations; PBT explores automatically.

## Relevance to QA/QE

| Pattern | QA Action |
|---------|-----------|
| Explicit C/P before code | Require bug ticket to define reproducible condition + expected invariant; agent proposes, human approves |
| Fix vs preservation split | Generate two suites: regression suite = preservation property; verifies no collateral breakage |
| Hypothesis as falsifiable prediction | Don't just test fix — test that bug-condition tests fail pre-fix for expected reason |
| Differential testing (unfixed as spec) | Preservation oracle = original behavior, not imagined expected |

## Critical Analysis

**Strengths:**
- Dual-intent (change + preserve) made testable; catches over-fixing.
- Checkpoint prevents wasting code on wrong hypothesis.

**Gaps:**
- Best for functional/testable properties (logic, edge cases, exceptions). Non-functional (perf, race) hard to express as P — open research.
- Requires quality hypothesis; if hypothesis wrong but tests still crafted to pass, gives false confidence.

## Cross-links

- Related: [PBT security bug](kiro-property-based-testing-security-bug-2026.md) — same SDD loop
- Related: [Diagnostics over time](kiro-diagnostics-over-time-agent-quality-2026.md) — static signal complements dynamic property checks
- Concept: [PBT LLMs](pbt-llm-code-generation.md)

---


## Limitations in Practice
- C/P formalization is extra upfront cost — worthwhile for critical paths, overkill for trivial typos.
- If bug report is vague ("app slow sometimes"), deriving C is hard → Kiro flags before code, forcing clarification — good gate, but slows vague tickets.
- For concurrency/perf, property `unchanged` is non-deterministic (timing, ordering) → needs statistical oracles, open research.
- Preservation tests compare to original behavior — if original already wrong on ¬C, you preserve a bug. Requires human review of baseline.


## When to Use (Heuristic)
Use property-aware flow when: bug has clear C, fix is functional, regression risk high. Skip when: one-off typo, urgent hotfix where writing P costs more than manual QA. Hybrid: let agent draft C/P, human approves in 2 min — keeps contract without heavy overhead.

Additional note: combine with mutation testing — C/¬C partition becomes mutant kill/preserve oracle.

*Ingested: 2026-08-30*

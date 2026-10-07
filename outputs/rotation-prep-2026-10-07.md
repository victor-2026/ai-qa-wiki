# Rotation prep package (DRAFT, NOT executed, 07.10, W5)

Trigger proposal (owner): prepare at 70% W1-context (now 58%). Execution ONLY on explicit owner order with explicit cutoff. This file is the plan, not the act.

## Lessons banked (load-bearing)

- W1 07.10 (f6cde42): blocked calls WRITE — verify by grep, not tail (shared checkout interleaves foreign lines). Bare git commands always (third trip on chained-output garbage).
- 10-04 post-mortem (standing): no concurrent rotations, single writer, push before + after, commit right after edit (uncommitted tree evaporates between turns).
- W2 reconfirm 07.10: rotation now = quote rot + repeat 10-04. Deferred to quiet moment or degradation-trigger with explicit cutoff.

## Live-quote inventory (method, not exhaustive)

Known-hot ranges cited across windows (from bus traffic 02-07.10): bench/D-series/escape/Rook tracks, checkpoint:372-385, :405-413, archive:3476+, plus all 07.10 W5 sections (digest triage, Jason audit, LD, Avito, bus-1/bus-2, stops). Rule at execution: grep the bus + other windows' checkpoints for `checkpoint:` refs in last 7 days — everything hit stays live, no exceptions. Re-verify by grep AFTER any move (W1 lesson).

## Cutoff candidate (PROPOSAL, owner decides at execution)

- Live file starts 10-02 (10-04 rotation already archived to session-archive-2026-09.md).
- Candidate: keep 10-06..today live, archive 10-02..10-05. Rationale: active tracks (bench, D, escape, Rook, Jason, LD) all touched 06-07.10; older = settled history.
- Alternative (thinner): keep 7 days rolling. Cost: bigger live file, zero rot risk.
- Owner picks one at order time. No default executes.

## Handover skeleton (for the fresh window)

1. Identity: W{окно}, project, owner files.
2. State pointers: this checkpoint (live part only) + session-archive-2026-09.md + WATCHLIST.md + window-discipline.md + outputs/rotation-prep (this file, then stiffness: delete after use).
3. Open tracks table: track / owner / next step / blocked-on.
4. No-go: foreign files list + 5-foreign-exclusion habit + guard markers.
5. First action: read tail-50 + handover, confirm inline.

## Pre-flight checklist (execution time)

1. Push all windows (clean trees) — verify by `git status --short`, bare call.
2. Single writer announced in bus; others hands off checkpoint.
3. Move sections (Edit tool, append-only target), grep-verify counts before/after.
4. Re-run live-quote grep — zero dangling refs or abort.
5. Commit + push, bus confirmation. Delete this prep file or mark USED.

## Cheap relief (no rotation, valid now)

- tail-50 + pinpoint reads only (adopted all windows).
- Heavy fetches/reads via bus to fresh-context windows.
- Disk (cosmetic, not context): pre-10-07 lint reports ~420K (regenerable), wiki_llm.log 80K truncate — both need explicit order, NOT done here.
- s1web jsonl 4.3M + _backup_chapters 792K = foreign (W2), flagged only.

---
*Status: PREP ONLY. Rotation deferred. Trigger watch: W1 70%.*

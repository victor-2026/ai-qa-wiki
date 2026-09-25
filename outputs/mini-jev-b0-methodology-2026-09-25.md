# B0 Methodology: Banking77 high-cardinality probe via local judges (2026-09-25)

**Scope:** frozen. B0 case (30 queries × 77 labels, first-seen prototypical) + P0 7-findings trial. No extensions without a new stamp.

## Freeze

- Judge A: `qwen2.5:3b` (digest `357c53fb659c5076de1d65cc`, temp 0, fixed one-line prompt). Judge B: `qwen3:4b` (pulled 2026-09-24, temp 0, think ON default).
- Runner code versioned in outputs/ (`mini-jev-local-runner-*`, `mini-jev-b0-runner-*`). Prompt/temp/model change → new stamp + rerun.

## Scoring rules

- Exact label match, **case-insensitive** (handover B0-30 gold lowercase vs Capitalized label; exact-match would false-negative a correct answer - documented, not silently fixed).
- UNPARSEABLE only when output matches no label (B0-12 qwen2.5 invented `Get_virtual_card` - counted as miss, correctly).
- Stability: 3 runs per item at temp 0; reported per (id, run).

## Model-specific requirements (earned the hard way)

- **qwen3:4b REQUIRES think ON.** think=false breaks instruction-following on this Ollama build (prompt echo → 0/90 void run, discarded). Thinking tax: median ~24s, max 461s per call.
- **qwen2.5:3b:** no thinking mode; steady ~0.1s warm, cold load ~100s one-time per Ollama restart/eviction.

## Harness incidents (logged, not hidden)

1. `false`/`False` NameError (sed JSON→Python) - void 90-call run, discarded, no data kept.
2. Paren-surgery syntax breaks during patching - runner clean-rewritten, syntax-verified before runs.
3. Overwrite-instead-of-merge data loss (28-row chunk; aggregates kept: 28 HIT) - runner switched to incremental save + merge-skip + slices. Lesson: never single-shot long batches; always incremental persistence.

## Latency reporting rules

- Report min/median/max + cold-vs-warm split, never bare means. Order-of-magnitude language in prose ("~0.1s", "~tens of seconds"); exact figures live in raw JSON only.
- Transport (LAN vs ZeroTier) measured separately (Phase D: identical verdicts, 5.9s both paths).

## Limitations (for merge/report)

- n=30 first-seen prototypical queries (round 1 per handover; ambiguous/low-distance round 2 pending).
- Generative judges, NOT System-One logprob readout - black-box agreement comparisons only.
- qwen3:4b numbers carry thinking-latency regime (10-460s); not comparable to qwen2.5 latencies as "same task cost".
- Full n=30 gold campaign (Phase A, human labels) still pending; B0 measures judge-vs-dataset, not judge-vs-gold.

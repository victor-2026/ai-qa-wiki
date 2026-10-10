# Agent Plasticity: Self-Improvement Through Experience (Meta et al. 2026)

**Source:** Singh et al. (Meta Superintelligence Labs + Berkeley/UW/Princeton), arXiv 2610.08902 (Oct 2026, 43pp). Raw: `raw/2610.08902v1.pdf` (selective read 10.10: abstract, protocol, §3.2–3.4, discussion, conclusion). Vendor-adjacent (Meta authors) but peer-style with honest limits.

## Definition: plasticity Psat

Held-out score gain per $1,000 learning cost, up to saturation. Setting: **frozen weights** — agent amortizes experience into persistent artifacts (tools, skills, memory, CLAUDE.md edits); every checkpoint scored on held-out games (ID + OOD). Three questions: does future performance improve + generalize; how efficiently; where does the loop break.

## Headline numbers

| Model | Psat (3-game) | Note |
|---|---|---|
| GPT-5.6 Sol | 298 | highest efficiency; NetHack declines (570→420) — task-dependent |
| Claude Opus 5 | 233 | strong both |
| Claude Fable 5 | 57 | highest endpoint (chess 37.5→73.3%) but pricey learning |
| Claude Opus 4.8 | 14 | Easy-only gains; Go loses ground |
| GPT-5.6 Luna | 0 | no reliable rise |
| Opus 5.5 NetHack | 61.75 | 2k→6k score, saturates ckpt 11 |

Best-final ≠ most-efficient (Fable vs Sol). OOD transfer smaller/inconsistent. Opus 5 Go gains wiped by a late tool-making error.

## Bottlenecks (failure tracing)

Low-plasticity: **fail to reuse** relevant artifacts. High-plasticity failures: reuse but fail → artifact **quality / generalization / application** limits. Reuse associated with gains, never sufficient.

## Limits (author-stated)

Protocol-dependent (not a universal ranking); pricing-dependent; experience-vs-compute confound unresolved; saturation-fit uncertainty. Finding 1: evaluate plasticity across task distributions, never as a model property.

## QA interpretation

- **Psat = learning-efficiency gate** for long-lived QA agents (memory/skills that compound vs clutter) — pairs with eval-driven development.
- **Frozen-weights + artifacts** is exactly our harness-memory setup: plasticity measures whether the memory layer earns its keep.
- **Reuse ≠ success** mirrors observed-only-vs-caught: activity in the loop proves nothing without held-out gains.
- **Experience-vs-compute confound** is the honest caveat our own seeded metrics should carry.
- Conclusion thesis ("better at becoming more capable") = post-training target for agent QA: buy learning rate, not just endpoint score.

## See also

- [[anthropic-demystifying-evals-agents-2026]] — eval-driven development, saturation
- [[arbiter-prompt-interference-mason-2026]] — $0.27 cheap checks
- [[durability-curve-seven-checks-kit-2026]] — practitioner gates

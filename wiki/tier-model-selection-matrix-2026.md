# Tier → Model → Threshold: Judge Selection Matrix (2026-09-24)

**Purpose:** which judge model for which risk tier, with measured bars. Operationalizes per-risk-tier gates (B0-B3) for verdict models on PC-224 inventory + cloud APIs. Parent: per-risk-tier framework v0.3 (Positions-CV-CL, Rupesh co-dev); sampling doctrine: rotation-without-relevance (stratified ~20).
**Evidence base:** SemIf site table (0.6B 44/53/41; 2B 69/69/64; 4B 81/77/85; Jev 88.3); Laya README (Banking77 collapse >20 options, soft-acc trail, ECE refit 0.213→0.081); Kev-0.5B (reading 0.75, pattern-match only); Archestra (Jev ~300ms, $0.37/100 calls; Sonnet +5-6pts but all-leak errors); local inventory verified 2026-09-24 (HARDWARE_SPEC.md).

---

## Matrix

| Tier | Risk examples (OrangeHRM map) | Judge model | Agreement bar | Latency / cost envelope | Escalation |
|------|-------------------------------|-------------|---------------|-------------------------|------------|
| **B0** | Auth, payment, security boundaries | 70b-Q4 local (slow OK) or Jev API / frontier judge | Dual-agree or 100% mutation-catch on seeded P0; any disagreement → human | Slow OK (3-5 tok/s), $0 local / $0.042 per 1M API | Always human on split |
| **B1** | PIM/Leave/Time main flows | qwen2.5:14b / coders 7-16b local | Agreement vs API spot-check; catch bar per tier sample | ms-level local, $0 | API re-judge on disagreement |
| **B2** | Edge flows, routine | mini 3b/7b local | Fast verdict + escalate-on-low-confidence | ms-level, $0, batchable | Low confidence → B1 model |
| **B3** | Cosmetic | Cheapest (mini / trend-only) | Trend signal, no gate | Minimal | None (observe) |

## Hard constraints (override tier default)

- **>20 options in one question → maxi/API only.** Small models collapse (Laya Banking77 0.425 vs Jev 0.870).
- **Russian text → qwen family; English reasoning → llama/deepseek.**
- **Calibration:** ECE refit on held-out domain data before trusting probabilities (Laya 0.213→0.081 lesson).
- **No 70b-Q4 batches:** P0 spot cases only (CPU 3-5 tok/s); volume stays on midi/mini.
- **Cache discipline:** volatile logs filtered (Applitools token-asset table); screenshot only at final checks.

## Selection procedure (how a model earns its tier)

1. Candidate runs the tier's judgment sample (same N tasks as W3 Jev-comparison protocol).
2. Measure: agreement vs reference (Jev/frontier) + latency + cost.
3. Cheapest model clearing the tier bar wins the tier. Re-run on task change (choice is measured, not declared).

## See also

- Per-risk-tier framework v0.3 (Positions-CV-CL outreach/active/Rupesh_Kabra) — tiers and gates
- [[rotation-without-relevance-preseed-mutant-filtering-2026]] — stratified sampling ~20 + OrangeHRM tier map
- [[jev-open-source-alternatives-2026]] — candidate judges (SemIf, GLiClass, Laya, OpenJevPro)
- HARDWARE_SPEC.md (repo root) — verified local inventory

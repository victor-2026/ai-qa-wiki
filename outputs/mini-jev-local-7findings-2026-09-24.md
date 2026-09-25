# W5 mini-jev-local arm: 7 FlowScout findings via Ollama CPU (RAW, no interpretation)

**Host:** http://192.168.1.209:11434 (PC-224 LAN) | **Model:** qwen2.5:3b | **Runs:** 3x, temp 0
**Method:** generative judge, fixed one-line prompt (severity=P0|P1|P2|noise + fp=yes|no). NOT System-One logprob readout. No vLLM touched (CPU only, per handoff).
**Task set:** 7 findings from W3 jev-integration-check.md (same set as Jev baseline).
**Date:** 2026-09-24

## Batch stats

- 21 calls, 106.3s total. Run 1/finding 1 = 104.1s (cold model load into memory, one-time).
- Steady-state (warm): ~0.1s/call, order-of-magnitude (observed range 0.08-0.18 across 21 calls; no p95/variance claims).
- Stability: 3/3 identical verdicts on all 7 findings (temp 0 deterministic).
- Cost: $0 (local).

## Raw table (finding × latency × verdict)

| # | Finding (short) | Jev ref (W3) | r1 lat | r1 | r2 lat | r2 | r3 lat | r3 |
|---|-----------------|--------------|--------|----|--------|----|--------|----|
| 1 | Forgot-pw link unverified | noise/FP-T/0.41 | 104.1s* | P1/no | 0.09s | P1/no | 0.09s | P1/no |
| 2 | Login button, safe | noise/FP-T/0.45 | 0.16s | P2/no | 0.09s | P2/no | 0.09s | P2/no |
| 3 | LinkedIn link destructive | P2/FP-T/0.06 | 0.18s | P1/no | 0.08s | P1/no | 0.09s | P1/no |
| 4 | Reset Cancel button | noise/FP-T/0.22 | 0.18s | NOISE/no | 0.09s | NOISE/no | 0.09s | NOISE/no |
| 5 | Nav menu items | noise/FP-T/0.25-0.65 | 0.18s | P1/no | 0.08s | P1/no | 0.08s | P1/no |
| 6 | Logout button | noise/FP-T/0.73 | 0.15s | P1/no | 0.08s | P1/no | 0.08s | P1/no |
| 7 | OrangeHRM Inc link | P2/FP-0.00-0.30 | 0.15s | P2/no | 0.08s | P2/no | 0.08s | P2/no |

*cold load, one-time. r1 lat format: seconds; verdict format: severity/fp.

## Log (persistent, in outputs/)

- Runner: `outputs/mini-jev-local-runner-2026-09-24.py`; raw JSON: `outputs/mini-jev-local-raw-2026-09-24.json` (21 rows verified).
- Parse rate 21/21 (single-line format held, zero UNPARSEABLE).
- Accuracy column intentionally EMPTY (needs Jev reference - W3 computes at merge, do not re-measure this side).

## Limitations (ready line for W3 report)

Latency figures: n=7 findings × 3 runs each (temp 0); order-of-magnitude comparison only. No p95/variance claims; full campaign at n=30 pending for statistical power.

## Handoff state

W5 DONE. Numbers as-is. Merge: W3.

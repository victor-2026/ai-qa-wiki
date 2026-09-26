# A-test: SemIf Browser Lab Offline (B0-01 probe, user hands, 2026-09-25)

**Method:** W2-approved A-procedure (pass/fail + fixed B0-01 probe). Executor: user, in-browser (openjev.com, MiniCPM5 2B, wllama). Recorder: W5, from chat-reported numbers (no automation involved - numbers transcribed verbatim, not measured by script).
**Case:** state "The refund isn't showing up on my account.", question "What is this message about?", options A=Refund_not_showing_up (gold), B=Billing support.

## Runs

| # | Condition | Direct readout | Generation | Timings | Verdict |
|---|-----------|----------------|------------|---------|---------|
| 1 | online, polluted option ("gold = " prefix) | A 0.624 / B 0.376 | 0.6 / 0.4 | 2.906s, 88 tok in | CORRECT (weak margin) |
| 2 | online(?), question-as-option (A=question text) | B picked | - | - | VOID (V1: gold absent) |
| 3 | online after reload, clean labels | A 0.994 / B 0.006 | 0.6 / 0.4 | load 5.854s, warmup 0.589s, run 2.284s / 3.678s | CORRECT, replicated |
| 4 | OFFLINE (airplane + reload) | A 0.994 / B 0.006 | 0.6 / 0.4 | load 6.327s, warmup 0.562s, run 2.336s / 3.633s | CORRECT, identical to online |

## Verdict: PASS

- Page alive from browser cache with network off (load 6.3s).
- B0-01 probe completes with correct verdict, numbers identical to online baseline.
- Hygiene effect measured: polluted label 0.624 → clean label 0.994 (same model, same case).
- Generation path stable 0.6/0.4 across all valid runs (weaker margin than direct readout, consistent).
- Generation token counters display "0 tok" (site display quirk, ignored).

# Durability Curve: Before You Trust Your AI Agent (Floyd Kit, Oct 2026)

**Source:** H. Floyd (Durability Curve, harryfloyd.substack.com), free 9-page field kit from 6 essays (May–Aug) + email 09.10. Raw: `raw/Before-You-Trust-Your-AI-Agent.pdf` (9pp, 16.7K chars, full text read). One-line thesis: **an agent cannot be the thing that confirms its own work.**

## The seven checks (in order of need)

| # | Check | Time | Pass rule |
|---|---|---|---|
| 1 | One agent, or a team? | minutes | fan out only if pieces are independent (no shared writes) + job too big for one context + worth ~4× tokens; default = simpler machine (Anthropic: multi-agent ≈15× tokens vs ≈4× single) |
| 2 | Model or harness? | 1 week | change one harness layer (context/recovery/tools/feedback/measurement) with model fixed; success holds/rises + cost holds/falls. LangChain agent 52.8→66.5% Terminal-Bench 2.0, model untouched |
| 3 | What does nothing check? | afternoon | every irreversible action has a person in front; every other has a watcher the agent can't touch; no empty third column (748 dead containers anecdote: scheduler logs success on any reply) |
| 4 | Can it reach its guardrails? | 30 min | no control trusts anything the agent can write; hooks run on fresh checkout. Real bypasses: hook wording narrowed, Bash(*) self-allowlisted, `core.hooksPath /dev/null` |
| 5 | Grade it twice | 1 hour | shape (right company/direction) vs exact (every figure/date exact when acted on): 91% vs 77% on 22 claims. Re-fetch what decays at write time, via an unskippable step |
| 6 | Filler test | 15 min | swap retrieved docs for filler: must say "cannot answer". Same answer = memory (fail); confident different answer = invention (fail). Tool-call hacking (Ma et al. 2025): citations as decoration |
| 7 | Test it cannot talk past | 20 min | agent never writes both code and test; Stop-hook runs suite, exit 2 blocks the stop. Gotchas: invalid JSON in settings silently disables hooks; 8 consecutive blocks auto-release (tool calls reset count) |

## Scorecard discipline

Run all seven per agent; re-run on every model swap. Each failure → exactly one fix + date.

## QA interpretation

- **Check 7 = our seeded-breaks in practitioner form:** test fails on known-broken code + agent can't edit the gate — examiner-author split as a shell script.
- **Check 4 is the action-boundary doctrine** (Huang): controls the agent can write are worth nothing; fresh-checkout ruleincluded.
- **Check 6 operationalizes grounding:** filler-swap is a cheap, no-LLM test for "citations doing work" — pairs with evidence-pack verification.
- **Check 2 quantifies harness-over-model** (52.8→66.5% fixed model) — the $0.27 Arbiter lesson at product scale.
- **Check 5 splits accuracy in two numbers** (shape vs exact) — honest denominators applied to agent answers; gap = hidden wrongness.
- Known limits: spend caps + secrets explicitly out of scope; check 6 fits retrieval agents, check 7 coding agents.

## See also

- [[arbiter-prompt-interference-mason-2026]] — 95% static prompt checks
- [[aqef-seeded-controls-spec-2026]] — oracle proves itself every run
- [[durability-curve-tests-pass-so-what-2026]] + [[durability-grader-answer-key-2026]] — same author

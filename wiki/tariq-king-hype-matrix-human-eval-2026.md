# Tariq King: Hype Matrix + Human Evaluation (Test IO / EPAM, 2024-2026)

**Source:** Tariq King (CEO Test IO, EPAM; ex-test.ai Chief Scientist; 40-50 scholarly works; Miami). Hype Matrix Pulse Mar 23 2025 (112 reacts, full text read 08.10): https://www.linkedin.com/pulse/red-pill-escaping-agentic-ai-hype-matrix-tariq-king-tpgre. Human-eval article EuroSTAR Apr 2025 + Experience Testing (AgileTD) via search summaries. PNSQC "Humanizing AI" keynote context.

## Hype Matrix (red pill)

- Agents not new: Russell/Norvig 1995; Tariq's own AGENT (AI Generation and Exploration in Test) bots since 2005, open-sourced, Dionny Santiago drove dev; 2019 TestGuild talk.
- Real: NARROW agents (bounded task, sandboxed tools, HITL, guardrails/fallbacks) — support/code-assist/data-analysis/commerce examples.
- Hype (5 failures): grounding (linguistic plans, hallucinated steps), memory/state, action reliability (no self-check), rogue/stuck autonomy, trust/verification open ("How do we know what an agent really did?").
- Triad: Co-Pilot (speed) + Agent (constrained multi-step) + Human (supervise at the wall) — "augmented intelligence, not artificial independence."
- Testing-community rebuke: overnight authorities who never trained a model; failed tool demo anecdote.

## Human evaluation at scale (Test IO practice)

Structured rubrics, crowdsourced communities (internal + external), human+AI judges with confusion-matrix correlation (GPT-4 vs human ground truth), RLHF feedback loop into regression. Position: automation monitors, humans validate alignment/UX/ethics.

## Comments (reception)

Alexander Galavach: stop pitching replacers ("find MORE bugs already — what kind of bugs?"); MORE testers needed for nondeterministic systems, different skillset. Minh Nguyen / Jonathon Wright thread (agentic AI isn't about agents).

## QA interpretation

- Pre-2025 authority for narrow-agents + HITL + verification-open-problems — citable seniority against 2026 hype (PNSQC keynote = same voice, bigger stage).
- Human-eval-at-scale practice (rubrics, confusion matrix, RLHF loop) = industry implementation of our calibration + human-agreement demands.
- Galavach comment = practitioner-side demand forecast for testers of nondeterministic systems (Article 27 angle).

## See also

- [[elastic-shared-eval-framework-chang-2026]] — calibration, judge pairing
- [[breaklight-ai-testing-methodology-whitepaper-2026]] — judge calibration, human agreement
- [[jason-arbon-book-v1-v2-audit-2026]] — held-out validation

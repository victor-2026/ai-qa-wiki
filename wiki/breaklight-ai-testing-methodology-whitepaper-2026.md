# Breaklight AI Testing Methodology (Whitepaper, Sep 2026)

**Source (link-only ref, no raw file — raw/ stays human-only per 30.09 decision):** Breaklight methodology whitepaper, PDF 296 KB, 18 pp. Text extracted and read 2026-10-07.
**URLs:** https://breaklight.ai/docs/breaklight-whitepaper.pdf · https://breaklight.ai/ · https://breaklight.ai/about.html · https://breaklight.ai/insights/
**Company:** Breaklight AI LLC, New York. Duncan Smith (Founder/COO, 25y testing/QA) + Nikolai Grabner (Technical Head of Strategy and Delivery). Consultancy testing AI only: retrieval quality, answer grounding, hallucination, adversarial, eval ops. Watch status: Duncan = Tier 3 (observe, no outreach — commercial-adjacent, W1 owns any contact).

## Core distinction: model vs deployment

"Most AI testing grades the model. We assess the thing you actually deploy." Exhibit pair: dealership chatbot selling a $1 SUV via direct prompt injection (Dec 2023); Air Canada bereavement-fare tribunal ruling (Moffatt v. Air Canada, 2024 BCCRT 149, ~CA$812 — bot contradicted its own cited policy; "chatbot is a separate legal entity" rejected).

## Five questions in order (chain of trust)

Retrieval (right context back?) → Grounding (claims anchored?) → Honesty/Hallucination (traps set per fabrication kind; direct contradiction never averaged away) → Safety/Adversarial (written permission, sealed env) → Eval Ops (repeatable routine, CI wiring). Each question only matters if the previous passed.

## Reference set hygiene (three failure modes guarded)

Borrowed questions (model saw answers in training — must come from your world), leaked answers (expected answer sitting in the prompt = open-book exam you wrote), wrong answer keys (expert mis-remembrance, doc updates).

## Numbers discipline (strongest section)

- **Long tail:** 92% headline can hide 50% failure on rare questions. Slice everything (topic, language, frequency, difficulty); read weakest slice as carefully as the average.
- **Slice floors:** ≥100 questions = scored verdict; 30-100 = directional, no verdict; <30 = raw failures listed qualitatively, no rate.
- **Language parity:** translated pairs compared as pairs; verdicts per language; weaker language carries the decision.
- **Noise floor:** ~400 questions pin a score to ±5 pts; detecting a genuine 5-pt drop run-over-run takes ~570-800 per run; paired designs cut this several-fold.
- **Verdict rule (on the interval, not the point):** PASS only if entire 95% CI clears the bar; FAIL only if entirely below; WARN = straddling ("inside noise: grow the sample, or accept the ambiguity in writing"). 90.7% on n=482 vs 90% bar = WARN, not pass. Two failure modes killed: chasing ghosts (fixing noise) and missing real decay (green dashboard, degrading prod).
- **Judge calibration:** ≥200-item hand-labelled key; report agreement (Cohen's κ target ≥ 0.75); carry judge error into downstream precision; recalibrate on judge/instruction change; judge from a DIFFERENT model family. "A grader that lets hallucinations pass is worse than no grader, because it manufactures false confidence."
- **Adversarial bar:** pass/fail, not percentage. Zero observed exposures; one reproducible leak = finding. Honest bound: zero in n attempts means "true rate ≤ ~3/n at 95% confidence". Serious finding stops the clock, escalates same hour.
- **Pinning:** model version+settings, judge+instructions, reference-set version, corpus snapshot, tooling — every number regenerable months later. Stochastic systems report run-to-run range.

## Framework mapping + verdicts

Findings mapped to OWASP LLM Top 10, MITRE ATLAS, NIST AI RMF 1.0 + GenAI Profile 600-1, ISO/IEC 25059, EU AI Act, ISO 27001/42001. Gaps stated in writing, never hidden behind green ticks. Verdicts: Ready / Ready with conditions / Not ready. Ten buyer questions (checklist §10: what was tested, question provenance, key verification, weakest slice, sample size, change threshold, grader calibration, adversarial attempt, framework mapping, re-runnability).

## QA interpretation

- Closest vendor-independent formulation of our own doctrine found to date: denominator discipline, interval-not-point verdicts, judge calibration with family separation, paired designs, language parity. Direct backup for Articles 26/28/29 and per-risk-tier gate language.
- Their WARN verdict ≈ our abstention/observed-only layer. Their "chasing ghosts vs missing decay" = green-dashboard trap vocabulary.
- Note: consultancy paper (method marketing), not peer-reviewed science. Numbers are illustrative-grade methodology, not client data (stated in-paper). Cite as practitioner doctrine, not empirical results.

## See also

- [Breaklight assurance-gap briefing (Oct 2026, companion doc)](wiki/breaklight-ai-assurance-gap-briefing-2026.md)
- [Ken Huang MAESTRO 3D control model](wiki/kenhuang-maestro-google-control-roadmap-2026.md)
- [Elastic shared eval framework](wiki/elastic-shared-eval-framework-chang-2026.md)
- [Anthropic + Spotify quality at AI speed](wiki/anthropic-spotify-quality-at-ai-speed-2026.md)

- [[kenhuang-maestro-google-control-roadmap-2026]] — metrics-hide-gaps, monitor independence
- [[runtime-authorization-ai-agents-2026]] — permission/governance axis
- [[swe-proof-machine-checked-proofs-2026]] — green suite ≠ correctness
- [[llm-testing-6-approaches]] — judge calibration

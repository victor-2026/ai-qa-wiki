# Elastic Shared Evaluation Framework (Susan Chang, QCon AI / InfoQ, Oct 2026)

**Source:** Susan Chang (Principal Data Scientist, Elastic), "Building Reusable Evaluation Frameworks for Agentic AI Products", QCon AI via InfoQ. Full transcript read 2026-10-07.
**URL:** https://www.infoq.com/presentations/elastic-ai-agent-evaluations/

## Context

Elastic runs multiple production agents on shared infra: attack-discovery (agents pulling attacks from security logs for a petabyte-scale banking customer) and enterprise chatbots over proprietary data. Each team initially built its own datasets, evaluators, trace stores — siloed evaluations.

## Shared framework building blocks

- **Dataset import + standardized schema** (security logs in, Q&A in — one schema).
- **Trace-based evaluators:** token usage, latency, tool calls, performance.
- **Shared RAG evaluators:** precision/recall on alert IDs, semantic similarity, factuality (no hallucinated MITRE tactics; no hallucinated product IDs/ES|QL syntax).
- **Custom evaluators** per use case on top.
- Flow: datasets (input/output) → run agent → code-based + LLM-judge + trace evaluators → results back into Elastic.
- Runner "Scout": customized Playwright, loads datasets, runs TS agents, collects, evaluates; local run with terminal scores for dev UX.

## Python → TypeScript port (match production)

Data-science team started evals in Python while production agents were TypeScript. Merged later with Claude/Cursor + SWE review. Position: start in what you know (even 20-50 records, cf. Eugene Yan — now at Anthropic), merge toward production stack when mismatch matters. Chang is "half and half" on whether she'd skip Python given a redo — the port itself upskilled the team.

## LLM-as-judge: pros/cons from 1-2 years of practice

**Pros:** scales to ambiguous scenarios (tone, brand, coherence, open-ended); chain-of-thought self-grading explains verdicts. **Cons:** not granular (query syntax, JSON/YAML shape, product IDs need programmatic checks); run-to-run variance; **same-family bias — Llama evaluating Llama scores Llama higher** (their finding, confirmed by Meta + CrowdStrike); Anthropic's January blog post independently validated their conclusions.

**Doctrine:** deterministic checks where the answer is exact + judge where it is ambiguous. Always paired, never judge-only.

## What could NOT be abstracted (per-team ownership)

1. **Bespoke data creation** — security analysts/researchers spinning up VMs and Okta test envs; only end users know what the test set should be.
2. **Product input** — positive/negative behaviors, what counts as regression (incl. behavior drift: agent turned aggressive on benign data after an update).
3. **Calibration** — evaluators must agree with human evaluators; uncalibrated judge output = junk. No shared framework can own this.

## Tracing doctrine

Evaluate intermediate steps, not just end results: wrong-database-queried is invisible in the final number. Tools tried: LangSmith (Add to Dataset from thumbs-down feedback), Phoenix, Elastic Observability. Proxy/implicit signals where full capture is restricted. Deterministic harness steps must be traced too (Q&A: failure is often in the deterministic step, not inference).

## Lessons learned

- Build first, consolidate later — but start cross-team communication earlier with consolidation as the goal.
- Feedback mechanisms (even Google Forms / thumbs up-down) beat no signal.
- Ad-hoc evaluation at small scale is fine and justifies further investment; don't overinvest in abstractions at stage one.

## QA interpretation

- Independent industry confirmation of our hybrid doctrine (deterministic + judge) and of judge-bias risks we cite (same-family grading).
- "Calibration cannot be abstracted" = our assessor-side argument: domain expertise + human agreement baseline are non-outsourceable.
- Scout (Playwright as eval runner) rhymes with our Playwright-based mutation/seeding practice.

## See also

- [Anthropic + Spotify quality at AI speed](wiki/anthropic-spotify-quality-at-ai-speed-2026.md)
- [Ken Huang Claude eval hillclimbing note](wiki/kenhuang-claude-eval-hillclimbing-note-2026.md)
- [Breaklight testing methodology whitepaper](wiki/breaklight-ai-testing-methodology-whitepaper-2026.md)
- [Avito agents setup metrics review](wiki/avito-agents-setup-metrics-review-2026.md)
- [Danyil LangSmith vs Langfuse comparison](wiki/danyil-langsmith-langfuse-comparison-2026.md)
- [Tariq King hype matrix + human eval](wiki/tariq-king-hype-matrix-human-eval-2026.md)

- [[llm-testing-6-approaches]] — LLM-as-judge, calibration
- [[kiro-continuous-prompt-evaluation-llm-judges-2026]] — 15-dim eval, behavioral deltas
- [[testmuai-agentic-regression-testing-2026]] — 4-level ladder, recall metric
- [[andrew-ng-coding-agents-skills-map-2026]] — eval-driven development

# Test-time reasoning economics: more thought ≠ more value (2026)

**Source:** arXiv 2609.30705 (Jiayi Chen, Guiling Wang, submitted 2026-09-25) — https://arxiv.org/abs/2609.30705 (abstract only ✅ 2026-09-28). Raw: `raw/arxiv-price-of-thought-reasoning-economics-2026.md`.
**Study:** DeepSeek / GPT / Gemini families; reasoning effort varied, everything else fixed; full-year US equities × 3 input conditions; 800,000+ predictions, repeated generations.

## Findings (abstract-verified, paper not read)

1. **More reasoning ≠ reliably better net outcomes** across all three families (net of costs).
2. **Nonmonotonic scaling** (DeepSeek no-reasoning → max): the curve goes up AND down — no "more is better" prior survives.
3. **Unstable treatment effects under repetition:** repeated generations change decisions and selections "even when overall scores remain similar." Scores stable, decisions not — the exact failure mode our determinism ×2 rule and flip-rate tracking exist for.
4. **Framing line:** "reasoning controls are rarely evaluated as economic interventions" — the evaluation gap stated as economics, not accuracy.
5. **Prescription:** "motivating validation for each task before deployment" — per-task validation, our standing rule, from an independent direction.

## Why this is our cost-of-verification line

- Our measured thinking tax (qwen3:4b 10–460s/call, think-ON required; B0 25.09) + token economics (135:1 agent loop, $0.32/10k evals claim) now have an independent peer: reasoning spend must clear an economic bar per task, not an accuracy bar in the abstract.
- Pairs with LangWatch's flip-rate reporting (2/300 on prompt injection) and our void-class discipline: instability under repetition is a first-class metric, not noise.
- Trading domain is incidental — the claims used here are domain-free (nonmonotonicity, instability, per-task validation). No trading content ingested.

## Cross-links

- `Positions company/pilots/Jev/` — B0 thinking-tax measurements (qwen3:4b); gold-n30 freeze protocol.
- [[llm-testing-6-approaches]] — eval economics; metrics beyond accuracy.
- [[ai-testing-metrics]] — cost-per-verdict, stability metrics.
- Quotes banked: Articles/quotes.md → Market Signals (economic-value line, per-task-validation line).

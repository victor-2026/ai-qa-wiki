# Source: arXiv 2609.30705 — "The Price of Thought: Does Test-Time Reasoning Pay in LLM Trading?"

**URL:** https://arxiv.org/abs/2609.30705 · **Authors:** Jiayi Chen, Guiling Wang
**Submitted:** Sep 25, 2026 (v1). **Fetched:** abstract only, 2026-09-28.

---

While inference-time reasoning promises better decision making, its higher computational cost may not yield better economic outcomes. Yet reasoning controls are rarely evaluated as economic interventions, where changes in model outputs must translate into better portfolios after trading costs.

Controlled study: representative LLMs from DeepSeek, GPT, Gemini families. Reasoning effort varied; information per formation date, prompts, output formats, portfolio construction all fixed. Full year of US equities under three input conditions (numerical, identifiable news, masked news). 800,000+ asset predictions, repeated generations.

Findings:
- Across all three families, additional reasoning does not reliably improve net portfolio returns.
- DeepSeek full progression (no reasoning → maximum): performance NONMONOTONIC.
- Repeated generations produce unstable treatment effects and portfolio selections, even when overall scores remain similar.
- "Additional reasoning can change financial decisions without reliably improving their economic value" → "motivating validation for each task before deployment."

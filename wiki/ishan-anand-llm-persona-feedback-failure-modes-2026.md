---
source: "ishan-anand-llm-persona-feedback-2026.md"
ingested: "2026-09-01"
---

## LLM Persona Feedback - Failure Modes (Ishan Anand)

**Summary**
Talk by Ishan Anand on using LLMs for persona feedback, shared via LinkedIn (https://lnkd.in/gNWQZJHm). Four systematic failure modes when synthetic personas substitute for real users. All modes produce plausible but non-human behavior, and all are hidden unless grounded in real human data.

---

## Four Failure Modes

| Mode | Mechanism | Example | Symptom |
|------|-----------|---------|---------|
| **Context Confounders (Improv Effect)** | Under-grounded prompt forces LLM to infer unstated details | Higher price inferred as luxury/jewelry | Inverted demand curves, bizarre non-human behavior |
| **Stated vs Behavioral Reality** | LLM trained on what people say, not what they do | Attitude surveys vs purchase actions | Predicts survey responses well, real-world actions poorly |
| **Prompt Sensitivity Trap** | Minor wording or choice order tweaks introduce extreme bias | Reordering options changes distribution | Brittle results, high variance on rephrase |
| **Sampling ≠ Significance** | 1,000 synthetic runs measures model distribution, not human population | Repeat sampling tightens model interval only | False confidence, no gain in real statistical power |

---

## Our analysis (for Victor)

1. **Persona feedback is Checking, not Testing (Bach).** Synthetic persona = check against LLM's internal model of "what a person would say." Testing requires human ground truth. Without anchoring, you measure the model's distribution, not the market.

2. **Maps to LLM-as-Judge risks.** Same three traps apply when LLM grades agent output: context confounders (judge invents criteria), stated vs behavioral (judge predicts plausible answer, not correct state), prompt sensitivity (judge flips on reword). Mitigation is identical: grounded evals + deterministic state checks.

3. **Sampling fallacy = false confidence for Article 20.** Running 1,000 synthetic persona simulations does not increase confidence - it only sharpens the model's self-consistency. Validation requires anchoring against real human ground truth, same as mutation matrix requires real defect seeding.

4. **Durability testing is mandatory.** Prompt sensitivity means any persona result must be re-tested across rephrases and option orders. Report the range, not a point estimate. For QA: treat persona feedback as an unmeasured signal until anchored.

---

## Cross-links
- [Prachi/Bach RST](wiki/prachi-dahibhate-james-bach-rst-2026.md) — Testing vs Checking; magic testing box
- [AI QA Evidence Layer](wiki/ai-qa-evidence-layer-validation-evals-guardrails-telemetry.md) — Downstream QA validation vs model evals
- [LLM Testing - Six Approaches](wiki/llm-testing-six-approaches-2026.md) — LLM-as-Judge, Golden Dataset, boundary prompts
- [Article 20 - False Discovery](wiki/your-agent-found-5-bugs-2026.md) — 80% false discovery when verifier shares context

---

*Source: Ishan Anand talk via https://lnkd.in/gNWQZJHm · Ingested 2026-09-01*

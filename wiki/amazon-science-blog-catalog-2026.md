# Amazon Science Blog: Catalog for AI-QA (2026)

**Source:** https://www.amazon.science/blog/ + RSS `https://www.amazon.science/index.rss` (HTTP 200 with plain curl, no UA tricks needed; full-text `content:encoded`, ~25-item window May-Sep 2026, saved `/var/folders/kl/2pdh9p0j585dv40l78p7wkch0000gn/T/opencode/amazon_science.rss` on 2026-09-23)
**Company:** Amazon Science (AWS/AGI) — research blog, ICML papers, benchmarks, verification. Not a vendor pitch channel: peer-reviewed-grade content with numbers.
**Last updated:** 2026-09-24 (TIER 1.5 all ingested; 13 articles + catalog)

---

## Legend

- **Relevance:** HIGH / MEDIUM / SKIP (for AI-QA / verdict layer / evals / mutation matrix)
- **Action:** ✅ ingested / FULL READ (candidate) / SKIP

---

## TIER 1: HIGH RELEVANCE — all ingested

| # | Date | Title | Why |
|---|------|-------|-----|
| 1 | Aug 26, 2026 | [When LLM Judges Agree, Should We Believe Them?](https://www.amazon.science/blog/when-llm-judges-agree-should-we-believe-them) | ✅ ingested → [wiki/amazon-science-when-llm-judges-agree-2026.md](wiki/amazon-science-when-llm-judges-agree-2026.md) — judge dependence (Ising), +9-14% over majority vote; formal backing for verdict-layer vote discounting |
| 2 | Jun 3, 2026 | [Ground Truth Is a Process, Not a Dataset](https://www.amazon.science/blog/ground-truth-is-a-process-not-a-dataset) | ✅ ingested → [wiki/amazon-science-ground-truth-is-a-process-2026.md](wiki/amazon-science-ground-truth-is-a-process-2026.md) — audit-then-score 60.8%→90.9%; golden-dataset doctrine, attestor-as-auditor |
| 3 | Aug 21, 2026 | [SOP-Bench: A New Benchmark for Evaluating AI Agents on Real Business Procedures](https://www.amazon.science/blog/sop-bench-a-new-benchmark-for-evaluating-ai-agents-on-real-business-procedures) | ✅ ingested → [wiki/amazon-science-sop-bench-agents-business-procedures-2026.md](wiki/amazon-science-sop-bench-agents-business-procedures-2026.md) — agent benchmark design |
| 4 | Aug 11, 2026 | [A Decade of Mathematical Certainty (Automated Reasoning Group)](https://www.amazon.science/blog/a-decade-of-mathematical-certainty-reflections-on-the-automated-reasoning-group) | ✅ ingested → [wiki/amazon-science-automated-reasoning-decade-2026.md](wiki/amazon-science-automated-reasoning-decade-2026.md) — SMT verification beyond testing (Zelkova/Tiros/Bedrock Guardrails/Kiro) |
| 5 | Jul 29, 2026 | [A New Benchmark for Evaluating Patient-Facing Health AI Agents](https://www.amazon.science/blog/a-new-benchmark-for-evaluating-patient-facing-health-ai-agents) | ✅ ingested → [wiki/amazon-science-patient-agent-bench-2026.md](wiki/amazon-science-patient-agent-bench-2026.md) — LLM-as-jury, 6 dimensions, contamination-proof design |
| 6 | Jun 8, 2026 | [Real-World Grounding in Agentic AI](https://www.amazon.science/blog/real-world-grounding-in-agentic-ai) | ✅ ingested → [wiki/amazon-science-real-world-grounding-agentic-ai-2026.md](wiki/amazon-science-real-world-grounding-agentic-ai-2026.md) — grounding = evidence for agent verdicts |
| 7 | Jun 8, 2026 | [Bridging Intent and Execution in Agentic Systems](https://www.amazon.science/blog/bridging-intent-and-execution-in-agentic-systems) | ✅ ingested → [wiki/amazon-science-bridging-intent-execution-agentic-systems-2026.md](wiki/amazon-science-bridging-intent-execution-agentic-systems-2026.md) — intent/execution gap, CIGE language |
| 8 | May 4, 2026 | [Building Trust into AI (Responsible-AI Pipeline)](https://www.amazon.science/blog/building-trust-into-ai) | ✅ ingested → [wiki/amazon-science-building-trust-into-ai-2026.md](wiki/amazon-science-building-trust-into-ai-2026.md) — 4-phase RAI pipeline, judge-in-RLHF, red-teaming |

## TIER 1.5: MEDIUM — all ingested 2026-09-24

| Title | Date | Note |
|-------|------|------|
| [Why Don't Machine Learning Research Agents Overfit?](https://www.amazon.science/blog/why-dont-machine-learning-research-agents-overfit) | Sep 10, 2026 | ✅ ingested → [wiki/amazon-science-research-agents-overfit-2026.md](wiki/amazon-science-research-agents-overfit-2026.md) |
| [Developing Provably Correct Rust Code with Verus](https://www.amazon.science/blog/developing-provably-correct-rust-code-with-verus) | Aug 31, 2026 | ✅ ingested → [wiki/amazon-science-verus-provably-correct-rust-2026.md](wiki/amazon-science-verus-provably-correct-rust-2026.md) |
| [Capturing Token IDs During Agentic Interactions for Better RL](https://www.amazon.science/blog/capturing-token-ids-during-agentic-interactions-for-better-reinforcement-learning) | Jul 9, 2026 | ✅ ingested → [wiki/amazon-science-token-ids-agentic-rl-2026.md](wiki/amazon-science-token-ids-agentic-rl-2026.md) |
| [EC2's Formally Verified Isolation Engine](https://www.amazon.science/blog/ec2s-formally-verified-isolation-engine-provides-mathematical-assurance-of-virtual-machine-isolation) | Jun 10, 2026 | ✅ ingested → [wiki/amazon-science-ec2-verified-isolation-engine-2026.md](wiki/amazon-science-ec2-verified-isolation-engine-2026.md) |
| [Diverse Reasoning Traces Teach LLMs to Make Better Decisions](https://www.amazon.science/blog/diverse-reasoning-traces-teach-llms-to-make-better-decisions) | May 26, 2026 | ✅ ingested → [wiki/amazon-science-diverse-reasoning-traces-2026.md](wiki/amazon-science-diverse-reasoning-traces-2026.md) |

## TIER 3: SKIP

- Hardware/chips (Trainium, Graviton5), robotics (touch), networking (flat vs fat), antibodies/biology, carbon tracking, TRISO, research-awards news, competitions.

---

## Why This Blog Matters (для нашей серии)

1. **Judges + ground-truth = eval-фундамент verdict-слоя:** голоса discountить по корреляции (Ising), golden labels держать как версионируемый процесс (audit-then-score), человека ставить аудитором споров (90.9%), а не лейблером с нуля (60.8%).
2. **CIGE-стык:** intent/execution-разрыв и evidence bar - тот же язык, что в CIGE-paper; intent-execution пост - независимое подтверждение модели.
3. **Верификация beyond testing:** ARG decade (SMT-гарантии в Bedrock Guardrails/Kiro) - верхний уровень строгости, к которому verdict-слой может апеллировать как к референсу.

---

## Digest

- Feed: `https://www.amazon.science/index.rss` (plain curl OK, full-text) → добавлен в `digest-config.json` (Articles repo) вручную 2026-09-24 как `amazon-science`, weight 0.9. Ручной fallback: страница https://www.amazon.science/blog/
- Проверка 2026-09-23: HTTP 200, 25 items (15 мая - 21 сент 2026), каждый с title/link/pubDate/description/full content:encoded.

*Источники: [raw/amazon-science-when-llm-judges-agree-2026.md](raw/amazon-science-when-llm-judges-agree-2026.md), [raw/amazon-science-building-trust-into-ai-2026.md](raw/amazon-science-building-trust-into-ai-2026.md), [raw/amazon-science-ground-truth-is-a-process-2026.md](raw/amazon-science-ground-truth-is-a-process-2026.md), [raw/amazon-science-sop-bench-agents-business-procedures-2026.md](raw/amazon-science-sop-bench-agents-business-procedures-2026.md), [raw/amazon-science-automated-reasoning-decade-2026.md](raw/amazon-science-automated-reasoning-decade-2026.md), [raw/amazon-science-patient-agent-bench-2026.md](raw/amazon-science-patient-agent-bench-2026.md), [raw/amazon-science-real-world-grounding-agentic-ai-2026.md](raw/amazon-science-real-world-grounding-agentic-ai-2026.md), [raw/amazon-science-bridging-intent-execution-agentic-systems-2026.md](raw/amazon-science-bridging-intent-execution-agentic-systems-2026.md)*


<!-- backlinks-start -->
### Backlinks
- [Amazon Science Automated Reasoning Decade 2026](wiki/amazon-science-automated-reasoning-decade-2026.md)
- [Amazon Science Ec2 Verified Isolation Engine 2026](wiki/amazon-science-ec2-verified-isolation-engine-2026.md)
- [Amazon Science Patient Agent Bench 2026](wiki/amazon-science-patient-agent-bench-2026.md)
<!-- backlinks-end -->

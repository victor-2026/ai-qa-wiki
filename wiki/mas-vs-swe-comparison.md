# MAS-Pipeline vs SWE-Tester: Comprehensive Comparison

**Last Updated:** 2026-04-18
**Sources:** Gemini analysis, arXiv papers, SWE-Tester framework

---

## Overview

Two fundamentally different approaches to AI testing:
- **MAS-Pipeline** — Multi-Agent System (Generator → Critic → Fixer)
- **SWE-Tester** — Single fine-tuned model (Retrieval → Edit)

| Aspect | MAS-Pipeline | SWE-Tester |
|-------|--------------|------------|
| Architecture | 3-4 agents | 2-step pipeline |
| Fine-tuning | Not required | Required (41K dataset) |
| Quality Control | Agent-based (Critic) | Inference scaffold |
| Memory | ChromaDB / JSON | Not built-in |

---

## Quantitative Benchmarks

| Metric | MAS-Pipeline | SWE-Tester | Notes |
|--------|-------------|------------|----------|
| **Pass@1 / Pass@5** | High (iterations) | Medium | MAS uses multiple attempts |
| **Mutation Score** | **Higher** | Lower | MAS-Critic "burns out" weak assertions |
| **Reproducibility Rate** | Lower | **Higher** | SWE-TESTER optimized for Issue→Test |
| **Token Efficiency** | Lower (multiple agents) | **Higher** | Single model call |
| **Code Coverage (LCOV)** | **~90%+** | ~70-75% | MAS covers more edge cases |

---

## Qualitative Comparison

### MAS-Pipeline: "Engineering Team"

Philosophy: Social structure simulation. Strong in **Design**.

| Pros | Cons |
|-----|------|
| Quality control through conflict | "Groupthink" risk (same model errors) |
| DoD compliance (Critic) | Higher token cost |
| Self-healing loop | More complex orchestration |
| Structured output (Pydantic) | Requires more setup |

**Best for:** New microservices, corporate standards, DoD enforcement

### SWE-Tester: "Specialized Tool"

Philosophy: Fine-tuned model for Issue reproduction. Strong in **Context**.

| Pros | Cons |
|-----|------|
| Trained on real repos | No internal "critic" mechanism |
| Higher efficiency | Limited to reproduction only |
| Simpler setup | Requires 41K training data |
| Better Issue→Test mapping | No self-healing |

**Best for:** Bug reproduction from reports, quick fixes

---

## Trust Cost Formula

$$E = \frac{T_{saved}}{C_{tokens} + C_{review}}$$

Where:
- $T_{saved}$: Human time saved
- $C_{tokens}$: API cost
- $C_{review}$: Human review time

**MAS wins** on minimizing $C_{review}$ — 35-40% fewer "junk" tests.

---

## When to Use What

| Scenario | Recommended |
|----------|-------------|
| New microservice from scratch | **MAS-Pipeline** (better design) |
| Bug report from support | **SWE-Tester** (Issue→Test) |
| Corporate DoD required | **MAS-Pipeline** (Critic) |
| Quick reproduction | **SWE-Tester** |
| Mutation testing priority | **MAS-Pipeline** |

---

## Hybrid Approach (Best of Both)

> In 2026, the best solution is **hybrid**:

1. Use SWE-TESTER weights for **Generator** (bug understanding)
2. Keep **Critic** + **Fixer** as quality overlay
3. Add ChromaDB for memory

This gives: deep bug understanding + hard quality control

---

## Related

- [[wiki/mas-testing-framework]] — Full MAS-Pipeline documentation
- [[wiki/swe-tester-framework]] — SWE-Tester framework
- [[wiki/ai-testing-glossary]] — Metrics (Mutation Score, Pass@K)

---

## Differential Testing: Mutation Testing

Most accurate way to compare: **Mutation Testing**.

### Methodology

1. Take stable code
2. Inject micro-errors (mutants): change `>` to `<`, `true` to `false`, remove function calls
3. Run tests from MAS and SWE-Tester
4. Calculate Mutation Score

**Formula:**
$$MS = \left( \frac{D}{M} \right) \times 100\%$$

Where $D$ = killed mutants (test caught the error), $M$ = total mutants.

---

## Qualitative Parameters

Rate each from 1-10:

| Parameter | MAS-Pipeline | SWE-Tester | Notes |
|-----------|-------------|------------|-------|
| **Readability** | High (Critic enforces style) | Medium ("spaghetti code" possible) |
| **Stability** | High (Docker + self-healing) | Lower (reproduction only) |
| **Generalization** | High (edge cases covered) | Lower (specific to issue) |
| **Maintainability** | High (Fixer adapts) | Low ("expires" quickly) |

---

## Benchmark Plan

1. **Prepare:** Take 10 tasks from backlog (or SWE-bench)
2. **Run MAS:** Through `main.py`. Record: tokens, time, Mutation Score
3. **Run SWE-TESTER:** Same setup
4. **Blind Review:** Ask colleague (or another LLM) to evaluate

**Summary:**
- **SWE-TESTER** = "Sniper" for reproducing existing bugs
- **MAS-Pipeline** = Full "QA Department" with maintainability

For long-term projects, MAS wins on **maintainability**.

## Sources

- Gemini analysis
- arXiv papers
- Applause State of Quality
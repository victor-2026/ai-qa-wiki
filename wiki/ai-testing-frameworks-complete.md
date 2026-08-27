---
title: "AI Testing Frameworks — Complete Technical Reference"
type: article
updated: "2026-08-17"
tags: [qa]
---

# AI Testing Frameworks — Complete Technical Reference

**Last Updated:** 2026-04-20
**Sources:** NotebookLM analysis, arXiv papers, IEEE, Applause 2026

---

## Overview — 4 Approaches

| Approach | What It Is | Mutation Score | Best for |
|----------|------------|-------------|----------|
| **MAS-Pipeline** | Multi-agent system (research-driven): Generator → Critic → Fixer → Executor | ~85% | CI/CD, internal quality |
| **SWE-Tester** | Fine-tuned model for bug reproduction from Issues | ~55% | Bug triage, incident response |
| **Applause** | AI-augmented crowdtesting with real devices | N/A | UX/E2E, real devices |
| **Traditional** | Manual testing + Selenium/TestNG | N/A | Small projects |

---

## 1. MAS-Pipeline (Multi-Agent System)

**Research Sources:**
- [arXiv:2601.02454](https://arxiv.org/abs/2601.02454) — "The Rise of Agentic Testing" (Naqvi et al., Jan 2026)
- [IEEE 11348399](https://ieeexplore.ieee.org/document/11348399/) — "Multi-Agent Systems in Software Testing" (Usman et al., 2025-2026)
- [arXiv:2512.21352](https://arxiv.org/abs/2512.21352) — "Multi-Agent LLM Committees" (Karanam & Kennady, Dec 2025)

### Technical Architecture

**4 Agent Roles:**
| Role | Function |
|------|---------|
| **Generator** | Creates test code |
| **Critic** | Reviews and checks code |
| **Fixer** | Applies corrections |
| **Executor** | Runs tests in CI/CD |

### Why 85% Mutation Score?

- Committee of 2-4 agents > single LLM (91-100% vs 78%)
- Mutual verification reduces invalid tests by 60%
- Coverage increases by 30%

---

## 2. SWE-Tester (Software Engineering Tester)

**Research Source:**
- [arXiv:2501.02647](https://arxiv.org/abs/2501.02647) — "SWE-Tester: Training Open LLMs"

### Two-Step Workflow

```
1. Code Localization (BM25 + embeddings)
   → Find defective code + relevant test files
   
2. Code Editing (fine-tuned LLM)
   → Generate test in Search/Replace format
```

### Training Data

- **41K examples** from real GitHub PRs
- 2600 open-source repositories

### Inference Scaffold

- Generate 32 candidate patches
- Execute in sandbox → filter syntax errors
- Rerank by self-consistency

### SFT vs LoRA

| Method | What | Pros | Cons |
|--------|------|------|------|
| **SFT** | Full fine-tuning | Best performance | Needs GPU |
| **LoRA** | Update 1-2% params | Low resource | Slightly lower |

---

## 3. Applause Framework

**Source:** [Applause State of Digital Quality 2026](https://www.applause.com/state-of-digital-quality-2026/)

- AI-augmented crowdtesting
- Real devices (500+)
- Real users

**Best for:** B2C with millions of users

---

## 4. Traditional Approach

- Manual + Selenium/TestNG
- Full control, slow, expensive
- Best for small teams

---

## Digital Quality Maturity Levels

| Level | Description | Characteristics |
|-------|-------------|-----------------|
| **Emergence** | No formal processes | Reactive, dogfooding |
| **Essentials** | Documentation exists | Checklists, basic regression |
| **Expansion** | Automated, scaled | KPIs, automation |
| **Excellence** | End-to-end quality | Innovations, red teaming |

---

## 5 Risks of MAS-Pipeline

| Risk | Description | Mitigation |
|------|-------------|------------|
| **Groupthink** | Same model = same blind spots | Different models per role |
| **Fixer Loop** | Infinite fix cycle | Max 3 iterations |
| **Test Suite Erosion** | Coverage up, quality down | Track mutation score |
| **RAG Poisoning** | Bad patterns stored as good | Monthly cleanup |
| **Objective Drift** | Pass ≠ quality | Multi-metric DoD |

---

## Key Statistics

- **54.5%** companies deployed AI for testing
- **44.1%** disabled due to quality issues
- MAS-Pipeline: ~85% mutation score
- SWE-Tester: ~55% mutation score

---

## Related Wiki Pages

- [[mas-testing-framework]] — Full MAS documentation
- [[mas-risks]] — 5 risks breakdown
- [[swe-tester-framework]] — SWE-Tester details
- [[three-way-comparison]] — Full comparison
- [[state-of-digital-quality-2026]] — Applause report

---

*This wiki page is updated with NotebookLM insights from arXiv/IEEE research.*










<!-- backlinks-start -->
### Backlinks
- [Iso 14971 Risk Management 2026](wiki/iso-14971-risk-management-2026.md)
- [Loris Bartolini Jean Yves Garcin Banking Rag Adversarial Testing 2026](wiki/loris-bartolini-jean-yves-garcin-banking-rag-adversarial-testing-2026.md)
<!-- backlinks-end -->

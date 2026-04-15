# AI/QA Testing Topics Map

**Last Updated:** 2025-04-15
**Source:** Organized from raw/ materials

---

## Core Knowledge Areas

### 1. Testing AI Systems
- [[wiki/testing-strategies]] — Metamorphic, adversarial, PBT, differential
- [[wiki/quality-characteristics]] — ISO 25010, bias, XAI, ethics, safety
- [[wiki/ai-testing-metrics]] — Ragas, TrickCatcher, ROI metrics

### 🎓 ISTQB AI Testing (CT-AI)
- [[wiki/istqb/index]] — Full syllabus with 8 sections
  - Introduction to AI
  - Quality Characteristics for AI
  - Machine Learning Overview
  - Testing AI-Based Systems
  - Testing AI-Specific Quality
  - Methods & Techniques
  - Testing Environments
  - Using AI for Testing

### 2. Agentic Engineering
- [[wiki/agentic-patterns]] — Prompt chaining, routing, parallelization, memory
- Pipeline Triad Pattern — Creator-Critic-Arbiter workflow

### 3. Vibe Coding
- [[wiki/vibe-coding-guide]] — Vibe vs spec-driven, when to use each
- Hidden costs — Security, CI/CD, monitoring gaps
- [[wiki/monitoring-observability]] — What vibe-coded apps need

### 4. AI-Assisted QA
- Test generation — 70% coverage in seconds
- Test prioritization — Run only relevant tests
- Self-healing — Auto-fix broken locators
- Flakiness detection — Quarantine unstable tests

### 5. Quality for AI Systems
- [[wiki/quality-characteristics]] — Bias, XAI, ethics, safety, evolution
- Concept drift — Model degrades over time
- Side effects & reward hacking — Unintended consequences

---

## Key Research Findings

| Topic | Finding |
|-------|---------|
| **WebTestBench** | AI agents for web testing: 26% F1 max |
| **TrickCatcher** | Bug detection in plausible code: 41-51% F1 |
| **PBT for LLM** | Property-based testing: +23-37% improvement |
| **Meta test selection** | 60% fewer test runs with ML |
| **Self-healing** | 70% maintenance time reduction |
| **ROI in AI QA** | 54% faster testing, 40-60% less maintenance |

---

## Testing Strategies Quick Reference

```
No test oracle?          → Metamorphic testing
Need edge cases?         → Adversarial testing  
Known invariants?         → Property-based testing
Multiple implementations?  → Differential testing
Production rollout?       → Canary deployment
AI-generated code?       → TrickCatcher
```

---

## When to Use AI in QA

| Use AI For | Don't Use AI For |
|------------|------------------|
| Test prioritization | Exploratory testing (human intuition) |
| Flakiness detection | Usability checks |
| Script maintenance | Compliance (needs audit trail) |
| Synthetic data | Complex reasoning tasks |
| Regression patterns | Novel/unpredictable scenarios |

---

## Implementation Roadmap

1. **Assess maturity** — Map current QA landscape
2. **Find high-value use cases** — Where waste is greatest
3. **Pilot with clear KPIs** — Start small, measure impact
4. **Involve QA engineers early** — Build trust
5. **Scale based on ROI** — Document lessons learned

---

## Sources Overview

| Category | Files | Key Sources |
|----------|-------|-------------|
| **Agents/Patterns** | 9 | BeyondQuality Agents Playbook |
| **ISTQB AI Testing** | 5 | AT*SQА Syllabus |
| **Qase Blog** | 7 | Ad-hoc, feature flags, testing fundamentals |
| **DeviQA Blog** | 4 | AI implementation, ROI, regression |
| **Research Papers** | 3 | WebTestBench, TrickCatcher, PBT for LLM |
| **Observability** | 3 | Honeycomb, Splunk, Diffian |
| **Vibe Coding** | 4 | Comprehension debt, spec-driven, hidden costs |
| **Other** | 4 | Canary, chaos testing, prompt engineering |

**Total raw sources:** 39 files

---

## Tags

#ai-testing #llm #rag #qa #evaluation #agentic #vibe-coding #observability #metrics #quality

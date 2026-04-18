# AI/QA Testing Topics Map

**Last Updated:** 2025-04-15
**Source:** Organized from raw/ materials (40 sources)

---

## Core Knowledge Areas

### 1. Testing AI Systems
- [[wiki/testing-strategies]] — Metamorphic, adversarial, PBT, differential
- [[wiki/quality-characteristics]] — ISO 25010, bias, XAI, ethics, safety
- [[wiki/ai-testing-metrics]] — Ragas, TrickCatcher, ROI metrics

### 2. Prompt Engineering & AI-Assisted QA
- **[[raw/winteringham-prompts]]** — Prompts from Mark Winteringham's book
- **[[raw/software-testing-with-generative-ai]]** — Book: Software Testing with GenAI
- [[wiki/agentic-patterns]] — Prompt chaining, routing, agents
- Test generation — 70% coverage in seconds
- Test prioritization — Run only relevant tests
- Self-healing — Auto-fix broken locators
- Flakiness detection — Quarantine unstable tests

### 3. Agentic Engineering
- [[wiki/agentic-patterns]] — Prompt chaining, routing, parallelization, memory
- Pipeline Triad Pattern — Creator-Critic-Arbiter workflow
- [[raw/pipeline-triad-pattern]] — Full pattern description

### 4. Vibe Coding
- [[wiki/vibe-wipe-coding-guide]] — Vibe vs spec-driven, when to use each
- Hidden costs — Security, CI/CD, monitoring gaps
- [[wiki/monitoring-observability]] — What vibe-coded apps need

### 5. Quality for AI Systems
- [[wiki/quality-characteristics]] — Bias, XAI, ethics, safety, evolution
- Concept drift — Model degrades over time
- Side effects & reward hacking — Unintended consequences

### 6. ML & Data
- [[wiki/istqb-certifications/ct-ai/ml-performance-metrics]] — Metrics framework (3 levels)
- [[wiki/istqb-certifications/ct-ai/testing-ai-specific-qc]] — AI-Specific QC

### 7. Observability & Monitoring
- [[wiki/monitoring-observability]] — ODD, 3 layers, implementation
- Production monitoring for AI systems

---

## 🎓 Certifications

### CT-AI: Testing AI (2021)
- [[wiki/istqb-certifications/ct-ai/]] — 11 chapters, 55% coverage
- Focus: Testing ML models "under the hood"

### CT-GenAI: Testing with GenAI (2025)
- [[wiki/istqb-certifications/ct-genai/]] — 5 modules, 55% coverage
- Focus: Using LLM as testing tool

---

## Key Research Findings

| Topic | Finding | Source |
|-------|---------|--------|
| **WebTestBench** | AI agents for web testing: 26% F1 max | [[raw/webtestbench-ai-web-testing]] |
| **TrickCatcher** | Bug detection in plausible code: 41-51% F1 | [[raw/trickcatcher-bug-detection]] |
| **PBT for LLM** | Property-based testing: +23-37% improvement | [[raw/pbt-llm-code-generation]] |
| **Meta test selection** | 60% fewer test runs with ML | DeviQA |
| **Self-healing** | 70% maintenance time reduction | DeviQA |
| **ROI in AI QA** | 54% faster testing, 40-60% less maintenance | DeviQA |

---

## Testing Strategies Quick Reference

```
No test oracle?          → Metamorphic testing
Need edge cases?         → Adversarial testing  
Known invariants?         → Property-based testing
Multiple implementations? → Differential testing
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
| Prompt engineering | Security-critical decisions |

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
| **Agents Playbook** | 9 | BeyondQuality |
| **ISTQB CT-AI** | 8 | AT*SQА + additional |
| **ISTQB CT-GenAI** | 1+ | Winteringham book |
| **Winteringham** | 1 PDF + 2 | Book + prompts |
| **Qase Blog** | 7 | Ad-hoc, feature flags |
| **DeviQA Blog** | 3 | AI implementation, ROI |
| **Research Papers** | 3 | WebTestBench, TrickCatcher, PBT |
| **Observability** | 3 | Honeycomb, Splunk, Diffian |
| **Vibe Coding** | 4 | Comprehension debt, spec-driven |
| **Other** | 5 | Canary, chaos, fundamentals |

**Total raw sources:** 40 files

---

## Book: Software Testing with Generative AI

**Author:** Mark Winteringham (Manning, 2025)
**[[raw/software-testing-with-generative-ai.pdf]]** — Full book (306 pages)
**[[raw/winteringham-prompts]]** — Prompt library from the book

### Key Chapters
1. Enhancing testing with LLMs
2. Prompt engineering principles
3. AI, automation, and testing
4. AI-assisted testing for developers (TDD, code analysis)
5. Test planning with AI
6. Rapid data creation
7. UI automation with AI
8. Exploratory testing with AI
9. AI agents as testing assistants
10. Customized LLMs
11. RAG for testing
12. Fine-tuning

---

## Tags

#ai-testing #llm #rag #qa #evaluation #agentic #vibe-coding #observability #metrics #quality #prompt-engineering #ct-ai #ct-genai #winteringham

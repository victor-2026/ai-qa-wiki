# Podcast Outline: AI Testing — From Hype to Practice

**Topic:** The State of AI Testing in 2026
**Duration:** 25-30 minutes
**Sources:** 40 articles from ai-qa-wiki

---

## Intro (2 min)

- What is AI Testing? Not just "using AI to test" but "testing AI systems"
- Why it matters now: 4500+ services, AI everywhere
- Today's journey: myths, realities, and practical approaches

---

## Section 1: The Oracle Problem (5 min)

**Problem:** Traditional testing = "pass/fail". AI doesn't have clear oracles.

**From sources:**
- [[raw/infinite-midwit]] — Objective vs Subjective intelligence
- [[raw/rag-evaluation-ragas]] — LLM-as-judge evaluation
- [[raw/trickcatcher-bug-detection]] — 41-51% F1 for bug detection

**Key insight:** You can't test AI the same way you test traditional software.

**Quote:** "The universe is not governed by Catan rules" — can't trade 4 objective points for 1 subjective point.

---

## Section 2: The Numbers That Matter (5 min)

**What actually works:**

| Approach | Result | Source |
|----------|--------|--------|
| AI agents for web testing | 26% F1 | WebTestBench |
| Human checklist + AI | 49% F1 | WebTestBench |
| PBT for LLM code | +23-37% improvement | Property-Generated Solver |
| Self-healing tests | 70% maintenance reduction | DeviQA |
| Meta test selection | 60% fewer runs | Meta |

**Key insight:** Human + AI > AI alone

---

## Section 3: The Three Levels of AI Testing (6 min)

### Level 1: Testing AI Systems
- Model performance (Precision, Recall, F1)
- Data quality, concept drift
- [[wiki/istqb-certifications/ct-ai/]] — CT-AI certification

### Level 2: Testing WITH AI Systems
- Prompt engineering
- AI-assisted test generation
- [[wiki/istqb-certifications/ct-genai/]] — CT-GenAI certification
- [[raw/winteringham-prompts]] — Winteringham's prompt library

### Level 3: Testing in Production
- Canary deployments
- Shadow testing
- Observability-driven development
- [[wiki/monitoring-observability]]

---

## Section 4: The Hidden Costs (4 min)

**From [[raw/hidden-costs-vibe-coded-apps]]:**

| What's Built | What's Missing |
|--------------|----------------|
| UI, features | Security hardening |
| Happy path | CI/CD |
| Demo-ready | Monitoring |

**From [[raw/comprehension-debt]]:**

AI writes code team doesn't understand → comprehension debt

Symptoms:
- Verbose PR descriptions
- Context rot
- Weak ownership

---

## Section 5: Practical Takeaways (5 min)

### For Teams Starting Out
1. Start with vibe coding → prototype fast
2. Migrate to spec-driven → production ready
3. Always add monitoring before shipping

### For Teams Scaling
1. Separate AI QC as distinct stream
2. Standardize prompt ops & model versioning
3. Build feedback loops (production → training data)

### For Certification Seekers
- **CT-AI (2021)** — Testing AI models "under the hood"
- **CT-GenAI (2025)** — Using LLM as testing tool

---

## Outro (2 min)

**Key message:** AI testing is not a revolution, it's a refinement.

AI should:
- Support QA, not complicate it
- Amplify what works
- Remove friction

**Resources:**
- ai-qa-wiki: github.com/victor-2026/ai-qa-wiki
- Winteringham's book: Software Testing with Generative AI
- ISTQB CT-AI / CT-GenAI certifications

---

## Timestamps

```
00:00 - Intro
02:00 - The Oracle Problem
07:00 - The Numbers
12:00 - Three Levels of AI Testing
18:00 - Hidden Costs
22:00 - Practical Takeaways
27:00 - Outro
```

---

## Related

- [[wiki/topics-map]] — Full wiki overview
- [[outputs/summaries/prompt-engineering-summary]] — Prompt engineering summary

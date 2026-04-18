# AI Testing Strategies

**Last Updated:** 2025-04-15
**Sources:** raw/istqb-*, raw/webtestbench, raw/trickcatcher, raw/pbt-llm-code-generation

---

## Overview

AI testing requires fundamentally different approaches than traditional software testing due to:
- Non-determinism (same input → different outputs)
- Dynamic specifications (models evolve with training data)
- Concept drift (model degrades when data distribution shifts)

## Testing Strategies by AI Type

| AI Type | Strategy |
|---------|----------|
| **Deterministic** | Traditional test case design |
| **Probabilistic/Non-deterministic** | Metamorphic, exploratory, adversarial testing |
| **RAG-based** | Retrieval accuracy + LLM-as-judge |
| **Agentic** | Multi-agent pipeline testing |

## Key Testing Approaches

### 1. Metamorphic Testing
Identify relationships between inputs/outputs. Generate new tests from transformations.

**Example:** If altitude increases → temperature should decrease (in weather model)

**Use when:** No oracle to verify single outputs, but relationships are known.

### 2. Adversarial Testing
Inputs designed to mislead or expose vulnerabilities.

**Applications:**
- Prompt injection
- Jailbreak attempts
- Bias amplification
- Edge case discovery

### 3. Property-Based Testing (PBT)
Test properties/invariants that must hold for ANY input.

**vs Traditional:** Instead of specific test cases, define rules:
- "Output is always non-negative"
- "Response time < 500ms"
- "All fields are populated"

**Tool:** Property-Generated Solver (+23-37% improvement over TDD)

### 4. Differential Testing
Compare outputs of multiple implementations or variants.

**TrickCatcher approach:**
1. Generate PUT variants
2. Create input generators
3. Trust minority outputs (not majority voting)

**Results:** 41-51% F1 for bug detection in plausible programs.

### 5. Canary Testing
Roll out AI features to small subset before full deployment.

```
Steps:
1. Select 1-5% users
2. Monitor error rates, latency, quality
3. If issues → rollback
4. If success → gradual rollout
```

## Test Levels for AI Systems (ISTQB)

1. **Input Data Testing** — verify data quality, detect biases
2. **ML Model Testing** — accuracy, precision, recall, F1
3. **Component Testing** — pre-processing, inference
4. **System Testing** — end-to-end functional/non-functional
5. **Acceptance Testing** — business objectives

## AI Web Testing (WebTestBench)

| Model | F1 Score |
|-------|----------|
| GPT-5.1 | 26.4% |
| Claude Sonnet 4.5 | 21.9% |
| Claude Opus 4.5 | 20.2% |

**Oracle (human checklist):** 49.2% F1

**Key finding:** Human checklist + AI execution > fully autonomous AI

## Decision Matrix

| Situation | Recommended Strategy |
|-----------|---------------------|
| No test oracle | Metamorphic testing |
| Need edge cases | Adversarial testing |
| Known invariants | Property-based testing |
| Multiple implementations | Differential testing |
| Production rollout | Canary deployment |
| AI-generated code | TrickCatcher |

## Anti-Patterns

1. **Testing without baseline** — no metrics to compare against
2. **Ignoring concept drift** — not monitoring data distribution
3. **One-shot evaluation** — not testing over time
4. **Human-only judgment** — not using automated metrics
5. **Trusting deterministic outputs** — expecting same results

## Related

- [[wiki/quality-characteristics]] — AI-specific quality attributes
- [[wiki/ai-testing-metrics]] — How to measure AI quality
- [[wiki/agentic-patterns]] — Agentic engineering patterns
- [[wiki/vibe-wipe-coding-guide]] — Vibe coding approaches

## Sources

- raw/istqb-ai-testing-overview.md
- raw/webtestbench-ai-web-testing.md
- raw/trickcatcher-bug-detection.md
- raw/pbt-llm-code-generation.md
- raw/canary-testing-guide.md

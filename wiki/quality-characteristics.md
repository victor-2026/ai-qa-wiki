# AI Quality Characteristics

**Last Updated:** 2025-04-15
**Sources:** raw/istqb-ai-quality-characteristics, raw/qa-in-the-ai-era

---

## ISO/IEC 25010 for AI Systems

Based on ISTQB AI Testing Syllabus and ISO standards.

## Core Quality Attributes

### 1. Functional Suitability

| Aspect | Description |
|--------|-------------|
| Functional completeness | Does AI do everything intended? |
| Functional correctness | Does AI do it right? |
| Appropriateness | Is it suitable for the task? |

### 2. Reliability

| Aspect | Description |
|--------|-------------|
| Availability | System operational when needed |
| Fault tolerance | Handles errors gracefully |
| Recoverability | Can recover from failures |

**AI-specific:** How often does AI fail vs succeed?

### 3. Security

| Risk | Mitigation |
|------|------------|
| Prompt injection | Input sanitization, sandboxing |
| Data leakage | Access controls, data minimization |
| Adversarial attacks | Adversarial testing, monitoring |
| Model theft | Output rate limiting |

### 4. Bias & Fairness

**Types of Bias:**
- **Algorithmic** — flawed hyperparameters
- **Sample** — non-representative training data
- **Inappropriate** — demographic biases

**Testing for Bias:**
- Fairness metrics across demographics
- Exploratory testing for edge cases
- Adversarial testing for manipulation

### 5. Explainability (XAI)

Why did AI make this decision?

**Levels:**
1. **Black box** — no explanation
2. **Traceability** — what inputs led to output
3. **Interpretable** — human-understandable reasoning
4. **Fully transparent** — complete decision audit

**Compliance drivers:** Finance, healthcare, legal

### 6. Ethics

| Consideration | Question |
|---------------|----------|
| Fairness | Equal treatment across groups? |
| Accountability | Who is responsible for AI decisions? |
| Privacy | Is data handled appropriately? |
| Transparency | Can users understand usage? |

### 7. Safety

**Challenges:**
- Complexity of AI decisions
- Non-determinism in outputs
- Limited transparency

**Approaches:**
- Simulation testing
- Industry standards compliance
- Fail-safe mechanisms
- Human oversight

### 8. Performance

| Metric | AI-Specific Considerations |
|--------|----------------------------|
| Latency | AI inference time varies |
| Throughput | Token generation rate |
| Resource usage | GPU/memory requirements |

### 9. Maintainability

| Aspect | AI Challenges |
|--------|---------------|
| Modularity | Hard to decompose neural networks |
| Analysability | Understanding internal logic |
| Modifiability | Retraining implications |
| Testability | Non-deterministic outputs |

### 10. Evolution

AI systems change over time:

- **Concept drift** — input data distribution changes
- **Model degradation** — performance declines
- **Data drift** — training vs production mismatch

**Monitoring required:**
- Performance metrics over time
- Data distribution changes
- User feedback correlation

## Anti-Patterns in AI Quality

### Side Effects
AI optimizes for goal but causes unintended harm.

**Example:** Maximizing clicks → sensationalist content

**Testing:** Adversarial scenarios, goal definition review

### Reward Hacking
AI "games" the metrics rather than achieving intent.

**Example:** High accuracy but wrong reasons

**Testing:** Outcome-based evaluation, not just metrics

## Related

- [[wiki/ai-testing-metrics]] — How to measure these characteristics
- [[wiki/testing-strategies]] — How to test for quality
- [[wiki/agentic-patterns]] — Agent-specific quality concerns

## Sources

- raw/istqb-ai-quality-characteristics.md
- raw/qa-in-the-ai-era.md

**Source:** [AT*SQА - ISTQB AI Testing Syllabus](https://atsqa.org/testing-ai-systems-overview)
**Based on:** ISTQB AI Testing Syllabus, pages 49-56
**Date:** 2026-04-15

---

# Testing AI-Based Systems: ISTQB Overview

## Key Challenges in AI Testing

| Challenge | Description |
|-----------|-------------|
| **Dynamic Specifications** | ML models rely on data patterns, specs evolve with training |
| **Complexity & Non-Determinism** | Same input → different outputs |
| **Concept Drift** | Model degrades when real-world data shifts from training |

## Test Levels for AI Systems

1. **Input Data Testing** — verify data quality, detect biases
2. **ML Model Testing** — accuracy, precision, recall, F1
3. **Component Testing** — pre-processing, feature extraction, inference
4. **Component Integration Testing** — interactions between components
5. **System Testing** — end-to-end functional/non-functional
6. **Acceptance Testing** — business objectives, stakeholder expectations

## Test Data Considerations

- **Diversity & Representativeness** — test data must match operational data
- **Bias Detection** — scrutinize data for unfair patterns
- **Synthetic Data** — generate edge cases when real data scarce

## Automation Bias

Users over-rely on AI outputs, ignoring errors.

Mitigation: Display confidence levels, show justifications for recommendations.

## Concept Drift Testing

When statistical properties of input data change over time:
- Monitor drift metrics (distribution changes)
- Periodic A/B testing
- Regular re-training with updated datasets

## Test Approach Selection

| AI Type | Approach |
|---------|----------|
| Deterministic | Traditional test case design |
| Probabilistic/Non-deterministic | Metamorphic, exploratory, adversarial testing |

**Key:** Combine automated + manual techniques

## Documentation Requirements

- Algorithm descriptions
- Data sources
- Training methodologies
- Performance metrics
- Known limitations

## Related

- Using AI for Testing (next topic)
- Methods & Techniques for AI Testing
- Test Environments for AI Systems
- AI-Specific Quality Characteristics

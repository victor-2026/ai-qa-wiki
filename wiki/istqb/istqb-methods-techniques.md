**Source:** [AT*SQА - ISTQB AI Testing Syllabus](https://atsqa.org/methods-and-techniques-for-testing-ai-based-systems)
**Based on:** ISTQB Certified Tester AI Testing (CT-AI) Syllabus v1.0, pages 65-72
**Date:** 2026-04-15

---

# Methods and Techniques for Testing AI-Based Systems: ISTQB

## Testing Techniques

### 1. Adversarial Testing
- Identify vulnerabilities with inputs designed to mislead
- Test with noisy/deliberately flawed data
- Applications: image recognition, fraud detection

### 2. Pairwise Testing
- Cover all combinations of input parameter pairs
- Efficient for high number of configurable inputs
- Example: recommendation engine testing

### 3. Back-to-Back Testing
- Compare outputs of two functionally equivalent systems
- Use cases: legacy migration, model validation

### 4. A/B Testing
- Deploy two versions simultaneously
- Collect feedback, statistical analysis
- Use cases: UI optimization, model accuracy comparison

### 5. Metamorphic Testing (MT)
- Identify relationships between inputs/outputs
- Generate new test cases from transformations
- Addresses non-deterministic systems
- Example: weather prediction — altitude ↑ → temperature ↓

### 6. Experience-Based Testing
- Leverage tester expertise
- Exploratory testing, EDA
- Detect unanticipated behaviors, edge cases

## Technique Selection

| Factor | Technique |
|--------|----------|
| High complexity | Experience-based, metamorphic |
| Data sensitivity | Adversarial testing |
| Non-determinism | Metamorphic testing |

**Key:** Combine multiple techniques, update regularly

## Related

- Testing AI Systems Overview
- AI-Specific Quality Characteristics
- Test Environments for AI Systems
- Using AI for Testing

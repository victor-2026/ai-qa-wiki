---
source: "quantum-mt-2025.md"
ingested: "2026-10-01"
title: "Quantum Mutation Testing: Empirical Analysis and Noise-Aware Detection"
type: article
tags: [mutation-testing, quantum, noise, empirical]
---

## Summary

Empirical analysis of quantum circuit mutants and noise-aware mutation analysis. Studies 41 quantum programs on noiseless and noisy simulators (3 IBM devices). Noise significantly alters behavioral distance, making equivalent mutants harder to distinguish from real faults.

## Key Findings

| Metric | Value |
|--------|-------|
| Quantum programs | 41 (6 algorithms) |
| Density-matrix misclassification | Up to 16.77% |
| Output-distribution accuracy | 73.03% |
| Output-distribution F1 | 74.89% |

## Method

1. Execute on noiseless and noisy simulators (3 IBM devices)
2. Compare distance metrics: density-matrix, output-distribution
3. Evaluate threshold strategies
4. Analyze circuit-, algorithm-, mutation-related characteristics

## Key Insights

- Quantum mutation testing requires noise-aware approaches
- Noiseless assumptions insufficient for real quantum hardware
- Output-distribution metrics are practical but imperfect
- Noise effects correlate with algorithm/circuit characteristics, not mutation types
- First empirical study on noise impact on quantum mutation analysis

## See also

- [[mutation-testing-vs-code-coverage-autonoma]] - General concepts
- [[witness-predictive-mutation-testing-2026]] - Predictive MT
- [[sting-swebench-mutation-diagnosis-2026]] - Mutation-guided diagnosis

---
*Source: [raw/quantum-mutation-testing-2025.md](../raw/quantum-mutation-testing-2025.md) · EMSE 2025*

---
source: "witness-predictive-mt-2026.md"
ingested: "2026-10-01"
title: "WITNESS: Lightweight Predictive Mutation Testing"
type: article
tags: [mutation-testing, predictive, machine-learning, cost-reduction]
---

## Summary

WITNESS uses classical machine learning to predict the kill matrix (which tests kill which mutants) without GPU-based training. 65-1722x faster than deep learning approaches while maintaining effectiveness. Enables predictive MT in resource-constrained environments.

## Key Results

| Metric | Value |
|--------|-------|
| Speedup vs Seshat | 65.92x |
| Speedup vs MutationBERT | 1722.81x |
| Speedup vs SODA | 986.17x |
| Approach | Classical ML (no GPU) |

## Method

1. Extract features from source and test code
2. Train classical ML model to predict kill matrix
3. Use predictions for test case prioritization
4. Validate on real-world projects

## Key Insights

- Deep learning unnecessary for predictive MT
- Classical ML achieves similar or better effectiveness
- MutationBERT prediction time exceeded actual mutation testing time
- Lightweight approaches enable CI/CD integration
- Opens predictive MT to resource-constrained environments

## See also

- [[mutation-testing-vs-code-coverage-autonoma]] - General concepts
- [[sting-swebench-mutation-diagnosis-2026]] - Mutation-guided diagnosis
- [[quantum-mutation-testing-2025]] - Quantum MT
- [[meta-ach-mutation-guided-llm-2025]] - Meta ACH

---
*Source: [raw/witness-predictive-mutation-testing-2026.md](../raw/witness-predictive-mutation-testing-2026.md) · 2025*

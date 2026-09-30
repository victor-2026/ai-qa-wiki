# Quantum Mutation Testing: Empirical Analysis and Robust Mutation Analysis Under Noise

**Source:** https://link.springer.com/article/10.1007/s10664-025-10643-z
**Authors:** Eñaut Mendiluze Usandizaga, Shaukat Ali, Tao Yue, Paolo Arcaini, Mohammad Reza Mousavi
**Published:** Empirical Software Engineering, Vol. 30, April 2025
**DOI:** 10.1007/s10664-025-10643-z

## Summary

Empirical analysis of quantum circuit mutants and noise-aware mutation analysis for quantum programs. Studies how quantum hardware noise affects mutant detection using 41 quantum programs executed on noiseless and noisy simulators emulating three IBM devices.

## Key Findings

- **41 quantum programs** implementing 6 algorithms
- **Noise impact:** Significantly alters behavioral distance between programs and mutants
- **Equivalent mutants:** Harder to distinguish from real faults under noise
- **Density-matrix metrics:** Best discrimination (misclassification up to 16.77%), but not accessible on real hardware
- **Output-distribution metrics:** Up to 73.03% accuracy, 74.89% F1-score (practical alternative)
- **Noise-specific thresholds:** Further improve detection compared to noiseless thresholds
- **Noise effects:** Correlate more with algorithm and circuit characteristics than with mutation types

## Method

1. Execute quantum programs on noiseless and noisy simulators (3 IBM devices)
2. Compare distance metrics: density-matrix, output-distribution, others
3. Evaluate threshold strategies for mutant detection
4. Analyze impact of circuit-, algorithm-, and mutation-related characteristics

## Implications

- Quantum mutation testing requires noise-aware approaches
- Existing noiseless assumptions are insufficient for real quantum hardware
- Need device-specific noise profiles for accurate mutant detection
- Output-distribution metrics are practical but imperfect
- First empirical study on noise impact on quantum mutation analysis

## Related

- Quantum computing testing
- Mutation analysis under real-world conditions
- Noise-aware testing methodologies
- QuanForge (FSE 2026) - QNN mutation testing
- QMutPy - quantum mutation testing tool

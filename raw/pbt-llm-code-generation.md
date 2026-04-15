**Source:** [arXiv:2506.18315](https://arxiv.org/abs/2506.18315)
**Date:** 2025-06-23
**Authors:** Lehan He, Zeren Chen, Zhe Zhang, Jing Shao, Xiang Gao, Lu Sheng
**GitHub:** https://github.com/HeLeHanPrivate/PBTwithCodeGen

---

# Property-Generated Solver: PBT for LLM Code Generation

## Problem

LLMs generate code, but ensuring correctness is hard. Traditional TDD with LLMs fails because:
- Tests share biases with generated code
- "Cycle of self-deception" — tests validate flawed assumptions

## Solution: Property-Generated Solver (PGS)

Two collaborative LLM agents:
1. **Generator** — code generation + iterative refinement
2. **Tester** — manages PBT lifecycle, formulates feedback from property violations

Key insight: Instead of validating specific I/O pairs, PBT validates **high-level properties/invariants** that code must satisfy for ANY input.

## Results

**23.1%–37.3% relative improvement** over established TDD methods on code generation benchmarks.

## Why PBT Works

- Properties easier to define than exhaustive test oracles
- Breaks "cycle of self-deception"
- Provides abstract, generalizable feedback

## Key Terms

- **PBT (Property-Based Testing)** — testing framework that validates properties/invariants, not specific inputs
- **Cycle of self-deception** — when tests share flaws with the code they're meant to validate
- **Property** — high-level rule the code must satisfy (e.g., "output is always non-negative")

## Related

- WebTestBench (AI agents for web testing — 26% F1 max)
- Comprehension debt (LLMs write code team doesn't understand)

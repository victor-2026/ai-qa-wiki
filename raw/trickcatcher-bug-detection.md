**Source:** [arXiv:2404.10304](https://arxiv.org/abs/2404.10304)
**Date:** 2024-04-15
**Authors:** Kaibo Liu, Zhenpeng Chen, Yiyang Liu, Jie M. Zhang, Mark Harman et al. (Peking University, NTU, King's College London, UCL)
**GitHub:** https://github.com/RinCloud/TrickCatcher

---

# TrickCatcher: LLM-Powered Bug Detection in Plausible Programs

## Problem

**Plausible programs** — pass existing tests but still contain tricky bugs (logical corner cases).

Examples:
- Program passes test suite but has subtle logical error
- 3,440 such bugs found in Online Judge platforms (human-written code)

## Solution: TrickCatcher

Three stages:
1. **Program Variant Generation** — LLM generates variants based on PUT + spec
2. **Test Input Generation** — LLM creates input generator script
3. **Differential Testing** — compare PUT outputs vs variant outputs

## Key Innovations

### 1. PUT-guided Program Variant Generation
Instead of generating from spec alone, use PUT as foundation. Filter variants using existing tests.

### 2. Generator-based Input Generation
Instead of directly generating inputs, generate a Python script (generator) that produces inputs. Separates reasoning from generation.

**Result:** 40% of direct inputs are invalid → 0% invalid with generator approach.

### 3. Diversity-driven Differential Testing
Counterintuitive: trust outputs that **differ** from PUT, not majority voting.

Rationale: Variants may inherit PUT's bugs. Trust the minority (different) output.

## Results

| Dataset | TrickCatcher F1 | Best Baseline F1 | Improvement |
|---------|------------------|------------------|------------|
| TrickyBugs (C++) | 41.31% | 24.95% | +65.57% |
| TrickyBugs (Python) | 42.35% | 36.20% | +17% |
| EvalPlus | 51.34% | 35.76% | +43.57% |

**1.80× recall, 2.65× precision, 1.66× F1** vs state-of-the-art baselines.

**16× fewer false positives** for correct programs.

## Why This Matters for AI Testing

1. LLMs write plausible but buggy code
2. Existing tests pass → false confidence
3. TrickCatcher finds the tricky bugs that escape

## Key Terms

- **Plausible Program** — passes existing test suite
- **Tricky Bug** — subtle bug that existing tests miss
- **Differential Testing** — compare multiple implementations
- **Majority Voting** — traditional approach (less effective here)

## Related

- PBT for LLM code generation (breaks self-deception cycle)
- WebTestBench (26% F1 for AI web testing)
- Property-Generated Solver (+23-37% improvement)

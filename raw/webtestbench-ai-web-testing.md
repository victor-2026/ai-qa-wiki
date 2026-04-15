**Source:** [LinkedIn - Anton Angelov](https://www.linkedin.com/pulse/%D1%82he-testing-frontier-research-brief-13-ai-model-can-break-angelov-5b0qf/)
**Date:** 2026-04-02
**Author:** Anton Angelov
**Paper:** [WebTestBench (arXiv:2603.25226)](https://arxiv.org/abs/2603.25226)
**Authors of paper:** Fanheng Kong et al. (Northeastern University, Kuaishou Technology)

---

# WebTestBench: AI Agents for Web Testing

## Context

"Vibe coding" (building web apps from natural language prompts) + non-expert creators = need automated testing. Can Computer-Use Agents (CUAs) fill this gap?

**Answer: No. Yet.**

## Benchmark Design

100 web apps (Lovable.dev), 7 categories:
- Presentation, Search, Tool, Commerce
- Data Management, Workflow, User-Generated Content

4 quality dimensions (ISO/IEC 25010):
1. **Functionality** — core features work
2. **Constraint** — implicit logical rules enforced
3. **Interaction** — UI visual feedback
4. **Content** — displayed info accuracy

## Results

| Model | F1 | Precision | Recall |
|-------|-----|-----------|--------|
| GPT-5.1 | 26.4% | 25.8% | 33.3% |
| MiMo-V2-Flash | 25.1% | 34.8% | 24.6% |
| Claude Sonnet 4.5 | 21.9% | 32.1% | 19.7% |
| Claude Opus 4.5 | 20.2% | 33.0% | 16.5% |

**Best F1 = 26.4%** — no model exceeds 30%

## Three Bottlenecks

### 1. Incomplete Test Checklists
- Coverage < 70% for all models
- Models miss **latent constraints** (implicit rules like "no double-bookings")
- Can extract explicit requirements, not implied ones

### 2. Unreliable Defect Detection
- **High false positives** (~30% precision)
- **Low recall** (< 25%)
- **Default-correctness bias** — judges "Pass" when uncertain
- Strategic divergence: GPT-5.1 = aggressive (high recall), MiMo = conservative (high precision)

### 3. Long-Horizon Interaction Unreliability
- 30-60 interaction turns per app
- 0.87M-7.26M tokens per app
- Cascading failures as history grows

## Oracle Experiment (Gold Checklist)

If agent gets human-written checklist:

| Model | F1 (Oracle) | Improvement |
|-------|-------------|-------------|
| Claude Sonnet 4.5 | 49.2% | +27.3% |
| GPT-5.1 | 46.8% | +20.4% |

**Checklist generation is the bigger bottleneck** — execution is ~50% when told what to test.

## Quality Dimensions Difficulty

| Dimension | Difficulty | Why |
|-----------|------------|-----|
| Functionality | Easiest | Explicit requirements |
| Constraint | Hard | Implicit rules, clear signals |
| Content | Hardest | Needs visual understanding + domain reasoning |

## Cost Analysis

- 0.87M-7.26M tokens per web app = **expensive**
- Cost-aware strategies necessary:
  - Test critical paths first
  - Tiered model selection
  - Targeted, not exhaustive testing

## Key Terms

- **CUA** (Computer-Use Agent) — interacts via screenshots + browser automation
- **Vibe Coding** — building apps from natural language with LLMs
- **Latent Logical Constraint** — implied but not stated rule (e.g., "no double bookings")
- **Default-Correctness Bias** — CUA judges Pass when not seeing explicit failure

## QA Implications

1. **Human checklist + AI execution** = better than fully autonomous
2. **Constraint testing** = hardest, where real bugs hide
3. **Two-stage decomposition**: what to test (human) + how to test (AI)
4. **Cost discipline** required — can't just run everything through AI

## Discussion Questions

1. What reliability threshold makes AI testing useful as first-pass filter?
2. Should AI-assisted testing = human plans + AI execution?
3. Can formal specs help AI identify latent constraints?

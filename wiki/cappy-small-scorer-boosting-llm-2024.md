# Cappy — Small Scorer Boosting Multi-Task LLMs

> Google Research (Mar 2024). Authors: Bowen Tan, Yun Zhu, Lijuan Liu, Eric Xing, Zhiting Hu, Jindong Chen. NeurIPS 2023. Paper: arxiv.org/abs/2311.06720

Cappy is a lightweight pre-trained scorer model (360M parameters, based on RoBERTa) that enhances multi-task LLM performance without fine-tuning or accessing LLM parameters.

## What It Does
- Takes an instruction + candidate response → scores 0-1 (estimated correctness)
- Works independently on classification tasks OR as auxiliary component boosting LLM predictions
- **No fine-tuning required** — bypasses back-propagation through LLM parameters
- Compatible with **closed-source LLMs** (API-only access)

## Key Results
- 360M parameters **outperforms** OPT-175B and OPT-IML-30B on 11 PromptSource tasks
- **Matches** accuracy of T0-11B and OPT-IML-175B (100-500x larger models)
- Boosts FLAN-T5 performance by large margin on 45 BIG-Bench tasks
- Works with other adaptation methods (fine-tuning, in-context learning) for additional gains

## Architecture
- continual pre-training on top of RoBERTa
- Regression-based scoring (0 to 1 correctness estimate)
- Lightweight (360M params vs LLM billions)

## Why It Matters for QA / Testing
1. **LLM-as-Judge alternative**: Cappy scores correctness without requiring a larger model — lightweight verification layer
2. **Test data quality**: Score generated test cases for correctness using a small, fast model
3. **Cost efficiency**: 360M params vs billions for scoring — dramatically cheaper inference
4. **Adaptation without fine-tuning**: Can adapt to domain-specific tasks without retraining the LLM
5. **Composable**: Works WITH fine-tuning/in-context learning, not instead of

## Connection to Existing Patterns
- [[llm-testing]] — Cappy as LLM-as-Judge implementation (lightweight variant)
- [[known_patterns|Pattern: llm_filter_approach]] — small model filtering before expensive LLM calls
- [[aria-qa-data-automation-agent-2026]] — ARIA's LLM-Judge verification layer (Cappy-style scoring)

## Source
- URL: https://research.google/blog/cappy-outperforming-and-boosting-large-multi-task-language-models-with-a-small-scorer
- Paper: https://arxiv.org/abs/2311.06720
- Code: https://github.com/tanyuqian/cappy
- Tags: #cappy, #lightweight-scorer, #roberta, #neurips-2023, #llm-boosting, #parameter-efficient, #google-research

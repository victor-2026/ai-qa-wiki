# Connect the Dots: Training LLMs for Long-Lifecycle Agents (arXiv:2606.20002)

**Authors:** Yanxi Chen, Weijie Shi, Boyi Hu, Zeyue Zhang, Zhiwei Wang, Yuexiang Xie, Yaliang Li, Bolin Ding, Jingren Zhou
**Source:** https://arxiv.org/abs/2606.20002
**Context:** arXiv cs.LG paper. v1 18 Jun 2026, v2 20 Sep 2026. Implementation: https://github.com/agentscope-ai/Trinity-RFT/tree/research/cod_v2/examples/research_cod. Digest 23.09 candidate.

---
Framework for training LLMs to "Connect the Dots" (CoD): a meta-capability required by long-lifecycle agents — as an LLM-based agent is deployed in an environment, it solves a long sequence of tasks while continuously exploring the environment, learning from its own experiences, and iteratively self-updating its context about the environment, achieving progressively better performance on future tasks conditioned on updated context.

Major components:
1. Algorithm design and infrastructure for end-to-end reinforcement learning (RL) with long rollout sequences interleaving solve-task and update-context episodes.
2. Tasks and environments for incentivizing/eliciting the targeted meta-capability during training + faithfully measuring progress during evaluation.

Proof-of-concept: GRPO-style RL algorithm with fine-grained credit assignment; tasks and environments tailored to the meta-capability (not domain-specific LLM capabilities or standard task-by-task RL).

Empirical results with Qwen3-8B and Qwen3.6-27B validate end-to-end RL training in CoD, and demonstrate out-of-distribution generalization — within training domains, across different domains, and from CoD to Ralph-loop settings.

v2 updates: scale up to larger Qwen3.6/3.8 models and new domains; multi-teacher on-policy distillation; theoretical study of learning dynamics.

QA relevance (digest): long-lifecycle agents (self-updating context over long sequences) → new QA strategies for long-duration monitoring and adaptive testing; memory/context drift as a test target.
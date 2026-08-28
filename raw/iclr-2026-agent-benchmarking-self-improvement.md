# ICLR 2026: Agent Benchmarking, Self-Improvement, Memory (Daria Satco)

Source: LinkedIn posts by Daria Satco (Head of ML @ Yandex Crowd, ex-McKinsey), ~May-Aug 2026. Series of posts after ICLR 2026 (Rio de Janeiro): observations #1 (benchmarks) and #2 (agent self-improvement and memory), plus post about support automation conference and Habr article on LLM quality control.

---

## 1. Old benchmarks measure new agents worse (post 5)

If an agent must work in the real world, evaluate it in conditions similar to real work. Focus shifts to interactive benchmark environments: tasks with state, tools, files, interfaces, constraints, dynamics.

Academic works:
- Gaia2 - testing agents in dynamic and asynchronous environments
- "Shoot First, Ask Questions Later" - how to check an agent for rational environment exploration and the ability to clarify information
- OpenApps - environment for testing UI-agent robustness to interface changes

Industry:
- Toloka - private benchmark infrastructure: hidden test cases, stateful enterprise environments, deterministic verification, constantly updated tasks
- Turing - PEbench (bench.turing.com): not just final score but traces, criteria-based checks, failure patterns
- Amazon SOP-Bench - agents on industrial processes: long workflows, step dependencies, tools, ambiguous conditions, failure handling

All 3 industry benchmarks share 3 parameters:
1. Business domains выделены
2. Test cases match complex business processes
3. Verification not just at dialogue level but full interaction with tools and applications

Trend: less focus on "model intelligence in general", more on the ability of a model inside an agent system to reliably complete a specific workflow in a specific environment.

## Details from primary sources (verified via ICLR 2026 site, arXiv, Amazon Science, GitHub)

### Gaia2 (Meta SuperIntelligence Labs, ICLR 2026 oral)
- arXiv 2602.11964; paper: Froger et al.; benchmark for LLM agents in realistic, asynchronous environments
- Scenarios evolve independently of agent actions: temporal constraints, noisy/dynamic events, ambiguity, multi-agent collaboration
- ARE framework (Agents Research Environments): open-source, event-based, time-driven simulations; re-implements tau-bench, tau2-bench, GAIA, BFCL-v3, VendingBench
- Each scenario paired with a write-action verifier -> fine-grained action-level evaluation, usable for RL from verifiable rewards
- Results: no model dominates. GPT-5 (high) strongest overall 42% pass@1 but fails time-sensitive tasks; Claude-4 Sonnet trades accuracy/speed for cost; Kimi-K2 leads open-source at 21% pass@1
- Key point: verifies at action level (intermediate steps), not just final output (unlike GAIA exact match)

### OpenApps (Meta, ICLR 2026)
- Ullrich et al.; open-source ecosystem with 6 apps (messenger, calendar, maps, etc.), configurable appearance/content, single CPU
- 10,000+ independent evaluations, 7 leading multimodal agents
- Finding: reliability within fixed app is stable, but varies drastically across app variations - task success fluctuates >50%; Kimi-VL-3B average success from 63% to 4% across app versions
- Agents loop or hallucinate actions differently depending on environment config
- QA reading: UI-agent robustness to interface drift = visual/UI testing relevance

### SOP-Bench (Amazon, ICLR 2026 expo talk + KDD 2026)
- Nandi et al.; 2,000+ tasks from human expert-authored SOPs, 12 business domains (healthcare, logistics, finance, content moderation, etc.)
- Human-AI collaborative framework: experts author SOPs, AI generates artifacts (tools, APIs, datasets), human-validated; executable interfaces + ground-truth outputs
- Metrics: ECR (Execution Completion Rate), C-TSR, TSR (Task Success Rate), outcome-aware
- 10-50+ decision points per procedure; two agent architectures (function_calling, react), 11 frontier models
- GitHub: github.com/amazon-science/sop-bench (CC-BY-NC-4.0); security note: not on PyPI
- Purpose: not model ranking, but rigorous evaluation framework for agent design choices, model selection, deployment

### TRAJECT-Bench (Amazon, ICLR 2026)
- Trajectory-aware benchmark for evaluating agentic tool use (found via amazon.science ICLR 2026 page)

## 2. Agents as self-improving systems (post 4)

Agents are no longer viewed as LLM + tools + prompt, but as a system that accumulates experience, learns from traces, uses tools optimally, improves itself. Many works on agent memory design and self-improvement:

- MASS (Multi-Agent System Search) - optimizes a multi-agent system in 3 stages: first improves prompts of individual agent blocks, then searches for the best interaction topology, then optimizes prompts at the level of the whole found system
- ACE (Agentic Context Engineering) - agent improves its own context via loop: trace generation, reflection on successes and errors, careful incremental context updates. Key idea: do not rewrite the whole context, do incremental updates - add, clarify, clean individual playbook items
- GEPA - prompt optimizer for agent systems: LLM analyzes traces, understands where the prompt caused an error, proposes an improved instruction, then evolutionarily selects best variants

Memory posters (main trend - agent needs not just a long dialogue history but managed memory: select, compress, structure, reuse experience):
- PlugMem - "pluggable" memory: instead of storing and searching raw past traces, the agent structures experience into a compact knowledge-centric memory graph (knowledge = extracted facts and strategies)
- SimpleMem - memory useful and cheap: 3-step pipeline - semantically compress raw interactions into memory units; within session merge related pieces into more abstract representations; at retrieve first determine what info is needed (intent planning), then fetch relevant memory

## 3. QA control for agents - open question (post 3)

Yandex Crowd support automation conference (Sber, T-Bank, AliExpress, Cloud.ru shared production experience):
- AI agents as first line of support - already the norm; main challenge - scenario selection and infrastructure adaptation
- AI agents for personalization - new trend, more controllability of communication style
- Trade-off between economic benefit and building a strong agent; optimization is next step
- Quality control and testing - areas that are only developing, many open questions: whose side has control? who is responsible for agent errors? how to keep agents relevant in a constantly changing product?

## 4. Habr article: LLM catches errors in support dialogues (post 9)

Yandex Crowd published a Habr article: "Ловим ошибки в диалогах поддержки с помощью LLM: опыт команды Yandex Crowd" - how an LLM pipeline catches errors in support dialogues. LLM as QA tool for dialogue quality.

## 5. Team results (post 13)

Yandex Crowd ML team year results with generative models (LLM + VLM):
- Automated labeling on 10+ projects, preparing a feature that fully removes ML team from the chain
- Covered 20%+ of quality control criteria of customer support
- Accelerated operators in 3 products via RAG hints in interface

---

## Why this matters for QA (analysis notes)

- Benchmark shift = verification layer thesis (parallel to Pavel Shcherbinin posts: checking is the bottleneck). PEbench with traces/failure patterns = downstream validation evidence, not just score
- "Whose side has control? who is responsible for agent errors?" - the open QA question; opportunity for QA leadership positioning
- ACE incremental playbook updates = context engineering pattern for test agents (Planner/Generator/Healer); MASS topology search = subagent orchestration
- Toloka hidden test cases + deterministic verification = golden dataset pattern for agent evals
- SimpleMem intent planning = retrieval-first approach for agent memory; maps to RAG patterns in known_patterns.json
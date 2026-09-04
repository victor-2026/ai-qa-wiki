# AI Engineering Skills Map: Building and Deploying AI Applications

**Author:** Andrew Ng (DeepLearning.AI)
**Source:** https://www.linkedin.com/pulse/ai-engineering-skills-map-building-deploying-applications-andrew-ng-gyn5e
**Date:** August 21, 2026 (9,308 reactions, 286 comments at fetch)
**Fetched:** 2026-09-04 (full text via webfetch)

---

Top-level skills recap: (i) Building and deploying AI applications, (ii) Software engineering fundamentals, (iii) Using coding agents, (iv) Shaping the build. This article fleshes out the first.

Being skilled at building and deploying AI applications means knowing: LLM foundations; Grounding models with data; Building agentic systems; Evaluation-driven development; Operating in production; Machine learning foundations. Formed from job postings, expert interviews, surveys.

Key difference AI vs non-AI software: output less predictable (LLM output unknown in advance; supervised predictions unknown on new examples). Building AI = more iterative: build piece, examine, decide next step influenced by intermediate results. Skillfully deciding next = reliable systems from unreliable components. Requires knowing:

**LLM foundations.** Tokenization, generation → when to count on them vs fail; multimodal choice; context window tradeoffs; cache hits, knowledge cutoff, reasoning effort, sampling params, tool calling; model/mix choice; fine-tuning, self-hosting.

**Grounding models with data.** LLMs need good input context. RAG via vector search was early; menu grew: prompt vs on-demand tool retrieval; representation (vector index, knowledge graph, semantic layer over structured data like customer records); turn documents (text, PDF, HTML, images) into LLM-ready inputs; pipelines to keep data clean/fresh.

**Building agentic systems.** Range: predefined LLM-call workflows → agent harness where LLM decides next step. Choose architecture: chain vs parallelize, code vs LLM, workflow/harness with fallbacks. Agent loop design: tools (MCP, CLI, sandbox), memory architecture, context over long sessions, single vs multi-agent. Productionize: guardrails, adversarial inputs, risks (data exfiltration), governance. Cutting edge: voice, computer-use, generative UI.

**Evaluation-driven development.** Most important trait distinguishing great AI builders: disciplined evals/error analysis loop. Varies by project and stage. Deep skill: traces/outputs + exploratory data analysis + product/business insight → what to measure. Menu: deterministic (code-based) evals vs LLM-as-a-judge vs human-in-loop; evaluate your evals, keep evolving. Evals feed iterative development, progress systematic not random.

**Operating in production.** Unpredictability, cost, latency. Observability on real usage; track performance, detect drift, respond to model failures and prompt injections. Regression testing + CI/CD need more statistical evals; testing effort calibrated to risk. Optimize cost/latency: model choice, distillation, fine-tuning, workflow simplification.

**Machine learning foundations.** Modern LLMs built with supervised + reinforcement learning. Good LLM builders understand ML/DL at depth. Many apps still need ML (own or others' trained models): popular models, accuracy/training/inference tradeoffs, data engineering for training/eval. Bias/variance, error analysis, engineering data — core mental frameworks for uncertain-output systems.

A lot to learn; every bit helps. Strong complement: software engineering (next post).

Notable: Leonardo Scelza (synapseForge OSS declarative agent-loop architecture, memory, permissions); Vaisakh R K (evaluation-driven development = building only beginning, continuous evaluate/learn/improve).

Series: (1) Map m479c → (2) this → (3) Fundamentals 7lnac → (4) Coding agents h8yxc.

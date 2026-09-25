# Superlinked — Open-Source Inference Engine for Agents (Company Profile 2026-09-25)

**Company:** Superlinked (https://superlinked.com/) — open-source inference engine (SIE) for AI agents. GitHub superlinked/sie 3.3K⭐, Apache 2.0, SOC2 Type 2. Deployment: self-host (Docker laptop, Helm K8s, Terraform AWS/GCP/Azure, air-gapped mirrored snapshots) or managed (GPU quotas/autoscaling, zero data retention). 138 models. Integrations: Chroma, LanceDB, Qdrant, Weaviate, LangChain, LlamaIndex, Haystack, DSPy, CrewAI.
**People link:** Alexandra Gyetvai — Head of Operations (US/UK/Hungary/Israel ops, internal AI systems, MCPs). Outreach peer log: `Positions-CV-CL/outreach/active/Alexandra_Gyetvai/index.md`.
**Sources:** https://superlinked.com/ (fetched 2026-09-25) + Alexandra profile paste.
**Layer verdict: INFERENCE INFRASTRUCTURE (execution substrate), NOT a QA verdict product → NO pilot** (nothing to mutation-test). Infra-relevance for verdict layer is direct (see below).

---

## Product surface (tasks, all self-hostable)

- **Search:** embed/match/rerank (bge-m3, SPLADE-v3, ColBERTv2, qwen3-reranker).
- **Document to markdown:** PDFs/Office/scans → clean markdown (glm-ocr, PaddleOCR-VL, Docling).
- **Structured output:** schema-valid JSON (gliner2, numer-zero, qwen3.6-27b).
- **Guard content:** safety verdict with probability to threshold (granite-guardian-2b) — adjacent to our guardrail thinking.
- **Run agent loop:** plan + tool calls with open LLMs, streaming (qwen3.6-27b/4b).
- Agent plugin: routes document work off frontier-model bill + redacts sensitive data pre-third-party-model.

## Vendor claims (directional, their benchmarks)

- Cheaper 50x (gte-multilingual vs text-embedding-3, AWS EKS L4); Faster 2.7x (bge-m3 vs Cohere rerank-3.5, MTEB AskUbuntu); Smart 96% (Qwen3.6-27b vs GPT-5.1, AA Intelligence Index); GPU efficiency 89% vs 51% (pool-then-batch vs route-then-blind). Comparison blog series vs vLLM/SGLang/TEI/Modal/llm-d/Dynamo. Worker pools (L4/H100/RTX PRO 6000), KEDA scale-from-zero, hot-reload profiles.

## Infra relevance for us (why this dossier exists)

- **Self-host our judges:** verdict models (rerankers, guard models, small judges) runnable on own cluster/air-gapped — cost + data-residency leg of tier-model matrix.
- **Qdrant integration:** matches Victor's stack (HARDWARE_SPEC Qdrant) — retrieval substrate already familiar.
- **Guard-content verdicts:** safety-verdict-with-probability pattern mirrors our threshold-gate design (cf. tier-model matrix escalation rules).
- **Inference grants:** free hosted capacity for selected projects (application form on site) — potential free compute for eval campaigns (n=30 etc.).
- **Blog as radar:** serving-fleet benchmarks (FlashNorm, small-model fleets, RAG grounding "stop answering what docs never said") — adjacent reading, not core.

## Hiring/context color (not leads)

- Hiring Senior Infrastructure Engineer (contract, Europe/Israel, inference/GPU/K8s); London Qwen hackathon with Alibaba Cloud. Employer context for Alexandra only.

## See also
- [Alexandra Gyetvai — Talks & Posts Catalog (talent engineering, AI in HR)](wiki/alexandra-gyetvai-catalog-2026.md)
- [[tier-model-selection-matrix-2026]] — where self-hosted judges fit per tier
- [[alexandra-gyetvai-catalog-2026]] — people/catalog side
- HARDWARE_SPEC.md (repo root) — Qdrant in local stack

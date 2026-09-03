# Making Your Data Ready for Agentic AI (Martin Fowler)

**Source:** https://martinfowler.com/articles/making-data-ready-for-agentic-ai.html (Pramod Sadalage & Prem Chandrasekaran, Thoughtworks)
**Date:** August 27, 2026
**Tags:** #data-contracts #agentic-AI #AI-ready #governance #semantic-layer #MCP
**Raw:** [martinfowler-making-data-ready-agentic-ai-2026.md](../raw/martinfowler-making-data-ready-agentic-ai-2026.md)

---

## What It Is

30-year data systems were built for human consumers (analysts bring implicit context, skepticism, judgment). Agentic AI consumers are opposite: act confidently on whatever handed, no smell test. Article defines what "AI-ready" must mean and layers to engineer it. Not about agent frameworks/orchestration — about data layer first. Layers are additive.

## AI-Ready = 5 Attributes (Human Did Free, Now Engineered)

| Human Did | Agent Needs | Attribute |
|-----------|-------------|-----------|
| Pauses at wrong number | Acts on wrong number | **Trusted** — accurate, fresh, validated before agent sees |
| Knows revenue = gross - returns, fiscal Feb | Must be told | **Contextual** — meaning explicit |
| Can explain why later | Reasoning gone in 30 sec | **Traceable** — reconstruct why |
| Bounded by role/judgment | Must be bounded by design | **Governed** — scoped, controlled, auditable |
| Reads dashboard then does something | Must be able to do something | **Operational** — readable → actionable |

Miss one = agent fails confidently, not gracefully.

## 4 Layers to Build (Order Matters)

### 1. Data Contracts and Quality — Agents Can't Smell Bad Data
- **Agents treat every value as truth.** Example: pricing agent quotes stale $49.99 vs $59.99 → loses $10/unit. No warning, cascade.
- **Schema is law: data contracts as code** (Open Data Contract Standard v3.1.0 + Data Contract CLI, Thoughtworks Radar 33). Example `product_pricing` contract: `price >0`, `currency IN (USD,EUR,GBP)`, `slaProperties: latency 24h on ingested_at`. Enforcement: schema, freshness SLA (key to successful load time, not value change), quality gates in CI/CD blocking deploy.
- **Quarantine pattern** (circuit breaker): raw → validation gate (schema/freshness/quality) → if pass → certified Gold, else → dead-letter queue + alert. Agent never sees bad data; says "no current data" vs wrong number.
- **Medallion for agents:** Bronze (raw, immutable), Silver (validated/deduped, quarantine lives), Gold (certified, governed, metrics trusted), **Adaptive Gold** — agents curate (watch query patterns, materialize views); Apple at CONTEXT 2025 described agents as "digital stewards" of catalog. Principle: agents see only Gold+.
- **Same rules for unstructured:** vector store RAG needs trust: freshness SLA = index rebuild success within 24h, contracts = metadata (source/version/timestamp/scope), quality = reject empty/truncated/duplicate/failed extraction/embedding drift.
- **Confidence-threshold routing:** data-level signals (freshness/completeness) + model confidence → if < threshold (e.g., 85%, pricing 90%, FAQ 70%) → defer to human. Start hard gate: any contract/SLA breach → human, then weighted scoring.
- **Where to start:** freshness SLAs per dataset per consumer, quarantine gates on highest-risk datasets, Data Contract CLI in CI, threshold routing 90%→down.

### 2. Traceability and Governance — Auditing Autonomous Agents
- **Audit gap:** bank agent approves $2.4M letter of credit in 30 sec (KYC → sanctions OFAC → credit terms). Traditional logs show *what* (tables/time/service account) not *why* (why that order, why approve despite minor doc discrepancy, alternatives). EU AI Act Art 12+19 requires high-risk systems auto-log events lifetime + retain 6 months + reconstruct why; breach = up to €15M or 3% turnover.
- **Agentic lineage:** extend data lineage to why: traces + spans (borrowed from Jaeger/Zipkin). Trace = end-to-end LC-4892 workflow; spans = KYC verified, OFAC clear, credit within limits, APPROVE 94% + reasoning chain. Tools: OpenTelemetry (Adopt), Langfuse (Trial), Arize Phoenix (Assess) on Thoughtworks Radar.
- **Staged autonomy:** Shadow (recommends, human executes, log accuracy) → Supervised (prepares, waits approval) → Autonomous with guardrails (acts within reversibility boundaries) → Full (spot checks, other agents monitor). Promotion on evidence, with deterministic tests (mock/replay, evals).
- **Delegated access + JIT credentials + least privilege:** act with Alice's permissions (not broad service account), short-lived scoped token (5 min), minimum access. Breaks Simon Willison's "lethal trifecta" (private data + untrusted content + external comms = prompt injection exfiltration).
- **Where to start:** instrument day one (traces with reasoning/sources via OpenTelemetry), shadow mode first, delegated access + JIT, build to be explainable.

### 3. The Context Layer — Teaching Agents What Data Means
- **Revenue problem:** agent doesn't know what "revenue" means (which tables, gross/net, fiscal Feb). Semantic layer fills gap.
- **Three models = context layer:** **Domain model** (what exists: entities/relationships/meaning rules, e.g., active customer = purchased 90d; consulted, never executed), **Semantic model** (how numbers computed: metrics as code, one versioned formula, compiled to SQL, e.g., `revenue = order_amount - discount_amount` via dbt MetricFlow/Cube/Snowflake), **Capability model** (what may do: curated reads/writes against live systems with permissions/owner/preconditions/reversibility). Nouns, numbers, verbs — all declared once in version control, not guessed per request. Domain with no arrow (consulted); others via MCP etc.
- **Explainer:** semantic layer = Business Objects → LookML/Cube → Apache Ossie; domain model = knowledge graph / DDD domain model (bounded context, federated Data Mesh, ontology RDF/OWL/SHACL — Palantir Foundry, Databricks Genie).
- **Metrics as code** example: YAML defines `revenue` measure, agent generates constrained SQL (correct table, formula, fiscal dates, join) vs without (guesses `sales_data` `SUM(amount)` `quarter='Q3'`).
- **Where to start:** find conflicting metric definitions (revenue gross vs net), pick tool (discipline > tool), route agents through layer never raw schema, adversarial test — every hallucination = missing definition (fix definition, not prompt).
- **Knowledge graphs** for traversal depth unknown pre-query.

### 4. From Searchable to Actionable — Agent-Ready Data Access
- **Spectrum:** readable → actionable; **Three primitives, one protocol (MCP):** (implied) read, write, capability; **Antipattern:** naive API-to-MCP conversion; **What capability declares:** permissions/owner/preconditions/reversibility; **Retrieved text informs, never gates** (second cut at lethal trifecta: poisoned doc can't grant permission).
- **End-to-end:** PO payment scenario (not detailed in excerpt).
- **Where to start:** not excerpted.

## AI-Ready Data Stack + Ownership

- Stack = trusted data + context layer + actionable access + observability (agentic lineage).
- Ownership: federated (Data Mesh), domain teams own their context layer; central enables via platform.

## Where Do You Stand? + Four Things to Start On

Diagnostic + additive adoption. Start: freshness SLAs, quarantine gates (pricing/inventory/customer first), Data Contract CLI, threshold routing.

## Relevance to QA/QE

| Pattern | QA Action |
|---------|-----------|
| Data contracts as code + quarantine | Treat test data as product: contract for test fixtures, quarantine bad seed data before agent sees |
| Freshness SLA | Test data freshness = signal; stale pricing = wrong test oracle |
| Agentic lineage (traces/spans) | QA evidence layer needs same: every agent decision must emit trace with reasoning/sources for audit/debug |
| Staged autonomy + delegated JIT | Mirror QA: shadow → supervised → autonomous with guardrails; least privilege for QA agent |
| Semantic/context layer | Same as test harness context: metrics/DB schema must be explicit, not guessed via LLM hallucination |
| Retrieved text never gates | Critical for MCP testing: poisoned retrieval must not authorize write |

## Critical Analysis

**Strengths:**
- Concrete: pricing agent $10 loss, bank $2.4M approval, contract YAML, medallion+Adaptive Gold, EU Act €15M.
- Distinguishes data-quality confidence vs model confidence (freshness SLA overrides model certainty).
- Layers are additive and ordered (trusted first).

**Gaps:**
- Confidence-threshold single score is open design problem — hard gate recommended until weighted scoring proven.
- Adaptive Gold early-days; agent as digital steward not yet proven at dataset level.

## Cross-links

- Related: [Zalando agentic snapshot](zalando-agentic-engineering-snapshot-2026.md) (LiteLLM proxy, risk-based gate, Identity Broker — complementary governance)
- Related: [Zalando search QA with LLM-as-judge](https://engineering.zalando.com/posts/2026/03/search-quality-assurance-with-llm-judge.html) — evaluate data quality with judge
- Related: [Building Reliable Agentic AI Systems](https://martinfowler.com/articles/exploring-gen-ai/building-reliable-agentic-ai-systems.html) (feed)
- QA evidence layer: [ai-qa-evidence-layer-validation-evals-guardrails-telemetry.md](ai-qa-evidence-layer-validation-evals-guardrails-telemetry.md)

---

*Ingested: 2026-09-01*

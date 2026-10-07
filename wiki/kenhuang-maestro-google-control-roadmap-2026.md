# Ken Huang: MAESTRO + Google AI Control Roadmap (3D Control Model, Oct 2026)

**Source:** Ken Huang, "I Love Google's Agentic AI Security Roadmap: Adding MAESTRO Will Make It More Powerful — An Open Letter to Google", Agentic AI Substack, 2026-10-05. Full text read (no paywall).
**URL:** https://kenhuangus.substack.com/p/i-love-googles-agentic-ai-security

## The two axes being synthesized

1. **Google DeepMind AI Control Roadmap (June 2026):** treats advanced internal agents as potential insider threats (rogue-employee framing). Builds on MITRE ATT&CK with TRAIT&R taxonomy (loss of control, work sabotage, direct harm). Two capability ladders: D1-D4 detection (scales with evasion ability), R1-R3 prevention/response (scales with severity). Empirically grounded: ~1M coding-agent trajectories analyzed; most anomalies = over-eagerness + misinterpretation, not malice.
2. **CSA MAESTRO (Feb 2025):** 7-layer decomposition of agentic systems — L1 Foundation Models, L2 Data Operations, L3 Agent Frameworks, L4 Deployment & Infra, L5 Evaluation & Observability, L6 Security & Compliance (vertical), L7 Agent Ecosystem. CSA + OWASP companion Red Teaming Guide = 12 operational test categories.

## Thesis: control = (behavior, capability, architecture)

> control = (behavior, capability, architecture)

TRAIT&R answers WHAT the attacker does. D/R ladders answer HOW capable. MAESTRO answers WHERE (origin, propagation, ownership, evidence). Without the third axis, "implemented" becomes a checkbox: tool allow-list at L3 means nothing if runtime still grants broad cloud credentials at L4.

**Integration rule:** no roadmap mitigation is complete until every relevant MAESTRO layer has an enforcement point, an evidence source, and a tested failure response.

## Four gaps that matter most

1. **Memory is an ungoverned persistence layer (L2).** Poisoned writes sit dormant, activate in later context, spread via retrieval. Prescription: provenance-tag entries, TTLs, separate tool observations from instructions, test that reset actually purges poison/index/cache/peer stores.
2. **The supervisor is a single point of failure (L5).** Checker-out-of-the-loop is a CSA threat category; tool poisoning evades output-based safety checks. Monitors need documented independence: different model family, raw event access (not agent-authored summaries), isolation, fallback signal. High-consequence actions never authorized solely by a monitor whose evidence the acting agent can modify.
3. **Multi-agent trust is under-modeled (L7).** Question shifts from "can this agent act?" to "which claims about this agent should another trust?" Needs delegation semantics: non-transitive grants, signed lineage, depth/expiry limits, cascading revocation (killing a parent kills descendants' authority).
4. **The metrics can hide catastrophic gaps (L5).** One headline coverage % can hide zero coverage of a rare catastrophic action. Fix: coverage by layer, action class, risk tier; time-to-contain and time-to-revoke separate from time-to-alert; residual autonomy after shutdown. Every percentage publishes its denominator.

## Ten metrics (report volume-weighted + risk-weighted side by side)

Layer coverage, authoritative-action coverage, attack-path coverage, trace completeness, detection precision, time-to-contain, time-to-revoke, rollback success, residual autonomy, monitor diversity (2+ independent signals on high-risk actions).

> risk_weighted_coverage = Σ(action_risk_weight x control_evidence_present) / Σ(action_risk_weight)

Weights from documented impact model, never from monitor confidence. Starting from zero: layer coverage, attack-path coverage, time-to-contain.

## Builder's playbook (7 steps)

1. Decompose system into 7 layers (30-min workshop; split spanning components at boundaries).
2. Adopt machine-readable event schema (id, traitr, csa categories, capability D/R, maestro entry/path/governance, asset, action, enforcement points, evidence, response incl. recovery, owners, tests, status). "A control with no path is a control you cannot compose."
3. Map 12 threat families to your layers = test backlog. Categories 7-12 (distributed/persistent) all need a recovery phase, not just a block.
4. Score control chains, not controls. Never claim D/R milestone from model benchmark alone; include at least one test attacking the safety mechanism itself.
5. Measure the ten metrics.
6. Enforce transitive-trust invariant: every authoritative action traceable to a current root authorization through an unbroken, non-expanding chain.
7. Close the loop: threat graph + control graph + evaluation graph, updated each cycle.

## External validation in the comments

Amit Spitzer (liked by Huang): all ten metrics are self-reported by the same org running the agent; every frontier-lab agent escape disclosed this year was caught by outsiders checking logs weeks later, not by the lab's own monitor. "A coverage number nobody outside the vendor can audit is still just a claim with better formatting."

## Author context (Oct 2026, self-stated in promo post)

Ken Huang, "Back by popular demand: Cohort 2 of Hands-On Harness Engineering with Claude" (Agentic AI Substack, 2026-10-07, free portion read 07.10; slides+repo links behind paywall): Adjunct Professor Univ. of San Francisco, CEO DistributedApps.ai, OWASP AI Verification and Security Standard (AIVSS) lead, co-chair of two CSA AI Safety working groups, OWASP Top 10 for LLM contributor; books "Harness Engineering" + "Graph Engineering for Agentic AI Systems". Live masterclass Cohort 2 with Packt: 17.10.2026 9:00-11:30 AM EDT, 10 Python modules + deep-research capstone, 14 automated suites, five-gate production readiness scorecard, kn40 = 40% off. Production failure trio named: context decay, infinite retry loops, unverified file modifications. Module list (9): harness-vs-traditional-SWE, 5 pillars (memory tiers, 31-event lifecycle), spec-driven (SPEC.md, AST filtering), guardrails (PreToolUse denial, secret scanning, append-only approvals ledger), tests-as-reliability, MCP architecture, multi-agent worktrees, 5-step SOP + 5-gate audit, capstone. Lead: exercises repo "packt-harness" claimed open-source (URL in paid section — unverified, check before citing). Status: promo — watch for attendee write-ups or free materials; scorecard may become W4 fodder.

## QA interpretation

- Direct vocabulary match with our tracks: denominator discipline (per-risk-tier), monitor independence (assessor vs author), seeded attacks on the safety mechanism itself (mutation matrix), residual autonomy (what "shutdown/pass" actually proves).
- Gap #4 is our Article 26/29 ammunition: vendor coverage claims without per-tier denominators.
- Spitzer's objection = our attestation thesis: independent evidence, not vendor telemetry.

## See also

- [Runtime authorization for AI agents](wiki/runtime-authorization-ai-agents-2026.md)
- [Anthropic + Spotify quality at AI speed](wiki/anthropic-spotify-quality-at-ai-speed-2026.md)
- [Breaklight testing methodology whitepaper](wiki/breaklight-ai-testing-methodology-whitepaper-2026.md)

- [[runtime-authorization-ai-agents-2026]] — provenance-bounded activation, envelopes
- [[andrew-ng-openworker-security-agents-2026]] — harness/model split
- [[ai-qa-evidence-layer-validation-evals-guardrails-telemetry]] — evidence layer

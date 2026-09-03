# rUv (ruvnet) — Agentic Stack

**Source:** https://ruv.io/ (Reuven Cohen) + https://github.com/ruvnet (11.3k followers, 214 repos, 172k stars)
**Date:** Snapshot August 10, 2026 (README metrics)
**Tags:** #agentic #harness #RuView #Ruflo #RuVector #MetaHarness
**Raw:** [ruvnet-overview-2026.md](../raw/ruvnet-overview-2026.md) *(to be fetched as raw if needed)*

---

## What It Is

rUv builds open-source infrastructure for agent orchestration, adaptive memory, vector intelligence, portable runtimes, and privacy-preserving spatial sensing. Core stack: **RuView + Ruflo + RuVector + MetaHarness + RVF/RVM**, plus Flow Nexus, AgentDB, QuDAG, FACT. Published via one account (214 repos, 176 owned non-fork, 24 forks). 91% stars concentrated on 2 flagships — strongest distribution wedge and main dependency.

**Aug 2026 note:** RuView and Ruflo remain distribution anchors; WiFi Veil, rvQR, RuCelium, RVForge extend sensing/portable execution.

## GitHub Reach (Verified 2026-08-10)

| Measure | Value |
|---------|-------|
| Followers | 10,880 |
| Owned non-fork repos | 176 |
| Stars owned | 172,270 |
| Downstream forks | 23,339 |
| RuView stars/forks/watchers | 89,184 / 11,873 / 793 |
| Ruflo stars/forks/watchers | 67,549 / 8,084 / 433 |
| RuVector | 4,411 / 581 / 33 |
| MetaHarness | 565 / 68 / 1 |
| npm packages (ruvnet) | 370, monthly 14-15M (May-Jul 2026, 44.3M = 69% of rolling year) |
| Rust crates | 398, 1.27M downloads |
| Rolling 14d clone events (Ruflo+RuView) | 116,556 (6,326/day Ruflo) |

*Clone/npm downloads = events, not unique users; contributions include anonymized private activity.*

## Stack Fit

| Layer | Systems | Responsibility |
|-------|---------|----------------|
| Spatial perception | RuView, rvCSI, RuField | RF/multimodal → privacy-aware spatial evidence |
| Sensing governance | WiFi Veil, RuCelium | Boundaries, provenance-aware observations |
| Agent control plane | Ruflo, MetaHarness | Coordinate, route, evaluate, preserve receipts |
| Learning memory | RuVector, AgentDB, AgenticOW | Vector/graph/temporal/episodic, branchable |
| Portable execution | RVF, RVForge, rvQR, RVM | Package, stage, optical transfer (alpha), capability-controlled exec |
| World/research | WorldGraph, RuPixel, PhotonLayer, Helix | World models, visual retrieval |

Recent delta (2026-06-13→08-10): 18 owned +5 fork repos added (WiFi Veil 11⭐, rvQR 8⭐, RuCelium 16⭐, rvFACE, AgenticOW, CVE-bench, etc.); MetaHarness 0.4.4 (10 hosts), Darwin 0.8.3/Flywheel 0.1.10 (harness evolution with gates).

## August 2026 Update Highlights

- **RuField** (5 crates), **RuVector ANN** (6 crates adaptive/speculative), **RuView RF/HOMECORE** (17 crates)
- **WiFi Veil** (privacy, synthetic L0), **rvQR** (QR optical transfer, SHA256), **RuCelium** (8 components, synthetic benchmarks)
- **RVForge** 0.2.0 (RVF containers → deterministic bundles, 303 downloads), **MetaHarness** portable harness across 10 hosts, **Darwin/Flywheel** measured evolution with signed lineage

## Provenance & Evidence

- `ruvnet/ruvnet` README separates: repository lineage (root commit anchor ≠ public date), feature evidence, public traction, verified usage.
- Dossiers: `docs/ruvnet-prior-art.md` (247 rows, commit-proof), `data/metrics.json` (machine-readable), `docs/ruvnet-packages.md` (322 crates/284 npm grouped in 28 families), `CITATION.cff`.
- Novelty = scoped candidate claims until supported by feature commits/tests/timestamps.

## Why It Matters

- **Harness-not-model thesis:** Year-One Executive Brief claims 31 first-mover positions (June 2025-2026) — harness evolution matters more than model swap.
- **Distribution:** npm 64M rolling year, 14M/month sustained — surface, not same-cohort growth (inventory expanded).

## Relevance to QA/QE

| Pattern | QA Application |
|---------|----------------|
| Ruflo/MetaHarness swarm orchestration | Reference for building QA agent harness (compare to Zalando Kiro harness, Autonoma) |
| RuVector/AgentDB adaptive memory | Memory for QA agents (failure history, flake ranking) |
| Provenance dossier + metrics.json | Evidence layer: lineage, receipts, replayable promotion |
| 4-level ladder invisible at L4 (like TestMu AI agentic regression) | Same risk: autonomous assertion rewrite → silent coverage loss |

## Critical Analysis

**Strengths:**
- Most prolific agentic OSS portfolio (214 repos, 398 crates, 370 npm) with verifiable metrics and provenance — rare transparency.
- Two flagships with real traction (RuView 89k, Ruflo 67k, 116k clones/14d).

**Gaps:**
- Concentration 91% stars on 2 repos — portfolio dependency; many new repos <20 stars, synthetic benchmarks, alpha (rvQR, WiFi Veil) not production.
- One-account publication (community contributions, automation, generated artifacts mixed) → requires dossier to separate original work vs imported history.

## Cross-links

- Related: [Zalando agentic snapshot](zalando-agentic-engineering-snapshot-2026.md) (Kiro harness + Identity Broker)
- Related: [Kiro diagnostics over time](kiro-diagnostics-over-time-agent-quality-2026.md) (harness evaluation)
- Related: [TestMu AI agentic regression](testmuai-agentic-regression-testing-2026.md) (L4 silent failure — same ladder)
- QA evidence: [ai-qa-evidence-layer-validation-evals-guardrails-telemetry.md](ai-qa-evidence-layer-validation-evals-guardrails-telemetry.md)

---

*Ingested: 2026-09-03 · Snapshot via ruvnet/README 2026-08-10 metrics + ruv.io*

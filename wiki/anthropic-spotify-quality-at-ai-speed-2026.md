# Quality at AI Speed: Anthropic CI + Spotify Delivery (STW #329 Pair, Sep 2026)

**Sources (both full-text read 2026-10-07, via STW #329 "Quality at AI Speed"):** Sachin Malhotra, "Agentic coding is straining CI…" (Anthropic, 2026-09-14) https://claude.com/blog/agentic-coding-is-straining-ci-heres-how-we-scaled-test-impact-analysis-at-anthropic · Tyson Singer, "AI Changed How Spotify Builds…" (Spotify Engineering, 2026-09-16) https://engineering.atspotify.com/2026/9/ai-changed-how-spotify-builds-what-we-learned-and-fixed-about-quality-at-higher-velocity
**Frame:** Dawid Dylowicz STW #329: merge requests × CI jobs multiply exponentially under agentic dev; verification must keep up. https://softwaretestingweekly.com/issues/329/

## Anthropic: 25x CI jobs in 6 months

- Engineers ship **8x code/quarter** vs 2021-2025; **Claude authors 80%** and reviews/approves PRs too. Tests across codebase grew **10x** on flat headcount → **25x CI jobs**.
- Deterministic test-impact-analysis service (listener records results, selector picks tests per PR from history + package relevance). Single-writer v0 couldn't shard.
- Three patches, shrinking returns: bigger machine (**70 days**), per-package sharding via Claude-generated code (**29 days**), daily restarts (**<1 day**, plus stale-selection risk: flaky/widespread-failing tests re-run, new tests skipped).
- Redesign: journal in in-memory store, stateless listener workers, separate rollup consumer. **3 weeks, 1 engineer** ("a year ago closer to a quarter"). Stable since.
- Advice: **plan for 25x load within two quarters**; over-engineering bar moves up (design for 10-20x perceived scale); instrument services as "Claude's eyes and ears" (in = out job counts); stateless from day one; Claude prefers smaller granular PRs (another reason not to run every test on every PR).

## Spotify: verification is the constraint

- Scale: 777M MAU, ~100M concurrent clients, 11-12M backend rps, ~3,000 services. Four areas tested at once (AI slop NOT among them — pace of change is).
- Content processing: silent failures (unprocessed media failing without paging) + video capacity; June 24 incident = garden-variety misses (alerting, capacity, workload controls). Fixed: end-to-end monitoring, scheduler, tiering/prioritization.
- Fleet management: agentic fleet changes (Java migration in 3 days); an automated dependency upgrade **passed checks yet failed in prod** → stronger safeguards, bigger rollback capacity, working-hours scheduling.
- Compute shortages: AI-driven scarcity breaks failover assumptions; tiered degradation accepted explicitly.
- Mobile: ebb-flow quality cycle runs at higher frequency; **single releases look healthy while small regressions accumulate outside watched signals** → broader signals + long-term trends in release decisions.
- Data: monthly major-incident retros ask two questions — (1) did AI-authored code directly contribute? (2) did change-volume pressure review/testing/rollout/observability? **No material direct AI-authored contribution found; volume-outpacing-verification confirmed.** PRs 8.1K→17K YoY Aug; quality/optimization share 27%→31% (2x+ absolute). Rework-rate metric rebuilt (churn ≠ rework; no AI quality-debt signal vs FAROS 2026 industry churn rise). Complexity + PR size creeping — thresholds deliberately NOT rewritten ("no conviction either way").

## Joint thesis

> Spotify: "AI increased the capacity to produce change. The next constraint became our ability to verify it."
> Anthropic: "Writing code is no longer the constraint… always plan for the exponential."

Generation scaled; verification is the bottleneck; stale/lagging selection is itself a defect class (Anthropic's stale-selector misses ≈ our observed-only gap: what didn't run is invisible). Spotify's "healthy release, accumulating regressions" = green-dashboard trap with vendor-independent numbers.

## QA interpretation

- Two independent confirmations that velocity-vs-verification is THE 2026 problem, with numbers (25x, 8.1K→17K, 70d→29d→<1d patch decay).
- Spotify's two retro questions are adoptable method: separate direct-authorship from volume-pressure in every incident review.
- "Don't rewrite thresholds to feel better" (complexity/PR size) = calibration honesty, pairs with Breaklight WARN rule.
- Article 26/29 material: per-tier verification pacing, rollback capacity as quality control, fleet-change safeguards.

## See also

- [Elastic shared eval framework](wiki/elastic-shared-eval-framework-chang-2026.md)
- [Breaklight testing methodology whitepaper](wiki/breaklight-ai-testing-methodology-whitepaper-2026.md)
- [Ken Huang MAESTRO 3D control model](wiki/kenhuang-maestro-google-control-roadmap-2026.md)
- [Avito agents setup metrics review](wiki/avito-agents-setup-metrics-review-2026.md)
- [LaunchDarkly guarded-release factory](wiki/launchdarkly-guarded-release-factory-2026.md)
- [Quality Minded first meetup](wiki/quality-minded-first-meetup-2026.md)

- [[breaklight-ai-testing-methodology-whitepaper-2026]] — WARN rule, chasing-ghosts vs missing-decay
- [[elastic-shared-eval-framework-chang-2026]] — eval scaling, calibration ownership
- [[kenhuang-maestro-google-control-roadmap-2026]] — residual autonomy, time-to-contain/revoke

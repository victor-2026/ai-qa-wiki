# Konstantin Slavnov (Qure/JetBrains): Why E2E Tests Change - 16K Commits via HekaJev (2026-09-24)

**Author:** Konstantin Slavnov (1st; Founder fixing QA for AI era; Qure @ JetBrains InnoHub; Qalti OSS). Post 23h old (25 reacts/25 comments) + full report + MIT tool.
**Sources:** post (user paste) + https://quretests.com/research/e2e-changes (+/data, +/methodology) fetched 2026-09-25; tool https://github.com/zurk/hekajev (MIT). Author's own framing: exploratory, NOT industry benchmark.
**Context:** Commit-level E2E-churn empirics via Jev-family classifier (HekaJev: user-defined questions over commits). 549,224 commits / 21 public repos (IBM, Mozilla, Red Hat, Automattic, Snowflake, Supabase...) → 16,024 E2E changes. API cost $23.20 (!). Directly our territory: maintenance-vs-coverage economics, flakiness trends, AI-attribution honesty.
**Captured:** 2026-09-25 from user paste + webfetch.

---

## Numbers (report-level, author-hedged)

- 38.4% new coverage vs 45.2% maintenance (26.1% product-driven, 8.1% env/tooling, 7.4% flaky, 3.5% refactor, 1.7% test-bug; 26.6% no confident reason).
- 2026 surge: new coverage 34.8%→47.7% (Jan-Sep windows), overtaking maintenance; robust (12/20 projects up, ex-Gutenberg+Mattermost still +7.5pp). Cause unknown (AI suspected, unproven).
- Flakiness repairs rising: 7.9%→10.0% (2024→2026), up in 11/13 projects. Cause unknown.
- 33.6% of new test files need maintenance within 30 days; 28.2% of flakiness fixes get another flakiness change in same file within 30 days.
- AI attribution: 805 AI-marked E2E commits; +5.69pp coverage vs unmarked BUT 95% CI includes zero → cannot claim AI effect. Honest null.
- E2E share of all commits grows with project age (0.8% Y1 → 5.1% Y12+).

## Author's own take (use with attribution, not as fact)

- AI adds coverage faster; maintenance value higher long-term (needs failure-cause understanding). New AI coverage without review → technical debt.
- "Someone will have to maintain them" = the wall our verification economics addresses.

## Use for us

- Empirical maintenance/coverage split for cost modeling (45.2% upkeep baseline; 33.6% 30-day rework on new files).
- Flakiness-rise trend (7.9→10.0%) = demand signal for anti-flaky work (Victor's 414aadd-class fixes).
- HekaJev (MIT) = Jev-family commit classifier, reproducible (research README), runnable on own repos (OrangeHRM history candidate!).
- Honest-null pattern (AI CI includes zero, stated plainly) = methodology exemplar for our own reporting.
- Konstantin Slavnov 1st connection, JetBrains InnoHub orbit, Qalti OSS - peer/vendor node; part-two promised on AI role (watch).

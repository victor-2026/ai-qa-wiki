# QA Wolf: 6 types of self-healing, diagnosis-first (2026)

**Source:** "The 6 Types of AI Self-Healing in Test Automation" (John Gluck, 2026-01-28) — https://www.qawolf.com/blog/self-healing-test-automation-types (fetched ✅ 2026-09-27). Raw: `raw/qawolf-6-types-self-healing-2026.md`.
**Author context:** QA Wolf vendor; Goran Gajic (Staff Eng Lead) wrote the Jev semantic-assertions piece in the same blog. Person card: `Positions outreach/active/Goran_Gajic/index.md`.

## The taxonomy (shares = vendor-claimed, arXiv-cited — see caveats)

| # | Type | Share | Fix shape |
|---|---|---|---|
| 1 | Timing (async order, late API) | ~30% | resilient waits / retries / polling from network + DOM-mutation signals |
| 2 | Selector (DOM/attribute drift) | ~28% | DOM-diff locator update |
| 3 | Test data (expired sessions, bad fixtures) | ~14% | session refresh / fixture reseed |
| 4 | Visual assertion (canvas/PDF/widgets) | ~10% | rendered-output compare, irrelevant-diff filtering |
| 5 | Interaction change (hidden behind menus/tabs) | ~10% | insert prerequisite steps |
| 6 | Runtime error (app/env crashes) | ~8% | log + isolate/stub, retry after transient outage |

Pipeline: **detection** (DOM snapshots, network, console, app state) → **diagnosis** (classify) → **remediation** (category-specific). Eval bar they propose: diagnosis-before-fix, all six categories, **FP rate under 5%**, Playwright/Appium integration, full audit trails.

## Two false-pass mechanisms, described by the vendor itself

1. **Healing delay as accidental wait:** "if a button is missing because the API is slow, patching the selector may add extra time during healing. That delay can give the page time to recover, so the test passes even though the underlying problem remains." The heal acts as an unrecorded sleep — green for the wrong reason, and the next slow API fails identically.
2. **Cross-page selector match:** expired session redirects to login; naive healer patches the dashboard selector, matches "a different element that happens to exist on the login screen. The step then passes, but the test no longer validates the dashboard. The result is the dreaded false negative." Same family as our QAEverest M2/M6 (5/5 green on drifted locators) — the vendor's own words for the failure mode we measure.

## Caveats (read before quoting)

- The 28/30/14/10/10/8 split is vendor-claimed with one arXiv citation (2504.16777, not fetched — `[SOURCE MISSING]` for the paper). Usable as "vendor's stated distribution", never as measured fact.
- "Virtually 100% of flakes" + naming Rainforest QA / Checksum as selector-only = competitive framing. The taxonomy is the durable part; the coverage claim is marketing.
- No seeded-break validation published: the article prescribes diagnosis but shows no catch-rate measurement on planted defects. Mirror experiment = our M2/M6 set shape against each of the six categories.

## Cross-links

- [[qawolf-semantic-assertions-jev-2026]] — same vendor, bounded-judgment primitives (`toSatisfy`/`act`); self-healing is the maintenance layer on top.
- [[testrigor-blog-catalog-all-publications-2026]] + QAEverest M2/M6 drift — the seeded-break comparison set: their "fewer dumb breaks" vs our measured green-on-drift.
- [[llm-testing-6-approaches]] — LLM-as-judge; diagnosis step is a judge over failure categories.
- [[ai-testing-metrics]] — FP <5% bar; flake-rate definitions.
- Quotes banked: Articles/quotes.md → Market Signals (delay-recovery pass, 28% stat), Independence (login-screen false negative).

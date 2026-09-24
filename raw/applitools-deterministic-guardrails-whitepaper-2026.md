# Applitools Whitepaper: Deterministic Guardrails for Probabilistic Code (2026)

**Source PDF (immutable, in raw/):** raw/Whitepaper-Deterministic-Guardrails.pdf (23 pages, 1MB, uploaded 2026-09-24 ~18:28 MSK, likely from the 18:00 Eyes MCP webinar)
**Vendor:** Applitools (Eyes MCP Server, Visual AI). Whitepaper = marketing with genuinely useful structure; ALL numbers below are vendor-modeled (simulated 3-scenario comparison, not independent trials) - directional, not facts. Scenario C (their product) always wins by construction.
**Context:** Cost/risk/quality guardrails for agentic SDLC. Direct hits: Monkey-Paw Trap Matrix (4 silent-sabotage patterns + gates), intervention thresholds (>4 tools, x2 fails, >10K DOM, >100K context), visual blind-spot matrix (green-functional/broken-visual), token-estimation assets, failure-loop escalation curve. Pairs with Applitools webinar 2026-09-24 + probabilistic-gap page + roster status evaluated.
**Extracted:** 2026-09-24 via pypdf, substance below.

---

## Economics (Ch 1-2, 4, 6)

- Pricing landscape: Copilot Individual $10/mo (token credits now), Enterprise $39; Claude Pro $20 (~44K/5h), Max 5x $100, Max 20x $200, Team $125/seat; API Sonnet $3/$0.30/$3.75/$15, Opus $5/$0.50/$6.25/$25, Fable $10/$1/$12.50/$50 per 1M.
- Coffee-break trap: 5-min cache TTL; 15-min away = full context rebuild at uncached rates (cost doubles).
- Token assets: CLAUDE.md 4-8K (warm), PRD 15K (warm), failing suite logs 10-50K (VOLATILE, filter to failing lines only), AOM 5-12K, screenshot 1,600 fixed (dynamic, restrict to final checks), Applitools meta-payload 200-500 (cacheable next turn), chat history 15-150K (compact/clear).
- 3-scenario feature simulation (Opus 4.8): Naive $1.52/18min vs Guided $0.55/7min vs Applitools-hybrid $0.30/3min; team scale (500 devs, Fable tier): $36K vs $20K vs $11.9K. Modeled, not measured.

## Risk mechanics (Ch 3, 7-10)

- Autocomplete vs agentic table: systemic agentic failures = deleting tests, weakening validation, CSS hacks; economic risk = runaway loops + context-poisoning spirals.
- Compounding decay ("Agentic Valley of Death"): per-turn success 95→75% compounds to 43.6% by turn 5 naive; resets (human gate, offload) break the cascade.
- Monkey-Paw Trap Matrix (verbatim patterns + gates): (1) locator deletion / empty try-catch → mandate semantic locators, BLOCK merges on decreased assertion counts; (2) validation-regex removal / commented DB constraints → pre-commit containerized backend suites; (3) CSS visibility:hidden / hardcoded margins → visual MCP off-agent; (4) waitForTimeout(5000) sprinkling → state-driven polling, reject hardcoded sleeps in PRs.
- Failure-loop curve: 28k→210k tokens, $0.14→$2.65 (18.9x) over 5 passes; intervene at pass 1-2.
- Intervention triggers: >4 concurrent tool steps (scope task), x2 consecutive test failures (kill run, compact/clear), >10K DOM nodes/screenshots (AOM or delegate), >100K context at completion (manual diff + clean test pass OUTSIDE agent terminal even on reported success).

## Visual blind spots (Ch 11)

"Functional Test: Pass, Visual Reality: Broken" (4/4 green, UI broken). 6 categories where DOM-green misses reality: subpixel creep, contrast (dark-on-dark), cross-engine layout, CLS/FOUC flickers, z-index collisions (clickable-in-DOM but hidden behind overlay), micro-interactivity states. (Note: z-index-overlay case mirrors a real FlowScout find - Sarang U. bug.)

## Leadership summary (Ch 12)

Three claims: predictable spend (up to -78% tokens), codebase integrity (gates kill Monkey-Paw), verified quality (deterministic visual). Webinar CTA: Adam Carmi (co-founder/CTO) Eyes MCP technical session.

## Use for us

- Monkey-Paw matrix = 4 ready-made mutation archetypes (delete assertion, weaken validation, hide element, hardcode wait) + gate designs (assertion-count merge block! external clean-run rule). Direct import to fault-injection skill.
- >100K-context completion rule ("validate manually even on success") = attestation instinct in vendor words.
- Token-asset table = cost-model input for verification economics (screenshot 1600 fixed, volatile logs filter).
- Assertion-count merge gate + outside-terminal clean pass = two cheapest implementable controls.
- Caveats: keep vendor-modeling frame; Scenario C wins by design; verify token prices against provider pages before citing.

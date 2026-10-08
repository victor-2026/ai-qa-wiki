# Quality Minded First Meetup (Sep 11 2026, Katja + Zoya, Full Triage)

**Sources (owner files 08.10, all read full):** transcript docx 31K chars (1h14m, transcription by Ekaterina Semenova) + deck-1 (11pp, defect divergence) + deck-2 (9pp, OSS platform). Community: https://www.meetup.com/quality-minded (biweekly cadence), contact ekaterina.tuna.v@gmail.com. Hosts: Katja (40y QA combined with Zoya), builder Dmitrii Drui. Attendees incl. Marius Argatu, Virtual Denis, Vlad Titov, Daniel Zakiryanov, Alexander Kai Matveev, Oleg Gusarov, Ilia, Zakir.
**Link to us (CONFIRMED 08.10 by owner):** Katja Semenova BaaS = Ursa-Minor — one line. Ekaterina viewed Victor's profile (notifications 08.10); Henock = Quality Minded speaker (inbound thread).

## Thesis: economics + defect shape changed

- Fix cost collapsed (good monitoring + fast deploy) except critical systems; 1K:5 devs formula dead under agent throughput.
- AI bugs structurally different, backed by two sourced studies: CodeRabbit State of AI vs Human (Dec 17 2025, 470 PRs: 1.7× issues, logic 1.75×/algo 2.25×, error-handling 2×, concurrency 2.29×, XSS 2.74×, I/O 8×; humans worse at spelling/testability) — deck-reported, primary unread; Naples Cotroneo et al. arXiv:2508.21634 (ISSRE 2025, >500k Python+Java, ODC+CWE: AI = assignment/function defects, unused args, shallow-but-valid; Python humans worse, Java AI worse; more high-risk vulns) — abstract verified.
- Katja's own data: 70-case suite catches 3-4/release, exploratory other ~20; pairwise/limits stop working ("bugs are in a different place").
- **Moving target:** defect profile shifts with models; quarterly heuristics partly wrong next quarter; "the only durable advantage is a community that keeps comparing notes in realtime."

## Marius Argatu intervention (strongest thread)

- Mutation testing as filter for shiny generated suites (nice tests → behave poorly under mutation; shows where app doesn't behave).
- **Counter-claim (unattributed white paper, NOT verified):** mutation testing against LLM-based tests "doesn't move the needle, just sounds like it does" — recorded as objection, source wanted.
- Invariants-first: ask PO/dev what app should do BEFORE spec; invariants solve most problems; same-spec chain (spec→code→tests from one source) multiplies one misreading (hallucination chain).
- Black-box stance: Katja's agents get no dev access. Katja: "mutation testing implementation interesting, will try in the UI."

## Platform (Ursa-Minor-Beta OSS)

agent-factory (JSON agents, any-LLM HTTP nodes, encrypted secrets, API keys, per-user isolation) + UI + BaaS (real browser, classic + llmClick selectors, local/Docker, Go client for old autotests). Rationale: shareable agents (JSON over Slack), CI/CD-callable (not laptop-bound), local-model friendly (NDA), MongoDB swappable. Feedback form; mobile BaaS planned; shutdown risk after New Year without community support. Repos: github.com/Ursa-Minor-Beta/{agent-factory, agent-factory-ui, baas, baas-client}.

## QA interpretation

- Independent practitioner confirmation: defect-divergence numbers + moving-target argument + community-as-infrastructure (pairs Avito cycle-time honesty, Breaklight weakest-slice).
- Marius counter-claim is the load-bearing objection to log (not hide): if a white paper shows mutation-blind LLM suites, we need its conditions, not its conclusion.
- Invariants-first + black-box + same-spec-chain = our pre-registration + examiner-author + seeded-breaks in community words.
- First-time-user + client-demo agents = discovery-probe pattern (W3-adjacent, no pilot proposed).

## See also

- [[anthropic-spotify-quality-at-ai-speed-2026]] — verification pacing, volume pressure
- [[breaklight-ai-testing-methodology-whitepaper-2026]] — weakest slice, reference hygiene
- [[kenhuang-maestro-google-control-roadmap-2026]] — coverage by layer/action/tier
- [[avito-agents-setup-metrics-review-2026]] — standard methods stop working

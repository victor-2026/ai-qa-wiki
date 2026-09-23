# AI Testing Tools Landscape — Hands-On Pilots & Verdicts (2026-09-09)

**What this is:** our independent map — tools WE piloted (with verdicts) + tools researched (vendor claims, discounted). Not another vendor comparison: every T1 row has run IDs behind it.
**Reviewed:** 2026-09-09. **Next review:** monthly lint (cadence ritual). **Rule:** no number without a source; unknown = TBD, never filled from erudition.
**Related:** `ai-testing-platform-comparison-2026.md` (vendor-claims layer, Autonoma-sourced), `ai-qa-tool-evaluation-mutation-matrix.md` (the method), Article 26 (playbook), Article 15 (DevAssure), Article 20 (FP case).

## Tiers (by OUR evidence depth, not vendor hype)

- **T1 — piloted deep** (mutation matrix + run IDs + verdict): QAEverest, testRigor, Agentiqa (Vendor C), DevAssure O2.
- **T2 — trialed light** (runs, no matrix): Autonoma.
- **T3 — researched** (blog catalogs / vendor claims / waitlist): everything else. Claims discounted 50% until hands-on.

## Clusters (by WHAT they automate — comparability lives inside a cluster, not across)

- **A. Agentic product verifiers** (point at app/URL, no test code): Agentiqa, Autonoma, Mabl, Panto (mobile-only), Donobu (mobile).
- **B. Codeless / NL authoring** (human writes steps in words): testRigor, Virtuoso, KaneAI/TestMu (2-way NL↔code), Functionize, Katalon (low-code).
- **C. Heal-your-suite layers** (import Playwright/Cypress, maintain it): QAEverest, Testim, Momentic (NL specs).
- **D. PR-diff agents** (test the change, not the suite): DevAssure O2. (Overlaps A in execution, differs in trigger: diff vs URL.)
- **E. Cloud grids / managed execution:** HyperExecute/TestMu, QA Wolf (managed service), BrowserStack, Testkube (OSS K8s orchestrator + AI-eval gates, see row).
- **F. Visual:** Applitools, SmartUI/TestMu. (Nobody piloted — open gap.)
- **G. Test management + AI:** TestRail, Testomat, BrowserStack TM, Testora-commercial (waitlist, $49+; research namesake arXiv 2503.18597 is a different thing).
- **H. Dev agents with testing features (NOT QA tools — compare with care):** Kiro (spec-driven IDE), Cursor/QA skills, DevAssure agent skill.
- **I. Methods (not tools, imported):** Gulin ten-run + record/assert + seven-checks review (keep/drop procedure — operationalizes Qase Q4), mutation matrix (ours), DORA.
- **J. Authenticity / provenance (is-the-work-theirs — mirror image of our axis):** Proctorio (Origin: AuthorProof writing verification explicitly WITHOUT AI detection + Behavior Tracker; Integrity: proctoring incl. secure interviews; Vault: leak mgmt).

## Matrix (T1+T2 full rows; T3 one-liners)

| Tool | Cluster | Trial / cost (sourced) | Popularity (sourced only) | Our verdict (1 line) | Pilot? |
|------|---------|------------------------|---------------------------|----------------------|--------|
| QAEverest (DevQAExpert) | C | vendor-shared access; commercial Stage 1 ~$2.5K proposal (not a price) | TBD | Locator-heal + per-risk-tier co-dev; B0 100% x2; decoy gap → vendor shipped passive layer (loop closed) | DONE, ongoing (commercial) |
| testRigor (Adam) | B | 14-day trial; enterprise custom (Gartner 2023 stale, ignore) | TBD | Text-match: M1 rename FAIL-plain/PASS-AI, M4 position-heal, M3 dup FAIL-honest, M2 trivial PASS | DONE (M5/M6 deferred) |
| Agentiqa = Vendor C (Radik) | A | Starter free 10 runs/mo; Pro $39; Company BYOK | npm 15K+ downloads Jun 2026, 219 versions | Plan quality: M1-M6 → 4 adapted, 2 killed-correct, 0 survived; flows yes, UI-root-cause no | DONE 8.1/10 (naming till OK) |
| DevAssure O2 (Badri/Santhosh/Divya) | D | trial EXPIRED; Starter $25/mo unlimited; SOC 2 | 9K LI followers, G2 listed | Article 15: 1 real critical + 4 self-artifact FPs (precision 20%); re-check queued (repeat + clean-PR) | QUEUED (trial/extension) |
| Autonoma | A | OSS (open since Apr 2026); trial: 3 runs $1.18–3.62 | TBD (stars unverified) | OrangeHRM trial: .md non-executable, no survival rate measured | LIGHT (matrix pending) |
| Mabl | A | enterprise custom ~$500–2000/mo (unofficial) | Gartner leader, 7+ yrs | T3: most mature AI-native, cloud-only, no self-host | WATCHLIST (no gap fit) |
| Testsigma | B+SAP/Desktop | Free → ~$299–999 Pro (unofficial) | 3000+ browsers claim | T3: widest platform incl. SAP; NLP lock-in | WATCHLIST |
| Panto AI | A-mobile | ~$999/mo Scale (unofficial) | TBD | T3: mobile-only, not Autonoma-competitor | NO (no mobile target) |
| Virtuoso | B | TBD | TBD | T3: composable/StepIQ claims | WATCHLIST |
| KaneAI / HyperExecute / SmartUI (TestMu) | B/E/F | 30-day trial claim (wiki, unverified); SEO-farm discount applies | TBD | T3: vendor claims only; SmartUI = visual-gap candidate if visual becomes priority | WATCHLIST (visual naked) |
| Applitools | F | TBD | established visual vendor | T3: visual diff, assertions-based | WATCHLIST (visual gap) |
| TestRail / Testomat | G | TestRail Cloud trial; AI credits | 10K+ teams claim (TestRail) | T3: management+AI-generate, human-gate built in | NO (we don't manage suites there) |
| Qase (Maksim Koutun, VP Eng) | G | Free tier $0 + 14-day Business trial no card; Startup $24 / Business $30 per user; MCP server; SOC2/ISO/GDPR | TBD | T3: TMS as shared quality layer for coding agents (MCP read/write, harness: gates/hooks/approvals, quality-graph roadmap mostly Planned). Thesis (verification bottleneck, deterministic gates, agent-written pass = claim until evidenced) aligns with ours. Evaluable without migration: MCP micro-probe on free tier (draft precision, dup-protection, scoping) | OPTIONAL micro-probe (free); peer angle strong |
| Testora-commercial | G | waitlist, $49+ | pre-launch | T3: test-gen quality measurable later (vs our 120 TEST_CASES) | WAITLIST (blocked on access) |
| Kiro | H | TBD | Amazon backing | NOT a QA tool: spec-driven dev agent; testing via specs | NO (category error to compare) |
| TestResults (Tobias Müller) | A-enterprise/business-user | quote-only (named users, cloud/on-prem/hybrid, guided onboarding — no self-serve visible) | Swiss DACH enterprise, G2 4.9/97% claim, 1M+ steps claim | T3: screen-understanding cross-platform (web→mainframe→PDF), business-user authoring, Business Risk Coverage metric. Thesis (confidence must be explainable, harness: fine-tune + lenses + repeatability) aligns with our verification work — peer/content angle > pilot angle | WATCHLIST (sales-led, no self-serve) |
| Klarent (fore ai) | A (+mobile iOS/Android) | NO self-serve visible (Book a Demo, founders cal.com); ISO 27001 + SOC 2 badges | MoTaCon 2026 presence; app.foreai.co login exists | T3: plain-English web+mobile, self-heal WITH human-review diff (gate built in — matches our doctrine), test-data mgmt, real devices. Closest to Agentiqa (URL→tests) + testRigor (NL) + Panto (mobile). Depth: real surface, demo-gated | WATCHLIST (demo-gated; pilot only on trial open or mobile-axis priority) |
| Playwright + playwright-cli | tooling | OSS free | industry standard | Recorder probe 2026-09-09: testid>role; M1 kills role-based (see recorder note) | TOOLING (not a subject) |
| Proctorio (authenticity pivot 2026) | J | sign-up exists, enterprise motion (contact sales); since 2013 | 300M+ exams claim | T3: Origin/AuthorProof (writing verification without AI detection — the testable claim: accuracy/FP on known authorship), secure interviews, Vault. Mirror image of our axis (they verify HUMAN authors, we verify AI testers) — article-grade, not pilot-grade | WATCHLIST (thesis note; pilot only if authorship-accuracy question becomes priority) |
| Testkube | E (+AI-eval gates) | OSS (kubeshop/testkube, GH 1.6K) + 30-day trial $0 no card | CNCF landscape | T3: K8s-native orchestration of DeepEval/Ragas as PR gates (faithfulness 0.80/recall 0.75/relevancy 0.80 — reference thresholds for our gate design) + baseline-vs-candidate prompt A/B (mutant analog!) + AI failure-analysis agents + MCP. Methodology overlap (thresholds-before-merge = Gulin rule), not an executor — complements pilots, doesn't compete | WATCHLIST (methodology import; pilot only if eval-orchestration becomes priority — needs k8s) |

## Cross-cluster comparability notes

- A↔D (Agentiqa vs DevAssure): same execution (browser agent), different trigger (URL vs diff) and failure mode (plan-quality vs FP-rate). Comparable via one matrix, different verdict axes.
- B↔C (testRigor vs QAEverest): flipped vulnerability (text vs locator) — the matrix flips accordingly. Strongest pair for contrast articles.
- F is the open gap: zero hands-on visual pilots. Fill only when an article needs the contrast.
- H must never enter vendor rankings (different job-to-be-done).

## Pilot queue (ordered)

1. DevAssure re-check (repeat → clean-PR) — blocked on trial/extension (Santhosh thread live).
2. Autonoma matrix (M-playbook on existing trial) — cheap, no vendor needed.
3. testRigor M5/M6 tail — deferred, low value.
4. Visual probe (SmartUI or Applitools) — only on article demand.
5. Testora test-gen precision/recall — blocked on waitlist.

## Pilot selection rule (2026-09-10 — no blanket evaluations)

Pilot ONLY if both hold: **(a) self-serve cheap** (trial without sales cycle, local or cloud target we control) AND **(b) our method has teeth** (executable output we can mutate, or countable claims: precision, heal rate, FP rate). Else: peer/content track only, no pilot.
- TM cores (TestRail/Testomat/Qase-management), grands (Mabl enterprise, BrowserStack), waitlists → content/peer, not pilots. Narrow evaluable surfaces (Qase MCP) are the exception, as micro-probes.
- Precedent: Notion AI (heavy + nothing to mutate → trial closed, reopen only on work encounter).


























<!-- backlinks-start -->
### Backlinks
- [Archestra Crab Bot Slack Agent 2026](wiki/archestra-crab-bot-slack-agent-2026.md)
- [Bach Everyone Not Responsible Quality 2026](wiki/bach-everyone-not-responsible-quality-2026.md)
- [Flowscout Akymenko Kanaris Thread 2026 09 22](wiki/flowscout-akymenko-kanaris-thread-2026-09-22.md)
- [Qodo Why Your Ai Coding Agent Shouldnt Review Its Own Code The Case For An Independent Verification Layer](wiki/qodo-why-your-ai-coding-agent-shouldnt-review-its-own-code-the-case-for-an-independent-verification-layer.md)
- [Qodo: AI Gave Teams Velocity – The Governance Harness Comes Next](wiki/qodo-ai-gave-teams-velocity-the-governance-harness-comes-next.md)
- [SOP‑Bench: Benchmarking AI Agents on Real‑World Business Procedures](wiki/amazon-science-sop-bench-agents-business-procedures-2026.md)
<!-- backlinks-end -->

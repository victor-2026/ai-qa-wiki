# Session Checkpoint — 2026-09-03 (Session 114)

## Pi + OpenCode Integration — Installed & Tested + Free-First Fixed

- **Pi installed:** `@earendil-works/pi-coding-agent` 0.84.4 (`npm install -g --ignore-scripts`, 136 pkgs) + `pi-subagents` 0.64.0 (`pi install npm:pi-subagents`, 5 pkgs, `~/.pi/agent/settings.json: packages=[pi-subagents]`)
- **Tested:** `pi --provider openrouter --model openrouter/deepseek/deepseek-v4-flash --print "Use reviewer..."` on `app.js` diff (`add +→-` + export removed) → **2×P0 BLOCK** (logic inversion + missing export); parallel `correctness/tests/complexity` → **3/3 BLOCK** synthesis — works.
- **OpenCode Desktop:** 1.18.27 installed (was 1.18.19) — `opencode upgrade` 1.18.19→1.18.27, verified `opencode --version 1.18.27`, `pi 0.84.4`, `pi list`
- **OpenRouter free-first fixed (global + 7 projects):**
  - `~/.pi/agent/settings.json` now: `defaultProvider: openrouter`, `defaultModel: openrouter/free`, `enabledModels: [openrouter/*:free, openrouter/*, groq/*, openai/*]`, retry 3
  - Free limits: 20 RPM, 1000/day (≥$10 lifetime, else 50/day) — 18 free models (nemotron/gemma/glm etc.), `openrouter/free` auto-router, 429 → fallback to paid without `:free`, concurrency 1-2
  - 7 `AGENTS.md` updated (`ai-qa-wiki`, `Articles`, `DYI-Building`, `MAS-realisation`, `OrangeHRM`, `Test-Dora-Plus`, `qa-automation-sandbox`) — added `## Subagents & OpenRouter — Free First (Global)` (5 KiB, <32 KiB, 77-279 lines) with rule + example `pi --provider openrouter --model openrouter/free --print`
  - Decision: global `~/.pi` is source of truth for Pi; `AGENTS.md` documents for team/OpenCode portability (no per-project `.pi/settings.json` needed)
- **Wiki:** `wiki/ruvnet-agentic-stack-2026.md:1` — 92 lines (11.3k followers, 214 repos, 172k stars, 64M npm/yr, Ruflo 67k, RuView 89k) — harness-not-model thesis
- **Wiki:** `wiki/pi-subagents-2026.md:1` — 93 lines, 6 agents (scout/researcher/worker/reviewer/oracle/delegate), council/parallel/fleet, `maxSubagentSpawnsPerRun=64`
- **Wiki:** `wiki/pi-opencode-integration-2026.md:1` — 117 lines, 3 layers (AGENTS.md / MCP / CLI as subagent), loop `scout(Pi)→worker(OpenCode)→reviewer(Pi)`, MCP proxy Zalando pattern
- **Raw:** `raw/ruvnet-overview-2026.md`, `raw/pi-subagents-2026.md` created
- wiki-topics.json: 292 → 295 (+3: ruvnet, pi-subagents, pi-opencode), raw 178 → 180

## Next
- Use Pi via Desktop: chat → `Use reviewer to review this diff` / `Run parallel reviewers...` / `Ask oracle...` — OpenCode delegates via bash `pi --print`
- Autonoma pending 16 HIGH — on demand; testRigor TOP25 detailed — on demand
- Article 21/27 bodies

---

# Session Checkpoint — 2026-09-03 (Session 113)

## Catalogs Bulk — Post-31.08 Continuation (Build Mode, 12 catalogs now)

- **TesterStories (Jeff Nyman):** `wiki/testerstories-blog-catalog-all-publications-2026.md:1` — 113 lines, ~150+ articles, AI ~40 / AI and Testing ~40 (Feb-Apr 2026, 20+ posts). TOP 15 HIGH: Evaluation Synthesis, Conversations, Recall/Relevancy, Faithfulness, Contextual Precision, Improving Retrieval Quality p1-4, Local Models, Model Pipelines, Knowledge Graphs & Ontologies, DSPy (Declaring/Pipelines/RAG), Causality trio (Hallucinates / Performs / Performing Experience). Category Breakdown 6 rows, tiers HIGH ~35/23%.
- **Virtuoso QA:** `wiki/virtuoso-blog-catalog-all-publications-2026.md:1` — 95 lines, ~200 articles (33 pages ×6), TOP 12 HIGH: Composable (Doughty 80% cost), Agentic vs Agents, StepIQ, Regulated AI Code, Journey Confidence + Latest 10 Best AI Tools, Flaky, User Journey, AdHoc vs Exploratory, Behavioural. Breakdown 7 rows, HIGH ~41/20%.
- **Quality Remarks (Keith Klain):** `wiki/qualityremarks-blog-catalog-all-publications-2026.md:1` — 93 lines, ~170 posts (sitemap 170, lastmod 2026-08-24). TOP 12 HIGH: Testing Mindset, Verification Asymmetry, Confidence Game, Speed of Stupid, Great Liberation I-III, EU AI Act, etc. Alias `?utm_source=softwaretestingweekly` → same as `wiki/keith-klain-testing-mindset-after-all-2026.md:1` (92 lines, alias added).
- **Postman Blog:** `wiki/postman-blog-catalog-all-publications-2026.md:1` — 110 lines, ~1,127 articles (post-sitemap 992+135, 2026-08-31). TOP 15 HIGH: QE Platform series (Structural Problem + 5 Metrics + 3 Paths—Rick Crawford), AI Agents (Orbit, three-way drift, context graphs, Postman.ai, Passport), Governance. Alias `?utm_source=softwaretestingweekly` noted in `wiki/rick-crawford-qe-structural-problem-2026.md:1`.
- **Julia Pottinger:** `wiki/juliapottinger-blog-catalog-all-publications-2026.md:1` — 96 lines, 46 articles, TOP 15 HIGH: Who Is Accountable, QA Control Layer, 6 Checks, Review AI Tests, Working With Agents, Agentic Testing, MCPs, Using AI to Generate Tests, Flaky Tests, Playwright vs Cypress 2026 etc.; + detailed `wiki/julia-pottinger-who-validates-ai-generated-code-2026.md:1` — 139 lines, RACI + 5-question sign-off + PR block `## AI-assisted change` (alias who-validates → Who Is Accountable, Weekly #325).
- **Martin Fowler:** `wiki/martinfowler-blog-catalog-all-publications-2026.md:1` — 125 lines, ~600+ articles (feed 100, /testing guide 45), TOP 15 HIGH: Making Data Ready for Agentic AI (27.08.2026) + Accidental Blackboard, Code Review (Rachel Laycock), TDD in agent loop, Building Reliable Agentic Systems, Conductor, DSLs, test suite as regression sensor, Pyramid/Practical Pyramid, Mocks etc.; + detailed `wiki/martinfowler-making-data-ready-agentic-ai-2026.md:1` — 91 lines, 5 attributes (Trusted/Contextual/Traceable/Governed/Operational) + 4 layers (Data Contracts/Quarantine/Medallion+Adaptive Gold / Traceability+EU Act €15M / Context Layer domain+semantic+capability / Searchable→Actionable via MCP) + raw `raw/martinfowler-making-data-ready-agentic-ai-2026.md`.
- **TestMu AI:** `wiki/testmuai-blog-catalog-all-publications-2026.md:1` — 114 lines, ~2,380 /blog/ (sitemap-blog.xml 2380), TOP 20 HIGH: Agentic Regression, Video Agent Testing, Agent Assurance, Agent CLI, Orchestration, Verification Agent, etc.; + detailed `wiki/testmuai-agentic-regression-testing-2026.md:1` — 133 lines, 4-level ladder (Advisory/Selective/Self-repairing/Autonomous), 3 decisions (selection/ordering/maintenance), recall metric Facebook 99.9%, TDAD 6.08%→1.82% with impact map, 4300ms→2050ms demo + raw `raw/testmuai-agentic-regression-testing-2026.md:46`.
- **Zalando:** `raw/zalando-agentic-engineering-snapshot-2026.md` created (1466 lines → raw now), wiki `zalando-agentic-engineering-snapshot-2026.md:1` already (43 lines) — summary provided. CCN inflection clarified (Cyclomatic Complexity per commit, 4 codebases, agents amplify).
- **DevQAExpert (Rupesh/QAEverest):** `wiki/devqaexpert-blog-catalog-all-publications-2026.md:1` — 86 lines evaluation only ( ~50-56 articles, 14 pages), sampled 4 (90× pipeline anecdote, Friend, API future, Magical) — signal/noise ~5%, decision NOT to build full catalog; lightweight evaluation kept.
- **Software Testing Weekly #325 — TOP 5 summaries:** 5 wiki 90-96 lines (`keith-klain-testing-mindset-91`, `rick-crawford-qe-structural-95`, `julia-pottinger-accountable-90`, `anton-gulin-regression-suite-museum-96`, `test-rocket-pyramid-ai-era-92`) + newsletter `wiki/software-testing-weekly-newsletter-2026.md:79` added `## Саммари TOP 5` with `[→ wiki]` + `[оригинал]`.
- **EventHorizon Showcase:** `https://christosgkovaris.github.io/EventHorizon-Showcase/` evaluated — Flask/C++ observability, competitors (Grafana Loki/SigNoz/ELK/Datadog), not prod-ready → not for monitoring, pet-project only.

## Stats (since 2026-08-31 checkpoint)
- wiki-topics.json: 267 → 292 (+25: testerstories + virtuoso + qualityremarks + postman + julia catalog + who-validates + martinfowler catalog + making-data-ready + testmuai catalog + agentic-regression + weekly 5 etc.), raw_count 162 → 178 (+16 raw), wiki *.md 292 files
- Verified: JSON valid, wc -l checks, html topics 291-292, raw md counts

## Next
- Autonoma pending 16 HIGH (Prompt Injection 2 + Mutation 8 + Chatbot 6) — on demand
- testRigor TOP25 detailed wiki — on demand (catalog ready 125 lines)
- Article 21/27 bodies (Ng/Krivitsky/Bolton/Bach anchored)
- Rupesh: wait fragility layer live → call; Megi pilot

---

# Session Checkpoint — 2026-08-31 (Session 112)

## Yampolskiy / Mogilko — Silicon Valley Girl (20.04.2026, 44 min, 1388 segments)
- `raw/mogilko-yampolskiy-35-ai-employees-2026.md` — LinkedIn post (full) + podcast descriptions (Apple/Spotify/Castbox) + 5 related interviews + **YouTube https://www.youtube.com/watch?v=00RHph_eok4** + **full transcript** (1466 lines, youtube-transcript-api 1.2.4, 1388 segments)
- `wiki/ai-agents-replace-team-entrepreneurs-mogilko-yampolskiy-2026.md` — Key thesis 35 agents, 3 structural advantages, Yampolskiy safety context, **8 key quotes** (80% fire 4/5, tools vs superintelligence, networks vs code, scarcity, cognitive gap humans vs squirrels, regulation impossibility, brand speed), networks unpacked (personal moat vs team infra vs why AI tools can't copy, paradox), **QA implications 8 rows** (expanded from 3)
- wiki-topics.json: 237 → 238 (Mogilko) → later 267 total

## Kiro Blog Catalog — 9 Wiki + Expanded Top 10 Block
- `raw/kiro-*.md` 9 files (continuous-prompt-evaluation, diagnostics-over-time, property-based-testing-security-bug, openapi-to-testsuite, bug-fix-paradox, root-cause-33s, soc2-planview-automation, snyk-guardrails, trust-agent-triage) via webfetch + pandoc (34-40K each)
- `wiki/kiro-*.md` 9 files (91,101,93,94,91,90,94,94,90 lines, EN, 90-120 target):
  - `kiro-continuous-prompt-evaluation-llm-judges-2026.md` — 4-stage Diagn/Design/Test/Evaluate, 15 dims, CLI -32% behavioral
  - `kiro-diagnostics-over-time-agent-quality-2026.md` — 1.5M convos, 406K invocations, Java 26.7% vs Python 4%
  - `kiro-property-based-testing-security-bug-2026.md` — fast-check trial #75 __proto__, Object.create(null)
  - `kiro-openapi-to-testsuite-2026.md` — spec→suite, mock+live toggle, headless CI
  - `kiro-bug-fix-paradox-2026.md` — C/P partition, fix vs preservation
  - `kiro-root-cause-33s-2026.md` — 33s RCA, 10 turns, 30m→1m
  - `kiro-soc2-planview-automation-2026.md` — custom soc2-compliance agent, 40h saved
  - `kiro-snyk-guardrails-2026.md` — MCP, AIBOM, toxic flow, hooks
  - `kiro-trust-agent-triage-2026.md` — 13m35s, 96.9% reads, 107 skills
- `wiki/kiro-blog-catalog-all-publications-2025-2026.md:181` — flat Top 10 → expanded 10 blocks (60-90w QA summaries + dual links wiki/original)
- wiki-topics.json: 237 → 246 (+9 Kiro), raw_count 133→142

## Autonoma Blog Catalog — 20 Wiki + Catalog Tables with Саммари Column
- `raw/autonoma-*.md` 20 files via `getautonoma.com/md/blog/<slug>` (Accept: text/markdown, 127-192 lines each, Task batches 4×5)
- `wiki/autonoma-*.md` 20 files (90-100 lines, EN, Task batches 4×5):
  - Agent Testing 1-10: tool-calls, e2e, multi-agent handoffs, memory, reliability, regression, langgraph, crewai, simulation, multi-turn
  - Fundamentals 21-25: non-deterministic outputs, llm-unit-testing, llm-evals-cicd, qa-ai-feature, streaming
  - RAG 36-40: rag-pipeline (two surfaces), rag-evaluation-metrics (4 metrics), rag-retrieval (MRR), hallucinations (code-first), mcp-server (3 layers)
- `wiki/autonoma-blog-catalog-all-publications-2026.md:19-66` — 6 tables added column `Саммари`; TOP 20 HIGH rows filled with 1-line QA summaries + `[→ wiki]`; other HIGH (Prompt Injection 2, Mutation 8, Chatbot 6) marked `_(wiki pending)_` / `—` for MEDIUM
- wiki-topics.json: 246 → 266 (+20 Autonoma), raw_count 142→162

## testRigor Blog Catalog — New Catalog Page
- `wiki/testrigor-blog-catalog-all-publications-2026.md` — 125 lines, analogous to Kiro/Autonoma
  - Source ~3,013 articles (post-sitemap 1001+1000+684+328 filtered to /blog/, pagination /blog/page/483 ≈ 2,898 cross-check), last updated 2026-08-31
  - Sampling: /blog/ p1-2 + /category/ai-in-testing/ (12 pages ~120) + /category/generative-ai/ (2 pages ~20)
  - TOP 25 Must-Read (4 tables: AI & Agentic 10, Prompt/GenAI 5, Codeless/Self-Healing 5, Test Strategy 5) — HIGH for QA/QE (plain-English, self-healing, prompt versioning/regression, Claude Code, ATDD/TPDD, coverage vs priority)
  - Category Breakdown (15 rows, est. counts) + Summary Statistics (HIGH ~165 /5%, MEDIUM ~400 /13%, LOW ~2448 /81%)
  - Strengths: largest codeless/GAI library, ERP/CRM coverage; Gaps: SEO-heavy, signal/noise ~5%, product-led vs harness-level
- wiki-topics.json: 266 → 267 (+1 testRigor), raw_count 162

## Stats
- wiki-topics.json: 237 → 267 (+30: 1 Mogilko +9 Kiro +20 Autonoma +1 testRigor), raw_count 133→162, wiki 243 files
- Verified: JSON valid, wc -l checks, 20 wiki links in Autonoma catalog, 10 in Kiro catalog

## Next
- Autonoma pending 16 HIGH (Prompt Injection 2 + Mutation 8 + Chatbot 6) — can generate wiki on `делай` (2 batches)
- Article 21 publish 31.08 10:00 (done? check)
- Article 27 body (Ng/Krivitsky/Bolton/Bach anchored)
- Rupesh: wait fragility layer live → call; Megi pilot; testRigor raw sampling for full wiki if needed

---

# Session Checkpoint — 2026-08-29 (Session 109)

## Mutation Matrix — Lite + Full production-ready
- `outputs/mutation-matrix-lite.md` — final polish (how-it-works bullets, checklist, EN, quick pilot checklist)
- `outputs/mutation-matrix-full.md` + `mutation-matrix-template.md` — final polish (expected-to-catch checklist, 6 verdict values, assertion quality Low-priority, audit Status values, Step 3 demo unified with Appendix scenarios)
- `outputs/mutation-set-login (rus/eng).md`, `mutation-set-payments (rus/eng).md`, `mutation-set-calculations (rus/eng).md`, `mutation-set-combined (rus/eng).md` — separate scenario templates for Megi pilot
- Формулы survival/FP в code-block (GitHub/Notion portable)

## Ingestion (wiki)
- `raw/michael-bolton-systems-thinking-constraints-2026.md` + `wiki/...` — systems thinking, perturb-the-system, «bottles have necks»
- `raw/prachi-dahibhate-james-bach-rst-2026.md` + `wiki/...` — James Bach / RST, magic testing box, Productivity Paradox, Testing vs Checking
- Cross-links: AI Productivity Paradox ← Bolton; Article 27 ← Bolton metaphor + Bach/RST
- wiki-topics.json: 219 → 221

## Articles
- `27-guided-qa-engineer.md` — скелет статьи 27 (Guided QA Engineer), threads: QA-as-gatekeeper, QA-as-supervisor, Karpathy «manifesting», Bolton metaphor, Bach Testing-vs-Checking
- `21-conways-law-qa.md` — добавлен inline-маркер `<!-- FEED IMAGE: 21-org-drift.png -->` в секцию drift; Bolton-цитату НЕ добавляли (не перегружать)

## Outreach
- Megi Tephnadze: PDF (Lite+Login) готов к отправке, каталог `outreach/active/Megi_Tephnadze/index.md` обновлён (sent 28.08)

## Next
- CARBON (testers.ai): ОТЛОЖЕН
- Article 27: дописать тело (после CARBON или параллельно)
- Article 21: публикация 31.08 10:00 (см. Articles/session-checkpoint.md)
- Ждать ответы: Rupesh (consulting), Max Kitaygora, X-FLOW (Tatsiana), HYPERHUG (founders)

---

# Session Checkpoint — 2026-08-27 (Session 107)

## Wiki updates
### Новые страницы
1. `wiki/google-kaggle-agent-skills-whitepaper-2026.md` — SKILL.md format, 98% context reduction, trajectory testing, context-rot testing
2. `wiki/ruslan-desyatnikov-qa-director-elimination-virus-2026.md` — QA leadership elimination warning
3. `wiki/loris-bartolini-jean-yves-garcin-banking-rag-adversarial-testing-2026.md` — adversarial testing catches what fidelity metrics miss
4. `wiki/ai-dlc-process-testing-guardrails-2026.md` — AI-DLC process testing, dual-agent verification, mutation testing as quality gate
5. `wiki/modeloptimizingagainstqualitygateinsteadofactualproblem.md` — quality gate rot, external verifier

### Cross-links
- ai-dlc → mutation-matrix, qaeverest-pilot, agent-skills, testing-ai-evidence, ai-qa-evidence-layer, desyatnikov, bartolini, zagirov
- wiki-topics.json: 213 → 217

## Outreach updates
- **Rupesh Kabra:** consulting methodology sent (mutation matrix + trajectory audit + scorecard). Reply: "I will get back to you." Mutation results M6-M9 sent (2/4 caught, 2/4 missed). Pattern: functional failures caught, structural fragility missed.
- **Tatsiana (X-FLOW):** "Как только будут новости от наших ребят" — waiting
- **Max Kitaygora:** peer exchange on AI review noise ratio, CloudFront race condition case
- **Yasin Aktepe:** hold — no current opening, keep warm
- **HYPERHUG:** hold — waiting for CEO/CTO connection replies
- **Radik Zagirov (Agentiqa):** wiki ingested, catalog created

## QAEverest mutations M6-M9 (2026-08-27)
| Mut | What | Result | Finding |
|-----|------|--------|---------|
| M6 | id loginBtn → login-button | 5/5 PASSED | Locator drift not detected |
| M7 | Remove id, bare button | 5/5 PASSED | Selector broadening not detected |
| M8 | Delete button | 3/5 FAILED | Correct - caught |
| M9 | Swap buttons | 3/5 FAILED | Correct - caught, risk 42.9% |

**Pattern:** Functional failures (missing/wrong element) → caught. Structural changes (id drift, selector broadening) → missed.

## Daily digest
- Fixed dedup: current day excluded from lookback, dedup moved before top_n
- Re-generated: 12 items from 492, 3 excluded by dedup, Groq gpt-oss-120b working

## Next
- Wait for Rupesh reply on consulting model (5-7 days)
- HYPERHUG: wait for founder replies
- X-FLOW: wait for Tatsiana's team
- Series 21: feed image published, carousel next
- Article 26: mutation-matrix data ready (M6-M9), can finalize

---

# Session Checkpoint — 2026-08-28 (Session 108)

## Wiki updates
### Новые страницы
1. `wiki/aiengineeringskillsmap-softwareengineeringfundamentals.md` — Andrew Ng AI Engineering Skills Map (software fundamentals, full-stack, data, architecture, security, scaling)
2. `wiki/ai-dlc-process-testing-guardrails-2026.md` — cross-linked (added earlier)

### CARBON plan
- `outputs/carbon-adoption-plan.md` — план апробации testers.ai CARBON
- Вопросы: caught bugs vs FP, persona feedback, mutation testing integration, $79/mo value

### Cross-links
- aiengineeringskillsmap → ai-dlc, mutation-matrix, agent-skills, testing-ai-evidence
- wiki-topics.json: 218 → 219

## Social/Outreach
- **Megi Tephnadze** (Head of QA, ProCredit Bank Georgia): connected, peer exchange on AI verification + governance. She runs pilot: AI executes + QA review, risk-based human gate. Mutation testing interested her as independent signal.
- **Sayeed S** (Jason Arbon post): replied with mutation testing angle (code access enables mutation check, 70% could run, most don't)
- **Jason Arbon post** comments reviewed: Anton Gulin (code-level checks), Jay Aigner (validation surface vs truth), Himanshu Soni (skill gap), Sarah McKenna (agent-friendly software)

## Daily digest
- 2026-08-28 generated: 12/459, OpenAI rogue incident top

## Next
- CARBON: decide URL for free sample (sandbox vs buzzhive vs public)
- Series 21: carousel next
- Max Kitaygora / Rupesh: waiting for replies

---

# Session Checkpoint — 2026-08-29 (Session 109 continued / 110)

## Wiki ingests (3 new pages, commits 03c4747 + d00510e + 37f76eb)
1. `wiki/andrew-ng-loop-engineering-2026.md` — 3 nested loops (agentic coding / engineering / developer-feedback); evals = mutation matrix; developer was QA, now moves up = Article 27 proof
2. `wiki/krivitsky-agentic-factory-nested-loops-2026.md` — Coding/Feature/Impact loops; outer loop = human-owned (Article 21 accountability + Article 27 gatekeeper); Ferrari Trap = Article 20 false-discovery
3. `wiki/andrew-ng-openworker-security-agents-2026.md` — open-source harness = auditable (Article 26); model+harness split = verification-layer architecture; shift-left
- Cross-links added: Skills Map "See also" → all 3; Article 27 → Ng loop + Krivitsky; mutation-matrix → Vendor adoption v2
- wiki-topics.json: 221 → 224

## QAEverest / Rupesh Kabra (vendor adoption v2)
- Rupesh sent **Suite Trust Scorecard** concept: Suite Sensitivity 78% (14/18 mutants caught), Fragility Index 4/31, "0 weakened selectors open" — mutation matrix PRODUCTIZED
- Victor replied (sent): recognized method productized, 3 methodology questions (survived vs observed-only; mutation-score threshold; fragility→fix), claimed attestation role
- Sample report PDF read: 100% pass / 0% risk but 5 passive findings (js-error, 500 retry, duplicate sign-in CONFIRMED, fragility id→position) — M6/M7 now caught
- Catalog: `outreach/active/Rupesh_Kabra/index.md` updated (status 🟢 Vendor adoption v2, reply sent)
- Wiki: mutation-matrix "Vendor adoption v2" added

## Next
- Rupesh: wait for reliability layer live → schedule call (attestation)
- CARBON (testers.ai): ОТЛОЖЕН
- Article 27 body: write (Ng + Krivitsky + Bolton + Bach anchored)
- Article 21: publish 31.08 10:00

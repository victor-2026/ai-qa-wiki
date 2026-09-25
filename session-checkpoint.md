# Session Checkpoint — 2026-09-07 (Product concept update; recovered checkpoint)

## Окно «Продукт+Мутации» умерло — чекпоинт записан из соседнего окна
- Причина: в исходном окне provider отвечает `Upstream request failed: [invalid_request_error]` на любой запрос (включая чекпоинт) — сессия невосстановима, окно можно закрывать. Потерь нет: все артефакты на диске.
- **Экспорт сессии сделан:** `session-archive/2026-09-07_product-mutations_ses_109d6cbf.json` (13.7 MB, 1390 сообщений, валидный JSON) — полная история окна, если понадобится дословно. Оживить через `opencode import <файл>`.
- Как продолжать: открыть новое окно, указать ему `outputs/product-concept-mutation-verifier-mvp.md` + этот чекпоинт — контекст восстановится без старой истории.

## Product concept (`outputs/product-concept-mutation-verifier-mvp.md`, правки 07.09)
- **§5 Рамки:** вшито требование из переписки с Aamir (07.09) — три сигнала раздельно, не схлопывать (ranking vs mutation vs drift).
- **§6 Ограничения:** версионирование скорера обязательно (урок свопа #3↔#4 на 0.2.34→0.2.40, OrangeHRM); tier-2 дефолт открыт (band ≤5% vs vendor 1/60).
- **§11 Этапы:** Pilot ✅ done 2026-09-03/07 (внешняя валидация Aamir: снапшот→реран протокол); Articles 🔄 draft; MVP ⏳ после статей; правило перехода — MVP кодим только при ≥3 внешних вопросах «а как посчитать самим?».
- **§12 Название:** 8 вариантов, рекомендация **MutGate** + артефакт `verdict.md`, запасной KillRate.
- **§Вопросы (5):** п.4 частично закрыт письмом Rupesh 04.09 (strict-0 для B0/B1 подтвержден; Medium открыт). Остальные открыты: MVP после статей или параллельно? Python vs Node? Название? Новый репо сейчас или после сигнала?

## Next
- Обсудить 5 вопросов из концепта (Articles 26/27 идут первыми — MVP только после них).
- Новое окно для продукта открывать с нуля, со ссылкой на этот файл.

---

# Session Checkpoint — 2026-09-05 (Rupesh catalogs + Product Q4)

## Rupesh correspondence → messages/ + emails/
- `messages/` — 10 датированных файлов 20.08–02.09 (все 36 ходов, сверено поштучно); починены границы 31.08/01.09, файл 03 переименован в спан 22–25. Raw-дамп — архив.
- `emails/` — Letter 1 SENT 03.09, письмо Rupesh 04.09 RECEIVED (сохранено впервые), Letter 2 DRAFT, paid-stage SUPERSEDED + оба INDEX.
- Фреймворк уже содержал правки 09:31 (проверено, править нечего).

## Product Q4 (tier-2 default) — частичный ответ письмом 04.09
- Да: strict-0 для B0/B1 без исключений (no decision проходит zero-tolerance; no-op = seeder defect) — зафиксировано в концепте.
- Нет: Medium-дефолт (≤5% vs 1/60) и числовой score-threshold — открыты.
- Next: deploy-confirm → re-run 2/2 → Letter 2.

## Next
- Обсудить product concept (5 вопросов, завтра); Aamir ждет; testRigor М5.

---

# Session Checkpoint — 2026-09-05 (wiki root reorg)

## Дедупликация корня wiki + README-навигация
- **Слито 4 пары дублей** (уникальное перенесено в канонические файлы, дубли удалены, ссылки починены):
  - `ai-in-qa-issue-17-butch-mayhew-2026-07-06.md` → в `ai-in-qa-issue-17-butch-mayhew-2026.md` (забран чек-лист Practical Applications, 6 пунктов)
  - `alex-barady-9-concepts-ai-builder-2026.md` → в `alex-barady-ai-builder-9-concepts-2026.md` (забрана таблица Practical Applications by Area)
  - `keithklain-testingmindsetafterall-2026.md` → в `keith-klain-testing-mindset-after-all-2026.md` (уже покрыто)
  - `mutationtestingplaywrightfront-end.md` (стаб 34 строки) → в `Mutation-testing-advanced-playwright.md` (секция FOM/HOM + Nightly Segmentation; файл 486 строк, в лимите)
- **Починено ~20 ссылок** в 11 файлах + 4 записи `wiki-topics.json`; raw/ не тронут (immutable).
- **Новое:** `wiki/README.md` — хаб-навигация по корню (Start here, 8 разделов, конвенции против дублей).
- Плоская структура оставлена сознательно: переезд 300 файлов по папкам порвал бы сотни `[[wiki/...]]`-ссылок.
- **Индекс:** `wiki-topics.json` → 300 topics (ресинк через `wiki_llm.py --update-index`, удалённые не вернулись). Без git-push (по умолчанию).

---

# Session Checkpoint — 2026-09-05 01:44 UTC (night of 04.09)

## Rotation-without-relevance wiki + глоссарий мутаций
- **Новое:** `wiki/rotation-without-relevance-preseed-mutant-filtering-2026.md` — маппинг нашего термина на классику: equivalent/low-utility mutants + unselective operators; 7 внешних опор (Google Practical Mutation Testing at Scale arXiv:2102.11378 — прямой прецедент pre-seed фильтра; Wikipedia RIP/equivalent/subsumed; selective/sufficient operators; Cerebro/TCE; ML pre-filter); выводы для gate (P0-1 baseline-green, P0-2 split Not-seeded, Decision-тип gap, логирование assertion kinds). Связано с fault-injection ревью.
- **Индекс:** `wiki-topics.json` → 301 topics. Без git-push (по умолчанию).
- **Глоссарий:** `wiki/ai-testing-glossary.md` + mutation-термины EN→RU (Arid nodes, Assertion scope, Assessor, Attribution, Baseline green gate, Decision log/mutation, Equivalent mutant, Evidence pack, FOM/HOM, Killed/Survived, Mutant, Mutation adequacy/density/operator/survivability, Not seeded, Observed-only, Open finding, Operator allowlist, Redundant/RIP/Rotation, Seed set, Selective/Statement/Strong/Subsumed/Sufficient, TCE/Targeted/Tooling gap, Value/Weak mutation). Без «ё», только дефисы (M5).
- Объяснение выводов для gate «как школьнику» дано в чате (аналогии: сигнализация, контрольная с опечаткой, замок, дневник).

## Next
- P0-1/P0-2 — отдельным блоком на согласование Rupesh (файл `per-risk-tier-framework-review-fault-injection-P0-P1-2026-09-04.md` уже в каталоге Rupesh), не вносить в v0.3 до согласия.

---

# Session Checkpoint — 2026-09-04 (Session 116)

## Ng Skills Map Series + Glossary + Product Concept (Build Mode, обсудим завтра)

- **Ng series (4 статьи, все полные тексты):** (1) Map m479c 14.08 (10k вакансий, 4 скилла) → raw `AI Engineering Skills Map - The Map.md`; (2) Building/Deploying gyn5e 21.08 (6 поднавыков, eval-driven development = главный trait) → raw `AI Engineering Skills Map - Building and Deploying.md`; (3) Fundamentals 7lnac 28.08 — уже был (проверено, дубль не делали); (4) Coding agents h8yxc 04.09 → raw 61 строка + wiki `andrew-ng-coding-agents-skills-map-2026.md:1` 94 строки (workflow Plan→Execute→Deploy, 5 навыков, open agents OpenCode/Pi у Ng, маппинг на Pi-loop, Worked Example + Checklist)
- **Articles 26/27:** в конец обеих добавлено `## Примечание (обсудить)` — ссылка gyn5e (eval-driven development = mutation matrix + evidence layer, цитата для 26/27)
- **Глоссарий:** `wiki/ai-testing-glossary.md` +45 терминов сессии (104 всего) → превысил 500 (559) → разбит: A–M 356 строк + новый `wiki/ai-testing-glossary-n-z.md` 224 строки (N–Z, O перед P поправлено, кросс-ссылки)
- **Product concept:** `outputs/product-concept-mutation-verifier-mvp.md:1` — PRD MVP по формату weekly-time-planner (Концепция/Цель/Почему не X/Функции v0/Рамки/Ограничения/Архитектура Python stdlib/Поток/Оценка 8-11ч/Слабое место/Этапы Pilot✅→Articles🔄→MVP⏳/8 названий, рекомендован **MutGate** + `verdict.md`); 5 вопросов на завтра (после статей или параллельно? Python vs Node? название? порог tier-2? скелет репо сейчас или после сигнала?)
- wiki-topics.json: 300 → 303 (+3: ng-coding-agents + 2 raw серии), raw_count 184 → 188

## Next (завтра)
- Обсудить product concept (5 вопросов из файла)
- Aamir: ждать ответа на delta (plain text отправлен)
- testRigor М5 на localhost:8080; Autonoma 16 HIGH — on demand

---

# Session Checkpoint — 2026-09-03 (Session 115)

## Pi Image Generation + Aamir Siddiqui Posts + OrangePro Pilots (Build Mode)

- **Pi Image Generation:** `wiki/pi-image-generation-2026.md:1` — 94 lines, OpenRouter 424 models (18 :free), pricing 1024×1024: gemini-3.1-flash-image $0.002-0.003 / flux-1.1-pro $0.055 / stable-diffusion-xl $0.02, no :free for images (paid counts to 1$/день), Pi worker via bash curl → /tmp/out.png → read inline (terminal.showImages:true) or path; prompt `Ask worker to generate image via openrouter model google/gemini-3.1-flash-image ... save to outputs/cover.png`; raw `raw/pi-image-generation-2026.md:1`; wiki-topics 295→298
- **Aamir Siddiqui (OrangePro):** `outreach/active/Aamir_Siddiqui/index.md:1` (profile, thesis, relevance ★★★★★, status) + `outreach/active/Aamir_Siddiqui/posts.md:1` — 14 posts scraped (20 loaded, 3d-5mo), 8 HIGH summarized (★ #2 same model writes code/tests/review ×3, #3 9→11→8 stochastic slot-machine, #5 Mattermost 38K 8600 methods 2% evidence editors.AddAttributeButton, #6 Fable vs OrangePro Twenty CRM 4,849 0 overlap, #8 behavioral graph 4 tiers mutation proven `npx -y @orangepro/mcp-server@latest start .`); table TL;DR + all 14 with metrics (4,725 PRs/mo 70% agents, 30 commits/6w etc.); draft connect fixed (generic, без QAEverest, #2/#6 → названия, не номера) — `followup-delta.md:1` with 122/108 delta
- **OrangePro 8600 methods analogy explained:** Mattermost 8600 public methods, 212 with evidence 2% → delta +195 behaviors, 1 new blind spot; vs qaeverset-pilot-mini 5 tests — same risk-profiling problem, coverage % hides which
- **Pilots (clones, не трогая оригиналы, детерминирован, static без выполнения где возможно):**
  - `qaeverset-pilot-mini-orangepro-compare` (9 файлов, app/index.html): `requirements.csv` fixed `behavior_name` (было id,title → теперь behavior_name,acceptance_criteria) → `behavior_anchors 6, score 54 usable` (было 0/16 thin); M6 drift `loginBtn→login-button` (1 строка), M7 bare `id` removed, M8 delete button, M9 swap loginBtn↔promoBtn, M5 reorder username↔password, M6 repeat — все `gaps 5 × No test evidence linked`, `denominator 5`, static, без Docker/тестов; `demo-math.js#add` Proven 670ms via `opro prove --runner vitest` (baseline 0→mutant 1, 0$, within 0.5$)
  - `OrangeHRM-orangepro-compare` (299M, 496 files) — `opro start . --no-ai` → 122 behaviors (pom/AdminPage.addEducation etc., k6/load-test.js#mainFlow, ClaimPage), 108 no signal, 14 candidate, 0 Proven (needs BYOK for auto-prove), 5 top attempts ClaimPage.getHeading etc. unrunnable (equivalent mutant); `gaps` 5× REQ-md-* No test evidence; `score 54 usable` after requirements.csv
- **Limits tightened (build mode, free-first):** `~/.pi/agent/scripts/openrouter-guard.sh` FIXED_LIMIT 1.0$/день (было 2$), SESSION_LIMIT 0.5$/сессию, WARN 0.75$, launchd 600s, `openrouter-guard.log`; `~/.pi/agent/settings.json` maxSubagentSpawnsPerRun 64→3, thinking medium 4096, compaction 8192/10000 for paid intensity; 7× AGENTS.md updated with `Интенсивность платного режима` bullet; dashboard still 3$ → надо вручную `https://openrouter.ai/keys → Limit 1` (PATCH 404, is_management false)
- **OpenRouter spend:** checked `GET /api/v1/credits` total 25 / usage 12.42, `GET /api/v1/key` limit 3, usage_daily 0.05, remaining 2.94 — guard now 1$/0.5$; parallel safe 2-3 (20 RPM / 1000д shared), 3 parallel reviewers tested OK

## Stats (since Session 114)
- wiki-topics.json: 295 → 298 (+3: pi-image-generation + Aamir posts? actually wiki 292→295→298), raw 180 → 183 (+3 raw: pi-image, ruvnet, pi-subagents), wiki *.md 292→295 files
- Verified: JSON valid, wc -l, html topics, raw md counts

## Next
- Aamir: ждать ответа на 01:18 connect (generic), затем follow-up с дельтой 122/108 vs M6-M9 (уже в `followup-delta.md:1`)
- OrangePro: Вариант A — добавить vitest пример в OrangeHRM клон для Proven витрины, Вариант B — прогнать на qa-automation-sandbox для 20 blind spots (как Mattermost)
- testRigor M5 на localhost:8080 — завтра (клон не трогаем)
- Autonoma pending 16 HIGH — on demand

---

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

# Session Checkpoint — 2026-09-09 (wiki digest processing + outreach + SwarmLLM)

## Wiki digest 2026-09-07 — 7 wiki pages created
All 7 marked [x] items processed:
1. `wiki/aria-qa-data-automation-agent-2026.md` — arxiv 2609.04913 (Agentic RAG + LLM Judge, 30+ tools)
2. `wiki/spaceducking-test-feels-like-autopilot-2026.md` — MoT (98% handoff, tester as orchestrator)
3. `wiki/integration-testing-systems-stitching-2026.md` — TestMu AI (integration testing guide)
4. `wiki/from-ai-agent-demo-to-production-2026.md` — InfoQ Jul 2026 (demo-to-prod gap, guardrails)
5. `wiki/openai-wiki-incident-2026.md` — TechCrunch (Wikipedia feedback loop, data poisoning)
6. `wiki/beyond-zero-google-experimentation-culture-2026.md` — Google Research (experimentation velocity)
7. `wiki/cappy-small-scorer-boosting-llm-2024.md` — NeurIPS 2023 (360M scorer beats 175B LLMs)
- Cappy: original URL broken, fetched via research.google/blog alternate
- **CAVEAT:** "How to tell whether an AI feature actually works" (anton.qa) → pilot catalog, NOT wiki

## Wiki digest 2026-09-08 — 3 wiki pages created
- `wiki/autonomous-testing-agent-fastest-feedback-2026.md` — KaneAI + HyperExecute (TestMu AI)
- `wiki/efficient-performance-testing-grid-cloud-2026.md` — HyperExecute AI-native orchestration
- `wiki/observatory-weekly-quality-gaps-2026.md` — MoT Observatory weekly roundup
- Blog URLs 404 on testmuai.com (KaneAI, HyperExecute), fetched from main site + search
- Anton Gulin article → pilot catalog decision (separate from wiki)

## Wiki pages filled from empty (previously stubs)
- `wiki/rag-evaluation.md` — comprehensive RAG eval overview (dimensions, frameworks, patterns)
- `wiki/ui-fuzzing.md` — full UI fuzzing guide (4 strategies, Playwright patterns, OWASP mapping)

## New pages created 2026-09-09
1. `wiki/distributed-llm-inference-swarmllm-2026.md` — SwarmLLM (Nehanth Narendrula / Red Hat AI)
   - Includes practical testing plan for PC-224 + MacBook via ZeroTier VPN
   - WebGPU check, SwarmLLM clone steps, failure scenario tests
   - Alternative approaches table (web-llm, enapt/Rust, Ollama multi-GPU)
2. `wiki/verification-completeness-testing-paradox-2026.md` — William Tran ↔ Iosif Itkin LinkedIn thread
   - Core thesis: verification completeness is impossible
   - Dev vs QA views, bridge closing
   - Connection to Exactpro and AI Testing
3. **Outreach pages created:**
   - `outreach/active/William_Tran/index.md` — 2nd connection, followed 2026-09-09
   - `outreach/active/Iosif_Itkin/index.md` — Exactpro co-CEO, HIGH-value contact
   - William: Prong C comment option (his post is public)
   - Iosif: wait for engagement pattern before following

## QAEverest blog evaluation
- Post: "Agent jailbroken, eval said it passed" — LLM-as-Judge compromised by prompt injection
- **Seriousness: 6/10** — real problem, known in AI safety community, not novel
- **Marketing: 7/10** — catchy framing, blog traffic driver, thought leadership
- **Our assessment:** per-risk-tier v0.3 already addresses this (B0 tier, deterministic checks, guardrails)
- **Comparison:** Our framework deeper (5 operators, 4 tiers, 100% B1 proven) vs QAEverest surface-level

## SwarmLLM Practical Testing Plan
- PC-224 (64GB, 6GB VRAM) + MacBook Pro (16GB) via ZeroTier VPN 10.24.175.x
- Steps: WebGPU check → clone → room code → model load → measure tokens/s → test dropout
- Status: planned, not executed yet
- **William Tran:** followed on LinkedIn, waiting for response

## Stats
- wiki-topics.json: 309 → 323 (+14 over 2 days)
- wiki/ files: ~250+
- raw/ count: 209

## Next
1. Execute SwarmLLM test on PC-224 + MacBook (if WebGPU available)
2. Wait for Iosif Itkin engagement pattern → decide on follow
3. Comment on William Tran or Iosif Itkin posts (Prong C) if no response
4. Update session-checkpoint.md in main project (OrangeHRM)
5. Aamir delta — pending
6. Rupesh: still waiting on Letter 2 response

---

# Session Checkpoint — 2026-09-09 (Buzzhive restart + wiki processing continued)

## Buzzhive Restart
- Docker Desktop was manually paused → `docker-compose up --build -d` restarted all 5 containers
- **Backend** (`localhost:8000/docs`): ✅ healthy
- **Frontend** (`localhost:3000`): ✅ healthy
- **Render** (`buzzhive-test.onrender.com/api/health`): ✅ healthy (after ~10s Free tier delay)
- Both local and Render confirmed working

## Wiki digest 2026-09-09 continued
- 5 wiki pages created from digest: Agentic AI Tools, Visual Regression, Evolving Quality, Meta Muse, Professional Resilience
- meta.com (ai.meta.com) returned 400 → used TechCrunch + The Verge as sources instead
- All Meta Muse articles consolidated into one page
- Total for 2026-09-09: 11 wiki pages across both digests

## Stats
- wiki-topics.json: 323 → 328 (+5 from digest 09-09)
- raw/ count: 214

## Next
1. Execute SwarmLLM test on PC-224 + MacBook (if WebGPU available)
2. Wait for Iosif Itkin engagement pattern → decide on follow
3. Comment on William Tran or Iosif Itkin posts (Prong C) if no response
4. Update session-checkpoint.md in main project (OrangeHRM)
5. Aamir delta — pending
6. Rupesh: still waiting on Letter 2 response

## 2026-09-11 — Testkube feed + 3 wiki ingests
- digest-config.json: +testkube RSS (weight 0.8, verified 200) → 19 sources.
- wiki: four-layers (layer map + thresholds), smart-suites (diff-selection + dual mode), local-vs-frontier (hybrid doctrine = our free-first validation). Topics 332→335 (1 parallel entry from another window, no collision).

## 2026-09-15 (night) - Ingest batch: RST pair + Anthropic month + cross-domain
- Raw ingests (topics 337→349): zborovsky chief-of-staff · jay-aigner green-light thread · radik ledger gate (ENGAGEMENT HOLD — chat+letter unanswered) · ivan-davidov context engineering (transcript 515 seg, career fluff dropped) · addy-osmani skill-decay · kiro judge loop (-32%) · bolton whereas · bach metamorphic talk (transcript 885 seg) · bach+bolton amodei teardown · siniouguine silent incompleteness · colantonio perf-as-savings · osmani month digest (37 posts→8 blocks) · pusuluri oracle boundary.
- Transcripts via youtube-transcript-api, evaluated full-read before save (davidov 80% fluff cut).
- Not saved (thin): testRigor agentic-QA promo, IcebergQA STARWEST promo (Arbon talk = radar), Lew PNSQC (quote → Articles/quotes.md instead).
- Open: Amodei Sept 2026 primary ingest · Colantonio episode link · Arbon STARWEST transcript watch.

## 2026-09-20 00:24 — Bolton/Bach sandwich test + FlowScout paradigm
- Note created: `wiki/bolton-bach-llm-sandwich-hygiene-protocol-2026.md` — 19.09 experiment (gpt-6-astra friendly tone vs gpt3.5-16k honest refusal; strict non-anthropomorphic instructions -> (c) "not applicable + reformulation"; visible reasoning optimizes tone not truth; "Astra now worse for truth/reliability"). Bach mental hygiene protocol included. Cross-links: green-dashboard trap, oracle design, "unreproducible = doesn't count".
- Heusser tangent saved (The Great AI Escape / HuggingFarce, xndev.com 19.09): recurring hype pattern, HF break-in report non-reproducible, burden of proof shifted.
- Section added: FlowScout (Igor Akymenko crawler) = live sober/literal QA tool — "never asserts anything", honest CAPTCHA-reject. Repo + pilot catalog pointer (Positions-CV-CL).
- index updated (348 topics). Pilot execution delegated to another window.

## 2026-09-21 — W5 handover CLOSED: BrowserStack wiki finished + registry fix (commit 84e4a67)
- Handover from Articles (77ef3bd): "finish + commit BrowserStack wiki in ai-qa-wiki". Owner was window 5 → DONE.
- `wiki/browserstack-blog-breakpoint-2026-test-companion.md` already complete (112 lines, pushed 158e817). Found registry bugs and fixed:
  1. BrowserStack entry desc = frontmatter instead of description → corrected.
  2. Applitools wiki (20.09, `applitools-probabilistic-validation-gap-2026.md`) was MISSING from wiki-topics.json — file existed, index claimed 351 but real count 350 → entry added.
  - Cross-link added Applitools → BrowserStack (verbatim + cross-route).
- Registry now valid JSON, topics 350 → 352, commit `84e4a67`, pushed to origin/main.

## 2026-09-21 11:47 - Digest 21.09: SWE-Proof + Runtime Authorization (037bc6f)
- Digest 2026-09-21 parsed (5 from 289). 2 saved, rest skip/POM low.
- NEW wiki `swe-proof-machine-checked-proofs-2026.md` (arxiv 2609.21190, 2026-09-18): 500 SWE-bench issues formally verified; 25-50% of test-passing patches admit counterexamples (green suite != correctness, independent academic backup for Article 27); 62% of self-authored specs pass audit; spec faithfulness open problem.
- NEW wiki `runtime-authorization-ai-agents-2026.md` (arxiv 2609.14744, 2026-09-18): post-fulfillment activation gap, provenance-bounded runtime auth (quarantine-resolve-activate), envelope, 8 safety props, MCP-to-Docker.
- Registry: topics 351 -> 353, JSON valid. Commit `037bc6f`, pushed origin/main. Cross-links: mutation-matrix / verification-layer / Andrew Ng security / MCP habr.

## 2026-09-22 02:00 - LLM-wiki pattern + log.md + auto-lint (commits 0587ffb, 609ec89, 05135a7)
- **wiki/llm-wiki-pattern-2026.md** — суть LLM-wiki Karpathy (3 слоя, compiler-аналогия, Ingest/Query/Lint, «compiled once, kept current») + delta-таблица наша реализация vs механизм (log.md, confidence, contradictions, каскад entity-обновлений, категории). 
- **wiki/log.md** — append-only операционный лог. Встроен в wiki_llm.py: append_wiki_log() авто-пишет при ingest / ingest-all / sync-links / update-index (новые + человеческие записи вручную).
- **wiki_lint.py** — авто-health-check ЗАМЕНЯЕТ ручной воскресный линт ритуал: битые внутренние ссылки, orphans (нет inbound), stubs (<200 chars), raw без wiki, дубли-стемы. Отчёт → outputs/lint-report-YYYY-MM-DD.md, exit-коды 1/2/3, --summary/--json. Через wiki_llm.py --lint (wrapper) или напрямую.
- **Trend across runs**: отчёт теперь парсит предыдущие lint-report-*.md и добавляет таблицу трендов + дельты orphans/missing к прошлому прогону (видно из одного файла). Internal links OK = total−broken (баг fixed).
- **Реальные находки линтера исправлены**: 6 битых ссылок → 4 репоинта (radik-zagirov-rotting-gate → executor-evaluator-split-zagirov; llm-testing-six-approaches → llm-testing-6-approaches; your-agent-found-5-bugs → executor-evaluator-split-zagirov) + ингест raw/typesafe-jev-judgment-service-gates-2026.md (страница существовала на ссылках, но не была заведена; 5 backlinks).
- **Итоговое состояние**: 375 страниц, 719 внутренних ссылок OK, 0 битых, 249 orphans, 0 stubs, 70 missing raw, темы 376.
- **AGENTS.md** (Quality Standards): секция auto health-check + log.md. **~/.opencode-memory.md**: договорённость «Wiki health check — авто» + команда wiki_lint.py в инструментах.
- Commits: 0587ffb (pattern+log+lint), 609ec89 (trend + link fixes + typesafe-jev), 05135a7 (backlink sync). Все push → origin/main.
- **Open**: contradiction-скан через LLM остался roadmap; orphans 249 — кандидаты на кросс-линковку (связность); 70 missing raw.

## 2026-09-22 03:05 - Karpathy pattern + lint (completed 02:00) + FlowScout Kanaris thread triage (commits 7b2bf3d, 142fffd)
- Earlier today (02:00): llm-wiki-pattern-2026.md, wiki/log.md (append-only), wiki_lint.py (auto health check, trend table, exit codes), fixed 6 broken links, typesafe-jev ingest. State: 376 topics, 375 pages, 0 broken.
- **FlowScout thread 2026-09-22 ingested** (raw+wiki, topics 376→378, raw 235→236): Igor Akymenko post + Paul Kanaris critique ("undiscovered vs uncovered behavior") + Igor's honest unsolved residue (run-condition visibility, config-scoped change detection, multi-actor handoffs, one-shot irreversible transitions, time-dependent flows) + Sarang U. real overlay bug (pointer-events:auto).
- **Article gold:** Kanaris "undiscovered vs uncovered" = our discovery/verification gap language; Igor "here is what this identity could reach, in this system state" = bounded claims for VerdictGate; honest-vs-invented = Article 26 evidence (Sarang found real bug, not invented).
- Quotes: 7 added → Articles/quotes.md "Honest QA tools / undiscovered vs uncovered" section. Digest: +source "flowscout-alternateqa" (manual, no RSS). Outreach + pilot catalog updated (Positions b326885), cross-link bolton-bach already present.
- Lint-relevant: fixed unclosed BrowserStack link in ingested page (that's exactly the class wiki_lint catches).

## 2026-09-22 15:00 - Qodo Source Triage (Company First) [Sources; 5 ingest + catalog]
- Qodo (ex-Codium, 30.09.2024 rename; Qodo Gen = ex-Codiumate, Qodo Merge = ex-PR-Agent; Context Engine, Rules, Software Map; ~$120.6M funding; HQ NY + Israel, 100-150 engineers). Blog = 395 posts, RSS https://www.qodo.ai/feed/ works ONLY with browser User-Agent (Cloudflare 403 otherwise); sitemap post-sitemap.xml (saved /tmp/qodo-blog-urls.txt).
- `raw/qodo-*.md` ×5 created (fetch via curl browser-UA + BeautifulSoup extract from `.ds-block-single-post__content`):
  1. ai-gave-teams-velocity-the-governance-harness-comes-next (Itamar Friedman CEO, 2026-06-23; Faros 2026: incidents/PR +242%, time in review +441%, bugs/dev +54%; maturity advantage gone at AI scale)
  2. why-your-ai-coding-agent-shouldnt-review-its-own-code...verification-layer (2026-06-30; Gartner June 2026 Code Review Agent Example Vendor; iterative self-refine → critical vulns +33% in 5 rounds)
  3. ai-slop-is-a-governance-problem-here-are-4-principles-to-fix-it (comprehension, review-as-responsibility-boundary, risk visibility, automation-preserves-discernment; "you can't govern what you don't measure")
  4. building-the-verification-layer...code-standards (verification layer = multiplier; alpha/beta/GA progressive rigor; Goodhart; Walmart humans-in-loop; spec-is-source-of-truth)
  5. when-claude-code-reviews-its-own-pr-who-reviews-claude (live experiment: Claude Code judge filtered below-80 and suppressed a TOCTOU security bug; Qodo surfaced as Action Required; "judge as filter" vs "judge as responsibility router")
- wiki pages ×5 ingested via wiki_llm.py (topics 378→384, raw 236→241). Catalog `wiki/qodo-blog-catalog-all-publications-2024-2026.md` (TIER 1 ×5 ingested, TIER 1.5 ×13 next candidates incl. why-ai-self-review-fails, contract-verification-across-repos, RAG-removal story, rules lifecycle, context engine; 37 HIGH total).
- Cross-links: backlinks auto-updated on 5 pages. digest-config.json (Articles) receives feed `qodo` (weight 0.9 + browser UA) — digest worker per-source user_agent support added in daily-digest.py.
- Quotes: 16 → Articles/quotes.md "Independent verification layer / generator vs grader (Qodo)".

## 2026-09-22 15:30 - Qodo Software Map ingested (Article 29 candidate)
- `raw/qodo-software-map-risk-across-repos-2026.md` + `wiki/qodo-software-map-risk-across-repos-2026.md` (Itamar Friedman 22.09, live beta).
- Thesis: "you cannot govern a system you cannot see"; Faros numbers (files/PR +59.7%, files/dev/mo +149.9%, incidents/PR +242.7% at high AI adoption); blast radius per repo + contract tracking + risk heat map = Article 29 candidate (risk-tiering across repos, contract seams where attestor adds value).
- Catalog Tier 1.5 row #19 linked. topics 384→386, raw 241→242.

## 2026-09-22 16:13 - CHECKPOINT (session close)
- Session: Qodo Source Triage completed (5+1 ingested, catalog 395 posts, digest feed, 16 quotes) + Software Map Article 29 candidate.
- Commits: 22a3f4a (Qodo triage batch), 79fdf1f (Software Map). Now topics 386, raw 242.
- Next: 29 variant C source material ready (risk heat map across repos from Software Map wiki).

## 2026-09-22 23:55 - Skill pages 101-beginner-* (4 pages, glossary + index updated)
- Admin request: прокачать skills для резюме (RAG arch, MCP familiarity, FastAPI, relational/non-relational DB design) + примеры для чайников.
- Created 4 pages renamed to 101-beginner-* pattern for findability:
  - wiki/101-beginner-rag-architecture.md (3-stage pipeline, embeddings, cosine similarity, vector DB, semantic search optimization)
  - wiki/101-beginner-mcp.md (client/server, tools/resources/prompts, JSON-RPC, what to test)
  - wiki/101-beginner-fastapi.md (example API, Pydantic, TestClient, mock servers)
  - wiki/101-beginner-database-design.md (SQL vs NoSQL, constraints, cascades, migrations, pytest example)
- Glossary: +6 terms (FastAPI, MCP, MongoDB, Vector DB; RAG expanded) with links to new pages.
- topics 386→390, raw 242 (unchanged). Broken links 0. Commits: b9e9fbd (pages+glossary), 402bd5e (renames to 101-beginner-* + links).
- Next: apply same 101-beginner-* findability if more beginner pages are requested; radar quotes (Testkube AI Test Creation, Codemify live, BitGN DDD) live in Articles quotes.md.

## 2026-09-24 00:30 - CHECKPOINT (mega ingest day: Qodo + Amazon + CIGE + simulator + profiles)

**Commits (all pushed):** a8fd422 TesterArmy catalog; ac19124 Qodo report + TIER 1.5 (13) + Kiran Sahu profile; e2b1a7c Amazon cluster (8) + CIGE paper; e3b3f39 Amazon TIER 1.5 (5) + Qodo TIER 2 (9) + simulator + Valentina. Topics 414→455, raw 262→301. Lint broken 0 each round. 5 foreign files (bach x3, mas-vs-swe, satisfice) excluded every time - other window's re-ingest, left unstaged.

**Ingested:** Qodo State of AI Quality report (89%/3.7%/26% numbers, directional), Qodo TIER 1.5 #6-18 + TIER 2 FULL READ x9 (catalogs updated), Amazon Science x13 + blog catalog (RSS index.rss verified 200 full-text, 25 items), CIGE paper (Amazon QRS 2026, intent-stable/execution-repairable = heal-must-preserve-verdict), AlternateQA simulator thread (not a duplicate of flowscout thread - new artifact + Kanaris outside-practice thesis).

**Profiles:** TesterArmy (YC P26), Kiran Sahu (Myelin Foundry, fabrications cleaned before commit: refresh-labs link, slug URLs), Valentina Jemuovic (Optivem, Kraljevo Serbia). Connect notes drafted for Kiran Sahu + Valentina (user sends).

**Triage verdicts:** Amsterdam vacancy skip (2x); Testkube NO pilot (orchestration layer, rule 2026-09-21 holds; GA 22.09 changes nothing); Valentina NO pilot (coaching, no product) but outreach candidate; AlternateQA simulator = related not duplicate.

**Digest:** amazon-science entry added to digest-config.json by user manually (verified, weight 0.9). Optivem Journal RSS unchecked.

**Outreach/misc:** QA Leadership Summit watchlist given (AWS CIGE #1, multi-agent workshop #2, keynote #3, career skip).

**Next:** Leonardo Lanni vs Victor profile comparison (freelance mechanics to borrow); commit routine holds (stage-all minus foreign, spot-check deletions); backup per AGENTS.md.

**Correction 2026-09-24 (Leonardo thread):** model wrongly called qa-cube "Victor's vehicle" - qa-cube is Vadim Glushonkov's pilot tool that Victor EVALUATES (listed correctly in his Experience as evaluated tool). No vehicle bridge exists. Stale line "собственный qa-cube" in Session 127+ global memory flagged for human fix (memory file not editable by AI).
**Geo 2026-09-24 (user):** relocation to Cyprus/Georgia/Montenegro possible AND desirable, visas unlikely (not willingness). On-site list in Open-to box stands. Overrides Sophia-eval "no relocation" (was eval-specific set, not general constraint).
**Profile fixes applied by user:** Company → Independent AI Quality Engineering Practice; Services cut; top-skills reorder; recruiters-only Open-to. Pending: articles number 30+ (About line), titles trim (drop Senior Test Lead, add AI title), remote minus US/UAE.

## 2026-09-24 - Leonardo Lanni comparison + Victor profile fixes (all applied)

**Comparison (freelance mechanics, Track 1 intact):** Leonardo wins on packaging (QA-Roots vehicle, 6 buyer-readable services, 2-skill crispness, patents/langs/countries scan); Victor wins on substance (numbers, artifacts, AI-native, attestation). Takes applied: services 10→5 (Software Testing, IT Consulting, Training, Project Management, Management Consulting), top-skills with Mutation Testing first, geo/lang scan noted.

**Profile final state (user applied):** About 30+ articles (was 20+, Experience already 30 - fixed with exact replacement string); Company renamed (duplication gone); Open-to recruiters-only (correct call); titles trimmed to 3 (Senior Test Lead dropped); remote minus US/UAE; AI title NOT addable (taxonomy has only fluffy AI Manager roles - skipped deliberately); self-employed KEPT over freelance (leadership positioning; company field carries vehicle logic); relocation = yes/desirable, visas unlikely (on-site CY/GE/ME list stands); About + Experience + header reviewed, consistent.

**Micro-trim left:** Experience "(self-employed, remote)" duplicates type/location fields - suggested cut, user decision.

**Baseline for 07.10 restart:** 557 views / 2,131 impressions / 75 search appearances per 7d on content pause.

**No repo commits in this thread** (profile work = LinkedIn UI + checkpoint lines only). Next commit picks up unstaged checkpoint edits.

## 2026-09-24 - W4 pilots README proposal (reviewed + applied, uncommitted)

**Review:** all 4 findings verified verbatim against company/pilots/README.md (Positions-CV-CL): KISS/Sorcar+Applitools+Kiro = executed with empty cells; 5 tooling rows as used-subjects; roster rules duplicated lines 3/29.
**Applied** (user-authorized, owner W3 to actualize): 3 sections (Matrix pilots 11 rows untouched incl. qa-cube / Evaluated otherwise with evaluated+TBD / Tooling used), one-line status dictionary with evaluated definition, dupe rules removed. Diff verified: data rows intact.
## 2026-09-24 - W4 pilots README proposal (reviewed + applied, uncommitted)

**Review:** all 4 findings verified verbatim against company/pilots/README.md (Positions-CV-CL): KISS/Sorcar+Applitools+Kiro = executed with empty cells; 5 tooling rows as used-subjects; roster rules duplicated lines 3/29.
**Applied** (user-authorized, owner W3 to actualize): 3 sections (Matrix pilots 11 rows untouched incl. qa-cube / Evaluated otherwise with evaluated+TBD / Tooling used), one-line status dictionary with evaluated definition, dupe rules removed. Diff verified: data rows intact.
**Not committed** (other repo + чужое дерево: DevQaExpert, binaries, checkpoint +461 - hands off). W3 open items: fill 3 TBD resumes, Jev row fate (`used` in Matrix section, kept deliberately - live catalog + lead).

## 2026-09-24 - Kaggle triage + pilots split analysis + cross-repo lint (commit 82aacd8)

**Kaggle:** homepage paste triaged - only Benchmarks track ours (FACTS grounding, Enterprise Ops workflows, open SDK, grants; rest SKIP). [[kaggle-benchmarks-track-evals-2026]] with Results-log section for future outcomes.
**Positions-CV-CL (my responsibility, "чужие" retracted):** DevQaExpert renamed by user - all 5 files intact in new dir, 3 links fixed (2 ai-qa-wiki + README href had extra %20, checkpoint:166 left as history). Binaries: CV pdf moved to packet (user-confirmed), qa-cube test artifacts safe to ignore. qa-cube gitignore proposal given (playwright-report/, test-results/, __pycache__/*.pyc + rm --cached 3 files); h4_stats_results (1.1M) left for W3. Positions checkpoint +489 = qa-cube Phase 1-3 + H4 + gotcha-10 (read 2238-2567 first).
**Split decision:** pilots→W3 separate project, outreach stays here (pending W3 stop). Blast radius: ai-qa-wiki 3 links, Positions internal 12 refs, README 9 relative, scripts 0. Options A (separate repo, max break) / B (top-level move + bulk replace) / C (convention, 0 break) - recommended C now. Cross-vault rule: absolute github URLs > relative fs paths (404 outside repo).
**wiki_lint.py:** cross-repo check implemented (P1, bases skipped when absent); paren-in-URL bug caught and fixed during negative test. Lint clean, broken 0.
**Commit 82aacd8 pushed** (Kaggle + DevQaExpert links + lint). 5 foreign excluded again. Leonardo profile work + geo/relocation decisions in previous section.

## 2026-09-24 - Kiran Sahu reply: attribution error caught by contact

**What happened:** connect note congratulated Kiran on STeP-IN Wall of Honor. He replied: award went to someone else, not him. Root cause: original pasted block mixed multiple people's content; Wall of Honor was never his. Same fabrication class as Gotcha #1, caught externally this time.
**Fixed:** profile downgraded (Wall of Honor removed, hosting details → ⚠️ unconfirmed), outreach log added.
**His substance:** QA+AI+dev jointly structure framework per new app; each development = new test strategy + accuracy metrics; invited specific questions. Reply drafted (acknowledge + one specific Q on RAG metrics/ownership), user sends.
**Rule reinforced:** mixed LinkedIn pastes (post + profile + related people) must be split per-person BEFORE drafting; congrats-lines only on self-stated achievements.

## 2026-09-24 - Split decision: pilots → W3 separate project, outreach stays here (pending W3 stop)

**User decision (to execute with W3 when it stops):** company/pilots becomes a separate project owned by W3; outreach stays with this window. Move only if nothing breaks.
**Blast radius counted:** ai-qa-wiki → pilots links = 3 files (2 just fixed for DevQaExpert rename); Positions internal `company/pilots` refs = 12 files (Rupesh x3, Igor, Maksim, DevAssure held, +); pilots/README internal `pilots/X` links = 9 (relative - survive a move as a unit); scripts referencing pilots = 0.
**Options:** A) separate GitHub repo - max breakage (all relative links die, URL rewrite needed); B) top-level move inside repo - medium (3+12 path-prefix fixes, mechanical bulk replace); C) no move, ownership by convention - 0 breakage. Recommendation: C now, B only with W3 stopped + bulk-replace script; A overkill without permissions/visibility need. Note: split complicates person↔pilots↔wiki cross-linking (this window's function) - cross-repo links already fragile plain text.

## 2026-09-25 - Jev-replacement track (W5 mini-jev runs, plan, B0, qwen3 saga) + ingest wave

**Commits:** a9dca0f (CodeScene batch+catalog, Vadim vendor page, Kiran fixes), 080ae84 (Haim patterns, Radik DGM, Exactpro book, Applitools whitepaper), 4834ce8 (tier-model matrix, JDAQA dossier, SHRM map, Grzegorz, Aigner, HW spec). PDFs (Darwin 3.8M/72pp, Guardrails) local-only per user, never git add -f.
**Ingest wave:** Vadim blog (JS-chunk extraction, vendor page + AlternateQA-affiliation hunt = NO evidence, peer-proximity only), Haim pattern-matching (4 orchestrators, retry-loop = verdict-gate miniature), Radik DGM post (paper verified via arXiv API + ar5iv full-text: skeleton real, "12 passed"/quota/markers dramatized; SWE 20→50 CONFIRMED after own grep-miss correction; German original via guest view), CodeScene 7 + catalog (Street Fighter case), Amazon cluster 13 + catalog + digest entry (user inserted manually), CIGE paper, Kaggle Benchmarks track, SHRM field manual (market map), Applitools whitepaper (Monkey-Paw matrix import), Exactpro CT-AI book record, simulator thread, Valentina + Kiran Sahu profiles (Kiran Wall-of-Honor attribution error caught by contact, fixed + gotcha logged; reply sent, awaiting answer).
**Profiles/outreach:** Kiran Sahu connect+followup sent; Valentina note ready; Igor engine-vs-car reply sent/logged; Radik reply drafted/discussed (answer-then-punchline kept, no @mention); Itkin comment + book approved (user posts).
**Triage verdicts:** Testkube NO pilot (orchestration, recorded); Valentina NO pilot (coaching) but outreach; AlternateQA simulator = related not duplicate; Kaggle partial (Benchmarks track only); Jev-cloud: OpenCode Zen jev-1.13-free CONFIRMED docs (own Console token invalid for Zen), Vercel paid not free, pngwn/open-jev Space CONFIRMED real, Laya verified w/ Banking77 caveat, Kev-0.5B research prototype, OpenJevPro Cloud private 401s (W3 confirmed), SemIf verified (4B heavy on Intel iGPU, 0.6/2B fine).
**Jev-replacement W5 track:** P0-trial qwen2.5:3b (21 calls, steady ~0.1s, 3/3 stable, $0) + ZeroTier repeat identical (5.9s both paths; roaming OK subject to PC-224 on). Handover plan doc written to pilots/Jev/plan-local-judge-2026-09-25.md (phases A-E + B0, thresholds 10pp/15% + P0-miss=0 approved, staffing W3+Victor/W2 arbiter, freeze digest 357c53fb). B0 Banking77 (77 labels, case-insensitive scoring after B0-30 lowercase catch): qwen2.5:3b = 69/90 = 76.7%, confusion clusters stable.
**qwen3:4b delta (IN PROGRESS, messy):** model pulled remotely (/api/pull, 2GB). Thinking ON required (think=false breaks instruction-following: prompt echo). Per-call 10-460s (thinking tax). Harness bugs hit: sed false/False, paren surgery, overwrite-instead-of-merge (lost 28-row chunk, aggregates kept: 28 HIT) - all fixed, runner clean-rewritten with incremental save + slices. State: 66/90 rows (56 HIT / 9 MISS / 1 timeout); remaining B0-07..10 + B0-28..30 (~24 calls, 2-3 windows). Files: outputs/mini-jev-b0-qwen3-4b-raw-*.json + runner. qwen2.5:3b freshness: weights Sep 2024 (pull date Apr 2026); VRAM check proved 100% GPU offload (3.36/6GB), RAM 6G/64 observation explained.
**Infra:** two-machine map corrected (MacBook remote vs PC-224 .209 LAN + .30 ZT; 192.168.1.224 stale); HARDWARE_SPEC.md updated (IPs, 20-model inventory, endpoints); ping ZT 5.6ms, LAN path absent; third addresses (.189 ZT self, .122 LAN self) identified.
**Events:** QA summit watchlist given; Applitools webinar (Eyes MCP) watched-item + TAU pointer; Evolve HR conf live-triaged (Gia agent video transcript, Derya Dogan peer logged + DM, Stan/Vladimir indexes updated, SHRM manual ingested, Derya + job-seeker noise triaged); Igor 4th-bug question resolved (no 4th: 3/3 closed, residual deep-SPA-nav unsent, ROADMAP Toggle misread; draft follow-up given to W3).
**W4 pilots README:** reviewed 4/4, applied 3-section restructure (Positions repo, uncommitted, W3 to actualize); DevQaExpert rename handled (files intact, 3 links fixed, checkpoint:166 kept as history); qa-cube = Vadim's (my vehicle-bridge hallucination corrected + logged; global memory line flagged for human fix).
**Open threads:** Kiran Sahu awaiting reply; Radik reply to send; Itkin comment to post; W3 merge (agreement) + n=30 campaign + gold assessors; Conf42 Haim materials watch; Lund study watch; Optivem RSS unchecked; 5 foreign files still excluded every commit; Leonardo profile fixes applied by user (services/skills/30+/geo).
**Fix-orphans night job (2026-09-25 19:33 → 04:00):** implemented TF-IDF fix_orphans in wiki_lint.py (dry-run + --limit + safe auto: FOREIGN_SKIP, fresh-mtime skip, See-also before backlinks marker, [Title](wiki/) format). Dry-run calibrated: 694 @0.05/3 → night mode 363 links/216 hubs @0.12/2. Runner scripts/fix-orphans-night.sh (snapshot /tmp, lint, report outputs/fix-orphans-night-DATE.md, NO commit, self-unload). launchd com.aiqa.fixorphans-night loaded, 04:00 one-shot. Morning: review report + git diff, then commit command.
**Q3 closed (`d91791b`, no follow-ups):** llama3.2:3b = 63/90 = 70.0% (cell 4: below bar + spots uncaught). Strongest finding of cycle: all three vendors hallucinate literally the same non-existent label (Get_virtual_card) on B0-12 despite Banking77 contamination predicting capture - contamination flipped from threat to decisive argument (task-intrinsic boundary: near-neighbor + label-set gap). Llama numbers kept as observations, not merged into T3.

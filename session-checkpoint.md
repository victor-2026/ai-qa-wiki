# Session Checkpoint — 2026-06-28

## Session — Video Capabilities in OpenCode Free

- **New wiki page:** `wiki/video-capabilities-opencode-free.md` — MiMo-V2.5 native omnimodal, TUI vs Desktop distinction, all 19 Go models analyzed, video support matrix
- **New raw:** `raw/video-capabilities-opencode-free.md` — source version with extended notes
- **wiki-topics.json updated** — 59 raw entries, Google ToS entry structurally fixed (was outside topics array)

## Previous

# Session Checkpoint — 2026-06-19

## Notion Kanban + Bot Integration

**Source of truth changed:** Notion Tasks DB = master, local `kanban/*.md` = auto-generated mirror.

### Что сделано

**Notion → Telegram auto-dispatch (3 бага пофикшено):**
1. `get_opencode_attach()` — lsof parser брал `(LISTEN)` вместо порта → `http://localhost:(LISTEN)/session`
2. Dispatch stuck на "tracked" — `setdefault` не перезаписывал "failed" статус при рестарте
3. "Session not found" от Desktop app (internal IPC, не session API) — теперь notification-only

**Kanban sync:**
- `~/bot/notion-sync-kanban.py` — новый скрипт: Notion Tasks DB → 9 файлов `kanban/*.md`
- Notion = master, `AGENTS.md` обновлён

**Wiki:**
- `wiki/notion-kanban-bot-setup-2026.md` — архитектура, DB ID, токены, нюансы
- `wiki-topics.json` обновлён (108 topics)

**Задачи закрыты (Notion → Done):**
- `[W1] Test Notion Agent: search, Plan Mode`
- `Update help center & FAQ`

### Key files
- `~/bot/bot.py` — Telegram bot (polling kanban + Notion)
- `~/bot/notion-sync-kanban.py` — Notion → local mirror
- `~/Projects/Articles/AGENTS.md` — source of truth updated
- `~/Projects/Articles/kanban/*.md` — 9 auto-generated files
- `wiki/notion-kanban-bot-setup-2026.md` — full setup docs

## Session 60c (2026-06-24) — AI Fluency Interview Reform + Article

**Wiki:**
- `raw/ai-fluency-interview-reform-2026.md` — NEW (Google, Meta, Canva, Cognition interview reform)
- `wiki/ai-fluency-interview-2026.md` — NEW (analysis + what QA needs to prepare)
- `wiki-topics.json` обновлён (111 topics)

**LinkedIn article (scheduled Jun 25):**
- `Articles/linkedin-posts/AI-Fluency/interview-format-change.md` — Pulse Article
- `Articles/linkedin-posts/AI-Fluency/ai-fluency-post.md` — Feed post
- Topic: AI Fluency as new interview standard (Google, Meta, Cognition, Canva)
- Pre-publish: needs [SCREENSHOT] images generated + [COVER] image

## Session 60b (2026-06-24) — Obsidian Scam + Security Audit

**Wiki:**
- `raw/obsidian-scam-audit-2026.md` — NEW (full scam story: fake QA audit → Obsidian vault → malicious plugins)
- `wiki/obsidian-security-checklist.md` — NEW (risk assessment, defense layers, automated checks)
- `wiki-topics.json` обновлён (110 topics)

**Security audit (all 8 vaults):**
- No dangerous plugins found ✅
- Restricted Mode OFF everywhere (expected — community plugins used) ⚠️
- Sync hygiene: fixed 6 vaults (`"sync": false`)
- DYI-Building: created proper `.obsidian/` config with Restricted Mode ON

**Script:**
- `~/scripts/obsidian-security-check.py` — weekly checker (dangerous plugins, unknown plugins, restricted mode, sync)
- Cron: Mon 9:00, logs to `~/scripts/obsidian-security.log`

## Session 60d (2026-06-25) — Google/Meta Interview Criteria Deep-Dive

**Topic:** AI Interview Reform — enriched with detailed evaluation criteria

**Что сделано:**
- Researched Google and Meta interview reform details (pipelines, evaluation criteria, stages)
- Added detailed sections to `raw/ai-fluency-interview-reform-2026.md`:
  - Google Evaluation Criteria (Code Comprehension, Prompt Engineering, Validation, Googliness)
  - Meta Evaluation Criteria (3-stage project, 4 competencies, CoderPad tool selection)
  - Common Success Markers (Ownership, Decomposition, Code Audit, Narrative)
- Updated `wiki/ai-fluency-interview-2026.md` with:
  - Google (L3–L4 + QA) structured section
  - Meta (AI-Enabled Coding) 3-stage + 4-competency breakdown
  - Common Success Markers section + "fundamental knowledge still required" note
- Linkedin article reviewed — structure already aligned with new details

**Next:** Generate [SCREENSHOT] images for interview article, or publish as-is

## Session 60e (2026-06-25) — Wiki Expansion + Improvements from Bugs + Carousel Plan

**Что сделано:**

**1. Wiki `ai-fluency-interview-2026.md` — расширение:**
- Добавлен Obsidian wikilink на raw: `[[raw/ai-fluency-interview-reform-2026|Source raw material]]`
- Добавлен Timeline (+ Stripe, Amazon, Microsoft, Coinbase, Shopify)
- Добавлены секции по Stripe, Amazon, Microsoft, Coinbase, Shopify (5 new companies)
- Добавлены 6 Common Success Markers (Output Validation, Prompt Granularity, Technical Ownership, Debugging, Delegation, Narration)
- Добавлен 3-5 Minute Rule, Common AI Bugs Checklist, Technical Ownership Strategies
- Добавлен Practice Checklist
- Добавлена таблица Industry Reports & Official Guides 2026 (TestGorilla, Google Guide, GoodTime, iMocha, Stripe)
- Удалены дублирующиеся секции (merged Old vs New tables)

**2. `wiki/improvements-from-bugs.md` — NEW (25 gotchas):**
- 10 из qa-automation-sandbox (regex selectors, test title colons, 429 retry, Render deploy, contract tests)
- 9 из OrangeHRM (timeout, selectors, strict mode, cross-version differences)
- 6 cross-project process improvements (Quality Gates, checkpoint protocol, TUI communication, seed test, Allure, mutation insight)
- Формат Perplexity gotchas с root cause / fix / rule added

**3. Carousel article plan:**
- 10 слайдов, аудитория testers + test managers
- Positive stance (no complaints, want to be ready)

**4. LinkedIn email ответ:**
- Отправлен отказ Thomas Carrillo Beeck (SAP Test Manager) с упоминанием non-EU

**Files modified:**
- `wiki/ai-fluency-interview-2026.md` — major expansion (82→210 lines)
- `wiki/improvements-from-bugs.md` — NEW (25 gotchas, ~170 lines)
- `wiki-topics.json` — +1 topic (62 total)

### Known issues
- Notion DB has duplicate tasks (от импорта)
- `get_opencode_attach()` не работает с Desktop app — IPC порт 63816 не session API
- Без сессии opencode → только Telegram уведомление

---

## Session 2026-06-27 — 7-Layer LLM Testing Framework

### Что сделано
- **wiki/7-layer-llm-testing-framework-2026.md** — новая статья (Rohit Krishna, Priceline)
  - 7 слоёв: Functional Correctness, Consistency, Integrity, Edge Cases, Groundedness (RAG), Regression, Latency/Cost
  - Custom Integrity Harness (CI gate на 200 строк Python)
  - 3 техники масштабирования (paraphrase generation, prod transcripts, nightly CI)
  - Цитата автора: "start with integrity testing first"
  - Перевод на русский (термины и код — английские)
- **wiki-topics.json** — обновлён (+1 topic, 63 total)

### Files modified
- `wiki/7-layer-llm-testing-framework-2026.md` — CREATED (188 lines)
- `wiki-topics.json` — added topic entry
- `session-checkpoint.md` — this entry

---

## Session 2026-06-29 — DS/ML Testing Go Code + LinkedIn Analyzer + Dark Theme

### Что сделано
- **code/ds-ml-testing-go/** — Go имплементация 4-уровневого DS/ML тестирования:
  - `liquidity.go` — алгоритм распределения ликвидности (weighted scoring)
  - `liquidity_test.go` — 11 тестов: PBT (4 invariants), table-driven edges, A/B gate, drift detection, golden dataset
  - Найден и исправлен баг: NaN при нулевых весах (zero_rating edge case)
- **code/linkedin-analyzer/** — Go-анализатор LinkedIn-контента с 4-уровневой моделью:
  - Читает performance-log.csv, проверяет PBT инварианты
  - Ранжирует хэштеги и форматы по avg impressions
  - Детектит недельный drift engagement
  - Вычисляет P50/P90 бенчмарк
  - Поддерживает CLI: `go run . <csv>`
- **raw/ds-ml-quality-testing-2026.md** — обновлён (ссылка на code/)
- **wiki/ds-ml-quality-testing-2026.md** — обновлён (ссылка на code/)
- **raw/linkedin-performance-analyzer-2026.md** — CREATED
- **wiki/linkedin-performance-analyzer-2026.md** — CREATED (ingested)
- **wiki-topics.json** — 123 topics, 73 raw sources
- **index.html** — dark/light theme via `prefers-color-scheme`
- **_layouts/default.html** — CREATED (GitHub-dark CSS vars + light fallback)
- **_config.yml** — `layout: none` → `layout: default`

### Pipeline
- Avito Test Lead (01.07) — DS/ML + Go gaps покрыты code example
- NextDay AI (02.07) — формат не известен

### Views/ReadRate
- Добавлена колонка `views` (индекс 12) — реальные открытия статьи/поста
- read_rate = views / impressions (читаемость)
- Пока N/A — исторические данные без views. Заполнять из LinkedIn Analytics
- A/B-вывод: articles дают больше impressions, posts — выше engagement. read_rate покажет правду

### Files modified (29 files total across 3 repos)
- `ai-qa-wiki/` — 2 code projects, 2 wiki articles, dark theme, config
- `Positions-CV-CL/catalog/Avito/interview-prep.md` — CREATED (2-day plan)
- `Case_TL_Avito/raw/` — 9 new answer files pushed
- `~/.opencode-memory.md` — this entry

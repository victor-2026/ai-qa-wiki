# KanDDDinsky 2025: "When DDD Met AI" — Rinat Abdullin (talk summary)

**Source:** https://www.youtube.com/watch?v=mdB6KbBeOjc (~50 min, EN auto-transcript, 1386 segments). Canonical: KanDDDinsky channel, 579 views, published 10.09.2026 (W1 28.09). Slides: https://abdullin.com/uploads/events/2025-KanDDDinsky-Rinat-Abdullin.pdf — verified live 28.09 (74 pages, 18 MB) but image-based, no text layer (953 chars extracted); vision review possible, not done. Raw transcript: `raw/kandddinsky-2025-rinat-abdullin-when-ddd-met-ai-transcript.md` (fetched 2026-09-28). Caveat: auto-transcript — names/terms may be off.
**Context:** follows Eric Evans' talk; Time to Act / TimeTag Austria strategy-hub community; enterprise challenges with public results/code; Greg Young mentioned (teaming up for the next challenge).

## Framing: the map of what actually worked

Community-observed successful AI cases (failures not counted): three categories — (1) **data extraction at scale** (highest ROI; invoices/POs/PDFs → internal systems), (2) AI search/assistant/chatbot/recsys (internal silo-connectors included), (3) **AI platforms** (track/host/version models, constrained decoding as rollout grows). Most adoption: sales/marketing/ops/knowledge-mgmt; manufacturing + business services lead.

## Story 1 — €400/hour (compliance gap analysis)

EU regulation → national implementation → company policy; fines/license at stake; experts charge ~€400/h to translate paper piles into procedures. Trick: replicate ONE expert's zettelkasten on paper first (copy-paste references = research), then transfer the paper workflow to LMs. Core technique: **schema-guided reasoning (SGR)** via constrained decoding — encode the expert's mental checklist in JSON-schema FIELD ORDER (the model attends to what it was forced to write first); enums to 10k items; routers/decision-makers/branching programs packed in a single prompt. Transparency: plot considered-vs-pulled clauses, expert reviews ("missing a couple of pages"), feed back into schema. Rule: more steps in one prompt → hallucination at cognitive capacity — hence SGR.

## Story 2 — 30-year-old code (AI code factory)

500k lines of mainframes/OpenEdge/Progress, file DBs, cryptic columns, retirement cliff; full rewrites fail. Pattern = translate between two domain models. **Thesis (the short): "if you have good requirements, if you have excellent tests, then you can actually throw the entire back end away... So, the tests are the most valuable part."** Legacy has zero tests. Concept: **AI code factory** — humans write the factory (processes, rules, prompts, tests, architecture, guidelines), AI writes tests + code; economics flip → 200% tests/code (parallel Python+Kotlin), event-driven specs, 10 agents in parallel keeping 1, TDD-as-it-should-be, restyle mid-flight without grumbling.

## Story 3 — Hail Mary, 6 days (power-component datasheets)

Unique-layout PDFs → single domain model; baseline LLM pipeline (days, ~€350, 60%). Method: Day 1–2 gather test data in Excel (1 row = 1 test, 60+ columns; boring for humans = shows the value); failing unit tests first; **strategic error maps** (heatmaps: rows = docs, columns = cells, green/red/gray — gray = not processed, red chunks = misaligned domain model); 15-minute experiment loops; **red team** ("find the worst cases, add as many reds as possible" — vault team gamified). 46% → 62% → 82.4% on the adversarial set → **99.7% on the customer's own data** (day 6); **$26 for 30,000 entities**. Discovered architecture (under test protection): agent writes a tool per step (100k lines no human ever saw); two prompts (SGR meta-analysis + "be lazy, write Python code"); GPT-5 mini (4o failed); 5% tool failures retried with high reasoning; two feedback loops (agent self-fix + human heatmap prioritization). Generalization came from tuning to the physical model (voltages), not words — new vendors worked.

## Closing

DDD unlocks enterprise AI (attention to words/language/thinking); take the boring repeatable part → paperwork → digitize; community research (SGR came from Enterprise Challenges 1–2); next challenge = agents deciding in enterprise.

## QA-relevant extraction (our lens — why this talk is filed here)

1. **Tests as the most valuable artifact** (replaceable implementations) — the short's thesis, now with the full argument behind it.
2. **Eval-team-first sequencing:** tests before pipeline, adversarial test data, heatmaps as shared truth, 15-min loops, red-team gamification. The 46→82.4→99.7 arc is the strongest public "evals saved the project" narrative in our corpus.
3. **SGR as judge determinism:** checklist-in-schema-order is directly applicable to our LLM-judge hygiene (force the label AFTER the evidence fields).
4. **Numbers (talk-claimed, not independently verified):** 46→62→82.4→99.7, $26/30k entities, ~€350 baseline, 100k unseen lines, 10 parallel agents keeping 1, 5% retry-with-high-reasoning.
5. Quote candidate (Articles, talk-verbatim via transcript): "if you have good requirements, if you have excellent tests, then you can actually throw the entire back end away" — NOT banked yet (transcript-grade source; bank on W4 call).

## Comment SENT 28.09 (owner, W1 merge of W5 base + W4 line)

> Love this framing — and the sharp edge: replaceable implementations demand irreplaceable verification. A suite that stays green on a broken implementation doesn't make it replaceable, it makes the breakage invisible. The replaceability test: remove something on purpose and see if the suite fails for the right reason.

First sentence = W4 antithesis ("firewall between captured and assumed" was the abstract alternative — rejected as unfalsifiable); rest = W5 concrete. Rationale recorded: Rinat respects measurement, not aphorisms; competence display with zero asks is ideal for a parked contact.

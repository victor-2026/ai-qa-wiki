# Durability Curve: Your Tests Pass. So What? (Harry Floyd, 2026-07-14)

**Author:** Harry Floyd (инди-издание The Durability Curve: сайт + Substack + tools + laws)
**Published:** 2026-07-14 (walkthrough 2/3; walkthrough 1 — Stop-hook gate против "done" на красном)
**Source:** https://durabilitycurve.com/blog/your-tests-pass-so-what/
**Status:** practitioner walkthrough, runnable (mutate.py, 180 строк stdlib, companion folder)

## Саммари

Мутационное тестирование AI-кода руками: 105 поломок прод-модуля 822 строк (21 green regression tests) → 38 killed / 67 survived. Toy-кейс: money-функция, 1/10 killed — скидка 20% → надбавка 20%, гейт зелен. `test_zero` (add(0,0)==0) аппрувит вычитание при 100% coverage. Survivors → work order агенту (4 теста, score 10/10, но с проверкой asserted values против должного, не текущего — иначе канонизация бага). Equivalent survivors живут с комментарием. CLAUDE.md-политика: "test I have never seen fail does not count as coverage".

## Ключевые формулировки (кандидаты в банк W4)

- "A test you have never watched fail is not yet a test."
- "Coverage measures reach. Mutation measures detection. Only your read decides what is right."
- "The score proves the tests ring when the code changes; only your read proves they are ringing for the truth."
- No-code версия: plant errors в отчете → "A review you have never watched catch a planted error is worth exactly what a test you have never watched fail is worth."

## Наши пересечения (дословные)

- test_zero-демо = наша弱-decoy логика (покрыто, но не pinned).
- Survivors → agent work order = MUTGEN-паттерн [[mutgen-mutation-guided-test-generation-2025]] + Meta ACH.
- "Score is a worklist, optimize % как KPI — болезнь" = наш gaps-first против score-threshold.
- Google mutants-as-review-diffs + Meta ACH цитируются — общие источники.
- Честность про границы (equivalent survivors, slow на repo, clean score bounded) — уровень disclosure как у Groetz.

## Связь

- [[mutgen-mutation-guided-test-generation-2025]] / [[meta-ach-mutation-guided-llm-2025]] — тот же mutation-guided цикл, индустриальные версии.
- [[ai-qa-tool-evaluation-mutation-matrix]] — seeded breaks + per-tier verdicts как standing-версия его one-off аудита.
- Серия: gate-walkthrough (Stop hook), Stable Liar, reliability; тул Potemkin Map; 5 laws; RSS `/rss.xml` — кандидат в дайджест.

## Potemkin Map (tool 05, https://durabilitycurve.com/tools/potemkin-map-d52e049b/)

Интерактивная 2×2-карта своих AI-циклов, полностью client-side (ничего не покидает страницу, карта в URL-hash). Оси: подделываем ли сигнал? терминален ли первый провал? Углы: Honest·irreversible / Potemkin corner (fakeable + terminal — опасный) / Safe·iterate / Fakeable·recoverable. Наш перевод: Potemkin corner = silent green зона (сигнал подделываем самой природой, первый провал — прод). Рядом еще 6 тулз (Two-Rate, Multi-Agent Decision, Marathon Calculator, Metric Validity Audit, Structure Spotter, Shape Test).

## Caveat

- Python/Unittest-мир, toy + один прод-модуль автора; цифр воспроизводимости нет.
- Raw не заводился: первоисточник — URL выше.

## Автор и метод (start/about, 03.10.2026)

- Одиночка Harry Floyd, с апреля 2026; evidence собирают агенты; claim ledger публичный: 478 клеймов, 372 verified у первоисточника (статусы Verified/Executed/Checked/Reported/Struck/Excluded — вычеркнутое тоже хранится с причиной).
- 5 законов с условиями фальсификации и историей правок: Bottleneck Migration, Difficulty Is Load-Bearing, Architecture Outlives Content, Instruments Over Theory, Targeting Problem.
- 5 читательских троп (trust agent, benchmark lying, harness, money edge, self) + printables (Seven-Layer Agent Audit, Skill BOM, State Channel Audit, Skill Routing Eval, Grounding Pass).
- Peer-мост: hello@durabilitycurve.com. Метод прозрачности — родственник нашего gaps-first.

## Линза (start-here манифест, https://harryfloyd.substack.com/p/start-here-what-survives-when-the)

- **Canopy vs substrate:** видимое (демо, бенчмарки, промпты) vs то, у чего останется работа после repricing (дата-пайплайн, eval-контракт, workflow, trust, failure memory, decision rule). "Durable architecture, которую bottleneck уже покинул — тающий кубик льда."
- **Durability test:** сначала письменно фиксируешь substrate-список, ПОТОМ называешь disturbance. Порядок — весь тест: "A test you cannot fail is not measuring anything." Наш pre-registration дословно.
- **Куда мигрирует scarcity:** обычно вверх (verify/select-слой), при физической/институциональной редкости — вниз (compute, permission).
- 5 читательских троп + claim ledger (478 клеймов, Verified/Executed/Checked/Reported/Struck/Excluded).

## Companion

- [Durability: AI grader needs a verified answer key (77 studies + Judge Check)](wiki/durability-grader-answer-key-2026.md) — key-сторона той же серии (mutation-сторона здесь).

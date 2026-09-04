# План — BeyondQuality + SlopCodeBench + Pi (2026-09-03)

**Цель:** обсудить подробнее последний материал (BeyondQuality 2 долга + SlopCodeBench 0/15) и где применим Pi.

---

## 1. Запланировать обсуждение — BeyondQuality + SlopCodeBench

**Когда:** предлагаю `2026-09-04 18:00-19:00` (1ч, после daily, до воскресного ритуала 21:00). Альтернатива: `2026-09-05 10:00`. Подтверди.

**Формат:** 60 мин, 3 блока по 15 мин + 15 мин next steps. Ведет Виктор, Pi `oracle` как второй взгляд (challenge assumptions).

**Повестка (из 8 страниц + SlopCodeBench):**

1. **09:00-09:15 — 2 долга (comprehension / intent) — что это у нас?**
   - Q: Где у нас comprehension debt уже виден? (Pi генерирует код, но кто понимает `qaeverset-pilot-mini` 5 тестов? Кто понимает mutation-matrix `C/P`?)
   - Q: Intent debt — где теряем `why`? (Rupesh 78% sensitivity — почему порог не хардкод? Megi — риск-уровни)
   - Данные: Bastani 17% хуже, Shen 50% vs 67%, METR 19% дольше но считают -20% — верим ли?

2. **09:15-09:30 — Boehm-кривая в AI-эре: где у нас дорого найти что переписать?**
   - Q: У нас `find what to rewrite` — где дорого? (Локатор drift M6/M7 vs функциональный сбой M8/M9 — структурный дороже)
   - Q: Prevention > appraisal — инвестируем ли в спеку/контракт перед генерацией? (Zalando data contracts, martinfowler context layer)
   - Данные: SlopCodeBench cost ×2, changed 97→30% — видим ли у себя?

3. **09:30-09:45 — SlopCodeBench как зеркало: 0/15 end-to-end, 5-7× erosion**
   - Q: Почему `0/15` даже с идеальной спекой? Что это говорит про `specs only → AI adapts forever`?
   - Q: Erosion 5-7× быстрее — как мерить у нас? (CCN inflection у Zalando, 473 human repos vs наши wiki 292 файла)
   - Данные: isolated 28.1% vs strict 14.8% — требуем end-to-end, не per-checkpoint

4. **09:45-10:00 — Применимость: 4 условия Direction 3 + наш per-risk-tier gate**
   - Q: Какие 4 условия для нашего gate? (Rupesh — Suite Sensitivity per tier, Megi — Review effort min, Article 21 — Conway ownership)
   - Next: гипотеза `AI-enabled collaborative building` — тестируем ли? (Pi `oracle` + `reviewer` как collaborative loop)
   - Решение: фиксируем 2-3 эксперимента на неделю (см. ниже Pi)

**Подготовка к обсуждению:**
- Прочитать `wiki/beyondquality-ai-era-testing-2026.md:1` (91) + `wiki/slopcodebench-2026.md:1` (97) — 15 мин
- Подготовить 1 пример своего comprehension debt (где ревью `looks fine` ≠ `is right`)
- Pi `oracle` заранее: `Ask oracle for second opinion on BeyondQuality 2 debts applied to our mutation matrix — what might we be missing?`

**Выход:** 2-3 решения, куда вставить prevention (спека/контракт) и как мерить erosion у себя (CCN, changed %, cost).

---

## 2. Pi — где заходит, где нет

**Принцип Pi (из `pi-subagents` 93 строки):** `scout` (recon) → `researcher` (web/docs) → `worker` (implement) → `reviewer` (check) → `oracle` (challenge). `pi install npm:pi-subagents`, `maxSubagentSpawnsPerRun=64`, FleetView. Глобально `openrouter/free` → fallback paid (20 RPM / 1000/day, ≥$10).

**Матрица применимости (для твоих задач):**

| Задача | Заходит? | Pi-агент + промпт | Почему да/нет | Ограничение |
|--------|----------|-------------------|---------------|-------------|
| **Ревью методики мутаций** (mutation-matrix-lite/full, M6-M9, risk tiers) | ✅ **Да, отлично** | `oracle` + `reviewer` parallel: `Ask oracle to challenge assumptions in mutation-matrix-full.md — C/P partition, fix vs preservation, per-risk-tier gate. Run parallel reviewers: one for correctness (C/P логика), one for test design (PBT vs unit), one for simplicity.` | Pi `oracle` ловит self-preference (как в BeyondQuality) — второй эпистемической позиции. `reviewer` проверит 5 вопросов Gulin. | Требует human sign-off — Pi не заменяет RACI `Accountable owner`. Используй как второй взгляд, не gate. |
| **Ревью статей** (LinkedIn Articles 16/20/21/26/27, 1200×644 cover) | ✅ **Да, сильно** | `reviewer` + `oracle`: `Use reviewer to review Articles/linkedin-posts/.../26-testing-the-ai-testing-tool.md against tech-writer skill (hook ≤100, money paragraph ≤150, ≤9 emoji, 3-5 hashtags). Ask oracle to challenge thesis: does Article 26 test the testing tool or just describe?` | Пи уже умеет `reviewer` для статей — ловит `looks fine` vs `is right`, проверяет evidence. `oracle` — на thesis. | Пи не чувствует `visual taste` (Julia Pottinger — AI cannot see UI) — cover/layout визуально проверяй сам. |
| **Подготовка материалов по вакансии** (Virto Commerce pitch, for-oleg slide/email) | ✅ **Да** | `scout` + `worker`: `Use scout to inspect Virto Commerce tech stack (89/109 endpoints) and Boris Khodok role, then worker to draft for-oleg-email.md with RACI per-risk-tier` | `scout` быстро мапит кодбасу, `worker` драфтит, `reviewer` чистит. Для вакансии — `scout` на JD + `researcher` на компанию. | Нужна твоя `intent` (why именно эта вакансия) — Pi не накопит intent debt, ты должен дать `why`. |
| **Оценка вакансий** (Head/Lead/Manager фильтр, EU/UK/Serbia, 6 мес.) | ⚠️ **Частично** | `researcher` + `oracle`: `Ask researcher to pull Head of QA vacancy, check Serbia remote, visa, date, then oracle to challenge: is this leadership or IC disguised?` | `researcher` хорош для сбора фактов (JD, location, date), `oracle` — на проверку контраргумента (фильтр leadership vs IC). | Финальное решение — **человеческое judgment** (риск, compensation, visa). Pi не чувствует `consequence-grounded` (BeyondQuality) — нет lived consequence. Не делегируй решение, только сбор + challenge. |
| **Подготовка Q&A по вакансии / переговоры** | ✅ **Да** | `scout` (JD) → `oracle` (challenge your answers) → `reviewer` (проверь STAR-ответы на 5 вопросов Gulin) | Pi `oracle` имитирует CTO (Oleg) и бьет по `can you sign off?` — дешево прогнать 10 итераций. | Не пускай Pi писать финальный email без твоего `own words` — иначе теряешь comprehension (ты должен объяснить своими словами, как в PR block Julia Pottinger). |
| **Триаж / перепроверка вакансий пачками** | ❌ **Нет, не заходит** | — | Объемный `generate` без `evaluate` — Pi сгенерит 100 оценок, но они будут `plausible but subtly wrong` (BeyondQuality novel failure modes). Нет independent evaluator — тот же `self-preference` что у SlopCodeBench. | Для пачек нужен **verification layer** (человек или второй независимый judge), а не еще генерация. |

**Правило Pi (из beyondquality):** AI хорош для **breadth** (draft, recon, breadth), человек — для **judgment** (risk, intent, done). Pi → `scout/researcher/worker/reviewer` заходит; `Accountable owner` и `QA sign-off` — всегда человек. Не давай Pi `Assess` без `Verify`.

**Где не заходит совсем:**
- High-risk sign-off (auth/payments/data) — Pi может `reviewer`, но `Accountable` и `QA sign-off` — только ты (PR block).
- `specs only` мечты — SlopCodeBench показал 0/15 end-to-end даже с идеальной спекой, без persistent comprehension.

**Быстрый старт (для твоих 4 задач):**
1. Методика: `Ask oracle to review mutation-matrix-full.md — challenge C/P partition and per-risk-tier gate, then run parallel reviewers (correctness, test design, simplicity) max 3 rounds.`
2. Статья: `Use reviewer to review Article 26 draft against tech-writer skill; ask oracle to challenge thesis.`
3. Вакансия (оценка): `Use researcher to pull vacancy details, then oracle to challenge my fit: Head vs IC? Serbia?`
4. Вакансия (подготовка): `Use scout to map vacancy JD + company, then worker to draft STAR answers, then reviewer to check each answer would fail if story were wrong.`

---

**Файлы:**
- `outputs/plan-beyondquality-pi-2026-09-03.md` (этот файл)
- `wiki/beyondquality-ai-era-testing-2026.md:1` (91) + `wiki/slopcodebench-2026.md:1` (97)
- `wiki/pi-subagents-2026.md:1` (93) + `wiki/pi-opencode-integration-2026.md:1` (117)
- `~/.pi/agent/settings.json` (global free-first) + 7× `AGENTS.md` (Articles, ai-qa-wiki, qa-automation-sandbox, DYI-Building, MAS-realisation, OrangeHRM, Test-Dora-Plus)

*Подтверди время обсуждения (04.09 18:00 или 05.09 10:00) — поставлю в календарь и запущу Pi oracle заранее.*

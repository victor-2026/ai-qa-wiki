# Пилот: рецензирование статьи через Pi (OpenCode Desktop 1.18.27 + Pi 0.84.4)

**Цель:** проверить, что Pi `reviewer`/`oracle` ловит `looks fine` ≠ `is right` для LinkedIn статьи, не тратя human время на 1-й проход. Пилот 1 статья, 60-90 мин.

**Вход:** черновик `Articles/linkedin-posts/AI-Agents/XX-draft.md` + `tech-writer` skill (SKILL.md: hook ≤100, money ≤150, ≤9 emoji / ≤4 data-heavy, 3-5 CamelCase hashtags, author line, 1200×644 cover обязательна).

**Стек:** Pi 0.84.4 + `pi-subagents` 0.64.0 (`~/.pi/agent/settings.json: openrouter/free` → fallback paid, 20 RPM/1000д), OpenCode Desktop 1.18.27 (тот же CLI, `pi` доступен в его bash).

---

## Шаги (копируй промпты в чат Desktop)

**0. Подготовка (5 мин, ты):**
- Статья в `Articles/linkedin-posts/AI-Agents/XX-draft.md` (уже есть, напр. `21-conways-law-qa-draft.md`)
- Убедись `AGENTS.md` в проекте содержит `## Subagents & OpenRouter — Free First` (уже в 7 проектах, 2026-09-03) — иначе Pi пойдет на платный.

**1. Scout (опционально, 5 мин) — если статья про новый домен:**
```text
Use scout to inspect Articles/linkedin-posts/AI-Agents/XX-draft.md and the tech-writer skill, then list risks: where thesis is vague, where evidence is missing.
```
→ Pi `scout` мапит файлы, entry points, риски. Проверь его вывод — он твой `comprehension` artifact.

**2. Reviewer — 1-й проход (10 мин, Pi):**
В Desktop чат:
```text
Use reviewer to review Articles/linkedin-posts/AI-Agents/XX-draft.md against tech-writer skill. Check: hook ≤100, money paragraph ≤150 with strongest number, ≤9 emoji, 3-5 hashtags, author line, cover 1200×644, evidence vs claim (does green prove?), and thesis clarity. Report P0/P1 with file:line.
```
Или напрямую в терминале Desktop (bash tool):
```bash
pi --provider openrouter --model openrouter/free --print "Use reviewer to review Articles/linkedin-posts/AI-Agents/XX-draft.md against tech-writer skill." -- @Articles/linkedin-posts/AI-Agents/XX-draft.md
```
→ Pi `reviewer` вернет `P0 BLOCK` / `P1` с `file:line` (как в тесте `app.js` 2×P0 — тот же механизм). Ожидай 2-5 находок.

**3. Oracle — challenge thesis (10 мин, Pi):**
```text
Ask oracle for second opinion on my plan/thesis in XX-draft.md. Challenge assumptions: does it really test the testing tool or just describe it? What might I be missing (counter-example where my gate fails)?
```
→ `oracle` не правит, только ставит под сомнение (как в BeyondQuality `oracle` = вторая эпистемическая позиция). Это ловит `self-preference` (Keith Klain).

**4. Parallel reviewers — 3 взгляда (15 мин, Pi, опционально):**
```text
Run parallel reviewers: one for correctness (thesis/evidence), one for tests (would tests fail if bug were real?), one for unnecessary complexity (can we cut 20% without losing meaning?).
```
→ Синтез как в тесте 3/3 BLOCK — три вердикта, где сходятся — точно фиксить.

**5. Worker — правка (15 мин, Pi или ты):**
```text
Have worker implement the reviewer feedback for XX-draft.md, then run reviewers again and apply feedback. Max 3 rounds.
```
→ `worker` правит, `reviewer` перепроверяет (`review-loop`). Лимит 3 раунда = `maxSubagentSpawnsPerRun=64` не даст разбежаться. Или правь сам — быстрее если правок <20%.

**6. Human gate — финальный sign-off (10 мин, ты):**
- Ты — `Accountable owner` (Julia Pottinger `who-validates`): можешь ли объяснить thesis в 1 абзаце без перечитки Pi-саммари? Есть ли тест/пример, который бы покраснел если thesis неверен? Готов ли к 2am вопросу?
- Проверь визуал (Pi не видит UI — `why-ai-cannot-see-your-ui`): cover 1200×644, скрин `21-org-drift.png` — смотри глазами.
- Добавь PR блок (если статья в git):
```md
## AI-assisted change
- Generated with: Pi reviewer/oracle (openrouter/free)
- Accountable owner: @victor (understands, owns rollback)
- What it does: ...
- Risk if wrong: ...
- Evidence it works: reviewer P0 fixed, oracle challenged
- QA sign-off: @victor
```

**7. Фиксация (5 мин):**
- Сохрани `outputs/pilot-article-XX-review-log.md` — логи Pi (reviewer P0, oracle challenge, parallel synthesis). Это твой `agentic lineage` для audit (как у Zalando).
- Закоммить `Articles` с `feat: XX draft reviewed via Pi reviewer (2 P0 fixed)`.

---

## Критерии успеха пилота (через 1 статью)

- Pi нашел ≥2 P0/P1, из них ≥1 ты бы сам пропустил (проверка add).
- Oracle дал ≥1 валидный контраргумент к thesis (не тавтология).
- Время: твой 1-й проход 60 мин → с Pi 20 мин твоего + 15 мин Pi (экономия 25 мин, но главное — 2-я позиция).
- Fallback: если Pi на `:free` уперся в 429 (20/мин, 1000/день) → автоматом `openrouter/*` платный (уже в `~/.pi/agent/settings.json: enabledModels`).

## Где не заходит (из `outputs/plan-beyondquality-pi-2026-09-03.md`)

- Pi не решает `High-risk sign-off` — ты всегда `Accountable` (auth/payments/data — только ты).
- Pi не судит визуал — cover/layout смотри сам.
- Не гоняй Pi пачками статей без verification layer — `plausible but subtly wrong` (BeyondQuality).

## Быстрый старт прямо сейчас (Desktop)

Открой Desktop → проект `Articles` → чат:
```
Use reviewer to review Articles/linkedin-posts/Quality-Operating-Model/27-guided-qa-engineer.md against tech-writer skill. Focus on evidence vs claim.
```
→ жди `Review Results` с `file:line` → `Ask oracle to challenge thesis` → правишь.

---

*Пилот 1 статья = 1 час. Если зайдет — масштабируй на `Articles` backlog, иначе откат без затрат (Free First).*

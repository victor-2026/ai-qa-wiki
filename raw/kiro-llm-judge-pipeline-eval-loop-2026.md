# Kiro LLM-judge pipeline — eval loop on real conversations (-32% behavioral issues)

**Источник:** Kiro (company page), LinkedIn ~2026-08. Пост + breakdown по ссылке spr.ly.
**Контекст:** у нас есть Kiro catalog (9 wiki). System prompt behavior hard to predict — инструкция, нормальная в изоляции, ломается в непредвиденных кейсах.

---

## Метод: judge pipeline на живых разговорах

Замкнутый повторяющийся loop:
1. **Diagnose complaint patterns** — из реальных разговоров Kiro извлекают паттерны жалоб.
2. **Design targeted fixes** — точечные фиксы под паттерн, не общий рерайт промпта.
3. **Test in cohorts** — проверка на когортах.
4. **Evaluate with the same rubric every time** — один фиксированный рубрикатор на все итерации.

## Цифры

- 27 кандидатов screened по осям: safety, verification, tone, behavior.
- Behavioral quality issues на Kiro CLI: **-32%**.

## Связки с нашей работой

- Verification как отдельная ось judge — четвертое независимое появление verification-темы за неделю (Jay, Radik, Osmani, Kiro). Ось зреет в индустриальный стандарт.
- «Same rubric every time» = ответ на drift оценки: фиксированный рубрикатор как аналог mutation allowlist / tiered thresholds (наши B0-B3). Без фиксации нельзя сравнивать итерации.
- Complaint-pattern-driven фиксы = тот же принцип, что gotchas log и learned_patterns: чинить по наблюдаемым failure modes, не по гипотезам.
- Cohort testing = сэмплинг-прогоны (наш ~20/прогон в wiki) — та же экономика замера.
- -32% — кандидат в money paragraph коллекцию (рядом с 7,000 commits, 40 мин - 2 часа).
- Engagement: нет standing, vendor пост. Только evidence. Breakdown по ссылке — кандидат на ингест при случае (проверить детали рубрики).

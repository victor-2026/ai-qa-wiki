# Addy Osmani (Anthropic) — skill decay, verification is the floor

**Источник:** Addy Osmani, Member of Technical Staff at Anthropic, LinkedIn ~2026-09-08. Пост + ссылка на free write-up про экспертизу.
**Тезис:** AI short-circuit-ит путь к интуиции (тысячи часов дебага, diffs, борьба с абстракциями). Получаешь готовую задачу, но пропускаешь reps. Риск — skill decay: качаем промптинг, теряем экспертизу, нужную чтобы верифицировать output, когда assumptions больше не ложатся на систему.

---

## Три практики deliberate mastery

1. **Hypothesis first.** Перед промптом — предсказать, как решение должно выглядеть или где архитектура сломается.
2. **Anchor on explanation.** Использовать агентов не только генерить новое, а разбирать существующие кодбазы. Объяснение чужой сложной логики строит ментальную модель быстрее, чем «напиши это».
3. **Codify the lessons.** Не давать learnings умирать с закрытием чата. Превращать исправленные assumptions в linting rules, documentation, tests в репо — чтобы выиграли и ты, и следующий агент.

## Ключевые формулировки

- «Verification is the floor. Imagination is the ceiling».
- «AI can build the feature, but it won't teach you the lesson unless you force it to».
- Agents/loops/software factories как «code vending machines» — путь к severe skill decay.

## Связки с нашей работой

- Verification as floor = обоснование attestor-роли: если экспертиза верифицировать атрофируется, green light держать некому. Ответ Evans (market value of testing): ценность = способность сказать «нет» обоснованно, а она требует reps.
- Codify the lessons = наш существующий loop: gotchas log в memory, learned_patterns.json в MAS, checkpoint append-only. Osmani независимо описывает ту же архитектуру памяти. Можно цитировать как внешнее подтверждение.
- Hypothesis first = научный метод в тестировании; ложится рядом с per-risk-tier step 0 (relevance gate): сначала предсказание, потом прогон.
- Engagement: standing нулевой (Anthropic, огромный аккаунт) — только как evidence в статьях, без outreach. Цитаты-кандидаты в Article 27 / attestation-материалы.
- Brownfield zones + characterization tests → wiki: `wiki/addy-osmani-brownfield-agentic-engineering-2026.md`

# CARBON (testers.ai) — Plan апробации

**Цель:** оценить steering + evidence layer, сравнить с QAEverest подходом

**Источник:** Jason Arbon post (28.08.2026), testers.ai CARBON beta

## Что такое CARBON
- **Intent-based тесты** — AI учит код/UI/API/AI features, создаёт risk-ranked тесты
- **Steering** — 9 widgets, настраиваешь что запускать
- **Local by default** — определение локально, cloud для масштабирования
- **30 AI agents** на отчёт (security, accessibility, performance, privacy)
- **SKILL.md** — работает в Claude Code, Cursor, ChatGPT
- **Evidence** — скриншоты, network traffic, console, traces + confidence score
- **Pricing**: Free (1 credit), Pro $79/mo (100 credits), Team $249/mo (300 credits)

## План
1. Выбор URL (sandbox / buzzhive / публичный сайт)
2. Steering plan: features, checks, personas, test cases, exploratory bots
3. Запуск + сбор evidence
4. Сравнение с QAEverest (таблица)
5. Вопросы для оценки

## Вопросы для оценки
- Caught bugs vs false positives?
- Persona feedback полезен или generic?
- Можно ли интегрировать mutation testing поверх CARBON?
- Стоит ли $79/mo для ongoing использования?

## Следующий шаг
- Какой URL тестировать? Или начать с sandbox?

## Сравнение: CARBON vs QAEverest
| Критерий | CARBON | QAEverest |
|----------|--------|-----------|
| Steering control | 9 widgets, настраиваешь | Пассивный (import + watch) |
| Evidence | Скриншоты, traces, network | Скриншоты, page diffs |
| Mutation testing | ❌ Нет | ✅ Есть (M2-M9) |
| Confidence score | Внутренний | Внутренний |
| Human gate | Steering = human gate | Human approval step |
| Price | $0 (free) / $79/mo | Нет прайса (vendor) |

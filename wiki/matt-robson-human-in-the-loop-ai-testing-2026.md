# Human-in-the-Loop: The Missing Layer in AI-Driven Testing — Matt Robson

**Автор:** Matt Robson (AI, Agile & Quality Transformation | Virtuoso QA)
**Дата:** 27 Aug 2026
**Источник:** LinkedIn post (Matt Robson)
**Статья:** Human-in-the-Loop: The often Missing Layer in AI-Driven Testing (blog, August 27, 2026)

---

## Ключевой тезис

«AI generates, humans govern» — легко сказать, трудно построить. Если oversight = экран, который никто не читает — это не oversight, а бумагажная волокита. И хуже: в аудите написано «человек согласился».

## Ловушка объёма

Если дать человеку 1000 сгенерированных тестов на approval — он их все одобрит. Не по халатности, а потому что задача по дизайну невозможна — единственный способ закончить — перестать читать.

**Вопрос не «есть ли human in the loop?», а «что именно мы просим человека сделать?»**

- ❌ «Here are 40 tests, tick to accept» = форма
- ✅ «Here is what changed, coverage that exists, the gap, and the proposed test» = что-то полезное

## Что ценного делает QA

Не writing scripts, а решения: какие из 40 failures важны до пятницы, что значит «customer must be notified» (email/push/audit log), какой acceptable risk для бизнеса/регулятора.

Это judgement — из контекста, которого у модели нет (история, политика, знание где система кусается). Единственная часть процесса с accountability — «agent generated it» не принимается как ответ.

## 4 вопроса к вендору

| Вопрос | Суть |
|--------|------|
| Reviewable change? | Каждое AI-действие = конкретный diff |
| Named approval? | Человек идентифицирован, прикреплён к решению |
| Auto-accept off by default? | Включать для low-risk, начинать с review |
| Explainable? | Каждый тест → requirement, document, business rule |

## Ключевая мысль

Review step = единственное место, где экспертиза организации записывается. Без review step знания сидят в головах 2-3 людей и уходят с ними. С review step — становится durable, versioned, available.

## Метрики

- Tests approved (не сгенерировано)
- Traceable к requirement (не raw coverage)
- Сколько времени команды на judgment vs repetitive validation

## Compliance

DORA, Consumer Duty, NIS2, 21 CFR Part 11 — named human approval + audit trail = licence to operate.

---

## Связи с AI QA Wiki

- `ai-productivity-paradox-verification-layer-2026.md` — Verification layer
- `ai-qa-evidence-layer-validation-evals-guardrails-telemetry.md` — Evidence layer + human review
- `ai-qa-tool-evaluation-mutation-matrix.md` — Mutation matrix как independent signal
- `software-testing-weekly-newsletter-2026.md` — Issue #325 (Testing Mindset — Keith Klain,相同的 тема)

## Добавлено

2026-09-01
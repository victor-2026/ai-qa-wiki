---
title: "Jason Arbon: How AI Tests Software (бета: AI Checks, AI Tests, AI Test Harness, AI Confidence)"
source: https://howaitestssoftware.com (private review copy, free edition, 2026-09-20) + howaitestssoftware.com
author: Jason Arbon (Jank.AI / IcebergQA, past: Bing QA lead, Google, test.ai)
date: 2026-09-20 (private review draft, first reading draft)
created: 2026-09-20
tags: [ai-testing, ai-check, ai-test, ai-test-harness, ai-confidence, intent, evidence, oracle, bounded-adaptive-exploration, jev, metamorphic-testing, synthetic-populations, independent-validation, release-confidence]
aliases: [How AI Tests Software, Arbon HATS, AI Test Harness, AI Confidence]
---

# Jason Arbon: How AI Tests Software (first reading draft, 2026-09)

**Источник:** private review copy (337 стр., free edition, PDF с unlock code от автора через LinkedIn DM 2026-09-20). Полный текст извлечён (765K chars). Саммари и разбор для пилота: `../../Private/Positions-CV-CL/outreach/active/Jason_Arbon/book-summary.md` (вне wiki, private).
**Контекст:** книга - флагманский текст Арбона по agentic testing. Дополняет заметки Bolton/Bach (evidence discipline) и Jev в Playwright (Appendix D книги содержит расширенный разбор того же эксперимента).

## Пять официальных терминов (главный фреймворк книги)
1. **AI Check** - неинтерактивная инспекция артефактов (screenshots, console, network, DOM/accessibility, traces). Не водит юзер-джорни, не меняет state. Высокий ROI, легко встроить.
2. **AI Test** - интерактивная, функциональная, часто stateful проверка (browser/device/API/DB/CLI). Сохраняет что сделал и что произошло.
3. **AI Test Framework** - bounded executor одной категории (browser, mobile, API): intent -> действия на поверхности; не владеет всем workflow.
4. **AI Test Harness** - долгоживущая stateful QA-система вокруг Checks/Tests/Frameworks: контекст, риск, authority, durable state, evidence, challenge, learning, reporting, repeatability. Может стартовать с незнакомого репозитория, рулить под-агентами, считать AI Confidence.
5. **AI Confidence** - evidence-qualified суждение о шпимости. НЕ test count, НЕ model вероятность, НЕ "looks good". Вопросы: репрезентативность и независимость свидетельств, что осталось неизвестным, severe/stale/nosiy failures, лучше ли чем предыдущая версия, какое следующее evidence изменит решение.

## Центральный тезис
AI поглощает тест-фреймворки, CI/CD, test management, issue trackers, dashboards как "reasoning surface". **Durable artifact = intent** (обещание, риск, evidence requirement, authority boundary, результат меняющий решение), а не selectors/scripts/ticket-fields. Фреймворк генерируется и выбрасывается; абстракция поднимается вверх.

4 причины: (1) AI не нужны human-артефакты для рассуждения; (2) инвестиционная асимметрия (56 активных коммиттеров Selenium vs thousand+ инженеров frontier labs); (3) LLM обучены на человеческом поведении = близко к работе тестировщика (emulate user, defend user, judge); (4) экономика: 10x дешевле за год + Jevons paradox (падает unit cost -> растёт объём meaningful verification).

## Ключевые концепции
- **Evidence-qualified testing:** conclusion привязано к именованному прогону и артефактам; hypothesis vs confirmed vs not established + назвать evidence которое изменит вывод
- **"Not established" != "не может"** - дисциплина сравнения человек/AI (гл. 26)
- **Green dashboard trap:** "trusting a green UI while downstream state is wrong" (гл. 17) - и "Works as written. Still feels wrong." (гл. 27)
- **Варьируй exploration, не obligations** - модель может выбирать путь, но не определение success (гл. 29)
- **Repeatable finding vs observation:** "task disappeared" необходимо сузить до state-последовательности, механизма, promise, воспроизводимости (гл. 26)
- **Self-healing is backwards:** чинить testability boundary, не учить переживать поломку (гл. 15)
- **Bounded repair:** фикс надо предел кол-ва попыток; никогда не ослаблять oracle и не retry till green (гл. 31)
- **Independence of validation:** creator не может быть единственным оценщиком; независимая validation-plane (свои модели, evidence, ledger) как аналог дои inspectтора моста (гл. 33)
- **Test moves inside the software:** тест = durable claim рядом с running software; validation как отдельная инфраструктура cloud-scale; validation compute > 80% в зрелых AI-циклах
- **Confidence is the hard problem of AI:** релизная граница, не генерация тестов

## App. D (Jev): результаты эксперимента
- 63 probes / 24.3s, 126 API calls, median HTTP 131ms; controller сбрасывает storefront между проходами
- 21 flagged по 5 seeded defect families, НЕ 21 уникальный баг
- $80 lamp -> 10% coupon once -> 72; повторный coupon -> 64.80; Jev: bug prob 0.97, confidence 0.95, judgment 121ms
- **Near-tie = unresolved, не вердикт:** valid-email checkout получила 0.49 expected / 0.47 bug; controller показал победителя, abstention rule отсутствовала = weakness harness; "a 49-51 split is confusion, not a verdict"
- Числа 0.95/0.97 - не калиброванные доверительные интервалы; калибровать на независимо размеченных примерах
- Jev не смотрел скриншоты - только текст + структурированные наблюдения
- Quantity 999 accepted (лимита верхнего не было), zero/negative prohibited (явно)
- Локально-приемлемое действие != корректное глобальное состояние (inherited discount error оставался в total после add-to-bag)
- Схема: fast decision model как компонент внутри управляемой системы; не заменяет release decision; literacy: сохранять raw response, threshold policy, before/after, действие; auditable execution record != explanation internal reasoning

## Связи с нашими темами (mutation matrix / VerdictGate / per-risk-tier)
1. **Gap книги = mutation-based proof.** Arbon описывает challenge, independence, seeded defects (leaderboard, workshop), но НЕ превращает fault-injection в методику оценки чувствительности качественной системы. Наш per-risk-tier + mutation matrix (B0-B3, операторы, sensitivity runs) = недостающая глава. Рабочий angle для feedback Jason.
2. **Confidence Testing (гл. 21-25)** = близкая сестра нашего per-risk-tier gate: вопрос что должно быть установлено до релиза, threshold привязан к риску, "crisp zero" для критичных инвариантов.
3. **Near-tie abstention** (Jev 49/51) = наш принцип "crisp zero / не вердикт при узком маржине" в действии. Arbon сам назвал отсутствие abstention-правила слабостью harness - валидация нашего подхода.
4. **Six views leaderboard** (Overall/F0.5/Discovery F0.5/Precision/Recall/Groundedness) - эволюция от одного score к многомерной оценке модели-тестера; близко к нашей идее многомерного scorecard.
5. **"Humans define what correct means, model chooses the path"** - второе крыло нашего "humans govern the evidence": если FlowScout = честный discovery (не изобретает expected), то Jev-архитектура показывает управляемую верификацию вердиктов.

## Anti-patterns (из книги)
1. Одно артефакт = universal proof (создавать богатый evidence bundle)
2. Просить AI маленькие вопросы и получать маленькие ответы (small-question trap)
3. Dashboard-polished reports врут про выполнение ("Do not let a polished transformation dashboard imply that anything executed")
4. Self-testing без независимого давления = self-approval
5. Превращать 0.49/0.47 в уверенный баг (near-tie = unresolved)
6. "Наш AI healed it" без показа original failure и evidence модели

## Статус и следующее
- Заметка создана 2026-09-20 после полного чтения (337 стр.).
- Решение по thank-you list: открыто (публичная видимость в AI-QA комьюнити).
- Потенциальный feedback Jason: (1) mutation/fault-injection слой в методологию Harness (глава), (2) abstention rule для near-tie в decision-моделях.
- Книга: first reading draft, часть claims требует публичной верификации (TODO стр. 5 самого автора), free edition содержит промо CARBON/IcebergQA/Jank.ai; paid убирает промо, не метод.

## Связанные заметки
- [[bolton-bach-llm-sandwich-hygiene-protocol-2026]] - evidence discipline, "unreproducible = doesn't count"
- [[jev-jason-arbon-playwright-bounded-exploration]] - тот же Jev-эксперимент, но по статье/анонсу
- [[zalando-agentic-engineering-snapshot-2026]] - risk-based PR approval ≈ per-risk-tier gate
- [[kiro-blog-catalog-all-publications-2025-2026]] - continuous-prompt-evaluation и другие vendor-каталоги
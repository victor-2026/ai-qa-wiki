---
title: "Jason Arbon: Jev в Playwright-цикле (bounded adaptive exploration)"
source: https://jarbon.substack.com/p/i-put-jev-in-a-playwright-browser (Substack, Paid) + LinkedIn-анонс Jason Arbon (Jank.AI / IcebergQA), 2026-09-20
author: Jason Arbon
date: 2026-09-19 (эксперимент/публикация Sep 2026)
created: 2026-09-20
tags: [llm-testing, structured-decisions, jev, typesafe, playwright, bounded-adaptive-exploration, oracle-design, human-judgment, verdict]
aliases: [Jev Playwright Loop, Bounded Adaptive Exploration, Jev Structured Decisions]
---

# Jason Arbon: Jev в Playwright-браузере (2026-09)

**Источник:** Substack Paid-статья Arbon "I Put Jev in a Playwright Browser Testing Loop. It's fast, but..." + открытый LinkedIn-анонс (4 часа до capture). Демо: 63 browser probes за 24.3 сек.
**Доступ:** только анонс + открытая часть; полный разбор результатов - Paid, недоступен для нас. Контекст: ещё не открыли широкий доступ к самому Jev - только анонсы.

## Суть

Jev - модель TypeSafe AI для **структурированных решений**: на вход state + question с заданным форматом ответа, на выходе - значения, которые софт потребляет напрямую. В демо: action names, verdicts, probability distributions. API также поддерживает rubric scores и yes/no вероятности (choice, score, noul). В прогоне - jev-1.13.0.

## Архитектура (два Jev-вызова на probe)

1. **Первый вызов:** какую probe-операцию исполнить дальше (выбор действия из доступных в текущем state)
2. **Второй вызов:** вердикт - нарушает ли наблюдаемый результат requirement

| Компонент | Роль |
|-----------|------|
| Storefront (HTML/CSS/JS) | приложение под тестом, включая deliberate defects |
| Node.js контроллер | requirements, меню доступных действий, история, цикл |
| Playwright | водит Chromium, читает страницу и значения форм |
| Jev API | выбирает действие, затем классифицирует результат |
| Dashboard | действия, тайминги, вероятности, вердикты |
| Recording + FFmpeg | MP4 для показа |

**Ключевые ограничения:** Jev НЕ смотрит на запись и НЕ инспектирует скриншоты в этой реализации. Контроллер шлёт только текст страницы и структурированные наблюдения: названия продуктов, количества, total, поисковые запросы, email, status-сообщения.

## Главная идея: bounded adaptive exploration

- Язык действий и selectors заранее определены человеком: "попробуй negative quantity", "негативный email", "повтори тот же coupon"
- Проба доступна только если применима в текущем state (quantity - когда товар в корзине; reapply coupon - после первого применения)
- Модель выбирает **последовательность**, код определяет **доступные ходы и смысл "правильного" поведения**
- Не генерация произвольного тест-кода, не discovery незнакомого сайта

> Модель выбирает последовательность, а наш код определяет доступные ходы и значение корректного поведения.

## Почему это важно для темы Виктора

1. **Оракул во владении кода, не модели** - вторая half "humans govern the evidence": Jev лишь вердиктует по правилам, которые задал человек. Тот же дизайн-принцип, что в заметке Bolton/Bach (sober/literal) и FlowScout ("не выдумывает ожидаемый результат"), но с другой стороны: FlowScout = discovery (что есть), Jev = verdict (правильно или нет) по заданным правилам. Вместе покрывают обе грани верификации.
2. **"It's fast, but..."** - сигнал про "but". Открытая часть заявляет только скорость и архитектуру. Вопрос "ловит ли Jev реальные deliberate defects" (= чувствительность, не только скорость) остаётся НЕ показанным - та же грань "green ≠ verdict", только в скорости. Проверять чувствительность, а не брать на веру.
3. **Jev доступен локально в opencode (opencode/jev-1.13, opencode/jev-1.13-free)** - эксперимент Arbon можно воспроизвести независимо, когда дадут доступ к Jev API.
4. **Вердикты + вероятности** - готовый объект для mutation-проверки: сидять ли вердикты Jev на известных мутациях (как QAEverest sensitivity runs).

## Anti-patterns

1. Покупать "быстро" как "хорошо" - скорость без продемонстрированной чувствительности не есть evidence
2. Считать, что модель "тестирует" - в этой архитектуре модель решает, а не верифицирует по-своему; правила и оракул человеческие
3. Путать "exploration" с "discovery" - здесь исследование ограничено заданными пробами, это не поиск всех юзер-флоу (в отличие от FlowScout)

## Открытые вопросы
- Чем вердикт Jev отличается от простого keyword-match на status-сообщениях? (насколько вердикт информативен)
- "but..." из заголовка - чего именно касается (скорость против качества, хрупкость проб, cost)
- Jev verdicts чувствительны к известным мутациям? (нет публичных данных - анонсы)

## Статус
- Заметка-референс. Jev API пока без широкого доступа ("только анонсы") - самопроверка отложена до получения доступа
- Арбон типа: IcebergQA/Jank.AI на радаре (STARWEST)
- Потенциальная статья: bounded adaptive exploration как компромисс между free-form AI-тестами и детерминированными мутациями




<!-- backlinks-start -->
### Backlinks
- [Jev Openai Proprietary Beaten Open Source 2026](wiki/jev-openai-proprietary-beaten-open-source-2026.md)
- [Opencode Jev 113 Free System One Model 2026](wiki/opencode-jev-113-free-system-one-model-2026.md)
- [Ruben Hassid Jev Internet Moment Setup 2026](wiki/ruben-hassid-jev-internet-moment-setup-2026.md)
<!-- backlinks-end -->

# Colantonio/Selvaraj — perf testing value reframed as AI-cost savings

**Источник:** Joe Colantonio (TestGuild, vendor-neutral since 2010), LinkedIn 2026-09-15. Разговор с Kandasamy Selvaraj, полный эпизод: https://lnkd.in/eBMMr8d4 (не разобран — мясо там).

---

## Тезис поста

- Классическая боль perf testing: value не переводится на язык бизнеса (response times никого вне инженерии не греют).
- С AI появляется cost-измерение: тестирование показывает, что запросы можно роутить на smaller model, резать tokens, убирать unnecessary work без потери outcome → management видит actual savings.
- Разговор о ценности performance engineering становится другим.

## Связки с нашей работой

- Частичный ответ на Evans («market value of testing unknown»): для perf value = доллары на токенах. Формула для копилки.
- Пара к Osmani digest #7 (Databricks efficiency frontier, $80/day HN): там supply-side (как резать), тут demand-side framing (как продать экономию менеджменту).
- Наша lived-практика (OpenRouter guard 1$/день, tripwires) — тот же разговор в миниатюре; при случае quotable как indie-кейс cost discipline.
- Эпизод по ссылке — кандидат на разбор при наличии времени (интересует: конкретные цифры savings, методология замера).

# TesterArmy-B pilot brief (for W1 decision, W3 execution)

W5 → W1: бриф ниже — продукт, факты с провенансом, опции решения, done-критерии, предусловия. Вслепую не решать — все цифры ниже помечены чьи. Исполнение за W3 после твоего решения.

## Что за продукт

- **TesterArmy (YC P26):** QA-агенты, тестирующие web + mobile как реальный юзер, CI-native до мержа, отчет со скриншотами/записями. 2-10 чел, Wilmington DE. Лица: Szymon Rybczak, Oskar Kwaśniewski. Pre-seed $1.2M (Script Capital, Eight Capital, AIP Seed + ангелы Rauch/Cheever/Yan/Browne/Rocha) — все из их LinkedIn-постов, независимого подтверждения нет. Wiki: wiki/testerarmy-qa-agent-yc-p26-2026.md.
- **Новое (Oct 2026, триггер брифа):** e2e — open-source AI test framework (команда Oskar, via STW #329 https://softwaretestingweekly.com/issues/329/): цель на английском → агент действует → детерминированные ассерты; remember + replay без повторного вызова модели. Сайт https://tester.army/e2e, доки https://e2e.tester.army/docs. Hands-on не проводился никем из нас.
- **Рядом:** MIT-тулсет (терминал-клиент, OpenAPI-тестер, trace viewer, npx + agent skill), unbox-ai токен-дебаггер ("310,800 tokens in, 2,300 out — 135:1 is normal for an agent loop", их anecdote).
- **Кейс Juno (ИХ маркетинг, не наш факт):** "10x faster shipping", "58% more PRs merged", "2 days/week → 0" ручного QA. Цитировать только с пометкой company-claimed.

## Почему сейчас

OSS-релиз e2e = нулевая цена входа (npx, без денег и шаринга данных) + два проверяемых клейма (remember/replay без модели; детерминированные ассерты поверх агента). Идеальная мишень под Article-26 линзу: seeded breaks как проверка проверяющего.

## Опции решения

- **A — light hands-on (рекомендую):** только e2e OSS, только staging, 2 засеянные поломки. Выход: ловит/нет + evidence + цена прогона в токенах (проверить их 135:1 на нашем стенде) + Unable-to-Verify policy. Оценка веса: часы, не дни.
- **B — watch:** без пилота; держать через STW-дайджест (уже в пайплайне) + ручной вотч LinkedIn персоны (машинного RSS у них нет). Триггер на A: их regression-заявление с числами или наш staging-слот.
- **Не предлагаю:** managed-сервис (деньги + данные наружу + чужой контур) — только после A.

## Пилот-критерий (done = ?)

1. Staging-мишень подтверждена (твое условие, без мишени пилота нет).
2. Отдельный неймспейс (свой стенд — правило клонов).
3. Прогоны: remember/replay кейс (второй прогон без модели — факт?) + 2 seeded breaks (ловит ли?).
4. Замер цены: токены in/out на прогон, wall-clock.
5. Выход: вердикты с evidence + решение go/no-go на e2e как инструмент + цитатность (что можно тащить в статьи, что нет).

## Предпосылки

- Staging-приложение с известными багами (2 шт под seed).
- Node/npx; стенд доступен исполнителю.
- Reviewed branch (агент реально кликает UI).

## Не делать

- Не гонять на проде (агент выполняет реальные действия).
- Не смешивать с D6/бенчем без реприоритезации (очередь твоя).
- Цифры Juno ($1.2M вне поста, 10x/58%/2d→0) — не наши, не цитировать как факты.
- Managed-сервис TesterArmy — вне скоупа этого брифа.

## Источники (наши wiki)

- wiki/testerarmy-qa-agent-yc-p26-2026.md (профиль + Oct-2026 e2e секция).
- wiki/qawolf-6-types-self-healing-2026.md (self-healing таксономия для сравнения remember/replay).
- STW #329 https://softwaretestingweekly.com/issues/329/ (первоисточник релиза в ленте).

---
*W5 → W1. Статус: DECIDED x2 (B-watch + park/auto/deferred, 07.10) — отсутствие движения корректно, реле закрыт.*

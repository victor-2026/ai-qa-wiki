# Vipul Verma call prep — 20 min peer exchange (2026-10-04)

## Logistics
- Format: 20 min, notes compare. He sends slots + link. You are CEST (Serbia).
- Lane: peer exchange, joint taxonomy. No commerce, no pricing, no promises, no pilot commitments on the call (W1 track).

## What he brings (his words, 04.10 1:28 AM)
- Running seeded breaks in practice. Validating their own grader right now.
- Offers to show Agent Assurance incl. where it says Unable to Verify.
- Thread context: false-pass vs coverage-gap split (your deep replies #1-2, liked, warmth confirmed per W1 eaaa78d).

## What you show (seeded side, method level only)
1. Taxonomy per seeded mutant: Caught (test failed, counts) / Observed-only (names the mutated element but stays green, does not count) / Survived (silent, gate-relevant). Only Caught counts toward score. Score reported per tier, never blended.
2. Tiers B0-B3 (mirror of risk engine): B0 Critical (payment/auth/credential, 0 survived tolerated, target 100%, two consecutive passing runs for sign-off) / B1 High (core journeys, 0 tolerated, vendor default 80%) / B2 Medium (secondary, band max 1 survived at small N, vendor default 1-per-60) / B3 Low (trend-only, never blocks).
3. No-op rule: a survivor that changes nothing observable is a seeder defect (refused pre-seed, outside N), never an accept-risk case.
4. Evidence you can cite: B0 sign-off day 07/09, 100% x2 rotations (checkpoint 2026-09-07); per-run evidence packs (HTML + execution PDFs pattern from Letter 2).
- Source of truth if he asks deep: per-risk-tier-framework.md v0.3 FROZEN (Positions, Rupesh catalog). Share method, not Rupesh commercial internals.

## What you ask (his Unable-to-Verify — this is the prize)
1. Which cases land in Unable to Verify today? (ask for 2-3 concrete classes, not the count)
2. What moves a case OUT of Unable to Verify? (exit criteria: whose decision, what evidence)
3. How are they validating their own grader? (seeded set like ours, or human labels, or prod incidents)
4. Who owns the false-pass vs coverage-gap split on their side? (terminology handshake for joint taxonomy)

## Guardrails (say / don't say)
- SAY: method, tiers, taxonomy, no-op rule, staging-only scope.
- DON'T: Rupesh commercial terms, QAEverest internals, promises ("we will verify you"), pricing, timelines.
- If he pitches a pilot: "interesting, let me take it back and come back written" — no yes on the call.

## After the call (capture immediately, 3 lines for W2 ledger)
1. Which Unable-to-Verify cases he showed (classes).
2. Their exit criteria (verbatim if possible).
3. Follow-up agreed (if any) + who sends first.
- Route: 3 lines → W2 (verdict-economics ledger) + W1 (card). Possible Article angle B (break-the-judge) if cases are juicy.

---

## Приложение A. Что уже сказано в переписке (подробно, по-русски)

> Пометки источника: VERBATIM — дословный текст есть у нас (паста от 04.10).
> PARAPHRASE — вербатима нет, пересказ по чекпоинту (не цитировать вовне).

| # | Кто / когда | Что сказано (подробно по-русски) | Источник |
|---|-------------|----------------------------------|----------|
| 1 | Victor, паблик-тред (comment #1, под постом Vipul про Agent Assurance) | Похвалил фрейминг — особенно "weakest evidence" и assurance gap рядом с pass rate, никогда не засчитываемый как проход: именно этой дисциплины не хватает большинству eval-сетапов. Добавка с нашей стороны: effect-grading спариваем с seeded breaks, о которых харнесс не знает. Если вердикт пережил подсаженные поломки — pass rate что-то значит; если нет — это коррелированная уверенность. Effect grading говорит, что случилось; seeding — бодрствовал ли грейдер. Оригинал: "Strong framing — especially "weakest evidence" and the assurance gap reported beside the pass rate, never counted as a pass. That's exactly the discipline most eval setups skip. One addition from our side: we pair effect-grading with seeded breaks the harness doesn't know about — if the verdict survives planted failures, the pass rate means something; if not, it's correlated confidence. Effect grading tells you what happened; seeding tells you the grader was awake." | VERBATIM (паста 04.10) |
| 2 | Srinivasan Rangachary, тот же тред (2nd, 27 лет eCommerce, Oracle ATG, VastPRO) | Поддержал подход: грейдить эффект вместо чат-лога — правильно; Unable to verify никогда не засчитывать как проход. Новый слабый тай (контакта еще нет). Пост: https://www.linkedin.com/feed/update/urn:li:activity/7511780753484038144/. Оригинал: "Grading the effect instead of the chat log is the right approach. "Unable to verify" should never be counted as a pass." | VERBATIM (паста 04.10) |
| 3 | Vipul, ответ #1 | Забрал фразу "seeding tells you the grader was awake". Факты с их стороны: model-level версия уже построена — labelled set из frozen runs с известными ответами Pass / Fail / Unable to Verify; новая модель не станет их грейдером, если добавит хоть один critical false pass. Их hard problem: сидирование внутри клиентского прогона — Assurance читает код агента для генерации сценариев, поэтому поломка в коде от него не скрыта; сид должен жить вне читаемого (например, tool response, который не предсказать). Вопрос нам: "How do you keep your seeds blind to the harness?" Оригинал — по пасте 04.10, начало: "Victor Ematin, "seeding tells you the grader was awake" is a line I'm keeping." | VERBATIM (паста 04.10) |
| 4 | Victor, ответ #2 | Frozen-runs планка (хоть один critical false pass дисквалифицирует) — ровно то на model level. Наш ответ на run level: сидер и раннер — разные стороны без общего read scope. Сиды живут там, куда харнесс конструктивно не смотрит: непредсказуемые tool responses, документы вне его индекса, network stubs, data diffs — никогда в читаемом коде. Плюс rotation (без повторов) и pre-registration (вердикт фиксирован до прогона). Слепота — свойство оргчарта, не сида: examiner can't be the author, примененное к file scopes. Оригинал — по пасте 04.10, начало: "Vipul Verma, great question, and your frozen-runs bar (even one critical false pass disqualifies) is exactly right at model level." | VERBATIM (паста 04.10) |
| 5 | Vipul, ответ #2 | "Examiner can't be the author" — то же правило, что их пост применяет к агенту, но на уровень выше (к харнессу). Уточнение: blind должно значить "не может предсказать сид", а не "не видит эффект". Если эффект сида вне наблюдаемого — честный вердикт Unable to Verify, не Fail. Предложил скоринг сидов тремя путями: caught / honestly unverified / falsely passed; дисквалифицирует только третий. Оригинал — по пасте 04.10, ядро: "So I'd score seeds three ways: caught, honestly unverified, falsely passed. Only the third disqualifies." | VERBATIM (паста 04.10) |
| 6 | Victor, ответ #3 | Three-way чище нашего: caught / honestly unverified / falsely passed ложится на caught / observed-only / survived с одной поправкой — "observed but unflagged" сидит между вторым и третьим. Согласен: blind = непредсказуемый сид + полностью наблюдаемый эффект, иначе Unable to Verify — единственная честная клетка. "Only falsely-passed disqualifies — taken as a shared rule." Оригинал — по пасте 04.10, ядро: "Only falsely-passed disqualifies - taken as a shared rule." | VERBATIM (паста 04.10) |
| 7 | Vipul, ответ #3 (финал треда) | Согласен; "observed but unflagged" — то, за чем следить жестче всего: доказательства были в руках, ничего не сработало. У них распадается надвое: критерий покрывал, но прошел (это false pass) vs критерий вообще не спрашивал (это coverage gap) — разные фиксы, держать врозь. Финал: "Enjoyed this thread. Let's continue over DM." — тред закрыт, дальше личка (стыкуется с инвайтом на колл 1:28 AM). | VERBATIM (паста 04.10) |
| 8 | W1, оценка треда (eaaa78d) | Метрика теплоты треда: Vipul цитирует нашу рамку обратно — значит, зашло (landed). Линия: joint taxonomy peer lane, без коммерции. То есть цель треда — общий язык терминов, не продажа. | PARAPHRASE (чекпоинт) |
| 9 | Victor → Vipul, DM вечером перед 04.10 (10:20 PM) | Рад, что тред зашел ("glad the thread landed"). Развилка false-pass vs coverage-gap названа правильным разрезом ("the right cut"); у нас внутри та же развилка ("we run the same fork"). Предложение: готов показать, как seeded side выглядит на реальном гейте — scope маленький, только staging, без sales talk. Направление оставляет на его усмотрение ("your call on direction"). Оригинал: "Hi Vipul, glad the thread landed. The false-pass vs coverage-gap split is the right cut; we run the same fork on our side. Happy to continue here - if useful, I can show how the seeded side looks on a real gate (small scope, staging only, no sales talk). Your call on direction." | VERBATIM |
| 10 | Vipul → Victor, DM 04.10 1:28 AM | Понравился seeding thread под его постом про Agent Assurance. Факты с его стороны: у них seeded breaks уже крутятся на практике, и прямо сейчас они валидируют собственный грейдер. Приглашение: 20-минутный колл, сравнить заметки. Встречное предложение: показать, что Agent Assurance умеет сегодня, включая места, где он говорит Unable to Verify. Оригинал: "Hi Victor, I enjoyed the seeding thread on my Agent Assurance post. You're running seeded breaks in practice, and we're working on validating our own grader right now. Would you be open to a 20-minute call to compare notes? Happy to show you what Agent Assurance does today, including where it says Unable to Verify." | VERBATIM |
| 11 | Статус на сейчас | Паблик-тред закрыт (Vipul увел в DM, стыкуется с инвайтом 1:28 AM). Ответ Victor (драфт v1, hyphen-only) — у W1 на аппруве, еще не отправлен. Слоты и ссылка — ждем от Vipul после отправки. Колл не запланирован. | Факт трека |

## Приложение B. Глоссарий терминов (переписка + дебрифинг)

> (П) — термин из переписки с Vipul. (Ф) — термин нашего фреймворка/дебрифа.
> Без буквы «е» с точками и без тире — только дефис, как заведено.

| Термин | Откуда | Что значит по-русски |
|--------|--------|----------------------|
| Seeded breaks / seeding | (П) | Искусственно внесенные поломки (мутанты), на которых проверяется, ловит ли их контроль. У нас — плановые, пре-регистрированные; у них — "крутятся на практике" (детали еще не раскрыты). |
| False-pass | (П) | Ложный проход: контроль зеленый, хотя дефект есть. То, против чего работает весь метод. |
| Coverage gap | (П) | Дырка покрытия: место, где контроля нет вообще (не путать с false-pass, где контроль есть, но слеп). Развилка false-pass vs coverage-gap — "правильный разрез" треда. |
| Frozen-runs bar | (П) | Планка замороженных прогонов: baseline фиксируется, дальше меряются отклонения от него, а не абсолютные цифры. Принята обеими сторонами в треде. |
| Seed-blindness | (П) | Слепота сидера: тот, кто вносит поломки, не должен знать/видеть объект оценки. Меры: org separation (разные люди/контуры), out-of-read-scope (скоуп чтения закрыт), rotation (ротация операторов/наборов), pre-registration (фиксация набора до прогона). |
| Three-way | (П) | Три исхода вместо двух: поймано / замечено-без-флага / пропущено молча. Принято обеими сторонами. |
| Observed-unflagged | (П) | Замечено, но флаг не поднят: сигнал есть, вердикта нет. По shared rule уходит на adjudication. |
| Adjudication | (П) | Разбор арбитром (человеком): куда отправляется observed-unflagged вместо молчаливого зачета. |
| Shared rule | (П) | Общее правило разбора спорных исходов, одинаковое для обеих сторон. Предложено, детали не зафиксированы. |
| Agent Assurance | (П) | Продукт/питч Vipul: assurance-слой для агентов. Что умеет сегодня — покажет на колле. |
| Grader | (П) | Оценщик (авто-грейдер) внутри Agent Assurance. Сейчас проходит их внутреннюю валидацию — зачем им и нужен наш опыт сидирования. |
| Unable to Verify | (П) | Вердикт их системы: "проверить не могу" (воздержание вместо выдуманного прохода). Главный приз колла: какие кейсы туда попадают и что их оттуда выводит. |
| No sales talk | (П) | Оговорка Victor в DM: показываем метод, не продаем. Держать и на колле. |
| Staging-only scope | (П)+(Ф) | Scope показа: только staging, маленький периметр. Никакого прода. |
| Caught | (Ф) | Поймано: тест упал на seeded-мутанте. Единственный исход, идущий в счет mutation score. |
| Observed-only | (Ф) | Только замечено: мутированный элемент назван в наблюдениях, но тест зеленый. В счет не идет. Probable аналог их Unable to Verify — проверить на колле. |
| Survived | (Ф) | Выжил молча: ни падения, ни наблюдения. Единственное, что смотрит гейт. |
| Mutation score | (Ф) | Доля Caught от всех seeded (N). Считается per-tier, никогда не смешивается в один глобальный процент. |
| No-op rule / seeder defect | (Ф) | Правило ноу-оп: survivor, ничего не меняющий наблюдаемо (например, своп одинаковых лэйблов), — дефект сидера, отказ до сидирования (вне N), никогда не accept-risk постфактум. |
| B0 / B1 / B2 / B3 | (Ф) | Тиры риска: B0 Critical (деньги/доверие, 0 tolerated, target 100%, два подряд зеленых прогона), B1 High (ядро, 0 tolerated), B2 Medium (вторичное, band max 1 survived), B3 Low (только тренд, не гейтит). |
| Zero-tolerance | (Ф) | Нулевая терпимость B0/B1: ни один survivor не проходит гейт; каждый — Open finding, но решение "принять риск" гейт не открывает. |
| Open finding / Open decision | (Ф) | Открытая находка/решение: зафиксированный пропуск с записанным человеческим решением. Документирует, но на zero-tiers не открывает гейт. |
| Assessor | (Ф) | Независимый ассессор (технический аудитор): сидит поверх живых sensitivity-прогонов с реальными мутантами, сверяет Caught/Observed/Survived. |
| Evidence pack | (Ф) | Пакет доказательств прогона (HTML + execution PDFs). Формат, в котором показываем seeded side. |
| Joint taxonomy | (Ф) | Общая таксономия: согласованный язык исходов и разборов между нами и вендором. Линия треда по W1 (eaaa78d), без коммерции. |
| Peer lane | (Ф) | Peer-режим обмена: равные заметки, без продажи и без обещаний. Рамка колла. |
| Verdict-economics ledger | (Ф) | Лежер экономики вердиктов (трек W2): куда после колла уходят 3 строки (кейсы Unable-to-Verify, exit criteria, follow-up). |
| Angle B (break-the-judge) | (Ф) | Заготовка article-угла W4: "сломай судью" — если кейсы Vipul окажутся сочными. Только через W4, не трогать самому. |
| Frozen runs, model-level | (П) | Labelled set замороженных прогонов с известными ответами Pass / Fail / Unable to Verify. Новая модель грейдера дисквалифицируется хоть одним critical false pass. Планка Vipul, принята нами для model level. |
| Examiner can't be the author | (П) | Экзаменатор не может быть автором — поднятое на уровень харнесса: сидер и раннер разные стороны без общего read scope. Слепота как свойство оргчарта, не сида. Принято обеими сторонами. |
| Honestly unverified | (П) | Честно непроверенное: эффект сида вне наблюдаемого скоупа, вердикт Unable to Verify (не Fail). Средняя клетка three-way. Не дисквалифицирует. |
| Falsely passed | (П) | Ложно прошедшее: сид внутри наблюдаемого, вердикт зеленый. Единственное, что дисквалифицирует (shared rule, принято обеими сторонами). |
| Observed but unflagged | (П) | Замечено, но флаг не поднят: доказательства были в руках, ничего не сработало. Сидит между honestly unverified и falsely passed. Vipul делит надвое (см. Coverage-gap split). Следить жестче всего. |
| Coverage-gap split | (П) | Распил coverage gap от Vipul: covered-but-passed (критерий покрывал, но прошел — чинить критерий, это false pass) vs no-criterion-asked (критерий вообще не спрашивал — дописывать покрытие). Разные фиксы, держать врозь. |

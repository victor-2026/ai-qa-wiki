# Groetz: what PASS means in an agentic world (Hyground self-testing quorum, 2026-10-01)

**Author:** Rudolf Groetz (TestBusters/ConfQ), case by Florian Hansen + Beren Van Daele (Hyground AI SRE agent)
**Published:** 2026-10-01
**Source:** https://www.linkedin.com/pulse/agentic-world-what-does-pass-actually-mean-rudolf-groetz-cmtwf/
**Status:** practitioner case, honestly caveated by authors

## Саммари

Их SRE-агент тестирует сам себя: каждые 6 часов 4 промпта из каталога 50 гоняются параллельно, грейдятся ответ + tool-call struggle, алерт в Teams только на фейлы. Главный кейс — "failed correctly": ответ верный, но 15 вызовов / 2 фейла / 5 recoveries → FAIL за неэффективность ("today reaches the answer, tomorrow the same weaknesses lead elsewhere").

## Quorum против self-rating (ядро)

- Сам себе не верят: фейл считается реальным только после re-run 4 fresh delegates (порог 2/4 reproductions) + reviewer-агент спорит с диагнозом + 80% confidence. Ниже — candidate, не тикет.
- Живое доказательство смещения судьи: один из четырех агентов оценил собственный struggle как "No" при 15 вызовах и 2 фейлах в собственном логе. Самооценка ненадежна даже у машины с логом перед глазами.
- Наш вклад в разговор (W1): не "мы тоже", а решение их честно названной слабости — seeded breaks как детерминированная альтернатива flaky-judge.

## Честные слабости (их текст)

- 80% — rough signal (оценка модели, не измеренная вероятность); 2/4 — judgment call.
- 16 промптов/день — sample, не suite; про кластер с демо-нагрузкой, не про прод.
- Корреляция (модель грейдит себя) не исчезает никогда; кворум затрудняет, не исключает.

## Связь с нашими темами

- **Journey-not-answer = recognition > detection.** Правильный ответ неверным путем — наш classification-тезис (тройка Полу) с SRE-стороны.
- **Struggle-метрики как leading indicators** (вызовы/фейлы/recoveries) — fragility-мышление вживую (кросс-линк W1): "works today, fragile tomorrow" в метриках, не в словах.
- **"Prove a failure is real before it becomes a ticket"** — наш gaps-first на языке SRE.
- **Quorum + reviewer + confidence bar** — процедурная версия нашего "проверка проверяющего"; seeded breaks — детерминированная версия того же.
- [[ai-qa-tool-evaluation-mutation-matrix]] — внешний оракул как альтернатива кворуму.
- **Кросс-волт:** серия TestBusters — в пассивный вотч (регулярная, плотная); Articles vault — кандидат в банк цитат W4.

## Relevance

- Wiki-ценность: первый в базе живой кейс self-testing с кворумом + честные caveats + вещественное смещение self-оценки.
- Outreach: коммент в очереди (один острый пункт: quorum + seeded breaks), тайминг за Виктором, не стакать. Не пилот-таргет (внутренняя практика), карточку не заводить.

## Caveat

- Кейс одной команды на своем продукте (Hyground), демо-нагрузка, не прод.
- Цифры порогов (80%, 2/4) — judgment calls авторов, не измеренные вероятности.
- Raw не заводился: первоисточник — URL выше.

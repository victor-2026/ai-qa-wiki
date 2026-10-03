# Durability: AI grader needs a verified answer key (Floyd, 77 studies, 2026-09-28)

**Source:** https://harryfloyd.substack.com/p/your-ai-grader-answer-key (companion: durabilitycurve site version)
**Status:** evidence review + runnable Judge Check protocol

## Саммари

Без verified answer key грейдеры наименее надежны ровно там, где сами не могут ответить. >80% их ошибок — false passes (frontier без ключа). Ключ-фикс дешев где модель решает сама (ответить → проверить → использовать как ключ); где не решает никто — ключ от человека/доверенного источника, и это вопросы где он нужнее всего.

## Цифры, которые забираем

- MT-Bench self-answer as key: failures 70% → 15%.
- GPT-4o κ: 0.78 (решил) vs 0.30 (не решил); чужой неверный ключ 0.21 < без ключа 0.46 < unrelated 0.50; model-checked 0.61 ≈ human 0.69.
- Proof grading с рубрикой в руках: 38–45.7% false passes (5/7 грейдеров). Рубрика говорит ЧТО искать — меньше чем ответ.
- Code review наоборот: 26–36% false fails (до 88% с repair-просьбой) — считать обе стороны.
- Order swap: 11.4% флипов (GPT-5.4); markdown bias 73–97% vs 57% у людей.
- 2026 rerun: Opus 4.6 κ 0.875, GPT-5.4 0.606; разрыв solved/unsolved сохраняется.

## Judge Check (протокол, 20 айтемов)

1. 20 айтемов грейдера (≥10 known-wrong), сам грейдишь все.
2. Два прогона: без ключа, затем с verified answers (open-ended — written must-do list, слабее ключа).
3. Single-answer: грейдер отвечает отдельно; >1–2 неверных + pass им = без ключа нельзя.
4. Re-layout + swap order; считать флипы.
5. False passes/fails раздельно; формулы Sheets в статье. Screen на 20 (поймать щедрого), clearance — ~100 на failure mode (Husain).
6. Его ран: 24 вопроса, $2.83, 3/5 registered predictions failed (честно).

## Наши мосты

- **Answer key = pre-agreed verdict** с числами: без ключа судья гадает там где не решает (наш examiner/author + seeded checks судьям).
- **False-pass asymmetry (12/19 lean pass)** — эмпирика под наш gaps-first: щедрый судья красит систему.
- **Рубрика < ключ < verified ключ** — иерархия строгости для prompt regression suites (Олден-серия).
- **Layout/order flips** — seeded-класс для судей: перестановка как бесплатная проба.
- **Registered call (κ ≥0.2 к 30.09.2027, 35%)** — watch-календарь, проверить через год.

## Связь

- [[durability-curve-tests-pass-so-what-2026]] — та же серия, mutation-сторона; key-сторона здесь.
- [[ai-qa-tool-evaluation-mutation-matrix]] — seeded breaks судьям как следующий шаг после ключа.
- Candidate quotes W4: "A pass rate graded by a model partly measures how generous the grader is."

## Caveat

- Большинство исследований — препринты, часть до новых грейдеров; human labels на newest отсутствуют (автор честно).
- Raw не заводился: первоисточник — URL выше.

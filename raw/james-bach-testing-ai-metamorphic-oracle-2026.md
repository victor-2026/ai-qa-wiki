# James Bach — Testing AI beyond test cases (metamorphic testing, oracle problem)

**Источник:** YouTube talk, https://www.youtube.com/watch?v=5bU1Ao3aIdc. Транскрипт 885 сегментов, ~32K chars. Спикер: James Bach, 39 лет tester, RST (пара к вчерашнему Bolton WHeReAS).
**Тезис:** test cases as normally conceived fall short для AI by a long way. Альтернатива: investigation + test activities, не cases.

---

## 1. Почему AI — самое трудное для теста (после людей)

- **Unconstrained input/output space:** vast input, vast output, bizarre mapping. Nobody wrote the code — системы grown, not built (bamboo trees).
- **Evaluation bottleneck:** задачи без easy answers → нужен human skilled judgment → expensive bottleneck.

## 2. Metamorphic testing (термин из 1998, Bach раньше звал random testing / simplified data oracle testing)

- Идея: взять тест с oracle (средство распознать баг) → делать вариации, не ломающие oracle → сравнивать выходы между собой.
- eBay-пример: поиск fountain pen 5,000 hits → фильтр <$15 → хитов не больше, а меньше. Новый ответ highly related к первому — легко оценить.
- Кейс Hyundai chatbot: **10,776 вариаций** вопроса про warranty (LLM-generated, только грамматически чистые — без misspellings/abbreviations, т.е. покрытие неполное даже так).

## 3. Tool suite (собран agentic coding)

- **Phrase variator** (Python CLI): N вариаций x M rounds + semantic analysis → топ-10 most different (экономика: smallest subset с biggest value при лимите времени/токенов).
- **Phrase visualizer:** embeddings (4096 dims) → PCA → 3D, кластеры семантики для выбора test data.
- **Runner:** «technically these aren't tests, these are operations because I don't have an oracle yet» — точная формулировка нашей Evidence-темы.
- **Text similarity analyzer (non-AI):** longest common string across answers → мера вариативности.
- **Contradiction detector (AI):** pairwise анализ всех ответов друг против друга, кликабельная матрица.

## 4. Находки на Hyundai chatbot

- 23 формулировки про leather seats → почти каждый раз **разный список машин**, иногда отказ отвечать на ответимый вопрос. Вывод: говорим не про один баг, а про pattern unreliability (аналогия садовника: один кривой лист vs желтеющие листья).
- Warranty: battery 10yr/100k miles vs lifetime warranty в разных ответах. Вывод: LLM не должен paraphrase legal language (Ford решает ссылкой, не перефразом — legal problem waiting to happen).
- Эвристика быстрого просмотра: sort outputs by length — короткие = отказы, длинные = попытки с растущей детализацией.

## 5. LLM-as-judge caveats (важно для нас)

- Разные модели — разные вердикты на тех же данных: ChatGPT 4.1 строгий, Gemma 4 easygoing. Judge bias эмпирически.
- Thinking models (DeepSeek, GPT 5.6) для judge лучше, но slow + expensive → budget problem. Стратегия: cheapest model that succeeds, вверх только при нужде; тюнинг prompt/temperature обязателен.
- Позиция: AI как hunting dog — снижает cognitive burden сотен результатов, но pass/fail ему не отдавать. Mind engaged обязательно.

## 6. Agentic coding как революция тестера + финальная философия

- Инструменты за 5 минут вместо часов; contradiction detector — 20 минут от идеи до v1. Non-coders могут строить свой tooling.
- «I don't want a tool that says all tests passed. I don't believe it... tools that help me think better, not take thinking away». Аналогия с машиной: не автопилот, а beeping + auto-brake, на которые не полагаешься.

## Связки с нашей работой

- Metamorphic testing = методологическое grounding для наших metamorphic API-тестов (Buzzhive api/metamorphic) — теперь с именем, годом (1998) и процедурой.
- Judge variance (Gemma vs ChatGPT) — эмпирика под Kiro-вывод «same rubric every time» (сохранено сегодня же).
- «Operations, not tests, without oracle» + hunting dog — третья формулировка attestor-позиции за 2 дня (Jay green light, Radik ledger, Bach).
- Hyundai case (10,776 вариаций, wall of red) — quotable кейс с числами для статей.
- Пара Bolton (WHeReAS, вчера) + Bach (metamorphic, сегодня) = RST-линия целиком за 2 дня. Кандидаты на кросс-линк в Article 27 first comment? Нет — тело заморожено, коммент худой под продукт. Держать как launch-ammo VerdictGate.

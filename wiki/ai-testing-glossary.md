---
title: "AI Testing Glossary"
updated: 2026-04-20
tags: [glossary, AI, testing, definitions]
type: glossary
---

# AI Testing Glossary

**Last Updated:** 2026-09-04
**Sources:** Bas Dijkstra blog, arXiv papers, SWE-Tester research, BeyondQuality/SlopCodeBench, QBurst, Tony Seale, Andrew Ng Skills Map, Martin Fowler, TestMu AI, Zalando, Pi/OpenCode

---

## A

### AC (Acceptance Criteria)
**Definition:** Критерии приёмки — условия которым должна соответствовать система/фича чтобы быть принятой.
**Пример:** "Пользователь может войти с правильным паролем"
**Связан:** [[wiki/test-management]]

### Agentic AI / Agentic Development
**Definition:** Подход где AI автономно выполняет задачи с использованием инструментов, планированием и итерациями.
**Пример:** AI-агент который сам находит баг, пишет тест, запускает его
**Связан:** [[wiki/agentic-patterns]]

### Applicability (W)
**Definition:** Процент сгенерированных LLM патчей, которые правильно сформированы и могут быть применены к коду.
**Метрика:** 0-100%
**Связан:** [[wiki/swe-tester-framework]]

### Arid nodes
**Definition:** Бесплодные узлы - места в коде, где мутанты заведомо бесполезны (логи, импорты). Google подавляет такие узлы до сидирования.
**Связан:** [[wiki/rotation-without-relevance-preseed-mutant-filtering-2026]]

### Assertion scope
**Definition:** Область проверки - то, что тест реально проверяет: текст, id, видимость. По скоупу выбирается оператор из allowlist.
**Пример:** assert_text -> text, assert_value -> attribute
**Связан:** [[wiki/rotation-without-relevance-preseed-mutant-filtering-2026]]

### Assessor
**Definition:** Асессор / технический аудитор - независимый проверяющий, который сверяет счет и подписывает "evidence holds".
**Связан:** [[wiki/ai-qa-tool-evaluation-mutation-matrix]]

### Attribution
**Definition:** Атрибуция - правило "чей это результат": засчитывать только падения на засеянном шаге и позже, плюс наблюдения с именем мутированного элемента.
**Связан:** [[wiki/rotation-without-relevance-preseed-mutant-filtering-2026]]

### Adaptive Gold
**Definition:** Адаптивное золото - четвертый уровень medallion-архитектуры для агентов: агенты сами курируют данные (материализуют часто запрашиваемые комбинации), а не только потребляют.
**Связан:** [[wiki/martinfowler-making-data-ready-agentic-ai-2026]]

### Agentic lineage
**Definition:** Агентская прослеживаемость - расширение data lineage: фиксируется не только что агент сделал, но и почему (какой источник, какая логика, какие альтернативы отвергнуты). Требуется EU AI Act ст. 12.
**Связан:** [[wiki/martinfowler-making-data-ready-agentic-ai-2026]]

### Agentic regression testing
**Definition:** Агентское регрессионное тестирование - агент сам решает какие тесты запускать, в каком порядке и что чинить; человек владеет стандартом доказательства для пропущенного.
**Связан:** [[wiki/testmuai-agentic-regression-testing-2026]]

### Autonomy ladder
**Definition:** Лестница автономии - уровни делегирования агенту: Advisory (рекомендует) → Selective (выбирает на PR + nightly safety net) → Self-repairing (чинит локаторы с аппрувом) → Autonomous (переписывает ассерты - небезопасно).
**Связан:** [[wiki/testmuai-agentic-regression-testing-2026]]

### Accountable owner
**Definition:** Ответственный владелец - ровно один человек на AI-assisted изменение, который понимает его и готов к звонку в 2 часа ночи; инструмент и комитет владельцем быть не могут.
**Пример:** `Reviewer of record: @name` в PR
**Связан:** [[wiki/julia-pottinger-who-validates-ai-generated-code-2026]]

---

## B

### BM25 (Best Matching 25)
**Definition:** Probabilisticный алгоритм поиска и ранжирования документов. Используется для поиска дефектного кода.
**Применение:** Code Localization в SWE-Tester
**Связан:** [[wiki/swe-tester-framework]]

### Baseline green gate
**Definition:** Гейт зеленого бейзлайна - в N считаются только кейсы, зеленые без мутантов; id базового прогона пишется в evidence pack.
**Связан:** [[wiki/rotation-without-relevance-preseed-mutant-filtering-2026]]

### Boehm curve (AI-era reshape)
**Definition:** Кривая Бёма в AI-эре - стоимость дефекта: писать/переписывать стало дешево, а найти ЧТО переписать стало очень дорого (долг понимания); prevention (спека) стал критичнее appraisal.
**Связан:** [[wiki/beyondquality-ai-era-testing-2026]]

### Brownfield / Greenfield
**Definition:** Браунфилд (существующий проект с пользователями - тяжелая спека) vs гринфилд (прототип с нуля - легкая спека-промпт); у Ng определяет вес спеки и строгость гейтов.
**Связан:** [[wiki/andrew-ng-coding-agents-skills-map-2026]]

---

## C

### Change Coverage (ΔC)
**Definition:** Доля строк кода в идеальном патче, которые стали выполняться чаще после добавления сгенерированных тестов.
**Метрика:** Показывает реальное влияние тестов на покрытие изменений
**Связан:** [[wiki/swe-tester-framework]]

### Code Coverage
**Definition:** Процент строк кода, которые выполняются хотя бы одним тестом.
**Метрика:** Industry: 80%+ unit, 60%+ integration
**Примечание:** Не путать с Mutation Score

### Code Localization
**Definition:** Первый этап SWE-Tester — поиск дефектного кода и тестовых файлов.
**Методы:** BM25, embeddings, semantic search
**Связан:** [[wiki/swe-tester-framework]]

### Code Editing
**Definition:** Второй этап SWE-Tester — генерация тестов в формате Search/Replace.
**Связан:** [[wiki/swe-tester-framework]]

### CrewAI
**Definition:** Open-source фреймворк для оркестрации AI-агентов. Промышленный стандарт 2026.
**Связан:** [[wiki/mas-testing-framework]]

### Comprehension debt
**Definition:** Долг понимания - никто глубоко не понимает AI-написанный код (автор-агент не накапливает модель); диагностика дорожает, хотя переписать дешево; пара к intent debt.
**Связан:** [[wiki/beyondquality-ai-era-testing-2026]]

### CCN inflection
**Definition:** Перегиб цикломатической сложности - резкий рост CCN на графике по коммитам в момент появления coding agents в кодбазе (Zalando: 4 кодбазы); сигнал к рефактору/гейтам.
**Связан:** [[wiki/zalando-agentic-engineering-snapshot-2026]]

### Capability model
**Definition:** Модель возможностей - часть context layer: что агенту можно делать (курируемые чтения/записи живых систем с правами, владельцем, предусловиями, классом обратимости).
**Связан:** [[wiki/martinfowler-making-data-ready-agentic-ai-2026]]

### Confidence-threshold routing
**Definition:** Маршрутизация по порогу уверенности - сигналы качества данных + уверенность модели; ниже порога (напр. 85%, pricing 90%) агент передает человеку; нарушение контракта/SLA = всегда человеку.
**Связан:** [[wiki/martinfowler-making-data-ready-agentic-ai-2026]]

---

## D

### Dify
**Definition:** Open-source платформа для визуальной сборки агентов без кода.
**Связан:** [[wiki/mas-testing-framework]]

### DeepEval
**Definition:** Open-source фреймворк для оценки качества AI-тестов.
**Связан:** [[wiki/mas-testing-framework]]

### Definition of Done (DoD)
**Definition:** Список условий, подтверждающих что тест написан корректно.
**Примеры:**
- [ ] Тест проходит в CI/CD
- [ ] Тест не flaky
- [ ] Код соответствует гайдлайну

### Definition of Ready (DoR)
**Definition:** Список условий до начала работы ИИ.
**Примеры:**
- [ ] Описан контракт API
- [ ] Доступны моки
- [ ] Есть тестовые данные

### Decision log
**Definition:** Журнал решений - кто и когда решил fix или dismiss по каждому выжившему мутанту; без записи автопочинка считается провалом контроля.
**Связан:** [[wiki/rotation-without-relevance-preseed-mutant-filtering-2026]]

### Decision mutation
**Definition:** Мутация решений - смена логики: a > b -> a < b, && -> ||. Единственный тип, которого нет в нашем allowlist из 5 операторов.
**Связан:** [[wiki/rotation-without-relevance-preseed-mutant-filtering-2026]]

### Data contracts
**Definition:** Дата-контракты как код - схема как закон (Open Data Contract Standard): типы, quality-правила, freshness SLA; валидируются в CI/CD, блокируют деплой.
**Связан:** [[wiki/martinfowler-making-data-ready-agentic-ai-2026]]

### Decision validation
**Definition:** Валидация решений - слой поверх трейсов: правильный ли агент, тул, параметры и порядок для интента (ловит fluent-but-wrong, где ответ гладкий, а путь неверный).
**Связан:** [[wiki/qburst-quality-engineering-framework-validating-agent-behavior-2026]]

### Delegated access
**Definition:** Делегированный доступ - агент действует с правами вызвавшего пользователя (не через общий сервис-аккаунт), чтобы сохранить атрибуцию "кто чей доступ использовал".
**Связан:** [[wiki/martinfowler-making-data-ready-agentic-ai-2026]]

### Diffusion of responsibility
**Definition:** Диффузия ответственности - чем больше людей "могли бы проверить", тем меньше каждый чувствует обязанность; AI усиливает (автор думает агент прав, ревьюер думает автор проверил).
**Связан:** [[wiki/julia-pottinger-who-validates-ai-generated-code-2026]]

---

## E

### Equivalent mutant
**Definition:** Эквивалентный мутант - код другой, поведение то же; убить нельзя никаким тестом. Вычитается из знаменателя: score = Killed / (Total - Equivalent).
**Связан:** [[wiki/mutation-testing-vs-code-coverage-autonoma]]

### Evidence pack
**Definition:** Пакет доказательств - оператор, целевой шаг, детали, виды assertion и кандидаты по каждому мутанту плюс sign-off.
**Связан:** [[wiki/ai-qa-tool-evaluation-mutation-matrix]]

### Erosion (code erosion)
**Definition:** Эрозия кода - деградация структуры при итеративных изменениях агентом: многословие, мертвые ветки, избыточность; в SlopCodeBench растет в 5-7 раз быстрее, чем в human-репо.
**Связан:** [[wiki/slopcodebench-2026]]

### Eval-driven development
**Definition:** Разработка через эвалы - главный trait у Ng: дисциплинированный цикл "эвалы → анализ ошибок → разработка"; что измеряешь (детерминированные, LLM-as-judge, human-in-loop), то и улучшаешь.
**Связан:** [[wiki/andrew-ng-coding-agents-skills-map-2026]]

### Evidence discipline
**Definition:** Дисциплина доказательств (коммент Billian к Ng) - durable-запись: что changed, какие assumptions, какие checks, что failed, что unresolved; скорость безопасна только когда верификация накапливается.
**Связан:** [[wiki/andrew-ng-coding-agents-skills-map-2026]]

### Execution tracing
**Definition:** Трассировка выполнения - захват каждого хода агента как структурированного трейса (роутинг, tool calls, аргументы, выходы, чекпоинты) для replay и сравнения сборок.
**Связан:** [[wiki/qburst-quality-engineering-framework-validating-agent-behavior-2026]]

---

## F

### Fine-tuning
**Definition:** Дообучение предобученной LLM на своих данных.
**SWE-Tester:** 41K instances из 2600 GitHub repos
**Прирост:** до +10% success rate

### Flaky Test
**Definition:** Тест который периодически падает без изменений в коде.
**Связан:** [[wiki/testing-stability]]

### Floor suite
**Definition:** Неснимаемый минимум - auth/payment/data-integrity гоняются на каждый коммит независимо от диффа (blast radius не коррелирует с размером изменения).
**Связан:** [[wiki/testmuai-agentic-regression-testing-2026]]

### Free-first (OpenRouter)
**Definition:** Сначала free - правило субагентов: пробовать `openrouter/*:free` (20 RPM, 1000/день при ≥$10), при 429 fallback на платный вариант; concurrency 1-2.
**Связан:** [[wiki/pi-opencode-integration-2026]]

---

## G

### Generative ratification loop
**Definition:** Генеративный цикл ратификации (BeyondQuality) - сломанная петля "тестирование → имплементация": агент не обновляет ментальную модель, один класс багов повторяется бесконечно.
**Связан:** [[wiki/beyondquality-ai-era-testing-2026]]

### Greenfield
**Definition:** См. Brownfield / Greenfield.
**Связан:** [[wiki/andrew-ng-coding-agents-skills-map-2026]]

---

## H

### Harness (agent harness)
**Definition:** Харнесс агента - обертка вокруг LLM (поиск/ретривал, контекст, tool calls, сабагенты, permissions); Ng: понимать харнесс = меньше black box, видишь failure modes.
**Связан:** [[wiki/andrew-ng-coding-agents-skills-map-2026]]

---

## I

### Inference
**Definition:** Процесс генерации ответа LLM — это "runtime", не обучение.
**Ключевой инсайт:** Масштабирование inference-time compute улучшает результаты.

### Inference Scaffold
**Definition:** Конвейер обработки ошибок: sample → filter → rerank
**Зачем:** Один LLM вызов часто недостаточно

### Issue Reproduction Test
**Definition:** Тест который воспроизводит баг по текстовому описанию.
**Цель SWE-Tester:** Автоматизация таких тестов

### Information boundary
**Definition:** Информационная граница - мембрана агента (active inference): что приватно (credentials, client data), а что shared; полезное и приватное переплетены, пересечение решается ODRL-контрактом.
**Связан:** [[wiki/tony-seale-multi-agent-semantic-web-2026]]

### Intent debt
**Definition:** Долг намерений - никто не несет "почему" (бизнес-рациональ, дизайн-решения, принятые trade-offs); проявляется не когда ломается, а когда надо решать (BeyondQuality, пара к comprehension debt).
**Связан:** [[wiki/beyondquality-ai-era-testing-2026]]

### Impact analysis
**Definition:** Анализ влияния - карта "код → тесты, его покрывающие" (граф зависимостей); по TDAD снижает регрессии 6.08% → 1.82%; без нее агент удовлетворяет инструкцию дешево (непокрывающие тесты).
**Связан:** [[wiki/testmuai-agentic-regression-testing-2026]]

### Isolated solve
**Definition:** Изолированный скор (SlopCodeBench) - доля чекпоинтов, решенных по отдельности (лучший 28.1%); отличается от strict solve (сквозного) - разрыв показывает цену длинного горизонта.
**Связан:** [[wiki/slopcodebench-2026]]

---

## J

### Just-in-time credentials
**Definition:** Just-in-time креды - короткоживущий токен под конкретную задачу (напр. OFAC read на 5 минут); вместо вечных ключей; вместе с delegated access и least privilege ломает lethal trifecta.
**Связан:** [[wiki/martinfowler-making-data-ready-agentic-ai-2026]]

---

## L

### LCOV
**Definition:** Формат отчёта о покрытии кода. Генерируется gcov/lcov.
**Использование:** `npm run test --coverage`

### LoRA (Low-Rank Adaptation)
**Definition:** Метод PEFT — обновляется только небольшая часть параметров (rank 8, alpha 16), остальная модель заморожена.
**Преимущество:** Быстрое дообучение, меньше GPU
**Связан:** PEFT

### LLM (Large Language Model)
**Definition:** Большая языковая модель — нейросетевая модель для генерации текста и кода.
**Examples:** GPT-4, Claude 3.5, Qwen-2.5, Llama-3.1

### LLM-as-a-judge
**Definition:** LLM-судья - оценка качества ответа моделью по фикс-рубрике (accuracy, relevance, grounding, hallucination, usefulness); требует калибровки, нескольких оценщиков, борьбы с self-preference (судья любит свои генерации).
**Связан:** [[wiki/keith-klain-testing-mindset-after-all-2026]]

### Lethal trifecta
**Definition:** Смертельная тройка (Willison) - агент опасен когда сразу: доступ к приватным данным + exposure к недоверенному контенту + внешний канал связи; одна отравленная страница = prompt injection + эксфильтрация.
**Связан:** [[wiki/martinfowler-making-data-ready-agentic-ai-2026]]

### Long-horizon tasks
**Definition:** Длинногоризонтные задачи - автономные прогоны часами на миллионы токенов; у Ng: полезность vs стоимость преувеличена, выигрывает итеративность + skilled intervention.
**Связан:** [[wiki/andrew-ng-coding-agents-skills-map-2026]]

---

## M

### MARTI
**Definition:** Open-source фреймворк для MAS-тестирования (Feb 2026). Поддерживает Tree Search RL.
**Связан:** [[wiki/mas-testing-framework]]

### MAS (Multi-Agent System)
**Definition:** Архитектура с несколькими специализированными AI-агентами.
**Note:** Концептуальный паттерн из research papers

### MTTR (Mean Time to Repair)
**Definition:** Среднее время восстановления после сбоя.
**В контексте AI:** Скорость работы AI-агента по исправлению тестов

### Mutation Score
**Definition:** Метрика качества тестов — способность находить реальные баги.
**Как измеряется:** Mutation testing framework (Stryker)
**Почему важно:** Покрытие ≠ качество
**Цель:** 80%+

### Medallion architecture
**Definition:** Медальонная архитектура - Bronze (сырое, immutable) → Silver (валидировано, там quarantine) → Gold (сертифицировано, только его видят агенты) → Adaptive Gold (агенты курируют).
**Связан:** [[wiki/martinfowler-making-data-ready-agentic-ai-2026]]

### MaxSubagentSpawnsPerRun
**Definition:** Лимит порождений субагентов за прогон (pi-subagents, дефолт 64, у нас 3 для paid-интенсивности) - граница против разбегания оркестрации.
**Связан:** [[wiki/pi-subagents-2026]]

---

## Продолжение

N–Z: [[wiki/ai-testing-glossary-n-z]]

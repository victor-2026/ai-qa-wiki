# AI Testing Glossary

**Last Updated:** 2026-04-18
**Sources:** Sessions with Gemini, SWE-Tester, agentic-patterns, ai-testing-metrics

---

## A

### Agentic AI / Agentic Development
**Термин:** Agentic AI / Agentic Development
**Определение:** Подход где AI не просто отвечает на запросы, а автономно выполняет задачи с использованием инструментов, планированием и итерациями.
**Пример:** AI-агент который сам находит баг, пишет тест, запускает его и исправляет если падает.
**Связан:** [[wiki/agentic-patterns]]

### Applicability (W)
**Термин:** Applicability (W)
**Определение:** Процент сгенерированных LLM патчей, которые правильно сформированы и могут быть без ошибок применены к коду.
**Метрика:** 0-100%
**Связан:** [[wiki/swe-tester-framework]]

---

## B

### BM25 (Best Matching 25)
**Термин:** BM25
**Определение:** Probabilisticный алгоритм поиска и ранжирования документов. Используется для поиска дефектного кода по текстовому запросу.
**Применение:** Code Localization в SWE-Tester
**Связан:** [[wiki/swe-tester-framework]]

---

## C

### Change Coverage (ΔC)
**Термин:** Change Coverage (ΔC)
**Определение:** Доля строк кода в идеальном патче, которые после добавления сгенерированных тестов стали выполняться чаще, чем в оригинальном наборе тестов.
**Метрика:** Показывает реальное влияние тестов на покрытие изменений
**Связан:** [[wiki/swe-tester-framework]]

### Code Coverage
**Термин:** Code Coverage
**Определение:** Процент строк кода, которые выполняются хотя бы одним тестом. Обычно измеряется через LCOV.
**Метрика:** Industry стандарт: 80%+ для unit tests, 60%+ для integration
**Примечание:** Не путать с Mutation Score — coverage не гарантирует качество тестов

### Code Localization
**Термин:** Code Localization
**Определение:** Первый этап SWE-Tester — поиск дефектного кода и тестовых файлов в кодовой базе.
**Методы:** BM25, embeddings, semantic search
**Связан:** [[wiki/swe-tester-framework]]

### DeepEval
**Термин:** DeepEval
**Определение:** Open-source фреймворк для оценки качества AI-тестов. Метрики точности и качества генерации.
**Связан:** [[wiki/mas-testing-framework]]

### Dify
**Термин:** Dify
**Определение:** Open-source / Self-hosted платформа. Визуальная сборка агентов без кода.
**Связан:** [[wiki/mas-testing-framework]]

### CrewAI
**Термин:** CrewAI
**Определение:** Open-source фреймворк для оркестрации AI-агентов. Промышленный стандарт 2026 года.
**Пример:** `agents=[tester, critic], process='sequential'`
**Связан:** [[wiki/mas-testing-framework]]

### Code Editing
**Термин:** Code Editing
**Определение:** Второй этап SWE-Tester — генерация тестов в формате Search/Replace.
**Формат:** `<<<< << .head ... ===== ... >>>> .tail`
**Связан:** [[wiki/swe-tester-framework]]

---

## D

### Definition of Ready (DoR)
**Термин:** Definition of Ready (DoR)
**Определение:** Список условий, которым должна соответствовать задача прежде чем ИИ начнёт писать тесты.
**Примеры чеклиста:**
- [ ] Описан контракт API
- [ ] Доступны моки для внешних зависимостей
- [ ] Есть тестовые данные
**Связан:** [[wiki/swe-tester-framework]]

### Definition of Done (DoD)
**Термин:** Definition of Done (DoD)
**Определение:** Список условий, подтверждающих что тест написан корректно.
**Примеры чеклиста:**
- [ ] Тест проходит в CI/CD без ошибок
- [ ] Тест не flaky
- [ ] Код соответствует гайдлайну
**Связан:** [[wiki/swe-tester-framework]]

---

## F

### Fine-tuning
**Термин:** Fine-tuning
**Определение:** Дообучение предобученной LLM на своих данных для специализации под задачу.
**SWE-Tester data:** 41K instances из 2600 GitHub repos
**Прирост:** до +10% success rate

### Flaky Test
**Термин:** Flaky Test
**Определение:** Тест который периодически падает без изменений в коде. Главная проблема AI-тестов.
**Mitigation:** [[wiki/testing-stability]]
**Связан:** [[wiki/testing-stability]]

---

## I

### Inference
**Термин:** Inference
**Определение:** Процесс генерации ответа LLM на входной запрос. В отличие от training — это "_runtime" а не обучение.
**Ключевой инсайт:** Масштабирование inference-time compute улучшает результаты.

### Inference Scaffold
**Термин:** Inference Scaffold
**Определение:** Конвейер обработки ошибок: sample → filter → rerank
**Зачем:** Один LLM вызов часто недостаточно — нужно множественные попытки с фильтрацией
**Связан:** [[wiki/swe-tester-framework]]

### Issue Reproduction Test
**Термин:** Issue Reproduction Test
**Определение:** Тест который воспроизводит баг по его текстовому описанию (без исходного кода с багом).
**Цель SWE-Tester:** Автоматизация написания таких тестов.

---

## L

### LLM (Large Language Model)
**Термин:** LLM — Large Language Model
**Определение:** Большая языковая модель — нейросетевая база для генерации текста и кода.
**Examples:** GPT-4, Claude 3.5, Qwen-2.5, Llama-3.1

### MARTI
**Термин:** MARTI
**Определение:** Open-source фреймворк для MAS-тестирования (release Feb 2026). Поддерживает Tree Search RL — агенты пробуют разные варианты пока не пройдут валидацию.
**Связан:** [[wiki/mas-testing-framework]]

### LangGraph
**Термин:** LangGraph
**Определение:** Open-source фреймворк для сложных AI-workflows. Позволяет строить графы: если Критик бракует → возврат к Генератору.
**Связан:** [[wiki/mas-testing-framework]]

### LoRA (Low-Rank Adaptation)
**Термин:** LoRA — Low-Rank Adaptation
**Определение:** Метод PEFT — обновляется только небольшая часть параметров, основная модель остаётся замороженной.
**Преимущество:** Быстрое дообучение, меньше GPU

### LCOV
**Термин:** LCOV
**Определение:** Формат отчёта о покрытии кода. Генерируется gcov/lcov.
**Использование:** Code Coverage measurement
```bash
npm run test --coverage
# generates coverage/lcov.info
```

---

## M

### MAS (Multi-Agent System)
**Термин:** MAS — Multi-Agent System
**Определение:** Архитектура с несколькими специализированными AI-агентами.
**Примечание:** Это концептуальный паттерн, NOT подтверждённый в SWE-Tester статье! [[wiki/agentic-patterns]]

### MTTR (Mean Time to Repair)
**Термин:** MTTR — Mean Time to Repair
**Определение:** Среднее время восстановления — время необходимое для починки упавшего теста.
**В контексте AI:** Скорость работы AI-агента по исправлению тестов

### MAS-Pipeline
**Термин:** MAS-Pipeline
**Определение:** Multi-Agent System для тестирования — архитектура с несколькими агентами (Generator, Critic, Fixer, Executor).
**Contrast:** [[wiki/mas-vs-swe-comparison]]
**Связан:** [[wiki/mas-testing-framework]]

### Mutation Score
**Термин:** Mutation Score
**Определение:** Метрика качества тестов — способность тесто�� находить реальные баги (мутации) в коде.
**Как измеряется:** Mutation testing framework (Stryker)
**Почему важно:** Покрытие кода ≠ качество тестов. Mutation Score показывает реальную ценность тестов.
**Цель:** 80%+ — означает тесты находят 80% внесённых багов.
**Связан:** [[wiki/ai-testing-metrics]]

---

## P

### PEFT (Parameter-Efficient Fine-Tuning)
**Термин:** PEFT — Parameter-Efficient Fine-Tuning
**Определение:** Методы дообучения требующие обновления лишь небольшой части параметров.
**Examples:** LoRA, Adapters, Prompt Tuning
**Примечание:** SWE-Tester paper показывает что full fine-tuning лучше PEFT для этой задачи.

### PoC (Proof of Concept)
**Термин:** PoC — Proof of Concept
**Определение:** Проверка концепции — пилотный проект для валидации подхода перед полным внедрением.
**В контексте AI:** 4-фазный план: Инфраструктура → Проектирование → Пилот → Масштабирование
**Связан:** [[wiki/mas-testing-framework]]

### POC (Proof of Concept)
**Термин:** POC — Proof of Concept
**Определение:** Проверка концепции — этап перед полноценной разработкой.
**Статистика:** 54.5% организаций дошли до POC, но 44.1% отключили после запуска
**Связан:** [[wiki/state-of-digital-quality-2026]]

### Precision (Prec.)
**Термин:** Precision — Точность
**Определение:** Метрика поиска — доля релевантных результатов среди всех найденных.
**Formula:** TP / (TP + FP)
**В контексте:** Code Localization — нашли 10 файлов, 7 релевантны = 70% precision

### Quality Gap
**Термин:** Quality Gap
**Определение:** Разрыв между скоростью внедрения AI и скоростью его тестирования/контроля.
**Статистика:** AI внедряется 100%, тестируется ~54%
**Связан:** [[wiki/state-of-digital-quality-2026]]

### Prompt Engineering
**Термин:** Prompt Engineering
**Определение:** Искусство формулирования промптов для получения нужного результата от LLM.
**Ключевые техники:**
- Few-shot examples
- Chain-of-thought
- Role-playing

---

## Q

### Quality Data Plane
**Термин:** Quality Data Plane
**Определение:** (Концептуальный) Общий слой данных для агентов в MAS — Shared база состояний.
**Примечание:** Это концепция из моего черновика, НЕ из оригинальных статей!

---

## R

### Recall (Rec.)
**Термин:** Recall — Полнота
**Определение:** Метрика поиска — доля найденных релевантных результатов от всех существующих.
**Formula:** TP / (TP + FN)
**В контексте:** Есть 10 релевантных файлов, нашли 7 = 70% recall

### Quality Data Plane
**Термин:** Quality Data Plane
**Определение:** Общий слой состояний (Shared JSON state) между агентами. Позволяет восстановиться после падения скрипта.
**Example:** `/tmp/qa-state.json`
**Связан:** [[wiki/mas-testing-framework]]

### RAG (Retrieval-Augmented Generation)
**Термин:** RAG — Retrieval-Augmented Generation
**Определение:** Teхнология позволяющая LLM "подсматривать" во внешнюю документацию в реальном времени.
**Применение:** Graph-RAG для контекста микросервисов

### Red Teaming
**Термин:** Red Teaming
**Определение:** Оценка безопасности AI через симуляцию атак. Используется для поиска уязвимостей в LLM и генерации токсичного контента.
**Подход:** Domain experts (глубокие проверки) + General testers (широкие, хаотичные)
**Связан:** [[wiki/state-of-digital-quality-2026]]

### RLHF (Reinforcement Learning from Human Feedback)
**Термин:** RLHF — Reinforcement Learning from Human Feedback
**Определение:** Обучение с подкреплением на основе отзывов людей. Критически важно для полезности и безопасности AI.
**Почему важно:** Предотвращает генерацию предвзятого или токсичного контента
**Связан:** [[wiki/state-of-digital-quality-2026]]

### Retrieval
**Термин:** Retrieval
**Определение:** Поиск релевантного кода/документов. Первый этап в SWE-Tester.
**Methods:** BM25, semantic embeddings, hybrid

---

## S

### Search/Replace Format
**Термин:** Search/Replace Format
**Определение:** Формат патча для генерации тестов — явные границы через `<<<< << .head` / `>>>> .tail`
**Преимущество:**
- Безопаснее чем raw code generation
- Легче валидировать синтаксис
- Explicit boundaries
**Связан:** [[wiki/swe-tester-framework]]

### Self-Healing Tests
**Термин:** Self-Healing Tests
**Определение:** Тесты которые автоматически адаптируются к изменениям UI/API без участия человека.
**Как работает:**
- Semantic understanding элементов
- Dynamic locators
- AI-driven修复мость

### SFT (Supervised Fine-Tuning)
**Термин:** SFT — Supervised Fine-Tuning
**Определение:** Контролируемое дообучение с уч��телем — стандартный метод fine-tuning на размеченных данных.
**Пример SWE-Tester:** 41K instances с ground truth тестами

### Success Rate (S)
**Термин:** Success Rate (S)
**Определение:** Процент случаев в которых сгенерированный AI тест успешно воспроизводит описанный баг.
**Ключевая метрика SWE-Tester:** до +10% после fine-tuning

---

## T

### TCO (Total Cost of Ownership)
**Термин:** TCO — Total Cost of Ownership
**Определение:** Совокупная стоимость владения. В контексте AI: API токены + инфраструктура + поддержка.

### TDD (Test-Driven Development)
**Термин:** TDD — Test-Driven Development
**Определение:** Разработка через тестирование — тесты пишутся до кода.

---

## W

### Wiki Layer
**Термин:** Wiki Layer
**Определение:** Организованный слой знаний в AI QA Wiki (папка `wiki/`).
**Принцип:** raw/ файлы НЕ модифицируются AI, wiki/ организуется автоматически
**См.** [[wiki/AGENTS]]

---

## Глоссарианность (Как добавлять термины)

1. **Новый термин найден** → добавить в эту статью
2. **Формат:** `### Term (EN) / Термин (RU)` + определение + пример
3. **Связанные термины** → ссылка на `[[wiki/...]]`
4. **Источник** → откуда впервые появился

---

## Related Wiki Topics

- [[wiki/swe-tester-framework]] — основной источник терминов
- [[wiki/agentic-patterns]] — agentic термины
- [[wiki/ai-testing-metrics]] — метрики
- [[wiki/testing-stability]] — flaky, stability

## Sources

- Session with Gemini (arXiv papers analysis)
- SWE-Tester framework paper
- Agentic patterns wiki
- AI testing metrics wiki
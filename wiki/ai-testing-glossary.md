---
title: "AI Testing Glossary"
updated: 2026-04-20
tags: [glossary, AI, testing, definitions]
type: glossary
---

# AI Testing Glossary

**Last Updated:** 2026-04-20
**Sources:** Bas Dijkstra blog, arXiv papers, SWE-Tester research

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

---

## B

### BM25 (Best Matching 25)
**Definition:** Probabilisticный алгоритм поиска и ранжирования документов. Используется для поиска дефектного кода.
**Применение:** Code Localization в SWE-Tester
**Связан:** [[wiki/swe-tester-framework]]

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

---

## F

### Fine-tuning
**Definition:** Дообучение предобученной LLM на своих данных.
**SWE-Tester:** 41K instances из 2600 GitHub repos
**Прирост:** до +10% success rate

### Flaky Test
**Definition:** Тест который периодически падает без изменений в коде.
**Связан:** [[wiki/testing-stability]]

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

---

## P

### PEFT (Parameter-Efficient Fine-Tuning)
**Definition:** Методы дообучения требующие обновления лишь небольшой части параметров.
**Examples:** LoRA, Adapters, Prompt Tuning
**Примечание:** SWE-Tester показывает что full fine-tuning лучше PEFT

### PoC (Proof of Concept)
**Definition:** Проверка концепции перед полным внедрением.

### PRD (Product Requirements Document)
**Definition:** Документ требований к продукту — основной источник для тест-кейсов.

### Precision
**Definition:** Метрика поиска — доля релевантных результатов среди найденных.
**Formula:** TP / (TP + FP)
**Example:** Нашли 10 файлов, 7 релевантны = 70% precision

### Prompt Engineering
**Definition:** Искусство формулирования промптов для нуж��ого результата.
**Техники:** Few-shot, Chain-of-thought, Role-playing

---

## Q

### Quality Data Plane
**Definition:** Концептуальный общий слой данных для агентов в MAS — Shared база состояний.
**Note:** Это концепция, НЕ из оригинальных статей!

### Quality Gap
**Definition:** Разрыв между скоростью внедрения AI и скоростью его тестирования.
**Статистика:** AI внедряется 54.5%, тестируется полноценно меньше

---

## R

### Recall
**Definition:** Метрика поиска — доля найденных релевантных результатов.
**Formula:** TP / (TP + FN)
**Example:** Есть 10 релевантных файлов, нашли 7 = 70% recall

### RAG (Retrieval-Augmented Generation)
**Definition:** Технология позволяющая LLM "подсматривать" во внешнюю документацию.

### Red Teaming
**Definition:** Оценка безопасности AI через симуляцию атак.
**Подход:** Domain experts + General testers

### RLHF (Reinforcement Learning from Human Feedback)
**Definition:** Обучение с подкреплением на основе отзывов людей.

### Retrieval
**Definition:** Поиск релевантного кода/документов. Первый этап в SWE-Tester.

---

## S

### Search/Replace Format
**Definition:** Формат патча для генерации тестов через явные границы.
**Преимущество:** Безопаснее, легче валидировать синтаксис

### Self-Healing Tests
**Definition:** Тесты которые автоматически адаптируются к изменениям UI/API.
**Как работает:** Semantic understanding, Dynamic locators

### SFT (Supervised Fine-Tuning)
**Definition:** Стандартный метод fine-tuning на размеченных данных с учителем.
**Пример SWE-Tester:** 41K instances с ground truth

### Success Rate (S)
**Definition:** Процент случаев когда сгенерированный AI тест воспроизводит баг.
**Ключевая метрика:** до +10% после fine-tuning

---

## T

### TCO (Total Cost of Ownership)
**Definition:** Совокупная стоимость владения. AI: API токены + инфраструктура + поддержка.

### TDD (Test-Driven Development)
**Definition:** Разработка через тестирование — тесты пишутся до кода.

---

## Abbreviations

| Abbreviation | Full Form | Meaning |
|--------------|-----------|---------|
| FN | False Negative | Тест не нашёл баг (ложноотрицательный) |
| FP | False Positive | Тест упал без бага (ложноположительный) |
| TN | True Negative | Тест корректно не упал |
| TP | True Positive | Тест корректно нашёл баг |

---

## Related

- [[wiki/swe-tester-framework]]
- [[wiki/agentic-patterns]]
- [[wiki/ai-testing-metrics]]
- [[wiki/testing-stability]]
- [[wiki/test-automation-quadrant]]

## Sources

- [Bas Dijkstra Blog](https://www.ontestautomation.com/feed.xml)
- SWE-Tester arXiv papers
- Agentic patterns research




<!-- backlinks-start -->
### Backlinks
- [Regression Checklist Llm Ci 2026](wiki/regression-checklist-llm-ci-2026.md)
<!-- backlinks-end -->

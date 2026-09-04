---
title: "AI Testing Glossary (N-Z)"
updated: 2026-09-04
tags: [glossary, AI, testing, definitions]
type: glossary
---

# AI Testing Glossary (N–Z)

**Last Updated:** 2026-09-04
**Часть 1 (A–M):** [[wiki/ai-testing-glossary]]

---

## N

*(пока пусто — резерв под новые термины сессии)*

---

## O

### Ontology alignment
**Definition:** Выравнивание онтологий - переговоры о соответствии моделей мира агентов ("Contract" = "Agreement"?); без него один термин - разные смыслы, интеграция падает.
**Связан:** [[wiki/tony-seale-multi-agent-semantic-web-2026]]

### ODRL data contracts
**Definition:** Дата-контракты на ODRL - машиночитаемые правила "что может пересекать границу агента" (DPROD 1.2); масштабируют мембрану на сложность.
**Связан:** [[wiki/tony-seale-multi-agent-semantic-web-2026]]

### Oracle (subagent)
**Definition:** Оракул - субагент второго мнения: ставит под сомнение план/assumptions, не правит код (в отличие от reviewer).
**Связан:** [[wiki/pi-subagents-2026]]

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

## Q

### Quality Data Plane
**Definition:** Концептуальный общий слой данных для агентов в MAS — Shared база состояний.
**Note:** Это концепция, НЕ из оригинальных статей!

### Quality Gap
**Definition:** Разрыв между скоростью внедрения AI и скоростью его тестирования.
**Статистика:** AI внедряется 54.5%, тестируется полноценно меньше

### Quarantine pattern
**Definition:** Паттерн карантина - circuit breaker данных: не прошедшие контракт (схема/свежесть/quality) уходят в dead-letter queue на human review; агент их никогда не видит (лучше "нет данных", чем уверенно неверные).
**Связан:** [[wiki/martinfowler-making-data-ready-agentic-ai-2026]]

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

### Recall on skipped tests
**Definition:** Полнота на пропущенных - доля дефектов, которые full suite поймал бы, а subset поймал; бар Facebook: 95% тест-фейлов, 99.9% faulty changes; меряется nightly full vs subset.
**Связан:** [[wiki/testmuai-agentic-regression-testing-2026]]

### Review loop
**Definition:** Цикл ревью - `worker → reviewer → worker` до чистоты, bounded (max 3 раунда); упакован в `/parallel-review`, `/review-loop`.
**Связан:** [[wiki/pi-subagents-2026]]

### Reviewer of record
**Definition:** Ревьюер записи - именованный человек в PR, который понимает изменение и готов к звонку; если никто не готов подписаться - проблема ясности, не качества AI.
**Связан:** [[wiki/julia-pottinger-who-validates-ai-generated-code-2026]]

### Risk-based PR approval
**Definition:** Риск-гейт PR (Zalando) - каждый PR оценивается low/medium/high; 33% low auto-approve → lead time -20-40%; правила из анализа прод-инцидентов.
**Связан:** [[wiki/zalando-agentic-engineering-snapshot-2026]]

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

### Semantics as compression
**Definition:** Семантика как сжатие (Seale) - согласованная семантика сообщений сжимает межагентскую коммуникацию в theoretical-смысле; лечит болтливость агентов и расход токенов.
**Связан:** [[wiki/tony-seale-multi-agent-semantic-web-2026]]

### Shared identifiers
**Definition:** Общие идентификаторы - обе стороны резолвят один ID сущности (паттерн Web - URL); мало договориться что такое Contract, надо знать что это тот же контракт.
**Связан:** [[wiki/tony-seale-multi-agent-semantic-web-2026]]

### Staged autonomy
**Definition:** Стадийная автономия - Shadow (рекомендует, человек исполняет) → Supervised (готовит, ждет аппрува) → Autonomous with guardrails (в границах обратимости) → Full (спот-чеки); повышение по доказательствам.
**Связан:** [[wiki/martinfowler-making-data-ready-agentic-ai-2026]]

### Strict solve
**Definition:** Строгий скор (SlopCodeBench) - доля чекпоинтов со сквозным решением (лучший 14.8%); 0 агентов решили хоть одну проблему end-to-end.
**Связан:** [[wiki/slopcodebench-2026]]

### Standing context
**Definition:** Стоящий контекст - `AGENTS.md`/`CLAUDE.md`: кодбаза, архитектура, стиль, доступ к данным; поддерживается актуальным, ретроспективы накапливают learnings.
**Связан:** [[wiki/andrew-ng-coding-agents-skills-map-2026]]

### Subagent
**Definition:** Субагент - сфокусированная дочерняя Pi-сессия (scout/researcher/worker/reviewer/oracle/delegate); родитель ставит задачу и забирает результат (foreground/background + FleetView).
**Связан:** [[wiki/pi-subagents-2026]]

---

## T

### TCO (Total Cost of Ownership)
**Definition:** Совокупная стоимость владения. AI: API токены + инфраструктура + поддержка.

### TDD (Test-Driven Development)
**Definition:** Разработка через тестирование — тесты пишутся до кода.

### Trace-first pipeline
**Definition:** Трейс-сначала - выполнение тестов эмитит события → нормализация в единую схему → хронологический трейс; стандарт позволяет replay и build-to-build сравнение.
**Связан:** [[wiki/qburst-quality-engineering-framework-validating-agent-behavior-2026]]

### Tool-correctness evaluator
**Definition:** Эвалюатор корректности тула - кастомная проверка: тот ли backend tool, те ли параметры, тот ли порядок для воркфлоу (ловит fluent-but-wrong в лизинге).
**Связан:** [[wiki/qburst-quality-engineering-framework-validating-agent-behavior-2026]]

---

## V

### Verbosity (code verbosity)
**Definition:** Многословие кода - метрика эрозии в SlopCodeBench (наряду с dead branches); растет в 75% траекторий агентов.
**Связан:** [[wiki/slopcodebench-2026]]

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
- [Autonoma Шагивпайплайне](wiki/autonoma-шагивпайплайне.md)
- [Regression Checklist Llm Ci 2026](wiki/regression-checklist-llm-ci-2026.md)
<!-- backlinks-end -->

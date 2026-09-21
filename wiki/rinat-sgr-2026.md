---
source: "https://abdullin.com/schema-guided-reasoning/"
ingested: "2026-09-21"
title: "Schema-Guided Reasoning (SGR)"
type: article
updated: "2026-09-21"
tags: [llm-testing, structured-output, constrained-decoding, agent-testing]
---

## Schema-Guided Reasoning (SGR)

**Автор:** Rinat Abdullin (Vienna, BitGN). Каталог: [[rinat-abdullin-blog-catalog-all-publications-2026]]. Связанная техника: [[structured-output]] (constrained decoding).

---

### Что это

Техника, заставляющая LLM рассуждать по предопределённым шагам через **структуру**, а не только промпт:

- какие шаги модель должна пройти (запрет на пропуск)
- в каком порядке (логический поток)
- где явно сфокусировать внимание (глубина и точность)

Схема - это "чеклист" / "структурный скрипт", который **механикчеки принудительно enforce-ится** через Constrained Decoding (Structured Output). Не заменяет весь промпт - только управляет процессом рассуждения.

---

### Ключевые преимущества

| Преимущество | Что даёт |
|--------------|----------|
| Reproducible reasoning | стабильный инференс между прогонами |
| Auditable | каждый шаг рассуждения явный и проверяемый |
| Debuggable & Testable | промежуточные результаты линкуются на тест-датасеты (evals) |
| Expert knowledge → executable prompts | DDD хорошо ложится на схему |
| Accuracy boost | +5-10% - не редкость |

Для локальных/слабых моделей особенно важен: помогает работать вокруг низкой когнитивной ёмкости.

---

### Пример (compliance/FinTech)

Pydantic-структура, которая требует от LLM выполнить анализ пункта внутренней процедуры в строго заданном порядке. Mental checklist доменного эксперта → структурированная схема рассуждения.

---

### Паттерны SGR

- **Cascade** - цепочка обязательных шагов
- **Routing** - маршрутизация между ветками
- **Cycle** - повторы/итерации с проверкой завершения
- **Checklist patterns** - чеклисты как раздел паттернов

---

## Связь с тестированием LLM

SGR напрямую усиливает contract-подход из `llm-testing` skill:

1. **Структурированный вывод = контракт.** Pydantic/JSON Schema - готовые контракты для проверок (не LLM-as-judge, а детерминированная валидация).
2. **Промежуточные шаги тестируются** - тестируется не только финальный ответ, но и каждая стадия рассуждения (по сути наблюдаемые слои агента).
3. **Reproducibility** - стабильный инференс снижает undefined-поведение, упрощает golden dataset сравнения.
4. **Auditability** - фундамент для "evidence contract" (ср. Verdictgate mutation evidence).

Производственное применение (по автору): production (manufacturing, EU logistics, fintech compliance, sales), extract/normalize (PO, data sheets, invoices), regulation parsing + gap analysis.

---

## Поддержка в провайдерах (для воспроизводимости)

- OpenAI (вкл. Azure), GPT-5 (JSON Schema через llguidance)
- Mistral Custom Structured Output; Google/Gemini (JSON Schema с Nov 2025); Grok; Fireworks; Cerberas; OpenRouter (проксирует в JSON Schema)
- Инференс-движки: ollama, vllm (xgrammar/guidance), TensorRT-LLM (GuidedDecoding), SGLang (Outlines/XGrammar/llguidance)

---

## Связанные темы

- [[rinat-sgr-adaptive-planning-2026]] - "план-на-каждый-шаг" агент
- [[rinat-ai-coding-kata-2026]] - схема-контракт в kata
- [[rinat-llm-benchmarks-2026]] - SGR-powered benchmark v2
- [[autonoma-non-deterministic-outputs-2026]] - недетерминизм → контракты
- [[llm-testing]] skill - golden dataset, contracts

---

### Источник
- [Schema-Guided Reasoning (SGR)](https://abdullin.com/schema-guided-reasoning/) (2025, citation 2025-07)
- Citation: @misc{abdullin2025sgr, author = {Abdullin, Rinat}, title = {Schema-Guided Reasoning (SGR)}, url = {https://abdullin.com/schema-guided-reasoning/}}
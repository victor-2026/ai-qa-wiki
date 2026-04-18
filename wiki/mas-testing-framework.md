# MAS-Testing Framework (Conceptual)

**Last Updated:** 2026-04-18
**Status:** Theoretical / Conceptual (NOT confirmed in original papers)
**Sources:** Gemini analysis, [[wiki/agentic-patterns]] pipeline triad

---

> **Note:** This framework was initially derived from incorrectly interpreted paper analysis. The actual papers describe SWE-Tester (2-step pipeline). However, MAS is included here as a valuable **conceptual model** for multi-agent testing architectures.

---

## Overview

**MAS = Multi-Agent System** для тестирования — это переход от "AI как ассистент" к "AI как автономный отдел QA".

Conceptual model: вместо одной модели используется сеть специализированных агентов (тестировщик, разработчик, критик).

**Ожидаемый результат:** Снижение уровня "галлюцинаций" в коде тестов на ~35% по сравнению со стандартным подходом.

---

## Agent Roles (Conceptual Model)

| Role | English | Russian | Goal |
|------|---------|---------|------|
| **Generator** | The Generator | Генератор | Пишет тесты, "оптимист" |
| **Critic** | The Reviewer | Критик | Ищет баги и антипаттерны, "пессимист" |
| **Fixer** | The Fixer | Исправитель | Исправляет упавшие тесты |
| **Executor** | The Executor | Исполнитель | Запускает тесты в изолированной среде |

### Why 4 roles?

Одиночная модель (даже GPT-5) склонна к "замыливанию глаза" — верит в свой ошибочный код. Разделение ролей снижает галлюцинации.

Это соответствует [[wiki/agentic-patterns]] — Pipeline Triad паттерн: `Creator → Critic → Arbiter`.

---

## Communication Protocol (Conceptual)

Conceptual: агенты общаются через **Quality Data Plane** — общий слой данных (JSON/Protobuf):

```
Generator → [Quality Data Plane] → Critic
    ↑                                   │
    └────────── Fixer ←────────────────┘
                    ↑
              Executor (sandbox)
```

**Conceptual rationale:**
- Избегает "испорченного телефона"
- Каждое решение фиксируется в реестре состояний
- Каждый агент видит что сделали коллеги на предыдущем шаге

---

## DoR/DoD Validation Layer (Conceptual)

### Definition of Ready (DoR)

Conceptual: прежде чем Generator начнет работу, валидатор проверяет:
- [ ] Достаточно ли описан контракт API?
- [ ] Доступны ли моки для внешних зависимостей?
- [ ] Есть ли тестовые данные?

### Definition of Done (DoD)

Conceptual: после генерации проверяется:
- [ ] Тест проходит в CI/CD без ошибок?
- [ ] Тест не "хрупкий" (flaky)?
- [ ] Код соответствует корпоративному гайдлайну?

**Если DoD не пройден** — цикл запускается заново.

---

## Pre-commit AI-Refining (Conceptual)

```
1. Developer pushes code
2. MAS перехватывает push до основных тестов
3. Agents анализируют изменения
4. Agents сами дописывают/исправляют тесты
5. Human получает PR с уже актуализированными тестами
```

---

## QA Engineer Role Evolution (Conceptual)

| Before (2024) | Concept (2026+) |
|---------------|----------------|
| Пишет тесты | Архитектор агентов |
| Проверяет код тестов | Настраивает Prompt-инструкции |
| Меняет тесты вручную | Мониторит AI Trust Score |
| Регрессионное тестирование | Стратегия качества |

**Вывод (conceptual):** QA инженер становится "Architect of AI QA Factory" вместо "test writer".

---

## Comparison: SWE-Tester vs MAS

| Aspect | SWE-Tester (confirmed) | MAS-Testing (conceptual) |
|--------|---------------------|---------------------|
| Source | arxiv papers | Gemini analysis |
| Agents | 0 (2-step pipeline) | 4 roles |
| Approach | Retrieval + Edit | Multi-agent system |
| Fine-tuning | Required | Prompt-only |
| Isolation | Via scaffold | Via Quality Data Plane |

---

## Related Wiki Topics

- [[wiki/agentic-patterns]] — Pipeline Triad паттерн
- [[wiki/swe-tester-framework]] — Подтверждённый фреймворк
- [[wiki/ai-testing-glossary]] — Термины и определения
- [[wiki/testing-stability]] — Flakiness и стабильность
- [[wiki/ai-testing-metrics]] — Новые метрики для AI QA

## Sources

- Gemini conversation analysis (not verified)
- [[wiki/agentic-patterns]] Pipeline Triad
- [[wiki/swe-tester-framework]] (confirmed framework)
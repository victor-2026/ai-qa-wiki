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

## Implementation Options (April 2026)

К 2026 году на рынке уже есть инструменты для реализации MAS-подхода.

### 1. Open-Source Фреймворки

| Tool | Description | Best For |
|------|------------|---------|
| **MARTI v2** (Feb 2026) | Tree Search RL — агенты пробуют разные варианты пока не пройдут | Complex test generation |
| **CrewAI / LangGraph** | Промышленный стандарт оркестрации | Draw graph: Analysis → Test → Review → Fix |
| **Microsoft AutoGen** | Агенты "разговаривают" в чате | Chat-based workflows |

### 2. Enterprise Платформы

| Platform | Description | Best For |
|----------|------------|----------|
| **Testomat.io** | AI-Powered Orchestration — сканирует Jira, генерирует edge case тесты | Enterprise teams |
| **Dify / DIMA-AI** | Визуальные конструкторы "QA-агента из кубиков" | Low-code approach |

### 3. Пример на Python (CrewAI)

```python
from crewai import Agent, Task, Crew

# 1. Агент-Генератор
tester = Agent(
  role='Senior QA Automation',
  goal='Generate high-coverage unit tests for {service_name}',
  backstory='Expert in Pytest and Mocking, focuses on edge cases.',
  allow_delegation=False
)

# 2. Агент-Критик
critic = Agent(
  role='Security & Quality Auditor',
  goal='Review tests for logic errors and security leaks',
  backstory='Former hacker, expert in finding flaky tests.',
  allow_delegation=True
)

# 3. Сборка отдела тестирования
qa_crew = Crew(
  agents=[tester, critic],
  tasks=[test_task],
  process='sequential'  # Пишем → Проверяем
)

result = qa_crew.kickoff()
```

### Практические советы

1. **Начните с "Агента-Критика"** — оставить тесты людям, AI проверяет DoD
2. **Используйте Docker-песочницы** — изоляция для Executor
3. **Единый контекст** — Swagger/OpenAPI + Sentry logs = Quality Data Plane

---

## Sources

- Gemini conversation analysis (not verified)
- [[wiki/agentic-patterns]] Pipeline Triad
- [[wiki/swe-tester-framework]] (confirmed framework)
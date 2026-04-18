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

## Open-Source Tools (Free / MIT / Apache 2.0)

Апрель 2026 — сформировался чёткий стек бесплатных решений.

| Tool | Status | Best For |
|------|--------|---------|
| **MARTI-v2** | Open-Source | Tree Search RL — "пробуй и ошибайся" для генерации тестов |
| **LangGraph** | Open-Source | Сложная логика — если Критик бракует → возврат Генератору |
| **CrewAI** | Open-Source | Быстрый старт через Role-based agentes |
| **Dify** | Self-hosted | Визуальная сборка агентов без кода |
| **DeepEval** | Open-Source | Оценка качества AI-тестов (метрики) |

---

## Implementation Plan (4 Phases)

### Phase 1: Инфраструктура (1-2 недели)

- [ ] **Выбор оркестратора** — LangGraph (гибкость) или Dify (скорость)
- [ ] **Sandboxing** — Docker-контейнеры для изоляции (AI не должен видеть боевую БД)
- [ ] **RAG layer** — Подключение Swagger/OpenAPI + эталонные тесты

### Phase 2: Проектирование "Отдела" (1 неделя)

- [ ] **Агент-Генератор** промпт: "Ты — эксперт по Pytest. Покрой код логикой из задачи"
- [ ] **Агент-Критик** промпт: "Ты — злой QA лид. Ищи хардкод, отсутствие ассертов, логические дыры"
- [ ] **DoD:** "Тест принят если прошёл Docker, 0 линтер-ошибок, одобрен Критиком"

### Phase 3: Пилотный запуск (2-3 недели)

- [ ] Выбрать 1 стабильный сервис
- [ ] Генерация тестов для новых PR
- [ ] **Метрика:** Сколько багов найдено / сколько "мусора"

### Phase 4: Масштабирование

- [ ] Интеграция в CI/CD
- [ ] Обучение на специфических багах системы

---

## PoC Checklist

> **[ ] DoR Analysis** — Умеет ли AI понимать требования из Jira/Notion?
> **[ ] Fix Loop** — Настроена ли обратная связь (если тест упал → агент-Fixer получает лог)?
> **[ ] Quality Validation** — Подключён ли DeepEval для проверки галлюцинаций?

---

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
3. **Единый контекст** — Swagger + Sentry = Quality Data Plane

---

## Practical Implementation Details

### A) Agent Prompt: Детальный промпт для Критика

**System Prompt (Role Definition):**
> **Роль:** Senior QA Automation & Security Auditor (L6).
> **Инструкция:** Ты специализируешься на выявлении логических изъянов в автоматизированных тестах.
>
> **Чек-лист проверки (Critical Points):**
> 1. **Логическая корректность:** Проверяет ли ассерт именно то, что заявлено в названии теста?
> 2. **Антипаттерны:** Ищи `hardcoded` значения, `Thread.sleep()`, отсутствие cleanup.
> 3. **Мутационный анализ:** Будет ли тест "красным" если изменить логику функции?
> 4. **Flakiness:** Зависимости от порядка выполнения или внешних ресурсов без моков?
> 5. **DoD Compliance:** Соответствует корпоративному стандарту.
>
> **Формат ответа:** JSON: `{status: PASS/REJECT, score: 0-10, critical_issues: [], suggested_fixes: []}`

---

### B) Extended CrewAI Code

```python
from crewai import Agent, Task, Crew, Process

# 1. Агенты
generator = Agent(
    role='SDET Generator',
    goal='Написать надежные интеграционные тесты для API на основе {specs}',
    backstory='Ты лучший в написании сложных моков и асинхронных тестов на Python.',
    verbose=True,
    allow_delegation=False
)

critic = Agent(
    role='QA Critic',
    goal='Провести аудит кода тестов и отклонить те с галлюцинациями.',
    backstory='Твой опыт позволяет видеть скрытые баги.',
    verbose=True,
    allow_delegation=True  # Позволяет вернуть задачу на доработку
)

# 2. Цепочка задач
task_generate = Task(
    description='Создать тесты для {module_name}. Использовать Pytest.',
    expected_output='Файл с тестами .py',
    agent=generator
)

task_review = Task(
    description='Проверить тесты на DoD и отсутствие галлюцинаций.',
    expected_output='Отчет об аудите.',
    agent=critic,
    context=[task_generate]  # Критик видит результат генератора
)

# 3. Сборка команды
qa_crew = Crew(
    agents=[generator, critic],
    tasks=[task_generate, task_review],
    process=Process.sequential,
    full_output=True
)

# Запуск
results = qa_crew.kickoff(inputs={'module_name': 'AuthService', 'specs': 'OpenAPI v3'})
```

---

### C) DoR/DoD Automation

#### Автоматизация DoR (Критерии готовности)

**LLM-Classifier** на этапе создания задачи:
1. Агент "Анализатор" сканирует описание задачи (Jira/Notion)
2. Проверка полноты: если нет API endpoints → комментарий *"DoR не пройден"*
3. Задача возвращается на доработку

#### Автоматизация DoD (Критерии приемки)

**Hybrid Validation** (AI + Инструменты):
1. **Static Analysis** — ruff/ESLint (синтаксис)
2. **AI-Review** — Критик проверяет смысл
3. **Execution Gate** — Docker container, Exit Code 0
4. **Coverage Check** — порог (напр. 80%), PR блокируется если ниже

---

### D) Docker Sandboxing

Критично: AI не должен иметь доступ к боевой БД.

#### Dockerfile для AI-тестов

```dockerfile
FROM python:3.11-slim

WORKDIR /app

# Установка зависимостей
RUN pip install --no-cache-dir \
    pytest \
    pytest-asyncio \
    ruff \
    requests-mock

# Копирование тестов (только чтение)
COPY tests/ ./tests/

# Запуск через ruff + pytest
CMD ["sh", "-c", "ruff check ./tests/ && pytest ./tests/"]
```

#### docker-compose для изоляции

```yaml
services:
  ai-tester:
    build: ./ai-tester
    volumes:
      - ./tests:/app/tests:ro  # только чтение
    environment:
      - API_URL=http://mock-server:8000
      - DB_CONNECTION=none  # явно отключено

  mock-server:
    image: wiremock/wiremock
    ports:
      - "8000:8080"
```

#### Workflow

```
Developer PR → GitHub Actions
    ↓
Build Docker (ai-tester)
    ↓
Run: ruff check → pytest → Coverage Check
    ↓
Artifacts: test-results.json
    ↓
If ALL passed → Merge
```

---

## С чего начать?

> **Лучше начать с автоматизации DoD.** Даже если тесты пишут люди, ИИ-Критик в CI/CD будет отсеивать "мусорные" проверки.

---

## Sources

- Gemini conversation analysis (not verified)
- [[wiki/agentic-patterns]] Pipeline Triad
- [[wiki/swe-tester-framework]] (confirmed framework)
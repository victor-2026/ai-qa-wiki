# MAS-Testing Framework

**Last Updated:** 2026-04-18
**Sources:** arxiv 2603.24160v1, arxiv 2603.23448v1

---

## Overview

**Multi-Agent System (MAS)** для тестирования — это переход от "AI как ассистент" к "AI как автономный отдел QA".

**Ключевой вывод статей:**
> К середине 2026 года ручное написание модульных и простых интеграционных тестов становится нерентабельным. MAS-подход покрывает до 90% типовых изменений без участия QA-инженера.

---

## Agent Roles

| Role | English | Russian | Goal |
|------|---------|---------|------|
| **Generator** | The Generator | Генератор | Пишет тесты, "оптимист" |
| **Critic** | The Reviewer | Критик | Ищет баги и антипаттерны, "пессимист" |
| **Fixer** | The Fixer | Исправитель | Исправляет упавшие тесты |
| **Executor** | The Executor | Исполнитель | Запускает тесты в изолированной среде |

### Why 4 roles?

Одиночная модель (даже GPT-5) склонна к "замыливанию глаза" — верит в свой ошибочный код. Разделение ролей снижает галлюцинации на **35%**.

---

## Communication Protocol

Агенты общаются через **Quality Data Plane** — общий слой данных (JSON/Protobuf):

```
Generator → [Quality Data Plane] → Critic
    ↑                                   │
    └────────── Fixer ←────────────────┘
                    ↑
              Executor (sandbox)
```

**Почему это работает:**
- Избегает "испорченного телефона"
- Каждое решение фиксируется в реестре состояний
- Каждый агент видит что сделали коллеги на предыдущем шаге

---

## DoR/DoD Validation Layer

### Definition of Ready (DoR)

Прежде чем Generator начнет работу, валидатор проверяет:
- [ ] Достаточно ли описан контракт API?
- [ ] Доступны ли моки для внешних зависимостей?
- [ ] Есть ли тестовые данные?

### Definition of Done (DoD)

После генерации проверяется:
- [ ] Тест проходит в CI/CD без ошибок?
- [ ] Тест не "хрупкий" (flaky)?
- [ ] Код соответствует корпоративному гайдлайну?

**Если DoD не пройден** — цикл запускается заново.

---

## Results from 500 Microservices Experiment

| Metric | Traditional (Human) | MAS (Agents) | Improvement |
|--------|---------------------|--------------|--------------|
| Code Coverage (LCOV) | 65% | 92% | +27% |
| Mutation Score | 48% | 76% | +28% |
| Test Creation Time | 25-40 min | 2-3 min | ~15x faster |
| Flakiness | 12% | 4% | 3x more reliable |

**Mutation Score** — главная метрика. Показывает способность теста найти реальную ошибку в коде.

---

## Graph-RAG Context Management

Проблема: нельзя "скормить" ИИ весь репозиторий.

**Решение:** Graph-RAG
1. Строим граф зависимостей микросервисов
2. При изменении сервиса "Оплата" — агент автоматически получает контекст из "Корзина" и "Пользователь"
3. Исключает несовместимость типов в соседних сервисах

---

## Pre-commit AI-Refining

```
1. Developer pushes code
2. MAS перехватывает push до основных тестов
3. Agents анализируют изменения
4. Agents сами дописывают/исправляют тесты
5. Human получает PR с уже актуализированными тестами
```

---

## Integration with CI/CD

### GitHub Actions Example

```yaml
ai-qa-refine:
  runs-on: ubuntu-latest
  steps:
    - uses: actions/checkout@v4
    - name: MAS Quality Gate
      run: |
        # 1. Generator creates tests
        # 2. Critic reviews
        # 3. Fixer fixes if needed
        # 4. Executor validates
```

---

## New Metrics (2026)

| Old Metric (deprecated) | New Metric |
|-------------------------|-------------|
| "Количество тестов" | **AI Trust Score** — % тестов от ИИ, не требующих human intervention |
| "Покрытие кода" | **Mutation Score** — реальная способность находить баги |
| "Время написания" | **MTTR** — Mean Time to Repair для упавших тестов |

---

## Risks and Mitigations

### 1. Collective Hallucination

**Проблема:** Все агенты соглашаются с неверным решением.

**Mitigation:**
- Агент-Arbiter с правом вето
- Periodic human review gates

### 2. Context Drift

**Проблема:** Качество кода от ИИ со временем деградирует.

**Mitigation:**
- Мониторинг Mutation Score в динамике
- Retraining на основе реальных багов

### 3. Zero-Code QA Risk

**Проблема:** "Тесты пишутся на основе анализа поведения пользователей" — без понимания бизнес-логики.

**Mitigation:**
- Человек как "дизайнер стратегии качества"
- Business rules в DoD

---

## QA Engineer Role Evolution

| Before (2024) | After (2026) |
|---------------|--------------|
| Пишет тесты | Архитектор агентов |
| Проверяет код тестов | Настраивает Prompt-инструкции |
| Меняет тесты вручную | Мониторит AI Trust Score |
| Регрессионное тестирование | Стратегия качества |

**Вывод:** QA инженер становится "Architect of AI QA Factory" вместо "test writer".

---

## Related

- [[wiki/agentic-patterns]] — Pipeline Triad паттерн
- [[wiki/ai-testing-metrics]] — Новые метрики для AI QA
- [[wiki/testing-stability]] — Flakiness и стабильность

## Sources

- arxiv:2603.24160v1 — Multi-agent Architecture for Autonomous Testing
- arxiv:2603.23448v1 — Benchmarking LLM Agents for QA
# MAS-Testing Framework 

**Last Updated:** 2026-04-18
**Status:** Theoretical / Conceptual 
**Sources:** Gemini analysis, arXiv papers

---

## Overview

**MAS = Multi-Agent System** для тестирования — это переход от "AI как ассистент" к "AI как автономный отдел QA".

Conceptual model: вместо одной модели используется сеть специализированных агентов (тестировщик, разработчик, критик).

**Ожидаемый результат:** Снижение уровня "галлюцинаций" в коде тестов на ~35% по сравнению со стандартным подходом.

---

## Agent Roles 

| Role | English | Russian | Goal |
|------|---------|---------|------|
| **Generator** | The Generator | Генератор | Пишет тесты, "оптимист" |
| **Critic** | The Reviewer | Критик | Ищет баги и антипаттерны, "пессимист" |
| **Fixer** | The Fixer | Исправитель | Исправляет упавшие тесты |
| **Executor** | The Executor | Исполнитель | Запускает тесты в изолированной среде |

### Why 4 roles?

Одиночная модель (даже GPT-5) склонна к "замыливанию глаза" — верит в свой ошибочный код. Разделение ролей снижает галлюцинации.

Это соответствует agentic-patterns — Pipeline Triad паттерн: `Creator → Critic → Arbiter`.

---

## Communication Protocol 

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

## Pre-commit AI-Refining 

```
1. Developer pushes code
2. MAS перехватывает push до основных тестов
3. Agents анализируют изменения
4. Agents сами дописывают/исправляют тесты
5. Human получает PR с уже актуализированными тестами
```

---

## QA Engineer Role Evolution

| Before (2024) | Concept (2026+) |
|---------------|----------------|
| Пишет тесты | Архитектор агентов |
| Проверяет код тестов | Настраивает Prompt-инструкции |
| Меняет тесты вручную | Мониторит AI Trust Score |
| Регрессионное тестирование | Стратегия качества |

**Вывод:** QA инженер становится "Architect of AI QA Factory" вместо "test writer".

---

## Research Sources 

- [arXiv:2601.02454](https://arxiv.org/abs/2601.02454) — "The Rise of Agentic Testing" (Jan 2026)
- [IEEE 11348399](https://ieeexplore.ieee.org/document/11348399/) — "Multi-Agent Systems in Software Testing" (2025-2026)
- [arXiv:2512.21352](https://arxiv.org/abs/2512.21352) — "Multi-Agent LLM Committees" (Dec 2025)

**Note:** These papers describe multi-agent systems, but none has exactly our MAS-Pipeline (4 roles) implementation. The 85% mutation score is our **estimated** target based on committee performance claims in papers.

---

## Risks (See [[mas-risks]])

| Risk | Description |
|------|-------------|
| Groupthink | All agents same model → same blind spots |
| Fixer Loop | Infinite fix cycle |
| Test Suite Erosion | Coverage grows, quality drops |
| RAG Poisoning | Bad patterns stored as good |
| Objective Drift | Optimizing for "pass", not quality |

---

## Real-World Examples

Based on research papers, there are actual multi-agent implementations:

| Example | Description | Source |
|---------|-------------|--------|
| **PersonaTester** | Multi-agent system for persona-based testing | arXiv |
| **c-CRAB** | Multi-agent code review, outperforms single agents | arXiv |
| **Devin** | AI developer agent (Autonomous) | Cognition Labs |
| **Claude Code** | Agentic coding assistant | Anthropic |
| **PR-agent** | AI-powered PR review | pr-agent.ai |

### Key Findings from Research

| Approach | Result |
|----------|--------|
| Multi-agent systems | 40% task solve rate improvement |
| Self-Consistency + CoVe + Dual Execution | +39% validity, +28% coverage, +18% mutation |
| LLM test amplification | Coverage increase in industry (logistics company) |

Source: [arxiv-ai-testing-effectiveness-2026.md](wiki/arxiv-ai-testing-effectiveness-2026.md)

---

## Open Questions

1. **How to implement Quality Data Plane?** — Shared database? Message queue?
2. **What happens if one agent fails?** — Error handling strategy?
3. **How to prevent infinite Fixer Loop?** — Max iterations limit?
4. **Can we use different models per role?** — To reduce Groupthink?

---

*This article is conceptual. Real implementations may differ.*
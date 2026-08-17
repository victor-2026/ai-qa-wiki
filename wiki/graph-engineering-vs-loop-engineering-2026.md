# Graph Engineering vs Loop Engineering — The 2026 Agent Roadmap

## Контекст

Июль 2026. Peter Steinberger (OpenClaw) задаёт вопрос: "Мы всё ещё говорим о циклах, или уже перешли к графам?" — и термин Graph Engineering кристаллизуется в сообществе.

**Loop Engineering** — дизайн цикла одного агента: discover → plan → execute → verify → repeat.
**Graph Engineering** — соединение нескольких специализированных агентов в граф.

Источник: [AI Builder Club — Graph Engineering vs Loop Engineering](https://www.aibuilderclub.com/blog/graph-engineering-vs-loop-engineering)

---

## Сравнение

| Характеристика | Loop Engineering | Graph Engineering |
|---|---|---|
| **Единица** | Цикл одного агента | Множество узлов + связи |
| **Состояние** | В контексте одного агента | Передаётся между узлами по рёбрам |
| **Структура** | Последовательный повтор | Параллелизм, ветвление, fan-out/fan-in |
| **Сложность** | Один промпт | Схема данных + множество промптов |
| **Когда падает** | Слабый верификатор | Ошибки топологии, утечка state |

**Главное правило:** Каждый узел в графе — это цикл. Граф не заменяет циклы, он их объединяет.

---

## 3 новые возможности графового подхода

### 1. Параллельные специализированные узлы

Разделение ролей: "исследователь", "писатель", "редактор" — каждый со своим чистым контекстом. Пример:

```text
        ┌──────────────┐   notes    ┌───────────┐  draft   ┌────────────┐
  in ──►│  researcher   │───────────►│  writer   │─────────►│  reviewer  │──► brief
        │ (fan-out over │            │ (clean    │          │ (fresh ctx,│
        │  N sources)   │            │  notes    │   ◄──────│  brief +   │
        └──────────────┘            │  only)    │  reject  │  the bar)  │
                                     └───────────┘  route   └────────────┘
```

Результат: ревьюер видит только brief + критерии, а не "болото" из HTML, черновиков и своих же рассуждений.

### 2. Явный auditable control flow

Логика "если ревью не пройдено → вернуться назад" видна на диаграмме, а не закопана в истории чата. Узлы и переходы определены upfront, inspectable.

### 3. Fan-out / Fan-in

Split → N параллельных веток → merge. Например, запустить 10 поисковых агентов одновременно, дождаться всех, объединить в один отчёт. Loop так не умеет.

---

## Это реально или ребрендинг?

**И то, и другое.**

Действительно новое: параллельные специализированные узлы, fan-out/fan-in, явный control flow.

Ребрендинг: LangGraph, Microsoft AutoGen (GraphFlow), Google ADK — все использовали графовую оркестрацию за годы до появления термина.

> "State-machine expert сказал бы, что это вторник." — David K. Piano (создатель XState)

---

## Gut Check: ты действительно перешёл на графы?

1. **Контексты разделены?** Разные промпты и инструменты на узел, а не один агент меняет шляпы.
2. **Есть fan-out/fan-in?** Что-то работает параллельно и объединяется, а не просто нарисовано в виде боксов.
3. **Control flow читается как диаграмма?** Маршрутизация определена upfront, inspectable, а не emergent из одного решения.
4. **Objective и success bar изменились?** Если "done and correct" то же самое — дисциплина не сдвинулась.

**0-1 да:** цикл в графовой одежде.  **2-3:** реально композитируешь.  **4:** парадигма сменилась.

---

## Связь с другими статьями

- [Karpathy: Autoresearch](wiki/karpathy-autoresearch-agentic-engineering-2026.md) — autoresearch = идеальный пример Loop Engineering (один агент, 5-min цикл, val_bpb как verifier). Bilevel Autoresearch = простейший граф (2 узла).
- [It Was Always a Loop](wiki/it-was-always-a-loop.md) — контраргумент к хайпу: loops не изобрели в 2026, это тот же паттерн что и термостат.

## Связь с QA-тестированием

| Loop Engineering | Graph Engineering |
|---|---|
| Aider `--test-cmd` (один агент, автофикс) | Autonoma pipeline (pageFinder → kb → entityAudit → scenarioRecipe → testGenerator) |
| Ralph Wiggum (bash loop: `while :; do cat PROMPT.md \| claude-code ; done`) | Gas Town (20-30 агентов с ролями Mayor/Polecat/Witness) |
| Один Playwright тест с retry | MAS patterns (known_patterns.json — 10 паттернов оркестрации) |
| Локальный self-healing при генерации | Production CI/CD self-healing (Claude Code, Playwright Test Agents) |

Проект qa-automation-sandbox использует оба подхода:
- **Loop:** PBT (property-based testing), retry на flaky, `--test-cmd` auto-fix
- **Graph:** modular API clients, setup/teardown pipelines, multi-stage CI/CD workflows

---

## Ресурсы

- [AI Builder Club — полная статья](https://www.aibuilderclub.com/blog/graph-engineering-vs-loop-engineering)
- [Loop Engineering Guide (AI Builder Club)](https://www.aibuilderclub.com/blog/loop-engineering-guide-2026)
- [Graph Engineering Guide (AI Builder Club)](https://www.aibuilderclub.com/blog/graph-engineering-guide-2026)
- [Agent Graph vs Loop: When to Use Which](https://www.aibuilderclub.com/blog/agent-graph-vs-loop-when-to-use)
- [Five Layers of AI Engineering](https://www.aibuilderclub.com/blog/five-layers-ai-engineering)
- [LangGraph Overview](https://docs.langchain.com/oss/python/langgraph/overview)
- [Google ADK](https://adk.dev/)





<!-- backlinks-start -->
### Backlinks
- [It Was Always a Loop](wiki/it-was-always-a-loop.md)
- [Karpathy: Autoresearch, Agentic Engineering и Self-Improvement Loops](wiki/karpathy-autoresearch-agentic-engineering-2026.md)
<!-- backlinks-end -->

# Karpathy: Autoresearch, Agentic Engineering и Self-Improvement Loops

## Контекст

Март 2026. Andrej Karpathy открывает код `autoresearch` — система, где один GPU работает как автономная исследовательская лаборатория. Человек пишет `program.md`, AI-агент за ночь проводит ~100 ML-экспериментов без вмешательства.

Это продолжение эволюции: Vibe Coding (2025) → Agentic Engineering (фев 2026) → Autoresearch (март 2026).

Источник: [Garry Tan — Karpathy Just Turned One GPU Into a Research Lab](https://garryslist.org/posts/karpathy-just-turned-one-gpu-into-a-research-lab-f55754a6)

---

## Autoresearch: как это работает

**Три файла:**

| Файл | Роль | Кто меняет |
|------|------|-----------|
| `prepare.py` | Подготовка данных (однократно) | Никто (фиксирован) |
| `train.py` | GPT модель + оптимизатор (Muon + AdamW), ~630 строк | **AI-агент** |
| `program.md` | Стратегия исследования | **Человек** (частично AI) |

**Цикл:**
1. Агент читает `program.md` — стратегию от человека
2. Редактирует `train.py` — архитектура, оптимизатор, гиперпараметры
3. Запускает тренировку на **ровно 5 минут**
4. Измеряет `val_bpb` (validation bits per byte) — метрика, независимая от размера словаря
5. Если результат улучшился — коммит в git feature branch; если нет — откат
6. Повтор ~12 раз/час = ~100 за ночь

**Результат:** 83 эксперимента, 15 улучшений за ночь на одном GPU. На 8×H100 — 276 экспериментов, 29 улучшений.

---

## Эволюция: от человека в цикле к человеку как архитектору арены

### Vibe Coding (фев 2025)

> "You are not writing code directly 99% of the time, you are orchestrating agents who do."

Человек управляет AI-агентами, которые пишут код.

### Agentic Engineering (фев 2026)

> "You are not orchestrating either. You write a Markdown file. The agent experiments indefinitely."

Человек проектирует **арену** — среду с правилами и метриками. Агент итерирует внутри.

### Autoresearch (март 2026)

Рекурсивное самосовершенствование. Агент сам улучшает свою архитектуру, оптимизатор, гиперпараметры. Человек спит.

---

## Родственные техники

### Ralph Wiggum (Geoffrey Huntley, сер 2025)

Простейший цикл обратной связи:

```bash
while :; do cat PROMPT.md | claude-code ; done
```

- Агент получает промпт → пишет код → результат подаётся на вход → повтор
- Один инженер выполнил контракт на $50K за $297 API-затрат
- На YC hackathon команда за ночь получила 1000+ коммитов
- Anthropic сделал официальный Ralph Wiggum plugin для Claude Code

### Gas Town (Steve Yegge, янв 2026)

Масштабная фабрика из 20-30 AI-агентов:

- Архитектура напоминает Kubernetes: Control Plane (Mayor + Deacon) → Data Plane (Polecats + Witnesses)
- K8s спрашивает "is it running?", Gas Town спрашивает "is it done?"
- Человек описывает задачи на естественном языке
- 75,000 строк Go, 2,000 коммитов за 17 дней (написаны AI-агентами)

---

## Связь с другими статьями

- [Graph Engineering vs Loop Engineering](wiki/graph-engineering-vs-loop-engineering-2026.md) — autoresearch = чистый Loop Engineering (один агент, цикл, verifier). Bilevel Autoresearch = простейший Graph Engineering.
- [It Was Always a Loop](wiki/it-was-always-a-loop.md) — контраргумент: autoresearch ценен не как изобретение, а как teaching artifact, уместивший loop в 600 строк.

## Ключевые инсайты

### The Arena Is the Product

Побеждают не те, у кого больше инженеров или GPU. Побеждают те, у кого **лучший `program.md`**.

> "You can't just ask the agent to self-improve. You have to design the arena." — Garry Tan

### Фиксированный бюджет времени

Гениальное решение Karpathy — жёсткий лимит 5 минут на эксперимент. Неважно, что меняет агент — новая архитектура, другой оптимизатор, batch size. Каждый запуск получает ровно 5 минут и оценивается по одной метрике. Это позволяет честно сравнивать архитектурные изменения.

### Donald Knuth + Claude Opus 4.6

Knuth сообщил, что Claude Opus 4.6 решил графовую задачу, над которой он работал недели, за один час через 31 LLM-направленное исследование. Назвал это "dramatic advance in automatic deduction".

---

## Связь с QA-тестированием

Прямые параллели с agentic testing:

| Концепция | Autoresearch | Agentic Testing |
|-----------|-------------|-----------------|
| Арена | `train.py` + 5-min budget | Test suite + CI gates |
| Метрика | `val_bpb` | Pass/fail, mutation score, coverage |
| Стратегия | `program.md` | Specs, acceptance criteria |
| Цикл | Edit → train → eval → keep/discard | Generate → run → fix → retry |
| Масштаб | 100 exp/night | 100+ tests/run |

Aider с `--test-cmd` — тот же Ralph Wiggum loop, но для тестов. Playwright Test Agents — аналог Gas Town для QA.

---

## Ресурсы

- [autoresearch GitHub](https://github.com/karpathy/autoresearch) — оригинальный репозиторий
- [Karpathy tweets: autoresearch announcement](https://x.com/karpathy/status/2030371219518931079)
- [Karpathy coins 'agentic engineering'](https://x.com/karpathy/status/2019137879310836075)
- [Ralph Wiggum technique (Geoffrey Huntley)](https://ghuntley.com/ralph)
- [Gas Town (Steve Yegge)](https://github.com/steveyegge/gastown)
- [Garry Tan — полная статья](https://garryslist.org/posts/karpathy-just-turned-one-gpu-into-a-research-lab-f55754a6)





<!-- backlinks-start -->
### Backlinks
- [Graph Engineering vs Loop Engineering — The 2026 Agent Roadmap](wiki/graph-engineering-vs-loop-engineering-2026.md)
- [It Was Always a Loop](wiki/it-was-always-a-loop.md)
<!-- backlinks-end -->

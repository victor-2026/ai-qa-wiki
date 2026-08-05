# It Was Always a Loop

## Контекст

Июль 2026. Dinesh Karakambaka публикует эссе-контраргумент к хайпу вокруг Loop Engineering. Тезис: **loops не изобрели в 2026 — это тот же паттерн, что и термостат. Изменился только substrate (LLM вместо фиксированных правил).**

Источник: [Medium — It Was Always a Loop](https://medium.com/@kdineshkvkl/it-was-always-a-loop-1a216f3eeb3c)

---

## Три части цикла (которые работали задолго до AI)

Любой loop состоит из трёх компонентов, и термостат имеет все три:

| Компонент | Термостат | AI-агент |
|---|---|---|
| **Verifier** | Термометр | Тест pass/fail, метрика |
| **State** | Текущая температура | Что уже попробовано, история |
| **Stop condition** | Целевая температура | Goal met, или N attempts |

> "Repeat without a verifier is not progress. It is the model nodding along with its own last answer forever."

---

## Проблема нейминга

Эволюция терминов за последние годы:

```
Prompt Engineering → Context Engineering → Harness → Skills → Loop Engineering
```

Каждый термин называет реальное явление. Но:

- **Prompt engineering** = научиться точно формулировать запрос
- **Context engineering** = решить, что подать системе перед reasoning
- **Skill** = документированные conventions, которые инженеры вели годами под своими именами

Проблема не в тех, кто придумал термины (naming — это сервис). Проблема в нас, когда мы путаем **момент именования** с **моментом изобретения**.

> "The concepts didn't become true when a famous person described them — they became popular. Those are not the same event."

---

## AutoResearch как teaching artifact

Karpathy's autoresearch (см. [Karpathy: Autoresearch и Agentic Engineering](wiki/karpathy-autoresearch-agentic-engineering-2026.md)) ценен не тем, что изобрёл loop — а тем, что умещается в 600 строк и читается за afternoon.

- `train.py` — модель (агент редактирует)
- `prepare.py` — scorer (агенту нельзя трогать — "agent allowed to edit its own exam makes the exam easier")
- `program.md` — стратегия от человека

За 2 дня: ~700 экспериментов, ~20 улучшений, включая пропущенный scaler в attention.

---

## Bilevel Autoresearch (Qu & Lu, Mar 2026)

Единственный реально новый поворот: **meta-loop**. Внутренний loop делает обычную работу (propose → train → evaluate → keep/discard). Внешний loop смотрит на трассы, находит, где поиск застревает, и переписывает код, меняющий стратегию поиска.

На том же Karpathy benchmark: **2-loop версия beat single loop в 5 раз**. Причём обе использовали одну модель — выигрыш от архитектуры, а не от размера.

Связь с [Graph Engineering vs Loop Engineering](wiki/graph-engineering-vs-loop-engineering-2026.md): bilevel loop = граф из 2 узлов (inner + outer), где outer оптимизирует inner.

---

## Когда loop окупается

Четыре условия, которые должны быть все вместе:

1. **Task recurs** — задача повторяется
2. **Verification can be automated** — проверка автоматизируема
3. **Budget absorbs wasted tokens** —你有 бюджет на холостые попытки
4. **Agent has real tools** — агент может запустить и проверить свою работу

Пропусти одно — и хороший одноразовый prompt побьёт loop.

---

## Что loop не фиксит

### Comprehension debt

> "The faster it ships code you didn't write, the wider the gap between what's in your repo and what you understand."

Чем быстрее AI генерирует код, тем меньше ты понимаешь свою систему. Утро, когда ты дебажишь систему, которую никто не читал — этот счёт перевешивает все сэкономленные токены.

### Апатия

Когда loop работает, возникает соблазн перестать формировать своё мнение и принимать любой результат. Loop — это инструмент, а не замена мышлению. Два человека могут построить одинаковый loop и оказаться в противоположных точках.

---

## Универсальный prompt для loop

Из статьи — рабочий промпт, который можно скормить любому chat model:

```
Work in a loop until the result clears the bar.

TASK: [describe exactly what you want produced]
SUCCESS CRITERIA (strict — these are your gate):
- [criterion 1]
- [criterion 2]
- [criterion 3]

Each turn, out loud:
1. PLAN   — the single next thing you'll fix.
2. DO     — produce or improve the work.
3. VERIFY — score 1-10 on every criterion; say what's still weak.
4. DECIDE — all criteria 8+? print DONE and stop.
            Otherwise print ITERATING and go again, weakest score first.

Rules: never done below 8 on any criterion; each pass targets the last
turn's weakest score; don't ask me questions — assume and keep moving.

Begin.
```

---

## Связь с другими статьями

| Статья | Связь |
|--------|-------|
| [Karpathy: Autoresearch](wiki/karpathy-autoresearch-agentic-engineering-2026.md) | AutoResearch = чистый пример loop (verifier + state + stop), но не изобретение |
| [Graph Engineering vs Loop Engineering](wiki/graph-engineering-vs-loop-engineering-2026.md) | Bilevel Autoresearch = простейший граф (2 узла, inner + outer) |
| Loop Engineering | Термин, вокруг которого статья построена как контраргумент |

---

## Ресурсы

- [Оригинал на Medium](https://medium.com/@kdineshkvkl/it-was-always-a-loop-1a216f3eeb3c)
- [Karpathy — Autoresearch](wiki/karpathy-autoresearch-agentic-engineering-2026.md)
- [Graph Engineering vs Loop Engineering](wiki/graph-engineering-vs-loop-engineering-2026.md)


<!-- backlinks-start -->
### Backlinks
- [Graph Engineering vs Loop Engineering — The 2026 Agent Roadmap](wiki/graph-engineering-vs-loop-engineering-2026.md)
- [Karpathy: Autoresearch, Agentic Engineering и Self-Improvement Loops](wiki/karpathy-autoresearch-agentic-engineering-2026.md)
<!-- backlinks-end -->

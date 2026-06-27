# NotebookLM: Visuals for "Three AI Testing Frameworks" Article

## UC: Visual Thinking (UC14) + Slide Deck (UC12)

Нужно 3 визуала для статьи. Каждый — отдельный запрос в NotebookLM.

---

## Source Material (загрузить в NotebookLM как контекст)

| # | Source |
|---|--------|
| 1 | Текст статьи: `linkedin-posts/AI-Agents/5-three-ai-testing-frameworks.md` |
| 2 | MAS wiki: `ai-qa-wiki/wiki/mas-testing-framework.md` (только summary) |
| 3 | Playwright Agents: `ai-qa-wiki/wiki/playwright-test-agents-2026.md` (первые 80 строк) |
| 4 | Anton Gulin: `ai-qa-wiki/wiki/anton-gulin-3-layer-ai-qa-architecture.md` (первые 70 строк) |
| 5 | `known_patterns.json` — 8 patterns (MAS-realisation) |
| 6 | Autonoma entity audit — 59 models, 7 factories |

---

## Visual 1 — Cover Image (1200×644 px)

**Назначение:** Cover статьи в LinkedIn Pulse.

**Описание:** Трёхслойная диаграмма-стопка. Три горизонтальных блока друг над другом:

```
┌─────────────────────────────────────┐
│  MAS              WHO              │
│  Roles: Generator → Critic → Fixer │
│  Memory: learned_patterns.json     │
├─────────────────────────────────────┤
│  Playwright Agents   HOW           │
│  Tools: Planner → Generator → Heal │
│  Auto-recovery: DOM inspection     │
├─────────────────────────────────────┤
│  Anton Gulin 3-Layer  WHY         │
│  Architecture: Orchestration →     │
│  Execution → Evidence + 6 gates    │
└─────────────────────────────────────┘
```

Справа от стопки — стрелка вниз с текстом "Your Stack = All Three".

**Цвета:**
- MAS: синий (#2563EB)
- Playwright Agents: зелёный (#059669)
- Anton Gulin: оранжевый (#D97706)
- Фон: белый/светло-серый
- Шрифт: sans-serif

**Prompt для NotebookLM:**
```
Create a vertical stacked diagram showing three layers of AI testing frameworks.
Top layer: MAS (blue) — labeled "WHO: Roles". Middle layer: Playwright Agents (green) — labeled "HOW: Tools".
Bottom layer: Anton Gulin 3-Layer (orange) — labeled "WHY: Architecture".
Right side: a downward arrow labeled "Your Stack = All Three".
Output as a 1200×644 PNG suitable for LinkedIn Pulse article cover.
```

---

## Visual 2 — Comparison Table (1920×1080 px)

**Назначение:** Feed image (то что видят в ленте) + inline в статье.

**Таблица:**

| | MAS | Playwright Agents | Anton Gulin |
|---|---|---|---|
| **Abstraction** | Who (roles) | How (tools) | Why (architecture) |
| **Pipeline** | Gen → Critic → Fix → Exec | Plan → Gen → Heal | Orch → Exec → Evidence |
| **Output** | `.ts` + `learned_patterns.json` | `.md` → `.ts` + patches | Policy + evidence |
| **Memory** | Patterns accumulate | None per session | Checklist only |
| **Auto-heal** | ❌ | ✅ Healer | ❌ |
| **Evidence** | ❌ | Trace viewer | Trace + screenshot + log + video |
| **Human** | Mandatory gate | Optional | Mandatory gate |
| **Scope** | Any test type | Playwright E2E only | Any test type |
| **Example** | 8 patterns, 13 modules mapped | Healer concept, not yet measured | 6 gates, 32 tests, 570 artifacts |

**Стиль:** Minimal, clean, тёмный заголовок строки, чередующиеся строки.

**Prompt:**
```
Create a comparison table with 4 columns and 9 data rows.
Columns: empty header | MAS | Playwright Agents | Anton Gulin.
Data rows: Abstraction, Pipeline, Output, Memory, Auto-heal, Evidence, Human, Scope, Example.
Use a clean professional style. Header row dark background with white text.
Alternating row colors (white/light gray). Output as 1920×1080 PNG.
```

---

## Visual 3 — Architecture Diagram: Combined Stack (1920×1080 px)

**Назначение:** Визуализация комбинированного стека (раздел "Why You Need All Three").

**Схема:** Горизонтальный pipeline слева направо:

```
[Risk Question] → [Orchestration] → [Generation] → [Execution] → [Evidence] → [Review Gate]
      ↑               ↑                  ↑              ↑              ↑             ↑
  Anton Gulin      AGENTS.md          MAS Gen        Playwright     Allure +     Human
  Layer 1          boundaries         + Critic        + Healer       Traces      decision
```

**Prompt:**
```
Create a horizontal pipeline diagram flowing left to right.
Stages: Risk Question → Orchestration → Generation → Execution → Evidence → Review Gate.
Below each stage, show which framework covers it:
- Risk Question = "Anton Gulin Layer 1"
- Orchestration = "AGENTS.md boundaries"
- Generation = "MAS Generator + Critic"
- Execution = "Playwright Agents + Healer"
- Evidence = "Allure + Traces"
- Review Gate = "Human decision"
Use arrows between stages. Clean engineering style, sans-serif. Output as 1920×1080 PNG.
```

---

## Как использовать в NotebookLM

1. Создать Notebook с 4 source-файлами
2. В Chat отправить prompt для Visual 1 → сохранить результат
3. Повторить для Visual 2 и Visual 3
4. Экспортировать PNG → сохранить в `linkedin-posts/AI-Agents/4-cover.png`, `4-table.png`, `4-pipeline.png`
5. Обновить `[COVER: ...]` и `[SCREENSHOT: ...]` маркеры в статье

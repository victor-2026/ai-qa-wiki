# Ivan Davidov (Agentic Playwright Scaffold) — context engineering for QA agents

**Источник:** YouTube-интервью Sergii Khromchenko (Codemify) → Ivan Davidov, 2026. Транскрипт 515 сегментов, ~22K chars.
**Кто:** Ivan Davidov, ex-civil engineer → QA (4 года), Agentic Playwright Scaffold (open source), Founder ArchQA, workshops 4k+ engineers. Болгария, ex-Teva Pharmaceutical.
**Фильтр:** карьерная часть (зарплаты BG 1-6K, English B1/B2, LinkedIn+AI, YouTube-канал) — пропущена. Сохранено только техническое.

---

## 1. Context engineering: void, rot, progressive disclosure

Три понятия, которые Davidov использует в своей практике:

- **Context void** — агент стартует с blank page каждую сессию. Если не дать контекст, результат trash.
- **Context rot** — если впихнуть все сразу, агент stuck, output плохой.
- **Progressive disclosure** — давать необходимую информацию в правильный момент. (Отмечает: Anthropic выкатили это в late 2025.)

## 2. Аналогия «техническая книга» → orchestration as code

Структура подачи контекста как чтение учебника (из его civil engineering опыта — wastewater treatment plants):

1. Back cover — main idea (что за система)
2. Table of contents — какие топики есть
3. Preface — main rules (без правил «не играешь правильно»)
4. Chapters — deep domain knowledge, открывать только когда нужны
5. Appendixes/tables — только под конкретный edge case

Реализация: main orchestrator file = back cover + ToC + preface (правила). Отдельные chapters под задачи: UI testing → только главы UI + POM + locators, все остальное dormant, контекст не pollute.

## 3. Agentic Playwright framework (open source)

- За несколько дней до интервью выложил biggest part своего agentic Playwright test automation framework.
- Строил около года. Задача — баланс: architecture of the tool + QA standards + power of AI.
- Позиция: сначала понять full-stack (язык, backend, frontend глубоко), потом automation — иначе архитектуры не будет.

## 4. «Stricter referee» (ad-read в видео, TestSprite/Testr CLI)

Встроенная реклама open-source CLI, но тезис точный и наш:
- «If your agent writes code, runs unit tests against local mocks, sees green and reports done — it's grading its own homework».
- «Stop chasing the bigger model. Build the stricter referee».
- Замкнутый loop: agent вызывает verifier midbuild → real browser против live deployed app (no mocks) → failure bundle (failing step + screenshot + root-cause fix) → agent патчит → runs to green unattended.
- Пометить как vendor claim, не verified evidence — но формулировка referee/verifier ложится на нашу Evidence-тему.

## 5. Афоризмы в нашу копилку

- «If a QA cannot achieve quality in their own work, how are they going to improve the quality of the work of others».
- Reverse-engineer the goal: цели наружу → разбить на мелкие → найти path.
- Агенты как способ пропустить blank-page страх: выполнить задачу самому → отдать агенту на review и feedback (ускорение обучения против ожидания senior review).

## Связки с нашей работой

- Progressive disclosure = тот же принцип, что заложен в /brief (читать только хвосты checkpoint, не полные файлы) и в memory budget. Davidov дает готовую аналогию «книга» для объяснения.
- Referee/verifier loop = runtime enforcement (Radik ledger gate) + Evidence gate #5, третья независимая формулировка за 2 дня.
- Scaffold Davidov — кандидат на разбор: сравнить его архитектуру chapters/orchestrator с нашей POM-структурой OrangeHRM при случае.
- НЕ сохраняем: зарплаты, English, LinkedIn-тактики, промо курсов Codemify (1-1, agentic course каждые 2 мес) — vendor marketing.

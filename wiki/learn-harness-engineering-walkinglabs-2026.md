# Learn Harness Engineering (walkinglabs, 17.8K stars, MIT)

**Source:** https://github.com/walkinglabs/learn-harness-engineering (265 commits, 14 lectures + 8 projects + resource library, 15 languages incl. Russian)
**Status:** external course; taken as patterns, not adopted wholesale

## Саммари

Проектный курс по инженерии харнесов: модель решает что писать, харнес — когда/где/как. Five-subsystem framework: Instructions / State / Verification / Scope / Session Lifecycle. Доказательная база: Anthropic Opus 4.5 — без харнеса $9/20 мин нерабочее, с полным харнесом (planner+generator+evaluator) $200/6 ч играбельное. Плюс Loop engineering (L13) и Graph engineering (L14), разборы харнесов Pi / Claude Code / Codex / DeepSeek, skill `harness-creator` (скаффолд AGENTS.md + feature lists + init.sh + verification workflows).

## Пять подсистем (маппинг на нашу практику)

| Подсистема | У них | У нас |
|------------|-------|-------|
| Instructions | AGENTS.md, CLAUDE.md, progressive disclosure | AGENTS.md в корне + Boundaries-таблица (кросс-вендорный стандарт) |
| State | progress.md, feature_list, git log, session handoff | session-checkpoint.md (append-only шина окон) + wiki/log.md |
| Verification | tests + lint + type-check, "agent stops only when verification passes" | wiki_lint.py + P1 хук на правки wiki; reviewer-сплит (план ТЗ) |
| Scope | one feature at a time, definition of done | per-task скоупы окон (window-discipline: one file one owner) |
| Session Lifecycle | init.sh, clean-state checklist, handoff note | бэкап-ритуал + чекпоинт в конце сессии |

## Что забираем точечно

1. **Maker-checker loops (L13/P07 + шаблоны maker/checker-prompt.md)** — теория под наш reviewer-паттерн; референс для ТЗ по оркестрации вместо выдумывания.
2. **L09 victory-too-early (confidence ≠ correctness)** — доктринально наше (silent green), с чужими цифрами.
3. **L12 clean handoff** — аргумент за append-only чекпоинт.
4. **Pi harness breakdown** — разбор харнеса нашего стека, материал к пилоту ТЗ.
5. **Resource library** (AGENTS.md/feature_list.json/init.sh шаблоны) — сверить наши файлы с их шаблонами при случае.

## Связь

- [[pi-subagents-2026]] / [[pi-opencode-integration-2026]] — наша инфраструктура делегации, которой курс дает теорию.
- [[ai-qa-tool-evaluation-mutation-matrix]] — verification-слой того же стека идей (независимый оракул).
- **Кросс-волт:** outputs/tz-small-opencode-orchestrator-draft.md — maker-checker и Flat Fan туда уже вшиты.

## Caveat

- Курс масштабный (8 фаз, капстоун Electron-app) — берем паттерны, не прохождение.
- Цифры Anthropic ($9 vs $200) — из их материалов, первоисточник не открывался.
- Raw не заводился: первоисточник — URL выше.

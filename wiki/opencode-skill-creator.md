# opencode-skill-creator: Eval-Driven Skill Development

**Автор:** Anton Gulin ([GitHub](https://github.com/antongulin/opencode-skill-creator))
**Лицензия:** Apache 2.0
**Пакет:** npm — `opencode-skill-creator`
**Звёзд:** ★123 (на 2026-06-25)
**Релизы:** 21 (последний v0.2.20, Jun 17 2026)

---

## Что это

Плагин + скилл для OpenCode, который превращает создание скиллов из гадания в **eval-driven development** (разработку, управляемую оценкой). Адаптация официального [skill-creator](https://github.com/anthropics/skills/tree/main/skills/skill-creator) от Anthropic для Claude Code, портированная на TypeScript под архитектуру плагинов OpenCode.

## Ключевая идея

Обычно скилл пишут на глаз, тестируют вручную и надеются, что description сработает. Gulin перенёс методологию train/test split из ML в разработку скиллов:

| Этап | Что происходит |
|------|----------------|
| Analyze | Определение типа скилла и его границ |
| Create | Генерация SKILL.md + фронтматтер + структура |
| Eval Set | 20 тестовых запросов: should-trigger + should-not-trigger |
| Evaluate | Каждый запрос прогоняется 3 раза (для статистики) |
| Optimize | LLM улучшает description на основе паттернов ошибок |
| Benchmark | Сравнение итераций с variance analysis |
| Install | Деплой проверенного скилла в `.opencode/skills/` |

## Основные компоненты

### Skill (Markdown-инструкции)

```
opencode-skill-creator/
├── SKILL.md                  — инструкции для агента
├── agents/
│   ├── grader.md             — оценка assertion'ов
│   ├── analyzer.md           — анализ бенчмарков
│   └── comparator.md         — слепое A/B сравнение
├── references/
│   └── schemas.md            — JSON schema
└── templates/
    └── eval-review.html      — UI для просмотра eval-сета
```

### Plugin (TypeScript — npm пакет)

8 инструментов, которые агент вызывает в процессе:

| Инструмент | Назначение |
|------------|------------|
| `skill_validate` | Проверка структуры SKILL.md |
| `skill_parse` | Извлечение name/description из SKILL.md |
| `skill_eval` | Тест точности триггеринга |
| `skill_improve_description` | LLM-улучшение description |
| `skill_optimize_loop` | Полный цикл eval → improve (до 5 итераций) |
| `skill_aggregate_benchmark` | Агрегация результатов → статистика |
| `skill_generate_report` | HTML-отчёт оптимизации |
| `skill_serve_review` | HTTP-сервер для просмотра eval |
| `skill_stop_review` | Остановка review-сервера |
| `skill_export_static_review` | Статический HTML-файл для ревью |

## Ключевые фичи

### 1. Description Optimization Loop

Самая мощная возможность. Description скилла обрабатывается как задача поиска:

1. Генерация 20 тестовых запросов (should-trigger + should-not-trigger)
2. Сплит 60% train / 40% test
3. Каждый запрос прогоняется 3 раза (надёжность статистики)
4. Анализ паттернов ошибок
5. LLM предлагает улучшенный description
6. Переоценка на train AND test (предотвращение overfitting)
7. Выбор лучшего по test-score
8. До 5 итераций

### 2. Review Workflow Guard

По умолчанию требует paired comparison (with_skill vs without_skill). Если пары отсутствуют — инструмент падает с явной ошибкой. Можно переопределить через `allowPartial: true`.

### 3. Skill Draft Staging

Новые скиллы создаются в `/tmp/opencode-skills/<skill-name>/`, вне репозитория. Только финальная версия копируется в `.opencode/skills/` или `~/.config/opencode/skills/`.

### 4. Чистая миграция

При обновлении плагин автоматически бэкапит старую папку `skill-creator` в `skill-creator.opencode-skill-creator-backup-YYYYMMDDTHHMMSS/`.

## Чем отличается от Anthropic оригинала

| Аспект | Anthropic (Claude Code) | Gulin (OpenCode) |
|--------|------------------------|-------------------|
| CLI | `claude -p "prompt"` | `opencode run "prompt"` |
| Путь скиллов | `.claude/commands/` | `.opencode/skills/` |
| Скрипты | Python (`scripts/*.py`) | TypeScript plugin (`plugin/lib/*.ts`) |
| Eval Viewer | Python (generate_review.py) | `skill_serve_review` tool |
| Бенчмаркинг | Python (aggregate_benchmark.py) | `skill_aggregate_benchmark` tool |
| Зависимости | Python 3.11+, pyyaml | Bun + @opencode-ai/plugin |
| Упаковка | `.skill` zip-файлы | npm пакет + skill-папка |
| Саб-агенты | Встроенный subagent concept | Task tool с general/explore |

## Плюсы для QA-инженера

1. **Измеримость** — вместо "скилл вроде работает" получаете точность триггеринга в процентах
2. **Train/test split** — защита от overfitting (скилл срабатывает только на тех запросах, на которых его тестировали)
3. **Воспроизводимость** — 3 прогона на запрос, variance analysis, benchmark между итерациями
4. **Human-in-the-loop** — review viewer с paired comparison перед деплоем
5. **Экосистема** — npm пакет, Apache 2.0, 21 релиз, активный open source

## Связь с другими статьями

- [[people/anton-gulin]] — профиль автора: Lead SDET, бывший Apple, первый "AI QA Architect" в LinkedIn. Gulin — не только автор этого пакета, но и создатель **3-Layer Architecture** и **pw-kit**.
- [[anton-gulin-3-layer-ai-qa-architecture]] — оркестрация, экзекьюшен, evidence. opencode-skill-creator логически встраивается в Layer 1 (Orchestration): создание скилла = формализация того, *какой риск и как* должен покрывать AI-агент.
- [[agent-skills-specification]] — общая экосистема скиллов (структура, автотриггеринг, 3 категории). opencode-skill-creator — инструмент, который *создаёт* такие скиллы с измеряемым качеством. Упоминается в статье как #10 в списке 15 скиллов.
- [[playwright-test-agents-2026]] — Playwright Planner/Generator/Healer. Gulin не упоминает их явно, но его eval-driven методология применима к описаниям Planner-скиллов: можно измерить, насколько хорошо Planner триггерится на "create a test for login flow".
- [[offline-evaluation-trajectories-2026]] — методология самопроверки скиллов (4 оси). opencode-skill-creator даёт *внешнюю* объективную метрику (trigger accuracy), которая дополняет самопроверку.
- [[ai-fluency-interview-2026]] — AI-интервью: методология Gulin применима для создания скиллов подготовки к собеседованиям с eval-driven quality.
- **superpowers** skill — /brainstorm, /write-plan, /execute-plan. opencode-skill-creator может создавать такие же многошаговые скиллы, но с гарантией качества через eval.

---

## Русское саммари

**opencode-skill-creator** — это npm-пакет + скилл от Антона Гулина, который позволяет создавать, тестировать и оптимизировать скиллы для OpenCode не на глаз, а с измеряемой точностью.

**Как работает:** Генерируется 20 тестовых запросов (половина должна триггерить скилл, половина — нет), скилл прогоняется 3 раза на каждом, анализируются ошибки, LLM улучшает описание, и так до 5 итераций. Результат — скилл с известной точностью срабатывания, без переобучения на конкретные примеры (train/test split).

**Главные плюсы:**
- Вместо "вроде работает" — проценты и статистика
- Адаптация методологии Антропик под OpenCode (TypeScript вместо Python)
- Встроенный human review перед деплоем
- 8 плагин-инструментов (валидация, eval, оптимизация, бенчмаркинг, отчёты)
- Apache 2.0, открытый исходный код, 21 релиз

**Кому нужно:** Тем, кто пишет скиллы для OpenCode и хочет знать, что они реально работают, а не просто "вроде срабатывают иногда".

## Установка

```bash
npx opencode-skill-creator install --global
```

После установки и рестарта OpenCode — попросить:

> Create a skill that helps with Docker compose files

## Источники

- [GitHub: antongulin/opencode-skill-creator](https://github.com/antongulin/opencode-skill-creator)
- [npm: opencode-skill-creator](https://www.npmjs.com/package/opencode-skill-creator)
- [Anthropic original (Claude Code)](https://github.com/anthropics/skills/tree/main/skills/skill-creator)
- [Anton Gulin — anton.qa](https://www.anton.qa)




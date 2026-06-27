---
title: "Agent Skills — экосистема скиллов для AI-агентов"
updated: 2026-05-26
tags: [skills, agents, opencode, claude, tools]
type: reference
---

# Agent Skills — экосистема скиллов для AI-агентов

**Источник:** [thecode.media](https://thecode.media/agent-skills-dlya-ii-agentov/) — статья Леры Турчак, май 2026

---

## Что такое скилл

Скилл — папка с файлами, которая учит агента делать что-то правильно без повторных объяснений.

### Структура
```
skill-name/
  SKILL.md       — обязательный, инструкции в Markdown + YAML фронтматтер
  scripts/       — опционально, исполняемый код (Python, Bash)
  references/    — опционально, документация
  assets/        — опционально, шаблоны, шрифты, иконки
```

### Автотриггеринг
Агент сам решает, какой скилл применить, читая description в YAML-фронтматтере. Хороший скилл триггерится на 90% релевантных запросов без явного вызова.

### Три категории
1. **Создание документов и артефактов** — дизайн, код, презентации
2. **Автоматизация процессов** — многошаговые процессы с валидацией
3. **Усиление MCP-интеграций** — MCP = кухня, скилл = рецепт

---

## 15 скиллов из статьи

| # | Скилл | Суть | opencode? |
|---|-------|------|-----------|
| 1 | PDF чтение | Извлекает таблицы, объединяет, разбивает | ✅ `pypdf` |
| 2 | DOCX создание | Генерация .docx с таблицами, стилями | ✅ `textutil` / `python-docx` |
| 3 | XLSX таблицы | Excel с формулами, сводными, графикой | ❓ openpyxl руками |
| 4 | Frontend Design | Выбор стиля (минимализм, ретро и т.д.) | ✅ пишем HTML напрямую |
| 5 | Web Artifacts | Интерактивные формы, калькуляторы без React | ✅ пишем HTML напрямую |
| 6 | Superpowers (20+ сценариев) | `/brainstorm`, `/write-plan`, `/execute-plan` | ❓ нет аналога |
| 7 | Debugging (4 шага) | Воспроизвести → сузить → найти причину → исправить | ✅ встроено в QA workflow |
| 8 | File Search (ripgrep + ast-grep) | Поиск по тексту и структуре кода | ✅ Glob + Grep tools |
| 9 | Context Engineering | Сжатие истории, снижение расхода токенов | ❓ нет прямого аналога |
| 10 | Skill Creator | Создать новый скилл за 5 минут через вопросы | ✅ делаем руками |
| 11 | Video from Code (Remotion) | Видео как React-компоненты → MP4 | ❓ не используем |
| 12 | SEO Audit | 12 параллельных проверок сайта | ❓ не используем |
| 13 | Marketing Skills (20+) | SEO, CRO, copywriting, analytics | ❓ не используем |
| 14 | Webapp Testing (офиц. Anthropic) | Playwright сценарии для твоего приложения | ✅ уже есть в Buzzhive |
| 15 | Playwright Browser Automation | Любой сайт, взаимодействие как человек | ✅ уже есть в Buzzhive |

---

## Что уже работает в opencode (без плагинов)

| Возможность | Инструмент |
|-------------|------------|
| PDF чтение | `python3` + `pypdf` |
| DOCX создание | `textutil -convert docx` или `python-docx` |
| XLSX таблицы | `python3` + `openpyxl` ✅ |
| HTML/JS прототипы | `write → open` |
| Поиск по коду | Glob + Grep tools |
| QA тестирование | Playwright (TypeScript) + Jest + PBT |
| Go тестирование | `go test` + table-driven + `playwright-go` |
| Создание скиллов | `~/.config/opencode/skills/<name>/SKILL.md` |
| Superpowers | `/brainstorm`, `/write-plan`, `/execute-plan` ✅ |
| Skill Creator | диалоговая генерация скиллов ✅ |
| Context Engineering | компрессия контекста, чекпоинты ✅ |

---

## Установка скиллов в разных агентах

| Агент | Путь |
|-------|------|
| Claude Code | `/plugin install ...` или `npx skills add ...` → `~/.claude/skills/` |
| Cursor | `.cursor/skills/<name>/SKILL.md` (проект) или `~/.cursor/skills/` (глобально) |
| Gemini CLI | `.gemini/skills/<name>/SKILL.md` или `.agents/skills/` |
| **OpenCode** | **`~/.config/opencode/skills/<name>/`** — авто-обнаружение |

---

---

## QA Use-Cases: какие скиллы применять для тестирования

| Ситуация | Скиллы | Что делают |
|----------|--------|------------|
| **Нужно написать тесты для API** | `rest-api-qa` + `qa-automation-engineer` | rest-api-qa задаёт структуру (endpoints, методы, статусы), qa-automation-engineer генерирует Playwright-код |
| **Тесты падают без причины** | `qa-automation-engineer` + `context-engineering` | qa-automation-engineer чинит flaky через expect().poll(), context-engineering сжимает историю поиска причины |
| **Нужен отчёт для тимлида** | `xlsx-qa` + `universal-qa-expert` | xlsx-qa генерирует Excel, universal-qa-expert подсказывает DORA-метрики и уровень Elite/High/Medium |
| **Рефакторинг большого тестового файла** | `superpowers` (/brainstorm + /write-plan) + `qa-automation-engineer` | /brainstorm ищет подход, /write-plan разбивает на фазы, qa-automation-engineer выполняет |
| **Нагрузочное тестирование** | `load-stress-qa` + `xlsx-qa` | load-stress-qa пишет k6-скрипты, xlsx-qa оформляет результаты |
| **Проверка безопасности API** | `rest-api-qa` + `qa-automation-engineer` | rest-api-qa находит незащищённые endpoints, qa-automation-engineer пишет тесты на 401/403 |
| **Первая неделя в новом проекте** | `context-engineering` + `skill-creator` | context-engineering учит работать с контекстом, [[opencode-skill-creator]] создаёт кастомные скиллы под проект |
| **Собеседование / резюме** | `career-mentor` + `tech-writer` + `universal-qa-expert` | career-mentor правит резюме, tech-writer пишет LinkedIn post, universal-qa-expert формулирует достижения |

---

## Установка скиллов в OpenCode

В OpenCode скиллы не требуют установки — они **авто-обнаруживаются** из папки:

```
~/.config/opencode/skills/<skill-name>/SKILL.md
```

### Как добавить новый скилл

```bash
# 1. Создать папку
mkdir -p ~/.config/opencode/skills/my-skill

# 2. Создать SKILL.md с YAML фронтматтером
#    (описание = условие автотриггеринга)

# 3. Готово — перезапуск не нужен
```

### Как проверить, что скилл работает

Дай команду, которая соответствует `description` в YAML. Если скилл подхватился — увидишь его инструкции в ответе агента.

Можно явно спросить: *«Какой скилл сейчас активен?»*

### Как удалить скилл

```bash
rm -rf ~/.config/opencode/skills/my-skill
```

Скилл перестанет триггериться сразу после удаления.

---

## Совместимость скиллов

### Можно использовать одновременно (без конфликтов)

| Комбинация | Почему работает |
|-----------|----------------|
| `qa-automation-engineer` + `rest-api-qa` | Разные роли: кодогенерация + спецификация API |
| `xlsx-qa` + `universal-qa-expert` | Один генерирует Excel, второй подсказывает метрики |
| `career-mentor` + `tech-writer` | Оба про карьеру, но не пересекаются по задачам |
| `superpowers` + `skill-creator` | superpowers ставит план, skill-creator создаёт файлы |
| `context-engineering` + любой другой | context-engineering управляет контекстом, не влияет на логику |
| `universal-qa-expert` + `load-stress-qa` | universal-qa-expert видит общую картину, load-stress-qa — узкую |

### Не рекомендуется вместе

| Комбинация | Почему |
|-----------|--------|
| `qa-automation-engineer` + `go-qa` + `java-qa` | Три скилла генерации кода — агент запутается, какой язык выбрать |
| `career-mentor` + `xlsx-qa` | Совершенно разные домены (карьера vs Excel), лишний шум |
| `superpowers` + `/write-plan` без `execute-plan` | Superpowers даёт план, но если не выполнять — бесполезно |

### Ограничения платформы

- **Максимум:** 20-50 активных скиллов одновременно (официальная рекомендация Claude)
- **Проблема при превышении:** падает качество автотриггеринга — агент начинает путать, какой скилл применить
- **OpenCode:** текущих 12 скиллов — комфортное количество. Можно расширять до ~20 без потери качества

---

## Источники
- [Статья на thecode.media](https://thecode.media/agent-skills-dlya-ii-agentov/)
- [Документация Claude Code Skills](https://code.claude.com/docs/en/skills)
- [aitmpl.com/skills](https://aitmpl.com/skills) — каталог скиллов
- [skills.sh](https://skills.sh) — каталог скиллов

---
title: "Obsidian Skills by Steph Ango (kepano)"
updated: 2026-05-04
tags: [obsidian, skills, kepano, AI, agent-skills, opencode]
type: guide
---

# Obsidian Skills by Steph Ango (kepano)

**GitHub:** https://github.com/kepano/obsidian-skills  
**Article:** https://pimenov.ai/blog/ceo-obsidian-napisal-skilly-dlya-claude-code/  
**License:** MIT  
**Stars:** 13,000+ ⭐  

---

## Overview

CEO Obsidian **Steph Ango (kepano)** лично написал официальный набор **Agent Skills** для Obsidian. Это не просто PR-ход, а признание: если агенты не умеют работать с инструментом правильно, они будут работать плохо, а пользователи решат, что виноват инструмент.

> "Если вы делаете инструмент и хотите, чтобы ИИ-агенты с ним работали — нужно самим описать правила игры."

---

## 4 Ключевых навыка (Skills)

### 1. Obsidian Markdown
**Что делает:** Учит агента правильно работать с вики-ссылками, callout-блоками, frontmatter-метаданными.

**Почему важно:** Без этого агент генерирует обычный Markdown, и вся сила Obsidian (двусторонние связи, графы знаний, структурированные свойства) теряется.

**Пример инструкции:**
```markdown
# Obsidian Markdown Skill

Use wikilinks [[Note Name]] for internal links.
Use callouts: > [!info] Title\n> Content
Always include YAML frontmatter with tags and type.
```

---

### 2. Bases
**Что делает:** Работа с базами данных Obsidian (типизированные свойства, фильтры, сортировки, представления).

**Возможности:**
- Создание CRM-таблиц
- Трекеры задач
- Исследовательские базы данных

**Пример использования агентом:**
```yaml
# Bases skill teaches:
filters:
  and:
    - file.hasTag("task")
    - 'status != "done"'
```

---

### 3. JSON Canvas
**Что делает:** Генерация и редактирование визуальных канвасов внутри хранилища.

**Преимущество:** Как Miro, только локально. Нет зависимости от облака (JSON-файлы внутри vault).

**Структура:**
```json
{
  "nodes": [{"id": "node1", "type": "text", "text": "Idea"}],
  "edges": [{"fromNode": "node1", "toNode": "node2"}]
}
```

---

### 4. CLI (Command Line Interface)
**Что делает:** Управление vault через командную строку.

**Возможности:**
- Создание заметок
- Поиск по vault
- Редактирование без GUI

```bash
# CLI commands for agents
obsidian note create "New Note"
obsidian search "query" --tag AI
obsidian edit "Note" --append "Content"
```

---

## Совместимость

| Агент | Поддержка |
|-------|----------|
| **Claude Code** | ✅ Нативно |
| **OpenCode** | ✅ Нативно (`.opencode/skills/`) |
| **GitHub Copilot** | ✅ Через Agent Skills спесификацию |
| **Cursor** | ✅ Совместимо |
| **Codex CLI** | ✅ Упомянут в статье |

---

## Study Guide Summary

### Quiz Answers (Key Points)

1. **Кто создал:** Steph Ango (kepano), CEO Obsidian → важно, так как создатель продукта сам определяет правила для агентов
2. **Риск без правил:** Пользователи винят инструмент, а не ИИ-агента
3. **Obsidian Markdown:** Учит вики-ссылкам, callouts, frontmatter (сохраняет графы знаний)
4. **Bases:** Типизированные свойства, фильтры, CRM-таблицы, трекеры задач
5. **JSON Canvas:** Визуальные канвасы локально (без облака, как Miro)
6. **CLI:** Управление vault через текстовые команды без GUI
7. **Совместимость:** Claude Code, Codex CLI, любой агент с Agent Skills спесификацией
8. **Почему создатель:** Чтобы агенты работали предсказуемо и качественно
9. **Agent Skills:** Открытый стандарт, obsidian-skills — реализация для Obsidian
10. **Тренд индустрии:** Каждый инструмент будет поставляться с «инструкцией для ИИ»

---

## Essay Questions (Discussion Points)

1. **Смена документации:** От «документации для людей» к «структурированным описаниям для ИИ»
2. **ИИ как power user:** Claude Code управляет vault не хуже человека (графы знаний, заметки, канвасы)
3. **Прецедент «правил игры»:** Другие CEO последуют примеру Steph Ango для защиты бренда
4. **Локальный ИИ:** JSON Canvas — данные остаются в vault (философия PKM)
5. **Открытые стандарты:** MIT license, GitHub stars → коллаборативная экосистема

---

## Glossary

| Термин | Определение |
|---------|-------------|
| **Agent Skills** | Открытый стандарт упаковки знаний для ИИ-агентов |
| **Bases** | Базы данных в Obsidian (свойства, фильтры, таблицы) |
| **JSON Canvas** | Визуальные канвасы в формате JSON (локально) |
| **CLI** | Управление vault через командную строку |
| **Frontmatter** | YAML-метаданные в начале Markdown файла |
| **Vault** | Папка с заметками Obsidian |
| **Wiki-links** | Синтаксис `[[Note]]` для двусторонних ссылок |
| **MIT License** | Открытая лицензия obsidian-skills репозитория |

---

## Установка в OpenCode

```bash
# Клонировать репозиторий
git clone https://github.com/kepano/obsidian-skills.git ~/.opencode/skills/obsidian-skills

# Проверить
/skills
```

**Пути поиска OpenCode:**
- `~/.opencode/skills/obsidian-skills/` ✅
- `~/.config/opencode/skills/` ✅
- `.claude/skills/` ✅ (совместимость)
- `.agents/skills/` ✅ (совместимость)

---

## Связанные материалы

| Ресурс | Ссылка |
|--------|---------|
| GitHub репозиторий | https://github.com/kepano/obsidian-skills |
| Статья Pimenov.ai | https://pimenov.ai/blog/ceo-obsidian-napisal-skilly-dlya-claude-code/ |
| Agent Skills Specification | https://agentskills.io/specification |
| OpenCode Skills Docs | https://opencode.ai/docs/skills/ |

---

## См. также

- [[agent-skills-specification]] — спецификация Agent Skills
- [[obsidian-bases-plan]] — план создания Bases для wiki
- [[HARDWARE_SPEC.md]] — настройка Obsidian Skills в opencode

---

**Tags:** #Obsidian #Skills #kepano #AgentSkills #OpenCode #AI #PKM  
**Updated:** 2026-05-04

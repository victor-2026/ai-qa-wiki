# AI-QA Wiki — Obsidian Vault Setup

## Troubleshooting

### Plugins Disabled / Button Not Working

**Common issues and solutions:**

| Problem | Cause | Solution |
|---------|-------|----------|
| "Turn on community plugins" button disabled | **Restricted mode** is ON | Click left of button — disable Restricted mode |
| Plugins disabled after restart | iCloud sync issue | Vault settings → Keep Downloaded |
| "Lazy Plugin Loader" causes issues | Plugin bug | Disable this plugin |
| Failed to install plugin | Internet/firewall | Download manually to `.obsidian/plugins` |
| Template folder lost (empty path) | Templates settings reset | Set: Settings → Templates → Folder → выбери папку |
| Periodic Notes settings lost | Plugins settings reset | Reconfigure in plugin settings |

### How to Manually Install Plugin

1. Download plugin from GitHub (release .zip)
2. Extract to `~/.obsidian/plugins/PLUGIN_NAME/`
3. Restart Obsidian

### Backup Plugins

```bash
# Backup your plugins
cp -r ~/.obsidian/plugins ~/ObsidianBackup/plugins
```

---

## Quick Start

### 1. Open as Vault

1. Open Obsidian → "Open folder as vault"
2. Select: `~/Projects/ai-qa-wiki`

### 2. Enable Wikilinks

**Settings → Files & Links** → ON: "Use [[wikilinks]]"

### 3. Recommended Plugins

| Plugin | Purpose |
|--------|--------|
| **Dataview** | Query notes like database |
| **Quick Explorer** | Fast navigation |
| **Auto Template Prompt** | Daily notes |
| **Tasks** | Todo management |

Install: Community Plugins → search name

---

## Vault Structure

```
ai-qa-wiki/
├── wiki/              ← основные заметки
│   ├── mas-risks.md
│   ├── three-way-comparison.md
│   └── ...
├── raw/              ← исходники
├── outputs/           ← сгенерированное
└── Obsidian-Setup.md ← этот файл
```

---

## Hub Notes (рекомендую создать)

### `[[AI-Testing-Map]]`
Главный хаб — обзор всей системы

### `[[MAS-Pipeline]]`
Ссылка на wiki/mas-testing-framework.md

### `[[RISKS]]`
Ссылка на wiki/mas-risks.md

---

## Search & Link

### Быстрый поиск
- `Ctrl+P` → Quick switcher
- `Ctrl+Shift+F` → Search in all files

### Создать связь
Пиши `[[` → начни писать → выбери заметку

### Посмотреть связи
В заметке → правый сайдбар → **Backlinks**

---

## Graph View

**Ctrl+G** → Graph View

- **Центр** — текущая заметка
- **Размер** — кол-во связей
- **Цвет** — кластеры (темы)

---

## Daily Notes (опционально)

Создай заметку на сегодня:
```
[[2026-04-19]]
```

Добавь линки:
```
Related: [[MAS-Pipeline]], [[RISKS]]
```

---

## Groq Integration

Можно добавить в заметку:
```markdown
## Last Research

![[qa_2026-04-19_163317]]  ← output из Groq
```

---

## Следующий шаг

1. Открой `~/Projects/ai-qa-wiki` в Obsidian
2. Включи wikilinks
3. Открой Graph View (Ctrl+G)
4. Начни добавлять `[[links]]` в заметки
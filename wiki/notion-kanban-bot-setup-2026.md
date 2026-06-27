# Notion Kanban + Bot Integration Setup

**Дата:** 2026-06-19
**Источники:** `~/bot/bot.py`, `~/bot/notion-sync-kanban.py`, `~/Projects/Articles/AGENTS.md`, `~/.opencode-memory.md`

## Архитектура

Notion Tasks DB — **source of truth** для всех задач. Локальные `kanban/*.md` файлы — авто-генерируемое зеркало.

```
Notion Tasks DB  ──→  ~/bot/notion-sync-kanban.py  ──→  kanban/*.md
                   ──→  ~/bot/bot.py (poll)  ──→  Telegram / opencode auto-dispatch
```

## Компоненты

### 1. Notion Tasks DB (Kanban)
- **DB ID:** `37da5ab6-666f-8028-a641-fdc8bfa0574b`
- **Статусы:** Backlog, This Iteration, In progress, Not started, To-do, Done, Complete, Cancelled
- **Поля:** Task name (title), Project (select), Status (status)
- **Проекты:** Articles, Bot, Buzzhive, Career, Notion, OrangeHRM, QA Architecture (Cross-Project), playwright-test-agents, Uncategorized
- **Всего задач:** ~90

### 2. Notion Test Runs DB
- **DB ID:** `382a5ab6-666f-81b5-8f5d-e6f1d415677f`
- **Назначение:** импорт результатов Allure-тестов
- **Скрипт:** `scripts/allure-to-notion.py` (парсит `allure-results/*.json` → Notion)
- **Интеграция:** добавлен step в 4 GitHub Actions workflow (playwright, nightly, mutation, contracts)
- **Импортировано:** 82 теста (34 qa-automation-sandbox + 48 OrangeHRM)

### 3. Telegram Bot (`~/bot/bot.py`)
- **Платформа:** python-telegram-bot (polling)
- **Запуск:** launchd (`com.user.tg-opencode`)
- **Токен:** `~/.notion-token` (ai-qa-wiki-bot)
- **Чат:** `117754174`

**Функции:**
- `/kanban <project> [keyword]` — поиск задач в локальном kanban
- `/kanban <project> [keyword] run` — запуск задачи через opencode
- poll_kanban_sync() — каждые 60с проверяет `kanban/*.md` на "In Progress"
- poll_notion_sync() — каждые 60с проверяет Notion Tasks DB на "In progress"
  - Если найдена новая задача → пытается запустить через `opencode run --attach`
  - Если opencode сессия не активна → уведомление в Telegram

**Dispatch tracker:** `~/bot/dispatch_state.json` — предотвращает повторный запуск задач

### 4. Синхронизация Notion → локальные файлы
- **Скрипт:** `~/bot/notion-sync-kanban.py`
- **Частота:** по запросу (планируется cron/авто)
- **Результат:** 9 файлов в `~/Projects/Articles/kanban/`
- **Принцип:** тупая перезапись — файлы НЕ редактировать вручную

## Source of Truth

| Слой | Source of Truth | Редактирование |
|------|----------------|----------------|
| Задачи (канбан) | Notion Tasks DB | Только в Notion |
| Локальные kanban/*.md | Зеркало | Не редактировать |
| Wiki-статьи | ai-qa-wiki/wiki/ | AI generates from raw/ |
| LinkedIn-посты | linkedin-posts/*.md | AI + user review |
| Сессионные логи | session-checkpoint.md | AI пишет |

## Ключевые файлы

```bash
# Токены
cat ~/.notion-token        # ai-qa-wiki-bot (доступ ко всем БД)
cat ~/.notion-token-2      # all-connection-1 (не подключён к страницам)

# Бот
code ~/bot/bot.py
code ~/bot/notion-sync-kanban.py
code ~/bot/allure-to-notion.py

# Логи
tail -f ~/bot/bot.log

# Локальные kanban
ls ~/Projects/Articles/kanban/
```

## Важные нюансы

- **Status filter case-sensitive:** в Notion API статус "In progress" (строчная p), не "In Progress"
- **get_opencode_attach()** ищет `lsof | grep "OpenCode.*LISTEN"` — находит Desktop app (порт 63816), но это internal IPC, не session API. `opencode run --attach` выдаёт "Session not found"
- **Без активной сессии:** задача маркируется как "dispatched" с пометкой "notification only"
- **Дубликаты в Notion DB:** есть (напр. "Allure/Playwright report" ×2). Созданы при импорте. Скрипт синхронизации отражает как есть

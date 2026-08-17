---
title: "Telegram Bot для OpenCode"
type: article
updated: "2026-08-17"
tags: [opencode]
---

# Telegram Bot для OpenCode

## Назначение

Telegram-бот, который принимает текстовые запросы и передаёт их в OpenCode (`opencode run`), а ответ отправляет обратно в Telegram. Позволяет работать с OpenCode с мобильного устройства без запуска TUI.

## Архитектура

```
Telegram → python-telegram-bot (бот) → subprocess: opencode run → stdout → Telegram
```

- Бот работает как фоновый процесс на MacBook.
- Каждый запрос — отдельный вызов `opencode run` (новая сессия, без истории).
- Ответ обрезается до 4000 символов (лимит Telegram).
- Таймаут выполнения: 180 секунд.

## Установка

**Зависимости:**
```bash
pip3 install python-telegram-bot
```

**Получение токена:**
1. Написать `@BotFather` в Telegram.
2. `/newbot` → указать название и юзернейм.
3. Сохранить токен: `export TG_BOT_TOKEN="123:ABCdef"` в `~/.zshrc`.

**Запуск:**
```bash
cd ~/bot && python3 bot.py
```

## Реализация

Основной файл: `~/bot/bot.py` (один файл, ~100 строк).

**Ключевые компоненты:**
- `Application.builder().token(BOT_TOKEN)` — инициализация бота.
- `MessageHandler(filters.TEXT)` — обработка любого текстового сообщения.
- `subprocess.run(["opencode", "run", text], timeout=180)` — вызов OpenCode.
- `ALLOWED_IDS` — белый список пользователей Telegram (безопасность).

**Команды:**
- `/start` — приветствие, модель и агент.
- `/model` — показать текущую модель.
- `/model <name>` — переключить модель.
- `/model reset` — сброс на дефолт.
- `/models` — список доступных моделей.
- `/agent` — показать текущего агента и список.
- `/agent <name>` — переключить агента.
- `/agent reset` — сброс на дефолт.
- `/stats` — статистика запросов.

## Модели

Бот поддерживает модели из двух провайдеров OpenCode — Zen (бесплатно) и Go (подписка).

**Разделение:**
- Модели Zen с пометкой FREE в названии — бесплатные, всегда доступны.
- Модели Go — оплачиваются из подписки ($5 первый месяц, $10/мес далее). Лимиты: $12 за 5 часов, $30 в неделю, $60 в месяц.

**Механизм выбора:**
- Пользователь указывает короткое имя модели (например, `deepseek-v4-flash`).
- Бот определяет провайдера по таблице: Zen FREE или Go.
- Подставляет правильный префикс: `opencode/` для Zen, `opencode-go/` для Go.
- `opencode run --model <полное-имя>` использует выбранную модель.

**Бесплатные модели (Zen):**
`deepseek-v4-flash-free`, `deepseek-v4-flash`, `gpt-5-nano`, `big-pickle`, `mimo-v2.5-free`, `nemotron-3-ultra-free`, `north-mini-code-free`, `qwen3.6-plus`

**Модели по подписке (Go):**
`deepseek-v4-pro`, `glm-5`, `glm-5.1`, `kimi-k2.5`, `kimi-k2.6`, `mimo-v2.5`, `mimo-v2.5-pro`, `minimax-m2.5`, `minimax-m2.7`, `minimax-m3`, `qwen3.7-plus`, `qwen3.7-max`

Модели Zen без "free" в названии (Claude, GPT, Gemini, DeepSeek Pro) платные — используются из баланса Zen. В бот не включены по умолчанию.

## Безопасность

- `ALLOWED_IDS = [<user_id>]` — только указанные пользователи могут отправлять запросы.
- Неавторизованный запрос получает отказ с инструкцией по добавлению.
- `--dangerously-skip-permissions` используется для неинтерактивного режима (без запроса подтверждения на каждое действие).
- API-токен хранится в переменной окружения `TG_BOT_TOKEN`.

## Ограничения

| Ограничение | Значение | Причина |
|-------------|----------|---------|
| Длина ответа | 4000 символов | Лимит Telegram |
| Таймаут | 180 секунд | subprocess timeout |
| Сессии | Отсутствуют | Каждый запрос — отдельный `opencode run` |
| Файлы | Не поддерживаются | Только текст |
| Контекст | Не сохраняется | Нет `--continue --fork` |
| Интернет | Требуется | Для Telegram API + OpenCode |
| Запуск | launchd | KeepAlive + RunAtLoad |

## Статус фич

| Фича | Статус | Что работает |
|------|--------|-------------|
| Модели (список/выбор/сброс) | ✅ | `/model`, `/models`, `--model <name>`, PER_USER_MODEL |
| Fallback модель | ✅ | `opencode/deepseek-v4-flash-free`, авто-retry при ошибке |
| Агенты (выбор/сброс) | ✅ | `/agent`, `--agent <name>`, PER_USER_AGENT. 4 предустановленных |
| Статистика | ✅ | `/stats`, stats.json, save_stats |
| Обход 4096 лимита | ✅ | split по 4000 chars; >12000 → файл |
| Загрузка файлов | ✅ | Document/Photo → `--file`, TEXT_EXTENSIONS, MAX_FILE_SIZE=10MB |
| Автозапуск (launchd) | ✅ | `com.user.tg-opencode` plist, KeepAlive+RunAtLoad |
| Безопасность | ✅ | ALLOWED_IDS, опасные команды через `--dangerously-skip-permissions` |
| Модели для разных чатов | 🔄 | PER_USER_MODEL глобальный, не per-chat |
| Агент .md файлы | 🔄 | Агенты в коде, но .md файлы не созданы |
| Кэш моделей | 🔄 | `refresh_models_cache()` пишет файл, но не читает его |
| Контекст файлов через stdin | 🔄 | Файлы передаются через `--file`, без inline content |
| HealthCheck тред | 🔄 | Нет кукушки (bot.py) |
| WatchPaths на bot.py | 🔄 | Нет авто-перезапуска при изменении кода |
| `/new` сессии + `--continue --fork` | 📋 | Не реализовано |
| tempfile.TemporaryDirectory | 📋 | Сейчас NamedTemporaryFile + ручной unlink |
| os_log / Console.app | 📋 | Вся логика описана, не реализована |
| install-launchagent.sh | 📋 | Скрипт не написан |

## План (📋)

**Сессионность (📋):**
- Команда `/new` — начало новой сессии.
- Каждое следующее сообщение — `opencode run --continue --fork`, которое продолжает предыдущую сессию.
- Сессия живёт, пока пользователь явно не завершит её.

**Поддержка файлов (🔄/📋):**

Download реализован ✅. Осталось:
- Текстовые файлы читать и передавать контекст через stdin: `<filename>:\n\`\`\`\n<content>\n\`\`\``
- `tempfile.TemporaryDirectory` context manager (сейчас NamedTemporaryFile + ручной unlink)
- Файлы без caption → "проанализируй этот файл"
- Если сессия `/new`, файл → `--continue --fork --file`

**Кэш моделей (🔄):**

`refresh_models_cache()` пишет в `~/.opencode_model_cache.json`, но файл никем не читается. Нужно:
- Загружать кэш при старте
- Использовать для автодополнения /model
- `/model reset` должен перечитывать

**Смена модели в реальном времени (🔄):**
- ✅ Сохранение выбранной модели между запусками (PER_USER_MODEL в памяти, но не в JSON)
- 🔄 Разные модели для разных чатов (сейчас глобальный словарь)

**Логирование и статистика (✅/📋):**
- ✅ Сколько запросов, какие модели, среднее время ответа
- 📋 Экспорт в CSV для анализа

**Мульти-агентность (🔄):**

- ✅ `/agent` команда, PER_USER_AGENT, `--agent <name>` в subprocess
- 🔄 Агенты — только имена в AGENTS dict, без `.md`-файлов
- 🔄 Список не грузится из `opencode agent list`
- 🔄 Нет персистентного состояния (`~/.opencode_agent_state.json`)

**Обход ограничений длины (✅):**

Реализовано. Два уровня:
1. split по 4000 chars
2. >12000 chars → файл через `reply_document`

**Автозапуск (✅/🔄):**

- ✅ plist с KeepAlive + RunAtLoad (файл `com.user.tg-opencode.plist`)
- 🔄 Нет WatchPaths, HealthCheck, os_log, скрипта установки

**Источник:** Реализация на базе OpenCode 1.14.41, python-telegram-bot 22.7, Python 3.12.

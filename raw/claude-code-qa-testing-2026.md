# Claude Code для QA-тестирования (2026)

Источник: исследование Victor Ematin, Jul 2026. Ссылки: utilo.io, testcollab.com, platform.claude.com, medium.com.

## Позиционирование

Claude Code (Anthropic) — главный конкурент специализированных QA-агентов в 2026. В отличие от Mabl/Testsigma (UI для QA), Anthropic идёт через CLI + агентную автоматизацию.

## 1. Claude Code (Автономный CLI-агент)

Работает в терминале и репозитории. С моделями Claude Opus 4.8 / Sonnet 5:

- **Генерация тестов по PR-диффам:** `claude "проанализируй изменения в этой ветке и напиши интеграционные тесты на Playwright"`
- **Автономный цикл отладки:** пишет тесты → запускает → перехватывает ошибки → исправляет → перезапускает до Green Build

## 2. Computer Use (Сквозное UI-тестирование)

Фундаментальное преимущество перед обычными LLM. Через Computer Use API:

- Доступ к виртуальному экрану / headless-браузеру
- Скриншоты, визуальный анализ, клики, ввод текста
- Тест-план на человеческом языке → Claude выполняет как живой человек → фиксирует баги → скриншоты для evidence

## 3. Экосистема Skills (SKILL.md)

Концепция Universal Skills. Готовые QA-навыки:

- **Browser Use / Playwright Migration** — перевод legacy Selenium → Playwright
- **API Contract Testing** — генерация тестов из OpenAPI/Swagger
- **Shannon** — встроенный агент для автономного пентеста

## 4. MCP (Model Context Protocol)

Подключение к TestCollab, Jira и другим системам. Автоматическое преобразование логов проверок в структурированные тест-кейсы и баг-репорты.

## Сравнение

| vs | Claude Code | Kiro | Mabl |
|----|-----------|------|------|
| Сила | "Инженер за клавиатурой" | Математическая верификация, PBT | No-code UI для QA |
| Computer Use | ✅ Нативный | ❌ | ❌ |
| Spec-driven | ❌ | ✅ EARS specs | ❌ |
| UI для QA | ❌ CLI-only | IDE | ✅ Dashboard |

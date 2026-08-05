# OpenCode + OpenRouter для QA-тестирования (2026)

Источник: исследование Victor Ematin, Jul 2026.

## Позиционирование

OpenCode — главный OSS-конкурент Claude Code. OpenRouter — прокси-хаб для LLM.
Связка: самый мощный, гибкий и экономичный стек для соло-разработчиков и QA.

Преимущество: **No vendor lock-in** — если Anthropic повысит цены, переключаешь модель одной командой.

## Финансы

| Статья | Стоимость |
|--------|----------|
| OpenCode | $0 (OSS) |
| OpenRouter комиссия | 5.5% (карта) / 5% (крипта) |
| Бесплатные модели | 25+ (Llama 3 базовые) |
| Реальные затраты (флагман) | $10–30/мес на сотни запусков |
| vs Mabl | от $499/мес |

## Установка

```bash
curl -fsSL https://opencode.ai/install | bash
opencode
/connect openrouter
```

## AGENTS.md — аналог SKILL.md для OpenCode

```markdown
# Agent Profile: Solo QA Automation Engineer

## LLM Configuration
- Primary Model: anthropic/claude-3.5-sonnet (via OpenRouter)
- Fallback Model: meta-llama/llama-3.1-405b-instruct (via OpenRouter)

## Context & Stack
- Project Type: Python API (FastAPI) & Frontend (Playwright Python)
- Test Framework: pytest
- Location: ./tests/

## Instructions
1. Analyze: Before writing code, scan ./tests/conftest.py for existing fixtures
2. Execute: Full permission to run pytest in terminal
3. Self-Heal: Если pytest failed → intercept stack trace → fix → rerun until green
4. Limits: Max 5 debugging loops without confirmation
```

## Практические команды

```bash
# Исследовательское тестирование
opencode "Изучи роуты FastAPI и напиши интеграционные тесты для всех эндпоинтов авторизации, которых нет в /tests"

# Автономный дебаг
opencode "Запусти pytest. Если упадет — проанализируй логи, исправь ошибку, добейся зеленого"

# Генерация тестовых данных
opencode "Создай json-фикстуры с граничными значениями для формы регистрации"
```

## Преимущества

1. **No vendor lock-in** — одна команда переключения модели
2. **Локальная безопасность** — код не уходит в облако, только промпты
3. **Offline режим** — Ollama для полностью локальной работы

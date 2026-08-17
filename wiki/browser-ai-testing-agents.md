---
title: "Browser-Based AI Testing Agents"
type: article
updated: "2026-08-17"
tags: [playwright, agents]
---

# Browser-Based AI Testing Agents

Browser-based AI agents — автономные AI-агенты, которые управляют браузером через код (Playwright, Puppeteer) для исследовательского тестирования, генерации тестов и валидации.

В отличие от традиционных E2E тестов (заранее написанные сценарии), browser agents **сами решают, что кликнуть, куда ввести текст, что проверить** — и записывают результат в виде скрипта.

---

## Webwright (Microsoft Research)

**Источник:** https://microsoft.github.io/Webwright/ | https://github.com/microsoft/Webwright  
**Статус:** research prototype (2026)

### Подход
Агенту даётся **терминал, локальный workspace и свобода писать код**, который запускает, инспектирует и уничтожает браузерные сессии. Результат — не выполненная задача, а **переиспользуемая программа**.

### Ключевые концепции
- **Disposable browsers** — агент спавнит браузер, делает скриншоты только когда нужно, rerun'ит скрипты, не застревая в одном stateful page
- **Code composes actions** — не цепочка кликов, а функции и циклы (date selection, form filling, filtering)
- **Artifacts survive** — скрипты, логи, скриншоты сохраняются в workspace
- **Premature done gate** — агент должен перезапустить финальный скрипт в чистой папке и пройти self-reflection
- **Reusable tools** — скрипты можно параметризовать, экспортировать как CLI, шарить между агентами

### Результаты
- 86.7% Online-Mind2Web (GPT-5.4)
- 60.8% Odysseys (long-horizon browsing)
- 66.2% Qwen3.5-9B с crafted tools

### Архитектура (3 модуля, ~1K строк)
1. **Runner** — отправляет контекст, команду и наблюдения модели
2. **Model Endpoint** — возвращает `thinking + bash command`
3. **Environment** — запускает команду, возвращает terminal output + logs + screenshots

### Цикл работы
```
workspace/run
├── final_script.py         # готовый скрипт
├── final_script_log.txt    # лог выполнения
├── screenshots/            # скриншоты ключевых точек
└── self_reflect_result.json # self-reflection
```

### Практическая ценность
- **Генерация тестов:** дать агенту URL → получить Playwright-скрипт → адаптировать под spec
- **Исследовательское тестирование:** агент сам обходит сайт, ищет баги
- **Reusable CLI tools:** скрипты можно сохранить как skills для Codex/OpenCode

### Ограничения
- Требует сильного LLM (GPT-5.4 или Qwen3.5-9B)
- Research prototype, не production-ready
- Не заменяет CI/CD E2E тесты, а дополняет exploratory testing

---

## Сравнение с другими подходами

| Аспект | Webwright | Mabl (Agentic Tester) | Классический E2E (Playwright) |
|--------|-----------|----------------------|-------------------------------|
| Тип | Open-source research | Проприетарный SaaS | Open-source framework |
| Управление | Терминал + код | UI + AI | Код |
| Тесты пишет | AI-агент | AI-агент + запись | Человек |
| Self-healing | Нет | Есть (локаторы) | Нет |
| Reusable | Как CLI/skills | Как test cases | Как spec-файлы |
| Для CI/CD | Нет | Да | Да |
| Для exploratory | Да | Частично | Нет |
| LLM зависимость | Критическая | Частичная | Нет |

---

## Применимость для Buzzhive

**Текущий подход:** 300+ Playwright тестов, CI/CD, PBT — закрывает регрессию и API.

**Webwright мог бы добавить:**
- Генерацию тестов для новых фич (агент изучает UI → пишет spec)
- Exploratory testing перед релизом (агент обходит site + API и ищет аномалии)
- Конвертацию исследовательских скриптов в постоянные тесты

**Но:** для внедрения нужен сильный LLM + стабильная версия инструмента. Пока — следить.

---

## Ссылки
- [Webwright GitHub](https://github.com/microsoft/Webwright)
- [Microsoft Research Blog](https://www.microsoft.com/en-us/research/articles/webwright-a-terminal-is-all-you-need-for-web-agents/)
- [[industrial-ai-testing-frameworks]] — Mabl и другие промышленные фреймворки
- [[agentic-patterns]] — паттерны проектирования AI-агентов

---

**Tags:** #ai-testing #browser-agents #webwright #research  
**Updated:** 2026-05-30  
**Related:** [[industrial-ai-testing-frameworks]] [[agentic-patterns]] [[ai-testing-map]]

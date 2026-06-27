# Десктопные AI-агенты для кода — обзор 2026

## Источники
- Ivern AI comparison (April 2026)
- ComputingForGeeks comparison (April 2026)
- 500k.io — 6-week real-world test (May 2026)
- TurboDocx — Cursor vs Claude Code vs OpenCode (May 2026)
- AI Builder Club — 3-way comparison (May 2026)
- NeuralStackly — 4 tools comparison (April 2026)
- LeadDev — enterprise perspective (March 2026)
- iBuidl Research — 4,000 engineer telemetry (March 2026)
- Pragmatic Engineer survey — 15,000 developers (Feb 2026)

---

## Классификация по типу

| Тип | Инструменты | Пример использования |
|-----|-------------|---------------------|
| **IDE (VS Code fork)** | Cursor, Windsurf, Google Antigravity | Повседневное редактирование, визуальные diff |
| **Terminal CLI** | Claude Code, OpenCode, Aider, agy (Antigravity CLI) | Глубокий рефакторинг, автономные задачи |
| **Desktop app** | Google Antigravity, Claude Desktop | Multi-agent оркестрация, фоновые задачи |
| **VS Code extension** | GitHub Copilot, Cline, RooCode | Бесшовная интеграция в существующий редактор |
| **Platform (IDE+CLI+SDK+API)** | Google Antigravity 2.0 | Единый agent harness на всех поверхностях |
| **Web-based** | Replit Agent, Bolt.new | Быстрый старт без установки |

---

## Tier 1 — Мейнстрим

### 1. Cursor (Anysphere)

| Характеристика | Значение |
|---------------|----------|
| Тип | IDE (VS Code fork) |
| Модели | Claude Sonnet 4.6, Opus 4.6, GPT-5.5, Gemini 3.1 Pro |
| Цена | Free (50 req/mo) → Pro $20/mo → Business $40/mo |
| Пользователи | 2M+, $1B ARR |
| GitHub | 80K+ stars |
| SWE-bench | Not published |

**Сильные стороны:**
- Самое быстрое Tab-дополнение в 2026 (<100ms)
- Composer mode — мульти-файловое редактирование
- План-затем-действие: объясняет изменения до применения
- Multi-model: переключение между Claude/GPT/Gemini
- Predictive indexing — предугадывает какие файлы понадобятся

**Слабые стороны:**
- Composer теряет связность на задачах >8-10 шагов
- Производительность падает на больших монорепозиториях
- $20/mo + API costs для Power Users (до $287/mo)
- Vendor lock-in (проприетарный)

**Лучше всего для:** Senior devs, сложные проекты, ежедневное редактирование

---

### 2. Claude Code (Anthropic)

| Характеристика | Значение |
|---------------|----------|
| Тип | Terminal CLI |
| Модели | Claude Opus 4.6 / Sonnet 4.6 / Haiku 4.5 (только) |
| Цена | Pro $20/mo → Max $100-200/mo (flat) |
| Пользователи | #1 по satisfaction (46% опрошенных), 84% satisfaction, 4% всех GitHub commits |
| Контекст | 200K-1M токенов |

**Сильные стороны:**
- SWE-bench 80.8% — #1 среди всех инструментов
- 1M context window — загружает весь кодbase
- Агентская автономия: 2-4 часа без присмотра
- Agent Teams: мульти-агентная оркестрация
- Flat-rate: $100/mo Max, никаких сюрпризов
- Deep git integration: авто-коммит, PR creation

**Слабые стороны:**
- Только Claude модели — никаких других провайдеров
- Терминал: нет GUI, нет визуальных diff
- Permission fatigue — 93% подтверждений избыточны
- Quality incidents: reasoning effort тихо понижали (Mar-Apr 2026)

**Лучше всего для:** Сложные рефакторинги, архитектурная работа, full-stack фичи

---

### 3. Google Antigravity (Google)

| Характеристика | Значение |
|---------------|----------|
| Тип | **Platform** — Desktop app + CLI (`agy`) + SDK + Managed Agents API |
| Модели | Gemini 3.5 Flash (основная, co-optimized), Claude Sonnet 4.5, GPT-OSS |
| Цена | Free → AI Pro $20/mo → AI Ultra $100/mo → $200/mo |
| Пользователи | "Millions of developers" (Alphabet, June 2026) |
| Дата запуска | 1.0: ноябрь 2025; 2.0: май 2026 (Google I/O) |
| GitHub | SDK: ~1.5K stars |

**Сильные стороны:**
- **Browser Sub-agent** — встроенный Chromium: агент сам кликает, заполняет формы, делает скриншоты — уникальная фича среди всех инструментов
- **Multi-agent DAG** — разбивает задачу на подзадачи, назначает специализированным саб-агентам, параллельное исполнение
- **Артефакты** — планы, скриншоты, записи браузера как верифицируемые результаты
- **Managed Agents API** — один HTTP-запрос → изолированный Linux sandbox с агентом
- **1M token context** (заявлено), эффективно ~200-400K
- Фоновые задачи по расписанию (cron-style)
- SDK для кастомных агентов на своей инфраструктуре
- Интеграция с Firebase, Android Studio, AI Studio

**Слабые стороны:**
- **Quota crisis** — 4 сокращения лимитов за 4 месяца (Dec 2025 — Mar 2026), Pro $20 подписчики были заロックаны на дни
- VS Code Marketplace не поддерживается (только Open VSX) — нет C# Dev Kit, GitHub sign-in и др.
- Нет JetBrains — только VS Code fork
- Permission model: 3-tier, частые прерывания (Tier 3 — per-command approval)
- Claude Opus 4.6 через BYOK: $5-15/час дополнительно
- Нет MCP (на roadmap)
- Agentic архитектура жрёт токены: 180-240K токенов на один Rails scaffold
- Бесплатный tier: всего 50K токенов/день

**Лучше всего для:** Senior devs, multi-file рефакторинги, визуальная верификация, Google Cloud экосистема

### 4. OpenCode (Anomaly Innovations)

| Характеристика | Значение |
|---------------|----------|
| Тип | Terminal TUI (Go/Bubble Tea) + Desktop app + VS Code extension |
| Модели | BYOK — 75+ провайдеров (OpenAI, Anthropic, Google, Groq, AWS, Azure, Ollama, local) |
| Цена | MIT license, $0 (только API costs) |
| GitHub | 150K+ stars (#1 open source AI coding agent) |
| Язык | Go (TUI) + JavaScript/Bun (HTTP server) |

**Сильные стороны:**
- Полностью open source (MIT) — нет vendor lock-in
- BYOK: любые модели, включая локальные через Ollama ($0)
- LSP integration — нативная поддержка Language Server Protocol
- MCP support — Model Context Protocol
- Multi-agent: 10 агентов (с OmO расширением)
- Privacy: код и контекст не покидают машину

**Слабые стороны:**
- RAM: 1GB+ для TUI приложения
- Stability: фризы, CPU spikes, hanging sessions
- Privacy incident: silent data exfiltration для title generation (даже с local-only моделями)
- Качество зависит от модели: frontier → отлично, local → inconsistently
- Контекст: 70-120K токенов на практике (меньше чем Claude Code)

**Лучше всего для:** Power users, multi-model workflows, бюджетные разработчики, приватность

---

### 5. GitHub Copilot (Microsoft)

| Характеристика | Значение |
|---------------|----------|
| Тип | VS Code extension (также JetBrains, Neovim) |
| Модели | GPT-4o / Codex (только) |
| Цена | Free (2000 компл/mo) → Individual $10/mo → Business $19/mo → Enterprise $39/mo |
| Пользователи | 26M+ (самая большая база) |

**Сильные стороны:**
- Самая большая установленная база
- Интеграция с GitHub: PR summaries, code reviews, Issues
- Copilot Workspace: plan-then-code для фич
- Multi-IDE: VS Code, JetBrains, Neovim
- Enterprise: SSO, audit logs, compliance

**Слабые стороны:**
- Tab completion отстаёт от Cursor и Windsurf по качеству
- Agent mode слабее чем Cascade или Claude Code
- Только одна модель (GPT/Codex)
- Контекст: только открытые файлы

**Лучше всего для:** Enterprise команды, GitHub-native проекты, начинающие

---

### 6. Windsurf (Codeium → OpenAI)

| Характеристика | Значение |
|---------------|----------|
| Тип | IDE (VS Code fork) |
| Модели | Claude, GPT, SWE-1.5 (custom) |
| Цена | Free (щедрый) → Pro $15/mo → Ultimate $60/mo |
| Примечание | Приобретён OpenAI (Cognition deal, early 2026) |

**Сильные стороны:**
- Cascade: лучший agentic workflow среди IDE
- SWE-1.5 custom model: Sonnet-level при 13x скорости
- Context engine: RAG для больших codebase
- Лучший free tier: unlimited completions
- Resource efficiency: меньше CPU/RAM чем Cursor

**Слабые стороны:**
- Отстаёт от Cursor по Tab completion
- Меньше community и экосистема
- Flow credit accounting путает пользователей
- Меньше model selection чем Cursor

**Лучше всего для:** Flow state, бюджет, большие рефакторинги

---

## Tier 2 — Нишевые / Специализированные

### 6. Augment Code

| Характеристика | Значение |
|---------------|----------|
| Тип | VS Code / JetBrains extension |
| Цена | Pro $30/mo → Max $200/mo |
| Уникальность | Semantic graph — связи типов, call chains, data flow |

- Лучшее понимание codebase среди всех (91% accuracy на tab completion)
- Self-hosted, SOC 2 Type II, enterprise compliance
- **Нет agent mode** — suggestion tool, не execution tool
- Цена $200/mo для Max — дорого для индивидов

### 7. Sourcegraph Cody

| Характеристика | Значение |
|---------------|----------|
| Тип | VS Code / JetBrains extension |
| Цена | Pro $9/mo |
| Уникальность | Sourcegraph-powered codebase search |

- Лучший для поиска по огромным монорепозиториям
- Дешёвый entry point ($9/mo)
- Слабее Cursor/Windsurf на multi-file задачах

### 8. Aider

| Характеристика | Значение |
|---------------|----------|
| Тип | Terminal CLI |
| Цена | Open source, бесплатно |
| Уникальность | Map of repo — контекстная карта проекта |

- Популярен в open source сообществе
- Поддерживает Claude, GPT, local модели
- Нет GUI, терминал-only

### 9. Cline

| Характеристика | Значение |
|---------------|----------|
| Тип | VS Code extension |
| Цена | Open source + API costs |
| Уникальность | BYOK agent внутри VS Code |

- Гибкость: сам выбираешь модель и контекст
- Меньше polish чем Cursor, но больше контроля
- Популярен в Reddit сообществе

### 10. Devin (Cognition → OpenAI)

| Характеристика | Значение |
|---------------|----------|
| Тип | Web-based автономный agent |
| Цена | $500/mo |
| Уникальность | Полностью автономный: берёт задачу и делает |

- Самый дорогой ($500/mo)
- Спорная ценность: benchmark показывает результат не лучше Claude Code
- Приобретён OpenAI в начале 2026

### 11. JetBrains Junie

| Характеристика | Значение |
|---------------|----------|
| Тип | JetBrains IDE plugin |
| Цена | ? |
| Уникальность | AI внутри IntelliJ, PyCharm, WebStorm |

- Для тех кто не хочет уходить из JetBrains
- Меньше фич чем Cursor, но нативная интеграция

### 12. Gemini CLI (Google)

| Характеристика | Значение |
|---------------|----------|
| Тип | Terminal CLI |
| Цена | Free tier + API costs |
| Уникальность | Gemini 2.5 Pro model |

- Бесплатный tier
- Gemini 2.5 Pro — сильная модель для кода
- Меньше фич чем Claude Code или OpenCode

---

## Tier 3 — Экспериментальные / Emerging

| Инструмент | Разработчик | Статус |
|-----------|-------------|--------|
| AWS Kiro | Amazon | Ранний доступ |
| Kilo Code | ? | Emerging |
| Zencoder | ? | Ранний |
| RooCode | Community | VS Code agent |

---

## Antigravity — наш опыт

Antigravity — это **Google Antigravity**, агентская IDE/платформа от Google. У нас был бесплатный preview-доступ 24-25 мая 2026 на новом macOS профиле.

**Что удалось сделать за 2 дня:**
- Prompt: "напиши всевозможные тесты логина под админом"
- Создан `login_test.go` (188 строк, 5 функций, 10 тестов) — миграция TypeScript auth.spec.ts → Go
- Найден race-баг (отдельно от известного refresh token race от 20 мая)
- Доступ потерян из-за VPN

**Сравнение с OpenCode (асимметричное):**

| Параметр | Antigravity | OpenCode |
|----------|-------------|----------|
| Задач | 1 | 40+ сессий |
| Модель | Gemini 3.5 Flash (предп.) | gpt-4o-mini |
| Prompt | "напиши всевозможные тесты" | Детальные пошаговые |
| Результат | 1 файл, 188 строк | 15 Go файлов, race_test.go |
| Баги | Нашёл race (24-25 мая) | Нашёл другой race (29 мая) |

**Вывод:** Antigravity показал хороший результат на 1 задаче, но для полного сравнения нужен стабильный доступ. Race-баги найдены независимо — разные инструменты находят разные проблемы.

---

## Позиционирование по задачам

| Задача | Лучший инструмент |
|--------|------------------|
| Ежедневное редактирование | Cursor (Tab completion) |
| Глубокий рефакторинг (40+ файлов) | Claude Code (1M context) |
| Multi-model эксперименты | OpenCode (75+ providers) |
| Enterprise compliance | GitHub Copilot |
| Flow state / бюджет | Windsurf ($15/mo) |
| Локальные модели / приватность | OpenCode + Ollama |
| Автономный agent (часы) | Claude Code (Agent Teams) |
| Multi-file рефакторинг + верификация | Antigravity (Browser Sub-agent) |
| Параллельные задачи | Antigravity (Multi-agent DAG) |

---

## Комбинации (как реально используют)

По данным исследований и форумов, большинство опытных разработчиков используют 2-3 инструмента:

### Stack: Cursor + Claude Code
- Cursor: ежедневное редактирование, Tab completion
- Claude Code: сложные рефакторинги, архитектура
- Цена: $20 + $100-200 = $120-220/mo

### Stack: Cursor + OpenCode
- Cursor: IDE editing
- OpenCode: multi-model эксперименты, локальные модели
- Цена: $20 + API costs = ~$30-70/mo

### Stack: Windsurf + Claude Code (бюджетный)
- Windsurf: IDE editing ($15/mo)
- Claude Code: только для сложных задач ($20/mo Pro)
- Цена: $35/mo

### Stack: Antigravity + Cursor (параллельный)
- Antigravity: multi-agent, Browser Sub-agent, параллельные задачи
- Cursor: точное редактирование, MCP, rules
- Цена: $20 + $20 = $40/mo

---

## OpenCode в сравнении (наши данные)

| Параметр | OpenCode Go ($10 flat) | OpenCode Free |
|----------|----------------------|---------------|
| Модель | gpt-4o-mini | gpt-4o-mini |
| Rate limit | ~1000 tool calls/час | ~100 tool calls/час (блок) |
| Контекст | 128K | 128K |
| Стоимость | $10 flat/mo | $0 |
| Сессий | 40+ | — |

**Вывод:** Go ($10) решил проблему rate limit, но модель (gpt-4o-mini) слабее чем Claude Opus 4.6 или Sonnet 4.6. Для сложных задач OpenCode Go стоит комбинировать с API Claude через BYOK.

---

## Источники

- Ivern AI: "AI Coding Agents Compared 2026"
- ComputingForGeeks: "OpenCode vs Claude Code vs Cursor 2026"
- 500k.io: "Claude Code vs Cursor vs Windsurf — 6-week test"
- TurboDocx: "Cursor vs Claude Code vs OpenCode 2026"
- AI Builder Club: "Claude Code vs Cursor vs Windsurf 2026"
- NeuralStackly: "Best AI Coding Assistants 2026"
- LeadDev: "Best AI-coding tools in 2026"
- iBuidl Research: "Developer Tools 2026 — 4,000 engineers"
- Pragmatic Engineer survey: 15,000 developers (Feb 2026)
- NivaaLabs: "Best AI Coding Tools 2026 — Every Major Tool Ranked"

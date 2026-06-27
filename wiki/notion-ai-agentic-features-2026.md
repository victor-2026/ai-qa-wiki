# Notion AI Agentic Features 2026

**Обзор:** Notion AI — встроенная AI-платформа внутри Notion с тремя уровнями агентов, External Agents API, hosted code runtime (Workers) и MCP-интеграцией.

**Источники:** notion.com/product/ai, notion.com/product/agents, notion.com/releases (Feb/May 2026), TechCrunch (May 13, 2026)

---

## Архитектура агентов

### 1. Notion Agent (личный)
- On-demand: чат → AI выполняет multi-step задачи
- Читает/пишет страницы, базы данных, properties, views
- Подключен к Slack, Gmail, Calendar через AI Connectors
- Plan Mode: показывает план до выполнения (approval)
- Skills: сохраняемые промпты для повторяющихся задач
- Доступен на всех планах с Notion AI

### 2. Custom Agents (командные)
**Запуск:** февраль 2026 (v3.3), 1M+ built by May 2026
- **Автономные:** работают 24/7 по триггерам/расписанию, без ручного промптинга
- **Триггеры:** расписание (cron), события в Notion (status changed), Slack-сообщения/emoji
- **Источники:** Notion pages + databases, Slack (public + private channels), Notion Mail, Calendar
- **Действия:** CRUD над БД, генерация страниц, Slack read/write, conditional branching
- **Plan Mode:** предпросмотр перед выполнением
- **Модели:** Claude, GPT, Gemini (выбор per agent или Auto)
- **Permissions:** per-agent, granular (read/write scope, как настоящий тиммейт)
- **Цена:** Notion credits — $10/1000 credits. Free through May 3, затем credits

**Типовые сценарии:**
- Q&A Agent — отвечает на вопросы команды из Notion + Slack
- Task Routing Agent — ловит запросы, создаёт задачи, назначает owner
- Status Update Agent — собирает статусы и постит в Slack по расписанию
- Autofill — автоматическое обогащение БД (извлекает, категоризирует, обновляет)

### 3. External Agents API (v3.5, май 2026)
- Notion стал **оркестратором внешних агентов**: Claude Code, Cursor, Codex, Decagon
- Чат с внешним агентом внутри Notion, назначение задач, трекинг прогресса
- External Agent API для кастомных агентов
- **Стратегический смысл:** Notion = нейтральный слой, где любые агенты работают как native teammates

### 4. Workers (v3.5, май 2026)
- Hosted code runtime (JS/TS) для кастомной логики
- Notion CLI: `curl -fsSL https://ntn.dev | bash`
- **Use cases:** Database Sync (Salesforce, Zendesk, Postgres), webhook triggers, агент-тулы с детерминированной логикой
- Бесплатно в beta, с Aug 11 2026 — credits

### 5. MCP интеграция
- Custom Agents подключаются к Linear, Figma, HubSpot, n8n
- MCP-сервера для Notion (external AI читает/пишет Notion)

---

## Внедрение Notion AI в тестирование ПО

### 1. Автоматическая обработка и трекинг багов (Custom Agents)

Custom-агенты под конкретные роли QA-команды:

- **Реализация:** Агент мониторит каналы обратной связи (Slack, клиентские формы). Автоматически анализирует сообщения, распознаёт баги, регистрирует в БД Notion (*Bug Tracker*), заполняет критичность, назначает ответственного QA-инженера, переводит статус в «Назначено».

### 2. Интеллектуальные базы данных для QA (Notion AI for Databases)

Развёртывание структуры проекта через текстовый промпт:

- **Build with AI:** *«Создай базу данных для трекинга багов с полями: ID, Описание дефекта, Шаги для воспроизведения, Ожидаемый/Фактический результат, Окружение (ОС/Браузер), Приоритет и Статус»*
- **AI Properties:** автозаполняемые ИИ-поля — генерация саммари для логов ошибок, автоподстановка тест-кейсов на основе описания бага

### 3. Сквозной поиск информации (Enterprise Search & AI Connectors)

Данные тестирования обычно разбросаны: Jira, GitHub, Slack, Google Drive.

- **Реализация:** Подключить Notion AI Connectors. Запросы вида: *«Какие дефекты авторизации обсуждались в Slack на этой неделе?»* или *«Каковы требования к новому API в Google Docs?»* — AI сканирует внешние приложения и выдаёт ответ со ссылками на источники.

### 4. Генерация тестовой документации (Notion Agent / Writing Tools)

- **Тест-кейсы и чек-листы:** *«На основе этого технического задания напиши негативные и позитивные тест-кейсы для формы оплаты»*
- **Тестовые данные:** *«Сгенерируй массив тестовых данных из 15 пользователей в JSON с невалидными Email и граничными значениями возраста»*
- **Отчёты о тестировании:** Выделить БД с багами → *«Сформируй отчёт для стейкхолдеров с главными уязвимостями и статусом релиза»*

### 5. Транскрипция встреч (AI Meeting Notes)

- Транскрипция аудио на 16 языках
- Автоматическое выделение багов из разговора
- Формирование Action Items для разработчиков и QA

---

## Сравнение Trial for Work vs Home Use

| Критерий | Trial for Work (Бизнес-триал) | Trial for Home Use |
|---|---|---|
| **Доступ к Notion AI** | Полный: AI Agents, Enterprise Search, Custom Agents | Ограничен: базовые AI-функции по лимитированным кредитам |
| **AI Connectors** | Jira, GitHub, Slack, Google Drive | Только Notion Mail/Calendar |
| **Совместная работа** | До 100 человек, расширенные гостевые доступы | Один пользователь, строгие лимиты |
| **Безопасность** | Управление доступом, администрирование, логирование | Базовые настройки без панели администратора |

**Вывод:** Для полноценного внедрения ИИ в QA-процессы (Jira, Slack, GitHub, автоматизация тест-менеджмента) необходима версия **Trial for Work**. Home Use — только для базового написания текстов и простых чек-листов.

---

## Ключевые возможности для QA/AI-инженера

| Возможность | Описание |
|---|---|
| AI Search across tools | Slack + Google Drive + Notion — единый поиск |
| Meeting Notes AI | Транскрипция + саммари + экшн-айтенмы |
| AI Autofill | Автообогащение БД (результаты тестов, метрики) |
| Slack Q&A Agent | Custom Agent отвечает на вопросы команды из Notion KB |
| Plan Mode | Агент показывает план → human approval |
| Webhooks two-way | Notion → external app и external → Notion |
| Database Sync | Любая API-based БД → Notion (через Workers) |

---

## Сравнение с Obsidian (текущий стек)

| Критерий | Obsidian | Notion AI |
|---|---|---|
| **Хранение** | Локальные .md, git-версионирование | Cloud, databases (не .md) |
| **AI-агенты** | OpenCode/Claude Code читают файлы напрямую | Custom Agents + External Agents API |
| **Коллаборация** | Нет (одна сессия) | До 100 человек, permissions |
| **Программируемость** | Файловая система (простота) | Workers + CLI + MCP (мощь) |
| **Тест-репортинг** | Руками в .md | Custom Agent генерирует и постит в Slack |
| **Knowledge base** | Wiki из .md (AI читает напрямую) | БД + AI search + Q&A Agent |
| **Offline** | Да (локально) | Нет (cloud-only) |
| **Цена** | Бесплатно | Business $15/user/mo + credits |
| **Vendor lock-in** | Нет (.md open format) | Высокий (проприетарный формат) |

**Вывод:** Notion НЕ замена Obsidian для локального wiki-workflow (AI agents → .md files). Notion — дополнение для коллаборации, автоматизации и оркестрации агентов.

---

## План апробации (3 месяца)

**Контекст:** Free 3 Month Trial for Work от Christina Muehller (GTM AI Solutions Engineering Lead @ Notion, LinkedIn outbound, Jun 2026). Начать после одобрения оффера.

### Week 1: Setup + Notion Agent
- [ ] Создать workspace, принять trial
- [ ] Импортировать wiki (ai-qa-wiki экспорт .md → Notion)
- [ ] Настроить AI Connectors (Slack, Gmail)
- [ ] Протестировать Notion Agent: поиск, генерация страниц, Plan Mode

### Week 2: Custom Agent — тест-репортинг
- [ ] Создать БД "Test Runs" (status, count pass/fail, date, module)
- [ ] Custom Agent: собирает статусы и постит в Slack daily standup
- [ ] Custom Agent: Q&A по wiki (agent отвечает команде в Slack из Notion KB)

### Week 3: External Agents API
- [ ] Подключить Claude Code / OpenCode через External Agents API
- [ ] Тест: дать задачу через Notion → Claude Code пишет тест
- [ ] Оценить: удобнее ли чем прямой CLI/OpenCode workflow

### Week 4-8: Workers + Data Sync
- [ ] Workers: парсинг Allure/Playwright report → Notion DB
- [ ] Workers: webhook из GitHub Actions → Notion (результаты CI)
- [ ] Database Sync: Postgres (если доступен) → Notion

### Week 9-12: Оценка
- [ ] Сравнить скорость работы в Obsidian vs Notion AI
- [ ] Оценить vendor lock-in риск
- [ ] Решение: гибрид (Obsidian для черновиков + Notion для команды) или Notion только

### Критерии успеха
- Custom Agent реально экономит время (не просто игрушка)
- External Agents API стабилен для продакшн-задач
- Workers покрывают кастомную логику без external infra

---

## Будущие обзоры (серия)

Статья рассчитана на дополнение. Написано — обзор платформы, архитектура агентов, внедрение в QA/QC, сравнение версий, план апробации. Планируемые аддендумы:
- **Part 2:** Практический опыт — первые 2 недели апробации
- **Part 3:** Custom Agents deep-dive — триггеры, permissions, модели
- **Part 4:** Workers — код, деплой, интеграция с CI/CD
- **Part 5:** External Agents API — Claude Code из Notion

---

**Запись создана:** 2026-06-10
**Основание:** LinkedIn outbound от Christina Muehller, Notion (2:00 AM, Jun 10)

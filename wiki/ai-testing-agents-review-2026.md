# 2026: Обзор и апробация ИИ-агентов для тестирования

## Введение

2026 год стал переломным для AI-native тестирования. Инструменты перестали быть "помощниками для записи тестов" — они стали агентами, которые анализируют код, генерируют тесты, находят баги и даже чинят себя.

Мы протестировали 10+ подходов на реальных проектах: OrangeHRM (PHP), Buzzhive (React/Node.js), Virto Commerce (.NET), FrontRow (React Native). Ниже — сводка что работает, что нет, и где правда.

---

## 1. Autonoma — codebase-aware agent pipeline

**Тестировали:** OrangeHRM (Session 45-48)
**Затраты:** $4.99 (deepseek-v3.2 + gpt-4o)
**Результат:** 4/6 pipeline steps выполнены

Autonoma строит pipeline: pagesFinder → KB → entityAudit → testGenerator. Мы запустили его на OrangeHRM и сравнили с ручным подходом KISS.

**Что хорошо:**
- PagesFinder (шаг 1) и Knowledge Base (шаг 2) работают стабильно на 131K контексте
- Автоматически строит карту приложения (страницы → действия → данные)
- entityAudit (шаг 3) находит 59 entities, если исключить POM-файлы

**Что плохо:**
- entityAudit переполняет контекст (274K токенов с POM-файлами)
- scenarioRecipe (шаг 4) падает с timeout на 191K — либо перегрузка, либо лимит провайдера
- **Auto-switch моделей** без спроса: deepseek → kimi → v4-pro → gpt-5.4-nano. Счёт $3.62 вместо $0.50
- testGenerator не достигнут — pipeline умирает на 4/6

**Вердикт:** Работает на малых проектах (<50 страниц). На реальном коде (с POM) упирается в контекст. KISS даёт те же тесты за $0.19 и без риска auto-switch.

→ [Статья: Autonoma vs KISS comparison](/Users/victor/Projects/Articles/linkedin-posts/AI-Agents/4-autonoma-kiss-comparison.md)

---

## 2. Kiro — AI security deep-dive агент

**Тестировали:** OrangeHRM + Virto Commerce (Session 79)
**Затраты:** ~3 credits (~$0.06) за запуск
**Скорость:** ~2 минуты на анализ

Kiro — это agent для security-аудита кода. Он не пишет тесты, а находит уязвимости.

**На OrangeHRM (PHP):**
- Нашёл 36 security-файлов без единого теста
- Auth, OAuth, permissions, SSO, certificates — все critical зоны

**На Virto Commerce (.NET):**
- vc-module-catalog: 14/16 controllers zero tests (87.5%)
- 400 source vs 48 test files (8.3:1)
- 5 test files с 0 test methods (файлы есть, тестов нет)

**Что хорошо:**
- Мгновенный результат (2 мин на репозиторий)
- Zero false positives по security-зонам
- Бесплатно (free tier)

**Что плохо:**
- Не генератор тестов (только аудит)
- Не понимает бизнес-логику —只看 technical coverage

→ [Статья: Kiro Coverage Gap Analysis](/Users/victor/Projects/Articles/linkedin-posts/performance-log.csv) (Jul 17, 2026)

---

## 3. Devin — autonomous SWE agent

**Тестировали:** OrangeHRM + Virto Commerce (Session 75, 76b, 79)
**Затраты:** Cognition AI ($250M valuation)
**Результат:** Бэкдор-доступ к репозиторию → самостоятельная работа

Devin — первый "software engineer agent". Мы дали ему доступ к OrangeHRM и Virto Commerce.

**Что хорошо:**
- Самостоятельно клонирует репо, анализирует, пишет код
- На Virto Commerce нашёл 89/109 endpoints untested (81.65%)
- 82 `[Authorize]` endpoints — 0 тестируют 401/403
- Смоделировал breaking change: удаление limited_permissions — CI бы не поймал, 110 эндпоинтов silent full access
- 4 модуля с нулевым покрытием (127 файлов: 3 SQL провайдера + DistributedLock)

**Что плохо:**
- Не работает с DOM — не видит UI-элементы (Aider тоже)
- На Maintenance POM (OrangeHRM) сгенерировал меньше методов чем Aider (4 vs 10)
- Нужен полный доступ к репозиторию (security risk)
- $250M компания — как их pricing будет выглядеть через год?

**Сравнение с Aider (Session 76b):**
- Aider: 1 тест, 10 методов в POM, auto-fix loop через `--test-cmd`
- Devin: 7 тестов, 4 метода, но без feedback loop
- Оба слепые на селекторы — угадывают из Playwright error output
- Aider надёжнее за счёт `--test-cmd` auto-fix

→ [Статья: 3 AI Tools on Same OrangeHRM App](/Users/victor/Projects/Articles/linkedin-posts/performance-log.csv) (Jul 6, 2026 — 82,520 imp, рекорд)

---

## 4. Playwright Test Agents — Planner + Generator + Healer

**Тестировали:** OrangeHRM (Session 47, 54, 58)
**Статус:** Встроено в Playwright (npx playwright init-agents)

Три агента:
- **Planner:** исследует приложение → пишет .md план
- **Generator:** .md план → .ts тесты
- **Healer:** запускает + чинит локаторы/wait/data

**Что хорошо:**
- Healer реально чинит: в Session 47 починил 2 stale snapshot + 1 test improvement
- Pipeline совпадает с MAS (exploration → generation → validation)
- Встроено в Playwright — не нужно ставить отдельно

**Что плохо:**
- 3 data-level бага Healer не смог починить (подтверждает thesis статьи)
- Нет learned_patterns.json (MAS) — не накапливает опыт
- Не работает с data seeding (в отличие от Autonoma)

→ [Статья 6: Playwright Test Agents](/Users/victor/Projects/Articles/linkedin-posts/AI-Agents/6-playwright-test-agents.md)

---

## 5. Aider — AI pair programming с feedback loop

**Тестировали:** OrangeHRM (Session 76b)
**Модель:** Nemotron
**Результат:** 2/2 PASS на первом `--test-cmd` запуске

**Что хорошо:**
- `--test-cmd` auto-fix loop — ключевое преимущество над Devin
- Пишет глубокие POM (10 методов на Maintenance)
- Работает через CLI, легко интегрируется

**Что плохо:**
- 1 тест вместо 7 (против Devin) — coverage ниже
- Слепой на селекторы (как и Devin) — не видит DOM
- Нужен работающий проект локально для `--test-cmd`

---

## 6. Claude Code — CI/CD + MCP agent

**Тестировали:** Virto Commerce (Oleg, CTO, использует ежедневно)
**Статус:** Работает в production у CTO

Claude Code — не генератор тестов, а SWE-агент с CI/CD-интеграцией.

**Что хорошо:**
- Работает с MCP (Slack, Jira интеграция)
- Closed-loop assignee: сам чинит то, что сломал
- Oleg (CTO Virto) использует для тестов — реальный production use case
- Бесплатный в OpenCode Go

→ [Wiki: Claude Code CI/CD MCP](/Users/victor/Projects/ai-qa-wiki/wiki/claude-code-ci-cd-mcp-2026.md)

---

## 7. MAS (Model-AI-Schema) — наш паттерн

**Тестировали:** Buzzhive (10 паттернов)
**Статус:** Перерос в learned_patterns.json

MAS — не инструмент, а архитектурный паттерн: Exploration → Generation → Human Review → Learned Patterns.

**10 confirmed patterns:**
1. fixture_data_prep
2. post_before_get
3. explicit_credentials
4. type_assertions
5. teardown_cleanup
6. modular_api_client
7. retry_on_flaky
8. llm_filter_approach (Prune4Web)
9. human_review_loop
10. playwright_mcp (experimental)

→ [Wiki: MAS Architecture](/Users/victor/Projects/ai-qa-wiki/wiki/)

---

## 7b. Kane AI (TestMu AI / бывший LambdaTest)

**Тип:** GenAI-native end-to-end testing agent
**Цена:** $199/mo Web, $299/mo Web+Mobile, 30-day free trial
**CLI:** `npm install -g @testmuai/kane-cli` или `brew install LambdaTest/kane/kane-cli`
**Источник:** [BotGauge article](https://www.linkedin.com/pulse/10-best-ai-test-automation-tools-2026-botgauge-pdd0c/) + [TestMu docs](https://www.testmuai.com/support/docs/kane-ai-free-trial-is-here/)

**Ключевые особенности:**
- **Natural Language → Tests** — описываешь тесты на английском, KaneAI генерирует исполняемые сценарии
- **2-way editing** — двунаправленное редактирование: код ↔ natural language (меняешь код → NL обновляется, и наоборот)
- **Multi-format input** — Jira, PDF, изображения, аудио, видео, таблицы → тест-кейсы
- **kane-cli** — CLI для CI/CD: пишется objective на NL, возвращается NDJSON результат. Позиционируется как validation layer для AI coding agents (Cursor, Claude Code, Copilot)
- **Multi-language export** — Selenium-Python, Appium-Python и другие фреймворки
- **Auto-healing** — детектит изменения UI, self-correct по intent (не селектору)

**Ограничения free trial:**
- 10 sessions max, 40 instructions/session, 10 min/session
- 2 параллельных execution
- Selenium-Python (web), Appium-Python (mobile) — только Python
- 2 min idle timeout

**Чем интересен:**
- Единственный инструмент в обзоре с 2-way NL↔code editing
- kane-cli — potential competitor to Kiro для CI/CD validation (но Kiro focused на security, Kane — на end-to-end flows)
- Прямой конкурент testRigor / Virtuoso QA в сегменте NL-based testing, но с более широким форматом input

**Не тестировали:** нет аккаунта.

---

## 8. Сводная таблица

| Инструмент | Тип | Цена | Наш опыт |
|-----------|-----|------|----------|
| Autonoma | Pipeline agent | $0.50-5/run | 4/6 steps, context overflow на шаге 3 |
| Kiro | Security audit | Free tier | 36 security файлов за 2 мин |
| Devin | SWE agent | $250M backed | 81.6% untested, breaking blind spot |
| Playwright Agents | Built-in agents | Free | Healer чинит stale, не чинит data |
| Aider | Pair programming | Free (OSS) | 2/2 PASS, глубже Devin |
| Claude Code | MCP agent | Free (Go) | Production у CTO |
| **Kane AI** | **GenAI testing agent** | **$199/mo (web), 30d trial** | **NL→tests, 2-way edit, kane-cli для CI/CD** |
| KISS | Manual workflow | $0.19 | Быстрее Autonoma, понятнее |
| Maestro | Mobile agent | Free (OSS) | 35 flows, 0 flaky на FrontRow |
| Sorcar | Test generation | Free (OSS) | Устарел, автономность низкая |
| MAS | Architecture | N/A | 10 patterns в learned_patterns.json |

---

## 9. Наш pipeline (что используем сейчас)

В production на qa-automation-sandbox и OrangeHRM:

1. **Kiro** — nightly security audit (CI)
2. **Planner** — exploration новых модулей
3. **Generator** — тесты из .md планов
4. **Healer** — auto-fix flaky тестов
5. **MAS learned_patterns** — повторное использование

Не используем: Autonoma (context overflow), Devin (blind на селекторы), Sorcar (устарел).

---

## 10. Все наши статьи по теме

| # | Статья | Дата | Импрессии |
|---|--------|------|-----------|
| 4 | Autonoma vs KISS — два подхода к AI-тестированию | Jun 10 | ~500 |
| 5 | MAS — Model-AI-Schema паттерн | Jun 12 | ~300 |
| 6 | Playwright Test Agents — Planner/Generator/Healer | Jun 16 | 1,523 |
| 7 | 3 AI Tools on Same OrangeHRM App | Jul 6 | **82,520** 🏆 |
| 8 | Skills Are Not npm Packages | Jun 18 | 479 |
| 9 | AI Fluency Interview Reform | Jun 26 | 733 |
| 10 | Kiro Coverage Gap Analysis | Jul 17 | 867 |
| 11 | ML Testing in Go | Jul 9 | 2,125 |
| — | VLM vs Blind AI Agents | Jul 14 | 1,852 |
| — | Maestro vs Appium: FrontRow | Jul 1 | 73 |
| — | Detox vs Appium for RN | Jul 2 | 1,362 |

---

*Обзор составлен по результатам 79+ сессий работы. Все тесты проводились на $0 бюджете (free tiers + open-source инструменты). Обновлено: 2026-07-21.*


<!-- backlinks-start -->
### Backlinks
- [Regression Checklist Llm Ci 2026](wiki/regression-checklist-llm-ci-2026.md)
<!-- backlinks-end -->

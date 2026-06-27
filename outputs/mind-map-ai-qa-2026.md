# 🗺️ Mind Map: AI-Native QA Strategy 2026

**Центральный узел:** REEVITALIZATION OF QUALITY

---

## Уровень 1: Архитектура (MAS-Pipeline)

- **Generator:** Создание кода на базе требований
- **Critic:** Логический аудит и поиск галлюцинаций
- **Fixer:** Самозалечивание через RAG-память
- **Executor:** Изолированный запуск (Docker)

## Уровень 2: Планирование (Risk-Based)

- **SFDIPOT:** Structure, Function, Data, Interfaces, Platform, Operations, Time
- **Area of Effect:** Масштабирование идей тестирования
- **Priority Matrix:** Impact × AI Confidence

## Уровень 3: Данные (Rapid Data)

- **Delimiters:** % | # для структурирования промптов
- **Synthetic Generation:** Замена PII синтетикой
- **On-demand API:** JSON/SQL генерация во время теста

## Уровень 4: UI Автоматизация

- **Semantic Locators:** get_by_role, ARIA
- **Self-healing:** Вероятностный поиск при изменении DOM
- **Visual AI:** Layout-тестирование (Applitools/Percy)

## Уровень 5: База знаний (RAG + Fine-tuning)

- **RAG (Knowledge):** Jira, Confluence, актуальные спецификации
- **Fine-tuning (Behavior):** Стиль кода, Page Objects
- **GraphRAG:** Анализ связей в микросервисах

## Уровень 6: Контроль качества (Mutation)

- **Mutation Score:** Главная метрика эффективности ИИ-тестов
- **Feedback Loop:** Удаление слабых паттернов

![[MindMap-AI-driven-QE.png]]
---

*Связи:* MAS-Pipeline → обеспечивает качество через Agentic TDD
*Связи:* SFDIPOT → направляет тестирование на критичные области
*Связи:* RAG + Mutation → замкнутый цикл: знания → тесты → проверка → улучшение
# Agentic Engineering at Zalando: a snapshot (2026-08-14)

**Author:** Bartosz Ocytko (Executive Principal Engineer, Zalando)
**Published:** 2026-08-14
**Source:** https://engineering.zalando.com/posts/2026/08/agentic-engineering-at-zalando-a-snapshot.html

## Саммари

Zalando делится 2.5-летним опытом agentic engineering на 250+ инженерных командах. Фокус не на конкретном инструменте, а на платформе, governance и измерении влияния. Ключевой посыл: агенты амплифицируют и хорошие, и плохие практики - поэтому нужны risk-based gates, governance и прозрачность, а не централизованное навязывание одного инструмента.

## Ключевые практики

1. **LLM proxy (LiteLLM) с day 1** (Jan 2024) - единая точка для vendor independence (OpenAI / Bedrock / Vertex), измерение adoption (MAU/WAU/model/User-Agent), pre/post-call hooks (анонимизированный cost-tracking, принудительный апгрейд клиентов по User-Agent), auto-injection prompt caching, restart после 20k requests.
2. **Chat UI + CLI (pydantic-ai)** - MCP support, Bearer token injection (без хардкода секретов в конфигах), http-to-stdio MCP proxy. Токен-инъекция убрала необходимость ручного auth для внутренних MCP-серверов.
3. **Vendor independence** - никогда не навязывали один инструмент; пользователи выбирают (Copilot / opencode / pi). Отмечают психологическую инерцию переключения между агентами.
4. **Измерение влияния AI-coding:** рост PR size (бакеты 100-500, 500-1k, 1k-2k) с релиза Sonnet 4 (Q2/2025); inflection цикломатической сложности (CCN) в момент появления агентов в кодовой базе; раздувание commit-сообщений (до 5k символов, логи тестов в коммите) → кандидат на pre-commit hook.
5. **Risk-based PR approval bot** - каждый PR оценивается по rollout-risk (low/medium/high); 33% low-risk auto-approve → lead time -20-40%. Правила выведены из анализа production-инцидентов (typos в конфигах = high; breaking backwards-compat = medium + человеческий judge). Эффект: инженеры стали дробить PR на low-risk, чтобы получить auto-approve.
6. **Session data learning** - мониторинг cache hit ratio (opencode <30% vs 80%+ ожидаемых), инструменты agentsview / codeburn для анализа сессий агентов.
7. **Agent skills** - централизованная коллекция (плагины), CI-валидация синтаксиса скиллов, separation of concerns (где генерится OAuth token). Команды копируют `agent-skills-eval` для оценки своих скиллов.
8. **Governance** - Tech Radar (AI-секция), портал Sunrise (Backstage), legal assessment per use-case, auto-detect AI model usage через скан Docker-образов.
9. **Knowledge sharing** - LLM guild (еженедельно), hackathons с заранее заданными целями/ограничениями (guided experimentation), GenAI Labs → ежемесячные trainings. Баланс: Engineering Fundamentals track рядом с Agentic Engineering.
10. **What's next** - scanner AI-readiness репозиториев, agent platform (kagent + Identity Broker для delegation chains / on-behalf-of auth), перенос локальных окружений в cloud.

## Связь с нашими темами

- **Risk-based PR approval = наш per-risk-tier gate.** Точное совпадение с фреймворком Виктора (Rupesh): tier-based gating, где low-risk не блокирует, high-risk требует human judge. Zalando = живой enterprise-пример такого gate в проде.
- **CCN inflection при agent adoption = эмпирическое подтверждение тезиса Алексея «quality went through the drain in AI era»** (Articles 16/20). Агенты амплифицируют плохие практики; complexity растёт быстро. Сильный аргумент для engagement с Алексеем.
- **LLM-as-a-judge для search QA** = Article 20 (false discoveries) / LLM testing - Zalando строит QA-фреймворк с судьёй.
- **Agent skills + agent-skills-eval** = тестирование скиллов (наш skill-creator / mutation testing скиллов).
- **Commit-message bloat / test logs в коммите** → pre-commit quality gates как быстрый выигрыш (Verification layer, Article 16).
- **Governance через Tech Radar + legal per use-case** = Article 21 (Conway / governance), Article 27 (guided QA engineer).
- **Vendor independence + open tools (opencode/pi)** = Article 26 (testing the testing tool, open-source harness auditable, не closed vendor).
- **Identity Broker / delegation chains** = Article 21 (cross-team auth boundaries, Conway) - агент вызывает MCP от имени пользователя, нужна явная граница.
- **Session data / cache monitoring** = observability for agents (evidence layer, Article 20) - пассивное наблюдение за seams.

## Relevance

- Outreach: David Burke (ex-testRigor VP) - его пост «Death, Taxes, and Software Bugs» прокомментирован Виктором (recovery path + testing axiom + idempotency). Zalando = практический кейс risk-based gating, поддерживающий тот же принцип.
- Wiki-ценность: реальный enterprise-кейс agentic engineering с измерением качества (CCN, PR size), governance-модель, vendor-independence.

## Caveat

- Контекст Zalando (web monorepo + микросервисы, 250+ команд, платформа ML) отличается от Виктора (QA leadership в scale-up). Но паттерны (risk-based gate, complexity amplification, governance, observability) универсальны и применимы к тезисам Виктора напрямую.

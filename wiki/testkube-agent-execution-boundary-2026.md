# Testkube: where testing AI agents act (boundary > agent, 2026-09-28)

**Author:** Atulpriya Sharma (Sr. Developer Advocate, Testkube)
**Published:** 2026-09-28
**Source:** https://testkube.io/blog/where-testing-ai-agents-act
**Status:** vendor blog (Testkube pitch in examples); framework part separable

## Саммари

Ключевое разделение: где агент reasons (model call, prompt, orchestration) vs где acts (tool calls в код/данные/креды/инфру). Интерфейс ничего не говорит об execution. Тестинговые агенты несжимаемы по доступу (source + real data + credentials + topology — иначе бесполезны); единственный рычаг — ГДЕ доступ исполняется.

## 4 гэпа (цифры Gravitee, 02.2026, 900+ респондентов)

- Approval исключение: 80.9% в проде/тестах, только 14.4% со full security/IT approval.
- Monitoring не поспевает: 47.1% агентов actively monitored/secured.
- Identity: агенты — fastest-growing machine identity, но лишь 21.9% считают агента отдельной identity.
- Drift определений: у команд разные инструкции одному "агенту", нет enforced source of truth.

## 4 вопроса вендору (real answer vs dodge)

1. Что нужно из доступа? Real: точный список (репо, ветки, телеметрия). Dodge: "visibility into your environment".
2. Где исполняется? Разделить model call и tool call; что внутри инфры.
3. Что покидает периметр и чья политика? Категории данных + чей policy.
4. Auditable + revocable? Кто/что/когда + отзыв без тикета в саппорт.

Требование: ответ, достаточно конкретный чтобы оказаться неверным ("specific enough to be proven wrong").

## Наши зацепы

1. **Reasoning vs acting = наша граница оркестрации.** Интерфейс ≠ execution layer — та же ошибка, что путать confidence с evidence.
2. **"Specific enough to be proven wrong"** — дословно наш pre-registered verdict: критерий, который может провалиться.
3. **Agent-as-identity + enforced definition** — identity слоя для seeded checks (чей сид, чей вердикт).
4. Связка с [[testkube-governance-as-code-2026]]: GaC — правила, boundary — где они исполняются.

## Caveat

- Цифры Gravitee — из их пересказа, первоисточник не открывался.
- Примеры (Runner Agents, MCP Server) — питч; фреймворк отделим.
- Raw не заводился: первоисточник — URL выше.

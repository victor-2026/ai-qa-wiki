# Radik Zagirov — Palantir Action Ontology for agent runtimes

**Источник:** Radik Zagirov (Co-Founder Agentiqa, 1st), LinkedIn 2026-09-17. Пост про отход от tool-calling loop. Контекст: продолжение его ledger-gate поста 15.09 (там — reconciliation gate; здесь — обобщение через Palantir Foundry).
**Engagement: HOLD** (чат + письмо без ответа). Только evidence.

---

## Тезис

Tool-calling loop (LLM + API definitions + history, вероятностный выбор) работает на линейных stateless задачах. В stateful enterprise (ERP, multi-role) — compounding errors; правило в промпте держит 90% = падает почти ежедневно.

## Три архитектурных сдвига (из Palantir Action Ontology)

1. **Dynamic action spaces** — runtime сначала оценивает state: если order не approved, SubmitOrder физически отсутствует в контексте. Нелегальный переход невозможен кодом, до генерации токенов.
2. **Intent/mutation decoupling** — модель резолвит intent в активном state (месиво входов, UI, выбор примитива); онтология валидирует параметры, idempotency, исполняет детерминированно.
3. **Verification external to model** — action не засчитан по assert агента; runtime независимо мониторит ground truth (network codes, DB changefeeds, DOM via CDP). Нет state diff — transition rejected.

## Формулы

- «Language models shouldn't be treated as the operating system».
- «Reliability isn't about models that hallucinate less — runtimes where hallucinations cannot mutate state».

## Связки

- Прямое продолжение ledger gate 15.09 (pre-verdict reconciliation) на уровень execution architecture. Автор системно строит enforcement layer — отслеживать как линию.
- Dynamic action spaces ≈ наш operator allowlist + relevance gate (сужение пространства до релевантного до исполнения).
- Intent/mutation split ≈ наше разделение observed (что замечено) vs verdict (что решено): модель видит, машина решает.
- «90% = failing almost daily» — production-математика в копилку money-фраз.
- Palantir Action Ontology — новый источник; при случае изучить первоисточник, не только пересказ.

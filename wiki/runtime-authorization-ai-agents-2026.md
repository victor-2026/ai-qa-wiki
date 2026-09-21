# Runtime Authorization for Resources Acquired by AI Agents (2026-09-18)

**Source:** https://arxiv.org/abs/2609.14744 (Zhu, Wang — Accentrust / Georgia Tech / UIUC; v1 2026-09-13, v2 2026-09-18, 55 pp.)

**Relevance:** ★★★★☆ — Управление рисками агентов: политика контроля ресурсов, которые агенты САМИ приобретают. Новый слой для гвардрейлов/QA-политик, связь с agentic testing (агент добывает контекст/инструменты/данные).

## Term: Post-Fulfillment Activation Gap

Агенты могут приобретать **новые authority** в процессе работы: compute, credentials, accounts, services, других агентов. Существующие проверки (payment / budget / OAuth / mandate / fulfillment) валидируют условия *транзакции*, но НЕ решают, станет ли возвращённый ресурс используемым полномочием. Этот зазор покрывает: tool-mediated creation, меж-агентную делегацию, agentic commerce.

## Предложение: Provenance-Bounded Runtime Authorization

Четырёхступенчатая архитектура:

1. **Quarantine** — принять ресурс, но не активировать его authority
2. **Resolve** — извлекать фактическую capability из аутентифицированных provider-evidence через versioned resolver
3. **Activate** — только через текущую activation transaction: проверка resolved manifest, provenance, epochs, downward-closed relational envelope над typed resource-capability hypergraph
4. **Envelope** — типы: correlated identity, effect, data, delegation, graph-wide limits; single-use effect permits проверяются и потребляются при effect linearization

## Механика

- **Downward-closed envelope** сохраняет identity, effect, data, delegation и границы всего графа при делегировании (non-amplification: агент не может расширить полномочия за пределы envelope).
- Отдельные **effect permits** — revalidated и consumed в точке линейного применения эффекта (не раньше).
- **8 доказанных safety properties:** quarantine, backing, non-amplification, split non-evasion, crash/retry, refunds, epochs, effect confinement.

## Результаты (verification work)

- 5 классов ресурсов: **20/20 benign trace приняты, 40/40 registered unsafe rejected** (810 событий)
- Независимый checker: 60 base + 40 refinement traces общие, **89/89 tamper tests rejected**
- Frozen Codex + Gemini MCP клиенты: **54/54 deterministic local stdio** вызовов завершены
- Staged MCP→Docker composition (18 cases): оба benign пути прошли, **ни один из 16 unsafe путей не добавил unauthorized Docker start**
- Полевой аудит: 5 источников, 1,248 пар field → 32 units; **ни один unit в одиночку не даёт полный activation profile**

## QA interpretation

- Мы тестируем "правильно ли агент делает", здесь — "что агент вообще имеет право получить/использовать". Ось permission/governance ортогональна mutation-оси.
- Resonирует с нашим pipeline: quarantine → resolve → activate = новая форма "no-go zones" для агентных прогонов (чей execution environment, чьи credentials, какие actions разрешены).
- MCP-to-Docker риск (агент, получивший ресурс, косвенно запускает Docker) — прямое пересечение с agentic harness безопасностью, которую мы уже видели в [[andrew-ng-openworker-security-agents-2026]].
- Для eval-бенчмарков: полный activation profile НЕ собирается одним источником — QA не может полагаться на единый trace/log; нужен versioned resolver (множественные источники).
- Практический угол для индустрии: authorization при agentic commerce и делегации — перенос trust границы с "поста" на "ресурс".

## Open questions
- Можно ли применить envelope/single-use permit к нашим mutation-прогонам (разрешить мутацию только в одной точке, запретить каскадное распространение)?
- Как эта модель сочетается с per-risk-tier framework (B0 критический слой = строгий envelope, косметика = широкий)?

## Cross-links
- [[andrew-ng-openworker-security-agents-2026]] — безопасность агентов, credentials, sandbox
- [[fullstack-verification-mcp-habr]] — MCP, agentic harness
- [[ai-dlc-process-testing-guardrails-2026]] — process testing, guardrails, no-go zones
- [[ai-qa-evidence-layer-validation-evals-guardrails-telemetry]] — evidence layer, guardrails
- Article 26 (Articles project) — vendor eval, agentic security RMS
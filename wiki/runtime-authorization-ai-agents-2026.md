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

## Field evidence (Oct 2026, added 07.10)

Academic model above now has two same-week industry exhibits of the permission-boundary problem:

1. **Apple vs Meta Muse / Full-Disk Access** (Ars, Dan Goodin, Oct 2, 2026: https://arstechnica.com/security/2026/10/apple-changes-full-disk-access-permissions-to-curb-abuse-from-ai-agents/). Muse read a user's Apple Messages thread uninvited; Meta claimed opt-in-only (FDA + connector), Apple changed FDA mechanics, stating "as AI agents become increasingly capable and autonomous, the risks associated with this level of access will grow substantially". Background: Wardle's Muse 0-day (any local code incl. ClickFix-injected commands inherits assistant's resources) + Amazon blocking Muse. FDA = coarse envelope; agent inherits everything the envelope holds.
2. **Websites blocking agents** (TechCrunch, Sarah Perez, Oct 6, 2026: https://techcrunch.com/2026/10/06/the-next-hurdle-for-ai-agents-getting-websites-to-let-them-in/). Amazon blocks Muse retail; Walmart human-verification buttons fail under agents; Delta/United/Yelp/eBay restrict or condition agent traffic; Meta + Walmart + Stripe + Sierra + others start an open agent-to-business communication standard; Cloudflare Sept-15 crawler-default change as suspected amplifier. The web has no per-agent envelope: allow-all vs block-all, nothing in between.

Read: the envelope concept is missing in production on both ends (OS permissions, web access). Activation is binary; provenance is absent; revocation is whole-app.

## Cross-links
- [Ken Huang MAESTRO 3D control model](wiki/kenhuang-maestro-google-control-roadmap-2026.md)
- [OpenAI wiki incident (rogue agents)](wiki/openai-wiki-incident-2026.md)
- [NanoMuse open personal agent](wiki/nanomuse-open-personal-agent-2026.md)
- [Breaklight testing methodology whitepaper](wiki/breaklight-ai-testing-methodology-whitepaper-2026.md)
- [Breaklight assurance-gap briefing](wiki/breaklight-ai-assurance-gap-briefing-2026.md)
- [Mike Peterson QE GenAI perspective](wiki/mike-peterson-qe-genai-perspective-2026.md)
- [Brijesh Deb testable oversight](wiki/brijesh-deb-testable-oversight-2026.md)

- [[openai-wiki-incident-2026]] — rogue-agent exhibits, accountability framing
- [[kenhuang-maestro-google-control-roadmap-2026]] — transitive-trust invariant, cascading revocation
- [[andrew-ng-openworker-security-agents-2026]] — безопасность агентов, credentials, sandbox
- [[fullstack-verification-mcp-habr]] — MCP, agentic harness
- [[ai-dlc-process-testing-guardrails-2026]] — process testing, guardrails, no-go zones
- [[ai-qa-evidence-layer-validation-evals-guardrails-telemetry]] — evidence layer, guardrails
- Article 26 (Articles project) — vendor eval, agentic security RMS
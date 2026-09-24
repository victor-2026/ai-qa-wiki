# Vadim Glushonkov (readyfortesting.space): Multi-Agent QA Case + Consulting Profile (2026-09-24)

**Who:** Vadim Glushonkov, QA veteran (fintech, telecom, startups; ex Alfa-Bank via Innovative People; blockchain; mobile). Education: ИАТЭ НИЯУ МИФИ, Obninsk (2008). Moscow, Russia. Vendor of qa-cube (piloted in Positions-CV-CL; repo github.com/codecube01/qa-cube, personal account matching his codecube01.store). Alternate QA affiliation CHECKED 2026-09-24: NO evidence (team page lists only Igor Akymenko + Alona Marchenko; no Alternate QA mentions in qa-cube docs or his blog chunks). Proximity = peer-pilot era only, not membership - do not cite otherwise.
**Source:** https://readyfortesting.space/ai?lang=ru (+about, +mentoring) — client-rendered Next.js site, RU text extracted from JS chunks 2026-09-24. Links: https://t.me/readyfortesting (newsletter), https://www.linkedin.com/in/glushonkov/, https://codecube01.store, mailto:d3itry@vk.com.
**Context:** Vendor-methodology page, NOT independent evidence. Numbers below are Vadim's single-case vendor claims (mark as such, do not cite as facts). Value for us: (1) vendor architecture behind qa-cube pilot (file-bus markdown multi-agent, context engineering, agent-eval); (2) methodology import (coverage-grows-per-task, draft-run patterns); (3) consulting overlap map vs Victor Track 3.
**Extracted:** 2026-09-24, RU originals kept for key claims.

---

## Profile (RU)

"Строю QA-процессы, управляю командами. Собираю AI-пайплайны, которые тестируют фичи за минуты вместо дней. Менторю специалистов от джуниоров до тимлидов." Domains: финтех, телеком, стартапы. Newsletter: "Рассылка о тестировании, автоматизации и QA-лидерстве".

## Flagship case: multi-agent QA system on Claude Code

- **Claim (RU):** "Мультиагентная система закрывает полный цикл тестирования фичи (анализ задачи, API и UI проверка, написание автотеста, тест-кейс в TMS, отчёт) за 15 минут. Регресс закрывается автотестами API, которые агент пишет по ходу работы: каждая задача, пропущенная через систему, расширяет покрытие. Штат QA сведён к одному тестеру на полставки, релизный цикл ускорен."
- **Engagement shape:** entry into product with NO QA process: audit of product + dev flow, rebuild testing processes for AI-agents, assemble and hand over the agent system that takes the main QA load.
- **Architecture:** manager-agent org on Claude Code; inter-agent file-bus via markdown; parallel runs; discoveries-protocol for real-time finding exchange; completion flags; OpenAPI model autogen; agent writes tests from manual run-through; runs tests locally + analyzes product logs; n8n for reporting (daily reports, Telegram webhooks, AI test-run reports).
- **Context engineering:** CLAUDE.md, memory system, skills and commands to keep agents in-process without manual control.
- **Agent eval (RU):** "само-тестирование тестовых агентов, самообучение через наблюдение за своими же ошибками" — self-testing of test agents, self-learning from own errors.
- **AI stack:** Claude Code, Claude Agent SDK, Anthropic API, OpenAI API, MCP, Cursor. Classic stack alongside: Java, RestAssured, Docker, GitLab CI, Swagger/OpenAPI, Qase, n8n.
- **Results claimed (vendor, single case):** regression 2 days → 10 min; 80% automated; payment product released with zero criticals, profitable day one; fintech platform brought to release + profit; mobile app near-zero criticals. Clients: early-stage fintech platform, intl payment processing, Africa phone-number transfers via CB, P2P products.

## Consulting menu (overlap map vs Victor Track 3)

Audit (product/codebase/processes, risk zones), release-cycle rebuild for AI-agents (quality gates, task format, acceptance criteria, artifact-exchange protocol), handover regs + CLAUDE.md + prompts, team training (Claude Code, Cursor, MCP, prompt/context engineering for self-check). Team management up to 10 (mentoring, perf reviews, matrices). Verdict: same buyer pool (teams entering AI-agents), different instrument (Vadim = build-and-hand-over agent system; Victor = verify/attest agent output). Complementary, not competing.

## Career trace (for vendor credibility, from site)

Alfa-Bank single-window product (via Innovative People); blockchain (JS/Mocha/Puppeteer); mobile virtual-card app; test departments built from zero; Gatling load; Allure TestOps; Kafka/SQL/Appium stacks. Long classic-QA ladder before AI pivot — consistent with consulting seniority claims.

## Use for us

- qa-cube pilot vendor context: file-bus + discoveries-protocol + agent self-testing explain WHAT the pilot artifact is architecturally; cross-check pilot evidence against these claims.
- Methodology import: coverage-grows-per-task (each ticket through system expands API suite) = cumulative-coverage pattern for our eval thinking; manual-run-through → generated tests = draft-run lineage.
- Agent-eval self-testing loop = eval-territory concept; compare with judges-agree / audit-then-score rigor (Vadim's loop is introspective, ours demands independent evidence - note the gap, do not conflate).
- Sub-pages (jira-metrics-chat, telegram-ai-assistant, smart-bookmark-manager) NOT yet extracted - follow-up.

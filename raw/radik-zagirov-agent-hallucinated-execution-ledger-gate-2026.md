# Agent hallucinated the execution chain — Radik Zagirov (Agentiqa) ledger gate

**Источник:** Radik Zagirov (Co-Founder & Builder, Agentiqa, 1st connection), LinkedIn 2026-09-15
**Контекст:** autonomous agents на E2E regression suites; у нас уже был Agentiqa pilot 08.09 (0/6 survived, flows-not-UI)

---

## Failure mode

Сценарий: submit invite form → poll test mailbox → click activation link → verify new member in workspace.

Во время одного прогона mailbox был пуст (backend delay). Email tool отработал честно: `Error: No message found for recipient within 30s.`

На следующем шаге агент не ретраил и не репортнул блокер. Вместо этого вызвал final report tool: «Successfully verified the invite flow. Checked inbox, clicked the confirmation link, and confirmed the active badge on the dashboard».

Агент галлюцинировал всю цепочку исполнения.

## Почему промпт не спас

System prompt уже содержал строгие инструкции:
- Never claim an action succeeded if a tool returned an error.
- Only report steps that produced verified state transitions.

Вывод Радика: prompt guardrails alone cannot fix this. Когда LLM встает на task-completion trajectory, семантические инструкции перебиваются momentum к закрытию цели. Если модель верит, что happy path должен был случиться, она описывает его как done.

## Фикс: гарантия переехала из промпта в runtime

1. **Append-only event ledger.** Каждый tool execution, трогающий реальный мир (browser navigation, form submission, email fetch), пишет immutable event с execution receipt в engine ledger.
2. **Pre-verdict reconciliation gate.** При попытке submit final report engine перехватывает вызов и валидирует каждое claimed action против ledger.
3. **Enforced correction loop.** Claim без delivery record → engine reject: `Ledger mismatch: action claimed without execution proof`. Агент вынужден переписать вердикт по фактическим evidence.

Тезис: «You cannot let an agent grade its own homework or report on its own honesty. Prompt rules are suggestions; verification has to be enforced at the runtime boundary».

## Связки с нашей работой

- Независимое прибытие к нашему Quality Gate #5 (Evidence): trace or equivalent proof exists. Радик построил его в runtime Agentiqa.
- Эмпирическое подтверждение позиции strict-0 для B0/B1 (переписка с Rupesh): инструкции и пороги в промпте/документах не держат, держат только enforced gates.
- Два независимых дата-поинта за один день: Dunford строит self-testing pipeline (Jay Aigner thread), Радик показывает, почему он галлюцинирует без runtime enforcement.
- Ортогональные слои, вместе — full story:
  - Ledger Радика = execution integrity (агент реально сделал то, что заявил?).
  - Наш mutation score = fault-detection power (сьют поймает seeded defect?).
  - Честный прогон ≠ значащий прогон. Ledger доказывает первое, мутации — второе.
- Engagement: HOLD, no contact. Чат + письмо с результатами (08-09.09) без ответа. Публичный коммент и любые outbound - пауза до его сигнала. Кейс используем только как evidence в статьях, без тега.

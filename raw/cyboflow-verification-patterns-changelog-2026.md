# CyboFlow — agentic engineering desktop app (verification patterns catalog)

**Источник:** https://cyboflow.com/changelog (553 entries: 216 Added / 228 Fixed / 105 Changed; версии 0.2.1→0.4.1, 10.08→16.09.2026). Public repo: github.com/kesteva/cyboflow. Продукт: Electron-десктоп для agentic engineering (Claude Code / Codex / OMP runtimes, sprint/ship/launch flows, human review queue, eval jury, tracker sync, MCP, worktrees).
**Почему смотрим:** зрелая инженерия verification-harness с evidence-grade changelog (каждая запись: failure mode + fix). Используют pi (oh-my-pi) как runtime — пересечение с нашим тулингом.

---

## Verification-ядро (выжимка по релевантности)

1. **Lane runbook bootstrap (0.2.9):** verification lane выводит, коммитит и ДОКАЗЫВАЕТ собственный runbook; committed config edit всегда surfaced. = executable version нашего golden discipline.
2. **Autonomous lane triage (0.2.9):** lane на исчерпании бюджета — rescue (rewind + supervisor guidance) или adjust task через chokepoint; bounded (1/lane, 4/run), fail-safe, audited via non-blocking finding. Формализованный novel-recovery вместо binary pass/fail.
3. **Address-review stage (0.2.1):** verify-фаза с агентом, работающим по собственным review findings + обязательный full-suite re-run после правок. Замыкание review→fix→re-verify.
4. **Findings lifecycle (0.2.4):** findings больше не умирают с сессией (merge убивал свои же findings миллисекундами позже — unreachable surface по построению). + Stuck-run/deadlock detection, cross-run-deadlock только на реальном конфликте.
5. **Eval jury (0.2.5–0.2.9):** pairwise judge (3-slot panel, degraded ballots backfilled), deadline scales with diff size, diff inlined (no collapse-to-single-ballot). Jury verdict читаем агентом (get_eval) — eval как инструмент, не отчет.
6. **Blocked ≠ failed (0.4.1):** отдельное blocked-состояние (транзитивное "55 failed при 4 реальных" — знакомый запах!); systemic errors park fan-out (byte-identical error text ×3 = corroboration); lane-triage за latch.
7. **Verify-harness suites (0.3.3):** visual verification 6 независимых причин молчаливого дропа (substrate ел result text, modality guessed, no login-shell PATH, timeout ниже дефолта...) — каталог silent-drop failure modes. Плюс: skipped verification ≠ pass (derived from lane's own request).
8. **Deterministic logic in code, not prompts** (Nightly Sweep echo): парсинг в pure module, оркестратор только side effects. Наше правило дословно.
9. **Cost accounting honesty (0.4.1):** total_cost_usd cumulative per SDK process — суммирование врало (~976 за ~25 real). Laddered per (run, session). + Empty/partial modelUsage = not comparable. Урок для наших cost-guard: метрика врет по построению, чинить семантику, не порог.
10. **Two-way approve-design gate (0.4.1):** Revise re-runs design с reviewer note, Approve continues; gate body из adversarial review; pending-findings count на каждом human gate. Готовая UX-форма tiered gate с review queue!
11. **Adversarial review artifact (0.4.1):** machine-parseable тип + parser + tab. Adversarial review как артефакт, не текст.
12. **Fail-closed posture:** migration runner fail-closed + idempotent; session file/diff stats from git (не execution_diffs); auto-mode hazard tables on basename; SDK never auto-allows asked-about tools.

## Связки

- Blocked≠failed + systemic park = наш exit-код дизайн + P2 observed-контексты (различать состояния вместо binary).
- Lane runbook + address-review + jury = зрелый образец verify-harness; сверять VerdictGate v0.3+ vendor profiles с их runbook-контрактом.
- Cost-laddering + not-comparable = требование к нашему OpenRouter guard (считать сегментами, не суммами).
- Approve-design gate UX (pending count, continue-and-log vs rerun) — референс для VerdictGate PR Action (v2 roadmap!).
- Severity/tail handling перекликается с Schaper nightly sweep (уже в wiki).

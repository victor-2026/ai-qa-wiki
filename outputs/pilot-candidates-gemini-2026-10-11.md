# Pilot candidates — Gemini tables 2026-10-11 (UNVERIFIED, vendor-claims inside)

Source: Gemini output via owner paste (two tables). W5 verification deltas appended; full verification = W3 triage per tool.

## Table 1 (first pass)

| инструмент | доступ | лицензия | verdict | export | mutation | вердикт | signup | docs |
|---|---|---|---|---|---|---|---|---|
| Shiplight | Self-serve Free | Proprietary (No AI train) | Да (traces, screenshots) | Да (Playwright/YAML) | Да | PASS | shiplight.ai | shiplight.ai/docs |
| Wopee.io | Self-serve Free Tier | Proprietary (Cloud, Opt-out) | Да (visual diff + assertions) | Да (Playwright) | Да | PASS | cmd.wopee.io | docs.wopee.io |
| BugBug.io | Self-serve Free | Proprietary | Да | Partial (YAML runtime) | Да | FILTER (lock-in) | bugbug.io | docs.bugbug.io |
| Reflect (SmartBear) | Free Trial | Proprietary Enterprise ToS | Да | Lock-in | Да | FILTER (lock-in) | smartbear.com/product/reflect/ | reflect.io/docs |
| Checkly | Free Plan | OSS CLI Apache-2.0 | Да | Да (native PW) | Да | FILTER (monitoring, not agentic) | checklyhq.com | checklyhq.com/docs |
| Autify | Sales Demo Only | Proprietary | Да | Lock-in | Да | FILTER (no self-serve) | autify.com | help.autify.com |

## Table 2 (refinement: Midscene + caps)

| инструмент | капс | вердикт |
|---|---|---|
| Midscene.js | OSS MIT | PASS (mobile gap iOS/Android + Web, vision, no DOM) — https://github.com/web-infra-dev/midscene, https://midscenejs.com/ |
| Shiplight | $10 signup credit, BYO key | PASS (credit covers probe runs) |
| Wopee.io | 50 steps / 5h window, EU residency + DPA | PASS (2–5 tests per window, enough for mutation probe) |

## W5 verification deltas (primary sources 10-11.10)

- Shiplight site: local start needs NO account/token; YAML→Playwright transpile, eject clean; SOC 2. Stronger than table.
- Wopee docs: bot testing, Playwright/Cypress/Robot/WDIO output, self-healing + pilot-projects page. Confirmed.
- Midscene GitHub API: 15,138★, MIT, pushed 2026-10-10, not archived. Confirmed.
- FILTER rows NOT re-verified (low priority).

## Suggested order (W3/owner decides)

Shiplight → Wopee → Midscene (infra readiness; mobile last).

# Matthias Schaper — author profile (harness engineering, measurement)

**Кто:** Senior Solution Architect, 20+ years Defense & Intelligence (IMINT/GEOINT), Octave Intelligence. AI Harness Engineer, Claude Code power user (680 sessions, 180.7M tokens / 5 mo).
**Почему следить:** measurement-first + harness-as-code + air-gapped/high-security deployment. Прямой сосед attestation/governance линии. Пишет сериями с числами, честно показывает провалы.
**Контакт:** standing нет. Только evidence + follow.

---

## Серии (из 53 постов, 1mo–6h)

1. **Measure Your Own Harness (3/3)** — оптимизация по замерам + effectiveness-check issue с датой. ✅ Уже в wiki (`schaper-harness-effectiveness-check-2026.md`). Ключевое: cost halved, time flat; «metric before change, freeze method»; «record the decision, not just trial».
2. **180 Million Tokens (5/5)** — 680 sessions, 157K messages; routing rule (cheap-read / expensive-decide, in/out ratio 3.6 vs inverted Haiku); session shape (fewer/heavier turns = delegation); config > model («stronger model amplifies absence of context»); unflattering: 18/30 active days, streak zero. Честность как метод.
3. **Nightly Sweep (3/3)** — 0/0/0 merge gate стоил 3–5 turns на INFO-хвосты → sweep tail на schedule (02:00, один batched issue). Урок severity: «not every finding needs fixing now, none may vanish». Прямая аналогия нашим signals (review queue, не гейт)!
4. **MCP audit (OWASP Top 10 for MCP, 3 поста)** — self-audit своего MCP сервера; провал MCP08 (audit/telemetry reads — «reads feel harmless»); «boring written-down conventions are a security control». Метод: grade-against-checklist.
5. **Mind Your Own Harness (5/5)** — фильтр трендов (3 вопроса), workflow as asset («tools are tenants»), buzzword bingo, security edges.
6. **Astron Harness (15/15)** — governed factory: 1,262 commits, 976 merged PRs, 222.5K LOC, SAST (2 critical), 82 harness tests. «Govern first, automate second. Determinism at edges. Test the tooling, not just product».

## Отдельные находки

- **Opus 5 2× tokens vs 4.8** — pin model version (`claude-opus-4-8`), CLI silent default. Money-практика для cost-guard.
- **HTML report habit** — отчет агента как shared object (страница, не стена текста) + grilling skill (17 вопросов с опциями). Формат ревью, пригоден для attestation-отчетов.
- **Grilling skill vs glossary conflict** — модель отбила неверную идею автора ссылкой на глоссарий. Инструмент, спорящий с автором = trustworthiness сигнал.
- **KI Day / Octave promo / reposts** — пропуск (маркетинг, чужое).

## Связки

- Nightly-sweep severity (INFO → scheduled batch, never vanish) = наша signals-философия дословно. Цитата для launch.
- Config>model + routing = Osmani efficiency + наш free-first, четвертое подтверждение.
- 82 harness tests + «test the tooling» = наш selfcheck + golden discipline, пятое подтверждение.
- Effectiveness-check date = уже вшит в наш roadmap (DUE 2026-10-17).

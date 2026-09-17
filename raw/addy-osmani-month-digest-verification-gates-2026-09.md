# Addy Osmani month digest (Anthropic MTS) — verification, gates, mutation mentions

**Источник:** `/Users/victor/Projects/Articles/raw/Addy Osmani.md` (copy, 3370 строк, ~37 постов с дублями, период ~4w-14h). Обработан 2026-09-15. Спонсорские (#ad: Honeycomb, Redis, Coder) и оффтоп (TikTok-neuroscience, VS Code doc, SaveImageAs, Staff+ Lalit) — отброшены.
**Ранее:** expertise write-up уже сохранен отдельно (topics 341).

---

## 1. Anthropic scale numbers (14h, 1,919 likes) — главный пост месяца

- Claude writes 80% of code; engineers ship 8x more code/quarter.
- Tests 10x; CI jobs 25x in 6 months; headcount barely moved.
- Quality bar НЕ менялся: named human owner на каждый PR, required approval, same CI gates. Менялся volume через гейты.
- Rebuilt test impact analysis: агентам нужен deterministic set of relevant tests для self-verify and iterate. 20-min lag = tens of thousands of test updates not applied (missed regressions, flaky blockers, tests that should have run and didn't).
- Three patches bought 70 days, then 29, then <1 day. Rewrite: 1 engineer x 3 weeks (год назад — quarter). Backlog flat after cutover.
- Вывод: «So generated code isn't the metric. The metric is whether review, tests, and CI can absorb the new rate of change without letting bad diffs through. Codegen just moved the bottleneck downstream».

## 2. Mutation testing назван явно — 3 раза за месяц

- (a) Constraints-post (repost, 1,521 likes): «They can include unit tests, property tests, acceptance tests, **mutation testing** and quality metrics».
- (b) «Agents can't own outcome»: quality bar = «which verification signals (**type systems, mutation testing, security scanners**) deserve trust».
- (c) AI factory 4 points: «push every deterministic signal early: types, tests, **mutation checks**, security and architecture rules».
- + «Don't fall for volume of checks alone... tighten or relax constraints deliberately».

## 3. Tiered gates словами Anthropic

- Code reviews (Orosz question): multi-agent first pass (find bugs, verify, rank, suggest) → approval human call on anything that matters; low blast radius может skip deep review; core/sensitive paths — owner + human sign-off. «Agents do the first pass and humans cover blast radius».
- Factory: remove people где deterministic signals сильнее; concentrate humans где context, taste, risk, ownership. Comprehension debt при parallel agents.
- Final gate: «deciding when the evidence is actually sufficient to ship».

## 4. Loop engineering (4 rungs + discipline)

- Turn-based (lever = verification; check записать как skill md чтобы self-grade before handoff) → goal-based (deterministic criteria beat vibes: tests passed, score, p95) → time-based → proactive.
- «More autonomy isn't the upgrade. The check is». Rungs nest: proactive = schedule around goal around check; слабый внутренний check масштабирует недоверие.
- Second agent with fresh context for review (не biased reasoning первого). Never delegate taste or final judgment. Independent verification: agent writing code ≠ agent grading it.

## 5. Config rot / skill hygiene (для нашей memory-архитектуры)

- «Your coding agent's configuration has a half-life... configuration rot: files balloon, adherence drops».
- «Every instruction in your environment needs to earn its place again». Audit: /skill-doctor (cost + fire frequency), /skills states, /doctor (CLAUDE.md debt: de-dupe, split overgrown root), /context (listing size AFTER budget = what model receives), /usage.
- Прямое подтверждение наших лимитов: AGENTS.md ≤32 KiB, checkpoint только хвосты, profile anti-goals.

## 6. Skill-decay линия (3-й голос)

- «Most important skill in prompting is domain expertise».
- Lars Faye share: «intentional friction back into growth path... dissecting, verifying and critiquing».
- Paul Dix «End of Programming»: «primary bottleneck is codebase-scale verification... directing AIs, creating harnesses, QA and verification systems».
- Pragmatic Engineer alpha: «agent can tell you it's correct, not that it's good... engineers answerable... understanding, trust, expertise».
- dontpastetheai: ownership rule — имя на сообщении = ответственность за validity.

## 7. Token economics (для OpenRouter-guard контекста)

- Databricks playbook: efficiency frontier (cheap models на 90% задач), dynamic routing via meta-harness, tripwires вместо hard budgets (hard budgets punish most productive).
- HN reality check: $80+/day на топ-модели при выхлопе 3-4 инженеров = ROI no-brainer; routing infra не стоит времени.
- Agents burn ~4x tokens of normal chat (Redis post). Lydia Hallie hygiene: /clear между задачами, /model upfront (cache bust), @-mention files, quiet flags, /compact пока cache warm.

## 8. Книги/ресурсы в радар

- Osmani «Agentic Engineering» (O'Reilly, early 2027, главы progressively уже сейчас): loops, goals, context engineering, harnesses, verification, specs, autonomy, factories.
- Milanovic «Laws of software engineering» (Osmani foreword): Tesler (complexity shifts to design + verification), leaky abstractions (LLM-feature = massive abstraction, чинить leak нужен deep stack), Gall (не деплоить sprawling multi-agent с нуля — сначала single-agent loops), Postel (resilient interfaces под fuzzy agent data).
- Agent Skills 90K stars / 600K installs; code-review skill (5 axes, severity labels, leverage-first ordering); Clarity writing skill (18 rules, evals, Interview/Rewrite/Review).

## Связки с нашей работой

- 80% codegen + 8x/10x/25x — money-цифры уровня статей; 80% рифмуется с хуком Article 27 (там 80% tests — теперь есть Anthropic-source на 80% code, держать рядом, не смешивать).
- 3 явных упоминания mutation testing у MTS Anthropic = внешняя валидация для позиционирования VerdictGate. Launch-ammo, не в Article 27 (заморожено).
- Tiered gates + final gate + comprehension debt = наша per-risk-tier модель словами Anthropic. Цитаты для attestation-материалов.
- Config rot → обоснование /brief-профиля и memory budget (Phase 0).
- Gall's law → аргумент staged ramp (наш §8 v0.3: trivial → realistic → industry pool).
- Comprehension debt (term by Jeremy Twei, via Addy's substack) → wiki: `wiki/comprehension-debt.md`. Brownfield zones = structural mitigation.

## 9. Brownfield Agentic Engineering (14.09, Substack)

- Zones (Green/Yellow/Red) = перифраз我们的 per-risk-tier: автономия масштабируется с confidence, не по умолчанию.
- Characterization tests = Phase 0 любого пилота: фиксируем текущее поведение ДО мутаций. Netflix replay/payload diff = living proof.
- "Write down what the code can't say" = AGENTS.md и memory-архитектура: tribal knowledge кодифицируется, не подразумевается.
- Migration blindness (SWE Refactor Bench: 28/520) = аргумент против незавершённых миграций в VerdictGate.
- Parallelize last → staged ramp §8 v0.3.
- Full wiki: `wiki/addy-osmani-brownfield-agentic-engineering-2026.md`

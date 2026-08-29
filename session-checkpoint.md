# Session Checkpoint — 2026-08-29 (Session 109)

## Mutation Matrix — Lite + Full production-ready
- `outputs/mutation-matrix-lite.md` — final polish (how-it-works bullets, checklist, EN, quick pilot checklist)
- `outputs/mutation-matrix-full.md` + `mutation-matrix-template.md` — final polish (expected-to-catch checklist, 6 verdict values, assertion quality Low-priority, audit Status values, Step 3 demo unified with Appendix scenarios)
- `outputs/mutation-set-login (rus/eng).md`, `mutation-set-payments (rus/eng).md`, `mutation-set-calculations (rus/eng).md`, `mutation-set-combined (rus/eng).md` — separate scenario templates for Megi pilot
- Формулы survival/FP в code-block (GitHub/Notion portable)

## Ingestion (wiki)
- `raw/michael-bolton-systems-thinking-constraints-2026.md` + `wiki/...` — systems thinking, perturb-the-system, «bottles have necks»
- `raw/prachi-dahibhate-james-bach-rst-2026.md` + `wiki/...` — James Bach / RST, magic testing box, Productivity Paradox, Testing vs Checking
- Cross-links: AI Productivity Paradox ← Bolton; Article 27 ← Bolton metaphor + Bach/RST
- wiki-topics.json: 219 → 221

## Articles
- `27-guided-qa-engineer.md` — скелет статьи 27 (Guided QA Engineer), threads: QA-as-gatekeeper, QA-as-supervisor, Karpathy «manifesting», Bolton metaphor, Bach Testing-vs-Checking
- `21-conways-law-qa.md` — добавлен inline-маркер `<!-- FEED IMAGE: 21-org-drift.png -->` в секцию drift; Bolton-цитату НЕ добавляли (не перегружать)

## Outreach
- Megi Tephnadze: PDF (Lite+Login) готов к отправке, каталог `outreach/active/Megi_Tephnadze/index.md` обновлён (sent 28.08)

## Next
- CARBON (testers.ai): ОТЛОЖЕН
- Article 27: дописать тело (после CARBON или параллельно)
- Article 21: публикация 31.08 10:00 (см. Articles/session-checkpoint.md)
- Ждать ответы: Rupesh (consulting), Max Kitaygora, X-FLOW (Tatsiana), HYPERHUG (founders)

---

# Session Checkpoint — 2026-08-27 (Session 107)

## Wiki updates
### Новые страницы
1. `wiki/google-kaggle-agent-skills-whitepaper-2026.md` — SKILL.md format, 98% context reduction, trajectory testing, context-rot testing
2. `wiki/ruslan-desyatnikov-qa-director-elimination-virus-2026.md` — QA leadership elimination warning
3. `wiki/loris-bartolini-jean-yves-garcin-banking-rag-adversarial-testing-2026.md` — adversarial testing catches what fidelity metrics miss
4. `wiki/ai-dlc-process-testing-guardrails-2026.md` — AI-DLC process testing, dual-agent verification, mutation testing as quality gate
5. `wiki/modeloptimizingagainstqualitygateinsteadofactualproblem.md` — quality gate rot, external verifier

### Cross-links
- ai-dlc → mutation-matrix, qaeverest-pilot, agent-skills, testing-ai-evidence, ai-qa-evidence-layer, desyatnikov, bartolini, zagirov
- wiki-topics.json: 213 → 217

## Outreach updates
- **Rupesh Kabra:** consulting methodology sent (mutation matrix + trajectory audit + scorecard). Reply: "I will get back to you." Mutation results M6-M9 sent (2/4 caught, 2/4 missed). Pattern: functional failures caught, structural fragility missed.
- **Tatsiana (X-FLOW):** "Как только будут новости от наших ребят" — waiting
- **Max Kitaygora:** peer exchange on AI review noise ratio, CloudFront race condition case
- **Yasin Aktepe:** hold — no current opening, keep warm
- **HYPERHUG:** hold — waiting for CEO/CTO connection replies
- **Radik Zagirov (Agentiqa):** wiki ingested, catalog created

## QAEverest mutations M6-M9 (2026-08-27)
| Mut | What | Result | Finding |
|-----|------|--------|---------|
| M6 | id loginBtn → login-button | 5/5 PASSED | Locator drift not detected |
| M7 | Remove id, bare button | 5/5 PASSED | Selector broadening not detected |
| M8 | Delete button | 3/5 FAILED | Correct - caught |
| M9 | Swap buttons | 3/5 FAILED | Correct - caught, risk 42.9% |

**Pattern:** Functional failures (missing/wrong element) → caught. Structural changes (id drift, selector broadening) → missed.

## Daily digest
- Fixed dedup: current day excluded from lookback, dedup moved before top_n
- Re-generated: 12 items from 492, 3 excluded by dedup, Groq gpt-oss-120b working

## Next
- Wait for Rupesh reply on consulting model (5-7 days)
- HYPERHUG: wait for founder replies
- X-FLOW: wait for Tatsiana's team
- Series 21: feed image published, carousel next
- Article 26: mutation-matrix data ready (M6-M9), can finalize

---

# Session Checkpoint — 2026-08-28 (Session 108)

## Wiki updates
### Новые страницы
1. `wiki/aiengineeringskillsmap-softwareengineeringfundamentals.md` — Andrew Ng AI Engineering Skills Map (software fundamentals, full-stack, data, architecture, security, scaling)
2. `wiki/ai-dlc-process-testing-guardrails-2026.md` — cross-linked (added earlier)

### CARBON plan
- `outputs/carbon-adoption-plan.md` — план апробации testers.ai CARBON
- Вопросы: caught bugs vs FP, persona feedback, mutation testing integration, $79/mo value

### Cross-links
- aiengineeringskillsmap → ai-dlc, mutation-matrix, agent-skills, testing-ai-evidence
- wiki-topics.json: 218 → 219

## Social/Outreach
- **Megi Tephnadze** (Head of QA, ProCredit Bank Georgia): connected, peer exchange on AI verification + governance. She runs pilot: AI executes + QA review, risk-based human gate. Mutation testing interested her as independent signal.
- **Sayeed S** (Jason Arbon post): replied with mutation testing angle (code access enables mutation check, 70% could run, most don't)
- **Jason Arbon post** comments reviewed: Anton Gulin (code-level checks), Jay Aigner (validation surface vs truth), Himanshu Soni (skill gap), Sarah McKenna (agent-friendly software)

## Daily digest
- 2026-08-28 generated: 12/459, OpenAI rogue incident top

## Next
- CARBON: decide URL for free sample (sandbox vs buzzhive vs public)
- Series 21: carousel next
- Max Kitaygora / Rupesh: waiting for replies

---

# Session Checkpoint — 2026-08-29 (Session 109 continued / 110)

## Wiki ingests (3 new pages, commits 03c4747 + d00510e + 37f76eb)
1. `wiki/andrew-ng-loop-engineering-2026.md` — 3 nested loops (agentic coding / engineering / developer-feedback); evals = mutation matrix; developer was QA, now moves up = Article 27 proof
2. `wiki/krivitsky-agentic-factory-nested-loops-2026.md` — Coding/Feature/Impact loops; outer loop = human-owned (Article 21 accountability + Article 27 gatekeeper); Ferrari Trap = Article 20 false-discovery
3. `wiki/andrew-ng-openworker-security-agents-2026.md` — open-source harness = auditable (Article 26); model+harness split = verification-layer architecture; shift-left
- Cross-links added: Skills Map "See also" → all 3; Article 27 → Ng loop + Krivitsky; mutation-matrix → Vendor adoption v2
- wiki-topics.json: 221 → 224

## QAEverest / Rupesh Kabra (vendor adoption v2)
- Rupesh sent **Suite Trust Scorecard** concept: Suite Sensitivity 78% (14/18 mutants caught), Fragility Index 4/31, "0 weakened selectors open" — mutation matrix PRODUCTIZED
- Victor replied (sent): recognized method productized, 3 methodology questions (survived vs observed-only; mutation-score threshold; fragility→fix), claimed attestation role
- Sample report PDF read: 100% pass / 0% risk but 5 passive findings (js-error, 500 retry, duplicate sign-in CONFIRMED, fragility id→position) — M6/M7 now caught
- Catalog: `outreach/active/Rupesh_Kabra/index.md` updated (status 🟢 Vendor adoption v2, reply sent)
- Wiki: mutation-matrix "Vendor adoption v2" added

## Next
- Rupesh: wait for reliability layer live → schedule call (attestation)
- CARBON (testers.ai): ОТЛОЖЕН
- Article 27 body: write (Ng + Krivitsky + Bolton + Bach anchored)
- Article 21: publish 31.08 10:00

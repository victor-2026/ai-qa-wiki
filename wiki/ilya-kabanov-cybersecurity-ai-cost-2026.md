---
source: "ilya-kabanov-cybersecurity-ai-cost-2026.md"
ingested: "2026-09-01"
---

## Ilya Kabanov - Cybersecurity Will Get More Expensive (OpenAI Collective Defense)

**Summary**
Ilya Kabanov (TheWeatherReport.ai) dissects OpenAI's call for collective cyber defense: Nasdaq Cybersecurity ETF +7.6%, CrowdStrike +20%, Okta +29% after the letter. 126 signatories, 72% benefit from their own prescriptions (GM only real business footing bill). Four objectives tell buyers to buy and sellers to build/sell more. Seven budget lines will drive growth, with $2.9B in agent-identity acquisitions in 2026 alone.

---

## Seven Budget Lines Driving Growth

1. Application security
2. Agent identity
3. Agent monitoring
4. AI add-ons on every renewal
5. Vulnerability management
6. SOC and incident response
7. Compliance

Agent identity example: $2.9B acquiring agent-identity startups in 2026 - must be recouped via metering/token spend (labs + hardware makers celebrating).

---

## Four Takes (Kabanov)

1. **Pick two:** Letter says AI makes security faster, cheaper, better. You can pick only two, cheaper is not one.
2. **Productivity vs taxpayer burden:** AI promises productivity gains, but higher risks hit energy/water utilities not yet benefiting; beneficiaries ask taxpayers to pay.
3. **5x cost:** Securing AI-written code may cost up to 5x as much as writing it. Curious about overall risk-adjusted return on AI advancements.
4. **Boring hygiene wins:** Basic hygiene remains most effective, but with AI spiral it's unpopular - not making net new money, not presentable at AI-security-vendor conferences. Network segmentation with IT + factory managers is not stage-worthy.

---

## Our analysis (for Victor)

1. **5x securing vs writing maps to Productivity Paradox (Article 16).** Ng/Cherny show generation cheap (388 PRs), Kabanov shows securing that code is 5x. Without external verifier and confirm/dismiss gate, AI generation externalizes cost to SOC/compliance - the same cost curve that stays flat only for teams with user-level tests.

2. **72% signatories benefit = rotting gate risk (Radik).** When sellers define the quality gate they sell, the verifier shares context with the generator. Independent external verifier (state verification, not code inspection) is required, otherwise metric is hacked.

3. **Agent identity $2.9B = new attack surface for QA.** If every agent needs identity/monitoring add-on per renewal, QA must test agent identity lifecycle (provision, rotate, revoke) and monitoring hooks - new budget line = new test surface, not just dev cost.

4. **Basic hygiene as Quality Operating Model (Article 24).** Kabanov's "boring" segmentation aligns with Victor's evidence layer: boring gates (DORA, test pyramid, network boundaries) prevent 80% of incidents cheaper than AI security add-ons. AI security vendor hype vs hygiene is the same as AI-QA vendor hype vs boring mutation matrix.

---

## Cross-links
- [Andrew Ng Loop Engineering](wiki/andrew-ng-loop-engineering-2026.md) — generation cheap, verification bottleneck
- [Boris Cherny Claude Maintains Apps](wiki/boris-cherny-claude-maintains-apps-2026.md) — 388 PRs, 180 merged, tuning cost
- [Radik Zagirov Rotting Gate](wiki/radik-zagirov-rotting-gate-2026.md) — verifier must be external
- [Article 16 - Productivity Paradox](wiki/ai-productivity-paradox-verification-layer-2026.md) — cost curves diverge

---

*Source: Ilya Kabanov LinkedIn (1d) via OpenAI collective defense letter · Ingested 2026-09-01*

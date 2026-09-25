# QualityMax (Ruslan Strazhnyk, Berlin): Independent Verifier Company Profile (2026-09-25)

**Company:** QualityMax (https://qualitymax.io/), Berlin. Founder/CEO/CTO Ruslan Strazhnyk (20y: Deutsche Bank, Quandoo 150M diners, Nuri/Bitwala, startups; Selenium Camp/QS-TAG speaker). AI-native QA platform, 4 layers: UI (AI crawl → Playwright gen → self-heal), API (OpenAPI import), Performance (k6 + trends), Security (Semgrep/Bandit/secrets).
**Services (priced!):** Essentials €6K/1wk (verdict report only: threat model, OWASP LLM Top 10 red-team, supply-chain scan + roadmap); Standard €12K/2wk (+ live evals harness + CI gate); Deep Dive €20K/3wk (+ 3 agent surfaces, EU AI Act note, fix-verification). Dogfoods own codebase; paying customers in production.
**Sources:** qualitymax.io (blog post "Why AI Code Testing Must Be Independent" + about + services, fetched 2026-09-25) + LinkedIn feed post (Europe waiting thesis, 25.09).
**Context:** Strongest vendor-side match to our thesis found so far: adversarial separation (generation vs testing = separate products), hollow-test rejection (deterministic quality gate, no LLM in verdict; tautologies/empty bodies/echo-literals scored, below threshold → regenerate), self-heal as reviewable diffs (locators = opinions rewritable, assertions = facts NEVER touched by machine; human approves), green corpus discipline (retrieve only verified-passing tests), 8-provider routing (6 cloud + 2 self-hosted GPU, circuit breaker), RAG-grounded generation, MCP server + Go CLI agent. Commercial anchor: Track-3 vendor doing paid attestation-shaped work (€6-20K) = pricing existence proof adjacent to our Rupesh framing.
**Captured:** 2026-09-25 from webfetch + user paste.

---

## Thesis overlaps (their words → our language)

- "You can't review your own work" (PR author ≠ approver; auditors independent) = author/examiner separation.
- Locators are opinions, assertions are facts = heal-path vs verdict-path split (cf. CIGE execution-repairable/intent-stable).
- "The moat isn't the model... It's the deterministic guardrail harness" = verdict infrastructure > weights.
- Europe waiting (pilots/committees vs frontier speed; verified speed: measure → reproduce failure → agent proposes → verify independently → expand autonomy on evidence) = staged ramp in vendor words.
- "A pilot is not transformation... waiting is not neutral" = quotable closers.

## Feed post 25.09 (Europe waiting)

- Numbers: US private AI $285.9B (2025) vs UK 5.9 / FR 4.36 / DE 3.89 (Stanford AI Index 2026); EU enterprise AI use 13.5%→20%; EC InvestAI €200B; DK/FI/SE >35% adoption.
- Verified speed 4-step model + article qualitymax.io. Engagement Q (capital/leadership/regulation/talent/pilot-to-production).

## Use for us

- Priced verification engagements (€6-20K) = Track-3 pricing anchor from a second vendor (after Rupesh framing).
- Deterministic-gate + reviewable-diff + green-corpus patterns = implementable controls checklist (cf. Applitools Monkey-Paw gates).
- Self-heal-never-touches-assertions rule = crispest formulation seen; adopt as quoted principle.
- Vendor node: peer/competitor watch (Berlin, paying customers, MCP/Go CLI). No pilot (their product tests customer apps, not a judge API - classification: services+platform, verdict-adjacent).

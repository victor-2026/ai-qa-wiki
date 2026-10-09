# Ursa-Minor Escape Talk — Fact-Pack (W5, 2026-10-09)

Support pack for owner's talk (in a week). Body stays W4 — here only facts, links, consent flags.

## 1. Anchor story (published, quotable)

- Pulse: https://www.linkedin.com/pulse/our-suite-went-green-someone-elses-website-victor-ematin-ijywe/ (verified live 06.10, all four verbatim in article)
- Full text: `Articles/linkedin-posts/Quality-Operating-Model/escape-green-on-wrong-site-FOR-KATYA.md` (Katya version) + `escape-green-on-wrong-site-DRAFT.md`
- Core: BaaS step-executor (Playwright stand, one allowed page = staging login) navigated to the public demo site of the same app family. Prompt said "open the login" with no address; model filled canonical demo URL from training data. No egress rule, no URL allowlist anywhere. Log timed navigateStatus 18:27 UTC, navigation errors ignored. 4/4 SUCCESS against unassigned target; 22 foreign-domain mentions in 6h logs. Caught in analysis, not in real time.
- Post-hardening: fix failed too (wording trick bypassed never-navigate; deterministic-only fell on banned element click; URL grounding never fired — hallucinated address lived upstream of the check). Dispositioned INVALID.
- Persistence: route survived in run memory → deleted, replaced with fresh-session-per-run rule.
- Terms coined: egress / allowlist / Trompe-l'œil run (perfect green vs wrong target).
- Hooks (banked, quotes.md):
  - «Our suite went green on someone else's website.»
  - «Four out of four SUCCESS — against a target we never assigned.»
  - «Memory, it turns out, is another place a boundary has to live.»
  - «Guards are claims until a red team measures them.»
- Adjacent (Jay Aigner, verified 06.10): «AI agents will make every test pass, whether the product works or not.» + Aston Cook «Agents optimize for the pass, not the product.»

## 2. Platform facts (Ursa-Minor-Beta)

- What: open-source agent — picks Jira bug → checks if fixed → posts result back to Jira.
- Stack: Agent Factory studio (agents design/chat) + BaaS Go service (real Chrome, headful) + MongoDB, Dockerized.
- Repos: github.com/Ursa-Minor-Beta/{agent-factory, agent-factory-ui, baas, baas-client} (+ agent-factory-docker-api-ui all-in-one).
- Setup: dev.to/quality_minder (Sep 25), 5-step + smoke test. Needs: GitHub account, OpenAI API key (paid calls), Chrome, Docker, Go, Jira subdomain + auth.
- Status: side project, beta. Shutdown risk after New Year without community support (Katja, meetup #1).
- CONFIRMED 08.10 (owner): Katja Semenova BaaS = Ursa-Minor, one line.

## 3. Katya co-ownership (public, quotable as her words)

- 06.10 reshare (verbatim, typos hers — do NOT correct publicly): "technical but funny story how did our open-sourced bug testing agent run away. Thanks Victor for his patience during the half-night long post-mortem research!" + embedded Escape post. Read: public co-ownership ("our agent").
- Card: `Positions-CV-CL/outreach/active/Ekaterina_Semenova/index.md`

## 4. Consent flags (read before publishing any Katya line)

- Charter SIGNED 06.10 → execution gate OPEN; publication consent GRANTED per charter terms. Ordering on record: Escape article published BEFORE signature (retro-covered).
- Judge doctrine («качество судьи = качество expectation») = PARAPHRASE via W4 relay only, VERBATIM STILL PENDING — do NOT publish until exact line recorded in quotes.md. Consent no longer blocks; precision does.
- Referral door OPEN 06.10 (owner): conversations via Katya's recommendation accepted.

## 5. Meetup links

- #2 (25.09, Henock + Ursa demo): https://www.meetup.com/quality-minded/events/316661276/ — artifacts in Katya card: recording https://lnkd.in/dPsY95n5, notes https://lnkd.in/d34H-xTg, adoption https://lnkd.in/d6q6uUm2, GitHub https://lnkd.in/d57y8dkR, feedback https://lnkd.in/d7NPgV4X
- #3 (TODAY 09.10, 17:00-18:30 CEST): self-learning agent + Agent Factory news + Chizhkoff Rho Metric. RSVP lnkd.in/eUKD9gmi
- Community: https://www.meetup.com/quality-minded (biweekly). Contact ekaterina.tuna.v@gmail.com
- Wiki: `wiki/quality-minded-first-meetup-2026.md` (covers #1 Sep 11; #2/#3 not yet in wiki)

## 6. Open items for W4 (not decided here)

- Katya judge-doctrine verbatim line (request it) — blocks that quote only, nothing else.
- #2/#3 wiki coverage — on demand, not started.
- Henock thread (returned 09.10, repo intent re-confirmed) — separate track, no talk impact.

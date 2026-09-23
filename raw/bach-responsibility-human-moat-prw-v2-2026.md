# Responsibility is the Human Moat — Principles of Responsible Work v2.0 (Satisfice, 2026-05-20)

**Author:** James Bach, Jon Bach, Michael Bolton
**Source:** https://www.satisfice.com/blog/archives/488082
**Context:** Satisfice blog. v2.0 of Principles of Responsible Work (updated 5/20/26). Grounded in research on AI-related hazards. Download: https://www.satisfice.com/responsible. Digest/source-triage candidate.

---
**AI cannot behave responsibly. Only natural persons can.** Humans have a "moat" around them that no AI can cross — AI can pretend to be part of society, interact with it, but cannot actually be a part of it. Legal standing is the core: the author dropped out of high school at 16 and became a videogame programmer; his employer's problem was that *a 16-year-old cannot enter into a binding contract*, solved by becoming an "emancipated minor". There is no such legal status for an AI tool.

"Whatever services define a business, there is a necessary web of responsibilities required to make those services safe and reliable... disclaiming all responsibility also makes business impossible."

## Principles of Responsible Work (v2.0)

1. Every non-trivial business comprises services that enable it to function; they must be sufficiently reliable or the business collapses.
2. Every service entails risk of failure; the business must recognize failures and recover. In regulated industries, risk management may be subject to process mandates.
3. A "responsible person" is a natural person reasonably competent, prepared, and accountable for some service. Neither a child nor a tool (such as AI) has the capacity (legally or socially) to bear responsibility.
4. A "responsible service" is performed in good faith by a responsible person: interpreting/following procedures, improving skills, anticipating problems, reporting to authorities/clients.
5. Responsible services may incorporate any tool, as long as the person can operate it safely, legally, with reasonable efficiency. Operator effort/skill scales with tool cost, complexity, obscurity of output, output volume per time, reliability. Operator must anticipate outages and breakdowns.
6. Responsibility can be taken, shared, declined, or delegated, as long as there is a clear and reasonable protocol; otherwise the business is vulnerable to negligence/breach-of-contract accusations.
7. Therefore businesses must maintain clear lines of responsibility, assure competence/readiness of responsible persons, put reliable tools in place, and maintain oversight of delegated responsibility.

## Responsible Operation of AI

1. **AI cannot bear responsibility** — not a responsible person, meaningless to speak of a tool operating in "good faith"; cannot provide a responsible service nor have responsibility delegated to it.
2. **An "AI agent" is always a tool operated by a natural person**, irrespective of whether the person is monitoring in real time.
3. **Thus the operator always bears responsibility for the behavior of that agent**, including anticipating outages, token rationing, poor performance.
4. The responsible operator must assure adequate quality; **they cannot merely prompt and pray.** Therefore the operator must:
5. be sufficiently skilled in use of the tool;
6. be sufficiently prepared to operate the tool in that context;
7. be sufficiently alert to risks, anomalies, defects in the work;
8. reasonably anticipate restrictions or interruptions of dependent services;
9. **feel empowered (and actually have the power) to reject or remediate any AI work** — otherwise the operator becomes a scapegoat, a "moral crumple zone";
10. avoid or mitigate the special hazards of AI operation.

## Special Hazards of AI Operation

**Technological:** Service Outage (frontier models not locally available); Service Adulteration (degradation vs reasonable expectation: model drift, context drift, model poisoning, model collapse, inadequate performance).

**Interactional (cognitive hazards):**
- **Cognitive Overload** — too much/too complex/too fast output; poor supervision, unnoticed mistakes, chronic stress, cognitive debt, cognitive surrender.
- **Cognitive Debt** — AI produces faster than operator can study; when backlog of learning grows, supervision collapses; worker stops feeling the work is "theirs" though no one else is accountable.
- **Cognitive Atrophy** — operator loses ability to judge the work from lack of regular practice (Ironies of Automation, Bainbridge 1983).
- **Cognitive Surrender** — operators cease critical thinking; passive acceptance; "complete abdication of responsibility".
- **Anthropomorphism / Anthropomorphizing** — treating AI as human; behavior consistent with a reasonable adult for reasons unrelated to human motivation; not predictive across contexts; leads to parasocial relationships and unjustified trust (Financial Over-Attribution Error).
- **Automation Bias** — trusting machine output over own judgment even facing clear evidence of malfunction.
- **Chronic Stress** — supervising/training/testing/collaborating leads to burnout, turnover, counterproductive behavior.

**Managerial:** Data Negligence; Reckless Spending (unpredictable AI-as-service costs, token budgets); Violations of Law (EU AI Act etc.); **Moral Crumple Zone** (system failure routinely carelessly blamed on the human — self-driving safety driver, ordinary "scapegoat" ChatGPT user); Business Disruption (loss of tacit/tribal knowledge, devaluation of craftsmanship, demoralization, perverse incentives, disruption of the human experiential learning pipeline).

## Discussion

**The Quality of AI is Not the Central Issue; the Central Issue is Responsibility.** Human oversight / "human-in-the-loop" are not merely techniques for unreliable AI — they are foundational requirements for ethical business practice *even with highly reliable AI*. Framing GenAI adoption as a quality question is the wrong frame (like choosing an absolute monarchy because the cost of living is low). "Can is not will" — the Space Shuttle *could* put satellites in orbit but no longer does because risks/costs outweighed benefits. GenAI benefits cannot be rationally considered without investigating its failures, which requires extensive (often prohibitively expensive) testing; adoption is happening in a frantic atmosphere discouraging close inspection.

Three moral hazards: (1) GenAI designed to operate as if it had agency/standing, yet cannot suffer consequences → reckless behavior insulated from consequences; (2) humans hide behind AI as an accountability sink (e.g. biased loan-decider claiming "shocked" at the bias); (3) the **AI Productivity Paradox** — "For many tasks it takes considerable time and effort to use AI responsibly. Yet for AI to be productive, it must save time and effort. Therefore, to maximize perceived AI productivity, we will be rewarded for using AI irresponsibly." Both managers and workers can point at each other as root cause while excusing themselves.

**It can be okay to use an irresponsible service** (e.g. ChatGPT — OpenAI expressly disclaims responsibility; new EU product liability directive 2024/2853 prevents disclaiming all warranties with consumers). As an employee you still bear responsibility for your own work — "you must be ready to stand by it."

Out of scope: broader fairness/sustainability principles; transparency/disclosure of AI use is NOT a hard requirement (people use tools; unless you cannot assure adequate quality, then warn the client).

QA relevance: the operator-responsibility and objection/attestation principles (rule 9: power to reject = the attestor role) map to Mutation Matrix "human gate", Article 27 (accountable human; QA role not removed), Article 21 (Conway/ownership), the AI Productivity Paradox connects to verification-first economics. Strongest single external authority for the "responsible human behind the agent" thesis.
# AI Productivity Paradox + Verification Layer (Pavel Shcherbinin posts)

Source: LinkedIn posts by Pavel Shcherbinin (CTO Yandex, ex-VP Eng SberMarket, ex-CTO TripleTen/Insolar; Belgrade, Serbia), ~2026-07..08. URL: linkedin.com/in/pavel-shcherbinin (500+ connections, 5,247 followers).

Post 1: "Will AI replace us all?" (1mo)
Post 4: "Block spent two years converting its engineering org to AI agents" (1mo)
Post 6: "AI Productivity Paradox" (1mo)

---

## Post 1: Will AI replace us all? (middle loop)

- Annie Vella (Distinguished Engineer, Westpac) — six-month longitudinal study, engineers from 28 countries.
- 82% now spend less time writing code. Not "a bit less" - most nearly stopped.
- The freed-up time does NOT move into architecture (design shrank too). It went into **checking**.
- New work layer: the **middle loop**.
  - Inner loop: write, build, run, fix (polished by IDEs and TDD).
  - Outer loop: commit, review, deploy, monitor (optimized by DevOps).
  - Middle loop: supervising an agent. Three tasks:
    1. **Directing** - say what you want, context and boundaries, standards baked into agent instructions.
    2. **Evaluating** - read what it produced, decide: accept, rewrite, throw away.
    3. **Correcting** - fix and integrate so nothing drifts across the codebase.
- AI code is dangerous because it is plausible: compiles, runs, produces output - logic error sits three commits deep.
- Paradox from same study: 84% report higher productivity, yet share of people whose experience got worse nearly doubled in 6 months: 14% -> 27%. "We do more and enjoy it less."
- Advice: (1) **Specs are the new code** - AWS compressed a two-week feature to two days with Kiro because the spec was precise. "The defining bug of 2026 isn't broken code - it's correct code built from a broken spec." (2) **Build the harness** - Agent = Model + Harness, production reliability ~90% comes from the harness, not the model.
- Question: "Which one are you becoming - a writer, or a curator?"

## Post 4: Block / Angie Jones (AI Engineer World's Fair)

- Block spent two years converting engineering org to AI agents. Angie Jones shared numbers.
- Paradox: within a couple of months 90% of engineers used agents regularly, yet CEO was convinced engineering wasn't using AI at all (features weren't reaching customers faster).
- She built a **maturity model that measures the engineer, not the agent** (0-5):
  - 0 - no AI at all
  - 1 - AI as autocomplete
  - 2 - chats with an agent, but writes code and PRs themselves
  - 3 - delegates tasks to an agent and reviews the output
  - 4 - runs several agents in parallel
  - 5 - hands over a complete task and gets a shippable result
- Almost the entire org sat at stage 1 or 2.
- Getting to stage 3 took champions, not mass training. **1/9/90 rule**: 1% create, 9% engage, 90% consume. ~50 engineers got a third of their work time, made repositories agent-ready: agents.md, rules files, mandatory AI reviewer. Delegation moved to where work is born: bug spotted in Slack - agent proposes fixes, team picks one, PR lands in 5 minutes.
- Three months in: AI-authored code **+69%**, automated PRs **21x**.
- Stage 4 breaks code review first: PR volume multiplies, human reviewers can't keep up. Fix: mandatory AI reviewer + auto-fix loop (one agent finds the problem, another repairs it).
- Stage 5 required a model of the organization, not another tool: **Builder Bot** orchestrator with a map of all 25,000 company repositories - without it an agent writes a local patch but can't plan a change across several systems.
- Ending: "This felt like a dream. Until it became a nightmare." In February, Block cut 4,000 people - nearly 40% of staff - on the day it reported the best quarter in its history. Jack Dorsey: intelligence tools plus smaller, flatter teams are a new way of working. Skeptics: Block over-hired during COVID. Open questions remain.

## Post 6: AI Productivity Paradox

- MIT and Wharton data: agents write **seven times more code** - for a **twenty percent** gain in releases.
- GitLab: 78% of developers say they code faster, while 79% admit delivery hasn't sped up.
- 4 causes:
  1. **Writing code was never the bottleneck** - roughly a third of the way to production. Rest (review, testing, integration, deployment, support) needs as many people as always. Fred Brooks: no silver bullet.
  2. **The pipeline after the code wasn't built for this volume** - review and QA were designed around human speed. PRs sit in review several times longer, more code merged with no review at all, post-deploy incidents multiplied. Every third team admits they're afraid to ship AI-written code to production.
  3. **The feeling of speed is deceiving** - METR controlled experiment: experienced developers were sure AI sped them up by 20%, measurement showed they were 19% slower.
  4. **Comprehension debt piles up** - code merged, tests green, three days later nobody can explain how it works.
- Takeaway for leaders: writing code became almost free, everything after it - understanding, verifying, shipping, maintaining - became more expensive.
- 3 directions: (1) **spec-driven development** (acceptance criteria, how to verify, what's off-limits; a bad spec produces wrong code faster); (2) **Domain-Driven Design** (clear boundaries = several times cheaper to verify; cluttered codebase -> model copies tech debt as pattern - "generative debt"); (3) **supervisory engineering** (engineer's job shifts from writing to supervising: give the agent a task, inspect the result, step in at the right moment; no line in most career ladders, yet it now determines how much a team ships).

---

## Why this matters for QA (analysis notes)

- The "checking"/verification layer (middle loop) = QA leadership's new territory: Directing + Evaluating + Correcting is literally test strategy, review gates, and quality ownership for agent-produced code.
- 21x automated PRs: the review pipeline breaks FIRST - that's a QA problem as much as engineering.
- "assert a string instead of behavior" - anti-overfit: mutation testing catches agent-written tests that check implementation details; matches Meta ACH anti-overfit pattern and JiTTest.
- 0-5 maturity scale (Angie Jones) parallels Alex Barady's L1-L5 AI Engineering Maturity Model - compare in one table.
- Block's layoffs (~40%) = the dark side; QA has a role in making agent orgs accountable (evidence, gates, metrics).
- Harness = Agent + Harness (Google whitepaper, ~90% from harness) - QA builds the harness gates: tests, linters, gates, instructions, quality gates, regression advice on PRs.
- Numbers for articles/interviews: 82%, 84%, 14->27%, 7x code / +20% releases, 78%/79% GitLab, METR 19% slower, +69% AI-authored, 21x PRs, 25,000 repos, 4,000 people / ~40%, 1/9/90, 0-5 scale, 5-min PR, Kiro 2 weeks -> 2 days.
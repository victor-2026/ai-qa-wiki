# Alternate QA: Test Automation Architect Simulator + Paul Kanaris Thread (LinkedIn, 2026-09-23)

**Source:** LinkedIn company page post (Alternate QA, 8 followers, posted ~3h before capture 2026-09-23) + comment thread. Pasted by user verbatim; no external fetch (LinkedIn auth wall).
**Context:** SECOND artifact from Alternate QA org (first: FlowScout crawler + Kanaris "undiscovered vs uncovered" thread ingested 2026-09-22). This one is a management SIMULATOR game for test automation architects, idea credited to Bas Dijkstra. Same commentator (Paul Kanaris, QACE Institute, The Umbrella Playbook) with a DIFFERENT thesis: constraints live OUTSIDE automation practice. Verdict: related, not a duplicate - new artifact + new argument. Cross-links: flowscout thread, Bas Dijkstra pages.
**Captured:** 2026-09-23 from user paste.

---

## Post (Alternate QA, company page)

What is it actually like to be a test automation architect?

Not the theory, the job: a team tells you their automation is in decent shape, and you have to decide what to believe.

We're building a simulator for exactly that. You run one company for six virtual quarters. The team's self-report is optimistic, and verifying it takes weeks you could spend fixing something. Fund a remediation on an unchecked assumption and it can hit a blocker you never saw coming. A sponsor's trust rises or falls on whether you close their gap on time. In the end, you see where the truth actually was.

This started with an idea from Bas Dijkstra. Thank you, Bas!

Try it out via the link in the comments.

P.S. This is an early version of the sim. Feedback is appreciated.

## Comment — Paul Kanaris (Founder & Architect, QACE Institute; Author of The Umbrella Playbook)

Interesting concept. One observation from my experience is that the most significant constraints to quality and automation maturity often originate outside the automation practice itself. Requirements quality, product understanding, business-rule clarity, organizational incentives, architecture decisions, delivery pressure, and culture frequently have a greater impact on outcomes than the automation framework or tooling. Early in my career I considered myself a QA architect who knew how to automate rather than an automation architect. The automation challenges were usually visible. Understanding why the organization arrived there was often the harder problem. Sometimes the largest bottleneck isn't the test suite, it's the conditions surrounding the teams expected to use it. I like the idea of distinguishing between what is believed and what is confirmed. In many organizations, that same distinction applies to far more than automation.

## Reply — Alternate QA (author)

Paul Kanaris Thank you, really valuable perspective! "QA architect who knew how to automate" is a great way to put it. Root causes sitting outside the automation practice (requirements, incentives, culture) are lightly covered in the simulator today, so this is going straight onto my list for the next iteration.

---

## Use for us

- Believed-vs-confirmed as a GAME mechanic maps directly to our evidence doctrine (claims vs verified verdicts); sponsor-trust-on-closed-gaps = attestation economics in miniature.
- Kanaris thesis ("conditions surrounding the teams") is the org-level analog of per-risk-tier thinking: the bottleneck is rarely the suite.
- Simulator as a FORMAT idea: mutation-matrix concepts (seeded doubt, verification cost, blocker on unchecked assumption) could be taught the same way.
- Watch: early version, company page with 8 followers - track next iteration for the "outside practice" coverage they promised.

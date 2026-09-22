# FlowScout Thread — Igor Akymenko + Paul Kanaris exchange (LinkedIn, 2026-09-22)

**Source capturado:** LinkedIn thread, Igor Akymenko (Quality Architect | Director of QE | Head of Quality Engineering, Fellow of Alternate QA, Founder FlowScout). Posted ~3 days before capture. Repr aired by Paul Kanaris (QACE Institute). URL: https://www.linkedin.com/feed/update/urn:li:activity:... (post + comments).

**Why in wiki:** honest-QA-tools thesis (report what you verifiably found, never invent expected results), "undiscovered vs uncovered behavior" dichotomy (Kanaris), genuine unsolved residue (multi-actor handoffs, irreversible transitions, time-dependent flows). Direct hit for Articles 26-28 (silent false negative, VerdictGate, mutation-matrix discovery/verification gap). FlowScout = live example companion to Bolton/Bach sober-literal hygiene.

## Post (Igor Akymenko, ~2-3d)

Most "AI testing" tools ask you to trust them. I built one that shows its work instead.

For the past few months, I've been building FlowScout - an autonomous browser agent that crawls your web app with Playwright, discovers the real user flows that actually exist (not the ones your docs assume), and tells you which of your existing test cases - from TestRail, Zephyr, Xray, qTest, or a plain CSV - actually cover them.

The part I care about most: FlowScout never invents an expected result and never asserts anything about data correctness. It only reports what it can verify by actually clicking through the app - which flows exist, which are covered, which aren't. That's a narrower promise than "AI writes your tests for you." I think it's a more honest one.

What it actually does:
- Crawls with real risk classification - destructive actions (logout, external links) are never touched; mutating ones (checkout, delete) only run if you opt in
- Three-way dedup, so you get real flows instead of 40 near-identical ones
- Gap analysis against your real test plan, plus generated test-case drafts and runnable pytest-playwright specs
- Multi-persona crawling, change tracking across runs, resumable flows, seeding from sitemap.xml for pages nothing links to
- Recognizes CAPTCHA/challenge pages and reports them honestly instead of pretending they're ordinary content - it never tries to solve or bypass one

It's open source (Apache-2.0) and genuinely still in progress - every feature gets verified against real, live sites before I call it done.

Here's the ask: if you work in QA, test automation, or just own a web app you're tired of manually re-testing, try pointing FlowScout at it (a staging environment or demo site is perfect) and tell me what breaks, what it misses, or what would actually make it useful for your workflow. Coverage gaps it finds, weird crawl behavior, a feature that's missing - I'd to hear all of it.

Repo: https://github.com/igorakymenko-create/FlowScout (Apache-2.0).

## Comment 1 — Paul Kanaris (QACE Institute, The Umbrella Playbook)

The idea is interesting, but I keep coming back to a different challenge. How do we know the discovered flows represent the complete picture?

In many enterprise systems, workflows are influenced by permissions, configurations, customer-specific customizations, integrations, feature flags, data conditions, historical decisions, and business processes that are not obvious from simple navigation paths.

If a workflow transition is missed, a customization introduces new behavior, or an undocumented process only appears under specific conditions, the resulting coverage analysis may look complete while still missing important parts of the system.

That doesn't reduce the value of discovering flows. It does raise an important question: **How do we distinguish between undiscovered behavior and uncovered behavior?**

In my experience, some of the highest-risk workflows are often the least documented, least understood, and least visible to automated discovery approaches. Finding flows is valuable. Understanding whether you've found the important ones is where the harder problem begins.

## Reply 1 — Igor Akymenko

Paul Kanaris Fair challenge, but I'd push back on most of that list - not because the concern is wrong, but because it's more answerable than it looks.

FlowScout's claim isn't "we found everything the system can do." It's narrower and precise: **"here is what this identity could reach, in this system state."** That's a checkable statement with a defined boundary, not a hopeful one.

Run it as a user with restricted permissions, and you'll see restricted flows - correctly. Give it the role you actually want covered, and it walks that surface. A feature flag that's off definitionally means "this doesn't exist for this user"; reporting it as absent is right, not blind. Customer-specific customization is arguably where crawling beats spec-derived test design outright - the crawler reads the UI that's actually deployed, not the one the documentation describes. Data conditions are a stand-up-the-fixture problem, same as they've always been.

So for most of that list, the honest answer isn't "we can't know" - it's "that's an access and environment-setup question, and it has a precise answer: provide the conditions you want covered."

## Reply 2 — Igor Akymenko (genuine residue)

Two things I do think are real, and that I'm building now:
- A run's conditions have to be visible in the report itself - which persona, which config, which seeded URLs, which limits. A not_found is always relative to those; if the report doesn't say so on its face, it reads as more absolute than it is.
- Change detection has to be scoped to a configuration. Comparing a run against customer A with a run against customer B is worse than useless, even from the same entry point.

And here's where I think the real residue is - narrower than your list, but harder, and not fixable by handing out permissions:

1. **Multi-actor handoffs.** Employee submits -> manager approves -> employee sees the result. Personas crawl sequentially and independently; there's no coordinated handoff between them. One super-user can't reproduce it, because the flow needs two actors in sequence.
2. **One-shot, irreversible transitions.** The whole architecture is reset-and-replay. "Activate account", "consume this token", "final approval" can't be re-walked against the same backend entity.
3. **Time-dependent flows.** Anything behind a scheduler or a 30-day wait.

Those are the ones I'd call genuinely unsolved. Appreciate the push - it moved two things onto the build list.

## Comment 2 — Sarang U. (Senior QA Engineer, Thinkproject; premium profile)

Great direction for AI-powered QA. The focus on verifiable coverage rather than blindly generating tests.

## Comment 3 — Sarang U. (real-world finding)

Tried this out today, hit a few environment snags getting set up (a stale DNS cache, an editable-install quirk), but once past that, pointed it at my own portfolio site and it actually caught something real: a full-page overlay from a fade-in animation with pointer events: auto left on, silently sitting on top of my nav links and blocking clicks that should've gone through. Not a fake finding either - reproduced it by hand, the topmost element at the link's click point genuinely wasn't the link.

That's exactly the kind of "show its work" honesty the pitch promises - it didn't invent a bug, it found a real one and told me precisely why. Great start, will keep testing against a bigger app.

## Reply 3 — Igor Akymenko (to Sarang)

Would you mind sharing the exact error/output from the DNS cache and editable-install issues? Environment setup friction is worth fixing properly, not guessing at it; happy to patch the docs (or the code, if it's actually a bug) once I know precisely what you hit.
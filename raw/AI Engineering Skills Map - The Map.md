# The AI Engineering Skills Map

**Author:** Andrew Ng (DeepLearning.AI, AI Fund, AI Aspire)
**Source:** https://www.linkedin.com/pulse/ai-engineering-skills-map-andrew-ng-m479c
**Date:** August 14, 2026 (13,884 reactions, 416 comments at fetch)
**Fetched:** 2026-09-04 (full text via webfetch)

---

I am delighted to present The AI Engineering Skills Map. AI allows us to build software very differently today than in 2022.

Method: analysis of over 10,000 job postings; dozens of structured interviews with AI experts, hiring managers, recruiters; surveys; other online data. Informally akin to clustering massive dataset to identify most important skills, now and near future.

Terminology: "AI Engineering skills" (broad, all developers) rather than "AI Engineer" role — like cloud: all devs need cloud skills, few have Cloud engineer title.

Four most important AI engineering skills (top level):

1. **Building and deploying AI applications.** Key difference: unpredictable outputs (LLM prompt → unknown; training → unknown predictions on new examples). Understand building blocks (LLMs, context engineering, RAG, agentic workflows, ML/DL) + statistical techniques to measure, steer, govern for predictability. Core: disciplined evals and error analysis loops.

2. **Software engineering fundamentals.** Deeply understand how software works → tradeoffs cost/scalability/reliability/speed + security/privacy. Recognize what tradeoffs exist → stack choice, architecture, data store, testing. Inexperienced vibe coder doesn't know tradeoffs exist → agent makes poor ones (no context to steer).

3. **Using coding agents.** Mental model of how agents work, limitations, workarounds, steer quickly — how much to intervene vs leave alone — build robustly without wasting time/tokens. Manage context, planning vs execution tradeoffs, verifiers/evals to close loops, clear spec (and when not to bother), multi-agent orchestration, avoid pitfalls (agent messing up production DB). Evolving quickly → routines to try new tools, evolve workflows.

4. **Shaping the build.** Given clear spec, agents rapidly improve at delivering. Work shifts to deciding spec content: product sense, business context, customer goals → participate in shaping/driving build. Greater ownership/agency: identify problems/opportunities, execute responsibly; know when to MVP fast vs build carefully.

Underlying all: mindset of continuous learning (AI changes fast).

DeepLearning.AI focus: help developers gain these skills. More posts flesh out each skill + detailed map.

Notable comments: Jafar K V (map shows what to learn first); Mohib Ahmad (eval-driven development + context orchestration = where production fails; regression suites as dividing line); yosra harb (system design around model — evaluation, tool boundaries, observability, recovery, human oversight — beats prompt tuning); Musarraf Hossain ("using coding agents" hardest to teach — judgment on when to trust vs check); Edgar Hernández (model cascades per task cut inference cost more than prompt tuning).

Series: (1) this map → (2) Building/Deploying gyn5e Aug 21 → (3) Fundamentals 7lnac Aug 28 → (4) Coding agents h8yxc Sep 4.

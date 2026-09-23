# So, You "10x'd" Your Work... (Satisfice, 2026-02-08)

**Author:** James Bach
**Source:** https://www.satisfice.com/blog/archives/488009
**Context:** Satisfice blog. Response to the "10x productivity with AI" meme. Categories: AI and Testing, Management, Testing Culture.

---
A naive way to assess wow-factor productivity claims: accept at face value. A skeptical way: 8-question inquiry for claims like "we 10x'd testing with AI".

1. **What exactly did you change?** The change may be trivial and easily replicable — or you may have gotten lucky, or your situation may be special.
2. **How did you measure it?** Maybe the baseline was unrealistically poor — prep work, garbage-config, someone who'd never used the tool — which you improved on. Little data, sampling problems, inattention to side-effects.
3. **Are we measuring anything real?** Fixing a broken process is not the same as 10x'ing it. Algorithmic improvements can compound unpredictably.
4. **What did you sacrifice?** Time now vs later (technical debt); testability; safety; skills of people ("temporarily" borrowing other people's competence); morale.
5. **Did anyone test your claim?** Are you a reliable source? Does the claim survive independent scrutiny?
6. **What was the gross vs net effect?** New costs: tools, licenses, compute, prompt-engineering, skepticism/verification, cleanup of AI slop.
7. **How many was it affecting the work?** "100x" is irrelevant if a few people do a small task. Number of people affected by the change matters.
8. **Will the new method work next time?** Different data, different problems, different goal — AI may excel at one task but be a regression elsewhere ("motivating 10x claims ignore the many ways AI can be a regression").

**"AI does not necessarily make you more productive. AI makes you able to produce."** Produce more attempts, more garbage, more options. "In six months, I have generated... probably millions of tokens" — trying is the work. Sometimes trying is 90% of the job; sometimes it is not worth it. AI productivity is about optimizing the whole loop (judgment included), not output rate.

Slack-channel meme ("we 10x'd testing with AI") inspired this post. Conclusion: be an evidence-based buyer — run the 8-question filter before taking any "10x" claim at face value. This is the testing-minded response to the AI hype cycle.

QA relevance: the skeptical inquiry is the anti-slop reviewer of vendor/metrics claims (Article 26 evaluation, verification-first); "produce, not necessarily productive" = the false-positive generation trap; question 8 = AI regression across contexts (Mutation Matrix context-dependence).
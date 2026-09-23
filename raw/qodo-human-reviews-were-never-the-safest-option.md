# Qodo: Human reviews were never the safest option (2026-09-23)

**Source:** https://www.qodo.ai/blog/human-reviews-were-never-the-safest-option/
**Context:** Qodo (ex-Codium) = AI code quality & governance platform. TIER 2 catalog FULL READ. Note: FULL READ - evidence. Fetched 2026-09-23 with browser UA.

---

Mark Zuckerberg is back to landing diffs at Meta. Twenty years after he last shipped code, he’s using Claude Code to write and submit changes to Meta’s codebase. Gergely Orosz
covered this story
in his latest newsletter issue and it tells an interesting story about human review and AI.
Around 200 engineers approved Zuckerberg’s diff. This is what you might call
approval inflation
: the reviews getting rubber-stamped not because the code is good, but because of who submitted it.
It’s questionable how many of those 200 reviewers actually reviewed the code. There’s a chance that few, if any, may have flagged an issue even if they found one. If someone did spot a bug in the CEO’s code, it’s unlikely they’d be the one to block it or have their voice heard in the noise.
During a time when there are rising concerns about AI-generated code, this story paints an interesting picture of how code reviews are being done. You’d think that more scrutiny would be applied to the CEO’s code, after all – he wrote it using Claude Code. But it seems that what happened is the exact opposite.
We’ve always had this problem
The logic behind code reviews makes intuitive sense. To ensure quality, don’t rely on a single developer’s judgment. Instead, have multiple people look at the changes and review them. More people looking at the changes reduces the risk of a disaster. There are many companies that require two or more approvals before releasing to production. And these measures are genuinely good.
But they only work when people actually review the code. Besides the mentioned authority bias, there are other issues that can arise, such as:
Approval inflation
– “everyone else approved, so it must be fine”
Alert fatigue
– “nothing bad happened last time, so it should be fine this time”
Social pressure
– nobody wants to be the person who blocks a release
Time pressure
– “we need to ship this fast”
Technical debt
– “we’ll fix it later”
Overloading
– “I have too many PRs to review”
These don’t make the human review bad, but it’s fair to say that a risk of mistakes increases with intensity and frequency of these issues. The problem nowadays is that AI coding tools have increased development output by 25–35% and the review and verification processes haven’t kept pace. There are many reasons for concerns about quality overall.
The Challenger-level disaster
One of these concerns was voiced by Simon Willison in a recent interview on
Lenny’s podcast
. He said that he sees a “Challenger-level disaster” happening in the age of AI. He referenced a paper that came out of Challenger’s disaster investigation called
normalization of deviance
– the gradual acceptance of known failures because they haven’t caused a catastrophe yet. Each time something works fine despite the risk, the risk feels more acceptable.
It’s an interesting analogy, because normalization of deviance is exactly what’s happening with AI-generated code. Each time AI produces working code, we trust it a little more. Each time a quick review reveals no issues, we skim a little faster next time. The risk doesn’t disappear, we just stop seeing it.
But if you look at
the full story
, the Challenger disaster didn’t happen solely because of a technology failure. The bigger part of the problem was human bias – known risks were normalized over years of “safe” launches, authority overrode engineering expertise, social pressure silenced dissent, and critical information never reached decision-makers. Engineers recommended against the launch, but they were overruled by a higher authority.
The real risk isn’t imperfect technology or human bias, but a combination of both. The engineering flaw on the Challenger space shuttle was known. That alone wouldn’t have caused a catastrophe. It took human biases on top of the technical problem to turn a manageable risk into one. The same applies to AI-generated code: imperfect output is expected. The disaster comes when the people reviewing the code are affected by the same biases.
Code governance as the answer
The nature of
AI generated code
is to be imperfect, which makes the pressure on quality control even higher. We’ve seen this happen with companies like Atlassian, where AI adoption led to an
89% jump in PRs per engineer
. The volume is outpacing human capacity. This invites re-thinking the approach to quality gates and code governance.
AI code review
solves some of the problems mentioned above, by making review systematic and enforceable. Traditional review relies on a human looking at a diff, leaving comments, and approving or requesting changes. The merge decision depends on one person’s judgment on that particular day.
Specialized AI agents each focus on their own specific concern – correctness, security, cross-repo impact, test coverage, policy compliance. They produce consistent enforceable checks that integrate into branch protection rules.
This addresses the biases mentioned earlier. Approval inflation disappears when the verdict comes from an automated check, not a crowd of approvers. Alert fatigue loses its grip when every PR is evaluated with the same rigor regardless of history. Social pressure becomes irrelevant – an automated security check doesn’t care if the author is the CEO or a junior developer. Time pressure can’t shortcut a governance rule the way it can rush a human reviewer. And overloading stops being a factor when the system scales with the volume of PRs, not with the number of available reviewers.
Instead of asking “did someone look at this?” the question becomes “does this meet our defined standards?” The review is versioned, auditable, and consistent regardless of who submitted the code or what time of day it is.
Human judgement still matters
The Challenger example showed how flawed technology combined with a flawed human system creates costly errors.
AI code review
addresses both sides of that equation. It catches technical issues that humans miss, and it removes the human biases that prevent those issues from being acted on.
But AI code review isn’t about removing humans from the process. It’s about moving them to where they actually add value and use the help of AI where they tend to fall short. Humans are excellent at making design decisions, understanding business context, mentoring through review feedback, and recognizing when something “feels off” even without a specific rule.
On the other hand, humans are not great at consistently enforcing coding standards across hundreds of PRs, catching security vulnerabilities in code they’re reviewing at 4pm on a Friday, resisting social pressure to approve the CEO’s diff, or maintaining the same attention to detail on PR #47 of the day as on PR #1.
AI code generation isn’t introducing a new problem. It’s scaling an existing one. More code, more PRs, more pressure to ship fast. The answer isn’t to double down on human review and hope people resist the same biases they’ve always been susceptible to. The answer is to build governance systems that enforce standards regardless of who wrote the code or who’s reviewing it.
The Challenger engineers knew there were problems with the launch. Two hundred Meta engineers approved Zuckerberg’s code. Human review was never the safest option. It was just the only option we had.
Now we can build systems that don’t rely on hope.


**Source:** [Gist by rossdm](https://gist.github.com/rossdm/080959eb58a5f72bcc297925b0a5be36)
**Author:** rossdm
**Date:** 2026-04-05

---

### background

the (known) [origins](https://addyo.substack.com/i/185933546/comprehension-debt-a-hidden-cost-we-dont-track "https://addyo.substack.com/i/185933546/comprehension-debt-a-hidden-cost-we-dont-track") of the term "comprehension debt"

> [Jeremy Twei](https://x.com/jeremytwei/status/2015886793955229705 "https://x.com/jeremytwei/status/2015886793955229705") coined the perfect term for this: _comprehension debt_. It’s certainly tempting to just move on when the LLM one-shotted something that seems to work. This is the insidious part. The agent doesn’t get tired. It will sprint through implementation after implementation with unwavering confidence. The code looks plausible. The tests pass (or seem to). You’re under pressure to ship. You move on.

### symptoms

- volume & verbosity inflation; PRs grow in size, making diffs harder to review & reason about.
    
- shift from “author knows” to “author curated”; folks merge code they _steered_ but didn’t fully internalize - particularly when delivery pressure is high.
    
- PR reviews trend towards “syntax checking” over “model checking”; reviewers fail to grasp deep system invariants/regressions while spending time on surface-level issues.
    
- context rot; long agentic runs accumulate contradictory approaches which confuses author & reviewers.
    
- weak ownership; if “who understands this end-to-end” isn’t explicit, everyone assumes someone else does.
    

### approach to mitigate

- robust PR reviews; reviewers follow conventional commits. Authors structure changes into atomic commits & stacked PRs. Complex PRs include analysis docs summarizing the nature of the effort. We expect that reviews may take time.
    
- AI-augmented review; we use LLMs to outline module hierarchies, suggest refactors, and verify assumptions when reading other contributors' code.
    
- quick feedback loops; we invest in ensuring that we are able to have automated validation of business logic & outcomes.
    
- ownership; we expect team members to be able to articulate their work and ship in reviewable chunks.
    
- metrics; as necessary, track _review iteration rate_, _follow-up PRs per PR, Revert rate / hot fixes per PR/epic_.
    

---

### related reading

>  We find that AI use impairs conceptual understanding, code reading, and debugging abilities, without delivering significant efficiency gains on average.

- ["How AI impacts skill formation"](https://arxiv.org/html/2601.20245v1)
    

> Over time, overwork can impair judgment, increase the likelihood of errors, and make it harder for organizations to distinguish genuine productivity gains from unsustainable intensity.

- [AI Doesn’t Reduce Work—It Intensifies It](https://hbr.org/2026/02/ai-doesnt-reduce-work-it-intensifies-it)
    

> The fundamental challenge is that **organizations cannot optimize for what they cannot measure**. Velocity is measurable. Comprehension is not, or at least not through any mechanism that currently feeds into performance evaluation, promotion decisions, or headcount planning.

- [Cognitive Debt: When Velocity Exceeds Comprehension | rockoder](https://www.rockoder.com/beyondthecode/cognitive-debt-when-velocity-exceeds-comprehension/)
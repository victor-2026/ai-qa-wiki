# CodeScene: Agentic AI Coding: Best Practice Patterns for Speed with Quality (2026-09-24)

**Source:** https://codescene.com/blog/agentic-ai-coding-best-practice-patterns-for-speed-with-quality
**Context:** CodeScene (Adam Tornhill, Markus Borg) = behavioral code analysis, Code Health metric. AI-vein 2026 batch. Note: Feb 20 2026. Best practice patterns speed with quality. Relevance: agentic workflow patterns. Fetched 2026-09-24 curl, vendor research (numbers directional).

---

This year has marked an interesting and fundamental shift. I’ve been coding for almost 40 years, 30 of those professionally, and yet I’m now at a point where 100% of my production code is written and maintained by AI agents. I’m not alone: companies at the forefront of the agentic AI revolution report the same pattern.
But let’s not get carried away by hype. This shift didn’t come for free. Coding via agents requires more rigor, more structure, more code quality, not less.
In this article I’ll share what worked for my team, as well as the general patterns I’ve observed in the industry. (I’m in the fortunate situation of regularly meeting and working with organizations across the globe in all states of AI adoption).
A Return on Investment: What can agents do better than the expert human?
Before jumping into specific patterns and advice, it’s fair to address the silicon elephant in the room. If it’s hard to succeed with AI coding, why bother at all? What are the gains?
It’s still too early to lean on hard productivity numbers from the industry for two reasons.
First, there is the obvious vendor hype. Second, the agentic future is unevenly distributed. Many enterprise companies are just beginning to explore it and are not yet in a position to leverage agentic AI effectively.
At CodeScene, our AI team went all agentic four months ago. We experience a 2–3x speedup on our tasks. However, focusing solely on coding speed misses the real benefit. The value lies in what that speed enables.
We get to build things we would not have had time for otherwise.
Speed encourages experimentation and rapid iterations.
Agentic AI removes coordination bottlenecks. (I no longer need infrastructure support for a GitHub Action, nor a React expert to modify our UI).
But automatic coding alone will not let you ship faster. Coding is only one part of software development. To reap the benefits of AI, you need the right kind of code, supported by strong engineering practices. That is what the rest of this article is about.
Motivating the Patterns: The Core Challenges for AI Agents
Agents lack a reliable understanding of maintainability and change risk inside a real codebase. In practice, this means agents operate with incomplete context:
AI operates in a self-harm mode,
often writing code it cannot reliably maintain later.
AI needs healthy code to reduce the defect risk
,
yet will happily comply and start modifying any spaghetti mess, no matter how unlikely to result in functionally correct code.
Agents cannot verify their improvements.
After a refactoring attempt, is the code objectively better or just a different arrangement of accidental complexity?
These problems share a common root cause. AI lacks an objective way of measuring “good”. The following patterns provide that missing context and turn agentic speed into reliable outcomes.
Operational Patterns for Reliable Agentic Coding
When agents gain visibility into code quality, maintainability and change risk, their behavior shifts. The patterns below capture how that feedback is operationalized. The bulk of them are productified and implemented in our
Code Health MCP server,
which we use ourselves as a mandatory requirement for agentic AI.
Together, the Code Health score, MCP safeguards, and AGENTS.md form the infrastructure layer behind these patterns. Code Health provides objective signals about maintainability and risk. MCP exposes those signals as actionable tools.
AGENTS.md
encodes how the tools are combined into predictable workflows. The result is: abstract engineering principles turn into executable guidance that agents can follow consistently.
Want to know more about Code Health? It’s not just a concept, but the metric underpinning our AI tools and safeguards. Read all about it here.
1. Pull Risk Forward: Assess AI Readiness
Problem
Code lacking in quality isn’t AI-ready. Low Code Health increases the likelihood that agents fail on their task or, at best, burn excess tokens.
Context
We know from
peer-reviewed research
that AI performs best in healthy code; agents get confused by the same patterns as humans. As evident from the following graph, you want to aim for a Code Health of at least 9.5, ideally a perfect 10.0.
TL;DR lower code health → worse AI performance
Solution
Healthy code is AI-friendly: benefit from AI acceleration now. Code that is not-yet AI-friendly needs to be refactored and uplifted before attempting to implement features via agents.
💡Tip: Visualize AI-readyness via the Code Health visualizations.
Example on a strategic assessment of AI deployment based on Code Health as a proxy for AI-friendly code. View from CodeScene.
2. Safeguard Generated Code
Problem
An agent won’t necessarily implement healthy code. Even a minor amount of Code Health issues will soon contribute to a major decline in subsequent iterations.
Context
So parts of your code are AI-ready – great. However, that doesn’t mean you can loosen control. The quality of AI code mirrors its training data, and we – as an industry – haven’t exactly done a consistently great job in the past. That comes back to bite now. Due to AI’s speed, small quality issues accumulate quickly.
Solution
All AI code must be safeguarded with respect to Code Health to ensure it stays healthy. Safeguards can – and should – be automated. The Code Health MCP adds safeguards as tools at three levels:
Continuous
code_health_review
invoked as each snippet of code is being generated
A
pre_commit_code_health_safeguard
on uncommitted/staged files only, run before each commit
The
analyze_change_set
tool, which performs a full branch vs base ref check (PR pre-flight), run before opening a PR
Together, these MCP tools enforce Code Health by kicking the AI into a refactoring loop on any quality issues.
An example of a PR pre-flight check where all AI commits on a local branch get checked.
3. Refactor to Expand the AI-Ready Surface
Problem
Many legacy functions are simply too large and complex for reliable AI work, resulting in inflated error rates, excess token spend, and fragile changes. Without objective feedback, agents tend to reshuffle complexity and do minor polish rather than truly moving the needle of code quality.
Context
AI performs best on code that is healthy and modular. Refactoring is where objective feedback makes the biggest difference.
Solution
A simple
code_health_review
changes that dynamic:
The Code Health score gives agents an explicit, measurable goal
The detailed review offers the direction via concrete maintainability issues, allowing the agent to formulate a structured refactoring plan rather than guessing at improvements
The workflow becomes straightforward:
review → plan → refactor → re-measure
Large legacy functions often require an additional preparation step. Breaking them into smaller, cohesive units increases modularity and makes subsequent refactorings far more reliable. The payoff is immediate. Higher Code Health, clearer intent, and a larger surface where agents can operate safely.
💡Tip: Watch the
2-min demo of agentic refactoring
on a real-world codebase.
4. Encode principles and rules for agents
Problem
The MCP protocol exposes powerful individual tools, but not the workflow that connects them. Left on their own, agents tend to invoke tools opportunistically (or not at all), which weakens safeguards and leads to inconsistent outcomes.
Context
Agents need guidance on sequencing and decision logic to combine MCP tools into a coherent workflow rather than discovering guardrails by trial and error.
Solution
AGENTS.md closes that gap. It documents the intended sequencing and decision logic so agents can combine MCP tools into a coherent workflow.
In our own development, we use
AGENTS.md
for guiding agents to:
pull risk forward with a
code_health_review
,
safeguard changes via pre-commit and PR pre-flight checks, and
enter refactoring loops when health regresses.
That way,
individual tools turn into a predictable workflow
, and engineering principles become executable guidance for agents.
Documented agentic principles and rules allow us to express and automate the safeguarding and self-correction process above.
5. Use Code Coverage as a Behavioral Guardrail
Problem
Healthy code alone does not guarantee correct behavior. A common shortcut for an agent facing a failing test is to delete it, weakening behavioral safeguards without obvious signals.
Context
Up to this point, the patterns focused on safeguarding structure and maintainability. The next dimension is behavioral correctness. In agentic workflows, strict coverage gates on Pull Requests make any attempt to weaken behavioral checks immediately visible.
Traditionally, hard overall coverage targets have often done more harm than good. Coverage became a number to game, leading to shortcuts, excessive mocking, and tests that inflate metrics without improving confidence. Agentic workflows change that dynamic. With agents iterating at high speed, erosion of behavioral checks becomes a real risk.
Solution
Code coverage becomes an effective safeguard when used as a regression signal rather than a vanity metric. By setting the thresholds high, regressions surface early and cannot slip through unnoticed. Coverage gates act as behavioral checks alongside Code Health safeguards, ensuring code remains healthy and does the right thing.
Example on code coverage gates in Pull Requests. Screenshot from
CodeScene’s automated coverage gates
.
6. Automate checks end to end
Problem
With agents iterating at high speed, manual verification quickly becomes the bottleneck. Without higher-level automation, teams fall back on slow validation loops and lose the very advantage agentic AI is meant to provide.
Context
Unit tests have always been important. Agentic AI just raises the stakes. Unit tests remain the foundation for agentic coding. They enable fast iteration and let agents converge on working solutions. But they only validate local behavior.
Solution
Higher-level automation closes that gap. End-to-end tests exercise the packaged product in realistic scenarios and verify real outcomes.
In
our own product
, we sit at around 99% unit test coverage. Still, we complement that with end-to-end tests that execute the full system. Our tests build the distributable product, create and modify Git repositories, inject code smells, and invoke the product to verify that those issues are detected as expected.
This level of automation was always desirable. With AI speed, it becomes non-negotiable.
The Real Shift Isn’t AI. It’s Engineering Discipline
Taken together, these patterns form a feedback system that keeps agentic speed aligned with engineering quality.
Speed amplifies both good design and bad decisions, which means code health, automated safeguards, and short feedback loops become the real enablers of progress. Get that foundation right, and agents stop being a novelty and become what we always wanted them to be: a reliable accelerator for meaningful software development.

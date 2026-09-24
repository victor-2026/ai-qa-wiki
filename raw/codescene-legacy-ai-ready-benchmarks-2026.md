# CodeScene: Making Legacy Code AI-Ready: Benchmarks on Agentic Refactoring (2026-09-24)

**Source:** https://codescene.com/blog/making-legacy-code-ai-ready-benchmarks-on-agentic-refactoring
**Context:** CodeScene (Adam Tornhill, Markus Borg) = behavioral code analysis, Code Health metric. AI-vein 2026 batch. Note: Mar 18 2026. Benchmarks raw vs MCP-guided refactoring (2-5x Code Health gain, Extract Method 21K vs 7.5K). Relevance: guided-vs-raw evidence. Fetched 2026-09-24 curl, vendor research (numbers directional).

---

Most enterprises are now on a trajectory towards agentic AI. The general assumption is that faster coding will translate into increased productivity across the board.
However, there’s a potential clash between expectations and reality:
The
Code Health benchmarks
show that the average Hotspot Code Health in the IT sector is 5.15 on a 10.0 scale.
The threshold for healthy code that is easy for a human to understand is 9.0.
AI requires even better code quality, not less:
research on AI-friendly code
shows that you need at least 9.5 to keep AI-induced bugs in check.
Given that the average industry Code Health is only 5.15, naive AI adoption is unlikely to deliver the expected benefits. Not because the agent’s underlying LLMs are weak, but because the average code structure is too unhealthy for an AI to comprehend and safely modify.
This implies that legacy code is a key bottleneck for enterprise adoption of agentic coding tools. Before AI can accelerate feature work, code health needs to improve. Let’s explore how AI can guide that uplift.
Benchmarks: Raw AI vs MCP-Guided Refactoring
Even code that is not AI-ready can benefit from agents when refocused on refactoring. To explore this capability, we ran a series of experiments.
These experiments compared raw agentic refactoring using Claude Code with the same refactoring tasks but now guided by the CodeHealth MCP.
To limit any vendor bias, we used a public data set of 25,000 source code files from competitive programming, including carefully crafted unit tests.
We assessed agent correctness by running those tests.
CodeScene was put to use for measuring the Code Health impact.
(See
Code for Machines, Not just Humans
for more details on the methodology and data.)
The difference between Claude Code off-the-shelf versus Claude Code guided by the CodeHealth MCP was significant. Across all scenarios, the MCP-guided agent      achieved
2–5x more improvements in Code Health
compared to raw refactoring attempts:
Benchmarking AI refactoring impact: comparing Claude Code with and without Code Health MCP-guided refactoring.
As evident in the preceding graph, Claude Code fixes fewer code smells the healthier the code. That’s because worse code tends to have more obvious problems (e.g. excessively long methods with multiple responsibilities, obvious code duplication).
With higher Code Health, the issues are harder to detect and less obvious for an LLM; its training data likely contains fewer examples of decently-structured yet still improvable code, which may reduce an agent’s confidence in proposing deeper refactorings.
Now, before explaining the CodeHealth MCP and its refactoring workflow, we need to look at what these benchmarking numbers mean for developers and enterprises in terms of impact.
More than a Metric: Code Health as a Predictor
At this point, it’s fair to ask: are we just optimizing for a number? No, those Code Health improvements come with predictive power:
Efficiency:
The Code Red research showed that low Code Health correlates with slower delivery and higher defect density. Healthy code is faster to evolve and breaks less frequently. (See the
Code Red whitepaper
or the
underlying academic research publication
.)
AI-friendly code:
Recent work on AI-ready code extends the same finding into the agentic world. Higher Code Health improves AI correctness. (See the
key findings in the whitepaper
, details in the
peer-reviewed research
.)
Token savings:
Healthy code reduces iteration churn, and cuts token usage. In practice, uplifted codebases can see ~50% lower token consumption for comparable tasks. (Upcoming research publication – stay tuned for details.)
Obviously, you could use any MCP to nudge the AI in a specific direction. But to be business relevant, the feedback must carry meaning.
So why aren’t LLMs and agents doing this on their own? The study on
How do Agents Refactor
sheds light on the topic. The study reports that agents perform more refactorings than humans, but that “these changes do not necessarily have the same structural impact as human refactorings”. That’s pretty much the same conclusion we reached: unguided agents are conservative and seem optimized to err on the safe side. Consequently, agents do shallow improvements (think: rename variable) that don’t really move the needle on code quality. Let’s illustrate the difference via a more detailed look at the type of refactorings that the agents performed in our benchmark study:
Frequency of refactorings
Refactoring operation
Coding Agent
Coding Agent with CodeHealth MCP
Extract Method
(structural impact)
7,550
21,702
Rename Variable
(shallow refactoring)
54,094
8,640
That is why the benchmark improvements matter. They are not just numerical gains. They reflect a codebase that becomes progressively easier to change, and therefore progressively more AI-friendly.
How MCP-Guided Refactoring Looks in Practice
Now, how does the workflow play out in practice?
A typical uplift starts with a simple
code_health_review
. This MCP tool provides the agent with concrete and actionable feedback: complexity drivers, readability issues, excessive responsibilities, and structural smells. The review also provides a measurable baseline. The agent now knows both where it stands and what to improve.
Example on AI planning in an agentic refactoring session based on Code Health feedback and direction.
That feedback changes the agent’s behavior. Rather than performing superficial cleanups, the agent forms a structured refactoring plan. After each iteration, the agent re-measures progress against Code Health, creating a tight feedback loop.
Outcome of an agentic refactoring session: iterative code health improvements leading to AI-ready code.
MCP guided refactoring video (2-min demo)
What stands out in practice is not just the improvement in Code Health, but the stability of the refactoring process. The agent stops guessing. Instead, it iterates toward a clearly defined target, much like an experienced developer working with objective feedback.
That shift from exploratory edits to measurable uplift is the core reason behind the benchmark improvements.
From refactoring to acceleration
Agentic AI doesn’t remove the need for refactoring. Legacy code remains the bottleneck for enterprise adoption, yet with the right feedback loops, agents can uplift that legacy rather than extend it.
One-off uplift isn’t enough, though. The real improvement occurs when
those feedback loops are embedded into everyday development
. Only then can your recently uplifted code remain healthy, and continue to benefit from agentic speed.
Ready to try the CodeHealth™ MCP Server? Sign up for early access

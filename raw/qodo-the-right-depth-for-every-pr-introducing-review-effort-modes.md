# Qodo: The Right Depth for Every PR: Introducing Review Effort Modes (2026-09-23)

**Source:** https://www.qodo.ai/blog/the-right-depth-for-every-pr-introducing-review-effort-modes/
**Context:** Qodo (ex-Codium) = AI code quality & governance platform. TIER 2 catalog FULL READ. Note: FULL READ - effort as risk-tiering. Fetched 2026-09-23 with browser UA.

---

As AI agents take on more tasks across the software development lifecycle, no single model or level of reasoning is ideal for every use case. The same is true within code review: different changes call for different levels of depth, speed, and reasoning power.
Fixing a typo in a README or adjusting a CSS margin shouldn’t trigger the same multi-model, deep-reasoning as refactoring a payment gateway or changing a database schema. Applying deeper analysis to a contained change can add unnecessary cost and latency while a lighter analysis to a change with a wide blast radius may not provide enough scrutiny.
Qodo’s new Review Effort Modes, now in research preview, dynamically routes each pull request to the exact level of scrutiny it warrants, applying deeper analysis to complex, high-risk changes while keeping routine reviews fast and cost-efficient.
https://www.qodo.ai/wp-content/uploads/2026/07/Review-Effort-Modes.mp4
From Fast Pass to Deep Dive
Review Effort Modes allow teams to match review depth to their specific operational needs:
Fast
: A single review pass using a lightweight model. Optimized for small, contained changes where speed and cost efficiency are top priorities.
Balanced
A comprehensive review pass powered by Qodo’s benchmark-leading model. It is the default mode and provides a balance of review depth, speed, and cost for typical development work.
Deep
: Multi-pass analysis combining independent models and different reasoning approaches to uncover subtle bugs that a single pass might miss. It is intended for complex changes
Auto:
An adaptive router that evaluates PR complexity and automatically directs the change to the ideal tier.
Configuration & Availability
Review Effort Modes can be configured globally across an organization or set differently for individual repositories. Teams can establish a default mode across their codebase, then adjust it for repositories with different risk profiles, workflows, or review requirements. A documentation repository might use Fast, for example, while repositories containing shared infrastructure or production services use Auto. This gives platform teams a central policy without requiring every repository to receive the same review depth.
Balanced is the default mode. During the public research preview, Deep Mode is accessed through Auto. When Auto determines that a change requires deeper analysis, it routes the review to a deep review automatically. During the research preview, Deep Mode cannot be selected directly and does not incur an additional cost during the preview.
Smart Routing: Risk Isn’t Measured in Lines
How does Auto mode decide when to elevate scrutiny?
A 2,000-line diff isn’t automatically a difficult review. Generated files, lockfile updates, renames, and mechanical migrations can change thousands of lines without introducing high operational risk. Conversely, a three-line modification to an authorization check or payment path can impact the entire system.
Auto evaluates the nature of the change rather than relying on diff size alone. Before the main review begins, a lightweight routing step assesses signals related to logic complexity, change dispersion, and potential blast radius. If a pull request is difficult to reason about, Auto ensures it receives deeper analysis rather than a surface-level pass.
Review effort is more than the model
The model behind an AI
code review
affects its quality, speed, and cost, but it is only one part of the review architecture.
Review depth also depends on how many analysis passes are performed, how much reasoning each pass applies, and how findings are combined. A lightweight model completing one pass creates a different review experience from several models examining the same change independently.
Qodo manages these decisions for the user. Each Review Effort Mode packages the appropriate models, reasoning effort, and review architecture into a defined level of scrutiny. Teams select an effort mode or use Auto, while Qodo chooses and updates the models behind it.
This means users do not need to follow every model release, compare vendor benchmarks, or reconfigure their review pipeline whenever a stronger or more efficient model becomes available.
Effort modes as a product contract
Review Effort Modes are defined by their intended outcomes, not a fixed model lineup:
Fast
prioritizes speed and resource efficiency for contained changes.
Balanced
provides Qodo’s default balance of review quality, speed, and cost.
Deep
provides the most thorough review available through multiple independent passes.
Auto
selects among those tiers based on the pull request.
Qodo evaluates the models and architecture behind each mode using code-review-specific benchmarks. That evaluation measures precision, recall, and F1, along with latency, token use, and cost per review.
Precision measures how many findings are valid. Recall measures how many real issues the review catches. F1 balances the two, preventing a mode from appearing successful by producing many low-quality findings or by returning only a small number of highly certain ones.
A new model does not enter a mode simply because it is newer or performs well on general-purpose benchmarks. It must improve the outcome the mode is intended to deliver while meeting the relevant quality, latency, and cost requirements.
As models evolve, Qodo can update the stack behind each mode without changing what teams configure or how developers interact with the review.
Scaling review resources
Using multiple frontier models for every pull request would increase token usage and review latency, including for changes where the additional analysis is unlikely to affect the outcome.
Using only a lightweight model would create the opposite problem. It would reduce resource use but limit the depth available for consequential changes.
Auto allocates those resources selectively. Routine changes can take a faster path. Typical development work can stay at Balanced. Changes with broader impact can receive several independent review passes through Deep.
This becomes more important as AI coding agents increase the volume of changes entering review. Review capacity needs to grow with that output, but every additional pull request does not need to consume the same review resources.
Dynamic routing allows deeper review to remain available across an organization without applying it uniformly.
What Qodo is evaluating during the preview
The goal of Auto is not to route as many pull requests as possible to Fast. A routing system that reduces cost by missing important issues would fail its purpose.
Qodo is evaluating whether Auto:
Identifies changes that benefit from Deep review
Preserves an appropriate quality floor when selecting Fast
Defaults safely when the risk of a change is unclear
Improves the balance among review quality, cost, and latency
Makes consistent decisions across different repositories and types of changes
The public research preview gives Qodo a wider range of codebases and development patterns against which to test those decisions. Usage and feedback will inform the routing policy, mode definitions, and experience as the feature develops.

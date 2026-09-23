# Qodo: Building an Adaptive Router for Code Review Depth (2026-09-23)

**Source:** https://www.qodo.ai/blog/building-an-adaptive-router-for-code-review-depth/
**Context:** Qodo (ex-Codium) = AI code quality & governance platform. TIER 2 catalog FULL READ. Note: FULL READ - progressive rigor. Fetched 2026-09-23 with browser UA.

---

Every team has that pull request that didn’t need a careful review. A version bump. A typo fix in a comment. A regenerated lockfile with four thousand changed lines and no logic in any of them. And every team has the opposite kind: the small, quiet diff that reroutes a payment path or loosens an authorization check, tucked inside a larger refactor that nobody flagged as risky.
Qodo’s automated PR reviewer used to treat both the same way. Every PR received the same model, review depth, and cost the same credits, whether the change was a rename or a migration touching authorization and billing at once.
Not all PRs carry the same risk. The review effort should not be equal either. When review volume was human-sized, that was realistic. Now developers are shipping with AI assistance, and PRs arrive faster than any fixed review budget can absorb. Paying full price on every trivial diff is real money and real latency spent where it bought nothing.
As part of our new
Review Effort Modes
, we built a router to enable Qodo to dynamically choose the depth of review a PR requires. The rotuer runs before the review starts; it whole job is to look at a change, decide how much attention it has earned, and spend accordingly.
We wrote the goal down as one expression and optimized against it:
max(F1 − λ·cost)
F1
: measures review quality by balancing precision and recall. Precision measures how many reported findings are valid. Recall measures how many real issues the reviewer catches. A reviewer needs both to achieve a strong F1 score.
λ
: the exchange rate that lets a unitless fraction (F1) and a dollar amount (cost) be subtracted at all. It also sets how frugal the router runs; we keep it small, so quality leads and cost only breaks ties between close tiers.
Cost
: total spend per PR, the routing decision plus every model call it triggers.
The objective is simple: preserve as much review quality as possible while avoiding work that does not improve the result.
Latency is not part of the equation directly, but it often improves with cost. Fewer model calls, passes, and tokens usually produce a faster review. That matters because feedback is most useful when it arrives while the developer is still working on the change.
At AI development velocity, organizations cannot apply maximum review effort to every change. They also cannot afford to apply minimum effort indiscriminately. Adaptive review allocates more scrutiny where the potential blast radius is high and less where a change is narrow or mechanical
Four tiers and a router
The Review Effort Modes comes in four tiers.
Mode
What it does
Cost
Fast
A single pass on a light model.
Low
Balanced
One complete pass on the benchmark-leader model. The default.
Medium
Deep
Several passes across different models.
High
Auto
Selects one of the tiers above, or can choose to skip the review (reserved for generated files like lockfiles, comment fixes, and pure formatting.Zero) based on the risk and scope of the change.
Varies with the PR
Why diff size is the wrong signal
We treat the router the way we treat any model: no change earns its place until a benchmark shows a measurable gain.
Our baseline is Balanced review applied to every pull request. The performance changes discussed below are relative to that baseline, not absolute F1 scores.
The first version of the router used a single prompt. It gave a model the diff and asked how much review effort the change needed. That version scored about 4% below the Balanced baseline. This decrease revealed that the router treated large diffs as difficult and small diffs as simple. A thousand-line mechanical rename frequently went to Deep because the change looked substantial. Some smaller changes received lighter reviews even when the model had not fully understood their implications.
Diff size is the first thing the model reached for to judges effort, however size is rarely what determines whether a review is hard. Closing that gap, then clearing it, became the target.
The improved router therefore combines a lightweight language model classifier with deterministic guardrails. The model interprets the change. The guardrails limit which decisions it can make.
Counting edit sites
The signal that materially improved routing was the number of diff hunks. A hunk is a contiguous block of changes within a diff. Hunk count provides a rough measure of how dispersed a change is across the code.
Consider two pull requests with the same number of changed lines:
One replaces a single implementation in one continuous block.
The other changes logic across 40 separate locations.
The second is usually harder to review. A reviewer must understand more relationships, track more assumptions, and determine whether the separate edits remain consistent with one another.
This is why hunk count can be more informative than raw line count. Forty scattered logic changes across a single file will hide bugs that a 5,000-line generated file never contains. It helps distinguish a large but mechanical change from a change spread across many independent edit sites.
The router uses this signal alongside the semantic content of the diff. Its instructions emphasize logic complexity, change dispersion, uncertainty, and potential blast radius. Large but shallow changes, such as renames, file moves, and generated updates, should not get a deep review based on size alone. The router is also instructed not to downgrade a change it cannot understand. Uncertainty should produce a more capable review, not a lighter one.
A payment-path edit buried in a larger refactor shows up as many hunks scattered across the diff, exactly the dispersion the router reads as high blast radius, so the whole change draws a thorough review instead of a wave-through. The router never has to single out the risky line; the dispersion routes the change there, and the never-downgrade rule keeps it from slipping back.
The guardrail on Deep mode
Deep mode is the highest-cost tier, so it earns the strictest gate. Its value comes from redundancy: an ensemble of several independent passes catches defects a single pass misses. This redundancy is useful for open-ended issue detection, where different passes can genuinely disagree. It is less useful for deterministic checks such as compliance with a defined rule. Repeating the same rule-matching task several times adds cost without improving coverage.
Deep also provides the most value when a pull request could plausibly contain several independent defects. In our testing, those changes tended to be both large and dispersed.
The router therefore allows Deep only when a diff clears two minimum thresholds:
A minimum number of changed lines
A minimum number of hunks
A large but linear edit remains in Balanced because one strong review pass is usually sufficient. A similarly sized change distributed across many hunks may reach Deep because it introduces more relationships and possible failure points for the reviewer to track.
These thresholds apply to every route into Deep, including the model’s decision and any fallback path. No pull request reaches the highest-cost tier without satisfying the same conditions.
This does not mean small, critical changes receive weak reviews. Changes involving sensitive logic can still be protected from Skip and Fast based on their content. The Deep gate answers a narrower question: when is the added redundancy of several independent passes likely to improve the review enough to justify its cost?
Safe behavior when routing fails
The router is designed so that a routing failure does not block the review.
If the classifier times out, returns an error, or produces a malformed response, the pull request falls back to a safe review tier. The Deep thresholds still apply, so a routing failure cannot send a change to the most expensive tier without evidence that the added depth is warranted.
Very large diffs receive the opposite protection. Skip and Fast are removed as options, preventing a substantial change from receiving only a lightweight review.
The result is a router that can reduce unnecessary work without allowing failures to eliminate meaningful review coverage.
How the router improved
Four changes moved the router from below the Balanced baseline to its current performance: matching Balanced F1 while reducing model cost by 21%, token usage by 30%, and average runtime by 27%.
Adding the two-threshold gate for Deep
Introducing hunk count as a measure of change dispersion
Rebuilding the routing prompt around logic risk, defect density, and independent edit sites
Removing redundant ensemble passes from deterministic compliance checks
Together, these changes corrected both sides of the routing problem. Mechanical changes stopped reaching Deep simply because they were large. Complex changes received more scrutiny when their structure and potential blast radius justified it.
The first router scored about 4% below the fixed Balanced baseline. After these changes, Auto matched the benchmark F1 achieved by applying Deep review to every pull request, while keeping average spend close to Balanced.
That does not mean every Auto-routed pull request receives a Deep review. It means that across the benchmark, Auto achieved the same measured quality as the all-Deep setup by reserving Deep for the changes where it improved the result.
We then tested the router on a held-out set of pull requests that was not used during tuning. The improvement held on that set as well, giving us evidence that the router had learned a useful routing strategy rather than the specific examples used to develop it.
What we learned
The benchmark determined whether the router was ready to ship. Our internal pull requests showed what it changed in practice.
Compared with the fixed-depth setup it replaced, Auto produced:
Two metrics stand out:
First, token usage fell further than cost, 30% against 21%. The remaining spend is concentrated on stronger, more expensive models used for the changes that need them. The router removed a larger share of low-value token volume than high-value model usage, which is the intended result.
Second, average runtime fell by 27%, while p90 runtime fell by 12%. Difficult changes still reach Deep and still require several review passes. The largest improvement therefore appears in the middle of the distribution, where routine pull requests no longer wait for unnecessary analysis. The longest reviews improve less because the router is intentionally preserving additional scrutiny for complex changes.
These are our own repositories and our own mix of changes, so another codebase will sit elsewhere on the curve, and quality stays something we measure on the benchmark rather than in production.
The result is the balance we set out to achieve: less unnecessary review work, faster feedback for routine changes, and deeper analysis where the code justifies it.

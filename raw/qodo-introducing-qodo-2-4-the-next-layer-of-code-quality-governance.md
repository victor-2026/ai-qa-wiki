# Qodo: New Features: Qodo v2.4 and the next layer of code quality governance (2026-09-23)

**Source:** https://www.qodo.ai/blog/introducing-qodo-2-4-the-next-layer-of-code-quality-governance/
**Context:** Qodo (ex-Codium) = AI code quality & governance platform. TIER 1.5 catalog candidate. Note: SKIM - RAG removal story interesting. Fetched 2026-09-23 with browser UA.

---

Every team relies on code review to catch what shouldn’t ship. As AI writes more of the code, reviewers face far more volume, moving faster, across systems more connected than any single repository. The hard part was never reviewing one diff well. The hard part is holding the line consistently across the way real engineering teams actually build software: dozens or hundreds of interconnected repos, standards that live in people’s heads instead of documents, and a growing layer of AI tooling quietly shaping how code gets written and reviewed.
Qodo brings each of those into the system with this release, adding three new capabilities, each built on the Context Engine, the data layer behind every Qodo agent.
Cross Repo Review
catches breaking changes before they ship by extending Qodo’s reasoning across the repos that depend on each other.
Rules Miner
makes review precise to how your team actually works by mining coding standards from your PR review history.
Skill Review Standards
gives engineering leaders control over the standards being enforced by turning skills into a managed, measurable entity.
All three are available now in Beta, across all Git providers, for both multi-tenant and single-tenant deployments.
Cross Repo Review: catch breaking changes before they reach production
Picture an engineer opening a PR that changes the signature of an exported function in a shared SDK. The change looks clean inside that repo. It passes review. It merges. Three other services that import the function break in production the next morning, and the team spends the day tracing the failure back to a PR that looked perfectly safe.
This is the reality of distributed engineering. A typical organization works across dozens or hundreds of interconnected repositories, and the most damaging issues are the ones that cross the boundaries between them. A change to a shared utility, an API contract, or a data schema in one repo can silently break consumers in another. Review tools scoped to a single repository miss these cross-cutting concerns entirely, so the break surfaces after merge, in production, where it is most expensive to fix.
Cross Repo Review changes the outcome of that scenario. Qodo now maps how repos depend on one another and surfaces cross-repo conflicts and breaking changes during PR review, before the code reaches production. In the example above, Qodo identifies the consumer repos that call the changed function and posts a cross-repo conflict finding on the PR, with a direct link to the affected line in the consumer code. The engineer updates the signature, adds backward compatibility, or coordinates with the consuming teams, all before merge.
Why it matters
Cross Repo Review moves code quality from a per-repository measure to a per-system one. In a distributed architecture, quality can’t be managed in silos. By extending Qodo’s reasoning across the dependencies that hold a distributed system together, engineering and compliance standards apply to the whole software ecosystem rather than its isolated parts.
It matters more as velocity climbs. When AI floods many repos with code at once, tracking cross-repo impact by hand becomes impossible. Cross Repo Review automates that oversight, so organizations hold structural integrity and prevent architectural drift even as the pace of change accelerates.
It also works the way large organizations are actually structured. Cross Repo Review reasons across all your Git providers, so a service in one provider and the repo that consumes it in another are still connected in review. Few engineering organizations live entirely in a single Git provider, and the dependencies that break in production rarely respect those boundaries. Qodo doesn’t either.
What it is
Cross Repo Review adds one new Context Engine capability, one new agent, and three new experiences.
Until now, the Context Engine collected structure, semantics, and embeddings for a single repo at a time. With this release, it builds relationship maps of how repos depend on each other, with a human in the loop so teams stay in control of which relationships Qodo reasons over. A new Cross Repo Agent puts those maps to work: when a PR opens, it reads the related repos to build cross-repo context and identifies downstream consumers, breaking changes, and blast radius across them.
That work surfaces in three places: as a new category of issue finding directly in the PR through the Git plugin, aggregated with metrics on the Findings page in the Qodo portal, and in new portal pages for managing repo relationships.
Check out Qodo docs to get started with Cross Repo Review.
Rules Miner: standards that reflect how your team actually works
A new engineer joins a team and opens their first few PRs. The same three reviewers leave the same kinds of comments they always do: this pattern isn’t how we handle errors here, this should use the shared client, this needs a feature flag. None of it is written down anywhere. It lives in the reviewers’ heads and surfaces one comment at a time, PR after PR. The standards that matter most to this team are the ones nobody ever had time to document.
That tribal knowledge is the richest signal of how a team really reviews code, and it’s sitting in plain sight in the PR history: recurring comments, discussions, the suggestions that get accepted, the ones that get rejected, the approval patterns. Without that signal, any review tool is guessing at a team’s standards instead of learning them. The usual alternatives don’t hold up. Writing rules by hand is tedious, so teams start, prioritize the wrong things, and abandon the effort, and the rules that exist are out of date within a quarter. At scale it gets worse: a customer with 400 repos can accumulate thousands of rules, and manually enabling, deduplicating, or auditing them is not realistic.
Rules Miner is a new learning capability inside Qodo’s rules system. It analyzes codebase patterns and PR review history, surfaces the standards that keep recurring, and creates rules that Qodo enforces on future PRs. It maps where those patterns cluster, so the rules it produces are scoped to the paths they govern. For the new engineer above, the team’s real standards are now enforced from their first PR, instead of learned through months of repeated comments.
https://www.qodo.ai/wp-content/uploads/2026/06/1920×1080-02-C.mp4
Standards that emerge from real behavior
Because the rules come from real review behavior, they reflect what the team actually cares about rather than generic best practices imported from elsewhere. Not all signal counts equally. Feedback from tech leads and maintainers carries more weight than a drive-by comment, so rules reflect real decision-making. Recurring comments rise into candidate rules while one-offs don’t. Accepted suggestions reinforce the rule behind them; rejected ones pull it down over time, so noise fades on its own. And explicit comments on findings give the system a direct steer, with no waiting for a pattern to form.
A rules system that maintains itself
Every interaction with the review agent becomes a learning signal, so that closed loop creates, updates, and deletes rules without manual curation. Duplicate detection catches near-identical rules before they’re created, keeping the rule set clean at any scale. Teams stay in control: Rules Miner is self-service through the onboarding wizard or the configuration page, set once at the org level and overridden per repo when needed. Every mined rule links back to the comment source it came from, and mined rules can go live automatically or sit in suggested mode for human review first.
See our documentation for more information
Skill Review Standards: governance for the standards you can’t see
A platform team builds a library of skills to keep their AI tooling consistent: a skills.md file that packages the rules, workflows, and context telling an AI tool “this is how we build software here.” It works. Then it spreads. Six months later there are dozens of skills across repos and authors, with overlapping scope, unclear ownership, and no one able to say which ones are actually helping and which are just adding noise.
Qodo already extracts context from these skills, turns them into rules, and enforces them during PR review. What’s been missing is governance. Skills proliferate fast and fragment across the org, with no single place to view, manage, or control them, which is a real problem for teams that have built internal skill marketplaces and want governance to match the discipline they’ve already invested in. And without analytics, there’s no way to measure a skill’s ROI, track its token cost, or spot the noisy, low-value ones worth retiring.
Skill Review Standards makes skills a first-class entity for coding standards. They go from invisible implementation detail to a managed entity with their own portal tab, governance controls, and analytics.
What ships
Skill discovery.
Qodo scans repos for skills files and surfaces every skill that carries review instructions, rules, and best practices.
A dedicated Skills tab.
A centralized view of every skill running in code review, with its description, type, support status, and source link.
Skill-level control.
Enable or disable a skill from the portal in one click. The toggle bulk-activates or deactivates all the rules inside it, with no code edits and no per-rule cleanup.
Per-skill analytics.
Enforcement, violation, and merged-with-violations counts show which skills do real work and which can be retired.
Skill attribution on findings.
PR comments link back to the skill that produced the finding, so engineers can trace a standard to its source.
External repository support.
Scan and govern skills from dedicated skills repos, matching how teams already organize them.\
https://www.qodo.ai/wp-content/uploads/2026/06/1920×1080-03-A.mp4
Why it matters
For the platform team above, this is the difference between hoping their skill library is working and knowing it is. Visibility, so teams see exactly what’s running in code review and why. Centralized control, so policy gets enforced at the org level without coordinating commits across every repo, treating skills as a program rather than a config file. And measurement, so per-skill metrics let the team that owns the standards manage skills like any other engineering investment, deciding what to double down on and what to retire.
One foundation, more of the system
The through line across Qodo 2.4 is the same one behind everything we build: review gets better when it understands more of the context that actually shapes a team’s decisions. With this release, that context grows in three directions at once. Outward, across the repos that depend on each other. Backward, into the review history that defines a team’s real standards. And into the skills that have been quietly shaping reviews all along.
Together, these capabilities move Qodo further toward what enterprises need as AI development scales: quality and governance that grow with the way teams actually build software.
Get started with Qodo

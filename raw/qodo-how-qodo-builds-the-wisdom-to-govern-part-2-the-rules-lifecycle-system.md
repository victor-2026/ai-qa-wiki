# Qodo: How Qodo Builds the Wisdom to Govern, Part 2: The Rules Lifecycle System (2026-09-23)

**Source:** https://www.qodo.ai/blog/how-qodo-builds-the-wisdom-to-govern-part-2-the-rules-lifecycle-system/
**Context:** Qodo (ex-Codium) = AI code quality & governance platform. TIER 1.5 catalog candidate. Note: FULL READ - rules = standards enforcement. Fetched 2026-09-23 with browser UA.

---

Part 1 of this series described the Context Engine
, the knowledge layer that gives review agents a verified picture of the system a change lands in: repository structure, pull request history, cross-repository relationships, and the requirements behind the work.
Context answers what is there. It does not answer what the organization requires.
Those are different problems. An agent can read a repository and still have no idea that your organization requires idempotency keys on every mutation endpoint, forbids raw SQL string interpolation, tolerates one logging library and not the other, and treats anything under the payments path as needing a second reviewer. That knowledge exists, but it lives in wikis nobody opens, in linter configs that only cover what can be checked statically, in a
CONTRIBUTING.md
last updated two reorganizations ago, and mostly in the heads of the four engineers everyone asks.
Qodo’s Rules Lifecycle System is the standards layer that turns that scattered knowledge into something a machine can enforce and an organization can govern. In the Qodo portal the surface where teams manage it is called Review Standards, and it manages both rules and skills as first-class entities. What follows is how a standard gets in, how it is scoped and enforced, and how its effect is measured.
Why an instruction file is not a standards system
The current default in the industry is the agent instruction file:
AGENTS.md
,
CLAUDE.md
,
.cursor/rules,
copilot-instructions.md
. These files are genuinely useful, and Qodo reads all of them. But they are also not a governance mechanism, for three structural reasons.
A rules file does not scale across an organization. One file per repository works at one repository. At five hundred repositories it means five hundred copies of a standard, drifting independently, with no way to answer “when should this rule be enforced?” or even “should this be a rule anymore?”
They have no lifecycle. A line in a markdown file has no severity, no owner, no scope beyond the file’s location, no record of when it was added or why, and no signal about whether it has ever changed a single line of shipped code. Nothing expires. Files accumulate. Stale guidance sits next to current guidance and looks identical.
And they conflate guidance with enforcement. Putting a standard in front of a model raises the probability it gets followed. It does not make a violation detectable, explainable, or traceable. Governance needs the second thing. An enterprise cannot attest to a control whose enforcement is best-effort and whose evidence is a model’s good intentions.
Rules in Qodo are the same standards, promoted into structured, addressable objects with a lifecycle attached.
What a rule actually is in Qodo
A rule is not a prompt fragment. It is a record with a fixed shape.
Each rule carries a name, the enforcement content the review agent evaluates against, and compliant and non-compliant code examples that get shown to the developer when the rule fires. On top of that sit four fields:
Category
: Security, Correctness, Quality, Reliability, Performance, Testability, Compliance, Accessibility, Observability, Architecture.
Severity
: Error means comply, Warning means comply by default, Recommendation means apply where it fits. Severity is what separates a policy from a preference, and it is set per rule rather than inferred at review time.
Scope
: the set of paths the rule governs, from global down to a directory inside one repository.
Source type
: is the provenance whether authored by a user, extracted from a repository file, drawn from a Qodo library, mined from an observed pattern, or taken from a compliance file.
Where standards come from
No single input captures an organization’s standards, so the system looks at four.
Authoring
An admin describes the standard in natural language, for example “disallow SQL string concatenation with user input,” and an agent turns it into a structured draft with content, examples, category, and severity for the admin to edit and activate.
Import from repository files
Qodo analyzes the whole repository rather than a fixed list of filenames. Detection starts where standards usually are, in the instruction files teams already keep:
AGENTS.md,
CLAUDE.md
,
GEMINI.md
,
copilot-instructions.md
,
best_practices.md
,
RULE.md
, .
cursor/rules/
, and skill directories. But standards rarely stay where a convention puts them. They also sit in a
docs/
folder, in a
readme.txt
, in an architecture decision record nobody thought to link. Qodo reads the repository to find those too..
Extraction identifies the sections that express enforceable standards, converts those into rules, and then normalizes and enriches them with category, severity, scope, and examples so an imported rule behaves exactly like an authored one.
Extraction runs in two steps. The first identifies the passages in a document that express an enforceable standard, discarding narrative and setup. The second turns each passage into a rule: content phrased as an enforcement criterion, compliant and non-compliant examples, a category, and a severity. Splitting the work is what keeps imported rules from reading like excerpts.
Every rule from a file keeps a pointer to the repository and path that produced it, so the portal can answer where a rule came from, and the path that produced the rule is the path that scopes it.
Rules are scoped to the folder containing the source file, at any depth. Rules extracted from
src/payments/AGENTS.md
apply only to changes under src/payments/ and below. A file at the repository root scopes to that repository, not across the organization.
Mining from review history
Qodo’s
Rule Miner
reads what the team has already enforced in its own reviews. It indexes up to roughly the thousand most recently merged pull requests per repository, then weighs four signals together:
Reviewer code ownership.
Qodo estimates each reviewer’s ownership of the code they commented on and weights their feedback accordingly, so a maintainer’s remark on their own subsystem counts for more than a passing comment from someone with no stake in it.
Recurrence.
Feedback that appears repeatedly across pull requests rises into a candidate. A single comment can qualify on its own when it comes from a reviewer with strong ownership.
Where feedback concentrates.
Clustering maps the areas that draw the most comment, which is what scopes a mined rule to the paths it actually governs rather than to the whole repository.
Rejected suggestions.
Once a rule is active, dismissed suggestions it generates reduce its signal over time, so a mined rule that turns out to be noise fades without anyone intervening.
A comment has to name a specific code issue, and the author has to have applied the fix. Praise, questions, nitpicks, and declined suggestions count for nothing. Volume is capped deliberately because a standards system that produces a hundred candidates a week is not a standards system.
Extracted from Agent Skills
A skill is a markdown capsule, a
SKILL.md
plus supporting files, stored in the repository, that teaches an agent how to do a multi-step task the way this organization does it. Qodo treats skills as first-class review inputs rather than as documentation. It discovers the skills in the repository, filters to the ones relevant to the diff, and uses them as live inputs. Findings driven by a skill are cited back to that skill by name, so the rationale is always traceable to the artifact the team wrote.
Preventing duplicates and conflicts
Multiple inputs feeding one rule set is a recipe for bloat and self-contradiction unless something stands between a candidate and enforcement. Two mechanisms do.
Similarity detection distinguishes three relationships between rules. Two rules are identical when they express the same enforcement logic regardless of scope, which means an organization-level rule and a repository-level rule with the same content are duplicates even though they cover different code. They are overlapping when one contains the other, typically a general rule and a narrower special case. They are contradictory when complying with one means violating the other.
Each wants a different resolution. Merge a duplicate. Keep the narrow rule and adjust the broad one. A contradiction is different: two rules demand opposite things, and only a person can decide which one the organization actually wants. Qodo surfaces it rather than resolving it.
Similarity is computed semantically and persists as links in both directions, so a rule always knows what it relates to. A user can dismiss a wrong one, since semantic closeness and normative equivalence are not the same thing.
Reconciliation is the automated counterpart. When mining produces a candidate, reconciliation compares it against the rules it most resembles and decides one of three things: keep it as a new rule, skip creating it because an existing rule already covers the ground, or generalize the existing rule so it covers the new case instead of adding a near-twin.
Because generalizing changes a rule that is already in force, the path is bounded by explicit guarantees:
The rule being modified has to be one of the rules actually surfaced for comparison, so the step cannot reach for an arbitrary rule.
The change has to be asserted as a generalization rather than a rewrite.
The new scope has to be a superset of the existing scope. This makes narrowing structurally impossible: reconciliation can broaden what a rule covers and can never quietly shrink it.
The rule’s name, severity, and category are out of reach entirely.
The modification and the retirement of the candidate happen together, so there is no window in which both exist.
If any of these cannot be satisfied, reconciliation adds the candidate as its own rule instead, leaving existing rules untouched. That is also how it runs today: keep or skip, never rewriting a rule already in force, with generalization switched on once it has earned confidence.
Enforce: how a rule reaches a pull request
Which rules apply to a change
A rule reaches the review as criteria to be evaluated rather than a pattern to be matched. Each rule is judged against the change plus the surrounding system Qodo’s Context Engine provides rather than the diff alone, which is what makes rules about architectural boundaries or cross-service contracts meaningful. When one fires, the finding carries the rule’s severity, category, examples, and a link back to the rule.
Choosing which rules reach that judgment is deterministic. A rule’s scope is the set of paths it governs, and scopes are hierarchical: the root, which applies everywhere, then the git organization, the repository, and any directory inside it at any depth. A rule can carry several, so one rule can govern three services and a shared library without being copied four times.
Rule selection runs from the change. When a pull request touches s
rc/payments/api.py
, Qodo collects every scope containing that path: the root, the organization, the repository,
src/
, and
src/payments/
. Every active rule scoped to one of those is selected. Paths are compared folder by folder rather than as raw text, so a rule scoped to
src/payments/
never fires on
src/payments-legacy/
.
When several rules match the same change, all of them run and none overrides another. There is no most-specific-wins and no shadowing: a rule scoped to
src/payments/
does not replace the organization-wide rule above it, it adds to it. Otherwise a team could exempt itself from an organization-wide security rule by writing a narrower one at its own path.
The same change against the same rule set therefore produces the same checks every time, and the organization can say exactly which standards were applied.
Measure: what the numbers are for
Every rule reports, over a rolling thirty-day window, three things: how often it was found compliant, how often it was violated, and how often a pull request was merged with an unresolved violation of it still open.
A high merged-violation count means the rule fired, a human read it, and the team shipped anyway. Read once, that is a statement about the code. Read across dozens of pull requests, it is a statement about the rule. Either the standard is not actually the organization’s standard, or it is correct and expensive and nobody has been given time to satisfy it, or it is firing in places it was never meant to apply. All three are actionable, and none of them are visible from a rule’s text.
This is the measurement that a rule set needs in order to be prunable. Compliance rates tell you the standard is being met. Merged violations tell you which of your standards the organization has quietly stopped agreeing to.
Skills report the same shape: how often a skill was triggered, how many violations it detected, and how many of those got merged anyway.
Governance is a feedback loop
A rule is useful only while it reflects what the organization actually expects. That is why the lifecycle matters as much as enforcement.
Standards enter the system from deliberate policy, repository instructions, agent skills, and the judgment already visible in review history. They are normalized into governed objects, checked for duplication and conflict, scoped to the code they belong to, and evaluated with the surrounding context needed to interpret them correctly. Then their outcomes flow back into the system. Accepted findings strengthen confidence, while repeated dismissals and merged violations reveal rules that are noisy, misplaced, impractical, or no longer true.
That feedback loop turns governance from a pile of instructions into an operating system for engineering judgment. The goal is not to accumulate more rules. It is to maintain the smallest set of standards that the organization genuinely intends to enforce and to know, with evidence, whether those standards are improving the code that ships.
The Context Engine gives Qodo the knowledge to understand a change. The Rules Lifecycle System gives it the institutional memory to judge that change by the standards of the organization making it. Together, they provide the foundation for review agents that do more than notice possible defects. They apply the right expectations, in the right place, for reasons the organization can inspect and govern.

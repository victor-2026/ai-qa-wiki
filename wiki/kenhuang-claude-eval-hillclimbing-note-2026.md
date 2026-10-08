# Ken Huang: Claude Eval Design and Hillclimbing (Note, Outline-Level, Sep 2026)

**Source:** Ken Huang, "Claude Eval Design and Hillclimbing: From Reliable Tests to Better Agents", Agentic AI Substack, 2026-09-30. PAYWALLED — only the 8-section outline (stakes) was readable 2026-10-07. Full text NOT verified; treat below as table of contents, not findings.
**URL:** https://kenhuangus.substack.com/p/claude-eval-design-and-hillclimbing
**Refs inside:** Anthropic eval docs (develop-tests); anthropics/skills claude-api SKILL.md (`/claude-api build-eval`, `/claude-api hillclimb`); Lance Martin 28.09.2026 automating-eval-design-and-hillclimbing.

## Outline (8 sections, stakes preserved)

1. **Separate measurement from optimization** — eval design vs app improvement; version boundaries; attribution (better app vs different grader vs different task population).
2. **Production behavior → reviewable cases** — support-routing example, 4 destinations + abstention; representative traffic, difficult cases, prohibited actions; coverage of costly interactions, not just label accuracy.
3. **Check the grader** — deterministic checks vs model judges vs human calibration; repeatable verdict can still reward incorrect behavior; unstable judge can obscure real improvement.
4. **Bounded experiment** — setup requirements vs team-owned decisions (editable files, eval budget, acceptance rule, stopping condition).
5. **Validation vs final test** — two-way vs three-way split for iterative selection; what repeated trials establish on small case sets; which score supports dev decisions vs claims about unseen tasks.
6. **Uncertainty at task level** — illustrative: six extra passes don't settle a release; repeated attempts ≠ distinct cases; protected categories separately from aggregate.
7. **Cost under quality constraint** — scrutinizes Lance Martin's results; operational cost incl. unsuccessful attempts; lower token bill ≠ lower cost per completed task.
8. **Reproducible release decision** — review procedure for config records, failure evidence, uncertainty, monitoring; another engineer must reconstruct why a change was kept and what would justify revert.

## Relevance (provisional)

Sections 1/3/5/6 rhyme with Breaklight verdict-rule + noise-floor doctrine and our evidence/improvement separation. Section 7 (cost per SUCCESSFUL task) belongs in verdict-economics ledger (W2 track). Upgrade to full ingest if paywall access appears.

## See also

- [Elastic shared eval framework](wiki/elastic-shared-eval-framework-chang-2026.md)
- [Breaklight testing methodology whitepaper](wiki/breaklight-ai-testing-methodology-whitepaper-2026.md)
- [ThinkingBox Microsoft stateful bench](wiki/thinkingbox-microsoft-stateful-bench-2026.md)

- [[breaklight-ai-testing-methodology-whitepaper-2026]] — verdict rule, noise floor
- [[kenhuang-maestro-google-control-roadmap-2026]] — same author, control model

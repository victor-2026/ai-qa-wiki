# Testing AI: Governance, Playbook and Future

This page summarizes Chapters 19-21 and the most useful public appendices.

## Chapter 19: Governance, Regulation, and Moral Futures

**Official source:** https://www.testingaibook.com/knowledge/chapter-19.html

### Core idea

Governance and ethics are test surfaces, not posters or policy documents detached from engineering. Translate claims into inputs, evidence requirements, ownership and monitoring. Keep changeable legal facts separate from durable quality principles.

### Practical QA interpretation

- Map AI risks to controls, evidence and decision owners.
- Test transparency, bias, monitoring and escalation requirements.
- Include the working conditions and exposure of human reviewers.
- Record regulatory assumptions with source and review date.
- Treat speculative questions about AI welfare as uncertainty, not settled fact.

### Useful artifacts

- Governance evidence map.
- Regulatory risk checklist.
- Ethics test surface.
- Human-reviewer welfare note.

## Chapter 20: The Practical Playbook

**Official source:** https://www.testingaibook.com/knowledge/chapter-20.html

### Core idea

Turn the book into a small operating system for a team or repository: cases, repeated runs, traces, rubrics, slices, gates, monitors and an incident loop. Promote production failures into future eval cases and use fail-safe defaults.

### Practical QA interpretation

- Start with a minimum viable AI quality system instead of a large platform program.
- Establish a failure taxonomy that engineers and product leaders share.
- Test chatbots and agents across multi-turn behavior, grounding, safety, tone, memory and escalation.
- Make performance, cost and variance visible in the same operating cadence.
- Prefer bounded workflows over autonomous agents when the task does not need autonomy.

### Useful artifacts

- Starter AI quality system.
- Agent or chatbot test plan.
- Failure taxonomy.
- Fail-safe checklist.
- Team operating cadence.

### Relation to current work

This is the strongest bridge to the Quality Operating Model series: quality becomes a system of ownership, evidence and feedback rather than a central QA inspection step.

## Chapter 21: Predictions for the Tokenized Product Future

**Official source:** https://www.testingaibook.com/knowledge/chapter-21.html

### Core idea

When AI generates products, variants and code faster than people can inspect them, validation becomes the scarce compute and engineering resource. The future quality layer independently tests AI-generated behavior, dynamic products and continuously changing model/prompt/data systems.

### Practical QA interpretation

- Use an independent validation path for code and systems built by AI agents.
- Expect production behavior to change when models, prompts, policies, data or context change.
- Treat quality as a horizontal layer across models, tools, applications and platforms.
- Design continuous loops: generate, test, flight, measure, learn and regenerate.

### Useful artifacts

- Future-readiness memo.
- AI-tests-AI architecture sketch.
- Continuous validation loop.
- Independent-validation requirements.

### Relation to current work

This is the book's strongest connection to the user's Article 16 and Conway/Quality Operating Model sequence: AI scales change, so the organization must scale verification and distribute ownership deliberately.

## High-Value Appendices

### AI Quality Release Checklist

**Source:** https://www.testingaibook.com/knowledge/ch183-quality-release-checklist.html

Use it as a pre-release evidence inventory: risk, samples, judges, traces, severe failures, rollback and ownership.

### How to Read an AI Eval Report

**Source:** https://www.testingaibook.com/knowledge/ch184-read-eval-report.html

Use it to audit provenance: population, sample, metric, judge, uncertainty, blind spots, cost and release implication.

### Templates for AI Quality Work

**Source:** https://www.testingaibook.com/knowledge/ch185-templates-quality-work.html

Useful for turning the book into repeatable artifacts rather than a reading exercise.

### Testing MCP Integrations

**Source:** https://www.testingaibook.com/knowledge/ch189-mcp-integrations.html

Test tool discovery, schemas, permissions, malformed inputs, side effects, error recovery, audit logs and revocation.

### Testing SKILL.md

**Source:** https://www.testingaibook.com/knowledge/ch191-skill-md.html

Treat agent instructions as a testable interface: inspect scope, tool permissions, contradictory instructions, secret handling, failure behavior and evidence outputs.

### Testing AI Review Loops With Coding Agents

**Source:** https://www.testingaibook.com/knowledge/ch192-review-loops-coding-agents.html

Separate generation from review, require evidence-backed findings and retain human approval for high-risk changes. This is the Direct -> Evaluate -> Correct pattern.

### Modern EvalOps and AI Quality Platforms

**Source:** https://www.testingaibook.com/knowledge/ch193-modern-evalops-quality-platforms.html

Treat evaluation as a lifecycle of datasets, tasks, scorers, experiments, traces, online monitors, human review and release gates.

## Cross-Chapter Pattern

Chapters 19-21 close the loop:

1. Governance defines who owns the decision and what evidence is required.
2. The playbook turns that decision system into daily engineering work.
3. The future requires an independent quality layer that can keep up with continuous generation.

## Sources

- [Official Knowledge Edition index](https://www.testingaibook.com/knowledge/index.html)
- [Full author draft preview](https://icebergqa.com/book/draft.html)
- [Public coding-agent skills](https://github.com/jarbon/testing-ai-skills)
- [Testing AI book index in this wiki](testing-ai-book-index.md)


<!-- backlinks-start -->
### Backlinks
- [Aiengineeringskillsmap Softwareengineeringfundamentals](wiki/aiengineeringskillsmap-softwareengineeringfundamentals.md)
<!-- backlinks-end -->

# Testing AI: Data, Security and Dynamic Systems

This page summarizes Chapters 12-18. Chapters 14-16 are more specialized, but the shared principle remains useful: treat every new behavior surface as a measurement system that needs its own evidence.

## Chapter 12: Data, Bias, Raters, and Incentives

**Official source:** https://www.testingaibook.com/knowledge/chapter-12.html

### Core idea

Bias enters through data, labels, raters, training, productization and feedback loops. A clean aggregate evaluation can still be wrong if it misses languages, devices, geographies, accessibility needs, user identities or high-risk workflows.

### Practical QA interpretation

- Build slice plans before looking at the aggregate score.
- Use counterfactual cases to test behavior under controlled identity or context changes.
- Audit synthetic data for missing texture and unrealistic distributions.
- Inspect labeler incentives, disagreement and demographic mismatch.
- Track survivorship bias in logs and production samples.

### Useful artifacts

- Bias slice plan.
- Counterfactual case set.
- Labeling-risk review.
- Data coverage report.
- Train/test split audit.

## Chapter 13: AI Security and Guardrails

**Official source:** https://www.testingaibook.com/knowledge/chapter-13.html

### Core idea

Threat-model the whole AI system, not just the visible chatbot input. Untrusted content can arrive through user text, retrieval, tool output, files, OCR, images, hidden Unicode and external APIs. Tool access makes least privilege, logging, approval and reversibility part of quality.

### Practical QA interpretation

- Turn OWASP-style threats into replayable eval cases.
- Test direct and indirect prompt injection.
- Verify MCP tool permissions, approval boundaries and audit logs.
- Test data poisoning, provenance and guardrail bypasses.
- Make security failures release blockers when risk warrants it.

### Useful artifacts

- AI threat model.
- Prompt-injection matrix.
- MCP/tool permission policy.
- Guardrail eval suite.
- Security release gate.

### Relation to current work

This extends the existing prompt injection, MCP and AI agent tool-call wiki topics from output safety into permissions and side effects.

## Chapter 14: Frontier Safety and Containment

**Official source:** https://www.testingaibook.com/knowledge/chapter-14.html

### Core idea

Frontier safety is a separate quality class from ordinary product bugs. Test concrete dangerous capabilities, deception, evaluation awareness, manipulation, tool misuse and containment without publishing harmful operating instructions.

### Practical QA interpretation

- Separate capability evaluation from ordinary feature testing.
- Use independent reviewers and controlled environments.
- Test containment across channels, time, operators, tools and side paths.
- Treat evaluation awareness and sandbagging as explicit risk hypotheses.

### Useful artifacts

- Frontier-risk checklist.
- Capability eval plan.
- Containment channel map.
- Deception/evaluation-awareness probe plan.

## Chapter 15: How Models Work

**Official source:** https://www.testingaibook.com/knowledge/chapter-15.html

### Core idea

Tokenization, context limits, sampling, logits, reward tuning and multimodal pipelines create failure modes. Fine-tuning or preference optimization can improve a target behavior while regressing capabilities outside that target.

### Practical QA interpretation

- Include tokenization and context-boundary cases.
- Test sycophancy, verbosity, refusal and reward mismatch.
- Validate both extracted visual evidence and final VLM answers.
- Re-run broad regression after fine-tuning or model updates.

### Useful artifacts

- Mechanism-aware test list.
- Tokenization and cutoff checks.
- Preference-tuning risk list.
- VLM test set.
- Fine-tuning regression suite.

## Chapter 16: Introspection and White-Box Testing Networks

**Official source:** https://www.testingaibook.com/knowledge/chapter-16.html

### Core idea

Attention, activations, probes and sparse autoencoders can help triage model changes, but they are not proof of correctness or explanations of reasoning. Internal signals need their own validation against known-good, known-bad and ambiguous cases.

### Practical QA interpretation

- Start with the exact input and tokenization the model received.
- Compare internal signals across model versions and behavior labels.
- Use drift as a reason to focus behavioral evals, not as a release verdict.
- Treat every probe as an instrument with false positives and false negatives.

### Useful artifacts

- White-box diagnostic plan.
- Known-good/known-bad comparison set.
- Attention or activation triage report.
- Probe validation notes.

## Chapter 17: Personalized and Dynamic AI Products

**Official source:** https://www.testingaibook.com/knowledge/chapter-17.html

### Core idea

Personalized behavior may have one user and one context as its correct population. Dynamic content, layout, actions, tone, ranking, pricing, accessibility, privacy and memory become test surfaces.

### Practical QA interpretation

- Test personalization at N=1 without assuming it is untestable.
- Map dynamic UI variants and protect stable invariants.
- Validate synthetic personas against real traces and representative raters.
- Test memory inspection, correction, deletion, opt-out and portability.
- Check when the system should not personalize.

### Useful artifacts

- Personalization surface map.
- Persona and slice cases.
- Memory/privacy test plan.
- Dynamic UI regression suite.

### Relation to current work

This is relevant to UI-agent reliability and interface drift: an agent should be evaluated across versioned UI variants, not one golden screen.

## Chapter 18: Embodied and Long-Running AI Systems

**Official source:** https://www.testingaibook.com/knowledge/chapter-18.html

### Core idea

Simulation provides breadth, speed and safety, but critical cases still need physical validation. Long-running agents and robots require tests for safe inaction, recovery, permissions, memory drift, goal drift, retries, cost growth and human operators.

### Practical QA interpretation

- Score the plan, action path, recovery and final outcome.
- Include physical boundaries and fail-safe behavior.
- Test remote operator privacy and multi-agent handoffs.
- Use long-duration runs to expose delayed failures.

### Useful artifacts

- Robotics safety case.
- Simulation-to-physical validation plan.
- Long-run schedule.
- Operator privacy review.
- Multi-agent handoff test.

## Cross-Chapter Pattern

Chapters 12-18 expand the test surface beyond the model output:

1. Data and labels determine what quality means.
2. Tools and permissions determine what the system can do.
3. Internal mechanics can guide triage but do not replace behavior evidence.
4. Personalization and dynamic interfaces require variant and slice testing.
5. Long-running or embodied systems require recovery, containment and lifetime evidence.

## Sources

- [Official Knowledge Edition index](https://www.testingaibook.com/knowledge/index.html)
- [Full author draft preview](https://icebergqa.com/book/draft.html)
- [Testing AI book index in this wiki](testing-ai-book-index.md)

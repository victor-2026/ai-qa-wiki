# Keith Klain — Turns Out Testing is Hard (2026-09-21)

**Author:** Keith Klain (Quality Remarks)
**Source:** https://qualityremarks.com/turns-out-testing-is-hard/
**Context:** Companion post to "One Loop After Another". Analysis of "A Large-Scale Empirical Study of Quality Assurance Practices and Gaps in AI Agents" (arXiv:2609.17698, 157 open-source LLM-based agent projects). Coins term "novelty laundering". Date 2026-09-21.

---
Somebody did actual research on testing agentic systems and accidentally found out good software testing is hard. Klain coins: **Novelty laundering** — taking an old, well-established idea, ignoring its history and prior scholarship, rebranding it in fashionable terminology, and presenting it as a new discovery.

Paper: "A Large-Scale Empirical Study of Quality Assurance Practices and Gaps in AI Agents" (arXiv:2609.17698), 157 open-source LLM-based agent projects: source code, config, documentation, tests, deployment artifacts, CI workflows.

Findings: lots of testing going on but frequently incomplete, didn't cover the entire workflow through which an agent can actually do something.
- 137/157 had some basic functional testing
- 95 had security/safety-oriented tests
- 78 contained some combination of evaluations, benchmarking, or red-team-like paths
- Only 8 contained explicit prompt-injection, adversarial, jailbreak or red-team testing paths of the kind researchers looked for

Agents shouldn't be evaluated just by inspecting outputs. Need to understand what happens as actions pass through tools, APIs, permissions, states and external services. Main problem isn't the absence of QA artifacts but whether those artifacts cover the "complete model-to-action workflow".

Chain types named: execution surfaces, safeguards, model-to-process chains, extension-to-authority chains, workspace-to-persistent-state chains, session-to-action chains, mode-switch-to-privilege chains.

Klain's translation: the technical term for all this is **System testing**.

Why aren't they tested? Developers don't know they need to; don't know how; the rush to turn everything agentic is outrunning our ability to understand; cynically, from a conference: "they don't like all this governance slowing me down" (covered in a future post).
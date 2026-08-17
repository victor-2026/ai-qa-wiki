---
source: "offline-evaluation-trajectories-2026.md"
ingested: "2026-06-18"
---

# Offline Evaluation of AI Test Agents with Trajectories  

**Author:** Anton Gulin (2026)  
**Source:** anton.qa / LinkedIn  

---

## Summary  
Offline evaluation turns the “green‑check” of AI‑generated tests into a measurable quality score. By recording an agent’s execution as a **trajectory**—a detailed log of observations, decisions, and generated code—you can replay the run later, apply a rubric, and obtain numeric grades for correctness, relevance, stability, and coverage. Because the replay uses no live model calls, scoring is cheap, repeatable, and suitable for CI gating on every pull request. This evidence‑layer completes the typical three‑layer testing stack (orchestration, execution, evidence) and lets teams trust AI agents the same way they trust human engineers.

---

## Model Evals vs Downstream QA Validation

Trajectory and model evaluations measure the behavior of the AI agent: tool choice, call order, argument shape, task correctness, relevance, safety, stability, and cost. They can be scored against a golden dataset, rubric, or K-of-N invariant without executing the generated artifact in the real product.

Downstream QA validation starts after the agent produces code or tests. It runs the artifact against the target system using contract, integration, E2E, mutation, fault-injection, and state-verification checks. It answers a different question: did the software behavior work in the tested scope?

A passing downstream test is not a model eval, and a passing trajectory is not proof that the downstream system applied the requested side effect. Use both layers. See [AI QA Evidence Layer: Validation, Evals, Guardrails, and Telemetry](ai-qa-evidence-layer-validation-evals-guardrails-telemetry.md) for the complete distinction.

## Key Concepts  

| Concept | What it means | Why it matters |
|---------|---------------|----------------|
| **Trajectory** | Serialized record of an agent’s run (inputs, decisions, produced test code). | Provides a permanent receipt that can be inspected repeatedly. |
| **Offline Replay** | Loading a saved trajectory and running the evaluation logic locally, without contacting the LLM. | Eliminates API cost, network flakiness, and ensures deterministic scoring. |
| **Rubric / Evaluation Types** | Functions that assign scores on axes such as **correctness**, **relevance**, **stability**, **coverage**. | Gives granular insight; a single pass/fail hides failure modes. |
| **Evidence Layer** | The third layer of a testing system that proves the generated work is right, not just runnable. | Bridges the gap between “tests passed” and “tests are meaningful”. |
| **CI Gate** | CI step that fails the build if the trajectory’s scores fall below thresholds. | Enforces quality automatically, similar to code review standards. |

---

## Practical Applications  

1. **Continuous Integration** – Add a CI job that loads each new trajectory, evaluates it against a shared rubric, and blocks merges when scores dip (e.g., correctness < 0.8 or any flaky tests).  
2. **Regression‑Safe AI Agents** – Keep trajectories in version control; when the rubric evolves, re‑score historic runs to detect regressions without re‑executing the agent.  
3. **Metric‑Driven Development** – Track score trends over time to quantify improvements in the agent’s test‑writing capabilities.  
4. **Edge‑Case Assurance** – Use the coverage axis to force the agent to generate tests for known failure scenarios, reducing production bugs.  
5. **Cost‑Effective Scaling** – Because replay incurs no LLM calls, teams can evaluate thousands of runs per day, enabling large‑scale PR validation.

**Typical workflow (pseudocode)**  

```ts
// 1️⃣ Record
const traj = await agent.run(task, { record: true });
await saveTrajectory(traj, "runs/checkout.json");

// 2️⃣ Replay & score
const saved = await loadTrajectory("runs/checkout.json");
const score = await evaluate(saved, rubric);

// 3️⃣ CI gate
if (score.correctness < 0.8 || score.stability < 1) process.exit(1);
```

---

## Related Topics  

- **Stagehand 3.5** – The framework that introduced first‑class trajectory handling and evaluation APIs.  
- **Prompt Engineering for Test Generation** – Crafting prompts that guide agents toward higher‑quality test code.  
- **Flaky Test Detection** – Techniques for identifying nondeterministic failures, complementary to the stability metric.  
- **AI‑Assisted Code Review** – Using LLMs to comment on trajectories before they are merged.  
- **Observability in AI Systems** – Recording and analyzing internal agent states, of which trajectories are a concrete example.  

---  

By recording, replaying, and scoring trajectories, teams move from “the agent thinks it passed” to “the agent proved it passed”, establishing a reliable evidence layer for AI‑driven testing.





<!-- backlinks-start -->
### Backlinks
- [Carbon Ai Agentic Verification Harness](wiki/carbon-ai-agentic-verification-harness.md)
<!-- backlinks-end -->

---
*Generated by wiki_llm.py (Groq) — ingested from `raw/offline-evaluation-trajectories-2026.md`*

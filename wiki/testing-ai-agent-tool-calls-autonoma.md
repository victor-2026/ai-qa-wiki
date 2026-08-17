---
source: "testing-ai-agent-tool-calls-autonoma.md"
ingested: "2026-08-06"
---

## How to Test AI Agents That Take Actions (Tool Calls)

**Source:** https://getautonoma.com/blog/testing-ai-agent-tool-calls  
**Author:** Tom Piaggio, Co‑Founder, Autonoma  
**Date:** July 2026  

### Summary
When an LLM‑driven agent invokes external tools, the testable artifact is the **trajectory** – the ordered list of tool calls together with the arguments supplied.  
Trajectory evaluation is a white‑box technique that checks *what* the agent decided to call, *when* it called it, and *with which data*. It does **not** guarantee that the downstream system behaved correctly; that requires a separate outcome‑verification layer. The most common failure mode is wrong arguments, followed by incorrect ordering and, rarely, the wrong tool altogether.

### Key Concepts  

| Concept | What it means | Why it matters |
|---------|---------------|----------------|
| **Trajectory evaluation** | Capture the full sequence of tool calls and their payloads after execution. | Gives a deterministic view of the agent’s decision logic, independent of external side‑effects. |
| **Six assertion types** (each implemented as a pytest file) | 1️⃣ *Right tool* – the expected tool appears, unwanted tools are absent.<br>2️⃣ *Right order* – calls follow the logical dependency (e.g., search before booking).<br>3️⃣ *Right arguments* – payload matches the user intent (the highest‑value check).<br>4️⃣ *Mock vs. live* – mock calls for speed vs. live calls for effect verification.<br>5️⃣ *Failure handling* – inject transient/permanent errors and assert proper retry or explicit failure.<br>6️⃣ *Non‑determinism* – run the scenario N times, require K successes, and assert on invariants (tool name, argument shape) rather than exact strings. | Together they cover selection, sequencing, data correctness, robustness, and stochastic behaviour. |
| **K‑of‑N gating** | A test passes only if at least K out of N runs meet the invariant criteria. | Prevents flaky passes from masking real issues while still allowing probabilistic models to be exercised. |
| **CI wiring** | Combine deterministic checks and the K‑of‑N gate inside the same required job step; surface the raw pass‑rate in the job summary. | Makes regressions visible as a trend rather than a binary green/red flag. |
| **Outcome verification gap** | Trajectory tests stop at the call boundary; downstream failures (e.g., a booking service that silently drops the write) remain undetected. | Requires a complementary behavioural E2E layer that observes the real system state. |
| **Autonoma’s role** | Provides the behavioural E2E layer: a planner derives expected flows, an executor drives the UI, and a diffing agent measures coverage. | Couples the white‑box trajectory view with black‑box outcome validation, giving a full picture of agent correctness. |

### Practical Applications  

1. **Implementing the six assertions**  
   *Create a pytest module per assertion.*  
   - Use a **ScriptedLLM** or similar fake to produce deterministic trajectories for the first three assertions.  
   - For mocking, replace real tool endpoints with lightweight stubs that record the call.  
   - For live verification, let the tool run against a test environment and query the resulting state (e.g., database row, UI element).  

2. **Handling non‑determinism**  
   - Define invariants such as `tool == "book_flight"` and `isinstance(date, str) and len(date) in {10, 8}`.  
   - Run the scenario, say, 20 times; require at least 18 successes (K‑of‑N).  
   - If the pass‑rate drifts, treat the test as a signal to tighten prompts or tool descriptions.  

3. **CI integration**  
   - Add a single required check that executes the deterministic suite plus the K‑of‑N gate.  
   - Emit a summary line like `Trajectory tests: 17/20 passed` so trends can be plotted over builds.  

4. **Coupling with outcome tests**  
   - After a trajectory passes, trigger an Autonoma‑driven E2E flow that validates the real effect (e.g., the flight appears in the user's itinerary).  
   - Use the outcome layer to pinpoint whether a failure originated in tool selection, argument formation, or downstream processing.  

5. **Fault‑injection for robustness**  
   - Simulate transient network errors or permanent authentication failures in the tool stub.  
   - Assert that the agent retries appropriately or surfaces the error without falsely reporting success.  

6. **Reusing the pattern across projects**
    - The 6‑assertion + K‑of‑N model maps directly onto existing LLM‑testing skills (boundary prompts, golden datasets, soft asserts).
    - It complements other AI‑testing assets such as `testing-ai-generated-auth-code` and `copilot-generated-tests`.

### Three Separate Evaluation Questions

Trajectory evaluation checks the agent's decision process: which tool it selected, in what order, and with which arguments. Downstream QA validation checks the real outcome after the tool call: whether the application, database, or external service reached the expected state. Model or agent evals additionally test whether the AI behavior generalizes across a benchmark of tasks, safety cases, and repeated runs.

A green trajectory test is not proof of a successful side effect. A green E2E test is not proof that the model is safe on unseen prompts. A complete AI QA evidence layer combines all three views. See [AI QA Evidence Layer: Validation, Evals, Guardrails, and Telemetry](ai-qa-evidence-layer-validation-evals-guardrails-telemetry.md).

### See also
- [Copilot Generated Tests Quality Pitfalls Autonoma](wiki/copilot-generated-tests-quality-pitfalls-auton


<!-- backlinks-start -->
### Backlinks
- [Carbon Ai Agentic Verification Harness](wiki/carbon-ai-agentic-verification-harness.md)
<!-- backlinks-end -->

---
*Generated by wiki_llm.py (Groq) — ingested from `raw/testing-ai-agent-tool-calls-autonoma.md`*

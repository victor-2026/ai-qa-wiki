# How to Test AI Agents That Take Actions (Tool Calls)

- **Source:** https://getautonoma.com/blog/testing-ai-agent-tool-calls
- **Author:** Tom Piaggio, Co-Founder at Autonoma
- **Date:** July 2026
- **Companion code:** https://github.com/Autonoma-Tools/testing-ai-agent-tool-calls (framework-neutral Python harness + pytest, all tests pass)

## Key thesis

Testing tool-calling agents means verifying the **trajectory**: the ordered list of tool calls the agent made, with what arguments, captured and inspected after the fact. This is **trajectory evaluation** — a white-box check on tool selection, call order, and argument accuracy. An agent can pass all three and still be wrong, because none confirm the tool's effect on the running application was correct.

Failure frequency: wrong arguments most often → wrong order less often → wrong tool rarest (once a system has real usage).

## The 6 assertion types (each = one pytest file)

1. **Right tool** — cheapest: does `book_flight` appear, does `get_weather` stay out. Catches reaching for entirely wrong capability. Least informative — says nothing about whether the call was useful.
2. **Right order** — search-then-book dependency; 3-tool trajectories are where teams get bitten (reordering under rephrased prompts). A weather check the user asked for, running after booking, is not the trajectory anyone asked for.
3. **Right arguments** — highest-value, most-skipped. Argument accuracy separates "the agent worked" from "the agent did what the user asked". `test_right_tool_wrong_argument_is_still_a_real_failure` is the through-line: right tool, wrong date → outcome wrong. **If you ship only one assertion type, ship this one.**
4. **Mocking vs live** — mock + assert on CALL = fast, isolates decision logic. Live tool + assert on EFFECT (record actually in app state) = only way to know the action landed. Neither replaces the other.
5. **Failure handling** — inject tool error; transient → assert retry succeeded; permanent → assert trajectory shows error explicitly AND no false-success state (an agent that swallows the exception and reports success is worse than one that visibly errors).
6. **Non-determinism** — run N times, require K of N, assert on the **invariant** (tool name, argument shape/type) not the exact string. `date == '2026-08-01'` breaks when model reformats to `08/01/2026`. Flakiness in K-of-N eval = signal about the test (assertion too strict, or tool description/prompt ambiguous), not a verdict on the model.

## CI wiring

Deterministic tests + K-of-N gate in the **same required check**. A K-of-N gate outside required checks is a gate nobody enforces. Report pass rate in job summary (17/20, not green checkmark) so a slow decline shows as a trend.

## The gap trajectory tests don't cover

Trajectory tests are white-box, stop at the boundary of the call. Right tool + right args can still fail if booking service drops the write, downstream queue never processes, or UI never reflects state. **Outcome verification = separate layer** (behavioral E2E against running app).

## Autonoma's positioning (vendor angle)

Autonoma = behavioral E2E layer: Planner derives expected flows from codebase, Executor drives real UI, Diffs Agent maintains coverage. Trajectory tests tell you the call was well-formed; Autonoma tells you the thing the call was supposed to do actually happened where a user would see it. Both layers needed: trajectory alone can't confirm effect; outcome tests alone wouldn't narrow down whether it was selection/ordering/arguments.

## Relevance to QA / resonance with our work

- **Directly reusable pattern** — the 6 assertions + K-of-N + invariant-based checks map to our LLM testing skill (llm-testing: boundary prompts, golden datasets, soft asserts) and fault-injection (Meta ACH mutation pattern).
- The `ScriptedLLM` fake → deterministic trajectory testing is the same trick as our Playwright test fixtures / Go table-driven tests.
- K-of-N non-determinism handling = the same lesson as our flaky-test work (Chatbot Automation Testing article resonates).
- Complements `testing-ai-generated-auth-code` and `copilot-generated-tests`: all three say AI-verification needs a source of truth independent of the AI's output — here it's "assert on arguments, not just tool names" and "verify the effect, not the call".
- Resolves DevAssure O2 lesson: the agent's JS-injection FP was an "effect vs call" confusion — trajectory said "input submitted", outcome was the app accepted a literal string.

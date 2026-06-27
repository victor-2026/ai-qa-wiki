# How to Score Your AI Test Agents: Offline Evaluation with Trajectories

**Author:** Anton Gulin  
**Source:** anton.qa / LinkedIn (2026)  
**Format:** Article  
**Tags:** #testing #ai #automation #playwright #evaluation #evidence-layer

---

AI test agent evaluation is the practice of scoring the tests an AI agent writes, instead of trusting that they pass. You record the agent's run as a trajectory (a saved log of every step), replay it offline, and grade each step for correctness and relevance. Offline scoring needs no live API calls, so you can check agent quality on every pull request.

An AI agent can write 200 tests before lunch. That feels like progress.

Then a real bug ships, and not one of those tests caught it. The agent was confident, and it was wrong.

This guide shows how to stop guessing and start scoring. Stagehand 3.5.0 made the method first-class on June 3, 2026, but the pattern works for any agent.

## 1. "It passed" is not a score

A green test suite tells you the tests ran. It does not tell you the tests were right.

An AI agent makes three mistakes a human reviewer would catch:

- It checks the wrong thing. The test passes, but it never asserts the real behavior.
- It writes flaky tests (tests that fail at random). They go green often enough to look fine.
- It tests a happy path and skips the edge case that actually breaks.

You cannot fix what you cannot measure. So the first job is a number, not a vibe.

## 2. Record the run as a trajectory

A trajectory is a saved recording of an agent's run. It captures each step: what the agent saw, what it decided, and what code it produced.

You capture it once, during the agent's normal run.

```typescript
// Illustrative pattern — confirm the exact Stagehand 3.5 API before use.
const trajectory = await agent.run(task, { record: true });
await saveTrajectory(trajectory, "runs/checkout-flow.json");
```

The recording is the receipt. Now you can study the run after it finishes, as many times as you want.

## 3. Replay it offline

Offline means you grade the saved run without calling the live model again. No new API cost. No flaky network. Same input every time.

This matters for two reasons. It makes scoring cheap, so you can run it on every pull request. It makes scoring repeatable, so two engineers get the same result.

```typescript
// Replay the saved run and score it, with no live API calls.
const run = await loadTrajectory("runs/checkout-flow.json");
const score = await evaluate(run, rubric);
```

## 4. Score each step with evaluation types

A single pass/fail hides too much. Grade the run on a few clear axes instead.

- **Correctness:** did the test assert the behavior the task asked for?
- **Relevance:** does each step move toward the goal, or wander?
- **Stability:** would this test pass on a clean re-run, or is it flaky?
- **Coverage:** did the agent test the edge case, or only the happy path?

Stagehand 3.5.0 added evaluation types for exactly this kind of offline scoring. You define the rubric once and apply it to every saved run.

```typescript
const rubric = {
  correctness: (run) => run.asserts.some(a => a.target === task.goal),
  relevance:   (run) => run.steps.every(s => s.onTask),
  stability:   (run) => run.reruns.every(r => r.passed),
};
```

A run that scores correctness 7/10, relevance pass, flaky tests 0 is a run you can talk about. "It passed" is not.

## 5. Wire the score into CI

A score you read once and forget changes nothing. Turn it into a gate.

```yaml
# CI step: fail the build if the agent's tests score too low.
- run: npx evaluate runs/ --min-correctness 0.8 --max-flaky 0
```

Now the agent earns trust the same way a junior engineer does. It ships work, the work gets graded, and only graded work reaches production.

## 6. Where this sits: the Evidence Layer

I design AI test systems on a 3-Layer System:

- **Orchestration:** decides what to test.
- **Execution:** runs the tests, where the agent writes code.
- **Evidence:** proves the work is right.

Most teams build the first two layers and stop. They let the agent write tests and assume the green check means quality.

Offline evaluation is the Evidence Layer. It is the difference between an agent you hope works and an agent you can prove works.

## The 5-line checklist

1. Record every agent run as a trajectory.
2. Replay it offline, with no live API calls.
3. Score it on correctness, relevance, stability, and coverage.
4. Gate your build on the score.
5. Keep the trajectory, so you can re-grade when the rubric improves.

Build the agent. Then prove it works.

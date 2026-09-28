# Source: QA Wolf — "Semantic assertions: Using Jev to make rigid tests flex"

**URL:** https://www.qawolf.com/blog/semantic-assertions-using-jev
**Author:** Goran Gajic · **Published:** September 25, 2026
**Fetched:** 2026-09-27 (webfetch, markdown). LinkedIn post: Goran Gajic (Staff Engineering Lead, 2nd), 3d.

---

AI

# Semantic assertions: Using Jev to make rigid tests flex

Goran Gajic, September 25, 2026

Jev doesn't write prose or hold a conversation. Give it some state and a set of typed questions, and it returns decisions with probabilities. That turns out to be really useful for end-to-end regression testing.

E2E tests need to be deterministic to be trustworthy. But not every variation in a workflow is a failure.

Take an AI support assistant. It might say, "Your package is on the way" one day and "Your order has shipped" the next. The wording changed, but the meaning didn't. Both responses are acceptable, yet an exact-match test would need to hardcode each one.

Or suppose you're A/B testing a new homepage and the Support link moves inside a menu. A test tied to the original path would fail, create noise, and need to be rewritten — even if the workflow still reaches the same correct state.

With Jev, we created two AI primitives for Playwright that let the test author (human or agent) draw a boundary between what may vary and what must remain exact. Jev judges the variation within that boundary; Playwright enforces the fixed requirements:

- `ai.expect(...).toSatisfy(...)` handles variation in generated language.
- `ai.act(...)` handles variation in the route to a known state.

These are separate use cases built on the same design principle: code owns the workflow and requirements, while Jev supplies narrow judgments where rigid rules become brittle.

## Let the words vary, not the requirement

```javascript
import { expect } from '@qawolf/flows/web';

await expect(page.getByTestId('assistant-reply')).toSatisfy(
  'The reply confirms the order has shipped'
);
```

"The parcel is on its way" can pass because it conveys the required meaning. "We're preparing your order" should fail because it does not confirm shipment.

Jev is well suited to this question because the answer is bounded. It does not need to generate a better response. It only needs to judge whether the observed response satisfies the requirement.

That judgment does not replace exact assertions. Playwright still opens the page, submits the request, and checks exact state. Jev appears only at the point where exact string matching would reject valid behavior.

## Verify what the application actually did

Language is not proof of an outcome. A support assistant can say it referred an issue to the delivery team without creating a ticket.

The product requirement has two parts:
1. Create an open ticket for the correct order and queue.
2. Tell the customer that the issue was referred to the delivery team.

The explanation may vary. The ticket may not.

Illustrative flow (example app, replace routes/selectors): order ORD-1042, delayed shipment, fresh support conversation. Ticket exposed at `POST /api/support/tickets` returning 201 only after saving. Reply element gets `data-generation-state="complete"` when generation finishes.

```javascript
await page.getByRole('button', { name: 'Send', exact: true }).click();
const response = await ticketCreated;
expect(response.status()).toBe(201);
const ticket = await response.json();
expect(ticket.orderId).toBe('ORD-1042');
expect(ticket.queue).toBe('delivery');
expect(ticket.status).toBe('open');
// ... then:
await ai.expect(reply).toSatisfy(
  'The reply tells the customer their delivery issue has been referred ' +
    'to the delivery team for investigation',
  { context: { customerRequest: request } }
);
```

The division of responsibility is explicit. Playwright verifies that the application returned 201 and saved an open ticket. Those are fixed requirements. If no ticket exists, the test fails no matter how convincing the assistant sounds. Jev evaluates whether the reply accurately communicates the handoff.

Use semantic assertions for generated language. Use exact assertions for structured state, side effects, and required copy. Because `toSatisfy` evaluates text, wait for generation to finish and check visibility separately. **Uncertain judgments and evaluator errors fail the assertion.**

Jev's typed output prevents it from returning an answer outside the expected shape. That does not make every judgment correct. Write specific requirements, supply relevant context, and validate the assertion with positive and negative examples.

## Let the route vary only when the route does not matter

```javascript
await act(page, 'Open the support conversation composer', {
  maxSteps: 5,
  timeout: 30_000,
});
```

At each step, Jev chooses among observed controls or determines whether the goal has been reached. Playwright executes the selected actions. Step and time limits bound the attempt. The test then uses exact assertions to verify the resulting state.

The test author still decides whether this flexibility is appropriate. **If onboarding is the behavior under test, the onboarding steps should be explicit. Letting `act` find another route could hide the defect the test is supposed to catch.**

That is the governing rule for both primitives: permit variation only outside the requirement.

## Fewer false failures, less test maintenance

With `toSatisfy`, a test does not need to be updated every time generated copy changes while preserving the same meaning. A failure is more likely to indicate that the response missed the requirement — not that it chose a new phrase.

With `act`, a test can get through small UI variations without hardcoding every acceptable route. Moving a link into a menu does not have to create a false failure or an immediate maintenance task when the route itself is not under test.

The rest of the flow remains ordinary Playwright. Exact assertions still verify the states and side effects that matter, so flexibility in one part of the test does not make the entire test ambiguous.

## Judgment without surrendering control

A QA Wolf test can allow an assistant to choose different words without allowing it to misrepresent what happened. It can allow different routes to a support composer without allowing the final state to be wrong. Jev handles those bounded judgments. Playwright executes the workflow and enforces the requirements.

The goal is not to make every part of the test probabilistic. It is to put judgment exactly where the product permits variation — and nowhere else.

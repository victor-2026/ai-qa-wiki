# Test Stability & Anti-Flakiness

**Last Updated:** 2026-04-17
**Sources:** raw/anti-flakiness-habr.md

---

## The Problem

Even with clean code, tests fail irregularly. Once in 10 runs, more often in CI than locally. Not because CI is special, but because:
- Less CPU
- Higher latency between services
- Multiple parallel processes

**The root cause:** Timing. Frontend renders, backend still processing, database transaction not committed. Test checks and doesn't find expected result.

## Anti-Pattern: waitForTimeout

```
await page.getByText('Submit').click();
await page.waitForTimeout(5000);  // ❌ BAD
const order = await api.getOrder(id);
expect(order.status).toBe('PAID');
```

In CI under load, backend responds in 5001ms → test fails.

## Solution 1: expect.poll

Poll system instead of guessing time:

```
await expect.poll(async () => {
  const order = await api.getOrder(id);
  return order.status;
}, {
  message: 'Waiting for order status PAID',
  timeout: 30000,
}).toBe('PAID');
```

> `expect.poll` appeared in Playwright 1.25.

**Tip:** Don't manually set intervals unless you have specific reason. Let Playwright choose reasonable pauses.

## Solution 2: expect.toPass

Repeat entire block when you need to retry action + UI check:

```
await expect(async () => {
  await page.getByRole('button', { name: 'Refresh' }).click();
  await expect(page.getByText('Status: Ready')).toBeVisible();
}).toPass({
  intervals: [1000, 2000, 5000],
  timeout: 15000
});
```

Here intervals make sense because we control retry frequency.

## Anti-Pattern: networkidle

`waitUntil: 'networkidle'` is unreliable. Playwright considers network "idle" after 500ms of silence. If analytics widget pings every 400ms, test hangs forever.

**Rule:** Wait for specific element or API response, not "network silence".

## Idempotency: Insurance Against Duplicates

In distributed systems, network flickers. If request reaches backend, order created, but response lost → duplicate orders on retry.

### Solution: Idempotency-Key

```
// api/infrastructure/Idempotency.ts
import { createHash } from 'crypto';

export function generateIdempotencyKey(method: string, url: string, data: any): string {
  const payload = `${method}:${url}:${JSON.stringify(data)}`;
  return createHash('sha256').update(payload).digest('hex').slice(0, 16);
}
```

```
// api/clients/BaseApiClient.ts
protected async post(url: string, data?: any) {
  const key = generateIdempotencyKey('POST', url, data);
  return await this.request.post(url, {
    data,
    headers: { 'X-Idempotency-Key': key }
  });
}
```

Each unique request gets unique key automatically.

## Mock Evolution

### Level 1: Native Mocks (page.route)

Good for UI isolation:

```
await page.route('**/api/orders', route => {
  route.fulfill({
    status: 500,
    body: JSON.stringify({ error: 'Internal Server Error' })
  });
});
```

> `page.route` doesn't intercept server-side requests via `request` fixture.

### Level 2: Infra Mocks (WireMock)

For external services (payment, SMS, courier):

```
# docker-compose.yml
services:
  wiremock:
    image: wiremock/wiremock:3.3.1
    ports:
      - "8080:8080"
```

### Level 3: Contract Testing (Pact)

Protects against **lying mocks** — when backend changed API but mock wasn't updated.

```typescript
import { PactV3, MatchersV3 } from '@pact-foundation/pact';

const provider = new PactV3({
  consumer: 'frontend-tests',
  provider: 'order-service',
  dir: './pacts',
});

provider
  .given('order ord_123 exists')
  .uponReceiving('GET /orders/ord_123')
  .withRequest({ method: 'GET', path: '/orders/ord_123' })
  .willRespondWith({
    status: 200,
    body: { order_id: MatchersV3.string('ord_123') }
  })
  .executeTest(async (mockServer) => {
    const order = await fetchOrder(mockServer.url, 'ord_123');
    expect(order.status).toBe('PAID');
  });
```

Provider verifies contract against real code.

## Data Hygiene

Tests that create users/orders/transactions must clean up. Otherwise test DB becomes garbage.

### Approach 1: TTL (Time To Live)

```
await api.createUser({
  email: `test_${Date.now()}@example.com`,
  expires_at: new Date(Date.now() + 24 * 60 * 60 * 1000).toISOString()
});
```

PostgreSQL cleanup via pg_cron:
```
SELECT cron.schedule('cleanup-test-data', '0 * * * *', $$
  DELETE FROM users WHERE expires_at < NOW() AND is_test = true;
$$);
```

### Approach 2: Cleanup Queue

```
protected async post(url: string, data?: any) {
  const response = await this.request.post(url, { data });
  const body = await response.json();
  if (body.id) {
    cleanupQueue.push({ url, id: body.id });
  }
  return response;
}

// global teardown
for (const item of cleanupQueue) {
  await api.delete(`${item.url}/${item.id}`);
}
```

### Approach 3: Partitioning

For high-load projects:
```
CREATE TABLE orders_test (...) PARTITION BY RANGE (created_at);
CREATE TABLE orders_test_2024_06 PARTITION OF orders_test
  FOR VALUES FROM ('2024-06-01') TO ('2024-07-01');
```

Drop partition = instant operation.

## Quick Reference

| Pattern | Tool | When to Use |
|---------|------|-------------|
| Dynamic wait | `expect.poll` | Check system state |
| Retry action | `expect.toPass` | Click + check UI |
| Duplicate protection | Idempotency-Key | POST requests |
| UI isolation | `page.route` | Test frontend behavior |
| External service isolation | WireMock | Test without dependencies |
| API contract protection | Pact | Consumer-Driven Contracts |
| Auto-cleanup | TTL + Cleanup Queue | Guaranteed hygiene |

## Related

- [[wiki/testing-strategies]] — Testing approaches
- [[wiki/agentic-patterns]] — Agentic testing

## Sources

- raw/anti-flakiness-habr.md

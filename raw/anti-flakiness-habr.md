# Анти-флаккинес: Вы всё сделали правильно. Тест всё равно упал

**Источник:** https://habr.com/ru/articles/1019950/  
**Автор:** playwright_no_hero  
**Дата:** 6 апр  
**Хабы:** Тестирование IT-систем, Тестирование веб-сервисов

---

Даже с чистым кодом тесты могут падать с завидной нерегулярностью. Раз в десять прогонов, чаще в CI, чем локально. Не потому что CI какой-то особенный, а потому что там может быть меньше CPU, выше latency между сервисами и куча параллельных процессов.

## 1. Хватит угадывать время. Принцип Наблюдателя

### waitForTimeout — не решение

```
await page.getByText('Оформить заказ').click();
await page.waitForTimeout(5000);  // ПЛОХО
const order = await api.getOrder(id);
expect(order.status).toBe('PAID');
```

В CI под нагрузкой бэкенд ответит за 5001 мс, и тест упадёт.

### expect.poll — спрашиваем систему

```
await expect.poll(async () => {
  const order = await api.getOrder(id);
  return order.status;
}, {
  message: 'Ожидаем, что статус заказа станет PAID',
  timeout: 30000,
}).toBe('PAID');
```

> `expect.poll` появился в Playwright 1.25.

### Ловушка networkidle

`waitUntil: 'networkidle'` работает плохо — Playwright ждёт 500 мс тишины. Если виджет шлёт пинги раз в 400 мс, тест висит бесконечно.

**Правило:** ждите конкретный элемент или ответ API, а не «тишину в сети».

### expect.toPass — повтор целого блока

```
await expect(async () => {
  await page.getByRole('button', { name: 'Обновить' }).click();
  await expect(page.getByText('Статус: Готов')).toBeVisible();
}).toPass({
  intervals: [1000, 2000, 5000],
  timeout: 15000
});
```

## 2. Идемпотентность — страховка от сетевого шума

Проблема: первый запрос до бэкенда дошёл, заказ создался, а ответ до теста — нет. При повторной попытке — `400 Order already exists` или два заказа.

### Idempotency-Key

```typescript
// api/infrastructure/Idempotency.ts
import { createHash } from 'crypto';

export function generateIdempotencyKey(method: string, url: string, data: any): string {
  const payload = `${method}:${url}:${JSON.stringify(data)}`;
  return createHash('sha256').update(payload).digest('hex').slice(0, 16);
}

// api/clients/BaseApiClient.ts
export abstract class BaseApiClient {
  protected async post(url: string, data?: any) {
    const key = generateIdempotencyKey('POST', url, data);
    return await this.request.post(url, {
      data,
      headers: { 'X-Idempotency-Key': key }
    });
  }
}
```

## 3. Эволюция моков

### Уровень 1: Native Mocks (page.route)

```
await page.route('**/api/orders', route => {
  route.fulfill({
    status: 500,
    body: JSON.stringify({ error: 'Internal Server Error' })
  });
});
```

> `page.route` НЕ перехватывает server-side запросы через `request` fixture.

### Уровень 2: Infra Mocks (WireMock)

```
# docker-compose.yml
services:
  wiremock:
    image: wiremock/wiremock:3.3.1
    ports:
      - "8080:8080"
    volumes:
      - ./wiremock/mappings:/home/wiremock/mappings
```

```
// wiremock/mappings/payment.json
{
  "request": { "method": "POST", "url": "/v1/payments" },
  "response": {
    "status": 200,
    "jsonBody": { "payment_id": "pay_test_123", "status": "succeeded" }
  }
}
```

### Уровень 3: Contract Testing (Pact)

Consumer-Driven Contract Testing защищает от "лживых моков" — когда бэкенд изменил API, а мок не обновили.

```typescript
// consumer: tests/contracts/order.pact.spec.ts
import { PactV3, MatchersV3 } from '@pact-foundation/pact';

const provider = new PactV3({
  consumer: 'frontend-tests',
  provider: 'order-service',
  dir: './pacts',
});

describe('Order API contract', () => {
  it('возвращает заказ по id', async () => {
    await provider
      .given('заказ ord_123 существует')
      .uponReceiving('GET /orders/ord_123')
      .withRequest({ method: 'GET', path: '/orders/ord_123' })
      .willRespondWith({
        status: 200,
        body: {
          order_id: MatchersV3.string('ord_123'),
          status: MatchersV3.string('PAID'),
        },
      })
      .executeTest(async (mockServer) => {
        const order = await fetchOrder(mockServer.url, 'ord_123');
        expect(order.status).toBe('PAID');
      });
  });
});
```

Provider verification:
```
pact-provider-verifier \
  --provider-base-url http://localhost:8080 \
  --pact-broker-url https://your-pact-broker \
  --provider order-service
```

## 4. Гигиена данных

Тесты, которые не убирают за собой, убивают окружение.

### TTL (Time To Live)

```
await api.createUser({
  email: `test_${Date.now()}@example.com`,
  expires_at: new Date(Date.now() + 24 * 60 * 60 * 1000).toISOString()
});
```

PostgreSQL cleanup через pg_cron:
```
SELECT cron.schedule('cleanup-test-data', '0 * * * *', $$
  DELETE FROM users WHERE expires_at < NOW() AND is_test = true;
$$);
```

### Cleanup Queue

```
protected async post(url: string, data?: any) {
  const response = await this.request.post(url, { data });
  const body = await response.json();
  if (body.id) {
    cleanupQueue.push({ url, id: body.id });
  }
  return response;
}

// глобальный teardown
for (const item of cleanupQueue) {
  await api.delete(`${item.url}/${item.id}`);
}
```

### Партиционирование

```
CREATE TABLE orders_test (...) PARTITION BY RANGE (created_at);
CREATE TABLE orders_test_2024_06 PARTITION OF orders_test
  FOR VALUES FROM ('2024-06-01') TO ('2024-07-01');
```

Drop партиции — мгновенная операция.

---

## Ключевые паттерны

| Паттерн | Инструмент | Когда использовать |
|---------|-----------|-------------------|
| Динамическое ожидание | `expect.poll` | Проверка состояния системы |
| Повтор действия | `expect.toPass` | Клик + проверка UI |
| Защита от дублей | Idempotency-Key | POST запросы |
| Изоляция UI | `page.route` | Проверка фронтенда |
| Изоляция внешних сервисов | WireMock | Тест без зависимостей |
| Защита от lying mocks | Pact | Consumer-Driven Contracts |
| Автоочистка | TTL + Cleanup Queue | Гарантированная гигиена |

---

## Полезные ссылки

- [Playwright BDR Template](https://github.com/dmitryAQA/playwright-bdr-template)
- [BDR Methodology Manifesto](https://github.com/dmitryAQA/bdr-methodology)

## Теги

`автотестирование` `playwright` `qa automation` `флаккинес`

---
title: "Pact Contract Testing — Полное руководство"
type: article
updated: "2026-08-17"
tags: [contract-testing]
---

# Pact Contract Testing — Полное руководство

## Что такое Pact

Pact — инструмент для consumer-driven contract testing (CDCT). Потребитель API (consumer) записывает ожидания от провайдера (provider) в файл-контракт (Pact file), а провайдер верифицирует, что реальный код удовлетворяет этим ожиданиям.

**Отличие от WireMock/mocks:** Pact не просто мокает — он проверяет, что реальный сервер выполняет контракт.

---

## Архитектура

```
Consumer                           Pact Broker                    Provider
   │                                    │                           │
   ├── 1. Пишет тест ───────────►        │                           │
   │    (pact file)                      │                           │
   │                                    ├── 2. Публикует pact ───►  │
   │                                    │                           ├── 3. Верифицирует
   │                                    │                           │    (реальный код)
   │                                    │◄── 4. Результат ──────────┤
   │◄── 5. Можно деплоить ──────────────┤                           │
```

---

## Установка

```bash
npm install --save-dev @pact-foundation/pact @pact-foundation/pact-core
# или
npm install --save-dev @pact-foundation/pact@latest
```

---

## Consumer Test — Полный пример (TypeScript/Playwright)

### Consumer: UserService (клиент, который дёргает API)

```typescript
// src/services/UserService.ts
export interface User {
  id: string;
  name: string;
  email: string;
  role: 'admin' | 'user';
}

export class UserService {
  constructor(private baseUrl: string) {}

  async getUser(id: string): Promise<User> {
    const res = await fetch(`${this.baseUrl}/users/${id}`);
    if (!res.ok) throw new Error(`HTTP ${res.status}`);
    return res.json();
  }

  async createUser(name: string, email: string, role: User['role']): Promise<User> {
    const res = await fetch(`${this.baseUrl}/users`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ name, email, role }),
    });
    if (!res.ok) throw new Error(`HTTP ${res.status}`);
    return res.json();
  }
}
```

### Consumer Pact Test

```typescript
// tests/contract/user-service.pact.spec.ts
import { PactV3, MatchersV3 } from '@pact-foundation/pact';
import { UserService } from '../../src/services/UserService';

const { like, eachLike, string, uuid, email } = MatchersV3;

const provider = new PactV3({
  consumer: 'frontend-app',
  provider: 'user-api',
  dir: './pacts',
  pactfileWriteMode: 'merge',   // merge с существующим, не перезаписывать
  logLevel: 'info',
});

describe('UserService consumer contract', () => {
  afterAll(() => provider.finalize());

  it('returns user by ID', async () => {
    provider
      .given('user usa_001 exists with role admin')    // состояние провайдера
      .uponReceiving('GET /users/usa_001')              // описание запроса
      .withRequest({
        method: 'GET',
        path: '/users/usa_001',
        headers: { Accept: 'application/json' },
      })
      .willRespondWith({
        status: 200,
        headers: { 'Content-Type': 'application/json' },
        body: {
          id: string('usa_001'),
          name: like('Alice'),
          email: email('alice@example.com'),
          role: string('admin'),
        },
      });

    await provider.executeTest(async (mockServer) => {
      const service = new UserService(mockServer.url);
      const user = await service.getUser('usa_001');

      expect(user.id).toBe('usa_001');
      expect(user.name).toBe('Alice');
      expect(user.role).toBe('admin');
    });
  });

  it('creates a new user', async () => {
    const newUser = {
      name: 'Bob',
      email: 'bob@example.com',
      role: 'user' as const,
    };

    provider
      .given('user creation is allowed')
      .uponReceiving('POST /users to create a new user')
      .withRequest({
        method: 'POST',
        path: '/users',
        headers: { 'Content-Type': 'application/json' },
        body: newUser,
      })
      .willRespondWith({
        status: 201,
        headers: { 'Content-Type': 'application/json' },
        body: {
          id: uuid('usr_abc123'),
          name: like(newUser.name),
          email: email(newUser.email),
          role: string(newUser.role),
        },
      });

    await provider.executeTest(async (mockServer) => {
      const service = new UserService(mockServer.url);
      const created = await service.createUser(newUser.name, newUser.email, newUser.role);

      expect(created.name).toBe(newUser.name);
      expect(created.email).toBe(newUser.email);
      expect(created.role).toBe(newUser.role);
      expect(created.id).toBeDefined();
    });
  });

  it('returns 404 for nonexistent user', async () => {
    provider
      .given('user nonexistent_999 does not exist')
      .uponReceiving('GET /users/nonexistent_999')
      .withRequest({
        method: 'GET',
        path: '/users/nonexistent_999',
        headers: { Accept: 'application/json' },
      })
      .willRespondWith({ status: 404 });

    await provider.executeTest(async (mockServer) => {
      const service = new UserService(mockServer.url);
      await expect(service.getUser('nonexistent_999')).rejects.toThrow('HTTP 404');
    });
  });
});
```

### Запуск consumer теста

```bash
npx jest tests/contract/user-service.pact.spec.ts
```

Результат: `./pacts/frontend-app-user-api.json` — файл-контракт.

### Пример сгенерированного Pact-файла

```json
{
  "consumer": { "name": "frontend-app" },
  "provider": { "name": "user-api" },
  "interactions": [
    {
      "description": "GET /users/usa_001",
      "providerStates": [
        { "name": "user usa_001 exists with role admin" }
      ],
      "request": {
        "method": "GET",
        "path": "/users/usa_001",
        "headers": { "Accept": "application/json" }
      },
      "response": {
        "status": 200,
        "headers": { "Content-Type": "application/json" },
        "body": {
          "id": "usa_001",
          "name": "Alice",
          "email": "alice@example.com",
          "role": "admin"
        }
      }
    }
  ],
  "metadata": {
    "pactSpecification": { "version": "4.0" }
  }
}
```

---

## Provider Verification

Provider должен запустить верификацию: поднять реальный код и прогнать pact-файлы через него.

### Provider Setup (Express.js)

```typescript
// src/server.ts
import express from 'express';

const app = express();
app.use(express.json());

const users: Record<string, any> = {
  usa_001: { id: 'usa_001', name: 'Alice', email: 'alice@example.com', role: 'admin' },
};

app.get('/users/:id', (req, res) => {
  const user = users[req.params.id];
  if (!user) return res.status(404).json({ error: 'not found' });
  res.json(user);
});

app.post('/users', (req, res) => {
  const { name, email, role } = req.body;
  const id = `usr_${Date.now()}`;
  users[id] = { id, name, email, role: role || 'user' };
  res.status(201).json(users[id]);
});

export { app };
```

### Provider Verification Test

```typescript
// tests/contract/user-api.verify.spec.ts
import { Verifier } from '@pact-foundation/pact';
import { app } from '../../src/server';

describe('user-api provider verification', () => {
  it('verifies all consumer contracts', async () => {
    const server = app.listen(4000);

    const options = {
      provider: 'user-api',
      providerBaseUrl: 'http://localhost:4000',
      pactUrls: [
        // Путь к pact-файлу от consumer
        'http://localhost:9292/pacts/provider/user-api/consumer/frontend-app/latest',
        // Или локальный файл:
        // path.resolve(__dirname, '../../../pacts/frontend-app-user-api.json'),
      ],
      stateHandlers: {
        'user usa_001 exists with role admin': async () => {
          // Подготовка данных на провайдере
          await setupTestData('usa_001', { role: 'admin' });
        },
        'user creation is allowed': async () => {
          // Ничего не нужно — POST /users всегда разрешён
        },
        'user nonexistent_999 does not exist': async () => {
          await removeTestData('nonexistent_999');
        },
      },
    };

    await new Verifier(options).verifyProvider();
    server.close();
  });
});
```

### Provider State Handlers

Provider states (`given(...)`) — это не условия, а **подготовка данных** на провайдере перед тестом:

```typescript
const stateHandlers = {
  // Consumer: "given user usa_001 exists with role admin"
  'user usa_001 exists with role admin': async () => {
    await db.users.upsert({ id: 'usa_001', role: 'admin' });
  },

  // Consumer: "given user nonexistent_999 does not exist"
  'user nonexistent_999 does not exist': async () => {
    await db.users.delete('nonexistent_999');
  },
};
```

### Provider CI-шаг

```bash
# Установить Pact Broker для обмена контрактами
docker run -d -p 9292:9292 pactfoundation/pact-broker

# Запустить верификацию
npx jest tests/contract/user-api.verify.spec.ts
```

---

## Matchers (типы совпадений)

Pact использует matchers, чтобы не проверять точное значение, а только тип/формат:

| Matcher | Что проверяет | Пример |
|---------|--------------|--------|
| `like(value)` | Тип данных | `like('Alice')` → string |
| `string(value)` | String | `string('id_001')` |
| `uuid(value)` | Формат UUID | `uuid('abc-def')` |
| `email(value)` | Формат email | `email('a@b.com')` |
| `integer(value)` | Целое число | `integer(42)` |
| `decimal(value)` | Число с плавающей точкой | `decimal(3.14)` |
| `boolean(value)` | Boolean | `boolean(true)` |
| `eachLike(value)` | Массив с элементом-шаблоном | `eachLike({ id: string() })` |
| `term({generate, matcher})` | Регулярное выражение | `term({generate: '2024-01-01', matcher: '\\d{4}-\\d{2}-\\d{2}'})` |
| `atLeastLike(value, min)` | Массив >= N элементов | `atLeastLike({ id: string() }, 2)` |

### Почему matchers, а не точные значения

```typescript
// ❌ Плохо: запишет точный ID в контракт
body: { id: 'usr_abc123' }

// ✅ Хорошо: запишет только то, что это UUID
body: { id: uuid('usr_abc123') }
```

Если consumer записывает точный ID, провайдер обязан вернуть `'usr_abc123'` — даже если у него другая схема генерации. Matcher `uuid()` говорит: «должен быть UUID, точное значение не важно».

---

## Pact Broker

Pact Broker — центральный сервер для публикации и распространения контрактов.

```bash
# Docker Compose
docker-compose -f docker-compose.pact-broker.yml up

# postgres + pact broker
```

```yaml
# docker-compose.pact-broker.yml
version: '3'
services:
  postgres:
    image: postgres:16
    environment:
      POSTGRES_USER: pact
      POSTGRES_PASSWORD: pact
      POSTGRES_DB: pact
    ports:
      - "5432:5432"

  pact-broker:
    image: pactfoundation/pact-broker:latest
    ports:
      - "9292:9292"
    environment:
      PACT_BROKER_DATABASE_URL: postgres://pact:pact@postgres/pact
      PACT_BROKER_BASIC_AUTH_USERNAME: pact
      PACT_BROKER_BASIC_AUTH_PASSWORD: pact
    depends_on: [postgres]
```

### Публикация pact-файла

```typescript
import { Publisher } from '@pact-foundation/pact';

const publisher = new Publisher({
  pactBrokerUrl: 'http://localhost:9292',
  pactBrokerUsername: 'pact',
  pactBrokerPassword: 'pact',
  consumerVersion: '1.0.0',       // версия consumer
  pactFilesOrDirs: ['./pacts'],   // путь к pact-файлам
});

await publisher.publish();
```

### Matrix проверка в CI

```
Consumer: frontend-app v1.0.0
  └── Contract: user-api (must pass)
        └── Provider: user-api v2.1.0

Can frontend-app v1.0.0 deploy with user-api v2.1.0?
  → Проверка: pact matrix
  → Результат: ✅ (contract verified at user-api v1.5.0+)
```

---

## Интеграция с Playwright

Contract testing и Playwright не заменяют друг друга — они дополняют:

```typescript
// e2e/contract.spec.ts — contract test внутри Playwright
import { test, expect } from '@playwright/test';
import { PactV3, like, string, uuid } from '@pact-foundation/pact';

test.describe('User API contract', () => {
  test('GET user returns expected structure', async () => {
    const provider = new PactV3({
      consumer: 'playwright-e2e',
      provider: 'user-api',
      dir: './pacts',
    });

    provider
      .given('standard user exists')
      .uponReceiving('GET /users/standard_001')
      .withRequest({ method: 'GET', path: '/users/standard_001' })
      .willRespondWith({
        status: 200,
        body: {
          id: string('standard_001'),
          name: like('Charlie'),
          email: string('charlie@example.com'),
          role: string('user'),
        },
      });

    await provider.executeTest(async (mockServer) => {
      const res = await fetch(`${mockServer.url}/users/standard_001`);
      const body = await res.json();

      expect(res.status).toBe(200);
      expect(body.role).toBe('user');
    });
  });
});
```

---

## CI/CD Pipeline

```yaml
# .github/workflows/contract-tests.yml
name: Contract Tests
on: [push]

jobs:
  consumer:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: npm ci
      - run: npx jest tests/contract/user-service.pact.spec.ts
      - run: npx ts-node scripts/publish-pacts.ts
        env:
          PACT_BROKER_URL: ${{ vars.PACT_BROKER_URL }}
          PACT_BROKER_TOKEN: ${{ secrets.PACT_BROKER_TOKEN }}

  provider:
    needs: consumer
    runs-on: ubuntu-latest
    services:
      postgres:
        image: postgres:16
        env:
          POSTGRES_DB: test
          POSTGRES_PASSWORD: test
    steps:
      - uses: actions/checkout@v4
      - run: npm ci
      - run: npx jest tests/contract/user-api.verify.spec.ts
        env:
          PACT_BROKER_URL: ${{ vars.PACT_BROKER_URL }}
          PACT_BROKER_TOKEN: ${{ secrets.PACT_BROKER_TOKEN }}

  can-i-deploy:
    needs: [consumer, provider]
    runs-on: ubuntu-latest
    steps:
      - run: npx pact-broker can-i-deploy --pacticipant frontend-app --version 1.0.0 --to-environment production
        env:
          PACT_BROKER_BASE_URL: ${{ vars.PACT_BROKER_URL }}
```

---

## Анти-паттерны

| Анти-паттерн | Проблема | Решение |
|-------------|----------|---------|
| **Точные значения в body** | Контракт привязан к конкретным данным | Использовать matchers (`like`, `string`, `uuid`) |
| **Один тест на всё** | Падает весь suite, сложно понять, что сломалось | Один interaction = один `it()` |
| **Тест без `given`** | Нет предусловия, тест нестабилен | Всегда указывать состояние провайдера |
| **Provider states без handler** | Provider verification падает | Каждый `given` требует state handler |
| **Тестировать через pact E2E-флоу** | Pact не для full-stack | Pact = один API-запрос. E2E — отдельно |
| **Не публиковать pact в Broker** | Никто не видит контракты | Публиковать в CI. Pact Broker = source of truth |

---

## Когда Pact НЕ нужен

- **Монолит** — нет границ consumer/provider
- **2 разработчика в одной команде** — дешевле поговорить
- **API меняется раз в месяц** — E2E достаточно
- **Нет автоматизации** — pact не для ручного тестирования

---

## Связанные темы

- [[post-about-contract-testing-guide]] — Consumer-driven vs bi-directional
- [[testing-stability]] — Pact + flaky prevention
- [[go-testing-for-qa-2026]] — pact-go в Avito
- [[avito-baas-platform-qa-2026]] — Contract testing в Avito (уровень 2)
- [[improvements-from-bugs]] — Contract test fixes в CI
- [[iso-9001-qa-testing-2026]] — п.8.4 Control of externally provided services

## Tags

#pact #contract-testing #cdct #microservices #api-testing

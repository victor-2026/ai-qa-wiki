# Advanced Mutation Testing with Playwright

## Обзор

Расширенные техники мутационного тестирования для black-box систем, основанные на исследовании Chalmers/University of Gothenburg (Zenseact) и алгоритмических подходах Wrocław University of Technology.

Цель: выйти за рамки базовых First Order Mutants (FOM) и измерять качество тестов профессионально.

---

## 1. Operator Selection Strategy

Не все мутации одинаково полезны. В браузерной автоматизации фокус на операторах, ломающих **детерминированную синхронизацию UI**:

| Оператор | Пример | Эффект |
|----------|--------|--------|
| **Логические** | `&&` → `\|\|` | Меняет условие рендеринга |
| **Сравнения** | `>` → `>=` | Off-by-one в отображении |
| **Удаление полей** | `items[]` → `undefined` | UI падает или показывает пустоту |
| **Типы** | `number` → `string` / `null` | Ломает рендеринг чисел |
| **Статус-коды** | `200` → `500` | Проверка error handling |
| **Задержки** | 0ms → 5000ms | Проверка timeout/loading |

### Anti-pattern: Неэффективные операторы
- Изменение diagnostic tracking IDs (equivalent mutant — поведение не меняется)
- Переименование полей, не влияющих на UI (developer-only data)
- Изменение строк редиректа на синонимы

---

## 2. The Flakiness Matrix

Проблема: в облачных средах (Render, Fly.io, Railway) невозможно отличить **убитого мутанта** от **timeout'а из-за cold start**.

| | Мутант убит | Мутант выжил |
|--|------------|--------------|
| **Сервер ответил быстро** | ✅ Надёжный fail | ❌ Слепая зона |
| **Cold start (5-10s)** | ⚠️ False positive | ❌ Слепая зона |
| **Network flake** | ⚠️ False positive | ❌ Слепая зона |

### Решение: Deterministic Virtualization
Использовать `page.route()` для мока бэкенда — полностью отвязать мутации от облачной инфраструктуры:

```typescript
// Вместо реального бэкенда — локальный mock через Playwright
await page.route('**/api/posts/feed', async route => {
  const response = await route.fetch();
  const json = await response.json();
  json.items = [];  // мутация
  await route.fulfill({ json });
});
```

---

## 3. The High Mutation Score Fallacy

**Проблема:** Тесты с `toBeVisible()` «убивают» мутантов без проверки логики.

```typescript
// Ложное убийство — тест проходит даже с мутантом
test('user can see posts', async ({ page }) => {
  await page.goto('/feed');
  const post = page.locator('[data-testid^="post-card-"]').first();
  await expect(post).toBeVisible(); // Убьёт мутанта, но не проверит данные
});
```

**Решение:** Использовать точные ассерты:

```typescript
// Настоящее убийство
test('user can see posts', async ({ page }) => {
  await page.goto('/feed');
  const postTitle = page.locator('[data-testid="post-title"]').first();
  await expect(postTitle).toHaveText(/[A-Za-z]/); // Проверяет контент, не просто наличие
  const likeBtn = page.locator('[data-testid="post-like-btn"]').first();
  await expect(likeBtn).toBeEnabled(); // Проверяет состояние, не просто visibility
});
```

### Таблица: Assertion Quality

| Ассерт | Убивает мутанта | Проверяет данные | Рекомендация |
|--------|:---------------:|:----------------:|:------------:|
| `toBeVisible()` | ✅ иногда | ❌ | Только для error states |
| `toHaveText('value')` | ✅ | ✅ | Для текстовых полей |
| `toHaveURL('**/path')` | ✅ | ✅ | Для редиректов |
| `toBeEnabled()` / `toBeDisabled()` | ✅ | ✅ | Для кнопок/форм |
| `toHaveCount(n)` | ✅ | ✅ | Для списков |
| `toContainText(/pattern/)` | ✅ | ✅ | Для частичного текста |
| `toBeChecked()` | ✅ | ✅ | Для чекбоксов |

---

## 4. Higher Order Mutations (HOM)

Комбинация 2+ мутаций одновременно. Subsuming HOM могут выжить там, где каждая FOM по отдельности умирает.

### Пример: Subsuming HOM

```
FOM #1: likes_count → 0          (умирает — тест проверяет счётчик)
FOM #2: author.username → null   (умирает — тест проверяет автора)
HOM: likes_count → 0 + author.username → null (может выжить — тест падает на первом и не доходит до второго)
```

### Паттерн для Playwright:

```typescript
test('HOM-001: likes_count=0 + author=null', async ({ page }) => {
  await page.route('**/api/posts*', async route => {
    const response = await route.fetch();
    const json = await response.json();
    if (json.items) json.items.forEach((p: any) => {
      p.likes_count = 0;
      if (p.author) p.author.username = null;
    });
    await route.fulfill({ json });
  });

  await login(page);

  // Первая мутация — likes
  const likes = page.locator('[data-testid^="post-likes-count-"]').first();
  await expect(likes).toHaveText('0');

  // Вторая мутация — автор
  const author = page.locator('[data-testid^="post-author-"]').first();
  await expect(author).not.toBeVisible();
});
```

### Виды HOM:

| Тип | Описание | Сложность |
|-----|----------|-----------|
| **Subsuming** | HOM, который заменяет несколько FOM | Высокая |
| **Hard to Kill** | Комбинация мутаций, сложно убиваемая | Средняя |
| **Equivalent** | HOM, не меняющий поведение программы | Бесполезный |
| **Timeout** | HOM, вызывающий зависание UI | Специфичный |

---

## 5. Test Suite Segmentation

Не гонять полный mutation suite в каждом PR. Стратегия:

```yaml
# .github/workflows/mutation-nightly.yml
name: Mutation Nightly
on:
  schedule:
    - cron: '0 2 * * *'  # 02:00 UTC daily

jobs:
  mutation:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: |
          CHANGED_FILES=$(git diff --name-only HEAD~1)
          # Запускать мутации только для изменённых модулей
          if echo "$CHANGED_FILES" | grep -q "e2e/api/auth"; then
            npx playwright test e2e/mutation/api-mutation.spec.ts --grep "MUT-003|MUT-007"
          fi
```

### Правила сегментации:

| Частота | Тип мутаций | Охват |
|---------|-------------|-------|
| **Каждый PR** | Smoke mutation (3-5 быстрых) | Ключевые эндпоинты |
| **Nightly** | Полный mutation suite | Все 58+ тестов |
| **Weekly** | HOM + Chaos | Глубокий анализ |
| **Manual** | DB mutation + Fuzzing | При изменении схемы БД |

---

## 6. Deterministic UI Virtualization

Принцип: мокать бэкенд через `page.route()` для устранения внешней flakiness.

### Схема:
```
Playwright → page.route() → Mock API Response → UI rendering → Assertions
                                     ↑
                            Мутация в mock-данных
```

### Преимущества:
- **Скорость:** нет network latency (2-5s → 200ms)
- **Стабильность:** нет Render cold starts
- **Контроль:** 100% воспроизводимость мутации
- **Стоимость:** 0 API calls к бэкенду

### Ограничения:
- Не тестирует бэкенд (только фронтенд)
- Если API изменился — mock устаревает
- Не ловит ошибки бэкенд-логики

---

## 7. Mutation Score для Black-Box

Формула для проектов без доступа к коду:

```
Mutation Score = Killed Mutants / (Total Mutants - Equivalent Mutants) * 100%
```

### Интерпретация:

| Score | Значение |
|-------|----------|
| < 40% | Тесты не ловят базовые мутации |
| 40-60% | Средний уровень |
| 60-80% | Хороший уровень |
| 80-90% | Отличный (соизмеримо с входными данными) |
| > 90% | Подозрительно — возможна High Score Fallacy |

### Как избежать Fallacy:
1. Каждый тест убивает хотя бы одну мутацию
2. Каждая мутация убивается хотя бы одним тестом
3. Минимум `toBeVisible()` — максимум `toHaveText()`, `toHaveURL()`, `toHaveCount()`
4. Регулярный аудит: удалять equivalent mutants и weak assertions

---

## 8. Edge Boundary Exposure

Из исследования Zenseact: граничные мутации (`>=` вместо `>`) часто выживают.

### Пример для Buzzhive:
```typescript
// Оригинал: кнопка лайка активна если likes_count >= 0
// Мутация: likes_count < 0 (отрицательные лайки)
test('MUT-edge: negative likes_count handled', async ({ page }) => {
  await page.route('**/api/posts*', async route => {
    const response = await route.fetch();
    const json = await response.json();
    if (json.items) json.items.forEach((p: any) => { p.likes_count = -1; });
    await route.fulfill({ json });
  });

  await login(page);
  const likes = page.locator('[data-testid^="post-likes-count-"]').first();
  const text = await likes.textContent();
  expect(text?.trim()).toMatch(/^\d+$/);       // Должно быть числом
  expect(Number(text)).toBeGreaterThanOrEqual(0); // >= 0
});
```

---

## 9. Buzzhive Assertion Examples

### What kills mutants in Buzzhive:

```typescript
// ✅ STRONG: kills MUT-001 (likes_count → 0)
const likes = page.locator('[data-testid^="post-likes-count-"]').first();
await expect(likes).toHaveText('0');

// ✅ STRONG: kills MUT-002 (author.username → null)
const author = page.locator('[data-testid^="post-author-"]').first();
await expect(author).not.toBeVisible();

// ✅ STRONG: kills MUT-004 (items → [])
const posts = page.locator('[data-testid^="post-card-"]');
await expect(posts).toHaveCount(0);

// ✅ STRONG: kills MUT-007 (/auth/me → 401)
await page.waitForURL('**/login');
expect(page.url()).toContain('/login');
```

### What doesn't kill mutants (weak assertions):

```typescript
// ❌ WEAK: doesn't verify data, just existence
const post = page.locator('[data-testid^="post-card-"]').first();
await expect(post).toBeVisible(); // mutant can survive

// ❌ WEAK: doesn't verify content
const emptyState = page.locator('[data-testid="empty-feed"]');
await expect(emptyState).toBeVisible(); // doesn't check text
```

### Recommendation table for Buzzhive:

| Assertion | Before | After | Impact |
|-----------|--------|-------|--------|
| `toBeVisible()` | 13 (65%) | 5 (25%) | Replaced with stronger assertions |
| `toHaveText()` | 3 (15%) | 6 (30%) | Increased for text verification |
| `toHaveCount()` | 0 (0%) | 4 (20%) | Added for list mutations |
| `toHaveURL()` | 1 (5%) | 2 (10%) | Added for redirect verification |
| `toBeTruthy()` | 3 (15%) | 3 (15%) | Kept for existence checks |

**Result:** Mutation score 25/34 → 34/34 (100%)

---

## 10. Common Pitfalls & Solutions

### Pitfall 1: `text=` selector with pipes

Playwright `text=a|b|c` treats `|` as literal character, not regex OR:

```typescript
// ❌ WRONG: looks for literal "not found|404|does not exist"
const el = page.locator('text=not found|404|does not exist');

// ✅ CORRECT: use regex pattern
const el = page.locator('text=/not found|404|does not exist/i');
```

### Pitfall 2: Route interception after page load

Frontend caches API responses. Route must be set before navigation:

```typescript
// ❌ WRONG: route set after feed loaded
await login(page);
await page.waitForLoadState('networkidle');
await page.route('**/api/posts/feed', ...); // too late!

// ✅ CORRECT: route set before navigation
await page.route('**/api/posts/feed', async route => {
  await route.fulfill({ json: { items: [], total: 0 } });
});
await login(page);
```

### Pitfall 3: Overly specific route patterns

Frontend may use different API endpoints than expected:

```typescript
// ❌ WRONG: misses /api/posts/feed, /api/posts/search, etc.
await page.route('**/api/posts/*', ...);

// ✅ CORRECT: broad pattern catches all post-related endpoints
await page.route('**/api/posts**', ...);
```

### Pitfall 4: Comments loaded with feed

Frontend doesn't make separate API call for comments — they're part of feed response:

```typescript
// ❌ WRONG: intercepting separate comments endpoint (never called)
await page.route('**/api/posts/*/comments', ...);

// ✅ CORRECT: modify feed response to set comments_count = 0
await page.route('**/api/posts**', async route => {
  const response = await route.fetch();
  const json = await response.json();
  if (json.items) {
    json.items.forEach((p: any) => { p.comments_count = 0; });
  }
  await route.fulfill({ json });
});
```

---

## Источники
- Chalmers University of Technology / University of Gothenburg — Industrial Case Study на Zenseact
- Wrocław University of Technology — Higher Order Mutations алгоритмы
- `/raw/Mutation Testing Playwright Front-End.md` — основной источник техник
- `/raw/Mutation-testing-without-code.md` — альтернативы для black-box
- Buzzhive实践 (2026-06-03) — 34/34 mutation tests pass, route interception patterns, Playwright selector pitfalls

## Связанные темы
- [[Mutation-testing-without-code]]
- [[Chaos-Engineering]]
- [[API-Testing]]
- [[Test-Reliability]]
- [[Self-healing-tests]]

---
*Теги: #Mutation-Testing #HOM #Playwright #Test-Quality #Black-Box-Testing #Flakiness #Route-Interception #Selector-Pitfalls*

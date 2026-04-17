# Full-stack Verification: Playwright Agent + Database

**Source:** [Habr - FaryaRos](https://habr.com/ru/articles/1022962/)
**Date:** 2025-04-17
**Author:** Перевод статьи Gurudatt S A
**Views:** 6.1K

## Суть

AI-агент с двумя MCP-серверами проверяет UI и базу данных одним промптом.

```
┌─────────────────────────────────────────┐
│          AI Agent (один промпт)          │
├─────────────────────────────────────────┤
│  1. Playwright MCP → UI actions         │
│     (click, fill, navigate)              │
│                                         │
│  2. Extract ID from page               │
│     (order #10472)                     │
│                                         │
│  3. Postgres MCP → DB verification      │
│     (read_query, describe_table)         │
│     НОЛЬ SQL от человека!               │
└─────────────────────────────────────────┘
```

## Настройка

### MCP Servers (claude_desktop_config.json)

```json
{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": ["@anthropic/mcp-playwright"]
    },
    "postgres": {
      "command": "npx",
      "args": ["@anthropic/mcp-postgres", "postgresql://readonly:****@localhost:5432/shop"]
    }
  }
}
```

**Важно:** Read-only пользователь для базы!

## Промпт

```
## Full-Stack Checkout Verification

Используй Playwright MCP-сервер:
1. Перейди на localhost:3000/products
2. Добавь «Wireless Charger» в корзину
3. Оформи заказ как «Ada Lovelace» (ada@test.dev),
   оплата — Credit Card
4. Захвати order ID со страницы подтверждения

Затем переключись на Postgres MCP-сервер и проверь:
- Строка заказа существует с правильным email
- Запись line_item для «Wireless Charger» (qty 1) присутствует
- Инвентарный остаток товара уменьшен на 1

Выведи результат pass/fail для каждого ассерта.
```

## Как работает

1. Агент выполняет UI действия через Playwright
2. Извлекает Order ID со страницы
3. Изучает схему БД (`list_tables`, `describe_table`)
4. Строит и выполняет SQL запросы
5. Возвращает результат

## Production паттерны

| Паттерн | Описание |
|---------|----------|
| **Read-only DB** | Только `read_query`, никакой записи |
| **Тайминг-гарды** | Ожидание async операций (5 сек, polling 500ms) |
| **Snapshot до/после** | Сравнение состояния БД до и после UI действия |
| **Расширение** | Redis, Elasticsearch, S3 через другие MCP |

## Результат

```
Full-Stack Verification — Order #10472
───────────────────────────────────────
✓ строка orders существует
    customer_email: ada@test.dev
    status: confirmed
    total: $34.99
✓ строка line_items найдена
    product_name: Wireless Charger
    quantity: 1
✓ products.stock уменьшен
    было: 48 → стало: 47
3/3 ассертов прошли
```

## Связь с Buzzhive

В Buzzhive уже есть DB тесты (jest + pg). Альтернатива — MCP подход:

| Подход | Плюсы | Минусы |
|--------|-------|--------|
| **Текущий (pg)** | Прямой SQL | Нужен SQL |
| **MCP** | Ноль SQL | Настройка MCP |

## See Also

- [[raw/ai-qa-exoskeleton-habr]] — AI-экзоскелет для QA

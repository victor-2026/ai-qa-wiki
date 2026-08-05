# HTTP QUERY Method (RFC 10008, June 2026)

Новый HTTP-метод `QUERY`, стандартизированный в RFC 10008. Первый новый метод после PATCH (2010).

## Суть

`QUERY` — безопасный (safe) и идемпотентный HTTP-метод с телом запроса. Заполняет gap между `GET` (нет тела) и `POST` (не safe/идемпотентен).

```
QUERY /orders HTTP/1.1
Host: api.example.com
Content-Type: application/json
Accept: application/json

{ "status": "paid", "created_after": "2026-01-01", "sort": ["-created_at"], "limit": 100 }
```

## Свойства

| Свойство | GET | QUERY | POST |
|----------|-----|-------|------|
| Safe | ✅ | ✅ | ❌ |
| Idempotent | ✅ | ✅ | ❌ |
| Тело запроса | ❌ | ✅ | ✅ |
| Кэшируется | ✅ | ✅ | ❌ |
| Свой URI | ✅ | ⬜ | ❌ |

## Ключевые сценарии для тестировщиков

### 1. Проверка поддержки метода
- Сервер отвечает `405 Method Not Allowed` если не поддерживает QUERY
- `Accept-Query` в ответе — сервер заявляет о поддержке
- Прокси/CDN могут не знать о новом методе → передавать как есть или отклонять

### 2. Кэширование
- QUERY-ответы кэшируются, ключ = URI + Content-Type + тело
- Кэш может нормализовать тело (сортировка JSON-ключей, обрезка whitespace)
- Тест: два идентичных QUERY с разным порядком полей в JSON → должны попадать в кэш

### 3. CORS
- Preflight-запрос (OPTIONS) с `Access-Control-Request-Method: QUERY`
- Сервер не знает QUERY → может отклонить preflight
- Тест: CORS-заголовки для QUERY отдельно

### 4. Прокси и WAF
- Прокси может не знать QUERY → передавать как Unknown Method
- WAF может блокировать QUERY как неизвестный метод (false positive)
- Тест: прохождение через reverse proxy (nginx, envoy, haproxy)

### 5. Conditional Requests
- If-Match / If-None-Match / If-Modified-Since работают с QUERY
- ETag учитывает тело запроса

### 6. Безопасность
- QUERY safe и idempotent → не меняет состояние сервера
- Тело может содержать SQL/LDAP/XPath инъекции (как и в POST)
- Логирование: тело QUERY может попасть в лог (в отличие от GET, где логируется URI)
- Чувствительные данные в теле QUERY должны маскироваться

### 7. Rate limiting
- QUERY не должен триггерить rate-limit для state-changing методов
- Но может забивать базу сложными запросами → отдельный rate-limit для QUERY

## Реализации

- HTTP-метод = строка — работает в любом HTTP-клиенте
- **Go:** `http.NewRequestWithContext(ctx, "QUERY", url, body)`
- **Rust/reqwest:** `Method::from_bytes(b"QUERY")`
- **Playwright API:** `page.request.fetch(url, { method: 'QUERY', data: queryBody })`

## Источники

- RFC 10008: https://www.rfc-editor.org/rfc/rfc10008.html
- Хабр: https://habr.com/ru/articles/1055310/
- Blain Smith: https://blainsmith.com/articles/rfc-10008-http-query-method/

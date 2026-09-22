---
title: "FastAPI Backend for Beginners"
type: skill
updated: "2026-09-22"
tags: [fastapi, api, python, backend, skill]
---

# FastAPI Backend for Beginners

## What It Is
FastAPI — современный Python-фреймворк для создания REST API. Базируется на двух библиотеках: **Starlette** (веб-часть) и **Pydantic** (валидация данных). Ключевые фишки — декларативные модели, автоматическая документация (Swagger/OpenAPI), асинхронность.

Для QA это важный навык: (1) быстрые mock/fake-серверы для тестов (мы сами уже писали `fake_stream_server.py` на FastAPI на Автономе), (2) понимание, как устроен тестируемый backend, (3) быстрые тест-услышители на Python.

## Самое главное (пример из жизни)

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    in_stock: bool = True

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/items")
def create_item(item: Item):
    return {"id": 1, **item.model_dump()}
```

Вот и готовый API: `GET /health`, `POST /items` с валидацией полей через Pydantic. Запуск: `uvicorn main:app --reload`. Документация автоматически появится на `/docs` (Swagger UI).

## Почему полезно для QA
- **Мгновенная документация:** `/docs` — Swagger, `/openapi.json` — спецификация. Спецификация = контракт для тестов. Сравнивать с фактическим поведением — наш подход (запрос vs реальность).
- **Pydantic-валидация = отличный тест-объект:** `price: "abc"` → 422, автоматическая проверка типов.
- **Лёгкие mock-серверы:** поднять фейковый API для E2E тестов — минуты работы:
  ```python
  # fake_server.py — часный пример для тестов
  from fastapi import FastAPI
  app = FastAPI()

  @app.get("/api/users/{uid}")
  def user(uid: int):
      if uid < 0:
          return {"error": "invalid id"}
      return {"id": uid, "name": "test-user"}
  ```
- **Асинхронность:** `async def` + `await` для быстрых I/O. Тест, подразумевающий последовательность — может ловить гонки.

## Как тестировать FastAPI-приложение
Стандарт — pytest + testclient (fastapi.testclient, "мешочек" testclient под капотом:
```python
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_health():
    r = client.get("/health")
    assert r.status_code == 200

def test_create_item():
    r = client.post("/items", json={"name": "стол", "price": 10.5})
    assert r.status_code == 200
    assert r.json()["name"] == "стол"
```

## TL;DR Для резюме
- FastAPI (Python) + Pydantic (модели/валидация) + Starlette.
- Автодокументация OpenAPI/Swagger (`/docs`, `/openapi.json`).
- Асинхронная обработка (`async def`), TestClient + pytest для тестов.
- Опыт: mock/fake-серверы для тестов, тестирование эндпоинтов, контракт из openapi.

## Связанные страницы
- [[wiki/opencode-openrouter-qa-2026|OpenCode/OpenRouter QA (FastAPI backend context)]]
- [[wiki/autonoma-streaming-responses-2026|Autonoma Streaming (FastAPI fake-server example)]]
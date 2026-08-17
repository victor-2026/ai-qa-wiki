---
title: "C4 Model — Visualising Software Architecture"
type: article
updated: "2026-08-17"
tags: [qa]
---

# C4 Model — Visualising Software Architecture

**Автор:** Simon Brown
**Сайт:** https://c4model.com
**Книга:** The C4 Model (O'Reilly, 2025)

---

## Что такое C4 Model

C4 — иерархический подход к диаграммированию архитектуры ПО. 4 уровня абстракции, каждый для своей аудитории:

| Уровень | Что показывает | Аудитория |
|---------|---------------|-----------|
| **C1 — System Context** | Система, пользователи, внешние зависимости | Все стейкхолдеры |
| **C2 — Container** | Приложения (web, mobile, API, DB) внутри системы | Dev + Ops |
| **C3 — Component** | Компоненты внутри одного контейнера | Разработчики |
| **C4 — Code** | Код (классы, файлы, interfaces) | Разработчики (rarely used) |

---

## 4 уровня

### C1: System Context Diagram
- Одна система = один бокс
- Пользователи (actors) + внешние системы
- **Вопрос:** куда наша система вписывается в мир?

```
[User] ──HTTP──► [Our System] ──► [External API]
```

### C2: Container Diagram
- Container ≠ Docker. Container = приложение/сервис/БД
- Web app, Mobile app, API, Database, Message queue
- **Вопрос:** из каких приложений состоит система?

```
[SPA (React)] ──JSON/HTTPS──► [API (Node)] ──SQL──► [(PostgreSQL)]
                                                                   │
[User] ──HTTPS──► [SPA (React)]           [API (Node)] ──AMQP──► [(RabbitMQ)]
```

### C3: Component Diagram
- Компоненты внутри одного контейнера
- Контроллеры, сервисы, репозитории
- **Вопрос:** как устроен backend?

```
┌─────────────────────────────────┐
│         API (Node)              │
│  ┌─────────┐  ┌──────────┐     │
│  │ Auth    │  │ User     │     │
│  │ Controller│  │ Controller│     │
│  └────┬────┘  └────┬─────┘     │
│       │            │           │
│  ┌────▼────────────▼─────┐     │
│  │    UserService        │     │
│  └────┬──────────────────┘     │
│       │                       │
│  ┌────▼─────┐                 │
│  │ UserRepo │                 │
│  └────┬─────┘                 │
└───────┼───────────────────────┘
        │ SQL
   ┌────▼──────┐
   │ PostgreSQL │
   └───────────┘
```

### C4: Code Diagram
- Классы, interfaces, отношения
- **Вопрос:** как реализован конкретный компонент?
- На практике редко используется (IDE сам рисует)

---

## Дополнительные диаграммы

| Диаграмма | Что показывает |
|-----------|---------------|
| **System Landscape** | Все свои и соседские системы (а не одну) |
| **Dynamic** | Последовательность вызовов между компонентами во времени |
| **Deployment** | Как код развёрнут: сервера, контейнеры, инфраструктура |

---

## Нотация

C4 **не привязан к конкретной нотации**:

- **Boxes + lines** — basic
- **C4-PlantUML** — PlantUML
- **Structurizr DSL** — текстовый DSL (рекомендованный)
- **Draw.io / Excalidraw** — ручное рисование
- **Mermaid** — текстовый

```c4
// Structurizr DSL
workspace "My System" {
    model {
        user = person "User"
        system = softwareSystem "My System"
        user -> system "Uses"
    }
    views {
        systemContext system {
            include *
            autoLayout
        }
    }
}
```

---

## Как C4 связан с QA

| QA-активность | C4-уровень | Применение |
|--------------|------------|------------|
| **Contract testing** | C2 — Container | API-границы между контейнерами = где ставить Pact |
| **Integration testing** | C2 → C3 | Какие интеграции тестировать |
| **Risk analysis** | C1 — Context | Кто зависит от системы, какие внешние риски |
| **Test strategy** | Все 4 уровня | Что покрываем тестами на каждом уровне |
| **Chaos engineering** | C2 + Deployment | Где вносить сбои |
| **E2E vs API vs unit** | C2 → C3 → C4 | Пирамида тестирования = иерархия C4 |

---

## Related

- [[structurizr-dsl-guide]] — Structurizr DSL for C4
- [[c4-plantuml-examples-2026]] — PlantUML examples for C4
- [[iso-9001-qa-testing-2026]] — Process approach (п.4.4)
- [[pact-contract-testing-guide-2026]] — Contract testing on C2 boundaries

# Weekly Time Planner — PRD Example

## Описание
Pet-проект: weekly planner для учёта времени с авторизацией через Google. Google Calendar читает events, custom категории в Firestore, подсчёт времени по категориям.

## Почему не Google Calendar
Google Calendar показывает events, но подсчёт времени по категориям — только в Business версии. Free tier не умеет.

## Архитектура

```
Next.js (Vercel)
  ├── Firebase Auth — Google sign-in
  ├── Google Calendar API — read events
  └── Firestore — хранит { eventId, category, userId }
```

## Поток

1. User → Sign in with Google (Firebase Auth)
2. App → GET /calendar/events (Google Calendar API, read-only)
3. User → проставляет категории каждому event
4. Firestore → сохраняет { eventId, category, userId }
5. App → группирует events по category → сумма duration

## Стек и почему

| Компонент | Выбор | Почему |
|-----------|-------|--------|
| Framework | Next.js (Vercel) | Дешево, serverless, готовые API routes |
| Auth | Firebase Auth | onAuthStateChanged, Google OAuth из коробки |
| DB | Firestore | Тот же Firebase, не плодить провайдеров |
| Calendar | Google Calendar API | Read-only, free quota (10k req/day) |

## Оценка

| Задача | Время |
|--------|-------|
| Auth + Calendar read (Firebase SDK) | 2-3ч |
| Категории UI + Firestore CRUD | 1-2ч |
| Подсчёт + weekly view | 1-2ч |
| **Итого MVP** | **4-7ч** |
| С Claude/Codex | ~3-4ч |

## Слабое место
Google Calendar API quota — 10k req/day. Для личного use case не критично.

## Связанные темы
- [[wiki/firebase-auth-google-playwright-testing]] — тестирование Google OAuth
- [[wiki/pbt-invariants]] — PBT для подсчёта времени (сумма != 24h)

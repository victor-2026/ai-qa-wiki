---
title: "Сравнение: OpenCode vs Antigravity (Go migration)"
type: article
updated: "2026-08-17"
tags: [antigravity, opencode]
---

# Сравнение: OpenCode vs Antigravity (Go migration)

## Контекст

**Antigravity** (неизвестная модель, новый профиль macOS) — 24-25 мая 2026, 2 дня бесплатного доступа:
- Свежая установка, репо склонирован в `/Users/Shared/Projects/`
- Prompt (предп.): "напиши всевозможные тесты логина под админом"
- Создала `login_test.go` (188 строк, 5 тест-функций, 10 тестов с SQLi subtests)
- Нашла race-баг (другой, не refresh token)
- Пофиксила nginx.conf (duplicate location "/api" в Docker)
- Доступ потерян из-за VPN — модель и точный prompt не подтверждены

**OpenCode Go** (gpt-4o-mini, $10 flat) — 40+ сессий:
- Создала 33 Go теста в `/victor/go-backend/`
- `api/race_test.go` (2 race-теста: parallel login + follow/unfollow) — другой race-баг

## Найденные проблемы

### Баг в login_test.go: неправильный пароль "admni123"
В переданных Antigravity credentials был пароль `admni123` (опечатка пользователя: "ni" вместо "in"). Тест проходил, потому что:
1. Фронтенд проксировал API на Render (`buzzhive-test.onrender.com`)
2. Render редиректил http→https с кодом **307**
3. `ExpectResponse` перехватывал 307 **до** проверки credentials
4. Тест проверял только `status in [200, 307]` и пропускал настоящий 401

**Урок:** Даже при корректно написанных тестах, если входные данные неверны, а инфраструктура (307 redirect) маскирует ошибку — тест может ложно проходить. Важно проверять не только HTTP-статус, но и URL, UI-элементы и localStorage.

### Race-баги
| Дата | Баг | Кем найден | Статус |
|------|-----|------------|--------|
| ~20 мая | Refresh token race (duplicate key) | OpenCode/docs | 🔴 открыт |
| 24-25 мая | Race-баг (другой, не refresh token) | Antigravity | ? |
| 26 мая | Refresh token race — root cause + fix (`jti: uuid.uuid4()`) | OpenCode Session 9 | 🟢 пофиксен |
| 29 мая | `race_test.go` (10 goroutines login + 5+5 follow/unfollow) | OpenCode | 🟢 заведён |

**Важно:** race-баги Antigravity и OpenCode — **разные**, найдены независимо.

## Сравнение тестов

| Тест | Antigravity | Описание |
|------|-------------|----------|
| `TestUserLoginFlow` | ✅ | Валидный логин + localStorage token |
| `TestUserLoginWrongPassword` | ✅ | Неверный пароль → 401 |
| `TestUserLoginInvalidEmail` | ✅ | Несуществующий email → 401 |
| `TestUserLoginHTML5EmailValidation` | ✅ | invalid-email → browser block |
| `TestUserLoginSQLInjection` | ✅ | 4 payloads table-driven |

### Качество кода Antigravity
- `runTestWithPage` helper — browser setup + navigation + teardown
- `response` event listener — логгирование HTTP (`🌐 RESPONSE LOG: 200 ...`)
- `WaitUntil: networkidle` — ожидание полной загрузки
- `assert` vs `require` — правильно разделены
- Nil check на response — защита от nil-паники

## Метрики

| Метрика | Antigravity | OpenCode Go |
|---------|-------------|-------------|
| Файлов | 1 (`login_test.go`) | 7 (`api/*_test.go` + `cmd/`) |
| Тест-функций | 5 | 33 |
| Go toolchain | testify (assert/require) | testify + helpers + warmup |
| Data-driven | SQLi table-driven (4 payloads) | Да (auth, posts, users) |
| Race тесты | 1 найден | 2 созданы |
| POM/helpers | `runTestWithPage` | `client.go`, `helpers.go` |
| Docker fix | nginx duplicate location | — |

## Контроль переменных

| Переменная | Antigravity | OpenCode Go |
|-----------|-------------|-------------|
| Модель | ? | gpt-4o-mini |
| Контекст | Чистый лист | 40+ сессий |
| Репозиторий | `/Shared/` (свежий clone) | `/victor/` (полная история) |
| AGENTS.md | Не читала | Читает (go-backend ❌) |
| Docker | Починила (nginx.conf) | Деплоил готовый |
| Go toolchain | Установила сама | Уже стоял |

## Ограничения эксперимента

1. Модель Antigravity неизвестна — не сравнить "модель vs модель"
2. Prompt не подтверждён
3. Асимметрия контекста: Antigravity с нуля, OpenCode с опытом 40+ сессий
4. Разное время: Antigravity 2 дня, OpenCode делала бы за 1 сессию
5. Shared go-backend потерян — VPN блокирует уточнение

## Выводы

- Antigravity (с нуля, 2 дня) = 5 тестов + race-баг + Docker fix. Сильный результат для чистого листа
- OpenCode (40+ сессий, 2.5 месяца) = 33 теста + 2 race-теста + полноценная структура
- Ключевой урок: проверять не только HTTP-статус, но и UI, localStorage, URL
- Race-баги найдены независимо разными инструментами — подтверждает ценность разнообразия подходов

## Что нужно для завершения

- [ ] Подтвердить модель Antigravity (когда появится VPN)
- [ ] Подтвердить точный prompt
- [ ] Запустить OpenCode на тот же prompt
- [ ] Сравнить head-to-head

**Updated:** 2026-07-02

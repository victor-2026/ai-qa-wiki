---
title: "QA Metrics Dashboard — Setup Notes"
type: article
updated: "2026-08-17"
tags: [qa]
---

# QA Metrics Dashboard — Setup Notes

**Location:** `qa-automation-sandbox/monitoring/`
**Open:** `dashboard.html` в любом браузере

## Что это

Самодостаточный HTML-дашборд на Chart.js. Данные встроены в HTML — не нужен ни сервер, ни Docker, ни плагины.

## Дашборды

| Вкладка | Источник данных | Что показывает |
|---------|----------------|---------------|
| OrangeHRM Coverage | `metrics/orangehrm-coverage.json` | 20%→65% coverage за 6 фаз, модули, POM, smoke |
| Buzzhive Test Health | `metrics/buzzhive-test-health.json` | Pass rate 78%→94%, API coverage, flaky→0, suite growth |
| Buzzhive Quality Gates | `metrics/buzzhive-quality-gates.json` | Mutation 28→34/34, contract schema/consumer/provider |

## Как обновлять

1. Добавить строку в `metrics/*.json`
2. Перегенерировать `dashboard.html` — см. скрипт в README

## Почему не Grafana

Попытки №1-3: Docker + Grafana + Infinity datasource. Проблемы:
1. Infinity datasource proxy не поддерживает внутренние Docker URL'ы (ошибка "no Host in request URL")
2. Direct access через CORS — работает, но JSON query format для Infinity v3.8.0 нестабилен
3. Python HTTPServer висел на бинде порта на macOS (известный баг Python 3.12 HTTP-сервера)

Решение: Chart.js + inline JSON. Никаких зависимостей кроме CDN скрипта. Работает везде.

## Скриншоты для LinkedIn

Открыть вкладку → F11 (full-screen) → скриншот. Тёмная тема совместима с LinkedIn.

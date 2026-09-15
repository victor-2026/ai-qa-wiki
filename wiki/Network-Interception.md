# Network Interception (Перехват сетевых запросов)

**Определение:** Перехват и модификация HTTP/HTTPS-запросов во время тестирования для имитации серверных ответов, ошибок, задержек и граничных случаев. В Playwright: `page.route()` для перехвата запросов на уровне браузера.

**Связь с мутациями:** Перехват — основной инструмент для мутаций без доступа к коду: подмена API-ответов (статус 500, пустой body, задержка 30s), изменение данных, эмуляция offline-режима.

**Инструменты:** Playwright `page.route()`, MSW (Mock Service Worker), mitmproxy, Charles Proxy, Toxiproxy.

**Связанные темы:**
- [[Mutation-testing-without-code]] — route interception как способ мутации
- [[Mutation-testing-advanced-playwright]] — Playwright route patterns
- [[API-Testing]] — mock API responses
- [[Chaos-Engineering]] — имитация сетевых сбоев

---

*Теги: #Network-Interception #Mocking #Playwright #Route #API*

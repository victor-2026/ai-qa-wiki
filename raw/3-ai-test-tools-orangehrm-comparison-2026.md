# 3 AI Test Tools on OrangeHRM: Playwright Agents vs KISS/Sorcar vs Autonoma

**Pulse Article:** https://www.linkedin.com/pulse/i-ran-3-ai-test-tools-same-orangehrm-app-heres-what-each-ematin-d9hpf/
**Feed Post:** https://www.linkedin.com/feed/update/urn:li:ugcPost:7479679946467176448/
**Published:** 2026-07-06 09:15
**Author:** Victor Ematin
**Series:** Article 12, AI-Agents series

## Summary

Сравнение трёх AI-инструментов генерации тестов на одной странице OrangeHRM 5.9 (Workspace Notification Configuration — 7 полей, Slack/Google Chat webhooks):

## Results

| Инструмент | Тестов | Время | Характеристика |
|-----------|--------|-------|----------------|
| Playwright Agents | 8 тестов | 10 мин | Pipeline, 2 автофикса (Vue race + duplicate API), 0 правок |
| KISS/Sorcar | 8 тестов + POM 187 строк | 2 промпта | Production-grade POM, 1 ручной фикс (HTTP 400) |
| Autonoma | 136 specs (14 модулей) | 3.5 часа | 40 .md файлов, NL specs, только 2 покрывают нужную страницу |

## Mutation Testing

6 fault-injections через page.route(): оба code-based набора поймали 6/6. Autonoma specs не участвуют — они intent, не код.

## Trade-offs

- Speed → Playwright Agents
- Maintainability → KISS
- Breadth → Autonoma

## Analytics (Single Post)

Файл: `SinglePostAnalytics_Victor Ematin_7479779995654144001.xlsx`
- Impressions: 274
- Members reached: 209
- Article views: 4
- Reactions: 1
- Comments/Reposts/Saves: 0
- Profile visitors from post: 0
- Followers gained: 0

## Key Insight

"These tools don't compete on the same axis. PW Agents and KISS generate test code that runs anywhere. Autonoma generates test intent that runs on its own platform."

## Sources

- Pulse Article (LinkedIn, Jul 6 2026)
- Feed Post (LinkedIn, Jul 6 2026)
- SinglePostAnalytics export

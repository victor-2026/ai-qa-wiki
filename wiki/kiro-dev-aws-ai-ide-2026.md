---
title: "Kiro.dev — AWS Agentic AI IDE (2026)"
type: article
updated: "2026-08-17"
tags: [kiro, agents, cursor]
---

# Kiro.dev — AWS Agentic AI IDE (2026)

Kiro — агентная AI IDE от AWS (запуск Jul 2025, AWS Summit NYC). Code OSS fork, доступен как IDE, CLI, Web и Mobile (iOS).

Ключевое отличие от Cursor/Copilot: **spec-driven development** — код пишется после формальных спецификаций, а не по одному промпту.

## Spec-Driven Development

1. Промпт → AI задаёт уточняющие вопросы
2. Генерация 3 spec-файлов: `requirements.md`, `design.md`, `tasks.md`
3. Specs проверяются на противоречия и пробелы (automated reasoning)
4. Параллельные агенты реализуют задачи по spec
5. Hooks синхронизируют spec и код при изменениях

## Quality Engineering Relevance

| Возможность | Отношение к тестированию |
|-------------|--------------------------|
| **PBT built-in** | Spec → property-based tests (fuzz-подобные) — ловят edge cases, которые юнит-тесты пропускают |
| **Specs включают тесты** | Каждая задача содержит unit, integration, loading states, mobile responsiveness |
| **Hooks** | Event-driven quality gates: тесты, линтер, security scan на каждый save/commit |
| **Steering** | `tech.md`, `structure.md`, `product.md` — кодификация стандартов качества кода |
| **Parallel agents** | Множественные агенты имплементируют по spec — нужна верификация, что не разъехались |
| **ACP** | Работает из JetBrains, Zed, Neovim — не привязывает к IDE |

## Ключевые фичи для QA

### 1. Property-Based Testing (PBT)
Главная «фишка» Kiro для QA. Вместо юнит-тестов агенты Kiro:
- Анализируют требования в формате EARS
- Извлекают логические свойства системы
- Генерируют тысячи случайных комбинаций входных данных для поиска edge cases

### 2. Coverage Gap Analysis
Kiro сканирует репозиторий и находит непокрытые методы/контроллеры.

**Практический результат (OrangeHRM + Buzzhive, Jul 2026):**

| Метрика | Значение |
|---------|----------|
| Coverage gaps найдено | 49 (14 OrangeHRM + 35 Buzzhive) |
| Тестов сгенерировано | 164 (42 + 122) |
| First-run pass | 144/164 (88%) |
| AI self-healed | 8 (OrangeHRM UI timing) |
| Реальных дыр | 6 (approveClaim, Search API 0%, admin ban non-existent endpoint) |
| Время анализа | 7 минут (vs 3-4 часа вручную) |

### 3. Security Code Audit
На Virto Commerce vc-platform за 2 минуты нашёл **36 untested security-critical файлов** в 7 категориях (authentication, OAuth/token, permissions, SSO, certificates, API key lifecycle, claims).

**Limitation:** статический анализ (dead code) слабее — CQRS command-слой `ICommandHandler` с 0 реализациями не был найден.

### 4. Cloud Automations
Через веб-интерфейс можно настроить регулярные агентные задачи:
- Ежеутренняя проверка коммитов на архитектурные тесты
- Автопокрытие тестами новых веток перед мержем

## Позиционирование в 2026

### vs Другие AI IDE

| vs | Kiro сильнее | Kiro слабее |
|----|-------------|-------------|
| Cursor | Spec lifecycle, hooks, enterprise governance | Cursor быстрее для prototyping |
| Copilot | Полноценная IDE, spec-first, infra-as-code | Copilot встроен в GitHub/VS Code |
| Cline/Claude Code/OpenCode | IDE (не только CLI), hooks, parallel agents | Легче, гибче, без vendor lock-in |
| Autonoma | Spec-driven dev workflow | Autonoma = test generation из codebase (другая задача) |

### vs Cognition AI (Devin + Windsurf)

**Важно:** Декабрь 2025 — Cognition (создатель Devin, $500/mo) приобрела Windsurf (IDE, $15/mo) за ~$250 млн. Теперь это одна компания, два продукта: Devin (автономный агент) и Windsurf (IDE с Cascade agent).

| vs | Kiro | Devin | Windsurf |
|----|------|-------|----------|
| Цена | Free beta (50 credits) | $500/mo | $15/mo |
| Доступ | IDE + CLI + Web | Cloud-only IDE | IDE (VS Code fork) |
| Spec-driven | ✅ Да (EARS specs) | ❌ Нет | ❌ Нет |
| PBT | ✅ Built-in | ❌ Нет | ❌ Нет |
| Coverage gap analysis | ✅ Практически проверено | ❌ Не тестировалось | Не тестировалось |
| Self-healing тестов | ✅ 8 из 164 | ❌ Нет цикла | Cascade agentic flow |
| Aider comparison | — | Devin шире (7 vs 1 тест), Aider глубже (POM 10 методов) + auto-fix | — |
| Практика QA | OrangeHRM + Buzzhive + Virto Commerce | Только OrangeHRM (Maintenance) | Не применялся для QA |

Windsurf **не применялся для тестирования или генерации тестов** ни в одном проекте. Упоминается только в общих обзорах AI-инструментов.

**Вывод:** Kiro и Cognition AI — разные ниши. Kiro = spec-first + PBT для инженерной корректности. Cognition (Devin+Windsurf) = автономный агент + speed-first IDE. Для QA Kiro даёт больше структуры, Devin/Windsurf — быстрее в генерации, но без гарантий корректности.

### Место в QA-иерархии

- **Для manual QA:** Mabl/Testsigma проще (record/playback, low-code)
- **Для SDET/automation:** Kiro мощнее — работает на уровне codebase, PBT, coverage gaps
- **Shift-Left:** позволяет тестировать логику на этапе проектирования, до UI

## QA Gaps

- **Нет test management** — Allure/TestOps, тест-планов, аналитики
- **PBT ≠ mutation testing** — не убивает мутантов, не меряет качество тестов
- **Нет QA-роли** — инструмент для разработчика, не для тестировщика
- **Vendor lock-in (soft)** — spec-формат Kiro, hooks API, steering files
- **Dead code analysis слабый** — не находит мёртвые интерфейсы без реализаций

## Ключевые фичи (общие)

- **Auto model**: выбирает модель по сложности задачи (Claude Opus/Sonnet/Haiku, DeepSeek, MiniMax)
- **Кредитная система**: предоплата, cap, без rate limits
- **Enterprise**: SSO/IAM, governance, IP indemnity, SOC 2 (через AWS)
- **Приватность**: код на локальной машине (IDE/CLI) или изолированные sandbox (Web)
- **Haim Michael**: CEO Zindell Technologies, использует Kiro с day 1

## Источники

- [kiro.dev](https://kiro.dev)
- [Kiro Docs — Correctness](https://kiro.dev/docs/specs/correctness/)
- [Kiro Web](https://kiro.dev/web/)
- [Kiro IDE](https://kiro.dev/ide/)
- [Kiro Automations](https://kiro.dev/blog/introducing-automations/)
- [ACP Adoption (Feb 2026)](https://kiro.dev/blog/kiro-adopts-acp)
- [LinkedIn Article 11 — Kiro Coverage Gap Analysis](https://www.linkedin.com/pulse/kiro-vs-traditional-code-coverage-7-minute-gap-analysis-victor-ematin-qcxaf)
- `raw/kiro-dev-aws-ai-ide-2026.md`











<!-- backlinks-start -->
### Backlinks
- [Google Antigravity Qa 2026](wiki/google-antigravity-qa-2026.md)
- [Десктопные AI-агенты для кода (2026)](wiki/desktop-ai-agents-2026.md)
<!-- backlinks-end -->

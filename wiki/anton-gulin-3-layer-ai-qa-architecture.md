# Anton Gulin: 3-Layer AI Test Automation Architecture

**Источник:** [anton.qa/blog/posts/ai-test-automation-architecture-3-layer-system](https://www.anton.qa/blog/posts/ai-test-automation-architecture-3-layer-system) (May 13, 2026)

**Автор:** Anton Gulin — первый человек с титулом "AI QA Architect" в LinkedIn. Бывший Apple SDET (Apple.com / Apple Card).

---

## Основной тезис

AI-тестирование без архитектуры — это просто prompt output без production gate. Anton делит систему на три обязательных слоя.

## 3 слоя

| Layer | Plain meaning | Main question |
|-------|--------------|---------------|
| **Orchestration** | test control plan | What risk should this cover? |
| **Execution** | actual test run | Did it run in the real pipeline? |
| **Evidence** | proof from runs | Can a human review it? |

Если один слой отсутствует — система даёт false confidence.

### Layer 1: Orchestration

Пять вопросов перед тем как AI пишет хоть строчку кода:

1. What user flow matters?
2. What risk does this test cover?
3. What data must exist first?
4. What browser state is allowed?
5. What failure should block release?

AI может помочь с draft, но risk call остаётся за человеком. "That is the difference between generation and architecture."

### Layer 2: Execution

Тест должен выжить в CI. Локальный demo не считается.

Ключевые требования:
- CI = automated build server
- Browser state control
- Cleanup, retries, test data, worker isolation
- Stable launch control (playwright-mcp v0.0.75 serializes shared browser launch)

### Layer 3: Evidence

Самый пропускаемый слой. Каждый AI-тест должен оставлять receipts:

- Trace
- Screenshot
- Log
- Video (когда timing matters)
- Saved browser state (когда auth matters)

Цель: reviewer должен проверить run без перезапуска.

## Practical Gate: 6 условий перед deploy AI-теста

| Gate | Pass condition |
|------|---------------|
| Scope | The test maps to one named risk |
| Data | Test data setup is explicit |
| State | Browser state is controlled |
| Run | The test passes in CI |
| Evidence | Trace or equivalent proof exists |
| Review | A human can explain the failure mode |

## Где AI полезен (по Anton)

1. Drafts coverage ideas
2. Writes first-pass test code
3. Explains failures from evidence

Humans still own: risk definition, evidence review, release decisions.

## The Rule

> Never ask AI to expand test coverage first.
> Build the proof system before that.
> Generation is cheap.
> Evidence is the architecture.

## Маппинг на наш стек

| Слой | У нас |
|------|-------|
| Orchestration | AGENTS.md boundaries + Autonoma exploration + Playwright Planner |
| Execution | Playwright CI/CD (playwright.yml, nightly.yml, contracts.yml) + Docker + SSH tunnel to local OrangeHRM |
| Evidence | Allure reports + Playwright trace viewer + screenshots + video on failure |
| Gate | Mutation score gate + smoke suite в CI + human review (AGENTS.md Rules) |

## Что Anton добавляет к нашему пониманию

1. **Чёткое разделение Orchestration/Execution/Evidence** — у нас все три есть, но не формализованы как слои
2. **Practical Gate** — 6 условий можно добавить как чеклист в AGENTS.md или CI/CD quality gates
3. **Evidence-first** — наш Allure покрывает, но video и saved browser state не везде
4. **Риск-ориентация** — Anton явно ставит risk question перед генерацией. У нас risk есть в TEST_CASES.md, но не всегда формализован

## Related

- [[opencode-skill-creator]] — eval-driven skill development от Anton Gulin. Логически встраивается в Layer 1 (Orchestration): создание скилла = формализация того, какой риск и как должен покрывать AI-агент.
- [[people/anton-gulin]] — полный профиль автора


<!-- backlinks-start -->
### Backlinks
- [Carbon Ai Agentic Verification Harness](wiki/carbon-ai-agentic-verification-harness.md)
<!-- backlinks-end -->

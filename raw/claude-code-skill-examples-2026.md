# Claude Code SKILL.md — QA Examples (2026)

Источник: исследование Victor Ematin, Jul 2026. Формат SKILL.md + MCP.

## Skill 1: qa-playwright-expert.md — Чистый Playwright E2E

```markdown
# Skill: Autonomous QA & Playwright E2E Automation

## Description
Senior SDET skill. Автономное исследовательское тестирование, генерация тестов,
self-healing, E2E автоматизация через Playwright + TypeScript.

## Context & Environment
- Testing Framework: Playwright (v1.50+) with TypeScript
- Target App: Next.js Web Application
- Main Directories:
  - Tests: `./tests/e2e/`
  - Page Objects: `./tests/page-objects/`
  - Test Data: `./tests/fixtures/`
- Execution Command: `npx playwright test`
- Report Path: `./playwright-report/index.html`

## Workflow 1: Test Generation from User Story
1. Scan `./tests/page-objects/` — существует ли POM
2. Если POM нет — создать со strict user-facing locators
   (`page.getByRole`, `page.getByText`)
3. Тест в `./tests/e2e/` — Arrange-Act-Assert
4. `npx playwright test <test-file>` — verify

## Workflow 2: Self-Healing & Debugging Loop
При падении теста:
1. Парсим stack trace / trace file
2. Timeout / Selector Error → Computer Use / DOM inspection → rewrite locator
3. Flakiness / Race Condition → web-first assertions (`expect(locator).toBeVisible()`)
   — никогда `page.waitForTimeout()`
4. rerun до 3 раз

## Workflow 3: Automated Bug Reporting
При баге в приложении (не в тесте):
1. Capture console logs, network payloads, reproduction
2. Формат Bug Report (готов для Jira/GitHub Issues через MCP)

## Constraints
- ❌ Не трогать `./src/` и `./app/` без разрешения
- ✅ Parallel-безопасные тесты, никакого shared global state
- ✅ `afterEach`/`afterAll` cleanup
- ✅ После каждого run: summary (Total, Passed, Failed, Actions)
```

## Skill 2: qa-hybrid-computer-use.md — Playwright + Computer Use

```markdown
# Skill: Hybrid QA Engine (Playwright + Computer Use)

## Description
Гибрид: программная автоматизация (Playwright) + визуально-пространственные
OS-взаимодействия (Computer Use). Для сложных, non-deterministic UI.

## Context & Environment
- Automation Core: Playwright (TypeScript)
- Visual Engine: Anthropic Computer Use API (Display Server: X11 / VNC)
- Working Paths: `./tests/e2e/`, `./tests/visual-baselines/`
- Execution Target: `http://localhost:3000`

## Hybrid Execution Rules
1. **Playwright (Default):** CRUD, формы, API, fast assertions
2. **Computer Use (Escalation):** Если Playwright упал с TimeoutError / Selector not found,
   ИЛИ когда нужна layout validation, canvas, drag-and-drop

## Workflow 1: Self-Healing via Computer Use
1. Stop headless Playwright
2. Docker/VNC container → visible browser
3. `computer_use_tool`: `mouse_click`, `key_press`, `take_screenshot`
4. Compare visual DOM state with code locator
5. rewrite CSS/XPath → `page.getByRole`
6. `npx playwright test` — verify

## Workflow 2: Visual & Layout Testing
Для charts, maps, SVG editors:
1. Playwright → navigate to target state
2. Computer Use image analysis
3. Compare с baselines в `./tests/visual-baselines/`
4. Check overlapping, clipping, colors, layout
5. Bug report с pixel-mismatch coordinates

## Computer Use Configuration
- Default Resolution: 1280x800, 24-bit color
- OS Command: `xdotool` / `screenshot` (Anthropic Agent SDK)
- Browser: Chromium `--no-sandbox`

## Constraints
- ❌ Не больше 3 координатных adjustment — иначе UI defect
- ✅ Close orphan browser tasks (`pkill chromium`) перед Playwright
- ✅ Только discrete state screenshots, не video streaming
```

## Резюме

Связка Computer Use + Playwright = вершина гибридного тестирования 2026.
Playwright — для быстрых программных проверок. Computer Use — для:
- Canvas, динамические графики
- Капчи, Flash-подобные компоненты
- Сложные SVG/iframe
- Сверка вёрстки (визуальная регрессия)

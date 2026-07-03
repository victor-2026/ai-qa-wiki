## Maestro vs Appium — Сравнительный анализ (2026)

### Философия

| | **Maestro** | **Appium** |
|---|---|---|
| Год | 2022 | 2012 |
| Подход | Декларативный (YAML flows) | Императивный (WebDriver protocol) |
| Языки | YAML только | Java, Python, JS, C#, Ruby, Kotlin |
| Установка | 10 мин (один бинарник) | 30–60 мин (Node.js + драйверы + SDK) |

### Возможности

| **Maestro** | **Appium** |
|---|:---|
| ✓ tapOn, inputText, scroll, swipe | ✓ Полный WebDriver API |
| ✓ assertVisible, assertNotVisible | ✓ Любые кастомные assertions |
| ✓ launchApp, clearState | ✓ Deep linking, push-нотификации |
| ✓ Переменные, условия, runFlow | ✓ Циклы, conditional logic, data-driven |
| ✓ WebViews, браузеры | ✓ Hybrid apps, WebViews |
| ✓ iOS (simulator) + Android | ✓ iOS (реальные устройства!) + Android + Windows |
| ✓ Flutter, React Native | ✓ Flutter, React Native, любые native |
| ✓ Геолокация, network stubbing | ✓ Gesture simulation, TouchID, биометрия |
| ✓ Maestro Studio (рекордер) | ✓ Appium Inspector, record & playback |
| ✓ Maestro Cloud (parallel paid) | ✓ BrowserStack/Sauce Labs/LambdaTest |
| ✓ MCP сервер (AI Agents) | ✗ Нет нативного MCP |
| ✗ **Нет реальных iOS устройств** | ✓ Реальные iOS и Android |
| ✗ **Нет 2FA кодов, сложной логики** | ✓ Любая сложность |

### Сравнение в цифрах

| Метрика | Maestro | Appium |
|---|---|---|
| Скорость boot to screen | **~12s** | ~24s (2x медленнее) |
| Flakiness | **Встроенная** (auto-retry, smart wait) | Ручная (нужны custom wait utilities) |
| Setup time | **~10 мин** | ~30–60 мин |
| Сообщество | Маленькое (emerging) | **Огромное** (10+ лет) |
| CI integration | Тривиальный (бинарник + YAML) | **Глубокая** (любой CI + device farm) |
| Версия | 1.x | **3.5.1** (Jun 2026) |

### Ограничения

**Maestro:**
- Только YAML — сложная логика (loops, conditional branching) превращается в грязь
- Нет реальных iOS устройств (только simulator)
- Нет детальных репортов
- Останавливается на первой ошибке (no continue-on-failure)
- Маленькое сообщество — решения редких проблем нет в Google
- No screenshot on failure (запрошено, не реализовано)
- Regex на iOS не работает (только Android)

**Appium:**
- Высокий порог входа — требует Node.js, SDK, драйверы, environment variables
- Flaky по дефолту — timing issues, нет built-in retry
- Locator maintenance — каждый change в UI ломает селекторы
- Инфраструктура — ты владеешь сервером, драйверами, плагинами
- Медленный boot (~24s vs Maestro ~12s)
- Community support — только форумы, нет dedicated support

### Когда что выбирать

**Maestro побеждает когда:**
- Быстрый старт (proof of concept, MVP)
- Простые smoke/critical path тесты
- Команда без Java/Python (QA analysts, manual testers)
- Flutter или React Native приложение
- CI важнее complexity (один бинарник)
- Существующая инфраструктура не рассчитана на Appium

**Appium побеждает когда:**
- Нужны реальные iOS устройства
- Enterprise масштаб — сотни тестов, device farms
- Сложные сценарии — 2FA, push, gestures, биометрия
- Команда уже пишет на Python/Java/JS
- Есть automation engineers для поддержки
- Нужен полный контроль над execution layer

### Кейс: FrontRow (2026)

**Контекст:** тестовое задание — 7 дней, мобильное приложение для live events (iOS + Android), open-source инструментарий. FrontRow: auth, events feed, search, ticketing, billing, push notifications.

**Результат:** 35 Maestro flows за 7 дней, 0 flaky.

#### Структура тестов

| Модуль | Maestro flows | Покрытие |
|--------|---------------|----------|
| smoke | 3 | Launch, onboarding skip, onboarding complete |
| auth | 7 | Login, register, forgot password, recovery deeplinks, profile edit, language switch |
| events | 8 | Browse, search, genre filter, sort, pagination, reviews, favorites, follow artist |
| tickets | 4 | Buy, tier select, cancel, transfer |
| billing | 3 | Payment methods CRUD, buy success, buy decline |
| native | 1 | Native device interaction demo |
| debug | 1 | Failure trigger |
| capabilities | 1 | Haptic feedback |

#### Сравнение одного и того же сценария

**Задача:** запустить приложение, дождаться экрана Events, проверить видимость.

**Maestro** (1 файл, 11 строк, 0 импортов, 0 конфигов):

```yaml
appId: app.frontrow.qa
---
- launchApp:
    clearState: true
- extendedWaitUntil:
    visible:
      id: 'screen.events'
    timeout: 20000
- assertVisible: 'Events'
```

**Appium + WebdriverIO** (4 файла, ~50 строк суммарно, импорты, конфиги):

```typescript
// wdio.ios.conf.ts (23 строки конфига)
export const config: Options.Testrunner = {
  ...sharedConfig,
  capabilities: [{
    platformName: 'iOS',
    'appium:automationName': 'XCUITest',
    'appium:deviceName': 'iPhone 15',
    'appium:platformVersion': '17.5',
    'appium:app': APP_PATH,
  }],
};
```

```
// smoke.spec.ts (тест)
import { expect } from '@wdio/globals'
describe('FrontRow iOS', () => {
  it('should display the Events screen on launch', async () => {
    const eventsScreen = await $('~screen.events')
    await eventsScreen.waitForDisplayed({ timeout: 20000 })
    expect(await eventsScreen.isDisplayed()).toBe(true)
  })
})
```

**Реальный опыт:** Appium session создалась, но первый же `findElement("accessibility id", "screen.events")` упал с `NoSuchElementError` (см. лог). Maestro отработал с первого раза — built-in wait и retry поглотили timing.

#### Вывод по кейсу

Maestro выиграл тестовое потому что "fast and reliable" победило "flexible but fragile" на недельном дедлайне. Однако Appium остаётся необходимым для:
- Реальных iOS устройств (Maestro поддерживает только simulator)
- Сложных сценариев (2FA, биометрия, сложные жесты)
- Enterprise device farms (BrowserStack, Sauce Labs)

**Реальная стратегия:** Maestro на 80% coverage (smoke + critical paths), Appium на 20% edge cases.

### Тренд 2026

Maestro догоняет по функциональности, но остаётся нишевым для простых E2E. Appium 3.x де-факто standard для enterprise mobile automation. Ключевое преимущество Maestro в 2026 — **MCP сервер** (AI Agents могут писать и чинить YAML flows), чего у Appium нет.

Если interviewer спрашивает про mobile testing — Maestro для "быстро и стабильно", Appium для "всё остальное".

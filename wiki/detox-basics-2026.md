# Detox Basics for React Native Testing

## Что такое Detox

**Detox** — gray-box E2E testing framework для React Native от Wix. Внедряется в RN runtime, мониторит JS thread, ждёт idle. Никаких `sleep()`, `waitForTimeout`, или explicit waits.

**Архитектура:**

```
React Native App
    │
    ├── Detox Library (встроен в билд)
    │       └── Мониторит JS thread + native UI
    │
    ▼
Test Runner (Jest/Mocha)
    │
    ├── element(by.id('foo')).tap()
    └── expect(element(...)).toBeVisible()
```

## Detox vs Playwright vs Appium

| Аспект | Detox | Playwright | Appium |
|--------|-------|------------|--------|
| **Архитектура** | Gray-box (в RN runtime) | Browser protocol | WebDriver HTTP |
| **Sync** | Automatic (idle monitoring) | Automatic (auto-wait) | Explicit (waitForElement) |
| **Платформы** | iOS + Android (RN) | Web only | iOS + Android (native) |
| **Скорость** | Fast | Fast | Medium |
| **Flaky rate** | Low | Low | Medium |
| **Установка** | Сложная (native deps) | Простая | Средняя |
| **Когда выбрать** | React Native | Web apps | Native/hybrid |

## Playwright → Detox mapping (для быстрого старта)

| Концепт | Playwright | Detox |
|---------|-----------|-------|
| Launch | `page.goto(url)` | `device.launchApp()` |
| Locator | `page.getByTestId('foo')` | `element(by.id('foo'))` |
| Click | `locator.click()` | `element(by.id('foo')).tap()` |
| Type | `locator.fill('text')` | `element(by.id('foo')).typeText('text')` |
| Visible | `expect(locator).toBeVisible()` | `expect(element(by.id('foo'))).toBeVisible()` |
| Text | `expect(locator).toHaveText('x')` | `expect(element(by.id('foo'))).toHaveText('x')` |
| Deep link | `page.goto('myapp://')` | `device.openURL({ url: '...' })` |
| Scroll | `locator.scrollIntoView()` | `element(by.id('list')).scrollTo('bottom')` |
| Wait | `waitForSelector()` | `waitFor(element(by.id('foo'))).toBeVisible()` |

## Пример теста

```javascript
describe('Promo codes', () => {
  beforeEach(async () => {
    await device.launchApp({ newInstance: true })
    await element(by.id('events.item.evt_001')).tap()
    await element(by.id('eventDetail.buyButton')).tap()
  })

  it('applies FRONTROW50 → $22.50', async () => {
    await element(by.id('buyTicket.promoInput')).typeText('FRONTROW50\n')
    await element(by.id('buyTicket.promoApplyButton')).tap()
    await expect(element(by.id('buyTicket.totalAmount'))).toHaveText('$22.50')
  })
})
```

**Ключевое преимущество:** нет `waitForTimeout` — Detox ждёт, пока приложение закончит все асинхронные операции (setTimeout, fetch, animation, navigation).

## Конфигурация (.detoxrc.js)

```javascript
module.exports = {
  testRunner: { args: { config: 'e2e/.detoxrc.js' } },
  apps: {
    'ios.debug': {
      type: 'ios.app',
      build: 'xcodebuild ...',
      binaryPath: 'ios/build/Build/Products/Debug-iphonesimulator/App.app'
    }
  },
  devices: {
    simulator: {
      type: 'ios.simulator',
      device: { type: 'iPhone 16' }
    }
  },
  configurations: {
    'ios.sim.debug': {
      device: 'simulator',
      app: 'ios.debug'
    }
  }
}
```

## Когда Detox НЕ подходит

- **Не React Native приложение** — Native iOS/Android, Flutter, Xamarin
- **WebView-heavy приложение** — Detox не управляет WebView (нужен Appium)
- **Команда без RN опыта** — Detox требует настройки native build pipeline
- **Редкие платформы** — Detox не поддерживает tvOS, watchOS, Android TV

## Detox vs Maestro

| Аспект | Detox | Maestro |
|--------|-------|---------|
| Тип | Code (JS/TS) | YAML |
| RN sync | ✅ Automatic | ✅ Implicit |
| Setup | 1-2 дня | 1 час |
| CI integration | npm test | maestro test |
| Learning curve | Средняя | Низкая |
| Гибкость | Высокая (JS код) | Низкая (YAML flow) |
| Когда выбрать | Сложная логика, CI | Быстрые smoke-тесты |

## Что сказать на интервью

> «Detox — лучший выбор для React Native E2E, потому что синхронизируется с RN runtime, а не ждёт таймауты. Если приложение на RN — Detox даёт меньше flaky тестов чем Appium. Я использовал Detox на FrontRow проекте: 7 тестов, 0 explicit waits. Но для кросс-платформенного тестирования (если есть WebView) — добавляю Appium.»

## Источники

- Официальная документация: wix.github.io/Detox
- Статья: Detox vs Appium — The Gap Is Architecture (linkedin-posts/Tools/detox-vs-appium.md)
- Код: FrontRow e2e/ (5 .test.js файлов)

**Created:** 2026-07-02

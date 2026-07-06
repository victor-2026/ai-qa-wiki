# Mobile Testing Infrastructure: Parallel Mac + Windows, MCP, Remote Execution

## Context

На проекте FrontRow (RN, Expo 54, iOS 26.3) используется 3 фреймворка: Appium, Detox, Maestro.
Возник вопрос: можно ли запускать тесты удалённо (MCP/agent mode) и параллельно на MacBook + Win-сервере.

## MCP Support

| Tool | MCP | How | Notes |
|------|-----|-----|-------|
| **Appium** | ✅ Official `appium-mcp` | `npx appium-mcp@latest` (stdio) | Полный контроль: session mgmt, AI vision (element find по NL), генерация тестов. Подключается к любому Appium Server. |
| **Maestro** | ✅ docs MCP + community | `https://docs.runmaestro.ai/mcp` (HTTP) | Только поиск по документации. Запуск flows — только CLI локально или Maestro Cloud. |
| **Detox** | ❌ | — | Нет MCP, нет remote server. Только локальный запуск. |

## Remote Execution

### Appium — native remote server
Appium Server 2.x изначально клиент-серверный. Можно:
- Запустить Appium Server на Windows (Android UiAutomator2)
- Запустить Appium Server на Mac (iOS XCUITest)
- Тесты шлют HTTP запросы на нужный сервер
- Один код тестов, два раннера

### Maestro — local only
- Нет self-hosted remote режима
- Только Maestro Cloud (платный) или локальный CLI

### Detox — local only
- Не поддерживает remote execution
- XCUITest требует macOS физически

## Mac + Windows Parallel Architecture

```
MacBook (macOS)                    Win Server (Windows)
┌──────────────────────┐          ┌──────────────────────┐
│  Appium Server (iOS) │          │  Appium Server (And) │
│  XCUITest driver     │          │  UiAutomator2 driver │
│  iOS Simulator       │          │  Android Emulator    │
│  Detox (iOS only)    │          │  Maestro (Android)   │
│  Maestro (iOS)       │          └──────────────────────┘
└──────────────────────┘
          │                              │
          └────────── Git repo ──────────┘
            (shared test code + configs)
```

## Xcode / iOS on Windows

**Невозможно нативно.** Xcode и iOS Simulator требуют macOS.

### Альтернативы:
1. **Облачный Mac** — Rentamac ($15/day), MacStadium, MacinCloud
2. **Remote iOS Simulator** — Visual Studio 2022 + Mac build host (.NET MAUI только)
3. **Hackintosh** — VM macOS на Windows. Легально серо, Apple EULA. Нестабильно.
4. **Cloud device labs** — BrowserStack, Sauce Labs, LambdaTest (реальные устройства)

## Android on Windows

**Полностью нативно.** Android Studio + Android Emulator работают на Windows. Appium UiAutomator2 и Maestro поддерживают Android без ограничений.

## Cloud Device Labs

| Service | iOS | Android | Appium | Maestro | Pricing |
|---------|-----|---------|--------|---------|---------|
| BrowserStack | ✅ real | ✅ real | ✅ | ✅ | от $150/mo |
| Sauce Labs | ✅ real+sim | ✅ real+emu | ✅ | ❓ | от $99/mo |
| LambdaTest | ✅ real+sim | ✅ real+emu | ✅ | ❓ | от $150/mo |
| Maestro Cloud | ✅ sim | ✅ emu | ❌ | ✅ native | custom |

Cloud labs — альтернатива Win-серверу, если не хочется поддерживать сервер.

## TL;DR

- **Appium** — единственный с native remote server и официальным MCP. Mac → iOS, Win → Android.
- **Maestro** — локально на каждой платформе, или Maestro Cloud.
- **Detox** — только Mac.
- Для Android на Windows — все три инструмента работают (кроме Detox, он только iOS).
- Для iOS на Windows — только облачные сервисы или аренда Mac.

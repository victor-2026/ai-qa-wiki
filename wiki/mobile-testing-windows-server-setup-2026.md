# Windows Server: Mobile Testing Setup

**Target:** PC-224 (192.168.1.224, Win 10 Pro, 64GB, ZeroTier 10.24.175.30)

## What's Already Installed

Docker, Ollama, Qdrant, BGE-M3. **Ничего для Android/mobile testing.**

## Installation Order

1. **Java JDK 17** — `winget install EclipseAdoptium.Temurin.17.JDK`
2. **Android Studio + SDK 34** — `winget install Google.AndroidStudio` + SDK Manager
3. **Environment Variables** — `ANDROID_HOME`, `ANDROID_SDK_ROOT`, platform-tools/emulator в PATH
4. **Node.js 22** — `winget install OpenJS.NodeJS.LTS`
5. **Appium** — `npm i -g appium && appium driver install uiautomator2`
6. **AVD** — `sdkmanager "system-images;android-34;google_apis;x86_64"` + `avdmanager create avd -n Pixel_9_API_34 ...`
7. **Maestro** — download from GitHub releases, add to PATH

## Architecture

```
Mac: Appium iOS + XCUITest + iOS Simulator
Win: Appium Android + UiAutomator2 + Android Emulator
Git: общий код тестов, разные конфиги
```

Appium Server на Win: `appium --address 0.0.0.0 --port 4723`

## Parallel Run

Appium — remote server через ZeroTier (`hostname: 10.24.175.30`). Maestro — локально на каждой машине.

## Access

`ssh win-server` (key auth, Victor@192.168.1.224)

**Note:** Server currently offline. Setup to be done when powered on.

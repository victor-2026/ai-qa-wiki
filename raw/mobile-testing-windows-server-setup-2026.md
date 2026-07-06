# Windows Server: Mobile Testing Setup

## Target Machine

- **Host:** PC-224 (192.168.1.224)
- **OS:** Windows 10 Pro
- **RAM:** 64 GB
- **CPU:** Threadripper 1920X
- **GPU:** 6 GB (RTX 3060)
- **SSH:** `ssh win-server` (Victor@192.168.1.224, key auth)
- **ZeroTier:** 10.24.175.30

## Prerequisites Already Installed

- Docker (qa-automation-sandbox)
- Ollama (4 models)
- Qdrant
- Python + FastAPI (BGE-M3)

## What Needs to Be Installed

### 1. Android Studio + SDK

```powershell
# Download Android Studio
winget install -e --id Google.AndroidStudio

# Or manually: https://developer.android.com/studio
```

После установки:
- Open Android Studio → SDK Manager
- Install SDK Platforms: Android 34, 35
- Install SDK Tools: Android SDK Build-Tools, Platform-Tools, Emulator
- Set env vars:

```powershell
[System.Environment]::SetEnvironmentVariable("ANDROID_HOME", "$env:LOCALAPPDATA\Android\Sdk", "User")
[System.Environment]::SetEnvironmentVariable("ANDROID_SDK_ROOT", "$env:LOCALAPPDATA\Android\Sdk", "User")
```

Add to PATH:
```powershell
$path = [Environment]::GetEnvironmentVariable("PATH", "User")
$add = "$env:LOCALAPPDATA\Android\Sdk\platform-tools;$env:LOCALAPPDATA\Android\Sdk\emulator;$env:LOCALAPPDATA\Android\Sdk\tools\bin"
[Environment]::SetEnvironmentVariable("PATH", "$path;$add", "User")
```

### 2. Java JDK 17

```powershell
winget install -e --id EclipseAdoptium.Temurin.17.JDK

# Verify
java -version
```

### 3. Node.js 22

```powershell
winget install -e --id OpenJS.NodeJS.LTS

# Verify
node --version
npm --version
```

### 4. Appium Server + Drivers

```powershell
npm install -g appium
appium driver install uiautomator2
appium plugin install --source=npm appium-wait-plugin

# Verify
appium --version
appium driver list --installed
```

### 5. Maestro

```powershell
# Via Maestro GitHub releases
# Download maestro-windows-amd64.zip from https://github.com/mobile-dev-inc/maestro/releases
# Unzip to C:\maestro
# Add C:\maestro to PATH

# Or via choco if installed:
# choco install maestro
```

### 6. Android Virtual Device (AVD)

```powershell
# List available system images
sdkmanager --list | findstr "system-images;android-34"

# Install a Pixel 9 image
sdkmanager "system-images;android-34;google_apis;x86_64"

# Create AVD
avdmanager create avd -n Pixel_9_API_34 -k "system-images;android-34;google_apis;x86_64" -d pixel_9

# Verify
emulator -list-avds
```

### 7. WSL2 + ADB over Network (опционально)

WSL2 для запуска Appium-сервера в Linux, а Android эмулятор в Windows — ADB коннектится через localhost.

```powershell
# Enable WSL2
wsl --install -d Ubuntu

# In WSL2
sudo apt update && sudo apt install -y adb
adb connect host.docker.internal:5555
```

## Architecture

```
MacBook                                  Win Server (PC-224)
┌───────────────────┐                   ┌──────────────────────┐
│ Appium (iOS)      │                   │ Appium (Android)     │
│ XCUITest driver   │                   │ UiAutomator2 driver  │
│ iOS Simulator     │                   │ Android Emulator     │
│ Detox             │                   │ ADB                  │
│ Maestro (iOS)     │                   │ Maestro (Android)    │
└───────────────────┘                   └──────────────────────┘
        │                                        │
        └─────────── Git (frontrow) ─────────────┘
```

Appium Server on Win:
```powershell
appium --address 0.0.0.0 --port 4723 --use-plugins=wait
```

На Mac тесты шлют запросы на Win Appium через ZeroTier:
```
APPIUM_REMOTE=http://10.24.175.30:4723
```

## Verification Checklist

- [ ] `java -version` — Java 17
- [ ] `node --version` — Node 22+
- [ ] `appium --version` — Appium 2.x
- [ ] `appium driver list --installed` — uiautomator2
- [ ] `emulator -list-avds` — Pixel_9_API_34
- [ ] `adb devices` — эмулятор в списке
- [ ] `maestro --version` — Maestro CLI
- [ ] Appium создаёт сессию на Android
- [ ] Maestro видит Android эмулятор

## Parallel Run (Mac + Win)

### Appium — один код на две платформы

```typescript
// wdio.ios.conf.ts — локально на Mac
exports.config = {
  port: 4723,
  capabilities: [{
    platformName: 'iOS',
    'appium:deviceName': 'iPhone 17 Pro',
    'appium:platformVersion': '26.3',
  }],
}
```

```typescript
// wdio.android.conf.ts — на Win через ZeroTier
exports.config = {
  hostname: '10.24.175.30',
  port: 4723,
  capabilities: [{
    platformName: 'Android',
    'appium:deviceName': 'Pixel_9_API_34',
    'appium:platformVersion': '34',
    'appium:automationName': 'UiAutomator2',
  }],
}
```

### Maestro — локально на каждой машине

```bash
# Mac
maestro test --device iOS tests/

# Win
maestro test --device Android tests/
```

## Troubleshooting

| Problem | Fix |
|---------|-----|
| ADB не видит эмулятор | `adb kill-server && adb start-server && adb devices` |
| Эмулятор медленный | Включить GPU acceleration (requires Intel HAXM или WHPX) |
| Appium не стартует | Проверить Java: `java -version` (нужна 17+) |
| ZeroTier нет коннекта | `ping 10.24.175.30` с Mac, проверить что обе машины в одной сети ZeroTier |

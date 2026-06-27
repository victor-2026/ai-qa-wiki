# VirusTotal — Практическое руководство

**Дата:** 2026-06-19
**Источники:** virustotal.com, практический опыт

---

## Что такое VirusTotal

Бесплатный сервис, который сканирует файлы и URL **60+ антивирусными движками** одновременно.
Не заменяет локальный антивирус, но даёт второй opinion на подозрительные файлы.

---

## Для обычного пользователя

### Когда проверять

- **Скачал архив с GitHub** — особенно из репозиториев, где нет звёзд и код незнакомый
- **Пришёл файл от незнакомца** — email, Telegram, WhatsApp
- **Сомнительный софт** — кейгены, крэки, "бесплатные VPN"
- **Файл с расширением `.exe`, `.bat`, `.ps1`, `.scr`, `.vbs`** внутри архива, который маскируется под конфиг/ключи
- **ISO/DMG образы** — вирусы часто маскируются под установщики
- **PDF документы** — макросы, эксплойты

### Как проверить (простой способ)

1. Заходишь на `virustotal.com/gui/home/upload`
2. Кидаешь файл (до 650 MB)
3. Ждёшь 10-60 секунд
4. **Если хотя бы 2 engine детектят = не открывать**

> 1 engine может быть ложным срабатыванием. 2+ — вероятность заразы высокая.

### Как проверить без загрузки (SHA256)

Если файл уже кто-то сканировал:

```bash
# macOS — получаем хеш
shasum -a 256 подозрительный_файл.exe
# Linux — sha256sum подозрительный_файл.exe

# Вставляем полученный хеш на virustotal.com/gui/search/{hash}
```

### Браузерное расширение

Установи `VirusTotal` для Chrome/Firefox — правый клик на ссылке → "Search with VirusTotal".

### Telegram боты

- `@virustotal_bot` — официальный. Отправляешь файл → получаешь результат
- `@file_scan_bot` — альтернатива

### Бесплатно?

Да. Регистрация по email (нужна для истории поиска и API запросов).
- Free: 500 запросов/день
- Premium: $89/year (не нужно для личного использования)

---

## Для QA автоматизации

### CI/CD Security Gate

Добавить шаг в GitHub Actions, который проверяет зависимости перед запуском тестов:

```yaml
- name: Check dependency hashes on VirusTotal
  run: |
    for f in package-lock.json node_modules/.package-lock.json; do
      [ -f "$f" ] || continue
      hash=$(shasum -a 256 "$f" | cut -d' ' -f1)
      response=$(curl -s "https://www.virustotal.com/api/v3/files/$hash")
      positives=$(echo "$response" | python3 -c "import sys,json; d=json.load(sys.stdin); print(d.get('data',{}).get('attributes',{}).get('last_analysis_stats',{}).get('malicious',0))" 2>/dev/null || echo "0")
      [ "$positives" -gt "1" ] && echo "⚠️  $f — $positives engines detect threat" && exit 1 || echo "✅ $f clean"
    done
```

**Лучше проверять:** хеши зависимостей (`package-lock.json`, `go.sum`, `Cargo.lock`) один раз при `npm install`, а не каждый запуск тестов (лимит 500/день).

### Проверка Docker образов

```bash
# Получить hash образа
docker pull alpine:latest 2>/dev/null
IMAGE_ID=$(docker images --no-trunc -q alpine:latest)
echo "alpine:latest → $IMAGE_ID"

# Вручную: вставить IMAGE_ID на virustotal.com/gui/search/
```

### Проверка URL в тестовом окружении

```bash
curl -s --request POST \
  --url 'https://www.virustotal.com/api/v3/urls' \
  --header "x-apikey: $VT_API_KEY" \
  --form "url=$TEST_URL" \
  | python3 -c "import sys,json; print(json.load(sys.stdin))"
```

### API лимиты

| Tier | Rate | Daily |
|------|------|-------|
| Free | 4 req/min | 500 |
| Premium | 20 req/min | 50000 |

Для личного CI/CD пайплайна Free достаточно, если проверять ключевые файлы, а не каждый артефакт.

---

## Как не надо

- ❌ Проверять каждый `npm install` на CI — съест лимит за час
- ❌ Слепо доверять 0/60 — бывают свежие угрозы (zero-day)
- ❌ Игнорировать 1/60 — может быть ложным, но лучше перепроверить
- ❌ Кидать конфиденциальные файлы (API ключи, пароли) — VirusTotal хранит результат публично

---

## Резюме

| Сценарий | Действие |
|----------|----------|
| Скачал файл с GitHub | VT перед открытием |
| Пришёл файл в Telegram | VT → бот |
| Подозрительный URL | VT URL scanner |
| CI/CD зависимость | VT API → fail build |
| Docker образ | VT lookup по hash |

VT не панацея, но бесплатный второй opinion, который ловит ~95% известных угроз.

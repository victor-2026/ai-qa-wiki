# OrangeHRM 5.4 → 5.8.1 Upgrade: Problems & Fixes

**Дата:** 2026-06-12
**Контекст:** Local Docker на MacBook (Intel 2019, 16GB RAM)
**Старая версия:** 5.4
**Новая версия:** 5.8.1
**Database:** MariaDB 10.11.4, 175 tables, ~1.1 MB

---

## 1. Docker Desktop не стартует engine

**Симптом:** `docker ps` — timeout 19+ минут, engine never starts. Docker Desktop 29.5.2.

**Причина:** Баг WSL 2 backend в Docker Desktop на Windows 10 Pro (X399). На MacBook (Intel 2019) — работает без проблем.

**Решение:** `sudo apt install docker.io` напрямую в WSL 2 Ubuntu. Docker Desktop не нужен.

**Урок (Session 35):** Для WSL 2 с Docker Desktop баг engine — ставить `docker.io` вручную.

---

## 2. libllhttp.9.3.dylib missing (macOS)

**Симптом:** Node.js не стартует:
```
dyld: Library not loaded: /usr/local/opt/llhttp/lib/libllhttp.9.3.dylib
```

**Причина:** Homebrew обновил llhttp с 9.3 до 9.4.1, но `node` собран под 9.3.

**Решение:**
```bash
ln -s /usr/local/Cellar/llhttp/9.4.1/lib/libllhttp.9.4.1.dylib \
      /usr/local/Cellar/llhttp/9.4.1/lib/libllhttp.9.3.dylib
```

---

## 3. Installer redirect после смены image

**Симптом:** После `docker compose up -d` с `orangehrm/orangehrm:5.8.1` — редирект на `/installer/index.php`.

**Причина:** Схема БД 5.4 несовместима с 5.8.1 — требуется миграция.

**Решение:** CLI-команда `upgrade:run` (не web-установщик):
```bash
docker exec orangehrm php /var/www/html/installer/console upgrade:run \
  --dbHost orangehrm-db \
  --dbPort 3306 \
  --dbName orangehrm \
  --dbUser orangehrm \
  --dbUserPassword orangehrm_pass \
  --systemCheckAcceptRisk \
  --no-interaction
```

**Нюанс:** Команда интерактивная — все параметры обязательны. Без `--no-interaction` запрашивает подтверждение на каждом шаге.

**Результат:**
- PHP version: 8.3.30
- MySQL Server: 10.11.4-MariaDB
- Database permissions → OK
- Applying database changes → OK
- Creating configuration files → OK (создан `lib/confs/Conf.php`)

---

## 4. Admin пароль не работает после upgrade

**Симптом:** `curl -X POST /auth/validate` → всегда 302 redirect на login. Ни `Orangehrm@2026` (5.4), ни `admin123` (docker-compose env) не подходят.

**Причина:** Пароль из БД 5.4 (bcrypt hash `$2y$12$...`) не совпадает. `ORANGEHRM_PASSWORD` env var в docker-compose работает только для **fresh install**, не для upgrade.

**Решение:** Сброс пароля через прямую запись в БД:
```bash
# 1. Сгенерировать bcrypt hash
docker exec orangehrm php -r "echo password_hash('Orangehrm@2026', PASSWORD_BCRYPT, ['cost' => 12]);"

# 2. Обновить в БД
docker exec orangehrm-db mysql -uorangehrm -porangehrm_pass orangehrm \
  -e "UPDATE ohrm_user SET user_password = '$2y$12\$...' WHERE user_name = 'Admin';"
```

**Важно:** cost должен совпадать с оригинальным (12). Если сгенерировать с cost 10 (PHP default) — логин всё равно не работает.

---

## 5. Три @local теста упали на 5.8.1

| Тест | Проблема |
|------|----------|
| `myinfo.spec.ts` — edit personal details | Селектор `#firstName` / `input[name="firstName"]` может измениться в 5.8.1 |
| `pim.spec.ts` — edit employee first name | `.oxd-table-row .oxd-table-cell` структура строки таблицы |
| `pim.spec.ts` — delete employee | Поиск не находит только что созданного employee (timing/search API) |

**22 @smoke тестов проходят полностью.** Все failures — @local destructive.

**Требуется:** `npx playwright test --headed` для визуальной инспекции.

---

## 6. Что НЕ изменилось

- **API v2 endpoints:** те же (`/api/v2/pim/employees`, `/api/v2/admin/users`, `/api/v2/auth/validate` и т.д.)
- **175 таблиц БД:** сохранены и промигрированы
- **Admin user:** id=1, user_role_id=1, status=1 — данные целы
- **bcrypt:** алгоритм хеширования не изменился
- **Login flow:** `input[name="username"]` + `input[name="password"]` + `button[type="submit"]` те же селекторы
- **Dashboard:** `.oxd-topbar-header-title` с "Dashboard" — без изменений

---

## 7. Инфраструктура

- **Backup:** `/tmp/orangehrm-5.4-backup.sql` (1,083,396 bytes)
- **Docker-compose:** `OrangeHRM/outputs/local-deployment.yml`
- **Container:** `orangehrm/orangehrm:5.8.1`
- **PHP:** 8.3.30 (Debian)
- **Apache:** 2.4.66 (Debian)
- **Docker path:** `/usr/local/bin/docker` (не в default PATH на Mac)
- **PATH fix:** `export PATH="/usr/local/bin:$PATH"` перед node/npm/docker командами

---

## Материал для статьи

**Потенциальные углы:**
1. **"Downtime-free upgrade"** — миграция БД без потери данных на live demo
2. **"5 проблем за 1 час"** — Docker, llhttp, installer redirect, пароль, тесты
3. **"Что сломалось между 5.4 и 5.8.1"** — selector changes, API стабильность
4. **"Local dev vs demo: upgrade реальный"** — опыт переезда на новую версию

# Сравнительное тестирование: OpenCode vs Claude Code

## Контекст

После 40+ рабочих сессий с OpenCode (Free → Go $10/mo) возник вопрос: насколько Claude Code (Anthropic) эффективнее/удобнее для наших типовых задач?

Нужен **объективный замер** — не субъективные ощущения, а SMART-критерии на одинаковых задачах.

## Принципы эксперимента

1. **Одна тест-база** — задачи из нашей реальной работы (OrangeHRM, qa-automation-sandbox)
2. **Одинаковый промпт** — дословно тот же текст задачи, те же входные данные
3. **Одинаковое начальное состояние** — git commit hash, чистый AGENTS.md контекст
4. **Измеримые метрики** — время, проход/падение, количество ошибок, правки человека
5. **Слепое ревью** — результат без указания агента → оценка человеком

## Типовые задачи для сравнения

### T1: POM-рефакторинг (10-15 мин)
**Что делает:** Дать spec c page.goto() и page.fill(), потребовать переписать через POM.

**Промпт:**
```
Refactor e2e/auth.spec.ts to use LoginPage from pom/LoginPage.ts.
The LoginPage already has login(email, password) and goto() methods.
Replace all raw page.fill() and page.click() calls with these methods.
Maintain all existing test structure and assertions.
```

**Метрики:**
- Время выполнения
- Все ли вызовы заменены (0 raw selector'ов)
- Assertions сохранены
- typecheck проходит

### T2: Code Review (10-15 мин)
**Что делает:** Дать spec с типичными ошибками (waitForTimeout, слабые assertions, page:any).

**Промпт:**
```
Review pom/PimPage.ts and e2e/pim.spec.ts for code quality issues based on AGENTS.md conventions.
Find: flake patterns (waitForTimeout), weak assertions (toBeVisible instead of toHaveCount), missing error handling.
Return a numbered list of issues with file:line references.
```

**Метрики:**
- Количество найденных проблем (из 8 заложенных)
- False positives (указал проблему которой нет)
- Время

### T3: Bug investigation (15-20 мин)
**Что делает:** Дать лог падающего теста, потребовать найти root cause и исправить.

**Промпт:**
```
The test "can view employee details @smoke" in e2e/pim.spec.ts is flaky on shared demo.
Run log: [playwright error + screenshot path attached]
Find the root cause and fix it. Explain why the fix works.
```

**Метрики:**
- Root cause найден (Y/N)
- Фикс проходит (Y/N)
- Времени меньше/больше чем у другого агента

### T4: Многофайловая задача (20-30 мин)
**Что делает:** Добавить новый модуль: POM + spec + fixture + test case doc.

**Промпт:**
```
Add test coverage for OrangeHRM Maintenance module:
1. Create pom/MaintenancePage.ts with goto() and accessMaintenance(password) 
2. Create e2e/maintenance.spec.ts with 2 tests: @smoke load, @local full access
3. Register page in helpers/fixtures.ts
4. Update TEST_CASES.md: add MAINT-001 and MAINT-002
```

**Метрики:**
- Все 4 файла созданы (Y/N)
- typecheck + lint pass
- Тест проходит хотя бы на LOCAL
- Количество попыток до правильного результата
- Hallucinations (придуманные API, неверные селекторы)

### T5: Документация (10 мин)
**Что делает:** Синхронизировать TEST_CASES.md с реальными тестами.

**Промпт:**
```
Read all .spec.ts files in e2e/ and update TEST_CASES.md:
- Mark implemented tests as ✅
- Add missing test IDs
- Update coverage percentage
Output: updated TEST_CASES.md diff
```

**Метрики:**
- Coverage % совпадает с реальностью
- Пропущенные/лишние тесты
- Время

## Протокол выполнения

### Шаг 1: Подготовка тест-стенда
```bash
git checkout -b test/agent-benchmark-$(date +%Y%m%d)
git commit --allow-empty -m "chore: benchmark starting point"
```

### Шаг 2: Выполнение серии (поочерёдно)
```
Session A: OpenCode Go (текущий, gpt-4o-mini)
Session B: Claude Code (Claude 4 Sonnet, API, --max-request-budget $5)
```

Для каждой задачи:
1. Записать `time_start` и состояние репозитория
2. Запустить с точно тем же промптом
3. Записать `time_end`, git diff, exit code
4. Запустить typecheck + lint
5. Запустить тест (если применимо)

### Шаг 3: Оценка результатов
```
Файл: outputs/agent-comparison/round-1.md
Таблица для каждой задачи:

| Metric | OpenCode Go | Claude Code |
|--------|-------------|-------------|
| Time | 45s | 32s |
| Passes typecheck | ✅ | ✅ |
| Passes test | ✅ | ❌ (flaky) |
| User corrections | 0 | 2 |
| Hallucinations | 0 | 1 |
| Accept as-is? | ✅ | ❌ |
```

### Шаг 4: Слепое ревью
1. Убрать идентификатор агента из результатов
2. Показать человеку 2 варианта
3. Оценить: какой чище, какой понятнее, какой приняли бы в PR

## Контроль переменных

| Переменная | OpenCode | Claude Code |
|------------|----------|-------------|
| Модель | gpt-4o-mini (Go) | Claude 4 Sonnet (API) |
| Контекст | 128K | 200K |
| Температура | 0 (по умолч.) | 0 (по умолч.) |
| AGENTS.md | читает | читает (через CLAUDE.md symlink) |
| session-checkpoint | читает | не читает — нужно руками |

## Ограничения эксперимента

1. **Нельзя ослепить от модели** — код gpt-4o-mini и Claude 4 Sonnet выглядят по-разному (стиль импортов, комментарии)
2. **OpenCode опытнее** — 40+ сессий на OpenCode значит лучшие prompt'ы для него
3. **Разный бюджет** — OpenCode Go $10 flat, Claude API тянет $2-5 за тест
4. **Неизвестная модель** — Sonnet 4 может быть сильнее всех протестированных
5. **Сессия ≠ изолированный контекст** — даже при одинаковом старте предыдущие шаги влияют на контекст

## Чек-лист перед запуском

- [ ] Установлен Claude Code (`pip install claude-code` или `brew install claude-code`)
- [ ] API ключ Anthropic с балансом > $10
- [ ] `--max-request-budget $5` для каждой сессии
- [ ] CLAUDE.md symlink → AGENTS.md
- [ ] Git commit для стартовой точки
- [ ] Запись времени + screen capture (опционально)
- [ ] После теста: `git checkout main && git branch -D test/agent-benchmark-*`

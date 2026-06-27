# Сравнительное тестирование агентов (benchmark)

## Зачем

После 40+ сессий с OpenCode (Free → Go $10/mo) нужно объективно сравнить его с Claude Code. Не субъективно, а по SMART-критериям на одинаковых задачах.

## Принципы

1. Одна тест-база — задачи из реальной работы (OrangeHRM, qa-automation-sandbox)
2. Одинаковый промпт — дословно тот же текст, те же входные данные
3. Одинаковое начальное состояние — git commit hash, чистый контекст
4. Измеримые метрики — время, pass/fail, ошибки, правки человека
5. Слепое ревью — результат без указания агента → оценка человеком

## Тестовые задачи

### T1: POM-рефакторинг (10-15 мин)
Refactor spec to use existing POM methods. Заменить все raw page.fill/page.click на POM-вызовы.

**Метрики:** время, 0 raw selector'ов, assertions сохранены, typecheck

### T2: Code Review (10-15 мин)
Найти 8 заложенных проблем: waitForTimeout, слабые assertions, page:any, flake patterns.

**Метрики:** найдено из 8, false positives, время

### T3: Bug Investigation (15-20 мин)
Дать лог падающего теста, найти root cause, исправить, объяснить.

**Метрики:** root cause найден (Y/N), фикс проходит (Y/N)

### T4: Многофайловая задача (20-30 мин)
Добавить модуль: POM + spec + fixture + TEST_CASES.md — 4 файла.

**Метрики:** все файлы созданы, typecheck+lint, тест проходит, попытки до успеха, hallucinations

### T5: Документация (10 мин)
Синхронизировать TEST_CASES.md с реальными тестами.

**Метрики:** coverage совпадает, пропуски, время

## Протокол

1. `git checkout -b test/agent-benchmark-$(date +%Y%m%d)` — стартовая точка
2. Session A: OpenCode Go (gpt-4o-mini), Session B: Claude Code (Sonnet 4, `--max-request-budget $5`)
3. Для каждой задачи: time_start → промпт → time_end → git diff → typecheck → lint → test
4. Результаты: единая таблица

## Контроль переменных

| Переменная | OpenCode Go | Claude Code |
|------------|-------------|-------------|
| Модель | gpt-4o-mini | Claude 4 Sonnet |
| Контекст | 128K | 200K |
| Температура | 0 | 0 |
| AGENTS.md | читает | читает (CLAUDE.md symlink) |
| session-checkpoint | читает | не читает (руками) |

## Ограничения

- **Нельзя ослепить** — код моделей выглядит по-разному
- **OpenCode опытнее** — 40+ сессий промпты лучше для него
- **Разный бюджет** — OpenCode $10 flat, Claude $2-5/тест
- **Сессия ≠ изолированный контекст** — предыдущие шаги влияют

## Чек-лист перед запуском

- [ ] Claude Code установлен
- [ ] API ключ Anthropic с балансом > $10
- [ ] `--max-request-budget $5`
- [ ] CLAUDE.md symlink → AGENTS.md
- [ ] Git commit для стартовой точки
- [ ] `outputs/agent-comparison/round-1.md` для результатов

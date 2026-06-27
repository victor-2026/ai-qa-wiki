# Hack'n'Vibe — BitGN PAC1 Agent

## Raw Post
Слепой прогон pac1-prod (~104 задачи). 3 место Accuracy Leaderboard, 5 место Ultimate. Бенчмарк Рината Абдуллина (LLM под капотом) — BitGN.

## Архитектура агента

**Ключевое решение:** Не чат-бот с LLM-циклом, а **тонкий транспорт + Claude Code как мозг**. Нет ключей OpenAI/Anthropic в коде — Claude Code CLI и есть LLM-петля.

### Компоненты

**runner.py** — голый Python, только RPC к harness и PCM runtime:
- 11 VM-нативных операций: tree, find, search, read, write, delete, mkdir, move, context, answer
- 1:1 маппинг на gRPC-вызовы
- Нет Python-sandbox внутри VM, нет посредника
- Операции — JSON-команды

**RULES.md** — паттерн-словарь (итеративно накопленный):
- 9 stop-rules
- 13 паттернов задач: CRM ops, knowledge repo, prompt injection, date math, lookups
- Подгружается перед каждой задачей
- Механизм `learn "..."`: агент сам дописывает правило после ошибки

**Skill-оркестратор** — `/solve-pac1` для Claude Code:
- Раздаёт trial_ids батчами по 10 субагентам
- Параллельный запуск в одном сообщении
- Все ~104 задачи решаются одновременно
- Каждый субагент получает свежий RULES.md
- На blind prod retry бесполезен — один точный прогон

**Цикл:** простой и плоский:
1. `recon` (tree глубины 3 + read всех файлов) → Claude видит весь vault
2. Доп. `exec` если нужны точные числа (recon truncate-ит большие файлы)
3. `submit` с answer + refs + outcome

### Слабые места
1. Даты от `context.time` (агент брал дату из файла, а не из контекста trial)
2. Counting через `recon` (truncate → 1 вместо 810)
3. Manager lookup без сканирования всех acct_*.json
4. Конфликт инструкций в двух документах — Claude выбирает, а надо CLARIFICATION

Все 4 грабли — в RULES.md stop-листе.

### Принципы (чтобы повторить)
1. Простой набор инструментов вместо одного execute_code
2. Растущий чеклист правил, переиспользуемый между прогонами
3. Параллелизм через субагентов
4. Чистая разводка: Python только транспорт, LLM — все решения

## Relevance

Прямое попадание в наш контекст:
- **RULES.md** = аналог `AGENTS.md` + `learned_patterns.json` из MAS
- **Parallel subagents** = batch execution (как мы делаем с Task tool)
- **Thin transport** = separation of concerns (Python ≠ LLM decisions)
- **Stop-rules** = anti-patterns / что НЕ делать
- **Mechanism design** (agent behavior) vs prompt engineering

## Source
Telegram: @hack_n_vibe

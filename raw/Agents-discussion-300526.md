=== Big Pickle
* Отличная статья. Сравнение с нашим текущим подходом:  
* Что уже есть (совпадает):  
* Global memory \= SESSION\_NOTES \+ checkpoint ✓  
* Правила для агентов через skills/ ✓  
* raw/ не модифицируется \= граница (boundary) ✓  
* Что можно добавить:

| Что | У нас | Нужно? |
| :---- | :---- | :---- |
| AGENTS.md в корне проектов | Нет | Да — для qa-automation-playwright и ai-qa-wiki |
| Таблица Boundaries (edit/ask/never) | Неформально (в памяти) | Да — формализовать |
| SESSION\_NOTES.md per-project | Только глобальная | Необязательно |
| Кросс-вендорность | OpenCode-специфичный формат | Если будешь использовать Cursor/Codex — нужен AGENTS.md |

Главный инсайт: AGENTS.md — это кросс-вендорный стандарт (поддерживается Codex, Cursor, Copilot, Zed). Если ты перейдёшь на другой инструмент, наш формат (memory \+ skills) не перенесётся. AGENTS.md в корне проекта — перенесётся.  

========  MiMo
Сравнение: статья vs наш проект  
Что у нас уже есть ✅

| Рекомендация из статьи | Наш статус |
| :---- | :---- |
| Project overview (что это, стек) | ✅ Есть |
| Setup (команды старта) | ✅ docker-compose up, npm test |
| Common commands (build, test, lint) | ✅ Есть |
| Testing (команды и паттерны) | ✅ Есть (runbook) |
| PR guidelines (формат коммитов) | ✅ feat:, fix:, docs: |
| Session checkpoint | ✅ session-checkpoint.md |
| E2E test rules (selector reuse, spec structure) | ✅ Добавлено сегодня |
| Self-review rule | ✅ Есть |
| End-of-session report | ✅ Есть |

Что НЕТ и стоит добавить ❌

| Рекомендация | Описание | Приоритет |
| :---- | :---- | :---- |
| Boundaries таблица | yes edit / ask / never — какие файлы можно трогать, а какие нельзя | High |
| Architecture карта | Карта директорий с описанием назначения | Medium |
| Code conventions | Именование, экспорты, фреймворки | Medium |
| Review guidelines | Рубрика для автоматического ревью PR | Low |
| CLAUDE.md симлинк | ln \-s AGENTS.md CLAUDE.md для кросс-вендорной совместимости | Low |
| SESSION\_NOTES.md | Отдельный файл для свежих событий (у нас session-checkpoint.md совмещает обе роли) | Medium |
| Размер ≤ 32 KiB | Наш AGENTS.md \~2.5 KiB — ок | ✅ |
| Датированные факты | У нас нет dated facts — ок | ✅ |
| Нет секретов | У нас нет секретов — ок | ✅ |

Что нужно добавить  
План: что добавить в AGENTS.md

| \# | Секция | Описание | Строк |
| :---- | :---- | :---- | :---- |
| 1 | Boundaries | Таблица yes edit / ask / never — какие файлы можно трогать | \~15 |
| 2 | Architecture | Карта директорий с назначением | \~20 |
| 3 | Code conventions | Именование, экспорты, паттерны | \~10 |
| 4 | CLAUDE.md симлинк | Кросс-вендорная совместимость | \~2 |
| 5 | SESSION\_NOTES | Отдельный файл или интеграция в checkpoint | \~5 |

Итого: \~50 строк к существующим 126\. Файл останется ≤ 32 KiB.  
\======  Nemotron
 Ваш AGENTS.md содержит хорошую основу, но можно улучшить согласно стандарту из статьи:

* Что у вас есть правильно:  
* ✅ Структура проекта с описанием директорий  
* ✅ Основные принципы (принципы Karpathy LLM Wiki)  
* ✅ Договорённости (сессии, GitHub, GitHub Pages, Wiki страницы)  
* ✅ Скрипты интеграции (wiki\_llm.py, dora\_charts.py, vision\_test.py)  
* ✅ Упоминание session-checkpoint.md  
* Что можно добавить/улучшить:  
* Структурировать по рекомендуемому каркасу:  
  * Добавить четкие секции: \#\# Setup (команды для быстрого старта), \#\# Common commands (build/dev/test/lint), \#\# Architecture, \#\# Code conventions, \#\# Boundaries (таблица yes/ask/never), \#\# Testing, \#\# PR guidelines, \#\# Review guidelines  
* Добавить SESSION\_NOTES.md:  
  * Создать отдельный файл для фиксации того, что сделано в каждой сессии (измененные файлы, принятые решения, следующие шаги)  
  * Как указано в статье: "Новый заход читает хвост SESSION\_NOTES и продолжает работу без повторной раскачки"  
* Улучшить секцию Boundaries:  
  * Сделать в виде таблицы "Можно / Спросить / Нельзя" как в примере статьи  
  * Например:| Область | Можно | Спросить | Нельзя |  
  * | wiki/pages/ | ✅ edit | | |  
  * | raw/sources/ | | ✅ ask | |  
  * | .env\* | | | ❌ never |

* Проверить на антипаттерны из статьи:  
  * Убедиться, что нет инструкций для конкретной модели  
  * Нет секретов/переменных окружения  
  * Нет датированных фактов  
  * Нет больших архитектурных обзоров (агент должен исследовать код сам)  
  * Нет личных предпочтений под видом правил  
  * Нет конфигурации инструментов (для этого есть конфиг-файлы)  
  * Нет role-play преамбул  
* Рассмотреть использование чекпоинтов для больших рабочих потоков:  
  * Как упоминается в статье: "Для крупных рабочих контуров SESSION\_NOTES недостаточно. Checkpoint — отдельная страница, содержащая: где лежит код и как запускать; что сделано в каждой версии; какие API доступны; что выяснили на практике; что нельзя делать без approval; следующий шаг."  
* Добавить символическую ссылку для Claude Code (если используете):  
  * ln \-s AGENTS.md CLAUDE.md в корне репозитория  
* Ваш текущий файл больше похож на комбинированный AGENTS.md \+ внутреннюю документацию проекта. Для оптимальной работы с AI-агентами рекомендуется разделить preocupations согласно стандарту, оставив в AGENTS.md только то, что нужно агенту для продуктивной работы с первых секунд.

\======  DeepDeek
Всё прочитал. Вот сравнение:  
Что у нас есть

| Элемент | Статья | У нас |
| :---- | :---- | :---- |
| AGENTS.md в корне | ✅ | ✅ qa-automation-sandbox |
| Project overview | ✅ | ✅ |
| Common commands | ✅ | ✅ (Runbook) |
| Core rules | ✅ | ✅ |
| Session notes/checkpoint | ✅ | ✅ session-checkpoint.md |
| Next steps in checkpoint | ✅ | ✅ |

Чего не хватает

| Элемент | Статья | Статус |
| :---- | :---- | :---- |
| Boundaries table (yes edit / ask / never) | "Наибольший вклад в соблюдение границ" | ❌ Нет нигде |
| Архитектурная карта директорий | e2e/, backend/, frontend/ | ❌ Нет |
| PR guidelines | формат коммитов \+ модель веток | ❌ Частично (только префиксы) |
| Review guidelines | рубрика для авто-ревью | ❌ Нет |
| AGENTS.md в др. проектах | вложенные AGENTS.md | ❌ В Positions-CV-CL и ai-qa-wiki нет |
| Symlink CLAUDE.md → AGENTS.md | кросс-совместимость | ❌ Нет |
| Чистый SESSION\_NOTES.md | отдельный файл от checkpoint | ❌ У нас гибрид session-checkpoint.md |
| Элемент | Статья | Статус |

Что можно  
Вот что предлагаю, по приоритету:  
1\. Boundaries table — самая полезная штука Добавить в AGENTS.md qa-automation-sandbox:  
| Область | Можно | Спросить | Нельзя |  
|---|---|---|---|  
| e2e/\*.spec.ts | ✅ edit | | |  
| e2e/pages/\*.ts | ✅ edit | | |  
| e2e/fixtures.ts | | ✅ ask | |  
| backend/ | | | ❌ never |  
| frontend/ | | | ❌ never |  
| render.yaml, CI/\* | | ✅ ask | |  
| session-checkpoint.md | ✅ edit | | |  
| AGENTS.md | | ✅ ask | |  
| .env\*, secrets | | | ❌ never |  
2\. Symlink ln \-s AGENTS.md CLAUDE.md в корне qa-automation-sandbox  
3\. Minimal AGENTS.md для Positions-CV-CL — 3 секции: overview, структура (raw/, wiki/, outputs/), правило "raw \= source only, wiki \= AI output"  
4\. Architecture map в AGENTS.md — 3 строки: e2e/ (Playwright), backend/ (FastAPI), frontend/ (React)  
5\. Review guidelines — добавить чеклист: "проверил типы → прогонил тесты → обновил checkpoint"  

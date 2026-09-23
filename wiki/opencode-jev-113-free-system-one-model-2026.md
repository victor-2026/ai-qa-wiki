---
source: "user-notes (2026-09-21)"
ingested: "2026-09-21"
---

## OpenCode/jev-1.13-free — Jev (TypeSafe AI) как System One модель

**Контекст:** OpenCode/jev-1.13-free — модель Jev от TypeSafe AI. Это НЕ обычная LLM для генерации текста или кода. Это « System One » модель для мгновенных структурированных решений. Не пишет ответы словами — возвращает типизированные данные (True/False, числа, категории) на конкретный вопрос.

---

### Сценарии использования

#### 1. Роутинг задач (Routing) — самый популярный сценарий
Jev выступает диспетчером: быстро и дешево решает, какую более мощную (и дорогую) модель вызвать.
- Пример: запрос пользователя → Jev классифицирует: `["frontend", "backend", "database", "devops"]`.
- Результат: "frontend" → OpenCode вызывает специализированную модель для JS/CSS; "database" → модель для SQL. Дорогие токены GPT-4o на классификацию не тратятся.

#### 2. «Семантические IF-операторы» (Semantic If-Statements)
Jev там, где в коде нужно решение по нечетким данным (текст), но четкий программный ответ (bool/enum).
- Сценарий: лог ошибок из 10 000 строк; задача: «Это критическая ошибка безопасности?» (Да/Нет).
- Почему Jev: читает лог и возвращает true/false за миллисекунды. Обычная LLM начала бы «Анализируя лог, я могу сказать...» — медленно и сложно парсится.

#### 3. Быстрая фильтрация данных (High-Volume Filtering)
Скорость (~250 мс) + free-версия → циклы с тысячами элементов.
- Пример: проверить 500 файлов, найти где используется устаревшая библиотека.
- Команда: «Содержит ли этот файл старый API?» → Jev возвращает список путей.

#### 4. Проверка состояния (State Checking) для агентов
Автономный агент в OpenCode проверяет, выполнена ли задача, не отвлекаясь на разговоры.
- Вопрос: «Решена ли проблема пользователя на основе последних изменений?»
- Ответ: оценка уверенности 0.0–1.0 (например, 0.95). Агент видит число и завершает работу.

---

### Сводная таблица отличий

| Характеристика | Обычная LLM (GPT-4, Claude) | Jev-1.13 (System One) |
|---|---|---|
| Выходные данные | Текст, код, объяснения | Boolean, Числа, Enum (Выбор) |
| Скорость | Секунды (медленно) | Миллисекунды (очень быстро) |
| Стоимость | Дорого (за генерацию) | Бесплатно (до 25.09.26) / Дешево |
| Главная роль | Исполнитель (Writer/Coder) | Решатель (Decision Maker) |

---

### Важно про суффикс -free
Свободный доступ — временная акция (обычно через Vercel AI Gateway или OpenCode Zen), действует до 25 сентября 2026 года. После этой даты модель станет платной или потребует API-ключ TypeSafe, но останется крайне дешевой для задач классификации по сравнению с большими моделями.

---

### Relevance
- **Связка с mutation-подходом:** Jev-вердикты + probabilities = готовый объект для mutation-проверки (сидять ли вердикты Jev на известных мутациях, как QAEverest sensitivity runs) — см. jev-jason-arbon-playwright-bounded-exploration.
- **Архитектурно** = наш детерминированный гейт + judgment-on-demand: «code controls workflow, Jev supplies judgment» (типы: choice/score/bool — те же примитивы, что в typesafe-jev-judgment-service-gates-2026).
- **Token-экономика:** платная классификация ~20–200x дешевле frontier (в копилку Osmani/антропного $80-дня аргумента).
- **Deadline 25.09.2026** — free-окно; по истечении сохранится «крайне дешевая» классификация. Полезно зафиксировать как временной факт, не как постоянное свойство.

---

### See also
- [Jason Arbon: Jev в Playwright-цикле (bounded adaptive exploration)](wiki/jev-jason-arbon-playwright-bounded-exploration.md)
- [TypeSafe Jev — judgment-as-service for gates (Paluy, Sharpe, Watsche hands-on)](wiki/typesafe-jev-judgment-service-gates-2026.md)
- [Jev: Proprietary Beaten by Open-Source? (Charly Wargnier)](wiki/jev-openai-proprietary-beaten-open-source-2026.md)
- [Ruben Hassid – Jev “Internet moment” (2026-09-21)](wiki/ruben-hassid-jev-internet-moment-setup-2026.md)













<!-- backlinks-start -->
### Backlinks
- [Jason Arbon: Jev в Playwright-браузере (2026-09)](wiki/jev-jason-arbon-playwright-bounded-exploration.md)
- [Jev Openai Proprietary Beaten Open Source 2026](wiki/jev-openai-proprietary-beaten-open-source-2026.md)
- [Ruben Hassid Jev Internet Moment Setup 2026](wiki/ruben-hassid-jev-internet-moment-setup-2026.md)
- [Typesafe Jev Judgment Service Gates 2026](wiki/typesafe-jev-judgment-service-gates-2026.md)
- [Jev Open Source Alternatives 2026](wiki/jev-open-source-alternatives-2026.md)
<!-- backlinks-end -->

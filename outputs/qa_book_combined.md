# Q&A — Software Testing with Generative AI
*198 вопросов (18 × 11 глав)*

---


## Prompt Engineering

# Как работают LLMs объясни на примере клавиатуры с техническими деталями.

---

LLM предсказывает следующий токен на основе probability distribution, учитывая весь контекст запроса (Context Window). В отличие от клавиатуры с n-граммами, LLM использует Attention Mechanism — «смотрит» на все предыдущие токены, чтобы понять их взаимосвязь. Токены — это не целые слова, а части слов (subword tokenization).



# Что такое hallucination и какие типы бывают?

---

Hallucination — уверенный, но ложный вывод. Два типа: 1) Factuality — ложь о мире («книга Джулиан Хартли»); 2) Instructional — нарушение логики промпта. В 2026 добавляют «Model Drift» — дрейф модели при перегрузке контекста.



# Почему не стоит антропоморфизировать LLMs?

---

LLM — это Stochastic Parrot (стохастический попугай). Модель минимизирует loss function при предсказании токена, а не «хочет» помочь. Она имитирует структуру языка, но не «знает» истинность.



# Разница supervised vs unsupervised learning в контексте LLM.

---

Современные LLM используют: 1) Self-supervised — обучение на массивах текста без разметки; 2) RLHF — Reinforcement Learning from Human Feedback (обучение с подкреплением на основе человеческих оценок).



# Пример слабого и сильного prompt с форматом вывода.

---

Слабый: «Создай тесты». Сильный: «Роль: Senior Test Engineer. Формат: Markdown таблица. Колонки: ID, Приоритет, Входные данные, Ожидаемый результат. Сгенерируй 10 тест-кейсов для функции загрузки файла.»



# Как работает delimiter tactic?

---

Delimiter (разделитель) — специальные символы (#, %, |) для разделения частей запроса. Пример: «Act as tester. # Focus on Functionality, Security # Generate test ideas».



# Что такое few-shot prompting?

---

Few-shot — техника с примерами в промпте. Даешь 2-3 примера «вопрос → ответ», и LLM понимает паттерн. Эффективно для структурированного вывода.



# Что такое time-to-think техника в 2026 году?

---

Chain of Thought Explicit Request. Фраза: «Let's think step by step» («Давай подумаем пошагово»). Заставляет модель использовать больше вычислительных ресурсов на логические переходы.



# Что такое zero-shot prompting и пример?

---

Zero-shot — техника без примеров в промпте. Пример: «Напиши стихотворение о летней ночи» — модель сама генерирует без исходных данных.



# Что такое chain-of-thought prompting и tree of thoughts?

---

CoT — «думай пошагово». Tree of Thoughts (ToT) — модель генерирует несколько путей рассуждения, сравнивает и выбирает лучший. Критично для тестирования логики.



# Как избежать prompt injection в 2026 году?

---

Методы защиты: 1) LLM-based Firewall; 2) System Message с высоким приоритетом; 3) Input sanitization. Валидация почти не работает против Jailbreaking.



# Какие есть common prompt errors?

---

Ошибки: 1) Generic prompts без контекста; 2) Missing output format; 3) Неправильная роль; 4) Слишком много требований сразу. Решение: SFDIPOT + структура.



# Что такое Context Window и почему это важно для тестирования?

---

Context Window — объем данных, который модель «видит» одновременно. В 2026: 128K-1M токенов. Важно для больших репозиториев: используй Chunking или RAG.



# Что такое Temperature и как использовать для тестов?

---

Temperature — параметр случайности (0.0-2.0). Для тестов: 0.0 = детерминизм. Для идей: 0.7-0.9 = креативность. Одинаковый промпт + разная temperature = разные результаты.



# Что такое Grounding и как избежать hallucinations?

---

Grounding — привязка ответа к фактам через RAG или базу знаний. Без Grounding модель «галлюцинирует». Используй Retrieval-Augmented Generation.



# Что такое Oracle Problem в AI-тестировании?

---

Oracle Problem — как понять, что AI выдал верный ответ, если нет эталона? Решения: 1) Agent-Critic; 2) Cross-checking; 3) Statistical threshold.



# Пример Золотого промпта для Prompt Engineering?

---

Golden Prompt: **Role**: Senior QA. **Context**: [код/фича]. **Task**: Проанализируй риски через SFDIPOT. **Output**: Markdown таблица. Пример: «Проанализируй функцию login через SFDIPOT».



# Итоговая таблица: Prompt Engineering 2026?

---

| Техника | Применение | Эффект |
|---|---|---|
| Zero-shot | Без примеров | Быстрый старт |
| Few-shot | 2-3 примера | Точный формат |
| CoT | Пошагово | Сложная логика |
| SFDIPOT | 7 измерений | Полное покрытие |

**Ключ**: Человек = вектор, AI = масштаб.




## AI Automation Testing

# Что такое AI-augmented testing?

---

AI-augmented = AI помогает, не заменяет. AI генерирует данные, идеи, код. Человек принимает решения. Симбиоз: AI = ускорение, Human = контекст + риски.



# Уровни AI в тестировании (Levels 2026)?

---

Teslafication levels: L2 'Hands on, eyes on' — вы проверяете каждую строку; L3 'Hands off, eyes on' — агент делает, вы проверяете отчет; L4 'Hands off, eyes off' — ИИ сам решает что тестировать по бизнес-метрикам.



# Какие задачи AI делает лучше человека?

---

1) Генерация тестовых данных; 2) Поиск edge cases; 3) Генерация boilerplate кода; 4) Анализ логов; 5) Создание документации. Человек: контекст, интуиция, решения.



# Какие задачи человек делает лучше AI?

---

1) Понимание бизнес-контекста; 2) Критическое мышление; 3) Тестирование UX; 4) Принятие решений о рисках; 5) Коммуникация с командой.



# Как AI изменил роль QA?

---

QA → Quality AI Engineer. Новая роль: Curating Gold Datasets — собирать 'золотые наборы' для обучения агентов. Плохие данные = бесполезное тестирование. Human = decisions + quality gate.



# Что такое AI test assistant?

---

AI test assistant = LLM, интегрированный в IDE/CI. Может: 1) Предлагать тесты; 2) Генерировать fixtures; 3) Анализировать failures; 4) Документировать.



# Пример AI assistant в workflow?

---

Developer пишет код → AI assistant предлагает тесты → Developer approve → AI генерирует код → Run → AI анализирует failure → AI предлагает fix.



# Как выбрать AI tool для QA?

---

Criteria: 1) Stack integration; 2) Quality; 3) Cost; 4) Security. Popular: Cursor, Codium, Copilot.



# Что такое code coverage AI?

---

LCOV = строки. Semantic Coverage = логический смысл. AI видит: 100% строк, но не протестирован 'отрицательный баланс'. AI подсветит логическую дыру.



# AI для test maintenance?

---

AI: 1) Detect stale tests; 2) Suggest updates; 3) Auto-heal selectors; 4) Identify flakiness.



# Что такое intelligent test selection?

---

TIA = Test Impact Analysis. AI анализирует не только code, но и метаданные: кто коммиттил (история багов), время, критичность для бизнеса. Smart selection.



# Как AI помогает с test debt?

---

AI может: 1) Анализировать что устарело; 2) Prioritize что рефакторить; 3) Генерировать missing tests; 4) Suggest simplifications. Test debt = накопленный technical debt.



# Пример AI для regression testing?

---

AI анализирует PR → определяет affected areas → запускает relevant tests only → если fail → AI предлагает fix. Это 80/20 rule: 20% tests = 80% coverage.



# Что такое AI-driven test strategy?

---

AI в стратегии: 1) AI анализирует requirements; 2) Оценивает risks; 3) Генерирует plan. Human = decisions.



# Как измерить AI effectiveness в QA?

---

Metrics: 1) Time saved; 2) Coverage improvement; 3) Bug detection; 4) Test stability; 5) Cost reduction.



# Риски AI в тестировании (Blind Trust Risk)?

---

Blind Trust Risk — главный риск 2026. ИИ повышает скорость, человек = ответственность за качество. MAS: Critic + HITL (Human validation) обязательны.



# Best practices AI testing?

---

1) Start small — pilot project; 2) Human in loop; 3) Continuous evaluation; 4) Quality over quantity; 5) Maintain human skills; 6) Document decisions.



# Итоговая таблица: QA vs AI Engineer?

---

## Эволюция ролей (2024 vs 2026)

| Функция | QA (2024) | Quality AI Engineer (2026) |
|:--- |:--- |:--- |
| Создание тестов | Ручной код | Дизайн промптов + оркестрация |
| Анализ падений | Логи в консоли | Валидация AI-анализа |
| Тест-данные | Фикстуры / Faker | Синтетика на проде |
| Поддержка | Ручной рефакторинг | Self-healing approval |

### Blind Trust Risk
Главный риск 2026: ИИ повышает скорость, человек = quality gate. Critic + HITL обязательны.



## TDD with AI

# Что такое TDD?

---

TDD = Test-Driven Development. 3 фазы: Red (fail) → Green (pass) → Refactor. Test-first. Красный → Зеленый → Рефактор.



# Как AI помогает в TDD?

---

AI ускоряет: 1) Генерирует тесты из requirements; 2) Code boilerplate; 3) Refactoring suggestions; 4) Code completion. AI не заменяет TDD cycle.



# AI-first vs TDD-first vs Agentic TDD?

---

Agentic TDD: ИИ генерирует тесты + код одновременно. TDD-first = тест до кода (золотой стандарт). AI-first = быстро, но риск Confirmation Bias (подгонка тестов под код). TDD-first надежнее.



# Пример TDD cycle с AI?

---

TDD + AI cycle: 1) Requirement → AI генерирует тесты; 2) Human review; 3) AI генерирует code; 4) Run; 5) AI suggests refactor. Короче cycle, фокус на решениях.



# Как AI генерирует unit tests (Context-Aware)?

---

Context-Aware Generation: AI анализирует не только функцию, но и смежные файлы, чтобы понять какие моки существуют. CodiumAI, Cursor предотвращают дублирование. AI видит project context.



# Что такое AI code review?

---

AI code review = статический анализ + AI. Предлагает: issues, security, performance, test coverage. Sonar, CodeRabbit.



# Как AI помогает с refactoring?

---

AI: 1) Suggest improvements; 2) Explain complex code; 3) Extract methods; 4) Suggest patterns.



# Пример AI для integration tests?

---

AI анализирует API docs → генерирует integration tests. Prompt: «Сгенерируй integration tests для /users endpoint: CRUD operations, auth, error cases».



# Specification-based testing (Specs-to-Code)?

---

Specs-to-Code: Генератор берет README.md или Swagger/OpenAPI → генерирует тесты. Это ключевой для MAS-пайплайна: спецификация → тесты → код.



# Как AI улучшает test coverage?

---

AI = semantic coverage, не line coverage. Понимает meaning, предлагает missing edge cases.



# TDD для AI-generated code?

---

Критично: когда AI пишет код, тесты = обязательство, не опция. Без тестов нельзя доверять чужому коду. AI TDD = 70% быстрее, но quality gate обязателен.



# Пример: AI + pytest workflow?

---

1) Describe function; 2) AI generates @pytest tests; 3) Run → AI sees failures; 4) AI fixes code; 5) Tests pass. Fast feedback loop.



# Что такое property-based testing с AI?

---

Property-based = AI генерирует random inputs, проверяет invariants. AI понимает meaning, smarter than random.



# AI для contract testing?

---

Contract = соглашение между сервисами. AI генерирует из spec → positive/negative tests.



# Как AI помогает с mocking?

---

AI creates mocks: from interfaces, stub responses, mock external APIs.



# Что такое mutation testing + AI?

---

Mutation = меняем code → tests должны fail. AI: 1) Generates better mutations; 2) Analyzes results.



# Что такое Agentic TDD?

---

## Agentic TDD (2026)

Agentic TDD = автономные агенты в цикле Red-Green-Refactor. Человек = автор спецификаций и судья.

### Процесс:
1. **Requirement** — опиши фичу
2. **Red** — Agent пишет падающие тесты
3. **Green** — Agent пишет код для прохождения тестов
4. **Refactor** — Agent-Critic проверяет качество

### Инструменты:
- AlphaCodium, Aider, OpenHands (OpenDevin)
- CrewAI для оркестрации

### Почему важно:
Agentic TDD решает "кто тестирует тесты". Агент-Критик проверяет агента-Генератора, Mutation Testing подтверждает что тесты "ловят" баги.

### Бизнес-выгода:
- Снижение стоимости ошибки
- 100% покрытие (Safety by Design)
- Автономный рефакторинг
- Прозрачность: requirement → test → code → verified


# Итоговая таблица: TDD vs AI-TDD?

---

## Эволюция TDD цикла

| Этап | Классический | TDD + AI | Эффект |
|:--- |:--- |:--- |:--- |
| Red | Ручной | AI пишет по идее | Секунды |
| Green | Ручной | AI генерирует | -70% рутины |
| Refactor | Ручной | AI предлагает паттерны | Качество |
| Verify | Локально | Agent в Docker | Надежность |

### AI сделал TDD "дешевым"
Раньше от TDD отказывались из-за времени. С AI: -70% времени → оправданий для отсутствия тестов нет.



## Test Planning

# Почему фокус на рисках важнее тест-кейсов?

---

Риски — инварианты, тест-кейсы — статичные слепки. В эпоху Vibe Coding код меняется быстрее обновления кейсов. При запросе рисков LLM включает Chain-of-Thought, давая более глубокий результат.



# Как weak prompts влияют на качество?

---

Weak prompts слишком абстрактные («протестируй форму»), без конкретики. AI генерирует generic тесты. Решение: добавь SFDIPOT, модель данных, ограничения.



# Какие типы моделей можно использовать?

---

Модели: 1) Data Model — структура данных; 2) Flow Model — потоки; 3) Component Model — компоненты; 4) State Model — состояния. Помогают AI понять контекст.



# Пример prompt с моделью данных (сильный)?

---

Сильный пример: «Роль: QA Engineer. Используй Data Model: User {id: UUID, role: Enum[ADMIN,GUEST], last_login: Timestamp}. Сгенерируйnegative сценарии для delete_report, учитывая риск IDOR».



# Что такое SFDIPOT и как применять с LLM?

---

SFDIPOT — мнемоника Джейса Баха (Rapid Software Testing). Применение с LLM: используй как System Prompt — «Используй эвристику SFDIPOT для анализа микросервиса».



# Как создавать модели для тестирования?

---

Создание модели: 1) Выбери тип (Data/Flow/Component/State); 2) Определи элементы; 3) Используй в prompt. Пример: Flow Model = последовательность действий.



# Как Area of Effect model работает?

---

AoE критична для MAS-пайплайнов. Человек бросает «камень» (риск), LLM создает «волны» (вариации). Профит: 5 минут → 50 проверок за 10 секунд.



# Разница между test cases и risks?

---

Test Cases — конкретные шаги. Risks — что может сломаться. Test Cases отвечают «как проверить», Risks — «что критично». Приоритизация по рискам > generic coverage.



# Как приоритизировать риски?

---

Приоритизация: 1) Impact × Likelihood = Risk Score; 2) Критичные бизнес-процессы; 3) Недавно измененный код; 4) Сложные компоненты. High Risk = тестировать первым.



# Что такое Risk-Based Testing Matrix с AI?

---

RBT Matrix = Impact × Likelihood. В AI дополняется параметром AI Confidence. Приоритизируем там, где LLM выявил наибольшую неопределенность в коде.



# Как определить тестовую стратегию с LLM?

---

Стратегия: 1) Определи контекст (SFDIPOT); 2) Сгенерируй риски через LLM; 3) Приоритизируй; 4) Сгенерируй тест-кейсы. LLM = ускорение, человеческий контроль обязателен.



# Как измерить эффективность тестов?

---

Метрики: 1) Risk Coverage; 2) Defect Detection Rate; 3) Pass Rate. Важно: не только coverage, но и качество обнаружения.



# Что такое Non-determinism в AI-тестировании?

---

Non-determinism — один промпт может дать разные результаты при разной temperature. Главный риск автоматизации. Решение: фиксируй temperature=0.0 для тестов.



# Что такое Model Decay и как тестировать?

---

Model Decay (Data Drift) — модель «глупеет» после обновлений. Тестирование: 1) Регрессионные тесты с эталонными промптами; 2) Сравнение ответов «до/после».



# Как использовать LLM для regression testing?

---

LLM для регрессии: 1) Создай baseline prompts с expected outputs; 2) После обновления запусти те же промпты; 3) Сравнивай ответы. Важно: зафиксируй model, temperature.



# Как выбрать тестовый фреймворк для AI-тестирования?

---

Выбор: 1) Поддержка LLM API; 2) Асинхронные вызовы; 3) Assertions для AI (semantic vs exact); 4) Интеграция с RAG. Popular: Playwright+Pydantic, Jest, pytest.



# Что такое Золотой промпт для тестовой стратегии?

---

Golden Prompt: Role=Senior Test Architect → SFDIPOT Analysis → AoE Expansion → Oracle Definition. Используй в MAS-пайплайне: Результат → Agent-Generator как Техническое Задание.



# Итоговая таблица: Test Planning 2026?

---

Workflow: Feature → Golden Prompt (SFDIPOT) → Agent-Generator → Agent-Critic → RAG. Key: «Человек = вектор, AI = масштаб».




## Rapid Data

# Как использовать delimiters для генерации данных?

---

Delimiter — сигнал для парсера. Используй пайп (|) для структуры. Пример: `% user_age | integer | random[18-99]`.



# Пример prompt для JSON данных.

---

Пример: «Вы — JSON-генератор. Создай 5 объектов rooms: id (UUID), type (single/double), price (100-500), available (boolean). Формат: JSON array.»



# Как LLM трансформирует JSON в SQL?

---

LLM работает как транспайлер: получает schema JSON → генерирует CREATE TABLE + INSERT. Пример: `{id, name} → CREATE TABLE (id UUID, name TEXT)`.



# Как интегрировать LLM в тестовый фреймворк через API?

---

В 2026 используем SDK с типизацией: Instructor для Python. Workflow: тест → prompt → LLM → JSON → Pydantic �� данные в БД.



# Как создать сложные данные для boundary testing?

---

LLM хорош в неочевидных границах. Для поля «Имя»: длина (255), спецсимволы, юникод, SQL-инъекция. Промпт: «Сгенерируй 5 значений на границе UTF-8».



# Что такое data masking и анонимизация?

---

Важен риск PII Leakage. LLM делает Synthetic Data Generation: создает «синтетических двойников», сохраняющих статистические свойства, но не реальных людей. GDPR-совместимо.



# Пример on-demand генерации данных?

---

On-demand = генерация во время выполнения теста. Пример: тест бронирования генерирует rooms в real-time: {id, type, price} с random значениями.



# Какие форматы данных поддерживает LLM?

---

LLM поддерживает: JSON, XML, SQL, CSV, YAML. Также: email, phone, URL, code snippets. Ключ — указать формат в prompt.



# Как сгенерировать pairwise test data?

---

All-Pairs вручную долго. LLM делает за секунду. Промпт: «Pairwise для Browser[Chrome,Safari], OS[iOS,Android], Network[5G,EDGE]. Минимальный набор.»



# Как создать negative test data?

---

Negative test = невалидные входные данные. Генерируй: пустые значения, неверный формат, слишком длинные строки, спецсимволы. Пример: email без @.



# Какие инструменты для test data?

---

Инструменты: 1) LLM (Groq/OpenAI); 2) Faker; 3) PostgreSQL generate_series; 4) SpecFlow. LLM = гибкость.



# Как измерить quality test data?

---

Quality метрики: 1) Coverage (% покрытых границ/классов); 2) Uniqueness; 3) Validity; 4) Correlation (реалистичность).



# Что такое On-the-fly Data Perturbation?

---

Data Perturbation — ИИ берет «хорошие» данные и вносит шум. Пример: «test@mail..com» (двойная точка). Тестирует устойчивость к грязным данным.



# Что такое Self-Referential Data?

---

Self-referential = LLM генерирует связанные данные. Создает «Заказ» → автоматически «Пользователь», «Товар», «Адрес» с логической связью (ID совпадают).



# Что такое Format Transformation (JSON to SQL)?

---

LLM как транспайлер: понимает схему JSON → генерирует CREATE TABLE + INSERT, адаптируя типы (ISO-8601 → DATETIME).



# Что такое data contract testing?

---

Data contract = соглашение о формате между сервисами. Тестируй: 1) Schema validation; 2) Type checking; 3) Required fields; 4) Breaking changes.



# Золотой промпт + Python код

---

## 🎯 Golden Prompt + Python Code Integration

### Prompt:
**Role:** Test Data Engineer. Генерируй качественные тестовые данные.

**Context:** Компонент, тип данных

**Instruction:**
1. Определи schema
2. Сгенерируй: Happy path, Boundary, Negative, Edge cases
3. Output: JSON

---

### Python Code (Pytest + Pydantic):

```python
import pytest
from pydantic import BaseModel, Field
from openai import OpenAI

# Schema-first
class BookingData(BaseModel):
    room_name: str
    price: int = Field(ge=100, le=5000)
    features: list[str] = Field(min_items=2)

# LLM Fixture
@pytest.fixture
def ai_data_generator():
    client = OpenAI()
    def _generate(prompt: str):
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            response_format={"type": "json_object"},
            messages=[
                {"role": "system", "content": "Генератор JSON. Отвечай только валидным JSON."},
                {"role": "user", "content": f"{prompt}. Schema: {BookingData.model_json_schema()}"}
            ]
        )
        return BookingData(**response.json())
    return _generate

# Test
def test_hotel_booking(ai_data_generator):
    data = ai_data_generator("VIP номер на границе max цены")
    assert data.price <= 5000
    assert len(data.features) >= 2
```

### Workflow:
1. Prompt → LLM → JSON → Pydantic → Test
2.Типизация решает проблему "хрупкости" ИИ
3. On-demand генерация с уточнениями


# Итоговая таблица: Test Data Generation?

---

Types: Happy path, Boundary, Negative, Edge, Synthetic, Pairwise. Tools: Faker + LLM + delimiters. Key: LLM = разнообразие, которое человек не может придумать.




## UI Automation

# Почему не генерировать полные тесты?

---

Кроме ручной настройки, есть проблема State Management. ИИ сложно знать состояние БД перед E2Е. Полные тесты страдают от «логических дыр» (забыл нажать Сохранить). Поэтому генерируем атомарные Page Objects, логику (Workflow) пишет человек или MAS-оркестратор.



# Что лучше генерировать через LLM?

---

Лучше генерировать: 1) Page Objects из HTML; 2) Locators; 3) Setup/Teardown методы; 4) Helper functions. Не генерируй полные E2E — они требуют контекста.



# Пример prompt для Page Object.

---

Пример: «Вы — Java-разработчик. Создай Page Object из HTML, используя @FindBy аннотации. Для элемента формы используй By.id("email").»



# Как улучшить HTML для AI в 2026?

---

Semantic Web for Bots. ARIA-labels важнее data-testid — мультимодальные LLM обучаются на accessibility. Если HTML понятен слепому (через экранный диктор), он на 99% понятен ИИ-агенту. Добавь: role, aria-label, alt для изображений.



# Как интегрировать Page Object в фреймворк?

---

Page Object = строительный блок. Используй в тесте: page.fillEmail("test@test.com").clickSubmit(). Assertions отдельны.



# Проблемы с deprecated API в LLM?

---

Решение 2026: RAG с актуальной документацией. Подавай в контекст свежий API Reference Playwright/Selenium вместо «напиши код». Это гарантирует актуальные методы.



# Разница Page Factory и @FindBy?

---

Page Factory — паттерн, @FindBy — аннотация для локаторов. Page Factory инициализирует элементы через @FindBy.



# Как улучшить testability HTML?

---

data-testid, стабильные ID, accessibility. Избегай динамических классов.



# Что такое visual regression testing в 2026?

---

Современный Visual AI отошел от pixel-perfect к Layout Alignment. ИИ понимает: смещение текста на 1px из-за шрифта — не баг. Баг = кнопка перекрыла текст. Инструменты: Applitools Eyes, Percy.



# Как генерировать locators автоматически?

---

AI генерирует locators из DOM: By.css, By.xpath. Пример: «Создай locator для кнопки Submit» → By.xpath("//button[@type='submit']").



# Что такое accessibility testing AI?

---

AI тестирует a11y: контрастность, клавиатурная навигация, ARIA. Инструменты: axe-core, Lighthouse.



# Как улучшить test flakeiness?

---

Стабильные wait, explicit waits, retry логика. AI может генерировать robustactions.



# Что такое smart selectors в 2026?

---

Multi-indicator Selectors. ИИ генерирует «ансамбль»: текст + роль + координаты. Если один признак изменился, тест использует другие. Пример: button[role='submit'] + button с текстом 'Buy'.



# Как тестировать dynamic content?

---

Dynamic content = контент меняется. Используй: waitForElement, verifyAfter, AI-generated assertions.



# Что такое AI test orchestration?

---

AI orchestration = AI управляет тестами. Выбирает что тестировать, адаптирует последовательность.



# Пример AI-driven test generation?

---

AI анализирует код → генерирует тесты → запускает → анализирует результаты → адаптирует.



# Golden Prompt: HTML → Playwright Page Object

---

## 🎯 Golden Prompt: HTML to Playwright Page Object

### Prompt:
**Role:** Senior SDET, эксперт по Playwright и Python.

**Context:**
```html
[ВАШ HTML]
```

**Task:**
Создай Page Object:
1. **Locators:** Используй `page.get_by_role`, `page.get_by_label`, `page.get_by_test_id`. Избегай XPath.
2. **Structure:** `__init__` → все локаторы. Высокоуровневые методы. Type Hinting.
3. **Robustness:** Добавь `is_loaded()` для проверки.
4. **PEP8:** Чистый код.

### Python Code Example:

```python
from playwright.sync_api import Page, Locator

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.get_by_label("Username")
        self.password_input = page.get_by_label("Password")
        self.submit_button = page.get_by_role("button", name="Sign in")
        self.error_message = page.get_by_role("alert")
    
    def is_loaded(self) -> bool:
        return self.submit_button.is_visible()
    
    def login(self, username: str, password: str) -> None:
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.submit_button.click()
    
    def login_with_invalid_credentials(self, username: str, password: str) -> str:
        self.login(username, password)
        return self.error_message.inner_text()
```

### Почему работает:
1. Семантика (get_by_role) → 80% стабильнее
2. Высокоуровневые методы → 1 изменение = 1 метод
3. is_loaded() → предотвращает flakiness

### Интеграция в MAS:
Результат → передается Agent-Executor для E2E сценариев.


# Итоговая таблица: UI Automation 2026?

---

## Summary: UI Automation (2026)

| Параметр | Традиционный | AI-Native |
|:--- |:--- |:--- |
| Локаторы | Жесткие (XPath) | Smart Selectors (Semantic) |
| Ожидания | sleep/waitFor | AI-анализ трафика |
| Поддержка | Ручная | Self-healing |
| Проверки | Сравнение строк | Визуальный + смысловой |

### Ключевой инсайт:
AI-тесты = устойчивость (resilience). Человек = Intent, AI = Implementation.



## Exploratory Testing

# Разница algorithmic vs heuristic?

---

Алгоритм = путь (Step 1 → Step 2). Эвристика = способ поиска (Fallible problem-solving). ИИ по природе = эвристическая система, ищет закономерности, не следует жесткому алгоритму. Это делает его идеальным партнером для ET.



# Формат charter для ET?

---

Charter = миссия, не тест-кейс. Формат: **Explore** <target> **With** <resources> **To discover** <info>. В 2026 добавляют Resources (инструменты/данные). ИИ заполняет этот блок автоматически.



# Как LLM помогает augment рисков?

---

LLM дополняет список рисков: генерирует новые идеи, обновляет существующие риски.



# Использование SFDIPOT для ET?

---

ИИ как SFDIPOT-сканер: скорми описание фичи → «Найди слабое место в Time (тайм-ауты) или Platform (совместимость)». Это направляет ET-сессию в зоны высокого риска.



# Как создать test data для сессии?

---

LLM генерирует тестовые данные для сессии ET. Пример: «Создай user с expired card».



# Пример использования LLM во время ET сессии?

---

Workflow: 1) Определи цель; 2) LLM генерирует variations (edge cases); 3) Тестируй; 4) Notes → LLM → bugs report. LLM = ускорение генерации идей.



# Как LLM помогает в summarization?

---

В 2026 LLM не просто суммирует — классифицирует: отделяет 'баг' от 'предложения UI/UX' от 'вопроса к аналитику'. Автоматическая категоризация наблюдений.



# Ограничения LLM в ET?

---

Multimodal LLMs (GPT-5) 'видят' UI. Главное ограничение теперь = Lack of Curiosity. ИИ не 'чувствует', что что-то не так. Человек = интуиция, ИИ = генерация идей.



# Что такое session-based testing?

---

Session-based = тестирование сессиями. Каждая сессия имеет цель, время, charter. Ограничение по времени.



# Как документировать находки?

---

Notes: что делал, что нашел, вопросы, идеи. LLM может структурировать в отчет.



# Какие техники для bugs discovery?

---

Техники: 1) Tour; 2) Bug hunting; 3) Scavenger; 4) Feasibility. LLM дополняет.



# Как определить когда остановиться?

---

Остановись когда: 1) Время вышло; 2) Новых находок нет; 3) Покрытие достаточное.



# Что такое coverage model для ET?

---

Coverage model = что тестируем. LLM помогает определить dimensions: функциональность, данные, платформы.



# Как использовать LLM для test charter?

---

LLM генерирует charter: «Explore [feature] with [test data] to discover [goal]». Структурирует мысли.



# Что такое rapid reporting?

---

Rapid reporting = LLM создает отчет сразу после сессии. Notes → Markdown → готовый отчет.



# Как AI расширяет ET сессию?

---

AI расширяет: 1) Генерирует variations; 2) Предлагает edge cases; 3) Документирует находки.



# ET + AI Workflow?

---

### Mind Map Augmentation
AI → достраивает карту приложения на лету. Предлагает неизвестные направления.

### Test Tours with AI
AI-агент параллельно выполняет рутинные туры, пока человек ищет сложные баги.

### Debriefing with LLM
AI как «напарник» задает вопросы после сессии. Выявляет дыры в исследовании.


# Итоговая таблица: ET + AI?

---

## Summary: Exploratory Testing (Human + AI)

| Этап | Человек | ИИ (Copilot) |
|:--- |:--- |:--- |
| Chartering | Миссия и фокус | Генерация идей |
| Execution | Интуиция, аномалии | Edge cases, данные |
| Note Taking | Ключевые мысли | Транскрибация |
| Reporting | Решение о качестве | Баг-репорты из заметок |

### Ключевой инсайт:
AI борется с когнитивной слепотой. Человек проверяет то, что знает. ИИ предлагает то, о чем не думал.



## AI Agents

# Характеристики AI agent?

---

2026: к характеристикам добавились: 1) Reasoning — способность рассуждать; 2) Persistence — восстановление после сбоя без потери прогресса. Агент = Goal + Perceive + Reason + Act + Remember.



# Как работает function calling?

---

LLM НЕ вызывает функцию сама — она генерирует JSON с аргументами. Вызов делает ваш код (оркестратор). Цикл: Промпт → LLM (выбор) → Код (выполнение) → LLM (финальный). Критично для безопасности.



# Разница tool vs agent?

---

Tool = конкретная функция. Agent = сущность, которая использует инструменты для достижения цели.



# Пример создания AI agent с LangChain4J / LangChain?

---

LangChain: from langchain import agent. @Tool('create_rooms') — декоратор для функций. Agent использует tools для достижения цели.



# Что такое chaining инструментов?

---

Chaining = передача данных от одного tool к другому. Tool A → output → Tool B → result.



# Как передавать данные между tools?

---

Chaining: результат tool A становится входом tool B. Пример: search → extract → validate.



# Пример use case для test data agent?

---

Test data agent: 1) Create rooms; 2) Create bookings; 3) Query DB. Complete workflow.



# Какие инструменты нужны для test data agent?

---

Инструменты: 1) DB create; 2) SQL execution; 3) HTTP calls; 4) File operations.



# Что такое ReAct agent pattern?

---

ReAct = Reasoning + Action + Observation. База для дебага: смотри логи, где сломалась логика — на Thought (неверный вывод) или Action (не тот инструмент).



# Как измерить agent effectiveness?

---

Metrics: 1) Completion time; 2) Success rate; 3) Autonomy level; 4) Resource usage.



# Что такое agent memory и context?

---

Short-term: контекст текущей сессии. Episodic: история прошлых успешных задач. Semantic: глобальные знания (RAG/Wiki). Три типа памяти в 2026.



# Какие риски при autonomous agents?

---

State Explosion: агент может насоздавать столько данных, что положит сервер. Решение: квоты на ресурсы + автоматический Cleanup (Teardown) после работы.



# Что такое agent orchestration?

---

Agent orchestration = несколько agentов работают вместе. Один координирует другими.



# Как создать multi-agent system?

---

Multi-agent: 1) Planner agent; 2) Execution agent; 3) Validator agent. Общаются через messages.



# Что такое agent monitoring?

---

Agent monitoring = логирование действий agent. Важно для debug и compliance.



# Как сделать agent safe?

---

Safety: 1) Budget limits; 2) Human-in-the-loop; 3) Transaction rollback; 4) Sandbox.



# Оптимальная комбинация моделей?

---

## Оптимальная комбинация моделей: 2 модели

### Почему не 3-4?
3-4 модели = академический идеал, но дорого и сложно. Groupthink риск сохраняется если модели из одного семейства.

### Оптимально: "Тяжелая" + "Быстрая"

| Роль | Модель | Почему |
|:--- |:--- |:--- |
| Generator | Быстрая (Llama/GPT-4o mini) | Пишет код по шаблону, поправят |
| Critic | Тяжелая (GPT-5/Claude 4) | Нужен "высший разум" |
| Fixer | Быстрая | Простое исправление |
| Executor | Код (Python/Docker) | Не LLM, детерминирован |

### Groupthink риск
Одинаковые модели соглашаются с ошибками друг друга. Используй разные семейства (OpenAI + Anthropic).

### Варианты:
- "Эконом" (1 модель + разные промпты)
- "Баланс" (2 модели) — рекомендуемый
- "Гетерогенный пайплайн" (2 разных семейства)

### Executor = не LLM
Это код на Python, который запускает тесты в Docker. Возвращает traceback — лучшее лекарство от hallucinations.


# Итоговая таблица?

---

## Tool vs Agent (2026)

| Параметр | Tool | AI Agent |
|:--- |:--- |:--- |
| Интеллект | Нет | LLM |
| Инициатива | Вызывается | Сам |
| Память | Нет | 3 типа |
| Пример | execute_sql() | Agent |

### Safety:
Docker sandbox + budget limits = обязательно для прода.



## Customized LLMs

# Проблема LLMs с контекстом?

---

Context Window — ограничение на объем данных, который модель видит одновременно. В 2026 типично 128K-1M токенов. Если контекст превышен — используй Chunking или RAG.



# Что такое token и context window?

---

Token — единица текста (часть слова). Context Window — сколько токенов модель 'видит' за раз. Llama 3.3 = 128K, Claude 3 = 200K. Важно для тестирования больших репозиториев.



# Как работает RAG?

---

RAG = Retrieval + Augment + Generate. Работает: query → search vector DB → top-K docs → augment prompt → LLM generates answer. Снижает hallucinations, привязывает к фактам.



# В чем разница между RAG и fine-tuning?

---

RAG — добавляет внешние знания (retrieval). Fine-tuning — переобучает модель на специфичных данных. RAG = актуальность, Fine-tuning = стиль/поведение.



# Когда применять RAG vs fine-tuning?

---

RAG: нужен актуальный контекст, большая база знаний, частые обновления. Fine-tuning: специфичный стиль, формат вывода, особая логика. Часто используют оба.



# Преимущества RAG?

---

1) Актуальные данные без переобучения; 2) Прозрачность (можно показать source); 3) Меньше hallucinations; 4) Масштабируемость.



# Преимущества fine-tuning?

---

1) Специфичный стиль/тон; 2) Лучше follow instructions; 3) Работает офлайн; 4) Единый API без external calls.



# Как выбрать подходящий подход для проекта?

---

Вопросы: 1) Данные часто меняются? → RAG. 2) Нужен специфичный стиль? → Fine-tuning. 3) Бюджет ограничен? → RAG дешевле. 4) Важна скорость? → Fine-tuning быстрее.



# Какие есть LLM провайдеры в 2026?

---

OpenAI (GPT-4o), Anthropic (Claude 3.5), Google (Gemini 2), Meta (Llama 3.3), Mistral, Cohere. Также локальные: Ollama, LM Studio.



# Как выбрать модель для задачи?

---

Критерии: 1) Context window; 2) Speed vs Quality; 3) Cost; 4) Rate limits. Тестирование: запусти same prompt на разных моделях — сравни ответы.



# Что такое quantization?

---

Quantization — сжатие модели (fp16 → int8 → int4). Уменьшает размер и ускоряет, но теряет точность. Q4-KVQ — популярный формат для локальных моделей.



# Как оптимизировать costs при работе с LLM?

---

1) Temperature=0 для deterministic output; 2) Кэширование ответов; 3) Smaller models для простых задач; 4) Batch processing; 5) Prompt engineering — точнее промпт = меньше токенов.



# Что такое embedding model и зачем?

---

Embedding — преобразование текста в вектор (числа). Используется для similarity search в RAG. Модели: text-embedding-3-small, sentence-transformers. Важно выбрать правильную размерность.



# Как тестировать RAG систему?

---

Метрики RAGAs: 1) Faithfulness — ответ vs найденные docs; 2) Answer Relevance; 3) Context Precision. Также: Hit Rate, MRR. Unit + Integration + E2E тесты.



# Что такое hybrid search в RAG?

---

Hybrid = keyword (BM25) + semantic (vector) search. Комбинирует точность keyword с пониманием semantic. В 2026 стандарт для production RAG.



# Что такое reranking в RAG?

---

Reranking — переупорядочивание результатов before generation. Модель (cross-encoder) оценивает пары query-documents. Улучшает quality ценой latency.



# Что такое evaluation metrics для LLM?

---

MT-Bench, HELM, TruthfulQA, MMLU. Для RAG: Hit Rate, MRR, NDCG. LLM-as-Judge — используй одну LLM для оценки другой. Важно: human evaluation остается gold standard.



# Итоговая таблица: RAG vs Fine-tuning?

---

| Параметр | RAG | Fine-tuning |
| Актуальность | +++ | - |
| Стиль | - | +++ |
| Стоимость | $ | $$ |
| Сложность | Средняя | Высокая |
| Latency | + | +++ |




## RAG

# Компоненты RAG?

---

4 компонента: 1) Corpus — база документов; 2) Embeddings — преобразование в векторы; 3) Vector DB — хранение и поиск; 4) Prompt Builder — объединение query + retrieved docs.



# Как работает similarity search?

---

Similarity search: query → embedding → vector → search. Метрики: 1) Cosine — угол между векторами; 2) Dot Product — быстрее при нормализации; 3) Euclidean (L2) — расстояние. Выбор зависит от обучения модели.



# Ограничение cosine distance?

---

Главная проблема 2026: 'Loss in the Middle' — модель игнорирует середину контекста. Решение: Reranking. Сначала fast vector search → 50 кандидатов → тяжелый reranker (BGE-Reranker) → правильный порядок.



# Какие vector databases используются?

---

Pinecone (managed), Weaviate (open-source), Chroma (simple), Qdrant (Rust), pgvector (PostgreSQL). Выбор: scale, latency, cost.



# Что такое embeddings?

---

Embeddings — числовые векторы, представляющие meaning текста. Model: text-embedding-3-large (OpenAI), sentence-transformers. Размерность: 384-3072.



# Как работает chunking документов?

---

Стратегии: 1) Fixed size (500-1000 chars); 2) Semantic (по параграфам); 3) **Syntax-aware** (для кода — по функциям/классам). QA-контекст: чанк должен содержать целую функцию с декораторами и docstring, иначе ИИ потеряет контекст.



# Что такое vector database?

---

База данных, оптимизированная для similarity search. Индекс: HNSW, IVF. Хранит embeddings + metadata. Поддерживает CRUD + approximate nearest neighbor (ANN) search.



# Пример использования RAG в тестировании?

---

QA Bot: 1) Загрузи документацию/код; 2) Вопрос → search → найденные docs → LLM → ответ со ссылками на source. Тестировщик получает точные ответы из docs.



# Какие есть vector store options?

---

Managed: Pinecone, Weaviate Cloud, Azure AI Search. Open-source: Qdrant, Milvus, Chroma. Self-hosted: pgvector. Edge: Redis, Elasticsearch.



# Как оценить retrieval quality?

---

RAGAs Framework: 1) **Faithfulness** — ответ соответствует найденным docs (нет hallucinations); 2) **Answer Relevance** — ответ решает вопрос; 3) **Context Precision** — качество чанков.



# Что такое hybrid search?

---

Hybrid = semantic (vector) + keyword (BM25). Семантика ловит синонимы, keyword — точные совпадения. В 2026 стандарт: weighted combination (0.7 semantic + 0.3 keyword).



# Как сделать chunking стратегию?

---

1) Анализируй типичный query length; 2) Для кода — по функции/классу; 3) Для docs — по параграфам; 4) Добавь overlap (10-20%); 5) Экспериментируй с размером.



# Что такое parent document retrieval?

---

Parent doc — хранишь большие docs, retrieval возвращает chunks. При генерации можно fetch full doc. Balance: small chunks for search, full doc for context.



# Что такое query expansion?

---

Query expansion — расширение запроса синонимами/related terms перед embedding. Используй LLM для генерации related queries. Улучша recall.



# Как сделать multi-modal RAG?

---

Multi-modal = text + images + tables. Используй: 1) CLIP для image embeddings; 2) Table extraction для структурированных данных; 3) Multi-vector retrieval.



# Что такое agentic RAG?

---

Agentic RAG = RAG + Agent. Agent может: 1) Determine if retrieval needed; 2) Multi-step retrieval; 3) Verify answer against sources. Более гибкий чем static RAG.



# Как тестировать RAG систему?

---

Уровни: 1) Unit — embedding quality; 2) Integration — retrieval accuracy; 3) E2E — generation quality. Инструменты: RAGAs, LangSmith, Promptfoo.



# Итоговая таблица: RAG стратегии?

---

## Стратегии RAG для QA

| Тип данных | Стратегия чанкинга | Способ поиска |
|:--- |:--- |:--- |
| Тех. документация | Semantic (заголовки) | Hybrid Search |
| Исходный код | Function-level (AST) | GraphRAG + Vector |
| Логи ошибок | Sliding Window (20% overlap) | Keyword |
| Спецификации | Parent-Document | Semantic |

### Agentic RAG = Fixer
Fixer = Agentic RAG: идет в базу паттернов → анализирует → применяет к багу.



## Fine-tuning

# Что такое fine-tuning?

---

Fine-tuning = 'изменение ДНК' модели. Учит модель 'разговаривать на языке компании'. RAG дает знания, Fine-tuning дает протокол: ответ в строгом JSON, специфичная терминология.



# Как работает LoRA?

---

LoRA = 'наклейка' на базовую модель. Основные веса frozen, тренируются tiny layers. Преимущество: можно мгновенно переключать специализацию: днем SDET, вечером техписатель — подменяй LoRA-файлы.



# Формат training data?

---

JSONL (JSON Lines). Каждая строка = один example. Формат: {'prompt': '...', 'completion': '...'}. Для chat: {'messages': [{'role': 'user', 'content': '...'}]}.



# Как оценить fine-tuned модель?

---

Метрики: 1) Loss на validation set; 2) Human evaluation; 3) Benchmarks (MT-Bench); 4) Compare with base model. A/B testing на реальных запросах.



# Когда применять RAG vs fine-tuning?

---

2026 правило: RAG = данные меняются чаще недели. Fine-tuning = нужно изменить логику рассуждений или гарантировать 100% структуру вывода (тесты по вашему фреймворку).



# Что такое JSONL формат?

---

JSONL (JSON Lines) — построчный JSON. {'prompt': 'Q', 'completion': 'A'}. Удобен для потоковой обработки. Конвертируй: pandas.DataFrame.to_json(orient='records', lines=True).



# Как подготовить данные для fine-tuning?

---

1) Clean data — удали noise; 2) Deduplicate; 3) Balance classes; 4) 100-500 examples minimum; 5) Format consistently; 6) Split: 80/10/10 train/val/test.



# Какие инструменты для fine-tuning?

---

OpenAI Fine-tuning API, Hugging Face PEFT/LoRA, LangChain fine-tuning, Modal (cloud GPU). Для локально: Lamini, Fireworks.ai. Основное: compute + data quality.



# Какие есть training frameworks?

---

1) OpenAI (gpt-3.5-turbo); 2) Hugging Face Transformers + PEFT; 3) Axolotl (open-source); 4) DeepSpeed; 5) LoRAX (serverless).



# Как определить training size?

---

Минимум: 50-100 examples для style, 500+ для complex tasks. Правило: enough to move the model, not overwhelm. Start small, eval, iterate. Quality > quantity.



# Что такое evaluation metrics?

---

1) Loss/Cross-entropy; 2) Perplexity; 3) Accuracy on test set; 4) BLEU/ROUGE для generation; 5) LLM-as-Judge. Human eval остается важным.



# Как избежать overfitting?

---

1) Early stopping; 2) Regularization (LoRA rank low); 3) Smaller learning rate; 4) More data; 5) Validation set early. Overfit = модель memorizes training, не generalizes.



# Что такое RLHF?

---

RLHF = Alignment. Мы учим модель 'писать тесты, которые нравятся нашим синьорам'. 3 этапа: 1) Collect preferences; 2) Train reward model; 3) PPO. Делает AI частью команды.



# Что такое DPO?

---

DPO = Direct Preference Optimization. Упрощенный RLHF: без reward model, directly optimize на pairwise preferences. Проще, дешевле, работает лучше на многих задачах.



# Как выбрать base model для fine-tuning?

---

Criteria: 1) Size (GPU memory); 2) Context length; 3) Quality/speed tradeoff; 4) License. Popular: Llama 3, Mistral, Qwen. Start with 7B, scale if needed.



# Что такое catastrophic forgetting?

---

Catastrophic forgetting = модель теряет старые abilities при fine-tuning на новые. Решение: 1) Multi-task learning; 2) Rehearsal (include old data); 3) Elastic weights.



# Пример fine-tuning для QA системы?

---

1) Collect 200 Q&A pairs from domain; 2) Format as JSONL; 3) Fine-tune Llama 3 8B с LoRA; 4) Eval на test set; 5) Deploy. Result: QA bot знает domain-specific terminology.



# Итоговая таблица: Fine-tuning?

---

## Fine-tuning в деталях

| Параметр | Full FT | LoRA/QLoRA |
|:--- |:--- |:--- |
| GPU память | Огромная | Низкая |
| Забывание | Высокий | Низкий |
| Скорость | Дни/Недели | Часы |
| Применение | Новая база | Специализация |

## 🏁 Интеграция в MAS
1. Base: Llama 3/GPT-4
2. Fine-tuning: Стиль (твой code style)
3. RAG: Знания (Jira/Confluence)
4. Agents: Действие (Docker/Playwright)
5. Mutation Testing: Контроль (арбитр)


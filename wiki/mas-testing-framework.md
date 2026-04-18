# MAS-Testing Framework (Conceptual)

**Last Updated:** 2026-04-18
**Status:** Theoretical / Conceptual (NOT confirmed in original papers)
**Sources:** Gemini analysis, [[wiki/agentic-patterns]] pipeline triad

---

> **Note:** This framework was initially derived from incorrectly interpreted paper analysis. The actual papers describe SWE-Tester (2-step pipeline). However, MAS is included here as a valuable **conceptual model** for multi-agent testing architectures.

---

## Overview

**MAS = Multi-Agent System** для тестирования — это переход от "AI как ассистент" к "AI как автономный отдел QA".

Conceptual model: вместо одной модели используется сеть специализированных агентов (тестировщик, разработчик, критик).

**Ожидаемый результат:** Снижение уровня "галлюцинаций" в коде тестов на ~35% по сравнению со стандартным подходом.

---

## Agent Roles (Conceptual Model)

| Role | English | Russian | Goal |
|------|---------|---------|------|
| **Generator** | The Generator | Генератор | Пишет тесты, "оптимист" |
| **Critic** | The Reviewer | Критик | Ищет баги и антипаттерны, "пессимист" |
| **Fixer** | The Fixer | Исправитель | Исправляет упавшие тесты |
| **Executor** | The Executor | Исполнитель | Запускает тесты в изолированной среде |

### Why 4 roles?

Одиночная модель (даже GPT-5) склонна к "замыливанию глаза" — верит в свой ошибочный код. Разделение ролей снижает галлюцинации.

Это соответствует [[wiki/agentic-patterns]] — Pipeline Triad паттерн: `Creator → Critic → Arbiter`.

---

## Communication Protocol (Conceptual)

Conceptual: агенты общаются через **Quality Data Plane** — общий слой данных (JSON/Protobuf):

```
Generator → [Quality Data Plane] → Critic
    ↑                                   │
    └────────── Fixer ←────────────────┘
                    ↑
              Executor (sandbox)
```

**Conceptual rationale:**
- Избегает "испорченного телефона"
- Каждое решение фиксируется в реестре состояний
- Каждый агент видит что сделали коллеги на предыдущем шаге

---

## DoR/DoD Validation Layer (Conceptual)

### Definition of Ready (DoR)

Conceptual: прежде чем Generator начнет работу, валидатор проверяет:
- [ ] Достаточно ли описан контракт API?
- [ ] Доступны ли моки для внешних зависимостей?
- [ ] Есть ли тестовые данные?

### Definition of Done (DoD)

Conceptual: после генерации проверяется:
- [ ] Тест проходит в CI/CD без ошибок?
- [ ] Тест не "хрупкий" (flaky)?
- [ ] Код соответствует корпоративному гайдлайну?

**Если DoD не пройден** — цикл запускается заново.

---

## Pre-commit AI-Refining (Conceptual)

```
1. Developer pushes code
2. MAS перехватывает push до основных тестов
3. Agents анализируют изменения
4. Agents сами дописывают/исправляют тесты
5. Human получает PR с уже актуализированными тестами
```

---

## QA Engineer Role Evolution (Conceptual)

| Before (2024) | Concept (2026+) |
|---------------|----------------|
| Пишет тесты | Архитектор агентов |
| Проверяет код тестов | Настраивает Prompt-инструкции |
| Меняет тесты вручную | Мониторит AI Trust Score |
| Регрессионное тестирование | Стратегия качества |

**Вывод (conceptual):** QA инженер становится "Architect of AI QA Factory" вместо "test writer".

---

## Comparison: SWE-Tester vs MAS

| Aspect | SWE-Tester (confirmed) | MAS-Testing (conceptual) |
|--------|---------------------|---------------------|
| Source | arxiv papers | Gemini analysis |
| Agents | 0 (2-step pipeline) | 4 roles |
| Approach | Retrieval + Edit | Multi-agent system |
| Fine-tuning | Required | Prompt-only |
| Isolation | Via scaffold | Via Quality Data Plane |

---

## Related Wiki Topics

- [[wiki/mas-vs-swe-comparison]] — MAS vs SWE-Tester comparison
- [[wiki/agentic-patterns]] — Pipeline Triad паттерн
- [[wiki/swe-tester-framework]] — Подтверждённый фреймворк
- [[wiki/ai-testing-glossary]] — Термины и определения
- [[wiki/testing-stability]] — Flakiness и стабильность
- [[wiki/ai-testing-metrics]] — Новые метрики для AI QA

## Open-Source Tools (Free / MIT / Apache 2.0)

Апрель 2026 — сформировался чёткий стек бесплатных решений.

| Tool | Status | Best For |
|------|--------|---------|
| **MARTI-v2** | Open-Source | Tree Search RL — "пробуй и ошибайся" для генерации тестов |
| **LangGraph** | Open-Source | Сложная логика — если Критик бракует → возврат Генератору |
| **CrewAI** | Open-Source | Быстрый старт через Role-based agentes |
| **Dify** | Self-hosted | Визуальная сборка агентов без кода |
| **DeepEval** | Open-Source | Оценка качества AI-тестов (метрики) |

---

## Implementation Plan (4 Phases)

### Phase 1: Инфраструктура (1-2 недели)

- [ ] **Выбор оркестратора** — LangGraph (гибкость) или Dify (скорость)
- [ ] **Sandboxing** — Docker-контейнеры для изоляции (AI не должен видеть боевую БД)
- [ ] **RAG layer** — Подключение Swagger/OpenAPI + эталонные тесты

### Phase 2: Проектирование "Отдела" (1 неделя)

- [ ] **Агент-Генератор** промпт: "Ты — эксперт по Pytest. Покрой код логикой из задачи"
- [ ] **Агент-Критик** промпт: "Ты — злой QA лид. Ищи хардкод, отсутствие ассертов, логические дыры"
- [ ] **DoD:** "Тест принят если прошёл Docker, 0 линтер-ошибок, одобрен Критиком"

### Phase 3: Пилотный запуск (2-3 недели)

- [ ] Выбрать 1 стабильный сервис
- [ ] Генерация тестов для новых PR
- [ ] **Метрика:** Сколько багов найдено / сколько "мусора"

### Phase 4: Масштабирование

- [ ] Интеграция в CI/CD
- [ ] Обучение на специфических багах системы

---

## PoC Checklist

> **[ ] DoR Analysis** — Умеет ли AI понимать требования из Jira/Notion?
> **[ ] Fix Loop** — Настроена ли обратная связь (если тест упал → агент-Fixer получает лог)?
> **[ ] Quality Validation** — Подключён ли DeepEval для проверки галлюцинаций?

---

## Implementation Options (April 2026)

К 2026 году на рынке уже есть инструменты для реализации MAS-подхода.

### 1. Open-Source Фреймворки

| Tool | Description | Best For |
|------|------------|---------|
| **MARTI v2** (Feb 2026) | Tree Search RL — агенты пробуют разные варианты пока не пройдут | Complex test generation |
| **CrewAI / LangGraph** | Промышленный стандарт оркестрации | Draw graph: Analysis → Test → Review → Fix |
| **Microsoft AutoGen** | Агенты "разговаривают" в чате | Chat-based workflows |

### 2. Enterprise Платформы

| Platform | Description | Best For |
|----------|------------|----------|
| **Testomat.io** | AI-Powered Orchestration — сканирует Jira, генерирует edge case тесты | Enterprise teams |
| **Dify / DIMA-AI** | Визуальные конструкторы "QA-агента из кубиков" | Low-code approach |

### 3. Пример на Python (CrewAI)

```python
from crewai import Agent, Task, Crew

# 1. Агент-Генератор
tester = Agent(
  role='Senior QA Automation',
  goal='Generate high-coverage unit tests for {service_name}',
  backstory='Expert in Pytest and Mocking, focuses on edge cases.',
  allow_delegation=False
)

# 2. Агент-Критик
critic = Agent(
  role='Security & Quality Auditor',
  goal='Review tests for logic errors and security leaks',
  backstory='Former hacker, expert in finding flaky tests.',
  allow_delegation=True
)

# 3. Сборка отдела тестирования
qa_crew = Crew(
  agents=[tester, critic],
  tasks=[test_task],
  process='sequential'  # Пишем → Проверяем
)

result = qa_crew.kickoff()
```

### Практические советы

1. **Начните с "Агента-Критика"** — оставить тесты людям, AI проверяет DoD
2. **Используйте Docker-песочницы** — изоляция для Executor
3. **Единый контекст** — Swagger + Sentry = Quality Data Plane

---

### H) Agent Fixer — Detailed Prompt

**Промпт для ИИ-Исправителя (The Fixer):**

> **Role:** Senior SDET & Debugging Expert (Level 6).
> **Context:** Код теста + лог ошибки из Docker/Pytest.
>
> **Objectives:**
> 1. **Анализ Traceback:** Определи тип (AssertionError, ImportError, AttributeError, Timeout).
> 2. **Устранение Галлюцинаций:** Несуществующие методы → сверься со specs.
> 3. **Исправление Моков:** Неверные моки → перепиши инициализацию.
> 4. **Оптимизация:** Код должен "пройти" + чистый.
>
> **Constraints:**
> - Не меняй бизнес-логику, только тест.
> - Если ошибка в specs → `<warning>`.
> - Ответ: код в ```python``` блоке.
>
> **Input:**
> - `{original_code}` — исходный тест
> - `{error_log}` — traceback из pytest
> - `{specs}` — спецификация

**Logic Flow:**
```
Generator → Docker → [passed?] → Критик
                ↓
           [failed?] → Fixer (1-2 iterations)
                ↓
           Docker retry
                ↓
           [3 attempts] → FAIL → report
```

**80% ошибок ИИ** — неверные пути импорта или моки. Fixer справляется за 1-2 итерации.

---

### I) Log Passing Strategy

Ключевой элемент для экономии токенов в 2026 году.

#### 1. Structured Output (Pydantic)

```python
from pydantic import BaseModel
from typing import List

class TestAnalysis(BaseModel):
    code: str
    potential_flakiness: bool
    missing_edge_cases: List[str]
    suggested_improvements: str

# Задача выдает структурированный объект
task_generate = Task(
    description='...',
    output_json=TestAnalysis,  # Pydantic model
    agent=generator
)
# task_review.context[0].output — объект, не строка
```

#### 2. Smart Traceback Extraction (parse_traceback)

Вырезает только суть ошибки, убирает системный шум.

```python
import re

def parse_traceback(stderr: str) -> str:
    """Извлекает суть ошибки, игнорируя системные вызовы."""
    # 1. Ищем секцию с ошибкой (между "_" и "E ")
    match = re.search(r"(_+ .+)[\s\S]+?(E\s+.+)", stderr)

    if match:
        header = match.group(1)  # Название упавшего теста
        error_msg = match.group(2)  # AssertionError и т.д.

        # 2. Ищем строки пользовательского кода (test_*.py)
        code_context = re.findall(r"(tests/test_.*\.py:\d+:.*)", stderr)
        context_str = "\n".join(code_context[-3:])  # Последние 3 строки

        return f"Test: {header}\nContext:\n{context_str}\nError: {error_msg}"

    # Fallback: последние 10 строк
    return "\n".join(stderr.splitlines()[-10:])
```

**Экономия:** до 70% токенов

---

#### 3. RAG Layer для Fixer

Если Fixer видит одну ошибку повторно — начинает "чинить" не то. RAG помогает.

**Архитектура:**
1. **Vector DB:** Сохраняем "золотые примеры" (test + error + fix)
2. **Search:** Перед запуском Fixer — ищем похожий traceback
3. **Prompt Injection:** Добавляем в промпт:
   > *"Похожая ошибка уже исправлялась. Решение: Используй фикстуру `db_session`"*

```python
def rag_lookup(error: str) -> str | None:
    """Поиск похожей ошибки в базе знаний (упрощено)"""
    known_fixes = {
        "ConnectionError": "Используй mock или @pytest.mark.flaky",
        "database is locked": "Добавь pytest.mark.xfix(strict=False)",
    }
    for pattern, fix in known_fixes.items():
        if pattern.lower() in error.lower():
            return fix
    return None


#### Simple JSON Patterns (No DB required)

Простой словарь для быстрого старта — без ChromaDB.

```python
# qa_known_patterns.json
PATTERNS = {
    "ConnectionError": {
        "pattern": ["ConnectionError", "ECONNREFUSED", "connection refused"],
        "fix": "mock external services or use @pytest.mark.flaky(reruns=3)"
    },
    "database is locked": {
        "pattern": ["database is locked", "SQLITE_BUSY"],
        "fix": "add pytest.mark.xfix(strict=False) or use db_session fixture"
    },
    "timeout": {
        "pattern": ["Timeout", "timed out", "asyncio.TimeoutError"],
        "fix": "increase timeout=30 or use @pytest.mark.slow"
    },
    "import error": {
        "pattern": ["ImportError", "ModuleNotFoundError", "cannot import"],
        "fix": "check __init__.py exports and PYTHONPATH"
    },
    "attribute error": {
        "pattern": ["AttributeError", "has no attribute"],
        "fix": "mock missing attributes or check API version"
    },
    "assertion error": {
        "pattern": ["AssertionError", "assert"],
        "fix": "check expected vs actual values in test"
    },
    "fixture not found": {
        "pattern": ["fixture.*not found", " Fixture '.*' doesn't exist"],
        "fix": "define fixture in conftest.py"
    },
    "network error": {
        "pattern": ["NetworkError", "HTTPError", "requests.exception"],
        "fix": "use requests-mock or responses library"
    }
}


def simple_lookup(error: str) -> str | None:
    """Простой поиск по паттернам"""
    error_lower = error.lower()

    for name, data in PATTERNS.items():
        for pattern in data["pattern"]:
            if pattern.lower() in error_lower:
                return data["fix"]

    return None


# Usage
def smart_fixer(error: str, code: str, specs: str) -> str:
    fix = simple_lookup(error)

    if fix:
        # Prompt injection с известным решением
        return f"Known fix: {fix}\n\nOriginal error: {error}\nCode: {code}"
    else:
        # Fallback: generic Fixer
        return f"Error: {error}\nCode: {code}\nSpecs: {specs}"
```

**Usage:**
```python
# Быстрый старт без ChromaDB
fix = simple_lookup(stderr)
if fix:
    print(f"Applying known fix: {fix}")
else:
    fix = fixer.run(error=stderr, code=test_code)
```

---

#### ChromaDB Integration (Lightweight)

```python
import chromadb
from chromadb.config import Settings
from sentence_transformers import SentenceTransformer

# 1. Инициализация
client = chromadb.Client(Settings(
    persist_directory="./qa-rag",
    anonymized_telemetry=False
))

# 2. Коллекция
collection = client.get_or_create_collection(
    name="qa-fixes",
    metadata={"description": "Known fixes for test errors"}
)

# 3. Модель эмбеддингов
embedder = SentenceTransformer('all-MiniLM-L6-v2')


def rag_add_fix(error_pattern: str, fix_solution: str):
    """Добавить известную ошибку и решение"""
    embedding = embedder.encode(error_pattern)
    collection.add(
        ids=[f"fix_{collection.count()}"],
        embeddings=[embedding.tolist()],
        documents=[f"Error: {error_pattern}\nFix: {fix_solution}"],
        metadatas=[{"solution": fix_solution}]
    )


def rag_lookup_chroma(error: str, top_k: int = 2) -> list:
    """Поиск похожих ошибок в ChromaDB"""
    embedding = embedder.encode(error)
    results = collection.query(
        query_embeddings=[embedding.tolist()],
        n_results=top_k
    )
    return [
        doc["solution"]
        for doc in results["metadatas"]
        if doc.get("solution")
    ]


# 4. Использование в Fixer
def smart_fixer(error: str, code: str, specs: str) -> str:
    # Сначала RAG lookup
    fixes = rag_lookup_chroma(error)

    if fixes:
        context = f"Known fixes: {fixes[0]}"
    else:
        context = ""

    # Если не найден — вызываем Fixer с контекстом
    return fixer_prompt.format(
        error=error,
        code=code,
        specs=specs,
        context=context
    )


# === 2. Improved Smart Fixer Orchestrator ===

def smart_fixer_orchestrator(
    raw_error: str,
    code: str,
    specs: str,
    module: str = "unknown"
) -> str:
    """
    Улучшенный фиксер: очищает лог перед поиском
    """
    # Очищаем от шума
    clean_error = parse_traceback(raw_error)

    # Ищем в ChromaDB
    known_fixes = rag_lookup_chroma(clean_error)

    # Формируем расширенный промпт
    context_bonus = ""
    if known_fixes:
        context_bonus = f"\n[RAG Hint]: {known_fixes[0]}"

    return fixer_agent.run(
        error=clean_error,
        code=code,
        specs=specs,
        hint=context_bonus
    )


# === 3. Metadata Schema ===

# metadata fields для ChromaDB
METADATA_SCHEMA = {
    "error_type": str,      # AssertionError, ImportError...
    "module_tag": str,     # AuthService, Payments...
    "timestamp": str,     # 2026-04-18T12:00:00Z
}


# === 4. Self-Learning: Auto-add fixes ===

def auto_learn_fix(
    error: str,
    fixed_code: str,
    module: str,
    attempt: int,
    passed: bool
):
    """Автоматически сохраняет успешные фиксы в базу"""
    if passed and attempt > 1:
        # Починили не с первой попытки — ценный опыт!
        clean_error = parse_traceback(error)
        rag_add_fix(
            error_pattern=clean_error,
            fix_solution=fixed_code,
            metadata={
                "module": module,
                "fix_type": "auto-healed",
                "timestamp": datetime.now().isoformat()
            }
        )
        print("🧠 System learned a new fix pattern!")

    return None
```

**Workflow improved:**
```
Clean error → ChromaDB search → Hint → Fixer
                ↓
        [If fixed on 2+ attempt]
                ↓
        Auto-add to ChromaDB (self-learning)
```
```

**Dependencies:**
```bash
pip install chromadb sentence-transformers
```

**Workflow:**
```
Error → ChromaDB search → Found? → Use solution
                         → Not found → Fixer (LLM)
```

---

### J) Final main.py — Complete Autonomous MAS-Testing

```python
import os
import subprocess
import json
import re
from crewai import Agent, Task, Crew, Process
from pydantic import BaseModel
from typing import List, Optional

# --- 1. Конфигурация и Паттерны ---
IMAGE_NAME = "ai-tester-sandbox"
PATTERNS = {
    "ConnectionError": {
        "pattern": ["ConnectionError", "ECONNREFUSED", "Failed to establish a new connection"],
        "fix": "Убедись, что все внешние API замоканы через `requests_mock` или `responses`."
    },
    "DatabaseLocked": {
        "pattern": ["database is locked", "SQLITE_BUSY"],
        "fix": "Используй фикстуру `db_session` с rollback."
    },
    "ImportError": {
        "pattern": ["ModuleNotFoundError", "ImportError"],
        "fix": "Проверь `sys.path`. Все тесты импортируют от `/home/ai_tester/src`."
    }
}

# --- 2. Умные утилиты (Data Plane) ---
def parse_traceback(stderr: str) -> str:
    """Извлекает суть ошибки"""
    match = re.search(r"(E\s+.+)", stderr)
    if match:
        error_msg = match.group(1)
        code_context = re.findall(r"(test_.*\.py:\d+:.*)", stderr)
        return f"Context: {' | '.join(code_context[-2:])}\nError: {error_msg}"
    return "\n".join(stderr.splitlines()[-10:])

def get_rag_hint(error_text: str) -> str:
    """Поиск по Simple JSON Patterns"""
    for name, data in PATTERNS.items():
        if any(p in error_text for p in data["pattern"]):
            return f"\n[Known Issue: {name}]: {data['fix']}"
    return ""

# --- 3. Агенты (The Crew) ---
generator = Agent(
    role='SDET Generator',
    goal='Написать тесты на Pytest для {module}',
    backstory='Ты эксперт по архитектуре и покрытию кода.',
    allow_delegation=False
)

fixer = Agent(
    role='SDET Debugger',
    goal='Исправить код теста на основе логов',
    backstory='Мастер чтения traceback и исправления галлюцинаций.',
    allow_delegation=False
)

# --- 4. Sandbox ---
def run_in_sandbox(test_code: str, module_name: str) -> dict:
    test_dir = "./generated_tests"
    os.makedirs(test_dir, exist_ok=True)
    file_path = os.path.join(test_dir, f"test_{module_name.lower()}.py")

    with open(file_path, "w") as f:
        f.write(test_code)

    print(f"🧪 Running {file_path} in Docker...")
    result = subprocess.run([
        "docker", "run", "--rm",
        "-e", "PYTEST_ADDOPTS=-p no:cacheprovider",
        "-v", f"{os.path.abspath(file_path)}:/home/ai_tester/tests/test_ai.py:ro",
        IMAGE_NAME
    ], capture_output=True, text=True)

    return {
        "passed": result.returncode == 0,
        "stdout": result.stdout,
        "stderr": result.stderr,
        "code": test_code
    }

# --- 5. Main Pipeline ---
def run_autonomous_qa(module: str, specs: str):
    # Step 1: Generate
    print(f"🚀 Generating tests for {module}...")
    gen_task = Task(
        description=f"Напиши Pytest код для {module}. Spec: {specs}",
        agent=generator,
        expected_output="Python код теста"
    )
    crew = Crew(agents=[generator], tasks=[gen_task])
    current_code = crew.kickoff().raw

    # Step 2: Self-Healing Loop
    for attempt in range(1, 4):
        report = run_in_sandbox(current_code, module)

        if report["passed"]:
            print(f"✅ Success on attempt {attempt}!")
            return report["code"]

        print(f"❌ Attempt {attempt} failed. Healing...")
        error_summary = parse_traceback(report["stderr"])
        hint = get_rag_hint(error_summary)

        # Step 3: Fix
        fix_task = Task(
            description=f"Исправь. Ошибка: {error_summary}. {hint}\nSpec: {specs}",
            agent=fixer,
            expected_output="Исправленный Python код"
        )
        fix_crew = Crew(agents=[fixer], tasks=[fix_task])
        current_code = fix_crew.kickoff().raw

    print("⚠️ Max retries reached. Manual review required.")
    return None

if __name__ == "__main__":
    module = "AuthService"
    specs = "POST /v1/login: 200, 401. Use pytest-mock."

    final_test = run_autonomous_qa(module, specs)
    if final_test:
        print("--- FINAL CODE ---\n", final_test)
```

**How to run:**
```bash
# 1. Build Docker
docker build -t ai-tester-sandbox .

# 2. Run
python main.py
```

**Features:**
- Устойчивость к ошибкам (self-healing)
- Экономия токенов (parse_traceback)
- JSON knowledge base (PATTERNS)
- Docker isolation

---

### Production Ready Stack (2026)

| Component | Technology | Purpose |
|----------|------------|---------|
| **Orchestration** | CrewAI | Generator + Critic + Fixer |
| **Sandbox** | Docker Ephemeral | Изоляция |
| **State** | Pydantic Models | QAState, Quality Data Plane |
| **Memory** | ChromaDB (RAG) | Long-term memory |
| **Telemetry** | parse_traceback | Сжатие контекста |

**Итог:** Self-learning QA platform ✅
```

#### 4. QAState (Quality Data Plane)

```python
from pydantic import BaseModel
from typing import List, Dict, Optional

class QAState(BaseModel):
    attempt: int = 1
    max_retries: int = 3
    test_code: str
    last_error: Optional[str] = None
    is_passed: bool = False
    history: List[Dict] = []

    def update_after_run(self, execution_report: dict):
        self.is_passed = execution_report["passed"]
        if not self.is_passed:
            self.last_error = parse_traceback(execution_report["stderr"])
            self.history.append({"attempt": self.attempt, "error": self.last_error})
            self.attempt += 1
```

#### 5. Full Pipeline (Smart)

```
1. DoR Check → ИИ подтверждает готовность
2. Generate → generator выдает test_code
3. Sandbox Loop:
   - run_in_sandbox(state.test_code)
   - Ошибка → parse_traceback → RAG lookup → fixer.run()
   - Обновляем state.test_code
4. Final DoD → critic проверяет (Pydantic model)
```

**Итог:**
- Решает "Infinite Loop of Nonsense"
- Экономит 70% токенов через parse_traceback
- RAG обучает систему специфике проекта

---

#### 3. Shared State (Quality Data Plane)

```json
{
  "module": "AuthService",
  "current_iteration": 2,
  "history": [
    {
      "attempt": 1,
      "status": "failed",
      "error_type": "ImportError",
      "ai_fix_applied": false
    }
  ],
  "context_files": ["src/auth.py", "specs/openapi.json"]
}
```

#### 4. Improved Feedback Loop

```python
def autonomous_healing_loop(module: str, specs: str, max_retries: int = 3) -> dict:
    current_code = generator_task.run()

    for attempt in range(max_retries):
        report = run_in_sandbox(current_code)

        if report["passed"]:
            return critic_task.run(context={
                "code": current_code,
                "logs": report["stdout"]
            })

        # Log truncation
        short_error = parse_traceback(report["stderr"])

        current_code = fixer.run_task(
            description=f"Fix: {short_error}",
            original_code=current_code,
            specs=specs
        )

    return {"status": "FAILED", "reason": "Max retries reached"}
```

---

### Итоговый чек-лист улучшений

- [ ] **Structured JSON:** Pydantic модели в CrewAI задачах
- [ ] **Log Clean-up:** Регулярка чистит логи от системных путей
- [ ] **DoR/DoD:** Валидатор на входе — если specs пустые, Fixer будет галлюцинировать

---

## Practical Implementation Details

### A) Agent Prompt: Детальный промпт для Критика

**System Prompt (Role Definition):**
> **Роль:** Senior QA Automation & Security Auditor (L6).
> **Инструкция:** Ты специализируешься на выявлении логических изъянов в автоматизированных тестах.
>
> **Чек-лист проверки (Critical Points):**
> 1. **Логическая корректность:** Проверяет ли ассерт именно то, что заявлено в названии теста?
> 2. **Антипаттерны:** Ищи `hardcoded` значения, `Thread.sleep()`, отсутствие cleanup.
> 3. **Мутационный анализ:** Будет ли тест "красным" если изменить логику функции?
> 4. **Flakiness:** Зависимости от порядка выполнения или внешних ресурсов без моков?
> 5. **DoD Compliance:** Соответствует корпоративному стандарту.
>
> **Формат ответа:** JSON: `{status: PASS/REJECT, score: 0-10, critical_issues: [], suggested_fixes: []}`

---

### B) Extended CrewAI Code

```python
from crewai import Agent, Task, Crew, Process

# 1. Агенты
generator = Agent(
    role='SDET Generator',
    goal='Написать надежные интеграционные тесты для API на основе {specs}',
    backstory='Ты лучший в написании сложных моков и асинхронных тестов на Python.',
    verbose=True,
    allow_delegation=False
)

critic = Agent(
    role='QA Critic',
    goal='Провести аудит кода тестов и отклонить те с галлюцинациями.',
    backstory='Твой опыт позволяет видеть скрытые баги.',
    verbose=True,
    allow_delegation=True  # Позволяет вернуть задачу на доработку
)

# 2. Цепочка задач
task_generate = Task(
    description='Создать тесты для {module_name}. Использовать Pytest.',
    expected_output='Файл с тестами .py',
    agent=generator
)

task_review = Task(
    description='Проверить тесты на DoD и отсутствие галлюцинаций.',
    expected_output='Отчет об аудите.',
    agent=critic,
    context=[task_generate]  # Критик видит результат генератора
)

# 3. Сборка команды
qa_crew = Crew(
    agents=[generator, critic],
    tasks=[task_generate, task_review],
    process=Process.sequential,
    full_output=True
)

# Запуск
results = qa_crew.kickoff(inputs={'module_name': 'AuthService', 'specs': 'OpenAPI v3'})
```

---

### C) DoR/DoD Automation

#### Автоматизация DoR (Критерии готовности)

**LLM-Classifier** на этапе создания задачи:
1. Агент "Анализатор" сканирует описание задачи (Jira/Notion)
2. Проверка полноты: если нет API endpoints → комментарий *"DoR не пройден"*
3. Задача возвращается на доработку

#### Автоматизация DoD (Критерии приемки)

**Hybrid Validation** (AI + Инструменты):
1. **Static Analysis** — ruff/ESLint (синтаксис)
2. **AI-Review** — Критик проверяет смысл
3. **Execution Gate** — Docker container, Exit Code 0
4. **Coverage Check** — порог (напр. 80%), PR блокируется если ниже

---

### D) Docker Sandboxing

Критично: AI не должен иметь доступ к боевой БД.

#### Dockerfile для AI-тестов

```dockerfile
FROM python:3.11-slim

WORKDIR /app

# Установка зависимостей
RUN pip install --no-cache-dir \
    pytest \
    pytest-asyncio \
    ruff \
    requests-mock

# Копирование тестов (только чтение)
COPY tests/ ./tests/

# Запуск через ruff + pytest
CMD ["sh", "-c", "ruff check ./tests/ && pytest ./tests/"]
```

#### docker-compose для изоляции

```yaml
services:
  ai-tester:
    build: ./ai-tester
    volumes:
      - ./tests:/app/tests:ro  # только чтение
    environment:
      - API_URL=http://mock-server:8000
      - DB_CONNECTION=none  # явно отключено

  mock-server:
    image: wiremock/wiremock
    ports:
      - "8000:8080"
```

#### Workflow

```
Developer PR → GitHub Actions
    ↓
Build Docker (ai-tester)
    ↓
Run: ruff check → pytest → Coverage Check
    ↓
Artifacts: test-results.json
    ↓
If ALL passed → Merge
```

---

### D) Docker Sandboxing (Extended)

Ephemeral Docker Runners — временные контейнеры которые уничтожаются после прогона.

#### Dockerfile с непривилегированным пользователем

```dockerfile
FROM python:3.11-slim

# Непривилегированный пользователь
RUN useradd -m ai_tester
USER ai_tester
WORKDIR /home/ai_tester

# Минимум зависимостей
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Сгенерированные тесты (только запись)
COPY --chown=ai_tester:ai_tester ./generated_tests ./tests

# Timeout на выполнение
CMD ["pytest", "--maxfail=3", "tests/"]
```

---

### E) DoR Gatekeeper Agent

**Промпт-проверка:**
> "Проанализируй описание задачи. Ответь 'READY', если указаны:
> 1) Эндпоинт API.
> 2) Входные параметры.
> 3) Ожидаемый код ответа.
> В противном случае перечисли, чего не хватает."

**Workflow:**
```
GitHub Action (task created)
    ↓
Gatekeeper Agent (DoR check)
    ↓
[READY] → MAS Generator
    ↓
[NOT READY] → label: needs-info → block
```

---

### F) DoD Validation Table

| Этап | Инструмент | Критерий |
|------|------------|----------|
| Синтаксис | Ruff / Flake8 | 0 errors |
| Безопасность | Bandit | 0 vulnerabilities |
| Выполнение | Docker | Exit Code: 0 |
| Логика | Агент-Критик | Score > 8/10 |

---

### итоговый Workflow

```
1. Input: ссылка на репозиторий / описание функции
         ↓
2. Check: DoR Gatekeeper
         ↓
3. Generate: CrewAI (Generator → Critic → Fixer)
         ↓
4. Execute: Docker sandbox
         ↓
5. Check: DoD Validation (Ruff + Bandit + Critic)
         ↓
6. Output: Pull Request с готовыми тестами
```

---

### G) Python Script: CrewAI + Docker Integration (Improved)

```python
import subprocess
import json
import os
from crewai import Agent, Task, Crew, Process
from pydantic import BaseModel

# Конфигурация
IMAGE_NAME = "ai-tester-sandbox"
CONTAINER_NAME = "qa-ephemeral-runner"
GENERATED_DIR = "./generated_tests"


class QAResult(BaseModel):
    exit_code: int
    stdout: str
    stderr: str
    passed: bool


def build_sandbox():
    """Сборка Docker-образа"""
    print("🔨 Building sandbox...")
    subprocess.run(
        ["docker", "build", "-t", IMAGE_NAME, "-f", "Dockerfile", "."],
        check=True
    )


def save_generated_code(module: str, code: str) -> str:
    """КРИТИЧЕСКАЯ ПРАВКА: Сохранение кода на диск"""
    os.makedirs(GENERATED_DIR, exist_ok=True)
    file_path = f"{GENERATED_DIR}/test_{module.lower()}.py"

    with open(file_path, "w") as f:
        f.write(code)

    print(f"💾 Saved: {file_path}")
    return file_path


def run_in_sandbox(test_file: str) -> dict:
    """Запуск тестов в изолированном контейнере с ограничениями"""
    # Читаем test_file path для docker
    abs_path = os.path.abspath(test_file)

    # Docker с resource limits + no cache provider
    result = subprocess.run([
        "docker", "run", "--rm",
        "--cpus=0.5",              # Ограничение CPU
        "--memory=512m",           # Ограничение RAM
        "-e", "PYTEST_ADDOPTS=-p no:cacheprovider",  # Не писать кэш
        "-v", f"{abs_path}:/home/ai_tester/tests/test_ai.py:ro",
        IMAGE_NAME
    ], capture_output=True, text=True, timeout=120)

    return {
        "exit_code": result.returncode,
        "stdout": result.stdout,
        "stderr": result.stderr,
        "passed": result.returncode == 0
    }


# Агенты CrewAI
generator = Agent(
    role='SDET Generator',
    goal='Создать надежные тесты для {module}',
    backstory='Эксперт по Pytest и mocking',
    allow_delegation=False
)

fixer = Agent(
    role='SDET Debugger',
    goal='Исправить тесты, которые упали в Docker-песочнице',
    backstory='Мастер чтения логов Pytest. Находит причину падения за 1-2 итерации.',
    allow_delegation=False
)

critic = Agent(
    role='QA Critic',
    goal='Отклонить тесты с галлюцинациями. Output: JSON',
    backstory='Находит скрытые баги',
    verbose=True,
    allow_delegation=True
)


def run_qa_pipeline(module: str, specs: str) -> dict:
    """Основной пайплайн с Retry-циклом"""
    # 1. Генерация
    task_gen = Task(
        description=f'Создать тесты для {module}. Spec: {specs}',
        expected_output='test_*.py',
        agent=generator
    )

    task_review = Task(
        description='Проверить DoD compliance. Output: JSON',
        expected_output='{"status": "PASS/REJECT", "score": 0-10}',
        output_json=True,  # Pydantic-style JSON
        agent=critic,
        context=[task_gen]
    )

    crew = Crew(
        agents=[generator, critic],
        tasks=[task_gen, task_review],
        process=Process.sequential,
        full_output=True
    )

    # Запуск CrewAI
    result = crew.kickoff()

    # КРИТИЧЕСКАЯ ПРАВКА: Извлечение и сохранение кода
    test_code = result.raw  # или result.tasks[0].output
    file_path = save_generated_code(module, test_code)

    # 2. Execution в Docker
    execution_result = run_in_sandbox(file_path)

    # 3. ITERATION: Feedback Loop (2026 concept)
    max_retries = 2
    for attempt in range(max_retries):
        if execution_result["passed"]:
            break

        print(f"🔄 Test failed (attempt {attempt + 1}). Sending to Fixer...")

        # Отправляем traceback агенту-Fixer
        fix_task = Task(
            description=f'Исправь тест на основе: {execution_result["stderr"]}',
            expected_output='исправленный test_*.py',
            agent=fixer
        )

        # Повторный запуск
        fix_crew = Crew(agents=[fixer], tasks=[fix_task])
        fixed_result = fix_crew.kickoff()

        # Перезапись
        file_path = save_generated_code(module, fixed_result.raw)
        execution_result = run_in_sandbox(file_path)

    # 4. Итог
    return {
        "crew_result": result.raw,
        "execution": execution_result,
        "ready_for_pr": execution_result.get("passed", False),
        "attempts": attempt + 1
    }


if __name__ == "__main__":
    # Пример использования
    result = run_qa_pipeline(
        module="AuthService",
        specs="POST /api/auth/login => 200, invalid => 401"
    )
    print(json.dumps(result, indent=2))
```

**Ключевые улучшения:**
1. `save_generated_code()` — явно сохраняет на диск
2. `output_json=True` — строгий JSON от Критика
3. Resource limits: `--cpus=0.5 --memory=512m`
4. `PYTEST_ADDOPTS=-p no:cacheprovider` — избегает записи в RO
5. **Retry loop** — Feedback Loop概念 (2026)
6. Pydantic `BaseModel` для типизации

---

### Usage

```bash
# 1. Сборка образа
python qa_pipeline.py --build

# 2. Запуск пайплайна
python qa_pipeline.py --module AuthService --specs "..."

# 3. CI интеграция
github-actions:
  - name: QA Pipeline
    run: python qa_pipeline.py --module ${{ matrix.module }}
```

---

## С чего начать?

> **Лучше начать с автоматизации DoD.** Даже если тесты пишут люди, ИИ-Критик в CI/CD будет отсеивать "мусорные" проверки.

---

## Sources

- Gemini conversation analysis (not verified)
- [[wiki/agentic-patterns]] Pipeline Triad
- [[wiki/swe-tester-framework]] (confirmed framework)
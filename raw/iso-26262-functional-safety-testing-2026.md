# ISO 26262 — Functional Safety for Road Vehicles: QA/Testing Perspective

## 1. Что такое ISO 26262

ISO 26262 — международный стандарт функциональной безопасности электрических и электронных (E/E) систем в дорожных транспортных средствах. Автомобильная адаптация общего стандарта IEC 61508.

**Цель:** обеспечить корректную работу safety-систем и снизить остаточный риск от отказов (случайные аппаратные + систематические ошибки) до приемлемого уровня.

**Последняя версия:** Second Edition, December 2018 (третья редакция в разработке).

### 12 частей ISO 26262:2018

| Part | Название | Содержание |
|------|----------|------------|
| 1 | Vocabulary | Термины и определения |
| 2 | Management of functional safety | Управление, audits, assessment, independence levels |
| 3 | Concept phase | Item definition, HARA, safety goals |
| 4 | System level | Technical safety concept, system design, integration, validation |
| 5 | Hardware level | Hardware design, metrics (SPFM, LFM, PMHF) |
| 6 | **Software level** | **SW requirements, architecture, unit design, verification** |
| 7 | Production & operation | Производство, эксплуатация |
| 8 | Supporting processes | Distributed dev, tool qualification, configuration mgmt |
| 9 | ASIL-oriented analyses | ASIL decomposition, dependent failure analysis |
| 10 | Guidelines (informative) | Примеры |
| 11 | Semiconductors (informative) | Полупроводники |
| 12 | Motorcycles | Адаптация для мотоциклов |

Стандарт следует **V-model**: требования → дизайн → имплементация → unit test → integration test → system test → validation.

---

## 2. ASIL Levels (Automotive Safety Integrity Level, A, B, C, D)

### 2.1 Как определяется ASIL

Три параметра в Hazard Analysis and Risk Assessment (HARA):

- **Severity (S)** — S0 (нет травм) → S1 (лёгкие) → S2 (тяжёлые) → S3 (смертельные)
- **Exposure (E)** — E0 (невероятно) → E1 → E2 → E3 → E4 (высокая)
- **Controllability (C)** — C0 (контролируемо) → C1 → C2 → C3 (неконтролируемо)

**Пример матрицы:** S3 + E4 + C3 → ASIL D. S0/E0/C0 → QM (стандартное качество).

### 2.2 ASIL уровни

| Level | Системы | Коэфф. стоимости |
|-------|---------|------------------|
| QM | Infotainment, освещение | 1× |
| ASIL A | Фонари (не стоп), стеклоомыватель | ~1.5× |
| ASIL B | Фары, стоп-сигналы, TPMS | ~2–3× |
| ASIL C | Круиз-контроль, адаптивные фары | ~3–4× |
| ASIL D | EPS, ABS, AEB, airbags, steer-by-wire | ~3–5× |

### 2.3 Ключевые требования по ASIL

| Требование | A | B | C | D |
|---|---|---|---|---|
| Structural coverage (unit) | Statement | Branch | MC/DC | MC/DC |
| SPFM | — | ≥90% | ≥97% | ≥99% |
| LFM | — | ≥60% | ≥80% | ≥90% |
| PMHF (FIT) | — | <100 | <100 | <10 |
| Fault injection (unit) | + | + | + | ++ |
| Fault injection (integration) | + | + | ++ | ++ |
| Independence (review → assessment) | I0 | I1 → I1 | I2 → I2 | I2 → I2/I3 |

### 2.4 ASIL Decomposition (Part 9)

Позволяет разделить высокий ASIL между независимыми элементами:

| Parent | Допустимые пары |
|--------|----------------|
| ASIL D | D(D) + QM(D), C(D) + A(D), B(D) + B(D) |
| ASIL C | C(C) + QM(C), B(C) + A(C) |
| ASIL B | B(B) + QM(B), A(B) + A(B) |

**Важно:** independence confirmation measures остаются на оригинальном ASIL.

---

## 3. Software Testing Requirements

### 3.1 SW Unit Testing (Part 6, Clause 9)

**Методы:**

| Метод | A | B | C | D |
|---|---|---|---|---|
| Requirements-based | ++ | ++ | ++ | ++ |
| Interface test | ++ | ++ | ++ | ++ |
| Fault injection | + | + | + | ++ |
| Resource usage | + | + | + | ++ |
| Back-to-back model vs code | + | + | ++ | ++ |

### 3.2 SW Integration Testing (Part 6, Clause 10)

| Метод | A | B | C | D |
|---|---|---|---|---|
| Requirements-based | ++ | ++ | ++ | ++ |
| Interface test | ++ | ++ | ++ | ++ |
| Fault injection | + | + | ++ | ++ |
| Resource usage | + | + | + | ++ |
| Back-to-back model vs code | + | + | ++ | ++ |

### 3.3 Structural Coverage

| Coverage | Что проверяет | Мин. ASIL |
|----------|---------------|-----------|
| **Statement** | Каждая строка выполнена ≥1 | QM, A |
| **Branch** | Каждый if/else пройден обеими ветками | B |
| **MC/DC** | Каждое условие независимо влияет на результат | C, D |

**Влияние на усилия:** Statement ~1 тест/функцию → Branch ~2-5 → MC/DC ~8-20+.

### 3.4 Test Environments (Table 16)

| Environment | Описание |
|-------------|----------|
| MiL (Model-in-the-Loop) | Функциональный тест модели |
| SiL (Software-in-the-Loop) | Код на host PC |
| PiL (Processor-in-the-Loop) | Код на целевом процессоре |
| HiL (Hardware-in-the-Loop) | ECU + plant model |
| Vehicle test | Реальное авто |

---

## 4. Verification и Validation

### 4.1 Четыре метода верификации (Part 8, Clause 9)

1. **Reviews** — экспертная оценка артефактов
2. **Analysis** — FMEA, FTA, DFA
3. **Testing** — динамическое выполнение
4. **Walkthroughs** — неформальные ревью

### 4.2 Confirmation Measures (Part 2, Clause 6)

| Measure | Что проверяет | Когда |
|---------|---------------|-------|
| **Confirmation Review** | Качество work product (HARA, safety concept) | ASIL A–D |
| **Functional Safety Audit** | Процесс (safety plan) | ASIL B (опц.), C, D |
| **Functional Safety Assessment** | Safety case в целом | ASIL B (рек.), C, D |

**Independence Levels:**
- I0: Self-assessment
- I1: Different person, same team
- I2: Different team/department
- I3: External (TÜV, SGS, exida)

---

## 5. Tool Qualification (Part 8, Clause 11)

Любой инструмент, влияющий на safety-продукт, требует квалификации.

**TCL (Tool Confidence Level):**
- TI1/TI2 (Tool Impact) — может ли инструмент внести ошибку
- TD1-TD3 (Tool Error Detection) — обнаруживается ли ошибка другими средствами

| | TD1 | TD2 | TD3 |
|---|---|---|---|
| TI1 | TCL1 | TCL1 | TCL2 |
| TI2 | TCL2 | TCL3 | TCL3 |

- **TCL1:** только rationale
- **TCL2:** validation инструмента
- **TCL3:** сертификация (vendor safety manual, compensating measures)

**Примеры:** GCC → TCL3 (нужен safety manual), Simulink Embedded Coder → TCL2-3 (IEC Certification Kit), test frameworks → TCL1-2.

---

## 6. ISO 26262 vs ISO 21448 (SOTIF) vs UL 4600

### 6.1 ISO 21448 — Safety of the Intended Functionality (SOTIF)

| | ISO 26262 | ISO 21448 (SOTIF) |
|---|---|---|
| Root cause | Отказы компонентов | Функциональная недостаточность |
| Hazard model | Fault-based (HARA, FMEA) | Scenario-based (ODD, triggering conditions) |
| Ключевой концепт | ASIL, safety goals | ODD, known/unknown scenarios |
| Mitigation | Redundancy, diagnostics | Algorithm improvement, ODD restriction |
| Validation | Fault injection, HIL | Scenario catalog, simulation |

**Ключевое различие:** Лидар перестал работать → ISO 26262. Лидар не видит пешехода в ливень → ISO 21448 (датчик исправен, алгоритм недостаточен).

### 6.2 UL 4600

- Goal-based (не prescriptive)
- Safety case + Safety Performance Indicators (SPIs)
- SAE Levels 3-5
- Self-certification возможна
- Включает ISO 26262 + ISO 21448 как building blocks

### 6.3 Разница: классическое авто vs автономное вождение

| | Classic (ISO 26262) | Autonomous (+ SOTIF + UL 4600) |
|---|---|---|
| Hazard | Component failures | Performance limitations + faults |
| Водитель | Controllability (C) | No driver — controllability = transferability + predictability |
| Test space | Finite | Infinite (scenario-based, ODD-driven) |
| Exposure | E parameter | **Not considered** — edge cases matter |
| Coverage | Code (statement/branch/MC/DC) | Scenario coverage, ODD coverage |
| Failure model | Deterministic | Non-deterministic (ML uncertainty) |
| Стандарты | ISO 26262 (single) | ISO 26262 + 21448 + 4600 + PAS 8800 |

---

## 7. ML/AI Testing и ISO 26262

### 7.1 Фундаментальный gap

ISO 26262 спроектирован для **детерминированного ПО** — нейросети не детерминированы.

**Что не покрывает ISO 26262:** robustness, uncertainty, interpretability, distribution shift, generalization.

### 7.2 ISO/PAS 8800:2024 — Safety and AI for Road Vehicles

**Опубликован:** 2024. Адаптация ISO 26262 + ISO 21448 для AI-систем.

**Ключевые требования:**
- AI safety lifecycle (data management, training, validation, deployment)
- ML-specific V&V: robustness, OOD detection, performance boundaries
- Data quality, bias, annotation correctness
- Safety argumentation for AI

### 7.3 Архитектурный паттерн ML в safety-critical системах

```
┌─────────────────────────┐
│   ML Perception Module  │ ← QM / ASIL A-B (advisory)
│  (Neural Network)       │
└────────┬────────────────┘
         ▼
┌─────────────────────────┐
│   Deterministic Safety  │ ← ASIL C-D (authoritative)
│   Monitor               │
│   (rules-based, formal  │
│    logic)               │
└────────┬────────────────┘
         ▼
┌─────────────────────────┐
│   Actuator / Controller │
└─────────────────────────┘
```

**Ключевые элементы:**
1. ODD enforcement — fallback при выходе из ODD
2. OOD detector — обнаружение out-of-distribution входов
3. Deterministic safety monitor — отменяет ML при нарушении safety constraints
4. Statistical validation — замена MC/DC на massive scenario testing
5. Field monitoring — SPI-based anomaly detection

### 7.4 Практические тесты для ML-компонентов

| Тест | Что проверяет |
|------|---------------|
| Robustness testing | Adversarial perturbations |
| OOD detection | False positive/negative rates |
| Performance boundary | Accuracy при дожде/ночи/бликах |
| Scenario coverage | % ODD покрытый validation |
| Back-to-back | Deployed vs reference model |
| Resource testing | Inference latency, memory |
| Data quality | Label accuracy, bias |
| Functional insufficiency | Triggering condition identification |

### 7.5 Стандарты для automotive AI (2026)

| Стандарт | Фокус | Статус |
|----------|-------|--------|
| ISO 26262:2018 | Functional safety (systematic + random HW faults) | Current |
| ISO 21448:2022 | SOTIF (performance limitations) | Current |
| ISO/PAS 8800:2024 | AI safety for road vehicles | **Published — most relevant for ML** |
| UL 4600:2023 | Safety case for autonomous products | Current |
| ISO/IEC TR 5469:2024 | AI functional safety (general) | Published |

---

## 8. Ключевые выводы для QA

1. **Classic automotive (ASIL A-D):** V-model, statement/branch/MC/DC, fault injection, confirmation measures. ASIL D = maximum rigor.

2. **Autonomous driving:** ISO 26262 + ISO 21448 (SOTIF scenario-based) + UL 4600 (safety case). Test space от fault-based → scenario-based.

3. **ML/AI:** ISO 26262 не применим напрямую. ISO/PAS 8800 — ML-specific lifecycle. ML = advisory (QM-ASIL B), deterministic monitor = authoritative (ASIL C/D). Чистая нейросеть не может быть ASIL D сертифицирована.

---

*Источники: ISO 26262-1:-12:2018, ISO 21448:2022, ISO/PAS 8800:2024, UL 4600:2023, piembsystech.com, lorit-consultancy.com, embitel.com, users.ece.cmu.edu/~koopman/ul4600, arxiv.org (Pavlitska et al., 2026).*

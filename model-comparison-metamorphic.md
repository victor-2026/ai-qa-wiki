---
title: "Model Comparison - Metamorphic Testing Answers"
updated: 2026-04-30
tags: [model-comparison, metamorphic-testing, Ollama, hardware]
type: comparison
---

# Model Comparison - Metamorphic Testing Answers

**Date:** 2026-04-30  
**Test Question:** "Что такое метаморфное тестирование?"  
**Method:** Ollama via ZeroTier VPN (10.24.175.30:11434)  

---

## Model Outputs (Real)

### 1. llama3.1:8b-instruct-q4_0 — ❌ BAD (6/10)

**Response:**
> "Метаморфическое тестирование (Metamorphic Testing) - это подход к программному обеспечению и играх, в котором программные компоненты или уровни представлены в форме неструктурированных экранов, которые необходимо преодолеть для продвижения вперед..."

**Major Issues:**
- ❌ Confused "metamorphic" with "Metroid" (video game!)
- ❌ Mixed in Castlevania references
- ❌ Completely wrong context (gaming vs software testing)
- ❌ Hallucinated about "screens" and "levels"

**Verdict:** Unusable. Model too small / not instruction-tuned well.

---

### 2. qwen2.5:14b — ✅ GOOD (8/10)

**Response:**
> "Метаморфное тестирование (Metamorphic Testing) — это метод тестирования программного обеспечения, который фокусируется на преобразовании данных input/output между различными системами или состояниями..."

**Pros:**
- ✅ Correct context (software testing)
- ✅ Clear Russian explanation
- ✅ Mentions key concepts (data transformation, integrity)
- ✅ Practical examples (REST API, microservices)

**Cons:**
- ⚠️ A bit verbose
- ⚠️ Some repetition

**Verdict:** Good for Russian text. Fast and reliable.

---

### 3. deepseek-r1:14b — ✅✅ EXCELLENT (9/10)

**English Response:**
> "Metamorphic testing is a software testing technique that leverages the transformation of existing test cases to generate new ones, ensuring consistent program behavior across all variations."

**Key Concepts:**
1. **Test Cases as Inputs**
2. **Transformation Functions**
3. **Consistent Behavior**
4. **Black-Box Testing**

**Pros:**
- ✅ Structured, academic style
- ✅ Clear definitions
- ✅ Lists benefits & use cases
- ✅ Professional formatting

**Cons:**
- ⚠️ English only (you asked in Russian)

**Verdict:** Best quality for technical content.

---

### 4. llama3.3:70b — ✅✅✅ TOP (10/10)

**Russian Response:**
> "Метаморфное тестирование (Metamorphic Testing) - это подход к тестированию программного обеспечения, который предполагает использование нескольких входных данных для проверки соответствия выходных результатов ожидаемому поведению..."

**Pros:**
- ✅ **Excellent Russian** (structured, clear)
- ✅ Comprehensive (3 key concepts + examples)
- ✅ Best reasoning quality
- ✅ Lists use cases (scientific, finance, ML)
- ✅ Handles complex topics perfectly

**Cons:**
- ⚠️ Needs 64GB RAM (you have it on PC-224!)
- ⚠️ Only ~5GB VRAM used (RTX 3060 12GB), rest ~35GB loaded to system RAM
- ⚠️ 70% system RAM usage → slow response times (~30s-1min per answer)
- ⚠️ Slower than smaller models

**Verdict:** Best overall INCLUDING Russian, but slow on 12GB VRAM. Requires 64GB RAM + sufficient VRAM for speed.

---

### 5. mistral-nemo:latest — ✅ GOOD (7/10)

**Response:**
> "Метаморфное тестирование — это вид тестового дизайна, при котором тестовые случаи разрабатываются на основе ожидаемых результатов. Такое название связано с тем, что тесты проверяют, как системное поведение трансформируется (metamorphoses) в разных условиях..."

**Pros:**
- ✅ Correct context (software testing)
- ✅ Russian language
- ✅ Mentions key concepts (properties, transformations)
- ✅ Gives example (associativity property)
- ✅ Lists pros & cons

**Cons:**
- ⚠️ Grammatical issues ("Propertiesproperty" repeated)
- ⚠️ Verbose
- ⚠️ Less structured than deepseek-r1
- ⚠️ Example could be clearer

**Verdict:** Decent Russian explanation, but qwen2.5:14b is clearer.

---

## Comparison Table

| Model                    | Size  | RAM Needed | Quality (1-10) | Speed       | Russian     | Best For                    |
| ------------------------ | ----- | ---------- | -------------- | ----------- | ----------- | --------------------------- |
| **llama3.1:8b-instruct** | ~5GB  | 8GB        | **2/10** ❌     | ⚡ Very Fast | Poor        | ❌ NOT recommended           |
| **mistral-nemo:latest**  | ~12GB | 16GB       | **7/10** ✅     | ⚡ Fast      | ✅ Decent    | Russian text (decent)       |
| **qwen2.5:14b**          | ~9GB  | 16GB       | **8/10** ✅     | ⚡ Fast      | ✅ Good      | Russian text, daily tasks   |
| **deepseek-r1:14b**      | ~9GB  | 16GB       | **9/10** ✅✅    | ⚡ Fast      | ⚠️ English  | Technical docs, analysis    |
| **llama3.3:70b**         | ~40GB | **64GB**   | **10/10** ✅✅✅  | 🐢 Slow     | ✅ Excellent | Complex tasks, best quality |

---

## Hardware Fit for YOU

| Device | RAM | Can Run 70b? | Recommended Model |
|--------|-----|--------------|---------------------|
| **PC-224** (Threadripper 1920X) | **64GB** | ✅ **YES** | **llama3.3:70b** (best) |
| **MacBook Pro** | 16GB | ❌ NO | **qwen2.5:14b** or **deepseek-r1:14b** |
| **Windows Laptop** | 16GB | ❌ NO | **qwen2.5:14b** |

---

## Recommendations

### For PC-224 (64GB RAM):
```bash
# ⚠️ NOT for daily use (uses 70% RAM, slow ~30s-1min)
ollama run llama3.3:70b --gpu  # Only for special tasks

# ✅ Daily drivers (fast, efficient)
ollama run qwen2.5:14b "вопрос"   # Russian
ollama run deepseek-r1:14b "question"  # English
```

### For MacBook (16GB, remote via ZeroTier):
```bash
# Already working
export OLLAMA_HOST=http://10.24.175.30:11434
ollama run qwen2.5:14b "вопрос"   # Russian
ollama run deepseek-r1:14b "question"  # English
```

### For Daily Use:
- **Russian text:** `qwen2.5:14b` ✅ (fast, clear)
- **English technical:** `deepseek-r1:14b` ✅✅ (structured)
- **Best quality (rare tasks only):** `llama3.3:70b` ⚠️ (slow, heavy)

**Bottom line:** 70b gives best quality but **cannot be used constantly** — use 14b models for daily work.

---

## Session Update

**Tested Models:**
1. ❌ `llama3.1:8b-instruct` — confused metamorphic with Metroid game
2. ✅ `mistral-nemo:latest` — decent Russian, verbose
3. ✅ `qwen2.5:14b` — good Russian explanation
4. ✅✅ `deepseek-r1:14b` — excellent English structure
5. ✅✅✅ `llama3.3:70b` — best quality (needs 64GB RAM)

**Rankings (Russian answers):**
1. **llama3.3:70b** (10/10) — best quality, comprehensive ✅✅✅
2. **qwen2.5:14b** (8/10) — clear, concise ✅
3. **mistral-nemo:latest** (7/10) — decent but verbose ⚠️
4. **llama3.1:8b-instruct** (2/10) — wrong (Metroid game!) ❌

**Key Learning:**
- Small models (8b) hallucinate badly on technical terms
- 14b models are sweet spot for daily use
- 70b gives best quality BUT:
  - Uses 70% system RAM + only 5GB VRAM (RTX 3060 12GB)
  - Slow response (~30s-1min) → **cannot be used constantly**
  - Reserve for rare, high-quality tasks only
- Mistral-nemo is okay but qwen2.5:14b is better for Russian

---

**Tags:** #ModelComparison #Ollama #MetamorphicTesting #Hardware  
**Related:** [[HARDWARE_SPEC.md]] [[qa-ai-transition-guide]]

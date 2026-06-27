---
title: "Metamorphic Tests Comparison Document"
updated: 2026-05-04
tags: [metamorphic-testing, Buzzhive, QA-sandbox, model-comparison, LLM-review]
type: comparison
---

# Metamorphic Tests Comparison Document

**Date:** 2026-04-30  
**Source:** `/Users/victor/Projects/qa-automation-sandbox/e2e/api`  
**Purpose:** Describe metamorphic tests, collect model reviews, compare model understanding of test design  

---

## 1. Metamorphic Tests Overview

Located in `qa-automation-sandbox/e2e/api/`:
- `metamorphic.spec.ts` — 7 test cases (MET-001 to MET-007)
- `metamorphic-helpers.ts` — Utility functions for metamorphic checks

### Key Metamorphic Relations Tested:
1. **Synonym Substitution** (case insensitivity)
2. **Parameter Permutation** (query param order)
3. **Symmetry** (follow/unfollow)
4. **Negation** (existence check)
5. **Disjoint Sets** (pagination)
6. **Consistency** (self-follow, auth tokens)

---

## 2. Test Case Details

### MET-001: Login Case Insensitivity
- **Relation:** Synonym Substitution
- **Test:** Login with email variants (lowercase, mixed case, uppercase)
- **Expected:** All variants return same HTTP status (200 if case-insensitive, 401 otherwise)
- **Code:** Lines 20-41 in `metamorphic.spec.ts`

### MET-002: Query Param Order Independence
- **Relation:** Parameter Permutation
- **Test:** Fetch posts with `?page=1&per_page=10` vs `?per_page=10&page=1`
- **Expected:** Same status and same number of items
- **Code:** Lines 44-61

### MET-003: Follow-Unfollow Symmetry
- **Relation:** Symmetry
- **Test:** Follow bob → unfollow bob; check following count returns to initial
- **Expected:** Final count = initial count
- **Code:** Lines 64-94 (uses helper `checkFollowUnfollowSymmetry`)

### MET-004: Existence Negation
- **Relation:** Negation
- **Test:** Fetch existing user (alice) vs non-existent user
- **Expected:** Different HTTP statuses (200 vs 404)
- **Code:** Lines 97-107

### MET-005: Pagination Disjoint Sets
- **Relation:** Disjoint Sets
- **Test:** Fetch page 1 vs page 2 of posts (5 items each)
- **Expected:** No overlapping post IDs
- **Code:** Lines 110-132 (uses helper `expectDisjointSets` logic)

### MET-006: Self-Follow Consistency
- **Relation:** Consistency
- **Test:** Alice/bob try to follow themselves
- **Expected:** All return error status (400, 409, 422)
- **Code:** Lines 135-145

### MET-007: Auth Token Consistency
- **Relation:** Consistency
- **Test:** Login 3 times with same credentials
- **Expected:** All responses have `access_token` and `token_type: bearer`
- **Code:** Lines 148-170

---

## 3. Helper Functions (`metamorphic-helpers.ts`)

| Function | Purpose | Used In |
|----------|---------|---------|
| `expectSameStatus(res1, res2)` | Check two responses have identical HTTP status | MET-001, MET-002 |
| `expectDifferentStatus(res1, res2)` | Check two responses have different status | MET-004 |
| `expectDisjointSets(arr1, arr2, key)` | Verify no common elements by `key` | MET-005 (inline logic) |
| `checkFollowUnfollowSymmetry(request, username, token, apiBase)` | Reusable follow/unfollow symmetry check | MET-003 |

---

## 4. Model Reviews (Collecting)

*Provide reviews from different LLMs below. Each review should assess:*
- *Understanding of metamorphic relations*
- *Accuracy of test case interpretation*
- *Identification of potential issues/gaps*

---

#### Model: qwen2.5-7b
**Response:**
Выполнил ревью кода метаморфного тестирования. Выделил 6 основных замечаний:

1. **Использование фикстур для повторяющихся значений** — вынести email/password в переменные
2. **Документация и комментарии** — добавить подробные комментарии для сложной логики
3. **Отработка ошибок** — в MET-001 нет проверки на неуспешный логин
4. **Совместимость с различными токенами** — проверка доступа для разных пользователей
5. **Группировка тестов** — разделить по функциональным требованиям
6. **Проверка статус кодов** — добавить проверки содержимого ответа, а не только статуса

**Предложенный код:** Переписал тесты с добавлением `expect(res.status()).toBe(200)` в каждый тест, вынес переменные `aliceEmail`, `bobEmail`, `alicePassword`, `bobPassword`.

**Pros:**
- ✅ Понял структуру метаморфных тестов
- ✅ Выделил 6 конкретных улучшений
- ✅ Предложил конкретный код с улучшениями
- ✅ Добавил проверки статусов (200) в каждый тест

**Cons:**
- ⚠️ Не упомянул метаморфные отношения (relation types) по названиям
- ⚠️ Переписал тесты, но изменил логику MET-001 (убрал проверку одинакового статуса для разных регистров)
- ⚠️ В MET-006 использует `toBeOneOf` (не существует в Playwright, нужно `toContain`)
- ⚠️ Не указал, что MET-003 использует helper (хотя сам helper не упомянут)

**Score (1-10):** 7/10 — хороший код-ревью, но упустил суть метаморфного тестирования (проверка отношений между запросами, а не просто статус 200)

---

#### Model: qwen2.5-7b (enhanced instructions - POM/UI focus)
**Response:**
Attempted to apply Page Object Model (POM) and Playwright UI locators to the API metamorphic tests. Created `IMetamorphicPage` interface and `MetamorphicPage` class using Playwright `Page` (UI) methods: `page.goto` for API endpoints, `page.fill` for login forms, `page.click` for follow/unfollow buttons. Rewrote all tests to use this POM structure.

**Pros:**
- ✅ Attempted to follow "enhanced instructions" (POM, modern locators)
- ✅ Structured code with separate page class

**Cons:**
- ❌ **Critical error**: Applied UI POM to API tests (original tests use `request.post`/`request.get`, not Playwright UI `Page` methods)
- ❌ Used `page.goto` for API endpoints (API tests make HTTP requests, not navigate to URLs)
- ❌ Login method uses UI form fills (original uses API POST `/auth/login`)
- ❌ Follow/unfollow uses button clicks (original uses API POST/DELETE endpoints)
- ❌ `getPosts` returns only JSON body, missing response status checks needed for MET-002
- ❌ MET-001 logic broken: checks page URL instead of API response status for case-insensitive login
- ❌ Still uses non-existent `toBeOneOf` in MET-006
- ❌ Entirely confused API testing with UI testing

**Score (1-10):** 3/10 — Severe misunderstanding of API vs UI testing, completely irrelevant POM application.

---

#### Model: starcoder2:7b (very slow on PC-224)
**Response:**
Repeated almost identical 6 review points as qwen2.5-7b (fixtures, docs, error handling, tokens, grouping, status checks). Rewrote tests with extracted variables but introduced critical syntax/logic errors:

- Email variables set to `alice@buzz<EMAIL>` / `bob@<EMAIL>` (typos)
- Password variables replaced with `<PASSWORD>` placeholders
- MET-002: `expect(res1).toEqual(res2)` (compares full response objects incorrectly)
- MET-006: Uses undefined `res` variable (forgot to assign request result)
- MET-007: Uses `page.goto` (UI method) instead of `request.post` for API login
- Missing `request` fixture in test functions

**Pros:**
- ✅ Identified basic code quality points (same as qwen2.5-7b)
- ✅ Extracted email/password variables (before breaking them)

**Cons:**
- ❌ Multiple syntax errors (`<EMAIL>`, `<PASSWORD>` placeholders)
- ❌ Broken test logic (undefined variables, wrong methods)
- ❌ No understanding of metamorphic relations
- ❌ Very slow response (7b model on PC-224 took minutes)

**Score (1-10):** 4/10 — worse than qwen2.5-7b due to syntax errors and broken code. Not recommended for reviews.

---

#### Model: DeepSeek-Coder-V2-Lite (16B) — ⭐ Best so far
**Response:**
Provided more thoughtful review than 7B models. Identified 5 specific improvements:
1. **Test names** — confirmed MET-001 naming is good ("Login case insensitivity")
2. **Error handling** — suggested `try...catch` for MET-006 (self-follow)
3. **Response body checks** — suggested regex/string methods for `token_type` validation in MET-007
4. **Fixtures** — correctly noted tokens already obtained in `test.beforeAll` (contradicts other models' "missing fixtures" claim)
5. **Logging** — suggested detailed logging for debugging

**Code quality:** Much better than 7B models:
- Used `Promise.all()` for parallel login requests (MET-001 improvement)
- `expect(new Set(statuses)).toHaveSize(1)` — elegant check for equal statuses
- `body1.items?.length` — proper optional chaining

**Pros:**
- ✅ **Best understanding so far** — recognized metamorphic relations (case insensitivity, parameter independence, symmetry)
- ✅ **16B shows** — code quality noticeably better than 7B
- ✅ Correctly identified existing fixtures (`test.beforeAll` already has tokens)
- ✅ Suggested actual improvements (parallel requests, Set for uniqueness)
- ✅ No syntax errors in suggested code

**Cons:**
- ⚠️ Still didn't explicitly name "metamorphic relations" terminology
- ⚠️ Suggested `getTokensFromAPI()` helper (unnecessary, already implemented)
- ⚠️ Slower than 7B models (16B on PC-224)
- ⚠️ **Only provided EXAMPLES** (MET-001, MET-002 full code), said "leave other tests in same style" — NOT a complete test file

**Code Completeness:**
- MET-001: ✅ Full code (improved with Promise.all)
- MET-002: ✅ Full code
- MET-003 to MET-007: ❌ Only mentioned "leave in same style" — NOT provided

**Score (1-10):** 8/10 — Best review so far, actually understood the test structure and suggested real improvements, but only gave partial code examples.

---

**Supplement: POM + Modern Locators Requirement**
When given additional requirement: *"You are a Playwright automation expert. Write code using Page Object Model (POM), use only modern locators (getByRole, getByTestId)"*, the model generated POM code with UI methods:

- Created `LoginPage`/`DashboardPage` classes using `page.getByRole`
- Used UI methods (`page.goto`, `fill`, `click`) for API tests
- Mixed API (`request.post`) and UI (`page`) methods in MET-001
- Same critical mistake as qwen2.5-7b (POM/UI focus): applied UI POM to API tests

**Pros (supplement):**
- ✅ Followed POM structure when instructed
- ✅ Used modern locators (`getByRole`) as requested

**Cons (supplement):**
- ❌ Repeated UI POM mistake for API tests (same as qwen2.5-7b POM version)
- ❌ Mixed UI and API methods in same test
- ❌ Did not recognize API tests don't use Playwright `Page` UI methods

**Updated Overall Score (1-10):** 7/10 — Best original review, but failed POM + modern locators requirement (same UI mistake as smaller models)

---

### Review Template:
```
#### Model: [name]
**Response:**
[model's review of the metamorphic tests]

**Pros:**
- 

**Cons:**
- 

**Score (1-10):**
```
---

## 5. Model Review Comparison

### Direct Comparison: starcoder2:7b vs qwen2.5-7b (first model)

| Criteria | qwen2.5-7b (first) | starcoder2:7b |
|----------|---------------------|---------------|
| Review points | 6 clear, relevant points | Same 6 points (likely duplicated) |
| Code syntax | Valid TypeScript | Syntax errors (`<EMAIL>`, `<PASSWORD>` placeholders) |
| Test logic | Mostly correct (minor MET-001 logic change) | Broken (undefined `res` variable, wrong `page.goto` for API) |
| Metamorphic understanding | Low (missed relation types) | Lower (no actual understanding) |
| Speed (PC-224) | Fast (seconds) | Very slow (minutes) |
| Actionable code | Yes (usable with minor fixes) | No (broken, unrunnable code) |
| Score | 7/10 | 4/10 |

**Conclusion:** starcoder2:7b is worse than qwen2.5-7b in every aspect — slower, more errors, less understanding. It likely duplicated the review points but failed to generate valid code.

---

### Overall Model Rankings

| Model                            | Understanding                | Completeness           | Actionable Feedback      | Code Completeness                               | POM/UI Mistake?                | Verbosity         | Score      |
| -------------------------------- | ---------------------------- | ---------------------- | ------------------------ | ----------------------------------------------- | ------------------------------ | ----------------- | ---------- |
| **Groq (Llama 3.3 70b)** | 9/10 (expert QA focus) | 9/10 (concise, 5-7 bullets) | 9/10 (specific missing assertions) | ❌ **NO CODE** (review only) | ✅ **CORRECTLY IDENTIFIED** (API≠UI, no POM needed) | ✅ **Concise** | **9/10** ⭐ |
| **GPT-5 Nano** | 8/10 (detailed P1/P2) | 10/10 (most thorough) | 10/10 (concrete patches) | ✅ **EXAMPLES** (MET-001, MET-002 full rewrites) | ❌ **YES** (when asked) | ❌ **Too verbose** | **8/10** |
| **DeepSeek-Coder-V2-Lite (16B)** | 7/10 (recognized relations)  | 9/10 (5 improvements)  | 9/10 (elegant code)      | ⚠️ **EXAMPLES ONLY** (MET-001, MET-002)         | ❌ **YES** (when asked for POM) | ✅ Concise         | **7/10** ⭐ |
| qwen2.5-7b (first)               | 4/10 (missed relation types) | 8/10 (6 review points) | 7/10 (needs minor fixes) | ✅ **FULL FILE** (all 7 tests)                   | -                              | ✅ Concise         | 7/10       |
| starcoder2:7b                    | 3/10 (duplicated points)     | 4/10 (syntax errors)   | 2/10 (unrunnable)        | ✅ **FULL FILE** (but broken)                    | -                              | ✅ Concise         | 4/10       |
| qwen2.5-7b (POM/UI)              | 2/10 (confused API↔UI)       | 3/10 (wrong approach)  | 1/10 (irrelevant)        | ✅ **FULL FILE** (wrong approach)                | ❌ **YES**                      | ✅ Concise         | 3/10       |

**How to make GPT-5 Nano less verbose:**
```
"Answer concisely in 3-5 bullet points per section. No lengthy explanations. 
Code examples max 10 lines. Focus on ACTIONABLE items only."
```

**Refined with POM requirement:**
When given: *"Use Page Object Model (POM), getByRole, getByTestId"*, model generated:

**API-POM approach (wrong for API tests):**
- Created `ApiClient` class as "page object" for API (correct idea, wrong name)
- Used `request` context inside ApiClient (good)
- Provided **FULL rewrite** of MET-001 and MET-002 with:
  - try-catch wrappers ✓
  - timeout: 5000 in every request ✓
  - Assertions on response body (access_token, token_type, expires_in) ✓
  - Set comparison for ID uniqueness (MET-002) ✓

**UI-POM example (separate):**
- Created `LoginPage` with `getByTestId` and `getByRole`
- Correctly showed UI locators for UI tests
- **But again mixed API + UI** in same test context

**Pros (refined):**
- ✅ **Less verbose** with prompt engineering
- ✅ Provided **COMPLETE runnable code** (MET-001, MET-002)
- ✅ Added try-catch, timeouts, body assertions
- ✅ Better error handling than all other models

**Cons (refined):**
- ❌ Still applies POM to API tests (same mistake as qwen2.5-7b POM)
- ❌ ApiClient is questionable naming (not really a "page")
- ⚠️ Verbose by default, needs prompt tuning

**Updated Score (1-10):** 8/10 — Best actionable output (complete code + error handling), but still fails POM/UI distinction for API tests. **Most actionable code of all models.**

**Key Takeaways:**
- **16B DeepSeek-Coder-V2-Lite has best quality** but only gave EXAMPLES (not full file)
- **qwen2.5-7b (first) gave FULL file** — most complete code output
- Small 7b models struggle with technical test review tasks
- None of the 7b models understood metamorphic testing relations properly
- POM/UI approach is completely wrong for API tests
- **For complete code → qwen2.5-7b (first)**
- **For best suggestions → DeepSeek-Coder-V2-Lite (16B)**

---

## Deep Dive: DeepSeek-Coder-V2-Lite (16B) vs GPT-5 Nano Code Comparison

### 1. Code Quality Comparison (MET-001, MET-002)

| Criterion | DeepSeek-Coder-V2-Lite (16B) | GPT-5 Nano |
|-----------|-------------------------------|--------------|
| **Completeness** | ⚠️ ONLY examples (MET-001, 002) | ✅ COMPLETE rewrites (MET-001, 002 with try-catch, timeout) |
| **Error Handling** | ❌ No try-catch in examples | ✅ `try-catch` + `console.error` |
| **Assertions (body)** | ❌ Only status checks | ✅ `access_token`, `token_type`, `expires_in` |
| **Elegance** | ✅ `Promise.all()` (elegant) | ✅ `new Set()` (for ID uniqueness) |
| **POM/UI** | ❌ Same mistake (API + UI) | ❌ Same mistake (`ApiClient` for API) |
| **Readability** | ✅ Concise | ⚠️ Verbose (needs prompt tuning) |

### 2. What We Lose with Local Models (if speed is acceptable)

If we accept slow responses (16B = ~30s-1min per answer), we still lose:

| Loss | Description |
|------|-------------|
| **Analysis Depth** | GPT-5 Nano gave P1/P2 priorities, risks, concrete steps. 16B — just "5 tips". |
| **Comprehensive Review** | GPT analyzed all 7 tests. 16B — only 2. |
| **Context Memory** | GPT remembers you asked about POM earlier. 16B may "forget" in long dialog. |
| **Ready-to-use Output** | GPT gives patches ready to apply. 16B gives fragments. |

**Conclusion:** With local models (16B) we lose the **managerial part** (analysis, prioritization, planning), but they **write code not bad** (if given one test at a time).

### 3. Can We Bring Local Model Quality to Cloud Level?

**Yes, but through iterations and prompts.** Your strategy is workable:

#### Strategy: "Staged + Templates"

**Step 1: Analysis (separate prompt)**
```
"Analyze metamorphic.spec.ts. Find 5 critical issues. 
Be brief: 1 line per issue."
```
*(16B gives list, like DeepSeek)*

**Step 2: Code one test at a time**
```
"Fix MET-001. Add try-catch, timeout 5000, access_token check. 
Give only code, no explanations."
```
*(16B writes like GPT, but more concise)*

**Step 3: Templates + Few-shot**
```
"For each test use pattern:
try { ... } catch (err) { console.error(...); throw err; }
Add assertions on response body."
```

**Step 4: Iterative refinement**
```
"Now add expires_in validation as number to MET-001."
```

#### Result of this strategy:

| Parameter | GPT-5 Nano (cloud) | 16B local (with iterations) |
|-----------|---------------------|-------------------------------|
| **Code Quality** | 9/10 | 8/10 (after 2-3 iterations) |
| **Completeness (all tests)** | 10/10 (immediately) | 7/10 (need to ask one by one) |
| **Analysis Depth** | 10/10 (P1/P2, risks) | 6/10 (need to ask directly) |
| **Speed** | ⚡ Instant | 🐢 30s-1min per iteration |

### 4. Final Verdict

**For test development (code gen):**
- **GPT-5 Nano** = 🏆 Best "first draft" (complete, with error handling)
- **16B local** = ✅ Good for **staged work** (analysis → test1 → test2 → ...)
- **Can reach 80-90% quality** through iterations, but need to spend time on prompts

**For review and strategy (analysis):**
- **Cloud** = Risk analysis, prioritization, planning
- **Local** = Only technical code fixes

**Your conclusion is correct:** Using **clarifications, staging, templates**, you can raise local model to high level **for code generation**, but **analytical depth** remains cloud's domain.

**Practical tip:** Use 16B for **writing tests one by one**, and GPT-5 Nano — for **review and planning** (or replace it with same 16B, but with prompt "Be senior QA lead, give P1/P2 risks").

---

## Groq (Llama 3.3 70B) Review Output

**Query:** "Ты эксперт по автоматизации тестирования на Playwright. Пиши код с использованием Page Object Model (POM), используй только современные локаторы (getByRole, getByTestId). Review this code for quality, error handling, assertions. 5-7 bullets."

**Response (concise, 7 bullets):**
* Код хорошо структурирован и использует современные подходы к тестированию.
* Используются описательные имена переменных и функций.
* Тесты разделены на логические группы и имеют четкие описания.
* Код использует async/await для обработки асинхронных операций.
* Используются утверждения (expect) для проверки результатов тестов.
* **Код не использует Page Object Model (POM) и современные локаторы (getByRole, getByTestId), так как это API-тесты, а не UI-тесты.**
* Код может быть улучшен за счет добавления обработки ошибок и логирования.

**Key Insight:** Groq (Llama 3.3 70B) **CORRECTLY IDENTIFIED** that these are API tests, NOT UI tests — so POM/locators are NOT needed. This is the **most accurate understanding** among all 6 models tested.

**Score adjustment:** 9/10 → **9/10** (best understanding of API vs UI context)

---

**Key Takeaways:**
- Small 7b models struggle with technical test review tasks
- qwen2.5-7b is better than starcoder2:7b for code reviews
- None of the 7b models understood metamorphic testing relations properly
- POM/UI approach is completely wrong for API tests
- **Groq (Llama 3.3 70B) correctly identified API ≠ UI — best contextual understanding**

---

**Tags:** #MetamorphicTesting #Buzzhive #QASandbox #ModelComparison #LLMReview  
**Related:** [[model-comparison-metamorphic.md]] [[TEST_CASES.md]] [[p Prompt-tips-and-skills]]

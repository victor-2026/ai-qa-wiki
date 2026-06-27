# Plan: Create Obsidian Bases for QA Wiki

**Date:** 2026-05-04  
**Location:** `/Users/victor/Projects/ai-qa-wiki/`  
**Skill:** obsidian-bases  

---

## 1. Current State

### Existing Files
- **Wiki topics:** 25+ `.md` files in `wiki/`
- **No frontmatter** (no tags, categories, dates in most files)
- **No `.base` files** yet (blank slate)
- **Links exist:** `[[wiki/test-management]]` style wikilinks

### Key Files to Surface in Bases
| File | Topic | Needs Frontmatter? |
|------|-------|---------------------|
| `qa-ai-transition-guide.md` | Career transition | ✅ Yes (date, tags) |
| `ai-testing-glossary.md` | Glossary (A-Z terms) | ✅ Yes (letter, category) |
| `mas-testing-framework.md` | MAS architecture | ✅ Yes (framework type) |
| `testing-strategies.md` | Strategies | ✅ Yes (strategy type) |
| `model-comparison-metamorphic.md` | LLM comparisons | ✅ Yes (date, model names) |
| `metamorphic-tests-comparison.md` | Test reviews | ✅ Yes (date, models reviewed) |

---

## 2. Proposed Bases

### Base 1: `wiki-topics.base` — Table View
**Purpose:** Overview of all wiki topics with metadata

**Columns:**
- `File` (name)
- `Topic` (from heading 1)
- `Last Updated` (from file or frontmatter)
- `Tags` (frontmatter)
- `Has Links` (wikilinks count)

**Filter:** Files in `wiki/` folder

---

### Base 2: `glossary.base` — Card View
**Purpose:** Browse AI Testing Glossary terms

**Columns:**
- `Term` (from heading 3 `###`)
- `Definition` (first paragraph)
- `Letter` (A, B, C... from term)
- `Related` (wikilinks)

**Filter:** File = `ai-testing-glossary.md`

---

### Base 3: `model-reviews.base` — Table View
**Purpose:** Track LLM model reviews and scores

**Columns:**
- `Model Name`
- `Test Type` (metamorphic, general QA, etc.)
- `Score` (1-10)
- `Date Reviewed`
- `Speed` (fast/medium/slow)
- `Russian Quality` (1-10)

**Source:** `model-comparison-metamorphic.md`, `metamorphic-tests-comparison.md`

---

## 3. Prerequisites (TODO First)

### Add Frontmatter to Key Files
```yaml
---
title: "QA Skills → AI Roles Transition Guide"
updated: 2026-05-01
tags: [career, transition, AI, QA]
type: guide
---
```

**Files needing frontmatter (6 total):**
1. `wiki/qa-ai-transition-guide.md`
2. `wiki/ai-testing-glossary.md`
3. `wiki/mas-testing-framework.md`
4. `wiki/testing-strategies.md`
5. `model-comparison-metamorphic.md`
6. `metamorphic-tests-comparison.md`

---

## 4. Implementation Steps

### Step 1: Add Frontmatter (6 files)
- Use Edit tool to add YAML frontmatter at top of each file
- Include: `title`, `updated`, `tags`, `type`

### Step 2: Create `wiki-topics.base`
- Use obsidian-bases skill
- Table view, filter on `wiki/` path
- Columns: File, Topic, Tags, Updated

### Step 3: Create `glossary.base`
- Card view for glossary terms
- Filter on `ai-testing-glossary.md`
- Group by Letter

### Step 4: Create `model-reviews.base`
- Table view for model comparisons
- Source from comparison markdown files
- Columns: Model, Score, Speed, Russian Quality

---

## 5. Skills Needed

✅ **obsidian-bases** skill loaded  
✅ **obsidian-markdown** skill (for frontmatter)  
✅ **obsidian-cli** (to verify Bases in vault)  

---

## 6. Time Estimate

| Task | Time |
|------|------|
| Add frontmatter (6 files) | 10 min |
| Create `wiki-topics.base` | 5 min |
| Create `glossary.base` | 5 min |
| Create `model-reviews.base` | 5 min |
| **Total** | **~25 min** |

---

## 7. Next Action

**Option A:** Start adding frontmatter now (prerequisite)  
**Option B:** Wait for DeepSeek-Coder-V2-Lite (16B) review, then do Bases  
**Option C:** Close session, leave plan for next time  

---

**Tags:** #ObsidianBases #Planning #QAWiki #AIQAWiki  
**Related:** [[metamorphic-tests-comparison.md]] [[model-comparison-metamorphic.md]]

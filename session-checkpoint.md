# Session Checkpoint — AI QA Wiki

**Updated:** 2026-04-30

---

## Project Goal

Build AI QA knowledge base from "Software Testing with Generative AI" book:
- Process chapters into Q&A using Groq API
- Verify with Gemini feedback
- Prepare for Windows-based deployment with Ollama + BGE-M3 + Qdrant

---

## Current State

| Component | Status |
|-----------|--------|
| **Chapters** | ✅ 11/12 done (ch01 skip) |
| **QA** | ✅ 198 questions |
| **Groq API** | ✅ Working |
| **Gemini feedback** | ✅ Applied (ch02, ch05-12) |
| **PDF Guide** | ✅ ai-native-qa-strategy-2026.pdf |
| **Mind Map** | ✅ mind-map-ai-qa-2026.png |
| **Backup** | ✅ Created |
| **ZeroTier VPN** | ✅ Configured (MacBook ↔ Windows .224) |
| **Ollama Remote** | ✅ Access via ZeroTier (10.24.175.30:11434) |
| **Transition Guide** | ✅ qa-ai-transition-guide.md updated |

---

## Plans

| Priority | Task | Status |
|----------|------|--------|
| 🔴 High | Windows PC (Threadripper) подключить | ⏳ Waiting |
| 🔴 High | Ollama + BGE-M3 + Qdrant | After PC |
| 🟡 Med | MAS Pipeline (qa-automation-sandbox) | ✅ Done |
| 🟢 Low | GitHub Pages deploy | Optional |
| 🟡 Med | Implement metamorphic tests (qa-automation-sandbox) | 🔧 Todo |
| 🟡 Med | Add promptfoo eval suite | 🔧 Todo |
| 🟡 Med | Create red-teaming tests | 🔧 Todo |

---

## Technical Debt

| Item | Notes |
|------|-------|
| **session-checkpoint.md** | ✅ Updated 2026-04-23 |
| **RAG pipeline** | Option A done (JSON), Option B pending |
| **wiki_qa.py** | Needs Ollama support |

---

## New Project: MAS-Realisation

Created: `/Users/victor/Projects/MAS-realisation/`

### Status

| Component | Status |
|-----------|--------|
| **Economy variant** | ✅ Tested |
| **Balance variant** | ✅ Tested |
| **RAG (Option A)** | ✅ Implemented |
| **Windows Ollama** | ✅ Connected (192.168.1.31) |
| **Strict Critic** | ✅ Updated |

### Files

| File | Purpose |
|------|---------|
| economy_pipeline.py | 1 model pipeline |
| balance_pipeline.py | 2 model pipeline |
| known_patterns.json | 8 error patterns |
| learned_patterns.json | Auto-learned (on REJECT) |
| SESSION_REPORT.md | Full session report |

---

## Windows Ollama Status

| Parameter | Value |
|-----------|-------|
| **.31 (local)** | 192.168.1.31:11434 |
| **.224 (remote)** | 192.168.1.224:11434 |
| **ZeroTier VPN** | ✅ 10.24.175.x network |
| **MacBook access** | ✅ 10.24.175.30:11434 |
| **Models** | qwen2.5:3b, deepseek-r1:7b/14b, llama3.2-vision |
| **Firewall** | ✅ Rules added |

---

## Backup Location

```
~/Backups/ai-qa-wiki/2026-04-23/
```

---

## Today's Work (2026-04-30)

### qa-automation-sandbox:
- ✅ Created `METAMORPHIC_TESTING.md` (guide + examples)
- ✅ Created `e2e/api/metamorphic.spec.ts` (7 relations)
- ✅ Created `e2e/api/metamorphic-helpers.ts`
- ✅ Added Stryker Mutator config (`stryker.conf.json`)
- ✅ CI fixed: `render-e2e` runs only smoke tests
- ✅ PR #3 merged to main

### ai-qa-wiki:
- ✅ Updated `qa-ai-transition-guide.md` with metamorphic/mutation testing
- ✅ Added Ollama answers (qwen2.5:3b, deepseek-r1:14b, Russian variants)
- ✅ Configured ZeroTier VPN (MacBook ↔ Windows .224)
- ✅ Ollama accessible remotely via ZeroTier (10.24.175.30:11434)
- ✅ Reviewed `Справочник_Windows_AI_QA_System.md` - kimi-k2.6:cloud in plans

### Router/Network:
- ✅ Asus RT-N56U B1 VPN Server configured (OpenVPN)
- ✅ ZeroTier network created (central.zerotier.com)
- ✅ Both devices authorized in ZeroTier
- ✅ KIMI-K2.6:cloud identified as planned model (32+ GB RAM needed)

---

## Next Session

1. Implement metamorphic tests in qa-automation-sandbox (Phase 1)
2. Add promptfoo eval suite to ai-qa-wiki
3. Create red-teaming tests for wiki_llm.py
4. RAG demo — show rag_lookup() on Windows PC

---

*Next session: Continue with RAG and review*
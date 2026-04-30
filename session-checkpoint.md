# Session Checkpoint — AI QA Wiki

**Updated:** 2026-04-30

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
- ✅ Added Ollama answers (qwen2.5:3b + deepseek-r1:14b) on metamorphic testing
- ✅ Added Russian variants of deepseek answers
- ✅ Configured ZeroTier VPN (MacBook ↔ Windows .224)
- ✅ Ollama accessible remotely via ZeroTier (10.24.175.30:11434)
- ✅ Reviewed `Справочник_Windows_AI_QA_System.md` - kimi-k2.6:cloud in plans
- ✅ Created `HARDWARE_SPEC.md` (PC-224: 64GB RAM, Threadripper 1920X, RTX 3060 12GB)
- ✅ Cloned Obsidian skills to `~/.opencode/skills/obsidian-skills/` (from kepano repo)

### Hardware:
- ✅ PC-224: 12-Core AMD Ryzen Threadripper 1920X, 64GB RAM, NVIDIA RTX 3060 (12GB)
- ✅ MacBook Pro: 16GB RAM, Intel (remote access via ZeroTier)
- ✅ Windows Laptop: 16GB RAM, Intel (old, standby)

### Router/Network:
- ✅ Asus RT-N56U B1 VPN Server configured (OpenVPN)
- ✅ ZeroTier network created (central.zerotier.com)
- ✅ Both devices authorized in ZeroTier
- ✅ KIMI-K2.6:cloud identified as planned model (32+ GB RAM needed, cloud model)
- ✅ Obsidian Skills setup for OpenCode (5 skills: markdown, bases, canvas, cli, defuddle)

---

## Current State

| Component | Status |
|-----------|--------|
| **Chapters** | ✅ 11/12 done (ch01 skip) |
| **Q&A** | ✅ 198 questions |
| **Groq API** | ✅ Working |
| **Gemini feedback** | ✅ Applied (ch02, ch05-12) |
| **PDF Guide** | ✅ ai-native-qa-strategy-2026.pdf |
| **Mind Map** | ✅ mind-map-ai-qa-2026.png |
| **Backup** | ✅ Created |
| **ZeroTier VPN** | ✅ Configured (MacBook ↔ Windows .224) |
| **Ollama Remote** | ✅ Access via ZeroTier (10.24.175.30:11434) |
| **Transition Guide** | ✅ qa-ai-transition-guide.md updated |
| **Hardware Spec** | ✅ HARDWARE_SPEC.md created |
| **Obsidian Skills** | ✅ Cloned to `~/.opencode/skills/` |

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
| 🟡 Med | Test Obsidian Skills in OpenCode | 🔧 Todo |

---

## Technical Debt

| Item | Notes |
|------|-------|
| **session-checkpoint.md** | ✅ Updated 2026-04-30 |
| **RAG pipeline** | Option A done (JSON), Option B pending |
| **wiki_qa.py** | Needs Ollama support |
| **Obsidian Skills** | 5 skills cloned, ready to test in OpenCode |

---

## Windows Ollama Status

| Parameter | Value |
|-----------|-------|
| **.31 (local)** | 192.168.1.31:11434 |
| **.224 (remote)** | 192.168.1.224:11434 |
| **ZeroTier VPN** | ✅ 10.24.175.x network |
| **MacBook access** | ✅ 10.24.175.30:11434 |
| **Models** | qwen2.5:14b, deepseek-r1:7b/14b, llama3.2-vision |
| **Firewall** | ✅ Rules added |

---

## Backup Location

```
~/Backups/ai-qa-wiki/2026-04-23/
```

---

## Next Session

1. Test Obsidian Skills in OpenCode (ask "What Obsidian skills do you have loaded?")
2. Implement metamorphic tests in qa-automation-sandbox (Phase 1)
3. Add promptfoo eval suite to ai-qa-wiki
4. Create red-teaming tests for wiki_llm.py
5. RAG demo — show rag_lookup() on Windows PC-224 (64GB RAM)
6. Test local models: llama3.3:70b (needs GPU), qwen2.5:14b, deepseek-r1:14b

---

*Next session: Continue with RAG and review*

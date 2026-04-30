# Hardware Specification - AI QA Projects

**Date:** 2026-04-30  
**Status:** Current Setup  

---

## Device Inventory

| Device | RAM | CPU | GPU | Storage | Role | Status |
|--------|-----|-----|-----|----------|------|--------|
| **PC-224** | 64GB | ? | ? | Main AI work (Ollama, models) | ✅ Active |
| **MacBook Pro** | 16GB | Intel | Integrated | Remote access, light work | ✅ Active |
| **Windows Laptop** | 16GB | Intel (old) | Integrated | Backup, light tasks | ⏳ Standby |

---

## PC-224 (Main Workstation)

### Current Setup:
- **OS:** Windows 10 Pro
- **RAM:** 64GB (supports large models: llama3.3:70b needs 64GB)
- **GPU:** 6GB video card (maybe RTX 3060 or similar)
- **Role:** 
  - Ollama server (qwen2.5:14b, deepseek-r1:14b, llama3.2-vision)
  - BGE-M3 embeddings server
  - Qdrant vector database
  - Docker (qa-automation-sandbox)

### Model Capacity:

| Model | Size | Fits? | Purpose |
|-------|------|-------|---------|
| **kimi-k2.6:cloud** | ~32GB+ | ☁️ Cloud only | Agentic coding |
| **llama3.3:70b** | ~40GB | ✅ Yes (64GB) | Q&A, Russian |
| **deepseek-r1:14b** | ~9GB | ✅ Yes | English tasks |
| **qwen2.5:14b** | ~9GB | ✅ Yes | Russian text |
| **llama3.2:3b** | ~2GB | ✅ Yes | Quick tests |

### Network:
- **Local IP:** 192.168.1.224
- **ZeroTier VPN:** 10.24.175.30 (accessible from MacBook)
- **Ollama API:** `http://192.168.1.224:11434`
- **Docker:** qa-automation-sandbox (backend, frontend, db)

---

## MacBook Pro (Remote Access)

### Specs:
- **Model:** MacBook Pro (Intel)
- **RAM:** 16GB
- **Role:**
  - Remote Ollama access via ZeroTier VPN
  - Light coding (OpenCode, VS Code)
  - Terminal access to Windows PC
  - Git operations

### Access Methods:
1. **ZeroTier VPN:** `10.24.175.x` network
2. **Ollama:** `export OLLAMA_HOST=http://10.24.175.30:11434`
3. **SSH/VPN:** Connects to PC-224

### Active Projects:
- `ai-qa-wiki` (wiki management)
- `qa-automation-sandbox` (remote testing)
- `Test-Dora-Plus` (DORA metrics)

---

## Windows Laptop (Backup)

### Specs:
- **RAM:** 16GB
- **CPU:** Intel (old 5th gen?)
- **Role:** Backup device, light tasks
- **Status:** Standby (not actively used)

---

## Network Architecture

```
┌─────────────────────────────────────────────┐
│                    Home Network                     │
│         (Asus RT-N56U B1 Router)                 │
│         External IP: 2a05:fc1:40:23c::3             │
├─────────────────────────────────────────────┤
│                 │                               │
│  ┌─────────────┐    ┌─────────────┐            │
│  │   PC-224    │    │  MacBook    │            │
│  │  192.168.1.224│    │  192.168.1.31│            │
│  │  (64GB RAM)  │    │  (16GB RAM) │            │
│  └─────┬───────┘    └──────┬──────┘            │
│        │                  │                   │
│        └──────────────────┘                   │
│                 │                               │
│         [ZeroTier VPN Network]                  │
│         (10.24.175.x)                         │
└─────────────────────────────────────────────┘
         │
         ▼
┌─────────────────┐
│   External     │
│   (MacBook LTE) │
└─────────────────┘
```

---

## Model Deployment Strategy

### PC-224 (Local Models):

| Model | Command | API Endpoint |
|-------|---------|---------------|
| **qwen2.5:14b** | `ollama run qwen2.5:14b` | `http://192.168.1.224:11434` |
| **deepseek-r1:14b** | `ollama run deepseek-r1:14b` | `http://192.168.1.224:11434` |
| **llama3.2-vision** | `ollama run llama3.2-vision` | `http://192.168.1.224:11434` |
| **llama3.3:70b** | `ollama run llama3.3:70b --gpu` | Needs GPU |

### Cloud Models (via Ollama Cloud):

| Model | Command | Notes |
|-------|---------|-------|
| **kimi-k2.6:cloud** | `ollama run kimi-k2.6:cloud` | Needs internet, ~32GB RAM in cloud |

---

## Obsidian Integration (Next Step)

### Resources:
- **Blog:** https://pimenov.ai/blog/ceo-obsidian-napisal-skilly-dlya-claude-code/
- **GitHub:** https://github.com/kepano/obsidian-skills
- **Skills:** obsidian-markdown, obsidian-bases, json-canvas, obsidian-cli, defuddle

### Setup Options:

| Option | Tool | How to Install |
|--------|------|-----------------|
| **1. Claude Code** | Anthropic CLI | `git clone https://github.com/kepano/obsidian-skills.git .claude/obsidian-skills` |
| **2. OpenCode** | Open-source alt | `git clone https://github.com/kepano/obsidian-skills.git ~/.opencode/skills/obsidian-skills` |
| **3. Codex CLI** | OpenAI tool | Similar to Claude Code, uses same `SKILL.md` format |

### Skills Structure:
```
obsidian-skills/
├── obsidian-markdown/
│   └── SKILL.md  # Wikilinks, callouts, frontmatter
├── obsidian-bases/
│   └── SKILL.md  # Database views, filters, formulas
├── json-canvas/
│   └── SKILL.md  # Mind maps, flowcharts
├── obsidian-cli/
│   └── SKILL.md  # CLI commands for vault operations
└── defuddle/
    └── SKILL.md  # Web content extraction to markdown
```

---

## Next Actions

### Hardware:
1. ✅ PC-224: 64GB RAM confirmed (supports 70b models)
2. ✅ MacBook: 16GB RAM (remote access working via ZeroTier)
3. ⏳ Windows Laptop: 16GB (standby, old Intel)

### Obsidian Skills Setup:
1. [ ] Choose tool: Claude Code vs OpenCode vs Codex CLI
2. [ ] Install skills to vault: `/Users/victor/Projects/ai-qa-wiki/`
3. [ ] Test: "What Obsidian skills do you have loaded?"
4. [ ] Verify: Skills auto-load and work with vault

### Model Optimization:
1. [ ] Test kimi-k2.6:cloud (requires internet)
2. [ ] Compare: deepseek-r1:14b vs qwen2.5:14b for Russian
3. [ ] GPU check: Use `--gpu` flag for 70b model on PC-224

---

**Tags:** #Hardware #AIInfrastructure #Obsidian #AgentSkills  
**Related:** [[Справочник_Windows_AI_QA_System]] [[qa-ai-transition-guide]]

# Obsidian Security Checklist

**Date:** 2026-06-24
**Source:** raw/obsidian-scam-audit-2026.md

## The Scam

Fake QA audit proposal via Telegram → Obsidian vault with shared credentials → malicious community plugins (Hider + Shell Commands) → remote code execution / data theft.

Full story: `raw/obsidian-scam-audit-2026.md`

## Risk Assessment by Plugin Type

| Plugin Type | Risk | Examples |
|-------------|------|----------|
| Shell execution | 🔴 Critical | Shell Commands, Custom Frames, any plugin with `child_process` |
| UI hiding | 🟡 Medium | Hider (can conceal malicious activity) |
| Scripting engines | 🟡 Medium | Templater (JS templates), Dataview (DQL) |
| Network access | 🟡 Medium | Any plugin making HTTP requests |
| Read-only queries | 🟢 Low | Dataview (default), Periodic Notes |
| Drawing/Diagrams | 🟢 Low | Excalidraw, Canvas |

## Defense Layers

### Layer 1: Before Opening Unknown Vaults

- [ ] Use a **sandbox** (VM, Docker container, or dedicated user account)
- [ ] **Never use someone else's Obsidian Sync account** — they control sync content
- [ ] **Disable community plugins** in sandbox before opening the vault
- [ ] **Check plugin list** before enabling anything: review `community-plugins.json`

### Layer 2: Plugin Verification

- [ ] Verify plugin on GitHub: stars, recent updates, code quality
- [ ] Check for known dangerous plugins: `obsidian-shell-commands`, `hider`
- [ ] Check plugin permissions: does it need `child_process`, network, file system access?
- [ ] **Enable plugins one at a time**, not all at once

### Layer 3: Restricted Mode

- [ ] Keep **Restricted Mode ON** by default
- [ ] Toggle OFF **only for trusted plugins** in trusted vaults
- [ ] Switch back to ON after installing/updating plugins

### Layer 4: Mobile Air Gap

- Shell Commands and similar plugins **do not work on mobile Obsidian**
- If you need to inspect a suspicious vault — use mobile as read-only viewer

### Layer 5: After Exposure

If you opened a vault with shared credentials:

- [ ] **Change passwords** immediately (Obsidian account, email, any reused passwords)
- [ ] **Revoke all sessions** (Obsidian Sync → "Log out of all devices")
- [ ] **Delete the shared account** (don't let scammer reuse it)
- [ ] **Scan for malware** (system-wide AV scan)
- [ ] **Rotate API keys and tokens** stored in vaults

## Automated Checks

A weekly script checks all vaults for dangerous plugins:

```bash
python3 ~/scripts/obsidian-security-check.py
```

**What it checks:**
- All `.obsidian/community-plugins.json` — known dangerous plugins (shell-commands, hider)
- Unknown or suspicious plugin IDs
- Restricted Mode status
- Sync configuration hygiene
- Report any anomalies

## Related

- `raw/obsidian-scam-audit-2026.md` — full story
- `wiki/obsidian-skills-kepano.md` — legitimate Obsidian usage

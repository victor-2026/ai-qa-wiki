# NanoMuse — Open-Source Personal Agent (Oct 2026, Watch Note)

**Sources (all fetched 2026-10-07):** https://github.com/nano-muse/nanoMuse · paper https://arxiv.org/abs/2610.08699 (released 2026-10-07) · site https://nanomuse.cn/
**Status:** product news, NOT evaluated. Pilot-candidate for W3 (tooling lane, W3 decides/owns). Not a matrix subject (agent product, not eval layer).

## Facts

- Open-source personal agent, **GPL-3.0-or-later**, released 2026-09-25; v0.1.41 (07.10); 208 stars / 25 forks / 800 commits at fetch time; CI badge + demo + Discord; 10-language README.
- Runs on Android/iPhone/desktop/Linux/browser; relay + self-host (`scripts/self-host.sh`, Docker); 18 model providers or relay allowance; own-key option.
- Built on **OpenMinis** (phone, proot/Alpine sandbox) + **DeepSeek Harness** (desktop plugin) + ported **UI-TARS-desktop** (ByteDance) operator hands; MCP servers + skills; chat-app presence (Feishu/DingTalk/WeCom/Telegram).
- Safety posture (claimed): **"asks before anything you cannot undo"** — stop before deleting/sending/paying, remembered per-case; logins/CAPTCHAs handed to user. Approval-gate pattern, same family as Agent Assurance "Unable to Verify" + Hari outcome packs (approvals).
- Own comparison table vs Meta Muse (cloud VM per user, closed) vs OpenMinis (single phone, GPL-3.0): nanoMuse = your devices + relay, BYO model, GPL-3.0-or-later. Explicit non-affiliation disclaimer re Meta trademark.
- Origin signals: nanomuse.cn, Chinese chat apps, mainland-China phone sign-in — Chinese community project.

## Why watch

1. First OSS personal-agent stack combining phone + desktop hands with an explicit ask-before-irreversible rule — testable claim for an Article-26-style seeded probe (does the gate actually fire?).
2. Same-week context: Apple FDA/Muse message-reading story + site-blocking wave (07.10 digest) — permission posture is the live question, and here is an OSS answer to inspect.
3. arxiv paper same-day (2610.08699) — read before any pilot.

## See also

- [[runtime-authorization-ai-agents-2026]] — permission/governance axis (field evidence Oct 2026)
- [[andrew-ng-openworker-security-agents-2026]] — harness auditing
- [Brijesh Deb testable oversight](wiki/brijesh-deb-testable-oversight-2026.md)
- W3 track: pilot candidacy (staging target + namespace preconditions per Rook precedent)

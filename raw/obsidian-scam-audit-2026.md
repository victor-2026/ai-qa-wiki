# Obsidian Scam: Fake QA Audit with Malicious Plugins

**Date:** 2026-06-24
**Source:** Personal experience

## The Setup

1. Telegram contact with unverified account (US phone number, newly created) asks: "Still doing QA?"
2. Proposes an audit of several projects for 400 USDT → negotiated to 8,000 USDT (4,000 upfront, 4,000 after delivery)
3. "Have you worked with Obsidian?" — all documentation is in an Obsidian vault
4. Provides login credentials (email + password) for Obsidian Sync + vault password

## The Attack Vector

5. Asks to enable **community plugins** — sends a video tutorial on how to enable them
6. User downloads plugin list from the shared vault — finds:
   - **Hider** — hides UI elements, making malicious activity harder to detect
   - **Shell Commands** — can execute arbitrary system commands

## Why It's Dangerous

| Risk | Mechanism |
|------|-----------|
| Data theft | Plugin reads vault contents, tokens, keys, passwords |
| Remote code execution | Shell Commands runs system commands with user privileges |
| Supply chain | Shared account could have pre-installed malicious plugins/scripts |
| Auto-execution | Shell Commands supports automatic execution on vault open or via URI links |
| UI hiding | Hider can conceal settings, warnings, or malicious activity |

## Defense

1. **Never install plugins from untrusted sources** — even Obsidian community plugins are vetted minimally
2. **Use a sandbox** — dedicated VM, container, or isolated environment for suspicious vaults
3. **Restricted Mode** — keep it ON by default, toggle only for trusted plugins
4. **Don't use someone else's sync account** — they control what gets synced
5. **Mobile limitation** — Shell Commands cannot run on mobile Obsidian (useful air gap for testing)
6. **After exposure:** change passwords, revoke sessions, delete the account

## Similar Patterns

- Fake job interviews requiring cloning a GitHub repo with embedded trojans
- "Freelance audit/consulting" as social engineering pretext
- This variant: **pretext = QA audit** → **tool = Obsidian** → **payload = malicious community plugins**

## Related

- See `wiki/obsidian-skills-kepano.md` — legitimate Obsidian skill usage
- General rule: sandbox ANYTHING from untrusted sources, even if the tool looks legitimate

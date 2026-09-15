# Meta Muse — Personal AI Agent (Consumer)

> Meta, Sep 2026. Multiple sources: TechCrunch (Sep 8), The Verge (Sep 8). Muse Spark model.

Meta introduced **Muse**, a personal AI agent that connects to a user's apps and services (email, calendars, payments, health, smart home, shopping, music, events) and performs tasks autonomously on their behalf.

## What Muse Does
- Sends emails, books travel, lowers bills, fills out forms
- Creates plans, turns recipe reels into grocery lists, sends party invitations
- Makes purchases via Stripe Link (with purchase protections)
- Works in background after user leaves the app
- Learns from conversations to make unprompted suggestions

## Technical Architecture
- **Model**: Muse Spark (Meta's in-house model)
- **Security**: "Muse Secure VM" — dedicated cloud computer with own browser
- **Isolation**: Another AI agent, **Sentinel**, patrols the same VM but stays separate
- **Privacy claims**: No visibility into passwords/payment methods, no sharing with Meta's ads systems
- **Opt-in**: User chooses which apps to connect one at a time
- **Cross-platform**: muse.ai web, iOS/Android apps, WhatsApp, Meta AI glasses (coming soon)

## Access & Pricing
- **Free** tier with usage meter
- **Power**: $20/month
- **Maximum**: $100/month
- Requires payment card to start
- 1Password and Shopify Shop Pay coming soon

## Trust Problem
Meta just settled a **$18 billion multistate lawsuit** over social media consumer harms (2026). The company has history:
- 2011: FTC settlement for deceptive privacy practices
- 2019: $5 billion FTC penalty (Facebook privacy violations)
- Cambridge Analytica scandal
- 2023: FTC charge for violating privacy order
- Instagram support chatbot helped hackers take over 20,000 accounts
- "Discover" feature displayed other users' prompts without consent

**The question**: Can consumers trust Meta with their personal data, passwords, and payment info — given this history?

## Testing Implications
- **Agent security testing**: Muse Secure VM needs verification (does it actually isolate?)
- **Permission boundary testing**: Does Muse respect opt-in boundaries?
- **Background task reliability**: Tasks continue after app closure — how to verify?
- **Privacy claims verification**: "Muse doesn't share data with ads" — need to test, not trust
- **Sentinel agent testing**: The guardrail agent itself needs testing
- **Cross-platform consistency**: Web, iOS, Android, WhatsApp, glasses — all need testing

## Source
- TechCrunch: https://techcrunch.com/2026/09/08/meta-debuts-its-muse-ai-agent-will-consumers-trust-it/
- The Verge: https://www.theverge.com/ai-artificial-intelligence/991216/meta-bets-on-ai-agent-muse-to-catch-up-in-ai-race
- Meta: https://ai.meta.com/muse/
- Tags: #meta-muse, #ai-agent, #consumer-ai, #privacy, #security-testing, #trust, #meta-2026
- See also: [[llm-testing]], [[Test-Reliability]], [[agent-jailbroken-eval-said-it-passed]]

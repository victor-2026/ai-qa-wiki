# Alexey (Proka4) — AI Transformation Lead

## Profile
- **Role:** AI Transformation Lead
- **Former:** QA (8+ years in testing)
- **Telegram:** [@aiproka4](https://t.me/aiproka4)
- **Product:** Magnum Studio

## Product: Magnum Studio
**What it does:** Platform that turns a Jira ticket into a live autonomous agent session.

**Flow:**
1. Ticket assigned or bot mentioned via @
2. Isolated agent (per-task worktree) starts:
   - Investigates the bug
   - Writes spec
   - Writes code
   - Opens merge request or releases
   - Assembles team of focused sub-agents as needed
3. Human-in-the-loop throughout:
   - Interactive questions with options, directly in Jira
   - Returns task to human on blockers
   - Honest failure screens
   - Live terminal access to intervene mid-work
4. Production reliability:
   - Stable webhook delivery via reverse tunnel
   - Auto-recovery of dead sessions
   - Catch-up after downtime
   - Shared bot routing by author

**Flow system:** Behavior per ticket type is configured without code (bug → investigate first, story → spec first).

## Positioning
- **Focus:** AI transformation for engineering teams — real delegation, not ChatGPT demos
- **Audience:** Engineering teams using Jira, GitLab, Confluence daily
- **Differentiator:** Built on QA thinking — "how things break in prod, where silent failures happen"
- **Key thesis:** "Модель есть у всех. Сложное — доверие и встроенность." (The model is available to everyone. Hard part is trust and integration.)
- **Agent design principle:** "Агент должен вести себя как нормальный коллега, а не как фокусник" — ask when unsure, return task when stuck, fail honestly, stay fully observable

## Key Ideas
- **QA мышца → агент дизайн:** Same muscle that finds how systems break is now used to design agent behavior
- **Делегирование (delegation) as core metric:** Not "AI generates code" but "AI takes real task from ticket to MR"
- **Human-in-the-loop as architecture:** Interactive questions, blocker return, live terminal — not an afterthought
- **No-code flow configuration:** Ticket type → behavior, no coding needed
- **Production reliability as feature:** Dead session recovery, missed event catch-up

## Relationship to our work
- QA background → AI agent design — identical trajectory to our positioning
- Magnum Studio solves the "enterprise trust" problem differently from our approach (Jira-native vs testing-native)
- Natural collaborator or reference for enterprise AI transformation content

## Last updated
2026-06-18 — initial profile (from his LinkedIn post)

---
title: "Master AI Before It Masters You — 27 Claude Tips"
type: article
updated: "2026-08-17"
tags: [claude-code, linkedin]
---

# Master AI Before It Masters You — 27 Claude Tips

**Author:** Ruben Hassid
**Source:** [LinkedIn](https://www.linkedin.com/in/ruben-hassid/) (6h)
**Full guide:** https://how-to-ai.guide

---

## Core Techniques

### 1. Make Claude Ask You Questions (Tip #8)

Paste at the end of any prompt:

> "Before answering, use the AskUserQuestion form to get more context from me if necessary."

Claude will repeatedly ask clarifying questions — impossible to fail when the AI directs its own context gathering.

### 2. Talk Instead of Type (Tip #5)

Use voice input (e.g., Wispr Flow, Shift key). Speak for 10 minutes straight: goals, constraints, what you tried, what you hate, your contradictions. Then:

> "These are the messy drafts. Ask me questions if you didn't get something as a form."

**Why it works:** When you type, you delete context without noticing. When you talk, you don't.

### 3. Make Images Without an AI Generator (Tip #3)

Upload a reference image, then prompt:

> "Code an HTML-like infographic like the one I attached, but about [topic]."

Export the HTML to Canva. Text is always correct — something image generators still can't promise.

### 4. Say What You Hate, Not What You Want (Tip #17)

"Make it punchier" does nothing. Adjectives are useless. Instead:

> "Never write like this: [paste the thing you hate]."

Draws the exact line not to cross.

### 5. Build a Mini-App in a Message (Tips #13 + #14)

> "Build me an artifact that tracks [my habits / my pipeline / my reading list], and make it save my data between sessions."

Then: "Make it so there is a Claude coach inside I can talk to, with the context of this artifact."

Publish, share the link. The other person uses Claude through your app.

---

## Settings (30 seconds, today)

1. **Connectors:** Turn off everything you don't actively use. Every active connector loads into every message — you pay for that.
2. **New chats at 50 turns.** Past 100, Claude re-reads a novel before every answer — dumber and pricier.
3. **When Claude is wrong:** Don't type "no, that's wrong." Go back to the prompt before the bad answer, edit it, save. The wrong answer stays in the conversation forever otherwise.
4. **Project files limit:** A Claude Project with 40 files makes everything sound the same. Claude answers FROM your files instead of thinking. Projects are for repeated tasks. Every new idea starts in an empty chat.

---

## Relevance to AI Testing

| Technique | Testing Application |
|-----------|-------------------|
| Ask questions before answering | Use in prompts for test case generation — force LLM to clarify requirements before writing tests |
| Say what you hate (anti-patterns) | Define test anti-patterns explicitly: "Never write tests that depend on external APIs without mocking" |
| Voice input for context | Useful for exploratory test session notes — preserve full context |
| Mini-app artifacts | Build test status dashboards, pipeline trackers as Claude artifacts |
| 50-turn limit | Critical for LLM-as-Judge eval runs — each turn adds cost and degrades quality |
| Project file overload | Directly relevant to Virto OZ KB governance — too much context = generic answers |

*Processed: 2026-07-30 from raw/Master AI before it masters you.md*

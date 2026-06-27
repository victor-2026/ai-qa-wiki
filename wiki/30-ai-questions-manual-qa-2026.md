# 30 AI-Focused Interview Questions for Manual QA

**Source:** Ruslan Desyatnikov — 28 years of QA interviewing experience
**Context:** Questions evolved because AI fundamentally changed what it means to be an effective tester
**Date:** 2026

---

## Overview

Knowing ChatGPT, Copilot, Claude, or Gemini no longer differentiates candidates. Everyone uses them. The key differentiator is **how the candidate thinks when AI is part of the equation.**

These 30 questions test 7 dimensions of AI-augmented QA thinking.

---

## 1. AI & Critical Thinking

*Core question: Can the candidate detect when AI is wrong?*

| # | Question | What It Tests |
|---|----------|---------------|
| 1 | Tell me about a time AI confidently gave you the wrong answer. How did you recognize it? | Hallucination detection, domain knowledge depth |
| 2 | What AI-generated output would you never accept without manual review and why? | Understanding of AI failure modes |
| 3 | How do you determine whether AI-generated test cases are complete? | Test coverage knowledge, critical evaluation |
| 4 | Can you describe a situation where you intentionally ignored AI's recommendation? | Independent judgment, confidence in own expertise |
| 5 | How do you know when AI has missed an important business risk? | Business domain understanding, risk awareness |

**Key signal:** Strong candidates don't just trust AI — they validate with domain knowledge and business context.

---

## 2. AI & Risk Analysis

*Core question: Can the candidate use AI for coverage without being fooled by it?*

| # | Question | What It Tests |
|---|----------|---------------|
| 6 | AI generated 500 test cases. How would you determine whether they are sufficient? | Risk-based testing, coverage modeling |
| 7 | What types of defects do you think AI is least likely to identify? | Understanding of AI blind spots (UX, business logic, domain-specific edge cases) |
| 8 | How would you validate that AI-generated tests provide meaningful risk coverage rather than just high test coverage? | Distinction between coverage quantity and quality |
| 9 | How would you prioritize AI-generated test cases? | Risk-based prioritization, triage skills |
| 10 | What business risks do you believe AI consistently underestimates? | Business domain expertise, strategic thinking |

**Key signal:** Strong candidates know that 500 tests != 500 valuable tests. They apply risk-weighting.

---

## 3. AI & Requirements

*Core question: Can the candidate use AI to improve requirements quality?*

| # | Question | What It Tests |
|---|----------|---------------|
| 11 | You upload a user story into ChatGPT and receive 200 test cases. What's your next step? | Requirements analysis, triage, critical review |
| 12 | How do you verify that AI correctly interpreted ambiguous requirements? | Ambiguity detection, requirement validation techniques |
| 13 | How would you use AI to improve poor requirements before creating test cases? | Shift-left thinking, AI as requirements quality tool |
| 14 | Can AI identify missing requirements? If yes, how would you validate its suggestions? | Gap analysis, validation methodology |

**Key signal:** Strong QA catches ambiguous requirements before AI generates meaningless test cases from them.

---

## 4. AI & Decision Making

*Core question: How does the candidate resolve AI-vs-human conflict?*

| # | Question | What It Tests |
|---|----------|---------------|
| 15 | When would you completely ignore AI-generated output? | Absolute boundaries of AI trust |
| 16 | If AI and your experience disagree, what do you do? | Conflict resolution, evidence-based decision making |
| 17 | How much confidence do you place in AI-generated answers? Why? | Nuanced understanding of AI reliability |
| 18 | What is AI's biggest weakness in software testing? | Meta-cognition about AI limitations |

**Key signal:** The best answer to #16 is not "always trust AI" or "always trust myself" — it's "I investigate the disagreement with data."

---

## 5. AI & Productivity

*Core question: Has AI genuinely improved the candidate's testing, or just made them faster at bad testing?*

| # | Question | What It Tests |
|---|----------|---------------|
| 19 | Besides generating test cases, how has AI genuinely made you a better tester? | Deep AI integration, beyond surface-level use |
| 20 | What testing activities have you stopped doing manually because of AI? | Practical AI adoption, workflow transformation |
| 21 | What activities would you never delegate entirely to AI? | Understanding of human-value activities |
| 22 | Has AI made you more effective, or simply faster? Give an example. | Distinction between speed and quality improvement |

**Key signal:** "Faster" is table stakes. "More effective" means better test design, better risk coverage, better defect detection.

---

## 6. AI & Leadership

*Core question: Can the candidate build AI governance for a QA team?*

| # | Question | What It Tests |
|---|----------|---------------|
| 23 | How would you prevent junior testers from becoming overdependent on AI? | Mentoring, skill development, guardrails |
| 24 | If your team blindly trusted AI, what risks would concern you most? | Systemic risk awareness, leadership perspective |
| 25 | How would you measure whether AI actually improved testing quality? | Metrics design, outcome measurement |
| 26 | What AI governance practices would you introduce into a QA organization? | Process design, AI policy creation |

**Key signal:** Lead/Manager-level candidates must have concrete governance ideas, not generic "we should be careful."

**Example governance practices:**
- AI-generated test cases require human sign-off before execution
- Hallucination detection as a daily QA routine
- Monthly AI output quality audit
- "Trust but verify" rule for all AI-produced artifacts

---

## 7. AI Evaluation

*Core question: Can the candidate evaluate AI tools methodically?*

| # | Question | What It Tests |
|---|----------|---------------|
| 27 | How would you test an AI agent before allowing it to generate production test cases? | Agent validation, sandbox testing, benchmarking |
| 28 | What metrics would you use to evaluate AI-generated test cases? | Quality metrics, not just quantity |
| 29 | How would you detect hallucinations in AI-generated testing artifacts? | Hallucination detection techniques |
| 30 | How would you compare two AI models for test design quality? | Model evaluation methodology, A/B testing for AI |

**Key signal:** This is where practical AI experience separates those who've read about AI from those who've worked with it.

**Suggested metrics for #28:**
- Relevance score (are tests aligned with requirements?)
- Coverage uniqueness (new scenarios vs obvious ones)
- Actionability (can a tester execute this?)
- False positive rate in practice
- Business risk coverage (not just functional coverage)

---

## Why These Questions Matter

Traditional QA interview questions test domain knowledge and process understanding. These questions test **AI awareness + critical thinking + practical integration** — the three qualities that separate modern QA from pre-AI QA.

> *"Almost every candidate says they use ChatGPT. That does NOT differentiate them."* — Ruslan Desyatnikov

---

## Related

- `wiki/ai-fluency-interview-2026.md` — Google/Meta interview reform with AI evaluation criteria
- `wiki/offline-evaluation-trajectories-2026.md` — Self-evaluation framework for QA skills
- `wiki/anton-gulin-3-layer-ai-qa-architecture.md` — 6 quality gates for AI-augmented QA

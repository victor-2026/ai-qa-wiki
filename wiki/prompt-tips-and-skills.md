---
title: "Prompt Tips & Agent Skills Architecture"
updated: 2026-05-04
tags: [prompts, agent-skills, opencode, playwright, pytest, best-practices]
type: guide
---

# Prompt Tips & Agent Skills Architecture

**Goal:** Effective testing through agents (OpenCode, Claude Code) with Playwright + Pytest  
**Method:** Multi-layered prompts + well-structured Agent Skills  

---

## 1. Prompt Types for Test Tasks

### 1.1 Context-Aware Test Creation
Instead of "Write login test", use prompts that force agent to study existing code first.

```
"Study pages/ folder structure and current fixtures in conftest.py. 
Write a new test for [function], using Page Object Model. 
Note: all locators must use data-testid. Save file to tests/ui/."
```

### 1.2 Exploratory Testing (Edge Cases)
Agents excel at finding edge cases you might forget.

```
"Analyze schemas/user_profile.py. Generate Pytest parametrization 
set for 'age' field. Include negative scenarios (strings, negative numbers, 
too large values) and verify how validator reacts."
```

### 1.3 Debugging (Self-Healing)
Since agent has terminal access, it can fix failing tests autonomously.

```
"Run tests/test_auth.py. If it fails, analyze logs and screenshots 
in test-results/. Fix locators in corresponding Page Object file, 
then re-run to verify."
```

### 1.4 Refactoring & Standards
If you created Agent Skills, use them for quality checks.

```
"Check tests/new_feature.py for compliance with our playwright-qa-expert skill. 
Replace page.wait_for_timeout() with Playwright dynamic waits 
and add @pytest.mark.smoke markers where appropriate."
```

### 1.5 Mocking (API Mocking)
Playwright can intercept requests.

```
"Write Playwright scenario that mocks /api/v1/user response with 500 status. 
Verify UI correctly displays 'Service Unavailable' message and Retry button is active."
```

---

## 2. Main Tips for Prompt Formulation

### Use Action Verbs
- ✅ "Study", "Run", "Compare", "Fix"
- ❌ "Can you maybe write..." (weak, unclear)

### Restrict Scope
- ✅ "Work only in /tests folder"
- ❌ "Help me with tests" (too broad)

### Demand Chain of Thought
```
"First describe testing plan in natural language, 
then write code. After that, self-check: did you use time.sleep? 
Fix any issues before showing me final result."
```

### Multi-layered Approach
1. Analysis prompt (risks, priorities)
2. Code generation (one test at a time)
3. Self-verification prompt (check standards compliance)

---

## 3. Learning Resources

### 3.1 Official Specifications & Docs
- [AgentSkills.io](https://agentskills.io/home) — Main spec for skill formatting, SKILL.md structure
- [Anthropic — Computer Use & Agents](https://docs.anthropic.com/en/docs/build-with-claude/computer-use) — How AI interacts with interface/code
- [Playwright Best Practices](https://playwright.dev/docs/best-practices) — Bible for automator (locators, web-first assertions, no time.sleep)

### 3.2 Practical AI-Coding Guides
- [Claude Code Guide](https://docs.anthropic.com/en/docs/agents-and-tools/claude-code) — How agents work with terminal and tests
- GitHub Copilot Extensions & Skills — GitHub blog posts on "teaching" agents for specific tasks

### 3.3 Communities & Open Source
- GitHub repos: search by `agent-skills` or `mcp-servers` (Model Context Protocol)
- **MCP** — Related tech from Anthropic, allows agents to connect to databases/browsers directly
- Awesome-LLM-Apps — Collection of ready-to-use skills and prompts

### 3.4 Key Principles (Cheat Sheet for Skills)

#### 1. Atomic Skills
One skill = one task ("Generate selectors", not "Everything about tests")

#### 2. RAG for Tests
How to feed agent documentation for your API so it writes relevant tests

#### 3. Self-Correction Loops
Prompt techniques forcing agent to run pytest and fix code until tests turn green

---

## 4. Architecture: "Matryoshka" Skills

Don't create one huge file. Divide agent knowledge into logical levels:

```
skills/
├── pytest-architect/          # Level 1: Structure (fixtures, conftest.py, plugins)
├── playwright-locator-expert/  # Level 2: Selector strategy (data-testid rules)
├── qa-reporter/              # Level 3: Log analysis, failure report generation
├── load-stress-qa/           # Level 4: k6, Locust scripts
├── rest-api-qa/              # Level 5: API testing patterns
└── universal-qa-expert/      # Level 6: Senior QA strategy (ISTQB, DORA)
```

**Installation in OpenCode:**
- Project-local: `.opencode/skills/skill-name/SKILL.md`
- Global: `~/.config/opencode/skills/skill-name/SKILL.md`

---

## 5. OpenCode Desktop Environment Setup

To maximize agent effectiveness:

### 1. Create `.opencode/agents.md`
```
"You are a Senior QA Automation Engineer. 
Your stack: Playwright, Pytest, Python 3.10+.
Your goal: 100% test stability and zero code duplication."
```

### 2. Grant Log Access
Ensure agent knows path to artifacts folder (`test-results/`) so it can read `trace.zip` or console logs on failure.

### 3. Verify Skills Detection
```
/skills
```
Should show:
```
Available skills:
- playwright-qa-expert
- universal-qa-expert
- obsidian-markdown
...
```

---

## 6. What to Read Right Now (Best Practices)

### Academic/Research
- [Principled Instructions for LLMs](https://arxiv.org/abs/2312.16171) — Fundamental paper on formulating prompts for 30-40% better code quality

### Industry Guides
- [The Art of Agentic Workflow](https://www.deeplearning.ai/the-batch/how-agents-can-improve-llm-performance/) (Andrew Ng) — Explains why "write-run-fix" cycle (what OpenCode does) is exponentially more effective than simple chat

---

## 7. Practical Example: Staged Prompt for Test Generation

### Step 1: Analysis (separate prompt)
```
"Analyze current test coverage in e2e/api/. 
List 5 critical gaps. Be brief: 1 line per gap."
```

### Step 2: Code Generation (one test at a time)
```
"Write MET-003: Follow-unfollow symmetry test. 
Add try-catch, timeout 5000, assertions on response body. 
Give only code, no explanations."
```

### Step 3: Self-Verification
```
"Check MET-003 code against playwright-qa-expert skill. 
Fix any issues: wrong locators, missing assertions, no time.sleep."
```

---

## 8. Related Skills (Recommended Structure)

| Skill Name | Location | Purpose |
|-----------|----------|---------|
| **playwright-qa-expert** | `.opencode/skills/` (project) | Playwright + TS for Buzzhive (API/UI patterns) |
| **universal-qa-expert** | `~/.config/opencode/skills/` (global) | Senior QA Lead: ISTQB, DORA, risk-based |
| **rest-api-qa** | `~/.config/opencode/skills/` | API testing patterns (requests, httpx) |
| **load-stress-qa** | `~/.config/opencode/skills/` | k6, Locust, JMeter scripts |
| **java-qa** | `~/.config/opencode/skills/` | JUnit, Selenium, RestAssured |
| **go-qa** | `~/.config/opencode/skills/` | testing, httpexpect, ginkgo |

---

## 9. Key Takeaways

1. **Prompts:** Use action verbs, restrict scope, demand chain of thought
2. **Skills:** Atomic, layered ("Matryoshka"), project-local + global
3. **Iterations:** Analysis → Code → Self-check → Fix (staged approach)
4. **Resources:** AgentSkills.io for spec, Playwright docs for practices
5. **OpenCode:** Setup `agents.md`, grant log access, verify skills with `/skills`

---

**Tags:** #prompts #agent-skills #opencode #playwright #pytest #best-practices #qa-strategy  
**Related:** [[agent-skills-specification]] [[obsidian-skills-kepano]] [[metamorphic-tests-comparison]]  
**Updated:** 2026-05-04








<!-- backlinks-start -->
### Backlinks
- [Ai In Qa Issue 17 Butch Mayhew 2026 07 06](wiki/ai-in-qa-issue-17-butch-mayhew-2026-07-06.md)
- [Alex Barady 9 Concepts Ai Builder 2026](wiki/alex-barady-9-concepts-ai-builder-2026.md)
- [Claude Code Skill Examples 2026](wiki/claude-code-skill-examples-2026.md)
<!-- backlinks-end -->

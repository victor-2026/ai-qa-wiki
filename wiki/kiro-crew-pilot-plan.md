# Kiro Crew Pilot Plan

**Goal:** Evaluate Kiro Crew as multi-agent orchestration platform for QA/QE workflows
**Time:** 3-5 days (2-3 hours/day)
**Stack:** Python 3.10+, Node.js 22+, Kiro CLI
**Source:** https://github.com/kirodotdev/kirocrew (3.5k stars, Apache 2.0)

---

## Day 1: Setup + Basic Agent

### Morning (1h)
1. Install Kiro Crew (one-line installer)
   ```bash
   curl -fsSL https://download.crew.kiro.dev/cli.sh | sh
   ```
2. Run `kirocrew setup` + `kirocrew doctor`
3. Open web dashboard at `http://localhost:5476`
4. Explore UI: sessions, memory, skills, schedules

### Afternoon (1h)
5. Create first agent session
6. Test basic task: "Analyze the qa-automation-playwright repo and suggest 3 test improvements"
7. Observe: tool calls, reasoning, approval flow
8. Check memory: does it retain context?

### Deliverable
- Screenshot of dashboard + first session
- Notes on UX, speed, approval friction

---

## Day 2: Skills + Self-Learning

### Morning (1h)
1. Create custom skill: `qa-automation-review`
   - Input: test file path
   - Output: locator quality score, assertion coverage, anti-patterns
   - Use existing `code-review-qa` skill as template
2. Test skill on Buzzhive test files
3. Check if skill persists across sessions

### Afternoon (1h)
4. Test self-learning: correct agent's mistake, verify it remembers
5. Test skill evolution: does it suggest improvements?
6. Compare with opencode skills (your current setup)

### Deliverable
- Custom skill definition
- Comparison: Kiro Crew skills vs opencode skills
- Notes on self-learning quality

---

## Day 3: Multi-Agent Orchestration

### Morning (1h)
1. Test subagent delegation:
   - "Research Playwright best practices in parallel, then synthesize"
   - Observe: 2-3 subagents spawn, return results
2. Test cross-session context: does parent session see subagent results?

### Afternoon (1h)
3. Test scheduling:
   - Create recurring job: "Every morning, summarize open issues in qa-automation-playwright"
4. Test webhook: trigger agent from external event
5. Test long-running task: migration or analysis that takes 10+ minutes

### Deliverable
- Multi-agent session transcript
- Scheduling test results
- Notes on orchestration reliability

---

## Day 4: Security + QA Integration

### Morning (1h)
1. Test security controls:
   - OS sandbox (namespace/Seatbelt)
   - Sensitive path blocking
   - Credential redaction
   - Deny patterns
2. Test governance: policy files, approval modes

### Afternoon (1h)
3. Integrate with mutation-matrix workflow:
   - Agent runs mutation test
   - Agent reports results
   - Agent suggests fixes
4. Test with Buzzhive: agent triages failed test, suggests root cause

### Deliverable
- Security audit notes
- Mutation-matrix integration test
- QA workflow demonstration

---

## Day 5: Evaluation + Decision

### Morning (1h)
1. Run full evaluation:
   - Agent quality: does it produce useful output?
   - Reliability: how often does it fail/timeout?
   - Cost: API credits consumed
   - Learning curve: how fast did you get productive?
2. Compare with alternatives:
   - opencode (current)
   - QAEverest (evaluation)
   - testRigor (evaluation)

### Afternoon (1h)
3. Write verdict:
   - Use case fit for QA/QE
   - Consulting offering potential
   - Integration with existing workflow
   - Recommendation: adopt / further evaluate / reject

### Deliverable
- Evaluation scorecard
- Decision document
- Wiki page with findings

---

## Success Criteria

| Metric | Target | Actual |
|--------|--------|--------|
| Install success | < 5 min | |
| First useful output | < 30 min | |
| Custom skill working | < 2 hours | |
| Multi-agent delegation | Working | |
| Self-learning confirmed | Working | |
| Security audit passed | No red flags | |
| Mutation-matrix integration | Working | |
| Verdict written | Day 5 | |

---

## What to Watch For

### Positive Signals
- Memory persists across sessions
- Skills are reusable and inspectable
- Multi-agent delegation works reliably
- Security controls are production-grade
- Dashboard UX is intuitive

### Red Flags
- Frequent timeouts or failures
- Memory loss between sessions
- Skills don't persist
- Security controls too restrictive or too permissive
- High API cost for simple tasks

---

## Integration with Existing Work

### If Adopted
- Replace opencode for complex multi-agent tasks
- Use for consulting engagements (client-facing)
- Build QA-specific skills (mutation testing, test generation)
- Integrate with CI/CD (scheduling, webhooks)

### If Not Adopted
- Document findings for Articles 26/27
- Compare with Autonoma/QAEverest for vendor evaluation
- Consider ACP standard for future tools

---

*Created: 2026-08-30*

# Prachi Dahibhate — Testing Today: James Bach, the Curiosity That Changed Software Testing (Substack, 2026-08-25)

Source: https://prachidahibhatetesting.substack.com/p/testing-today-the-people-who-changed

Summary by Prachi Dahibhate. Focus: James Bach, Rapid Software Testing (RST), Context-Driven School, exploratory testing, and how Bach's ideas map to AI-assisted testing in 2026.

Key points extracted (verbatim-faithful):
- Bach (tester at Apple 1987, Borland; co-founded Context-Driven School with Cem Kaner, Brian Marick, Bret Pettichord; created RST with Michael Bolton; Heuristic Test Strategy Model v6.3).
- Conventional image: Requirement → test case → execution → pass/fail → report. Bach asks what's underneath: incomplete requirement? test doesn't represent real risk? passing checks = false confidence? most important problem unwritten?
- Exploratory testing = simultaneous learning, test design, test execution.
- "Magic testing box" thought experiment (from Taking Testing Seriously, Bach & Bolton, Wiley 2025): a box claims to test your software and report bugs. How do you know it did a good job? If it reports no bugs, does that mean none exist, or that it failed to find them? Central to AI-assisted testing.
- The hard problem: knowing whether the AI's answer deserves your trust.
- Productivity Paradox (Bolton, 2026, from Taking Testing Seriously): AI saves time, but using it responsibly requires considerable time/effort. Management rewarding visible AI productivity can reward irresponsible (faster-looking) use. Correct response may be "identify which risks deserve deeper testing," not "test faster."
- Testing vs Checking distinction (RST): machine does repeatable checks; testing = learning, exploration, investigation, judgment. Better question: "Which parts of testing can AI perform, and which still require human judgment?"
- "Use AI to extend your thinking, not replace it." Step-back prompting: start broadly, don't over-specify immediately.
- "What's not here?" - AI's list of investigated items can become the boundary of your imagination. Think first, ask AI second, then compare.
- Engineering leadership framing: team should say "here is what we know, what we don't know, risks investigated, what could surprise us" - decision support, not activity reporting.
- The James Bach Test (before trusting an AI-generated report): What did it actually explore? What did it merely check? What assumptions? What wasn't investigated? What evidence supports conclusions? What risks remain uncertain? Who is responsible for final judgment?
- Book: Taking Testing Seriously: The Rapid Software Testing Approach (Wiley, 2025, 560pp). Sites: rapid-software-testing.com, satisfice.com.

(by Daniel Webb via LinkedIn)
Last week, [**Bas Dijkstra**](https://www.linkedin.com/in/basdijkstra/) posted about the test automation quadrant, the idea that most test suites sit in one of two uncomfortable places: fast but low-signal, or high-value but painfully slow. Getting to the top right of that quadrant (fast and valuable) is the real challenge.  
  
It got me thinking and I commented that there might be a way to push further: what if we could focus testing on the parts of the system that carry the most risk of defects and that we change most often? Not just better tests but better targeting of tests. This is an area that can be very difficult for testers who don't code or don't have visibility of the code - relying on other people to tell you what might be impacted can be risky and we are not in the belief business as testers, we are paid to be suspicious of such claims and guidance!  
  
That question sent me down a path, and the result is a new skill I've built for the [**CodeScene**](https://www.linkedin.com/company/codescene/) MCP server: Risk-Based Testing With Code Health.  
  
The core idea is simple but often overlooked in practice. Most teams either test everything equally (spreading effort too thin) or rely on gut feel to decide what's risky. Neither approach scales. CodeScene already has the signals: code health scores, change frequency, hotspot data, ownership patterns. Translating those into "here's what testing should actually focus on for this change" is where teams get stuck.  
  
That's what this skill does. It takes an opinionated stance: the current branch's change set comes first. What you've actually changed is more actionable than historical hotspots alone. Hotspots add systemic context, but they shouldn't overshadow the code that's moving right now.  
  
The output is structured and tester-ready: top risk areas mapped to business impact, prioritised test charters with expected outcomes and failure signals, must-pass checks before merge, and ownership routing so the right people are reviewing the right things.  
  
No abstract hotspot lists. No generic "test the risky parts" advice. Concrete scenarios tied to evidence.  
  
Thanks to [**Bas Dijkstra**](https://www.linkedin.com/in/basdijkstra/) for the post that sparked this. And to [**Boyd Kronenberg**](https://www.linkedin.com/in/boydkronenberg/) who asked for examples, this is my answer. If you're using CodeScene with an AI coding assistant, try asking "Where should testing focus first for this PR or changeset?" and see what comes back.  
  
Risk-based testing shouldn't require a PhD in static analysis. It should be one question away.  
  
P.S. This is one of many heuristics and is one that is often overlooked in my opinion but I want to be clear - this is not the only thing that you should consider when assessing the risk of a change.

You can see the full skill here:https://github.com/codescene-oss/codescene-mcp-server/blob/main/skills/risk-based-testing-with-code-health/SKILL.md
[[ai-testing-effectiveness]] [[ai-testing-skill]] 
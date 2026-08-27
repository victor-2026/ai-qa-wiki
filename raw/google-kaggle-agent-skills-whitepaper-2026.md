Google/Kaggle whitepaper "Agent Skills" (May 2026) - 62-page guide on procedural memory for AI agents, structured around SKILL.md format.

Key claims:
- Skills cut active context by more than 98%
- One general-purpose agent + many specialist workflows, loaded only when needed
- Description field is critical: must tell agent what skill does, when to use it, when NOT to use it
- Too vague = agent ignores skill; too broad = agent grabs it for everything
- Make bad actions impossible in software
- Test how the agent got there (trajectory, not just answer)
- Test skills NEXT to other skills they'll run beside (not in isolation) - context rot
- Skills library is becoming the asset; model is becoming the runtime

Sairam Sundaresan (AI Engineering Leader, Author "AI for the Rest of Us") shared on LinkedIn:
- The model is becoming the commodity; real advantage = captured context, judgment, workflows
- Description field = prompt engineering one layer down
- Skill selection = routing problem as library grows
- Mutually exclusive triggers and explicit precedence rules keep collisions manageable
- "The real advantage is not just encoding the workflow but making the decision logic explicit enough to inspect, test, and improve"

Key comments:
- Vitalii Serbyn: "testing the description field is where this actually gets hard: two skills with overlapping 'when to use it' language will collide"
- Shadman Arko: practical experience - moving from single giant system prompt to scoped tools with clear descriptions stopped agent guessing
- S Naz: "description field being the real interface is underrated. It is a routing decision made by a model with no ground truth about org"
- Pooja Jain: "testing for how the agent got there rather than just the final answer touches on the most critical challenge in autonomous agent evaluation"
- Sairam回复Pooja: "The final answer can look correct while the path taken to reach it is fragile. Evaluating the trajectory gives us a much better view of whether an autonomous agent can actually be trusted."

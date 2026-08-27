[

Radik Zagirov

• 1st



](https://www.linkedin.com/in/rzagirov/)

Co-Founder & CEO, Agentiqa. Independent agentic quality layer. TUM.ai

9h •

[

](https://www.linkedin.com/in/rzagirov/)

Every self-improvement loop for agents hits the same wall: the model eventually starts optimizing against the quality gate itself instead of the actual problem.  
  
You see this everywhere right now. OpenAI's research runs showed agents exploiting infrastructure and bypassing filters just to get a pass on evaluation tasks. In smaller setups, you give a coding agent an autonomous loop to refactor code and pass tests, and within hours it figures out how to rewrite mock assertions or relax validation thresholds to turn the pipeline green.  
  
When AI writes code and AI grades code, the verifier becomes part of the optimization landscape.  
  
This raises a fundamental architecture question for anyone building agent systems:  
  
How do you build a quality gate that doesn't rot under iterative self-improvement?  
  
A few hard constraints we keep running into at Agentiqa:  
  
- The verifier must be external to the agent's execution runtime. If the model can inspect, prompt, or touch the eval harness, it will eventually tamper with it.  
- State verification over code verification. Checking what the code looks like or what mocks return is useless. You have to verify the final side-effects in a real, isolated environment (actual browser DOM, real database state, external network boundaries).  
- Independent evaluation traces. A verifier cannot share context or memory with the agent that produced the output.  
  
If the quality gate lives inside the same closed loop, "self-improvement" is often just sophisticated metric hacking.  
  
Curious how other teams are isolating their eval gates from their generation loops right now. Are you relying on sandboxed environments, multi-agent adversarial setups, or strict immutable black-box testing?
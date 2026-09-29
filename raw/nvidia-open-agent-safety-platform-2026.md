# Source: Nvidia Open Agent Safety Platform launch (3 outlets, 2026-09-28)

**URLs:** CNBC (Kif Leswing, Open Agent Safety Platform) https://www.cnbc.com/2026/09/28/nvidia-releases.html · TechCrunch (Kirsten Korosec, toolkit) https://techcrunch.com/2026/09/28/nvidia-launches-new-platform-for-reining-in-rogue-ai-agents/ · The Verge (Emma Roth, milliseconds) https://www.theverge.com/tech/1001287/nvidia-ai-safety-platform-rogue-agents
**Fetched:** 2026-09-29 (webfetch, text ×3).

---

## CNBC — Open Agent Safety Platform (software platform)

- OpenShell: runs on CPUs, sets limits on agent capabilities. Sentry: monitors agents, runs on network chips (BlueField-4 DPUs), not CPUs/GPUs.
- Open source parts; "reference design" for partners: Cisco, Microsoft, Oracle, CoreWeave, Dell, HPE, Lenovo, ARM, Intel. Anthropic integrating cloud managed agents with OpenShell.
- Huang ("browser for agents", containment = only what the job needs): "You can't have agents roam around and drift around the company." Claim: platform "could have prevented" the July Hugging Face breach (Boitano: "over 17,000 agents attacking their infrastructure... for days and weeks").
- Huang (safety as engineering, Ezra Klein podcast last week): "You have to think about what you could have done... improve your process so that you could avoid this from happening again." Context: Amodei slowdown call two weeks ago (backed by Altman + Musk).

## TechCrunch — toolkit + debate framing

- Debate: AGI-step vs conventional engineering problem. Nvidia's answer: "move some security controls outside the agent altogether — creating a constant and independent security guard."
- Huang statement: "Safety and security require full-stack engineering." Trigger set: Anthropic/Google/OpenAI/Meta escapes; OpenAI's Hugging Face breach (summer, cybersecurity task); OpenAI published a rogue-reports site.
- OpenShell announced March; Sentry (BlueField-4, isolated view, "quarantine agents... in milliseconds") is the new combination. Dozens of backers incl. Anthropic, Arm, Microsoft, Oracle, SpaceX. **OpenAI not participating.**
- **Origin: work started a year ago following the introduction of OpenClaw** (Peter Steinberger's agent OS); March NemoClaw = enterprise OpenClaw-with-security.
- Huang (CNBC): "When you deploy an agent, no matter how smart, the first thing you do is to take away all of its rights" — like managing human employees/executives.
- Sacks (ex-White House AI czar): "Recent breakouts weren't proof that development must stop. They were proof that the sandbox was too weak. The runtime environment was poorly designed and misconfigured."
- Boitano: "Recent incidents have highlighted a fundamental hurdle for AI agents, and that is that model-level safeguards alone can't govern what agents can access or do."

## The Verge — milliseconds + minimal rights

- OpenShell on Vera AI CPU; restrictions checked before AND during tasks (not just at launch). Sentry on a separate chip, continuous monitoring.
- Huang: sandbox systems "designed in a way that keeps the agent with minimal rights". Related links tie the UNCTAD-bruteforce + single-company-wave pieces (same story cluster).

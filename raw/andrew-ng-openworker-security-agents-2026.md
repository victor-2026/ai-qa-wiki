# Andrew Ng — OpenWorker: open-source security agents (LinkedIn, 2026-08-26)

Source: LinkedIn post by Andrew Ng (DeepLearning.AI, AI Fund). 3d ago.
Full: https://openworker.com/ · Code: https://lnkd.in/gvZYspRv

---

OpenWorker - an open source agent that completes tasks on your laptop - released a new version with features for security workflows.

- After initial release, users found it useful for cybersecurity. "Attackers are already using AI; OpenWorker is committed to giving defenders the same leverage."
- Running an agent requires both (i) A model and (ii) A harness (the software around the model). Because the OpenWorker harness is fully open source, security teams can audit it to make sure no backdoors exfiltrate code/data to a company or foreign adversary.
- Built-in cybersecurity agents: (i) Scan code for vulnerabilities. (ii) Scan dependencies for supply-chain injections. (iii) Check cloud security configuration for attack surfaces. Enables developers to do more security work before deployment (shift-left).
- You choose the model: run open-weight models fully locally so sensitive code never leaves your machine. Helps with legit security work (reproducing a known exploit) that triggers refusals in closed models. Or use ChatGPT subscription, Ox Alpha, or any model via API key.

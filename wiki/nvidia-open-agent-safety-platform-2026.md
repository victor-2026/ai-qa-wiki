# Nvidia Open Agent Safety Platform: the industry's engineering answer (2026)

**Sources (3, all fetched ✅ 2026-09-29):** CNBC https://www.cnbc.com/2026/09/28/nvidia-releases.html · TechCrunch https://techcrunch.com/2026/09/28/nvidia-launches-new-platform-for-reining-in-rogue-ai-agents/ · Verge https://www.theverge.com/tech/1001287/nvidia-ai-safety-platform-rogue-agents. Raw: `raw/nvidia-open-agent-safety-platform-2026.md`.

## What shipped

- **OpenShell** (open source, CPU/Vera): capability limits, restrictions checked before AND during tasks. **Sentry** (BlueField-4 DPU, separate processor): continuous monitoring, "quarantine agents... in milliseconds", isolated view off-CPU/GPU.
- Reference design + partners (Cisco, Microsoft, Oracle, CoreWeave, Dell, HPE, Lenovo, ARM, Intel; Anthropic integrating). OpenAI not participating. Claim: would have prevented the July Hugging Face breach (17,000 agents, days/weeks).
- Doctrine: least privilege as the FIRST act ("take away all of its rights", like employee management); controls OUTSIDE the agent ("constant and independent security guard"); "model-level safeguards alone can't govern"; "Safety and security require full-stack engineering."
- Counter-position on record: Amodei slowdown call (backed Altman + Musk) vs Nvidia/Sacks engineering line ("sandbox was too weak... poorly designed and misconfigured" — Sacks).

## Why this page matters to our tracks

1. **Rogue-line, fourth entry** (after Holz/Li airgap, irregular wave, UNCTAD ladder): this one is the industry's ANSWER, not another incident. Parked for W4 Article 27 with the other three.
2. **Independence pattern, vendor-built:** monitoring on a separate processor so the watched cannot touch the watcher = the independence principle (author ≠ examiner) implemented in silicon. Compare our attestation doctrine — same shape, hardware substrate.
3. **OpenClaw origin story:** "work started a year ago following the introduction of OpenClaw"; March NemoClaw = enterprise OpenClaw-with-security. OpenClaw is our Section-1 pilot (RMT 53/58 + 22/24, fork frozen) — the pilot subject sits in the genealogy of this platform. Noted for W3, no pilot action (our fork is frozen; their platform is a reference design, not a runnable subject for us).
4. **Honesty check:** "would have prevented Hugging Face" is untestable counterfactual marketing; milliseconds-quarantine is a vendor claim until independently measured. Numbers treated as claims throughout.

## Cross-links

- Rogue-line siblings: UNCTAD ladder page, Holz/Li airgap (Verge 25.09), irregular-wave page.
- [[testerarmy-qa-agent-yc-p26-2026]] — no; instead: pilots/OpenClaw (Positions) via the origin story.
- Quotes banked: Articles/quotes.md → AI Safety (Huang rights, Sacks sandbox), parked W4.

# Rebuild Dossier: Mechanically-Enforced Specs for Agentic App Rebuilds (arXiv:2608.23616)

**Author:** Parker Fawcett
**Source:** https://arxiv.org/abs/2608.23616
**Context:** arXiv cs.SE paper. v1 22 Aug 2026, v3 20 Sep 2026. Tool MIT licensed, open source: https://github.com/Parker-Fawcett/rebuild-dossier (DOI 10.5281/zenodo.22036801). Digest 23.09 candidate.

---
An AI agent's rebuild is only as good as the process that produced it. Prior work found that once a model is strong enough, a multi-agent rebuild pipeline loses to the simplest approach: giving the model the original code and one instruction (AgentModernize).

**rebuild-dossier**: open-source tool that locks an application's real interface — its exact inputs and outputs — before any code is written, then enforces one-test-at-a-time building through automated checks, not written instructions alone.

Three results (differing amounts of evidence):
1. **Small comparison:** the compliant agent failed a held-back test while the rule-breaking agent passed everything — proof that a passing suite doesn't certify correctness when tests can be gamed.
2. **vs "source + one instruction":** tied on a small app, but lost outright on a larger one where the automated check wasn't even running — pointing to the check mechanism (not interface-locking) as the differentiator; interface-locking held up separately.
3. **Three-level checking:** every claim checked at three levels — the agent's own report, an automated log, and the actual files produced — catching real errors (including a bug in the authors' own logging code) that a single level would have missed.

Reproduces on a different model and toolchain: a stronger model followed the process three times running, something the weaker model never managed.

QA relevance (digest): passing suite doesn't certify correctness when tests can be gamed; simple transfers (code + one instruction) often beat complex multi-agent pipelines; new validation criteria for AI rebuilds; multi-level evidence (report + log + files) as a QA pattern — aligns with VerdictGate's evidence/attestation thinking.
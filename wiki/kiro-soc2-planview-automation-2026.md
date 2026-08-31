# Planview Saves 40+ Hours per Audit Cycle with SOC 2 Automation

**Source:** https://kiro.dev/blog/automating-soc-2-compliance/
**Date:** April 10, 2026
**Authors:** Medha Aiyah, Keerthi Konjety (Kiro), Mukesh Belde, Faizan Mansuri (Planview)
**Tags:** #soc2 #compliance #kiro-cli #custom-agents #aws
**Raw:** [kiro-soc2-planview-automation-2026.md](../raw/kiro-soc2-planview-automation-2026.md)

---

## What It Is

Planview (strategic portfolio mgmt, 3K+ customers) cut SOC 2 audit prep from 40+ hours per annual cycle (manual evidence across 20+ AWS services, spreadsheet archaeology, multi-person coordination) to automated, on-demand evidence collection via Kiro CLI custom agent.

Evaluated commercial continuous-compliance platforms Q1 2025 but needed interim quick value without full platform overhead — Kiro fit as workflow-integrated interim that doesn't block future platform adoption.

## Custom Agent Setup

**File:** `~/.kiro/agents/soc2-compliance.json` — purpose-built assistant with scoped tools.

```json
{
  "name": "soc2-compliance",
  "description": "SOC 2 compliance work",
  "prompt": "./prompts/soc2-expert.md",
  "tools": ["read","write","aws"],
  "allowedTools": ["read"],
  "toolsSettings": {
    "write": {"allowedPaths": ["compliance docs","policies","audit"]},
    "aws": {"allowedServices": ["IAM","CloudTrail","Config","GuardDuty","SecurityHub","Inspector","KMS","S3"]}
  },
  "aws": {"autoAllowReadonly": true},
  "resources": ["policies/*.md","compliance/*.md","audit/*.json","security/*.yaml"]
}
```

- `autoAllowReadonly` → `describe-*`, `list-*`, `get-*` don't require approval → 40h manual → automated.
- `allowedServices` + `allowedPaths` = least privilege, non-invasive read-only.
- Alternative: `/help Help me create a custom agent for soc-2 compliance` → Kiro's `/help` agent introspects docs and drafts config + prompt.

**Launch:** `kiro-cli --tui --agent soc2-compliance` (or `--classic` or `/agent` inside CLI). Loads context + permissions.

## Usage

Prompt: `Generate SOC 2 CC6.1 compliance report showing all S3 buckets with encryption, public access, access logging.`

Agent:
- Queries 34 buckets across all regions (S3 configurations)
- Checks encryption + KMS, ACLs + bucket policies, access logging
- Generates timestamped evidence formatted to control requirements
- Can also generate scripts for repeatable queries

*Note:* AI output depends on prompt specificity; not a replacement for deterministic compliance tools; requires qualified professional review before auditor submission.

## Results

- **40+ hours saved** per cycle → redirected to customer features
- **60% overall efficiency gain**, 3-4x faster audit response
- **1-1.5 SDE sprint per member** saved per cycle
- **On-demand evidence** → prepare throughout year, not just pre-audit crunch
- Integrates without changing dev environment; evidence aligned to SOC 2 and ISO controls via existing workflow

Planview expanding to other use cases (infra monitoring agent querying CloudWatch, S3, Lambda for health reports).

## Relevance to QA/QE

| Pattern | QA Application |
|---------|----------------|
| Custom agent with scoped read-only | QA evidence agent: read-only access to CI, test reports, infra → generate evidence with timestamps |
| `allowedServices` least privilege | Apply to QA: allow read on test artifacts, block write to prod |
| Prompt → evidence + script | Generate repeatable evidence scripts (not just one-off report) |
| On-demand vs crunch | Shift-left compliance: continuous evidence vs annual scramble |

## Critical Analysis

**Strengths:**
- Concrete enterprise outcome (40h, 60%, 1-1.5 sprints) with real customer.
- Least-privilege design + read-only safety.
- Interim solution narrative — pragmatic vs platform lock-in.

**Gaps:**
- AI-generated compliance still requires human validation — disclaimer explicit.
- No detail on drift detection or control coverage %; success metric is time saved, not audit pass rate.
- AWS-centric (IAM, S3, etc.) — other providers need adaptation.

## Cross-links

- Related: [Kiro and Snyk guardrails](kiro-snyk-guardrails-2026.md) — same custom agent + MCP pattern, security layer
- Related: [Root cause 33s](kiro-root-cause-33s-2026.md) — same Kiro CLI, different domain
- Concept: [SOC 2 / ISO evidence automation](iso-27001-qa-testing-2026.md)

---

*Ingested: 2026-08-30*

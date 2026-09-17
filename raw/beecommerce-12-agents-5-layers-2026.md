# BeeCommerce — 12 AI Agents, 5 Layers, Zero Hiring (2026)

**Source:** https://beecommerce.pl/en/blog/12-agents-no-recruitment-ai-dev-team
**Company:** BeeCommerce (Lublin/Warsaw, Poland) — headless e-commerce software house
**Date:** 2026-04-20
**Timeline:** 15 months (Jan 2025 → Apr 2026) from "write us a function" to 12-agent production pipeline

---

## Architecture: 5 Layers, 12 Agents

### Layer 0 — Strategic Advisory (new features only)
- **Visionary** — market trends, innovation, "demo factor" (can you show this off?)
- **Pragmatist** — risk, TRL 1-9, costs, "is there a simpler 80/20 solution?"
- Deliberately independent — don't influence each other

### Layer 1 — Core Development (parallel)
- **PM** — breaks briefs, coordinates agents, manages pipeline, logs architecture decisions, reports. Knows human team + escalation triggers.
- **Backend Developer** — API, business logic
- **Frontend Developer** — Next.js, Vite, Storyblok, Tailwind. Knows `output: 'standalone'` for Docker.

### Layer 2 — Quality & Security (parallel)
- **Code Reviewer** — OWASP Top 10, SOLID, TypeScript strict. **Read-only**: reads, reports, doesn't edit. Loops back to developer with specific feedback.
- **QA Tester** — acceptance criteria, E2E tests, smoke tests on K8s (CrashLoopBackOff, probes, ingress).
- **Security Engineer** — OWASP, container security (non-root, alpine, .dockerignore), K8s security context, ExternalSecrets. **On every MVP**, not quarterly.

### Layer 3 — Optimization & Delivery
- **DevOps K8s** — image build → registry → tag update → ArgoCD sync. Helm, ExternalSecrets, RBAC, 1Password, Kyverno cluster constraints.
- **Performance Engineer** — Core Web Vitals (LCP < 2.5s, INP < 200ms, CLS < 0.1), bundle size, resource quotas, rollout stability.

### Layer 4 — SEO & Analytics (frontend only)
- **SEO Specialist** — meta tags (title 50-60, desc 150-160), H1-H6, robots.txt, sitemap, Schema.org, hreflang. **Read-only.**
- **Web Analyst** — GTM, GA4, dataLayer (reset before routeChange in SPA!), custom events, firing rates.

---

## Pipeline

```
Phase 0: Visionary + Pragmatist         → strategic review (new features only)
Phase A: Backend + Frontend             → implementation (parallel)
Phase B: Code Review                    → fix loop until APPROVED
Phase C: Security + Performance + QA    → audit, E2E, acceptance criteria (parallel)
Phase D: SEO + Web Analyst              → frontend quality (frontend only)
Phase E: DevOps K8s                     → deploy to cluster
                                        → PM Final Report
```

Quality gates: Code Review must pass BEFORE Security starts. SEO doesn't fire for pure backend. Deploy always last.

---

## Key Patterns

### Context-as-a-Service
- Agents are technologically agnostic (no repo names, URLs, GTM IDs in definitions)
- Same 12 agents serve **dozens of projects**
- Each project = one context file (repo, URLs, specific rules, analytics IDs)
- PM reads context at kickoff → distributes path to all agents
- New project = new context file → entire team knows it instantly

### Read-Only Quality Agents
Code Review and SEO are read-only: they report findings, don't edit code. Forces human decision on whether to fix.

### Escalation, Not Guessing
Every agent has a human owner and backup. When agent doesn't know → escalates to human, doesn't guess.

### The Real Problem
> "Writing code accounts for maybe 30% of the work. The rest is 'glue': Dockerfile, RBAC, code review, security audit, E2E tests, GTM config, meta tags, post-deploy smoke tests. This isn't a code problem. It's a **context management problem at scale**."

---

## Key Quotes

- "An agent doesn't write better code than a senior. But a senior writes better code when the agent handles review, testing, SEO, analytics, and deployment. This isn't replacing legs — it's an exoskeleton."
- "The question 'will AI replace developers' is poorly framed. The right question: how much of a developer's work is actually context management?"
- "Every agent has a human owner and backup. When an agent doesn't know — it escalates to a human, it doesn't guess."

---

## Connections to Our Work

- **Context file = AGENTS.md / per-project context:** same pattern — agents are generic, context makes them project-specific.
- **Read-only quality agents = attestor role:** Code Reviewer reports but doesn't fix. SEO reports but doesn't edit. This IS the governance model.
- **"Context management at scale" = Article 27 thesis:** QA role shifts from running tests to governing the evidence/context system.
- **Quality gates = per-risk-tier:** Code Review → Security → Deploy ordering. Same as B0 always → B2/B3 optional.
- **"Exoskeleton, not replacement"** = direct quote candidate for Article 27.
- **15 months to 12 agents** = realistic timeline reference. Not overnight.
- **Security on every MVP** = our B0 (always verify high-risk). They prove it's practical at scale.
- **Escalation protocol** = our stop-rules. Agent doesn't know → ask human.

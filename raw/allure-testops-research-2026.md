# Allure TestOps — research notes

**Date:** 2026-06-16
**Source URLs:**
- https://qameta.io/ (main)
- https://docs.qameta.io/allure-testops/ (docs)
- https://docs.qameta.io/allure-testops/setup/architecture/
- https://docs.qameta.io/allure-testops/install/docker-compose/
- https://docs.qameta.io/allure-testops/integrations/github/
- https://qameta.io/cloud-pricing

## 1. What it is

**Allure TestOps** is a Test Management / TestOps platform from Qameta Software. It centralizes manual + automated test cases, runs, and analytics. Not the same as **Allure Report** (open-source, static HTML report generator).

### Two products in the family
| Product | Type | Purpose |
|---------|------|---------|
| **Allure Report** | Open source (Apache 2.0) | Static HTML reports from test results |
| **Allure TestOps** | Commercial (Cloud or Self-hosted) | Server, dashboards, manual+auto test management, CI integration |

### Position vs other TMS
- **Allure Report** ↔ TestNG/Extent for HTML reports
- **Allure TestOps** ↔ TestRail / Zephyr Scale / Xray for test management
- We use **Allure Report** today (qaa-sandbox + OrangeHRM already have `allure-playwright`)

## 2. Key features (out-of-the-box)

From official docs:
- **Test cases:** manual + automated, real-time auto-documentation from test runs
- **Test plans:** combined manual + automated
- **Test runs:** start, stop, rerun jobs in CI from Allure UI
- **Test results:** real-time aggregation, defect linking, issue tracker export
- **Analytics:** built-in dashboards + AQL (Allure Query Language) for custom KPIs
- **Smart Test Cases:** auto-generated test documentation from results

### Test framework support (relevant to us)
- JavaScript/TypeScript: **Allure Playwright**, Allure Cypress, Allure Cucumber.js
- Python: Allure Pytest, Behave, Robot
- Java, C#, PHP, Ruby: many adapters

## 3. Deployment options

### 3.1 Allure TestOps Cloud (SaaS)
- Hosted on Qameta AWS infrastructure
- Pricing: **$39/user/month** (1-30 users), volume discounts
  - 31-50: $36
  - 51-100: $34
  - 100+: $30
  - Annual: 10% discount
- 60 GB storage included
- Free trial: 30 days (request via qameta.io/cloud-trial-request)
- **No IT required** — Qameta maintains

### 3.2 Allure TestOps Self-hosted (on-premise)
Two install methods:
- **Docker Compose** — small/medium (≤3K tests/launch, ≤30K tests/day)
- **Kubernetes Helm chart** — production / HA

#### Architecture (5 components)
**Stateful (must be external in production):**
- PostgreSQL 15+ (data)
- RabbitMQ (message queue, 3.x for HA, 4.0+ supported from 26.2.1.4)
- S3-compatible storage (AWS S3, MinIO, Ceph) — for artifacts/screenshots/videos
- Redis (sessions, in-RAM)

**Stateless:**
- Allure TestOps service (Java/Spring)

#### Minimum hardware (small project)
- 4 vCPU, 8 GB RAM for Allure service
- PostgreSQL on SSD: ~300 GB/year for 100K tests with daily runs
- Object storage: 50 GB+ SSD
- Supported OS: Ubuntu 20.04/22.04/24.04 LTS, CentOS/RHEL 8+

#### License
- Self-hosted requires license key from sales
- License + credentials to Qameta Docker registry (private images)

### 3.3 Allure TestOps Sandbox (evaluation)
- Public sandbox at `sandbox.testops.cloud`
- Pre-loaded with demo data
- Free, for evaluation only — not for real projects

## 4. GitHub integration (relevant to us)

All our projects use **GitHub Actions**. The integration flow:

### 4.1 Upload results: GH → Allure TestOps
1. Add `allure-framework/setup-allurectl@v1` action to workflow
2. Wrap test command: `allurectl watch -- <test-command>`
3. Set env: `ALLURE_RESULTS` to allure output dir
4. Pass API token via `${{ secrets.ALLURE_TOKEN }}`

### 4.2 Trigger workflows: Allure TestOps → GH
1. Create global GitHub integration (admin): endpoint, name
2. Create PAT (fine-grained or classic with `workflow` scope)
3. Add to project settings as secret
4. Configure Job in Allure TestOps (links to GH workflow)
5. Add `workflow_dispatch` inputs to .yml: `ALLURE_JOB_RUN_ID`, `ALLURE_USERNAME`
6. Sync job: **Update job from the build server**

### 4.3 Bi-directional flow
- Allure TestOps stores launch ID → passes to GH workflow
- GH runs tests, allurectl uploads results
- Allure TestOps UI shows live status

### 4.4 Environment tracking
- Map workflow env vars → Allure TestOps environment variables
- Examples: `GITHUB_REF_NAME` → Branch, custom vars → Browser/Product

## 5. Current state in our projects

**Already have `allure-playwright` reporter enabled:**
| Project | Reporter | `allure-results/` | CI upload |
|---------|----------|-------------------|-----------|
| qa-automation-sandbox | ✅ enabled | ✅ exists | ❌ local only |
| OrangeHRM | ✅ enabled | ✅ exists | ❌ local only |

**Current setup (sandbox, lines 5-7 of playwright.config.ts):**
```typescript
reporter: [
  ['html'],
  ['junit', { outputFile: 'test-results/junit.xml' }],
  ['allure-playwright']
],
```

Tests produce `allure-results/*.json` files. We then run `npx allure generate` → static HTML in `allure-report/`. **No server, no aggregation across runs.**

**What Allure TestOps would add:**
- Cross-launch history (currently we have no aggregate view)
- Test case auto-documentation (currently ad-hoc)
- Trends/dashboards
- Manual test cases alongside automated
- Defect linking
- Trigger tests from UI

## 6. Pros / Cons for us

### Pros
- **Low migration cost:** we already produce allure-format results
- **Cloud option** = no infrastructure (we don't have K8s/DBA)
- **GitHub-native:** fits our CI/CD stack
- **AQL** = custom KPIs (could feed DORA + QA metrics dashboards)
- **Smart Test Cases** = auto-generated test docs

### Cons
- **Cost:** $39/user/mo minimum; even for 3 users = ~$1,400/year (Cloud)
- **Self-hosted overhead:** 4 services to maintain, license key required, license loss = integrations break
- **Vendor lock-in:** test cases and dashboards live in their DB
- **No free tier** (only 30-day trial)
- **Cloud = data leaves our control** (test artifacts on Qameta AWS)
- **Not OSS** (vs TestRail, Zephyr — same commercial model)

## 7. Alternatives (for context)

| Tool | Type | Cost | Notes |
|------|------|------|-------|
| **Allure TestOps Cloud** | SaaS | $39/u/mo | Best DX for Allure users |
| **Allure TestOps Self-hosted** | Docker/K8s | License + infra | For regulated/enterprise |
| **TestRail** | SaaS/On-prem | Custom ($) | Mature, manual-heavy |
| **Zephyr Scale** (Jira plugin) | SaaS | $) | Tight Jira integration |
| **Xray** (Jira plugin) | SaaS | $) | Strong BDD, Jira native |
| **Testsigma** | SaaS/OSS | Free+Pro | Codeless, AI-driven |
| **None + GitHub PR comments** | DIY | $0 | What we have now |

## 8. Open questions for decision

1. **Who is the audience?** Solo portfolio projects (no team) vs demo for employers (need polish)
2. **What problem are we solving?** Lack of trend history across runs, or lack of test case docs, or just wanting to try?
3. **Budget tolerance?** $0 (use sandbox only) / $39-100/mo (Cloud single user) / $1-2K/yr (Cloud team) / $5K+/yr (self-hosted with infra)
4. **Privacy constraints?** Test artifacts may contain prod URLs, test users (Buzzhive has `alice@buzzhive.com` etc.) — can those go to Qameta cloud?
5. **Future direction?** Just collecting info, or planning to deploy in next 1-3 months?

## 9. Initial deployment plan (DRAFT — pending answers)

### Phase 0: Evaluation (1-2 days, $0)
1. Sign up for 30-day free trial at https://qameta.io/cloud-trial-request
2. Create 2 test projects: `qa-sandbox-testops`, `orangehrm-testops`
3. Add `allurectl` to one workflow in each project (smoke only)
4. Verify results appear in TestOps Cloud
5. Trigger workflow from Allure UI (bi-directional test)

### Phase 1: Pilot on one project (1 week, $0 if using trial)
- Pick **qa-automation-sandbox** (more diverse: API+UI+DB+chaos)
- Add `allurectl` to `playwright.yml` and `nightly.yml`
- Add `workflow_dispatch` inputs for bi-directional triggers
- Build 1-2 dashboards: launch history, test case coverage by feature
- Document workflow for team

### Phase 2: Roll out to OrangeHRM (1-2 days)
- Same as Phase 1 but simpler (UI only, no chaos/DB)
- Compare results to manual report

### Phase 3: Decision point
- **If we like it:** budget for Cloud subscription ($39-117/mo for 1-3 users)
- **If not:** stop using, remove allurectl from workflows (no code changes, just env vars)

### Phase 4 (optional, if budget approved): Self-hosted
- Only if data residency or cost at scale becomes issue
- Render.com or similar doesn't fit (need stateful Postgres + RabbitMQ + S3 + Redis)
- Realistically: needs a VM (Hetzner, DigitalOcean) or K8s cluster (~$50-200/mo infra)

## 10. Risk matrix

| Risk | Probability | Impact | Mitigation |
|------|------------|--------|------------|
| Trial expires before we decide | High | Low | Phase 0 in 2-3 days max |
| Cloud data residency concerns | Medium | Medium | Use trial, decide self-hosted if blocker |
| License key loss = integrations break | Low (Cloud) / High (Self-hosted) | High | Backup crypto password, document recovery |
| Migration cost from existing reports | Low | Low | Both projects already produce allure-format |
| Allure TestOps shuts down / pivots | Low | High | We can fall back to local Allure Report (OSS) — no data lock-in for test RESULTS, only for dashboards/test cases |

## 11. References

- [Allure TestOps main](https://qameta.io/)
- [Allure TestOps docs](https://docs.qameta.io/allure-testops/)
- [Architecture](https://docs.qameta.io/allure-testops/setup/architecture/)
- [Docker Compose install](https://docs.qameta.io/allure-testops/install/docker-compose/)
- [GitHub integration](https://docs.qameta.io/allure-testops/integrations/github/)
- [Cloud pricing](https://qameta.io/cloud-pricing)
- [allurectl docs](https://docs.qameta.io/allure-testops/ecosystem/allurectl/)
- [AQL docs](https://docs.qameta.io/allure-testops/advanced/aql/)
- [Allure Framework (OSS)](https://allurereport.org/)

---
source: "allure-testops-research-2026.md"
ingested: "2026-06-16"
generator: "llama-3.3-70b-versatile (Groq)"
---

# Allure TestOps

## 1. Summary

Allure TestOps is a Test Management and TestOps platform that centralizes manual and automated test cases, runs, and analytics. It offers a range of features, including test case management, test planning, and real-time analytics. By integrating Allure TestOps with our existing GitHub Actions workflow, we can streamline our testing process and gain valuable insights into our test results.

> **Key distinction:** Allure TestOps (commercial server) ≠ Allure Report (open-source static HTML). We already use Allure Report in `qa-automation-sandbox` and `OrangeHRM` — adding TestOps is an evolution, not a migration.

---

## 2. Key Concepts

| Concept | Description |
| --- | --- |
| **Allure Report** | Open-source static HTML report generator (Apache 2.0). We use this today. |
| **Allure TestOps** | Commercial Test Management / TestOps platform (Cloud or Self-hosted). |
| **Test Cases** | Manual and automated tests managed in one repository. Auto-documented from runs. |
| **Test Plans** | Combined manual + automated test plans, runnable from one place. |
| **Test Runs** | Test executions started, stopped, and rerun from Allure UI. |
| **Analytics** | Real-time dashboards with built-in KPIs. |
| **AQL** | Allure Query Language — custom KPI queries (think SQL for test data). |
| **Smart Test Cases** | Auto-generated test documentation from latest results. |
| **allurectl** | CLI tool that uploads results from CI to TestOps. |
| **Bi-directional GH integration** | TestOps → trigger GH workflow, GH → upload results to TestOps. |

---

## 3. Practical Applications for our team

| Application | How it helps | Implementation |
| --- | --- | --- |
| **Cross-launch history** | Aggregates all Playwright runs into a single view. Trends across runs. | Keep `allure-playwright` reporter, add `allurectl watch` to GH Action. |
| **Auto test documentation** | Smart Test Cases turn JSON results into readable specs. | No code changes — just run tests, TestOps generates docs. |
| **Trend dashboards** | AQL-driven charts: pass-rate drift, flaky-test frequency. | Build "Launch History" and "Feature Coverage" dashboards. |
| **Defect linking** | Attach GitHub Issues / Jira tickets to failing cases. | Configure integration in project settings. |
| **Trigger tests from UI** | QA leads start regression suites with a button. | Add `workflow_dispatch` inputs to GH workflow + PAT. |
| **Environment tracking** | Map GH env vars (branch, browser) to TestOps variables. | Configure environment variable mappings. |

### Our current state (verified)
- ✅ `qa-automation-sandbox` and `OrangeHRM` already have `allure-playwright` reporter enabled in `playwright.config.ts`
- ✅ Both produce `allure-results/*.json`
- ❌ No server — only local HTML reports
- ➡️ Adding TestOps = add `allurectl` to workflows (no test code changes)

---

## 4. Pilot Plan

### Phase 1: Evaluation (1-2 days, $0)
1. Sign up for 30-day free trial at [qameta.io/cloud-trial-request](https://qameta.io/cloud-trial-request)
2. Create 2 test projects: `qa-sandbox-testops`, `orangehrm-testops`
3. Add `allurectl` to one workflow in each (smoke tests only)
4. Verify results appear in TestOps Cloud
5. Trigger workflow from Allure UI (bi-directional test)

### Phase 2: Pilot on `qa-automation-sandbox` (1 week)
- Add `allurectl` to `playwright.yml` and `nightly.yml`
- Add `workflow_dispatch` inputs for bi-directional triggers
- Build 1-2 dashboards: launch history, test case coverage by feature
- Document workflow for team

### Phase 3: Roll out to `OrangeHRM` (1-2 days)
- Same as Phase 2 but simpler (UI only, no chaos/DB)
- Compare results to manual report

### Phase 4: Decision point
- **If we like it:** budget for Cloud subscription ($39-117/mo for 1-3 users)
- **If not:** stop using, remove `allurectl` from workflows (no code changes, just env vars)

### Phase 5 (optional, if budget approved): Self-hosted
- Only if data residency or cost at scale becomes an issue
- Render.com doesn't fit (need stateful Postgres + RabbitMQ + S3 + Redis)
- Realistically: needs a VM ($50-200/mo infra) or K8s cluster

---

## 5. Risk Matrix

| Risk | Likelihood | Impact | Mitigation |
| --- | --- | --- | --- |
| **Vendor lock-in** (test cases in Qameta DB) | Medium | High | Keep `allure-results/*.json` archived — can fall back to local Allure Report (OSS) anytime |
| **Cost overrun** ($39/user/mo can grow) | High | Medium | Set budget alert; review quarterly; self-hosted option if >$200/mo |
| **Trial expires before decision** | High | Low | Phase 1 in 2-3 days max |
| **Data residency concerns** (Cloud stores on Qameta AWS) | Medium | Medium | Use trial, decide self-hosted if blocker |
| **License key loss = integrations break** (self-hosted) | Low (Cloud) / High (Self-hosted) | High | Backup `TESTOPS_CRYPTO_PASSWORD` securely; document recovery |
| **Integration breakage** after upgrade | Low | Medium | Read release notes before upgrading; pin version |
| **Allure TestOps company pivots/shuts down** | Low | High | Open-source Allure Report still works — no data lock-in for results, only for dashboards/cases |

---

## 6. Decision Checklist

Before committing to Allure TestOps (or any TMS), answer:

1. **What problem are we solving?**
   - [ ] Lack of trend history across runs
   - [ ] Lack of test case documentation
   - [ ] Need for manual+auto combined plans
   - [ ] Just exploration / "nice to have"

2. **Who is the audience?**
   - [ ] Solo portfolio (no team)
   - [ ] Demo for employers (need polish)
   - [ ] Small team (2-5 people)
   - [ ] Large org (10+ users)

3. **Budget tolerance?**
   - [ ] $0 — sandbox only
   - [ ] $39-100/mo — Cloud single user
   - [ ] $1-2K/yr — Cloud team
   - [ ] $5K+/yr — self-hosted with infra

4. **Privacy constraints?**
   - Test artifacts may contain prod URLs, test users
   - Can those go to Qameta Cloud (AWS)?
   - [ ] Yes — Cloud OK
   - [ ] No — need self-hosted

5. **Migration cost?**
   - We already produce allure-format results → low cost
   - Would need to add `allurectl` to workflows (~30 min per project)
   - [ ] Acceptable
   - [ ] Too much

6. **Future direction?**
   - [ ] Just collecting info
   - [ ] Pilot in 1-3 months
   - [ ] Deploying soon (this quarter)

7. **Vendor lock-in tolerance?**
   - Test cases + dashboards in Qameta DB
   - Results (JSON) stay in our repo
   - [ ] OK with lock-in for convenience
   - [ ] Need open standards (consider TestRail API, or OSS tools)

---

## 7. Cost Reference (Cloud)

| Users | Monthly | Annual (10% off) |
|-------|---------|------------------|
| 1-30 | $39/u | ~$35/u |
| 31-50 | $36/u | ~$32/u |
| 51-100 | $34/u | ~$31/u |
| 100+ | $30/u | ~$27/u |
| **3 users (estimate)** | **$117/mo** | **~$1,264/yr** |
| **5 users** | **$195/mo** | **~$2,106/yr** |

Storage: 60 GB included per plan. Enterprise plans: custom quote.

---

## 8. References

- [Allure TestOps main](https://qameta.io/)
- [Allure TestOps docs](https://docs.qameta.io/allure-testops/)
- [Architecture](https://docs.qameta.io/allure-testops/setup/architecture/) — 5-component stack
- [Docker Compose install](https://docs.qameta.io/allure-testops/install/docker-compose/)
- [GitHub integration](https://docs.qameta.io/allure-testops/integrations/github/) — bi-directional flow
- [Cloud pricing](https://qameta.io/cloud-pricing) — $39/user/month
- [allurectl docs](https://docs.qameta.io/allure-testops/ecosystem/allurectl/)
- [AQL docs](https://docs.qameta.io/allure-testops/advanced/aql/)
- [Public sandbox](https://sandbox.testops.cloud/) — for evaluation

---

*Generated by Groq llama-3.3-70b — ingested from `raw/allure-testops-research-2026.md`*

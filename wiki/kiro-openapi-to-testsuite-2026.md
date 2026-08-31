# From OpenAPI/Swagger to Test Suite in Seconds

**Source:** https://kiro.dev/blog/from-openapi-swagger-to-test-suite-in-seconds-with-kiro/
**Date:** June 25, 2026
**Author:** Sumitha AP, Rajdeep Mukherjee
**Tags:** #openapi #swagger #api-testing #mock-server #kiro
**Raw:** [kiro-openapi-to-testsuite-2026.md](../raw/kiro-openapi-to-testsuite-2026.md)

---

## What It Is

Kiro treats OpenAPI/Swagger spec as source of truth and generates a runnable Node.js integration test suite in seconds: test client (axios), mock Express server, config toggle, HTML/MD report, no external test framework. Prompt: `Generate Node.js test suite from https://petstore.swagger.io using axios, Express for mocking, no external test frameworks`.

**Problem:** Spec and tests drift when maintained separately. Tests from launch grow stale; new endpoints ship without coverage. OpenAPI Generator gives stubs with minimal assertions (green CI, no real coverage — e.g., 400 returned as 500 slips through). Kiro reasons over spec: infers payloads from schemas, resolves enums to realistic values, asserts status codes and schemas, builds mock matching spec behavior.

## Solution Overview (PetStore Example)

**Prereq:** Node.js, Kiro installed, OpenAPI URL.

**Steering file:** `*.kiro/steering/openapi-test-generation.md` — persistent team standards (define once, apply to all prompts).

**Generated project:**
- `config.js` — `useMockServer: true` (local) / `false` (live) toggle
- `mock-server/server.js` — Express handlers per endpoint, realistic responses per schema
- `test/` — files by resource (pet, store, user), assertions on status codes and payload shape
- `test-runner.js` — vanilla Node runner (no framework conflicts), discovers tests, tracks pass/fail

**How Kiro parses spec:**
1. Identify every endpoint + method (PetStore: POST /pet, GET /pet/{petId}, PUT, DELETE, etc.)
2. Infer request payloads from model definitions (Pet: id, name, category, photoUrls, tags, status)
3. Generate assertions on expected response codes (200, 201, 404, 405 per spec)
4. Create matching mock routes with consistent response schemas

## Running Tests

**Mock server:** Prompt `Run the tests with the mock server` → starts Express on ephemeral port, in-memory seed data, deterministic, no network.

**Quality classification:** Integration tests (TCP, middleware, routing, handler, store, JSON), not unit. Multi-request chains (e.g., DELETE lifecycle: POST → DELETE → GET 404 verifies state transition, not just response code). Self-sufficient fixtures (create own pet, not relying on seed) → order-independent, though no per-test state reset yet. Strengths: happy + error paths, real assertions. Gaps: no full JSON schema validation, no auth.

**Live API:** `PETSTORE_URL=https://petstore.swagger.io npm test` or prompt `Run tests with real server`. Failures triage:
- Real API more permissive than spec (spec 405 vs live 200) → decide mock vs live truth
- Error code semantics differ (400 vs 404)
- Response shape mismatch → update mock/test
- Shared state assumptions break (live lacks seed data) → make tests self-sufficient
- Not about green in both modes; about surfacing assumption drift.

**Auth for internal APIs:** shared client factory + config for credentials (env-based), plus dedicated auth-enforcement tests (no creds → 401, expired → 401, wrong scope → 403).

**Headless regeneration:** `kiro --headless` in CI/CD → regenerates suite on spec change, hooks surface drift early.

## Relevance to QA/QE

| Capability | OpenAPI Generator | Kiro |
|------------|-------------------|------|
| Executable tests with assertions | Limited | Yes |
| Mock server | No | Yes |
| Realistic payloads (enum resolution) | Partial | Yes |
| Adapt to team standards (steering) | Custom templates | Yes |
| Regenerate on drift (headless CI) | Manual | Yes |

**Patterns:**
- Steering file = contract-testing standards as code.
- Mock + live toggle = shift-left + integration confidence.
- Round-trip verification (POST-DELETE-GET) = genuine state proof, not status-code theater.

## Critical Analysis

**Strengths:**
- Zero-framework, parallel-safe (ephemeral port), deterministic.
- Produces meaningful assertions vs stubs.

**Gaps:**
- No per-test isolation (state leak risk), no full schema validation, no auth by default — need hardening for prod-grade suite.
- Mock strictness may diverge from live leniency — requires triage discipline.

## Cross-links

- Related: [Bug fix paradox](kiro-bug-fix-paradox-2026.md) — preservation vs fix properties complement contract tests
- Related: [Root cause 33s](kiro-root-cause-33s-2026.md) — Kiro CLI investigation vs generation
- Catalog: [Kiro blog catalog](kiro-blog-catalog-all-publications-2025-2026.md)

---


## Triage Checklist (Mock vs Live Drift)
When live run fails but mock passes, ask:
1. Is spec wrong? (Live lenient, spec strict) → relax mock or tag test mock-only.
2. Are error codes underspecified? (400 vs 404 both plausible) → align on live as truth.
3. Is response shape evolving? (string vs object) → update schema assertion.
4. Is fixture missing live? (seed data exists only locally) → make tests self-seeding.
5. Is auth missing? (PetStore sandbox has none) → add shared client + 401/403 negative tests.

*Ingested: 2026-08-30*

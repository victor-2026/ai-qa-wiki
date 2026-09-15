# Recorder Locator Quality: playwright-cli 0.1.19 vs Human POMs (2026-09-09)

**Source:** hands-on micro-probe (Victor) following Anton Gulin's [browser-task-to-playwright-test](https://www.anton.qa/blog/posts/browser-task-to-playwright-test) (2026-09-09). Tool: `@playwright/cli@0.1.19` (`recording-start/stop`, scripted headless session, no manual input).
**Targets:** OrangeHRM 5.9 login (no testids) + Buzzhive/qa-automation-sandbox composer (testids present).

## What was recorded

OrangeHRM login (Admin + password + submit, landed on dashboard):

```js
await page.getByRole('textbox', { name: 'Username' }).fill('Admin');
await page.getByRole('textbox', { name: 'Password' }).fill('***');
await page.getByRole('button', { name: 'Login' }).click();
```

Buzzhive login + create-post ("locator-probe post", local :3000):

```js
await page.getByTestId('auth-email-input').fill('alice@buzzhive.com');
await page.getByTestId('auth-password-input').fill('alice123');
await page.getByTestId('auth-login-btn').click();
await page.getByTestId('post-composer-input').fill('locator-probe post');
await page.getByTestId('post-composer-submit').click();
```

## Findings

1. **Recorder priority confirmed empirically: testid > role.** Same tool, two apps: testids present → `getByTestId`; absent → `getByRole`. No configuration, automatic fallback.
2. **Buzzhive: convergence.** Recorder output is byte-identical in strategy to human specs (`[data-testid="post-composer-input"]` in `e2e/ui/posts.spec.ts`). Where testids exist, recording == human practice.
3. **OrangeHRM: divergence with clear trade-offs.** Recorder = role-based (`textbox "Username"`); human POM (`pom/LoginPage.ts`) = CSS/name-coupled (`input[name="username"]`, `button[type="submit"]`, `.oxd-*`).
   - Recorder dies on label rename (M1 Employee Id breaks `name: 'Username'`) — same failure mode as testRigor plain-English mode. Immune to CSS churn (M2).
   - POM survives M1 (names stable), vulnerable to class/attribute churn. Neither dominates; depends on what changes more often: labels or markup.
4. **Gulin's two points confirmed:** `fill` needs no click+select-all preamble (clean output); recording gives steps only — dashboard check after login is the human's job (saved-result check missing by design).
5. **Role names can be value-coupled:** Buzzhive login snapshot showed `textbox "admin@buzzhive.com"` (prefill/placeholder as name) — role-based naming is only as stable as the accessible name source.

## Methodology implication (proposal, not decree)

- **Matrix extension candidate M7 (attribute rename):** current M0-M6 attack labels (M1), classes (M2), structure (M4/M5). No mutant attacks the `name` attribute — which kills POM-style locators but not recorder/testid ones. M7 would complete the locator-strategy coverage: role vs name vs testid each get their killer mutant.
- **Authoring guideline (hybrid):** testid > role > name > css, plus record-then-review workflow (recorder drafts steps, human adds saved-result checks + test data). Matches both observed convergences.
- **Caveat:** single probe, two apps — signal, not proof. Re-run per app before hardening into a rule.

## Links

- Gulin tutorial (method source) + ten-run check (companion piece, reliability angle)
- Human baselines: `OrangeHRM/pom/LoginPage.ts`, `qa-automation-sandbox/e2e/ui/posts.spec.ts`
- Tool eval context: Agentiqa pilot M1/M2 (role-heal vs CSS-immunity), testRigor text-axis
- Stand: OrangeHRM via mutant-proxy :8082 (M0); Buzzhive local :3000 (one "locator-probe post" left in local DB, throwaway)

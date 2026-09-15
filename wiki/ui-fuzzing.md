# UI Fuzzing — Mutation Through Input

Fuzz testing for web UI: inject malformed, unexpected, or boundary-breaking data into forms, search fields, file uploads, and navigation — then verify the app doesn't crash, leak, or behave unpredictably.

## Why UI Fuzzing Matters
- Forms are the most common attack surface (XSS, SQLi, data leakage)
- Boundary conditions break things that normal testing misses
- Double-clicks, fast navigation, and concurrent actions expose race conditions
- File upload is a black box — any file type can be sent

## Fuzzing Strategies

| Strategy | Description | When to Use | Example |
|----------|-------------|-------------|---------|
| **Random** | Random data from pool | Find unexpected crashes | Random strings, numbers, files |
| **Boundary** | Edge values | Boundary conditions | 0, -1, MAX_INT, empty string, 10K chars |
| **Regression** | Known-bad patterns | Verify fixes | `' OR 1=1 --`, `<script>`, `%00` |
| **Known-bad** | OWASP patterns | Security | XSS, SQLi, path traversal, command injection |

## Checklist

- **Empty fields** — `loginForm.submit('', '')` → validation error, not 500
- **Long strings** — 10,000 chars in email → truncation or validation error
- **SQL injection** — `' OR 1=1 --` in search → 0 results, not data leak
- **Double-click** — fast Submit 2x → one request, no duplicate
- **Unicode in content** — emoji, hieroglyphs, null byte → correct rendering
- **XSS via form** — `<script>alert(1)</script>` in bio/displayName → escaped
- **Avatar upload** — non-image file, SVG with script, >10MB → error, not upload
- **Navigation history** — fast back/forward → consistent state

## Patterns (Playwright)

### Random Fuzzing (data-driven)
```typescript
const RANDOM_INPUTS = Array.from({ length: 10 }, () =>
  Math.random().toString(36).substring(2, 15)
);

for (const input of RANDOM_INPUTS) {
  test(`search handles random: "${input}"`, async ({ page }) => {
    await page.fill('[data-testid="search-input"]', input);
    await page.keyboard.press('Enter');
    await expect(page.locator('[data-testid="search-results"]')).toBeVisible();
  });
}
```

### Boundary Fuzzing (boundary values)
```typescript
const BOUNDARY_EMAILS = [
  '',                    // empty
  'a'.repeat(255),       // max length
  'a'.repeat(256),       // over max
  'user@',               // incomplete
  '@domain.com',         // no local part
  'user@.com',           // invalid domain
  'user@domain',         // no TLD
];

for (const email of BOUNDARY_EMAILS) {
  test(`register boundary email: "${email.slice(0, 20)}..."`, async ({ page }) => {
    await page.goto('/register');
    await page.fill('[data-testid="auth-email-input"]', email);
    await page.click('[data-testid="auth-register-btn"]');
    const error = page.locator('[data-testid="auth-error-message"]');
    await expect(error).toBeVisible({ timeout: 3000 });
  });
}
```

### Regression Fuzzing (known-bad patterns)
```typescript
const KNOWN_BAD = [
  { name: 'SQL injection', value: "' OR 1=1 --" },
  { name: 'XSS script', value: '<script>alert(1)</script>' },
  { name: 'Path traversal', value: '../../../etc/passwd' },
  { name: 'Null byte', value: '%00' },
  { name: 'Unicode overflow', value: '💀'.repeat(1000) },
];

for (const { name, value } of KNOWN_BAD) {
  test(`regression: ${name} in search`, async ({ page }) => {
    await page.fill('[data-testid="search-input"]', value);
    await page.keyboard.press('Enter');
    await expect(page.locator('[data-testid="search-results"]')).toBeVisible();
    expect(await page.content()).not.toContain('error stack');
  });
}
```

### XSS in Bio
```typescript
test('XSS in bio is escaped', async ({ page }) => {
  await login(page);
  await page.goto('/settings/profile');
  await page.fill('[data-testid="bio-input"]', '<script>alert(1)</script>');
  await page.click('[data-testid="save-profile"]');

  await page.goto('/profile');
  const bio = page.locator('[data-testid="user-bio"]');
  await expect(bio).not.toContainText('<script>');
});
```

## OWASP Top 10 Mapping

| OWASP Category | UI Fuzzing Approach |
|---------------|---------------------|
| A03: Injection | SQLi, XSS in form fields |
| A04: Insecure Design | Business logic bypass via rapid actions |
| A05: Security Misconfiguration | Error message leakage on invalid input |
| A07: Auth Failures | Empty/long credentials, session fixation |
| A08: Data Integrity | File upload type/size validation |

## Self-Evaluation (Post-Fuzz Audit)

1. **Correctness** — does each fuzz input match the stated strategy?
2. **Relevance** — does every fuzz case target a real input field?
3. **Stability** — deterministic input + assertion? No race conditions?
4. **Coverage** — at least 3 of 4 strategies used?

## Related Pages
- [[fault-injection]] — API/DB mutation, chaos engineering (complements UI fuzzing)
- [[Fuzzing]] — general fuzzing concepts
- [[Test-Reliability]] — test stability and determinism
- [[mas-testing-framework]] — mutation testing overview
- Reference skill: `~/.config/opencode/skills/ui-fuzzing/SKILL.md`

## Source
- Tags: #fuzzing, #ui-testing, #xss, #security, #boundary-testing, #owasp, #playwright

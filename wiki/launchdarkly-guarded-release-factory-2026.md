# LaunchDarkly: Guarded-Release Incident + AI Software Factory (Aug 2026)

**Source:** Alex Engelberg (Engineer), "Stories from the Factory Floor: Our AI software factory saved me from an incident", LaunchDarkly blog, 2026-08-14. Full text read 2026-10-07. URL: https://launchdarkly.com/blog/our-ai-software-factory-saved-me-from-an-incident/
**Status:** LaunchDarkly previously had zero coverage here (no wiki/raw/digest 07.10). Feed added: https://launchdarkly.com/blog/feed.xml (RSS, 1003 items, verified live).

## Company (Company-First profile)

LaunchDarkly (Catamorphic Co.) — feature flags → runtime control platform: **CodeControl** (ship with automated control) + **AgentControl** (agent behavior in prod; "Catch agent drift before customers do"). Solutions: Release AI-built code, Control AI agents, Optimize AI perf/cost, Self-heal systems, Experiments. Blog runs ongoing series "Stories from the Factory Floor" (closing the loop of AI SDLC): factory era, small-enough factory, factories-that-don't-look-like-factories, forgotten stack, private factory, self-driving ops triage loop (09-02), baseball side project, scariest code.

## The incident (guarded release catches routine cleanup)

API migration cleanup (last frontend caller, old→new endpoint) on the flag-targeting page — flagged "just in case". Guarded release (progressive traffic + metric watch + auto-rollback) fired: **13/243 errors on true variation vs 0/250 control** — statistically significant, rolled back before most users saw it. Debug: dashboard screenshot → Claude → Datadog, one shot. Root cause: entitlement check on the new endpoint (old never had it). Fix: remove check from read path; re-release green.

## Doctrine (their words)

Auto-flagging / auto-releasing / auto-cleanup take the annoying scaffolding off developers. "When a software factory automates this scaffolding, the hard parts of shipping more safely become the default." Guarded releases "save you when you least expect" — but guarding must be EASY, or cognitive cost discourages the safe choice.

## QA interpretation

Vendor-independent exhibit of the statistical gate with auto-rollback: treatment-vs-control with denominators published (13/243 vs 0/250). Safe-by-default doctrine = our gate language (cheap gates get used; expensive gates get skipped). Debug loop (screenshot → agent → observability) rhymes with Hari trace+decision packs. Article 26/29: guarded-release pattern as vendor-eval question ("show me your auto-rollback evidence").

## See also

- [[breaklight-ai-testing-methodology-whitepaper-2026]] — interval verdicts, WARN rule
- [[anthropic-spotify-quality-at-ai-speed-2026]] — rollback capacity, safeguards
- [[kenhuang-maestro-google-control-roadmap-2026]] — time-to-contain/revoke metrics

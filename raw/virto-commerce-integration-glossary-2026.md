# Virto Commerce — Integration Capabilities Glossary (2026)

**Source:** Oleg Zhuk (Virto Commerce CTO) email/LinkedIn post, 2026-08-17 + official deck: https://virtocommerce.github.io/vc-release-notes/presentations/integration-capabilities.html (via lnkd.in/eAa8bnkc)
**Context:** Virto Commerce Head of QA pipeline — interview prep; e-commerce domain terms.

## The Model: "A Door Per Audience"

Virto positions integrations as ready-made doors: every party gets a door built for them, one platform with "same data, same rules":

| Audience | Doors |
|----------|-------|
| Buyers | Storefront · app, Coupa · Ariba (Punchout), AI agents (UCP) |
| Your team | REST API, Integration middleware, Admin UI |
| Suppliers | Vendor API, Integration middleware, Vendor Portal |

## Terms

### xAPI (Experience API)
- Virto's storefront-facing API. "A new front end, not a new back end."
- One request per screen, with the buyer's own contract pricing already resolved server-side.
- Use: branded store, mobile app, customer portal, custom digital experiences.

### Punchout
- B2B procurement standard: buyer "punches out" of their procurement system (Coupa, Ariba, Jaggaer) into your catalog and brings a cart back.
- Flow: punchout request (cXML) → Virto verifies buyer, opens session with the right organization/contract → catalog at negotiated prices over xAPI → cart handed back (cXML) → approval → PO → order in Virto.
- Result: you appear inside the buyer's approval flow — no manual POs, no re-keying.

### cXML
- Message format procurement systems (Coupa, Ariba) use to talk to suppliers.

### eProcurement
- Software large organizations buy through: Coupa, Ariba, Jaggaer, Oracle. Budgets and approvals live here.

### UCP — Universal Commerce Protocol (⚠️ not Microsoft's UCP)
- Open standard that lets **AI agents browse, build a cart and check out** — agent-driven commerce.
- "The open standard Shopify, Walmart and Target are adopting." No adapter to build per agent: one verified endpoint, every compliant agent.
- Virto exposes it **over MCP**: "Universal Commerce Protocol through a verified MCP endpoint."
- Choose UCP when you want to be discoverable/buyable by AI assistants, or give customers a conversational reorder path.
- **Homonym warning:** UCP also = Universal Chat Protocol (Microsoft, agent↔agent messaging, Sep 2025) — different protocol, same acronym. Virto's UCP is commerce-specific.

### MCP — Model Context Protocol (commerce context)
- How an AI agent reaches tools and data such as your catalog. Virto ships a verified MCP endpoint that speaks UCP.

### REST API (seller side)
- For systems you already own: ERP, CRM, PIM, DAM, warehouse, BI, tax & payments.
- OpenAPI · token auth; every module publishes a schema.

### Integration middleware
- System between two others: map, transform, schedule, route, retry messages; holds enterprise-specific business logic.
- Virto delivery default: **Azure Function Apps**; alternatives Azure Logic Apps and others.
- Advantage: "enterprise-specific orchestration and transformation you can revise between releases, not per release."

### Admin UI
- Self-service configuration door for the business team.

### Vendor API / Vendor Portal
- Supplier-facing doors: Vendor API for supplier systems, Vendor Portal for unaided small vendors (feeds · CSV · SFTP).

## Release Strategy Terms (from Oleg's 3rd deck)

- Modules, bundles, release cadence, upgrade paths, hotfixes — "if I take this feature, when am I locked into an upgrade?" (presentation: lnkd.in/ezPExk6f)

## QA Relevance

- xAPI = the API surface QA tests for storefront (contract testing, pricing-per-buyer scenarios).
- Punchout flows = cross-system E2E (procurement ↔ catalog ↔ cart handback via cXML).
- UCP/MCP endpoint = agent-driven commerce: QA needs eval harnesses for agent ordering paths (discover → cart → checkout), audit trail parity with human channels.
- Integration middleware = contract + error-handling testing (retries, transformations).

*Created: 2026-08-17*

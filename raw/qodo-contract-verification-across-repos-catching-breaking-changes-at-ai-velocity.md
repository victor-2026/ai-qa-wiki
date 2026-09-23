# Qodo: Contract Verification Across Repos: Catching Breaking Changes at AI Velocity (2026-09-23)

**Source:** https://www.qodo.ai/blog/contract-verification-across-repos-catching-breaking-changes-at-ai-velocity/
**Context:** Qodo (ex-Codium) = AI code quality & governance platform. TIER 1.5 catalog candidate. Note: FULL READ - cross-repo = seams/attestor. Fetched 2026-09-23 with browser UA.

---

In most production systems, a single feature spans multiple repositories. A backend service defines an API, one or more clients consume it, a separate repository may generate SDKs, and another may package or deploy the resulting artifacts. Even build and configuration logic often lives outside the code it affects.
AI coding assistants and agents accelerate how quickly changes are introduced across the system, increasing the volume and scope of modifications that need to remain compatible. That speed is useful, but it changes the shape of software risk. When a developer moves faster in one part of the system, the rest of the system still needs to remain compatible with that change.
That is where failures tend to surface. Changes that look correct in isolation can introduce subtle mismatches across repository boundaries, only becoming visible when different parts of the system interact. Those interactions depend on shared contracts between producers and consumers. As long as the contract holds, both sides can evolve independently. When one side changes it without the other adapting, the integration breaks.
To review these changes safely, teams need more than repository-level context. They need to understand the contracts that connect repositories and verify that those contracts still hold.
Qodo treats this boundary as a first-class object. This post walks through how contract verification works across repositories in Qodo, and how the platform discovers those repository relationships in the first place so you do not have to wire them up by hand.
The contract is often larger than an API schema
When engineers hear “contract,” they often think of an API specification, a protobuf definition, or a typed interface. These are important, but they represent only part of the dependency surface between repositories.
A cross-repository contract can also be encoded in:
Function names and parameters
Request and response fields
Runtime messages
Build output paths
Environment variables
Configuration keys
Generated files
CLI
arguments
Package exports
CI/CD workflows
Deployment assumptions
Consider a payment platform split across three repositories:
payment-service
payment-sdk
checkout-web
The
payment-service
repository defines the payment API. The
payment-sdk
repository generates a TypeScript client from the service’s API schema. The
checkout-web
repository uses that SDK to create payments during checkout.
The service exposes the following endpoint:
POST /v1/payments
Content-Type: application/json
{
"amount": 100,
"currency": "USD"
}
The generated SDK provides a corresponding method:
payments.create({
amount: 100,
currency: "USD"
});
The checkout application uses that method:
await paymentClient.payments.create({
amount: cart.total,
currency: cart.currency
});
Together, these implementations form a contract. The endpoint path must match. The request fields and types must match. The generated SDK must represent the service correctly, and the application must use the SDK according to that interface.
Now imagine that a developer changes the service request format:
POST /v1/payments
Content-Type: application/json
{
"value": 100,
"currency_code": "USD"
}
The updated service may compile successfully. Its tests may also pass because the service implementation and its local test fixtures were updated together.
The SDK, however, may still generate or expose the previous interface:
payments.create({
amount: 100,
currency: "USD"
});
The checkout application also continues to pass
amount
and
currency
. Each repository may appear internally consistent, but the system contract no longer holds.
Automatically discovering repository relationships
Qodo uses cross-repository context to evaluate whether a proposed change remains compatible with the code that depends on it.
Cross-repository verification depends on knowing which repositories are connected. Maintaining these relationships manually becomes difficult as systems grow.
Services are split, SDKs are added, package names change, and new clients begin consuming existing APIs. CI/CD workflows also evolve over time. A manually maintained dependency map can quickly become incomplete.
Qodo automatically discovers repository relationships by analyzing technical signals across connected repositories.
In the payment system, those signals include:
The SDK generator referencing the payment service’s OpenAPI schema
The checkout application declaring the SDK as a dependency
Source code importing the generated SDK package
CI workflows checking out another repository
Build scripts copying or generating artifacts
Service URLs stored in configuration
Client methods matching server routes
Shared request and response types
Deployment workflows coordinating service and client versions
Relationships need technical context
Knowing that two repositories are related is only the first step. The relationship also needs enough detail to identify how they interact.
For the payment system, Qodo discovered the following relationship:
Producer repository:
payment-service
Consumer repository:
payment-sdk
Relationship type: Code
Relevant surfaces:
api/openapi.yaml
generator-config.yaml
generated/api/PaymentsApi.ts
generated/models/Payment.ts
It also discovered a second relationship:
Producer repository:
payment-sdk
Consumer repository:
checkout-web
Relationship type: Package dependency and API usage
Relevant surfaces:
package.json
generated/api/PaymentsApi.ts
This context helps Qodo retrieve the right parts of each repository for a given change.
Catching contract failures during review
Cross-repository failures are often detected late because validation is divided across teams and pipelines. The payment service team knows what changed in the API. The SDK pipeline knows how the client is generated. The checkout team knows how the client is used. Each repository may run its own tests, while full integration validation happens only during release or deployment.
Bringing repository relationships into the PR review moves part of that validation closer to the change.
This does not replace integration tests, consumer-driven contract tests, or staged deployments. It adds a layer of verification while the proposed change and its intent are still visible to the author and reviewers.
During a pull request review, Qodo will:
Identify a change to a contract surface.
Determine which repositories are connected to that surface.
Retrieve the relevant producer and consumer implementations.
Compare the changed behavior with its actual usage.
Produce an actionable review finding
In the payment example, Qodo connects the changed request model in
payment-service
to the method in
payment-sdk
and its usage in checkout-web.
The finding is based on a concrete relationship and a specific usage. It identifies which contract changed, where the old contract is still consumed, and what must be coordinated before the change is safe to release. This gives the author enough context to evaluate the issue without manually tracing the dependency through several repositories.
Reviewing the connected system
A pull request may change only a few lines in payment-service, but those lines can alter assumptions shared by
payment-sdk
,
checkout-web
, and the workflows that connect them.
Qodo’s cross-repository relationships provide the context needed to follow those assumptions across repository boundaries. Automatic discovery identifies how repositories are connected. Relationship-aware retrieval locates the relevant contract surfaces. Contract verification compares the proposed change with the code, artifacts, and workflows that depend on it.
The result is a review process that evaluates whether the contract still holds across the connected system before the change is merged.

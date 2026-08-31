# Source: https://kiro.dev/blog/kiro-and-snyk-guardrails/

**URL:** https://kiro.dev/blog/kiro-and-snyk-guardrails/
**Fetched:** 2026-08-31

---

<div class="relative z-20 bg-black-900" role="main">

<div class="mx-auto w-full max-w-none px-4 sm:px-8 md:px-16 md:pt-6 xl-custom:max-w-[1480px]">

<div class="grid grid-cols-12 gap-4">

<div class="col-span-12 mx-auto w-full min-w-0 lg:col-span-12" role="region" aria-label="Page content">

<div class="grid grid-cols-12 gap-4 pb-20 pt-[7.5rem]">

<div class="col-span-12 mb-8 lg:col-span-2 lg:mb-0 xl:col-span-3">

<a href="/blog/" class="sticky top-24 inline-flex gap-2 text-sm text-secondary transition-colors hover:text-foreground"><img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgdmlld2JveD0iMCAwIDI0IDI0IiBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLXdpZHRoPSIyIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGNsYXNzPSJsdWNpZGUgbHVjaWRlLWFycm93LWxlZnQgbXQtWzFweF0gaC00IHctNCIgYXJpYS1oaWRkZW49InRydWUiPjxwYXRoIGQ9Im0xMiAxOS03LTcgNy03IiAvPjxwYXRoIGQ9Ik0xOSAxMkg1IiAvPjwvc3ZnPg==" class="lucide lucide-arrow-left mt-[1px] h-4 w-4" /><span>Back to all posts</span></a>

</div>

<div class="header mb-12">

<div class="mb-6 flex items-center gap-4 text-sm text-secondary">

July 20, 2026

</div>

# How Kiro and Snyk create multi-layered security guardrails

<div class="flex items-center gap-2">

<span class="text-sm text-muted-foreground">By</span>

<div class="flex flex-wrap items-center gap-4">

<div class="flex items-center gap-2">

<span class="relative flex shrink-0 overflow-hidden rounded-full h-8 w-8"><span class="flex h-full w-full items-center justify-center rounded-full bg-muted">GO</span></span>

<div>

Gourav Bhardwaj

Developer

</div>

</div>

<a href="https://www.linkedin.com/in/schottdb/" class="flex cursor-pointer items-center gap-2 transition-opacity hover:opacity-80"><span class="relative flex shrink-0 overflow-hidden rounded-full h-8 w-8"><span class="flex h-full w-full items-center justify-center rounded-full bg-muted">DA</span></span></a>

<div>

David B. Schott

Snyk

</div>

<a href="https://www.linkedin.com/in/ryanj16/" class="flex cursor-pointer items-center gap-2 transition-opacity hover:opacity-80"><span class="relative flex shrink-0 overflow-hidden rounded-full h-8 w-8"><span class="flex h-full w-full items-center justify-center rounded-full bg-muted">JA</span></span></a>

<div>

Jack Ryan

Snyk

</div>

</div>

</div>

</div>

<div class="blog-content changelog prose-prey prose max-w-none dark:prose-invert prose-code:before:content-none prose-code:after:content-none">

The rapid adoption of AI-powered development tools like <a href="/" class="text-primary hover:underline">Kiro</a> is transforming how we build software, enabling unprecedented speed and innovation. However, this advancement also introduces new information security challenges. To truly leverage the power of AI in development, a robust, multi-layered security strategy is not just recommended – it’s essential. This blog post explores how integrating <a href="https://docs.snyk.io/integrations/developer-guardrails-for-agentic-workflows" class="text-primary hover:underline" target="_blank" rel="noopener noreferrer">Snyk</a> Studio with Kiro provides a critical additional layer of automated security and compliance, ensuring that rapid development doesn't compromise the integrity of your applications. Snyk Studio is a recently launchedoffering from Snyk that combines the Snyk MCP Server with guardrails to scan code as it’s written and provide fixes.

<a href="https://modelcontextprotocol.io/docs/getting-started/intro" class="text-primary hover:underline" target="_blank" rel="noopener noreferrer">Model Context Protocol (MCP)</a> is an open protocol that standardizes connecting AI assistants to the external world, including content repositories, data sources, business tools, and development environments. At its core, MCP follows a client-server architecture where a host application can connect to multiple servers. An MCP architecture has the following components:

- <a href="https://modelcontextprotocol.io/docs/learn/client-concepts" class="text-primary hover:underline" target="_blank" rel="noopener noreferrer"><strong>MCP hosts and clients</strong></a> – AI-powered applications such as Kiro that need access to external data or tools.
- <a href="https://modelcontextprotocol.io/docs/learn/server-concepts" class="text-primary hover:underline" target="_blank" rel="noopener noreferrer"><strong>MCP servers</strong></a> – Lightweight servers such as the Snyk MCP Server that exposes specific functionalities through tools, connecting to local or remote data sources.
- <a href="https://modelcontextprotocol.io/docs/learn/architecture#data-layer" class="text-primary hover:underline" target="_blank" rel="noopener noreferrer"><strong>Data sources</strong></a> – Databases, files, or services that contain the information your AI assistants need.

<div class="heading-anchor-wrapper">

## The information security challenges of AI-powered development

<a href="#the-information-security-challenges-of-ai-powered-development" class="anchor-link" aria-label="Copy link to The information security challenges of ai powered development section"><span class="anchor-icon-wrapper"><img src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iYW5jaG9yLWljb24iIHZpZXdib3g9IjAgMCAxNiAxNyIgd2lkdGg9IjE2IiBoZWlnaHQ9IjE3IiBmaWxsPSJjdXJyZW50Q29sb3IiPjxwYXRoIGQ9Ik0yLjI3MTQzIDE0LjIyOEMwLjU5MTg5NyAxMi41NDg1IDAuNTkxODk3IDkuODI1MzkgMi4yNzE0MyA4LjE0NTg1TDMuNDIzMjQgNi45OTQwNEwzLjQ0MTg4IDYuOTc2MzVDMy42MzgxNiA2Ljc5OSAzLjk0MTE4IDYuODA0ODggNC4xMzAzNSA2Ljk5NDA0QzQuMzE5NTEgNy4xODMyMSA0LjMyNTM5IDcuNDg2MjMgNC4xNDgwNCA3LjY4MjVMNC4xMzAzNSA3LjcwMTE1TDIuOTc4NTQgOC44NTI5NkMxLjY4OTUzIDEwLjE0MiAxLjY4OTUzIDEyLjIzMTkgMi45Nzg1NCAxMy41MjA5TDMuMDA4ODggMTMuNTUwOUM0LjMwMDE0IDE0LjgwOTggNi4zNjc1MSAxNC43OTk4IDcuNjQ2NDYgMTMuNTIwOUw4Ljc5ODI3IDEyLjM2OTFMOC44MTY5MSAxMi4zNTE0QzkuMDEzMTkgMTIuMTc0IDkuMzE2MjEgMTIuMTc5OSA5LjUwNTM4IDEyLjM2OTFDOS42OTQ1NCAxMi41NTgyIDkuNzAwNDYgMTIuODYxMyA5LjUyMzExIDEzLjA1NzZMOS41MDUzOCAxMy4wNzYyTDguMzUzNTYgMTQuMjI4QzYuNjg3MTUgMTUuODk0NCAzLjk5MzQ3IDE1LjkwNzQgMi4zMTEgMTQuMjY3TDIuMjcxNDMgMTQuMjI4Wk0xMy4wMjE1IDMuNDc3OTNDMTEuNzQyNSAyLjE5ODk5IDkuNjc1MTcgMi4xODg5NiA4LjM4MzkgMy40NDc5NEw4LjM1MzU2IDMuNDc3OTNMNy4yMjU3OSA0LjYwNTdDNy4wMzA1MyA0LjgwMDk2IDYuNzEzOTUgNC44MDA5NiA2LjUxODY5IDQuNjA1N0M2LjMyMzQyIDQuNDEwNDQgNi4zMjM0MiA0LjA5Mzg2IDYuNTE4NjkgMy44OTg1OUw3LjY0NjQ2IDIuNzcwODJMNy42ODYwMyAyLjczMTc3QzkuMzY4NSAxLjA5MTM4IDEyLjA2MjIgMS4xMDQ0MSAxMy43Mjg2IDIuNzcwODJMMTMuNzY3NyAyLjgxMDM2QzE1LjM5NTIgNC40Nzk1OCAxNS4zOTUxIDcuMTQ0MTcgMTMuNzY3NyA4LjgxMzM4TDEzLjcyODYgOC44NTI5NkwxMi42MDA4IDkuOTgwNzNDMTIuNDA1NiAxMC4xNzYgMTIuMDg5IDEwLjE3NiAxMS44OTM3IDkuOTgwNzNDMTEuNjk4NSA5Ljc4NTQ3IDExLjY5ODUgOS40Njg4OCAxMS44OTM3IDkuMjczNjJMMTMuMDIxNSA4LjE0NTg1TDEzLjA1MTUgOC4xMTU1MUMxNC4zMDA1IDYuODM0NDIgMTQuMzAwNSA0Ljc4OTM3IDEzLjA1MTUgMy41MDgyN0wxMy4wMjE1IDMuNDc3OTNaIiAvPjxwYXRoIGQ9Ik0xMC4wMjE5IDUuODY2MzJMMTAuMDQwNiA1Ljg0ODU4QzEwLjIzNjkgNS42NzEyNCAxMC41Mzk5IDUuNjc3MTYgMTAuNzI5IDUuODY2MzJDMTAuOTE4MiA2LjA1NTQ4IDEwLjkyNDEgNi4zNTg0NiAxMC43NDY4IDYuNTU0NzRMMTAuNzI5IDYuNTczNDJMNi4xNDU4OCAxMS4xNTY2QzUuOTUwNjIgMTEuMzUxOCA1LjYzNDAzIDExLjM1MTggNS40Mzg3NyAxMS4xNTY2QzUuMjQzNTEgMTAuOTYxMyA1LjI0MzUxIDEwLjY0NDcgNS40Mzg3NyAxMC40NDk1TDEwLjAyMTkgNS44NjYzMloiIC8+PC9zdmc+" class="anchor-icon" /><span class="copied-indicator docsearch-exclude" aria-live="polite" aria-atomic="true"></span></span></a>

</div>

While AI tools accelerate code generation, they also present unique security considerations. The sheer volume and speed of AI-generated code can make traditional security reviews difficult to scale. Furthermore, AI-specific vulnerabilities, such as <a href="https://genai.owasp.org/llmrisk/llm01-prompt-injection" class="text-primary hover:underline" target="_blank" rel="noopener noreferrer">prompt injection</a>, require specialized detection and mitigation techniques. A "defense-in-depth" approach, where multiple security layers work in concert, is the best practice for professional software development, regardless of how the code is produced.

<div class="heading-anchor-wrapper">

## Enabling multi-layered security in AI workflows

<a href="#enabling-multi-layered-security-in-ai-workflows" class="anchor-link" aria-label="Copy link to Enabling multi layered security in ai workflows section"><span class="anchor-icon-wrapper"><img src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iYW5jaG9yLWljb24iIHZpZXdib3g9IjAgMCAxNiAxNyIgd2lkdGg9IjE2IiBoZWlnaHQ9IjE3IiBmaWxsPSJjdXJyZW50Q29sb3IiPjxwYXRoIGQ9Ik0yLjI3MTQzIDE0LjIyOEMwLjU5MTg5NyAxMi41NDg1IDAuNTkxODk3IDkuODI1MzkgMi4yNzE0MyA4LjE0NTg1TDMuNDIzMjQgNi45OTQwNEwzLjQ0MTg4IDYuOTc2MzVDMy42MzgxNiA2Ljc5OSAzLjk0MTE4IDYuODA0ODggNC4xMzAzNSA2Ljk5NDA0QzQuMzE5NTEgNy4xODMyMSA0LjMyNTM5IDcuNDg2MjMgNC4xNDgwNCA3LjY4MjVMNC4xMzAzNSA3LjcwMTE1TDIuOTc4NTQgOC44NTI5NkMxLjY4OTUzIDEwLjE0MiAxLjY4OTUzIDEyLjIzMTkgMi45Nzg1NCAxMy41MjA5TDMuMDA4ODggMTMuNTUwOUM0LjMwMDE0IDE0LjgwOTggNi4zNjc1MSAxNC43OTk4IDcuNjQ2NDYgMTMuNTIwOUw4Ljc5ODI3IDEyLjM2OTFMOC44MTY5MSAxMi4zNTE0QzkuMDEzMTkgMTIuMTc0IDkuMzE2MjEgMTIuMTc5OSA5LjUwNTM4IDEyLjM2OTFDOS42OTQ1NCAxMi41NTgyIDkuNzAwNDYgMTIuODYxMyA5LjUyMzExIDEzLjA1NzZMOS41MDUzOCAxMy4wNzYyTDguMzUzNTYgMTQuMjI4QzYuNjg3MTUgMTUuODk0NCAzLjk5MzQ3IDE1LjkwNzQgMi4zMTEgMTQuMjY3TDIuMjcxNDMgMTQuMjI4Wk0xMy4wMjE1IDMuNDc3OTNDMTEuNzQyNSAyLjE5ODk5IDkuNjc1MTcgMi4xODg5NiA4LjM4MzkgMy40NDc5NEw4LjM1MzU2IDMuNDc3OTNMNy4yMjU3OSA0LjYwNTdDNy4wMzA1MyA0LjgwMDk2IDYuNzEzOTUgNC44MDA5NiA2LjUxODY5IDQuNjA1N0M2LjMyMzQyIDQuNDEwNDQgNi4zMjM0MiA0LjA5Mzg2IDYuNTE4NjkgMy44OTg1OUw3LjY0NjQ2IDIuNzcwODJMNy42ODYwMyAyLjczMTc3QzkuMzY4NSAxLjA5MTM4IDEyLjA2MjIgMS4xMDQ0MSAxMy43Mjg2IDIuNzcwODJMMTMuNzY3NyAyLjgxMDM2QzE1LjM5NTIgNC40Nzk1OCAxNS4zOTUxIDcuMTQ0MTcgMTMuNzY3NyA4LjgxMzM4TDEzLjcyODYgOC44NTI5NkwxMi42MDA4IDkuOTgwNzNDMTIuNDA1NiAxMC4xNzYgMTIuMDg5IDEwLjE3NiAxMS44OTM3IDkuOTgwNzNDMTEuNjk4NSA5Ljc4NTQ3IDExLjY5ODUgOS40Njg4OCAxMS44OTM3IDkuMjczNjJMMTMuMDIxNSA4LjE0NTg1TDEzLjA1MTUgOC4xMTU1MUMxNC4zMDA1IDYuODM0NDIgMTQuMzAwNSA0Ljc4OTM3IDEzLjA1MTUgMy41MDgyN0wxMy4wMjE1IDMuNDc3OTNaIiAvPjxwYXRoIGQ9Ik0xMC4wMjE5IDUuODY2MzJMMTAuMDQwNiA1Ljg0ODU4QzEwLjIzNjkgNS42NzEyNCAxMC41Mzk5IDUuNjc3MTYgMTAuNzI5IDUuODY2MzJDMTAuOTE4MiA2LjA1NTQ4IDEwLjkyNDEgNi4zNTg0NiAxMC43NDY4IDYuNTU0NzRMMTAuNzI5IDYuNTczNDJMNi4xNDU4OCAxMS4xNTY2QzUuOTUwNjIgMTEuMzUxOCA1LjYzNDAzIDExLjM1MTggNS40Mzg3NyAxMS4xNTY2QzUuMjQzNTEgMTAuOTYxMyA1LjI0MzUxIDEwLjY0NDcgNS40Mzg3NyAxMC40NDk1TDEwLjAyMTkgNS44NjYzMloiIC8+PC9zdmc+" class="anchor-icon" /><span class="copied-indicator docsearch-exclude" aria-live="polite" aria-atomic="true"></span></span></a>

</div>

Integrating Snyk with Kiro via MCP creates a powerful defense-in-depth approach, aligning with industry best practices for secure, professional development. This layered strategy helps developers shiftsecurity left by supporting fast iteration in any IDE or coding environment.

<div class="heading-anchor-wrapper">

## Prerequisites

<a href="#prerequisites" class="anchor-link" aria-label="Copy link to Prerequisites section"><span class="anchor-icon-wrapper"><img src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iYW5jaG9yLWljb24iIHZpZXdib3g9IjAgMCAxNiAxNyIgd2lkdGg9IjE2IiBoZWlnaHQ9IjE3IiBmaWxsPSJjdXJyZW50Q29sb3IiPjxwYXRoIGQ9Ik0yLjI3MTQzIDE0LjIyOEMwLjU5MTg5NyAxMi41NDg1IDAuNTkxODk3IDkuODI1MzkgMi4yNzE0MyA4LjE0NTg1TDMuNDIzMjQgNi45OTQwNEwzLjQ0MTg4IDYuOTc2MzVDMy42MzgxNiA2Ljc5OSAzLjk0MTE4IDYuODA0ODggNC4xMzAzNSA2Ljk5NDA0QzQuMzE5NTEgNy4xODMyMSA0LjMyNTM5IDcuNDg2MjMgNC4xNDgwNCA3LjY4MjVMNC4xMzAzNSA3LjcwMTE1TDIuOTc4NTQgOC44NTI5NkMxLjY4OTUzIDEwLjE0MiAxLjY4OTUzIDEyLjIzMTkgMi45Nzg1NCAxMy41MjA5TDMuMDA4ODggMTMuNTUwOUM0LjMwMDE0IDE0LjgwOTggNi4zNjc1MSAxNC43OTk4IDcuNjQ2NDYgMTMuNTIwOUw4Ljc5ODI3IDEyLjM2OTFMOC44MTY5MSAxMi4zNTE0QzkuMDEzMTkgMTIuMTc0IDkuMzE2MjEgMTIuMTc5OSA5LjUwNTM4IDEyLjM2OTFDOS42OTQ1NCAxMi41NTgyIDkuNzAwNDYgMTIuODYxMyA5LjUyMzExIDEzLjA1NzZMOS41MDUzOCAxMy4wNzYyTDguMzUzNTYgMTQuMjI4QzYuNjg3MTUgMTUuODk0NCAzLjk5MzQ3IDE1LjkwNzQgMi4zMTEgMTQuMjY3TDIuMjcxNDMgMTQuMjI4Wk0xMy4wMjE1IDMuNDc3OTNDMTEuNzQyNSAyLjE5ODk5IDkuNjc1MTcgMi4xODg5NiA4LjM4MzkgMy40NDc5NEw4LjM1MzU2IDMuNDc3OTNMNy4yMjU3OSA0LjYwNTdDNy4wMzA1MyA0LjgwMDk2IDYuNzEzOTUgNC44MDA5NiA2LjUxODY5IDQuNjA1N0M2LjMyMzQyIDQuNDEwNDQgNi4zMjM0MiA0LjA5Mzg2IDYuNTE4NjkgMy44OTg1OUw3LjY0NjQ2IDIuNzcwODJMNy42ODYwMyAyLjczMTc3QzkuMzY4NSAxLjA5MTM4IDEyLjA2MjIgMS4xMDQ0MSAxMy43Mjg2IDIuNzcwODJMMTMuNzY3NyAyLjgxMDM2QzE1LjM5NTIgNC40Nzk1OCAxNS4zOTUxIDcuMTQ0MTcgMTMuNzY3NyA4LjgxMzM4TDEzLjcyODYgOC44NTI5NkwxMi42MDA4IDkuOTgwNzNDMTIuNDA1NiAxMC4xNzYgMTIuMDg5IDEwLjE3NiAxMS44OTM3IDkuOTgwNzNDMTEuNjk4NSA5Ljc4NTQ3IDExLjY5ODUgOS40Njg4OCAxMS44OTM3IDkuMjczNjJMMTMuMDIxNSA4LjE0NTg1TDEzLjA1MTUgOC4xMTU1MUMxNC4zMDA1IDYuODM0NDIgMTQuMzAwNSA0Ljc4OTM3IDEzLjA1MTUgMy41MDgyN0wxMy4wMjE1IDMuNDc3OTNaIiAvPjxwYXRoIGQ9Ik0xMC4wMjE5IDUuODY2MzJMMTAuMDQwNiA1Ljg0ODU4QzEwLjIzNjkgNS42NzEyNCAxMC41Mzk5IDUuNjc3MTYgMTAuNzI5IDUuODY2MzJDMTAuOTE4MiA2LjA1NTQ4IDEwLjkyNDEgNi4zNTg0NiAxMC43NDY4IDYuNTU0NzRMMTAuNzI5IDYuNTczNDJMNi4xNDU4OCAxMS4xNTY2QzUuOTUwNjIgMTEuMzUxOCA1LjYzNDAzIDExLjM1MTggNS40Mzg3NyAxMS4xNTY2QzUuMjQzNTEgMTAuOTYxMyA1LjI0MzUxIDEwLjY0NDcgNS40Mzg3NyAxMC40NDk1TDEwLjAyMTkgNS44NjYzMloiIC8+PC9zdmc+" class="anchor-icon" /><span class="copied-indicator docsearch-exclude" aria-live="polite" aria-atomic="true"></span></span></a>

</div>

1.  Install <a href="/downloads/" class="text-primary hover:underline">Kiro IDE</a>.
2.  Create your <a href="https://app.snyk.io/signup/" class="text-primary hover:underline" target="_blank" rel="noopener noreferrer">Snyk account</a>.
3.  In your Snyk account, <a href="https://docs.snyk.io/implementation-and-setup/enterprise-implementation-guide/phase-2-configure-account/set-visibility-and-configure-an-organization-template/enable-snyk-code" class="text-primary hover:underline" target="_blank" rel="noopener noreferrer">enable Snyk Code</a> for code scan.
4.  <a href="https://docs.snyk.io/developer-tools/snyk-cli/install-or-update-the-snyk-cli" class="text-primary hover:underline" target="_blank" rel="noopener noreferrer">Install the Snyk CLI</a>.
5.  <a href="https://docs.snyk.io/integrations/developer-guardrails-for-agentic-workflows/quickstart-guides-for-mcp/kiro-guide#install-the-snyk-mcp-server-in-qodo" class="text-primary hover:underline" target="_blank" rel="noopener noreferrer">Configure the Snyk MCP server in Kiro</a>.

<div class="heading-anchor-wrapper">

## 1. Repository and project scanning: automated security assessment

<a href="#1-repository-and-project-scanning-automated-security-assessment" class="anchor-link" aria-label="Copy link to 1 repository and project scanning automated security assessment section"><span class="anchor-icon-wrapper"><img src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iYW5jaG9yLWljb24iIHZpZXdib3g9IjAgMCAxNiAxNyIgd2lkdGg9IjE2IiBoZWlnaHQ9IjE3IiBmaWxsPSJjdXJyZW50Q29sb3IiPjxwYXRoIGQ9Ik0yLjI3MTQzIDE0LjIyOEMwLjU5MTg5NyAxMi41NDg1IDAuNTkxODk3IDkuODI1MzkgMi4yNzE0MyA4LjE0NTg1TDMuNDIzMjQgNi45OTQwNEwzLjQ0MTg4IDYuOTc2MzVDMy42MzgxNiA2Ljc5OSAzLjk0MTE4IDYuODA0ODggNC4xMzAzNSA2Ljk5NDA0QzQuMzE5NTEgNy4xODMyMSA0LjMyNTM5IDcuNDg2MjMgNC4xNDgwNCA3LjY4MjVMNC4xMzAzNSA3LjcwMTE1TDIuOTc4NTQgOC44NTI5NkMxLjY4OTUzIDEwLjE0MiAxLjY4OTUzIDEyLjIzMTkgMi45Nzg1NCAxMy41MjA5TDMuMDA4ODggMTMuNTUwOUM0LjMwMDE0IDE0LjgwOTggNi4zNjc1MSAxNC43OTk4IDcuNjQ2NDYgMTMuNTIwOUw4Ljc5ODI3IDEyLjM2OTFMOC44MTY5MSAxMi4zNTE0QzkuMDEzMTkgMTIuMTc0IDkuMzE2MjEgMTIuMTc5OSA5LjUwNTM4IDEyLjM2OTFDOS42OTQ1NCAxMi41NTgyIDkuNzAwNDYgMTIuODYxMyA5LjUyMzExIDEzLjA1NzZMOS41MDUzOCAxMy4wNzYyTDguMzUzNTYgMTQuMjI4QzYuNjg3MTUgMTUuODk0NCAzLjk5MzQ3IDE1LjkwNzQgMi4zMTEgMTQuMjY3TDIuMjcxNDMgMTQuMjI4Wk0xMy4wMjE1IDMuNDc3OTNDMTEuNzQyNSAyLjE5ODk5IDkuNjc1MTcgMi4xODg5NiA4LjM4MzkgMy40NDc5NEw4LjM1MzU2IDMuNDc3OTNMNy4yMjU3OSA0LjYwNTdDNy4wMzA1MyA0LjgwMDk2IDYuNzEzOTUgNC44MDA5NiA2LjUxODY5IDQuNjA1N0M2LjMyMzQyIDQuNDEwNDQgNi4zMjM0MiA0LjA5Mzg2IDYuNTE4NjkgMy44OTg1OUw3LjY0NjQ2IDIuNzcwODJMNy42ODYwMyAyLjczMTc3QzkuMzY4NSAxLjA5MTM4IDEyLjA2MjIgMS4xMDQ0MSAxMy43Mjg2IDIuNzcwODJMMTMuNzY3NyAyLjgxMDM2QzE1LjM5NTIgNC40Nzk1OCAxNS4zOTUxIDcuMTQ0MTcgMTMuNzY3NyA4LjgxMzM4TDEzLjcyODYgOC44NTI5NkwxMi42MDA4IDkuOTgwNzNDMTIuNDA1NiAxMC4xNzYgMTIuMDg5IDEwLjE3NiAxMS44OTM3IDkuOTgwNzNDMTEuNjk4NSA5Ljc4NTQ3IDExLjY5ODUgOS40Njg4OCAxMS44OTM3IDkuMjczNjJMMTMuMDIxNSA4LjE0NTg1TDEzLjA1MTUgOC4xMTU1MUMxNC4zMDA1IDYuODM0NDIgMTQuMzAwNSA0Ljc4OTM3IDEzLjA1MTUgMy41MDgyN0wxMy4wMjE1IDMuNDc3OTNaIiAvPjxwYXRoIGQ9Ik0xMC4wMjE5IDUuODY2MzJMMTAuMDQwNiA1Ljg0ODU4QzEwLjIzNjkgNS42NzEyNCAxMC41Mzk5IDUuNjc3MTYgMTAuNzI5IDUuODY2MzJDMTAuOTE4MiA2LjA1NTQ4IDEwLjkyNDEgNi4zNTg0NiAxMC43NDY4IDYuNTU0NzRMMTAuNzI5IDYuNTczNDJMNi4xNDU4OCAxMS4xNTY2QzUuOTUwNjIgMTEuMzUxOCA1LjYzNDAzIDExLjM1MTggNS40Mzg3NyAxMS4xNTY2QzUuMjQzNTEgMTAuOTYxMyA1LjI0MzUxIDEwLjY0NDcgNS40Mzg3NyAxMC40NDk1TDEwLjAyMTkgNS44NjYzMloiIC8+PC9zdmc+" class="anchor-icon" /><span class="copied-indicator docsearch-exclude" aria-live="polite" aria-atomic="true"></span></span></a>

</div>

The integration of Snyk with Kiro via MCP goes beyond traditional IDE extensions by allowing developers to run security scans using natural language. This functionality not only identifies potential vulnerabilities and misconfigurations, but also informs the underlying AI model of key information, such as what the vulnerabilities are, what file they’re in, what line number they’re on, and remediation details.

This context provides immediate, actionable insights early in the development lifecycle.

You can test the Snyk MCP server by opening a project, or if you want to use a sample application for you to test the Snyk scanning capabilities in Kiro, you can use this <a href="https://github.com/snyk-labs/nodejs-goof" class="text-primary hover:underline" target="_blank" rel="noopener noreferrer">nodejs-goof application provided by Snyk</a>.

Then type on the Kiro chat, “*Scan this directory for code security and dependency vulnerabilities using Snyk*”. As a one-time setup, you may need to authenticate to Snyk and trust the current project directory.

<div>

<div class="my-8">

<figure class="overflow-hidden rounded-2xl border border-[#4a464f] bg-muted/30">
<span class="group relative inline-block transition-all duration-200 cursor-zoom-in" style="display:block" tabindex="0" role="button" aria-label="Open image lightbox: Kiro main window with code editor and Kiro chat agent with prompt to Scan the directory"><span class="relative overflow-hidden h-auto w-full border-0"><span class="absolute inset-0 flex animate-pulse items-center justify-center bg-muted"><span class="sr-only">Loading image...</span></span><img src="/images/blogs/kiro-and-snyk-guardrails/1.png?h=40834ae6" class="transition-opacity duration-300 opacity-0" style="color:transparent" loading="lazy" decoding="async" data-nimg="1" width="1200" height="600" alt="Kiro main window with code editor and Kiro chat agent with prompt to Scan the directory" /></span><span class="absolute bottom-2 right-2 z-10 flex items-center justify-center rounded-full bg-prey-600/60 p-2.5 transition-opacity duration-200 opacity-100 group-hover:opacity-100" aria-hidden="true"><img src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdib3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48cGF0aCBkPSJNMTUuNjIyIDAuMDA5MTU3NTFDMTUuNzEyMyAwLjAyNzEzMzUgMTUuNzk1OSAwLjA3MTM0IDE1Ljg2MiAwLjEzNzM2M0MxNS45NSAwLjIyNTQzNiAxNS45OTk1IDAuMzQ1MjI2IDE1Ljk5OTMgMC40Njk3OEwxNS45OTI5IDUuNDIzMDhMMTUuOTgzNyA1LjUxNzRDMTUuOTM5OSA1LjczMTA2IDE1Ljc1MDYgNS44OTIwNCAxNS41MjQgNS44OTE5NEMxNS4yNjUxIDUuODkxNjIgMTUuMDU0OSA1LjY4MTA2IDE1LjA1NTIgNS40MjIxNkwxNS4wNTk3IDEuNjAxNjVMMTAuMTc2OSA2LjQ4NTM1QzkuOTkzODQgNi42Njg0NSA5LjY5NzA0IDYuNjY4NDUgOS41MTM5NCA2LjQ4NTM1QzkuMzMwODMgNi4zMDIyNCA5LjMzMDgzIDYuMDA1NDUgOS41MTM5NCA1LjgyMjM0TDE0LjM5NjcgMC45Mzg2NDVMMTAuNTc3MSAwLjk0NDEzOUwxMC40ODI4IDAuOTM0OTgyQzEwLjI2OSAwLjg5MTU4NCAxMC4xMDc2IDAuNzAxOTAzIDEwLjEwNzMgMC40NzUyNzVDMTAuMTA3MiAwLjIxNjUwNyAxMC4zMTc0IDAuMDA2NzM0ODQgMTAuNTc2MiAwLjAwNjQxMDI2TDE1LjUyOTUgMEwxNS42MjIgMC4wMDkxNTc1MVoiIGZpbGw9ImN1cnJlbnRDb2xvciIgLz48cGF0aCBkPSJNMC4zNzcyOSAxNS45OTA4QzAuMjg3MDU3IDE1Ljk3MjkgMC4yMDMzODUgMTUuOTI4NyAwLjEzNzM2MiAxNS44NjI2QzAuMDQ5Mjg4OCAxNS43NzQ2IC0wLjAwMDE1NzAyNCAxNS42NTQ4IC04LjE4MjM1ZS0wNyAxNS41MzAyTDAuMDA2NDA5NDcgMTAuNTc2OUwwLjAxNTU2NyAxMC40ODI2QzAuMDU5Mzg5MSAxMC4yNjg5IDAuMjQ4NzQxIDEwLjEwOCAwLjQ3NTI3NiAxMC4xMDgxQzAuNzM0MTkxIDEwLjEwODQgMC45NDQ0MTUgMTAuMzE4OSAwLjk0NDE0MyAxMC41Nzc4TDAuOTM5NTY0IDE0LjM5ODRMNS44MjIzNyA5LjUxNDY1QzYuMDA1NDcgOS4zMzE1NSA2LjMwMjI3IDkuMzMxNTUgNi40ODUzOCA5LjUxNDY1QzYuNjY4NDggOS42OTc3NiA2LjY2ODQ4IDkuOTk0NTUgNi40ODUzOCAxMC4xNzc3TDEuNjAyNTcgMTUuMDYxNEw1LjQyMjE4IDE1LjA1NTlMNS41MTY1MSAxNS4wNjVDNS43MzAyOSAxNS4xMDg0IDUuODkxNjggMTUuMjk4MSA1Ljg5MTk3IDE1LjUyNDdDNS44OTIwOCAxNS43ODM1IDUuNjgxOTIgMTUuOTkzMyA1LjQyMzEgMTUuOTkzNkwwLjQ2OTc4MSAxNkwwLjM3NzI5IDE1Ljk5MDhaIiBmaWxsPSJjdXJyZW50Q29sb3IiIC8+PC9zdmc+" /></span></span>
</figure>

</div>

</div>

After authenticating to your Snyk account, you should see the Kiro agent starting an MCP call to the Snyk MCP server to scan the code for security and dependency vulnerabilities.

<div>

<div class="my-8">

<figure class="overflow-hidden rounded-2xl border border-[#4a464f] bg-muted/30">
<span class="group relative inline-block transition-all duration-200 cursor-zoom-in" style="display:block" tabindex="0" role="button" aria-label="Open image lightbox: Kiro agent chat window communicating with Snyk through MCP"><span class="relative overflow-hidden h-auto w-full border-0"><span class="absolute inset-0 flex animate-pulse items-center justify-center bg-muted"><span class="sr-only">Loading image...</span></span><img src="/images/blogs/kiro-and-snyk-guardrails/2.png?h=2303a770" class="transition-opacity duration-300 opacity-0" style="color:transparent" loading="lazy" decoding="async" data-nimg="1" width="1200" height="600" alt="Kiro agent chat window communicating with Snyk through MCP" /></span><span class="absolute bottom-2 right-2 z-10 flex items-center justify-center rounded-full bg-prey-600/60 p-2.5 transition-opacity duration-200 opacity-100 group-hover:opacity-100" aria-hidden="true"><img src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdib3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48cGF0aCBkPSJNMTUuNjIyIDAuMDA5MTU3NTFDMTUuNzEyMyAwLjAyNzEzMzUgMTUuNzk1OSAwLjA3MTM0IDE1Ljg2MiAwLjEzNzM2M0MxNS45NSAwLjIyNTQzNiAxNS45OTk1IDAuMzQ1MjI2IDE1Ljk5OTMgMC40Njk3OEwxNS45OTI5IDUuNDIzMDhMMTUuOTgzNyA1LjUxNzRDMTUuOTM5OSA1LjczMTA2IDE1Ljc1MDYgNS44OTIwNCAxNS41MjQgNS44OTE5NEMxNS4yNjUxIDUuODkxNjIgMTUuMDU0OSA1LjY4MTA2IDE1LjA1NTIgNS40MjIxNkwxNS4wNTk3IDEuNjAxNjVMMTAuMTc2OSA2LjQ4NTM1QzkuOTkzODQgNi42Njg0NSA5LjY5NzA0IDYuNjY4NDUgOS41MTM5NCA2LjQ4NTM1QzkuMzMwODMgNi4zMDIyNCA5LjMzMDgzIDYuMDA1NDUgOS41MTM5NCA1LjgyMjM0TDE0LjM5NjcgMC45Mzg2NDVMMTAuNTc3MSAwLjk0NDEzOUwxMC40ODI4IDAuOTM0OTgyQzEwLjI2OSAwLjg5MTU4NCAxMC4xMDc2IDAuNzAxOTAzIDEwLjEwNzMgMC40NzUyNzVDMTAuMTA3MiAwLjIxNjUwNyAxMC4zMTc0IDAuMDA2NzM0ODQgMTAuNTc2MiAwLjAwNjQxMDI2TDE1LjUyOTUgMEwxNS42MjIgMC4wMDkxNTc1MVoiIGZpbGw9ImN1cnJlbnRDb2xvciIgLz48cGF0aCBkPSJNMC4zNzcyOSAxNS45OTA4QzAuMjg3MDU3IDE1Ljk3MjkgMC4yMDMzODUgMTUuOTI4NyAwLjEzNzM2MiAxNS44NjI2QzAuMDQ5Mjg4OCAxNS43NzQ2IC0wLjAwMDE1NzAyNCAxNS42NTQ4IC04LjE4MjM1ZS0wNyAxNS41MzAyTDAuMDA2NDA5NDcgMTAuNTc2OUwwLjAxNTU2NyAxMC40ODI2QzAuMDU5Mzg5MSAxMC4yNjg5IDAuMjQ4NzQxIDEwLjEwOCAwLjQ3NTI3NiAxMC4xMDgxQzAuNzM0MTkxIDEwLjEwODQgMC45NDQ0MTUgMTAuMzE4OSAwLjk0NDE0MyAxMC41Nzc4TDAuOTM5NTY0IDE0LjM5ODRMNS44MjIzNyA5LjUxNDY1QzYuMDA1NDcgOS4zMzE1NSA2LjMwMjI3IDkuMzMxNTUgNi40ODUzOCA5LjUxNDY1QzYuNjY4NDggOS42OTc3NiA2LjY2ODQ4IDkuOTk0NTUgNi40ODUzOCAxMC4xNzc3TDEuNjAyNTcgMTUuMDYxNEw1LjQyMjE4IDE1LjA1NTlMNS41MTY1MSAxNS4wNjVDNS43MzAyOSAxNS4xMDg0IDUuODkxNjggMTUuMjk4MSA1Ljg5MTk3IDE1LjUyNDdDNS44OTIwOCAxNS43ODM1IDUuNjgxOTIgMTUuOTkzMyA1LjQyMzEgMTUuOTkzNkwwLjQ2OTc4MSAxNkwwLjM3NzI5IDE1Ljk5MDhaIiBmaWxsPSJjdXJyZW50Q29sb3IiIC8+PC9zdmc+" /></span></span>
</figure>

</div>

</div>

After Kiro completes all the client calls to Snyk MCP server, you should have a summary of all security vulnerabilities the Snyk scanners have found and a summary with each risk level and suggestions on fixes. Like in this sample, we can see there are 3 high severity security vulnerabilities that were found related to NoSQL injection and hardcoded secrets, and we can even ask Kiro to help us remediate them based on the context provided by the Snyk scanners.

<div>

<div class="my-8">

<figure class="overflow-hidden rounded-2xl border border-[#4a464f] bg-muted/30">
<span class="group relative inline-block transition-all duration-200 cursor-zoom-in" style="display:block" tabindex="0" role="button" aria-label="Open image lightbox: Kiro agent chat window showing output of scanning run by Snyk and remediation suggestions"><span class="relative overflow-hidden h-auto w-full border-0"><span class="absolute inset-0 flex animate-pulse items-center justify-center bg-muted"><span class="sr-only">Loading image...</span></span><img src="/images/blogs/kiro-and-snyk-guardrails/3.png?h=66ad347b" class="transition-opacity duration-300 opacity-0" style="color:transparent" loading="lazy" decoding="async" data-nimg="1" width="1200" height="600" alt="Kiro agent chat window showing output of scanning run by Snyk and remediation suggestions" /></span><span class="absolute bottom-2 right-2 z-10 flex items-center justify-center rounded-full bg-prey-600/60 p-2.5 transition-opacity duration-200 opacity-100 group-hover:opacity-100" aria-hidden="true"><img src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdib3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48cGF0aCBkPSJNMTUuNjIyIDAuMDA5MTU3NTFDMTUuNzEyMyAwLjAyNzEzMzUgMTUuNzk1OSAwLjA3MTM0IDE1Ljg2MiAwLjEzNzM2M0MxNS45NSAwLjIyNTQzNiAxNS45OTk1IDAuMzQ1MjI2IDE1Ljk5OTMgMC40Njk3OEwxNS45OTI5IDUuNDIzMDhMMTUuOTgzNyA1LjUxNzRDMTUuOTM5OSA1LjczMTA2IDE1Ljc1MDYgNS44OTIwNCAxNS41MjQgNS44OTE5NEMxNS4yNjUxIDUuODkxNjIgMTUuMDU0OSA1LjY4MTA2IDE1LjA1NTIgNS40MjIxNkwxNS4wNTk3IDEuNjAxNjVMMTAuMTc2OSA2LjQ4NTM1QzkuOTkzODQgNi42Njg0NSA5LjY5NzA0IDYuNjY4NDUgOS41MTM5NCA2LjQ4NTM1QzkuMzMwODMgNi4zMDIyNCA5LjMzMDgzIDYuMDA1NDUgOS41MTM5NCA1LjgyMjM0TDE0LjM5NjcgMC45Mzg2NDVMMTAuNTc3MSAwLjk0NDEzOUwxMC40ODI4IDAuOTM0OTgyQzEwLjI2OSAwLjg5MTU4NCAxMC4xMDc2IDAuNzAxOTAzIDEwLjEwNzMgMC40NzUyNzVDMTAuMTA3MiAwLjIxNjUwNyAxMC4zMTc0IDAuMDA2NzM0ODQgMTAuNTc2MiAwLjAwNjQxMDI2TDE1LjUyOTUgMEwxNS42MjIgMC4wMDkxNTc1MVoiIGZpbGw9ImN1cnJlbnRDb2xvciIgLz48cGF0aCBkPSJNMC4zNzcyOSAxNS45OTA4QzAuMjg3MDU3IDE1Ljk3MjkgMC4yMDMzODUgMTUuOTI4NyAwLjEzNzM2MiAxNS44NjI2QzAuMDQ5Mjg4OCAxNS43NzQ2IC0wLjAwMDE1NzAyNCAxNS42NTQ4IC04LjE4MjM1ZS0wNyAxNS41MzAyTDAuMDA2NDA5NDcgMTAuNTc2OUwwLjAxNTU2NyAxMC40ODI2QzAuMDU5Mzg5MSAxMC4yNjg5IDAuMjQ4NzQxIDEwLjEwOCAwLjQ3NTI3NiAxMC4xMDgxQzAuNzM0MTkxIDEwLjEwODQgMC45NDQ0MTUgMTAuMzE4OSAwLjk0NDE0MyAxMC41Nzc4TDAuOTM5NTY0IDE0LjM5ODRMNS44MjIzNyA5LjUxNDY1QzYuMDA1NDcgOS4zMzE1NSA2LjMwMjI3IDkuMzMxNTUgNi40ODUzOCA5LjUxNDY1QzYuNjY4NDggOS42OTc3NiA2LjY2ODQ4IDkuOTk0NTUgNi40ODUzOCAxMC4xNzc3TDEuNjAyNTcgMTUuMDYxNEw1LjQyMjE4IDE1LjA1NTlMNS41MTY1MSAxNS4wNjVDNS43MzAyOSAxNS4xMDg0IDUuODkxNjggMTUuMjk4MSA1Ljg5MTk3IDE1LjUyNDdDNS44OTIwOCAxNS43ODM1IDUuNjgxOTIgMTUuOTkzMyA1LjQyMzEgMTUuOTkzNkwwLjQ2OTc4MSAxNkwwLjM3NzI5IDE1Ljk5MDhaIiBmaWxsPSJjdXJyZW50Q29sb3IiIC8+PC9zdmc+" /></span></span>
</figure>

</div>

</div>

<div class="heading-anchor-wrapper">

## 2. Visibility and governance at the supply chain layer: AIBOM

<a href="#2-visibility-and-governance-at-the-supply-chain-layer-aibom" class="anchor-link" aria-label="Copy link to 2 visibility and governance at the supply chain layer aibom section"><span class="anchor-icon-wrapper"><img src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iYW5jaG9yLWljb24iIHZpZXdib3g9IjAgMCAxNiAxNyIgd2lkdGg9IjE2IiBoZWlnaHQ9IjE3IiBmaWxsPSJjdXJyZW50Q29sb3IiPjxwYXRoIGQ9Ik0yLjI3MTQzIDE0LjIyOEMwLjU5MTg5NyAxMi41NDg1IDAuNTkxODk3IDkuODI1MzkgMi4yNzE0MyA4LjE0NTg1TDMuNDIzMjQgNi45OTQwNEwzLjQ0MTg4IDYuOTc2MzVDMy42MzgxNiA2Ljc5OSAzLjk0MTE4IDYuODA0ODggNC4xMzAzNSA2Ljk5NDA0QzQuMzE5NTEgNy4xODMyMSA0LjMyNTM5IDcuNDg2MjMgNC4xNDgwNCA3LjY4MjVMNC4xMzAzNSA3LjcwMTE1TDIuOTc4NTQgOC44NTI5NkMxLjY4OTUzIDEwLjE0MiAxLjY4OTUzIDEyLjIzMTkgMi45Nzg1NCAxMy41MjA5TDMuMDA4ODggMTMuNTUwOUM0LjMwMDE0IDE0LjgwOTggNi4zNjc1MSAxNC43OTk4IDcuNjQ2NDYgMTMuNTIwOUw4Ljc5ODI3IDEyLjM2OTFMOC44MTY5MSAxMi4zNTE0QzkuMDEzMTkgMTIuMTc0IDkuMzE2MjEgMTIuMTc5OSA5LjUwNTM4IDEyLjM2OTFDOS42OTQ1NCAxMi41NTgyIDkuNzAwNDYgMTIuODYxMyA5LjUyMzExIDEzLjA1NzZMOS41MDUzOCAxMy4wNzYyTDguMzUzNTYgMTQuMjI4QzYuNjg3MTUgMTUuODk0NCAzLjk5MzQ3IDE1LjkwNzQgMi4zMTEgMTQuMjY3TDIuMjcxNDMgMTQuMjI4Wk0xMy4wMjE1IDMuNDc3OTNDMTEuNzQyNSAyLjE5ODk5IDkuNjc1MTcgMi4xODg5NiA4LjM4MzkgMy40NDc5NEw4LjM1MzU2IDMuNDc3OTNMNy4yMjU3OSA0LjYwNTdDNy4wMzA1MyA0LjgwMDk2IDYuNzEzOTUgNC44MDA5NiA2LjUxODY5IDQuNjA1N0M2LjMyMzQyIDQuNDEwNDQgNi4zMjM0MiA0LjA5Mzg2IDYuNTE4NjkgMy44OTg1OUw3LjY0NjQ2IDIuNzcwODJMNy42ODYwMyAyLjczMTc3QzkuMzY4NSAxLjA5MTM4IDEyLjA2MjIgMS4xMDQ0MSAxMy43Mjg2IDIuNzcwODJMMTMuNzY3NyAyLjgxMDM2QzE1LjM5NTIgNC40Nzk1OCAxNS4zOTUxIDcuMTQ0MTcgMTMuNzY3NyA4LjgxMzM4TDEzLjcyODYgOC44NTI5NkwxMi42MDA4IDkuOTgwNzNDMTIuNDA1NiAxMC4xNzYgMTIuMDg5IDEwLjE3NiAxMS44OTM3IDkuOTgwNzNDMTEuNjk4NSA5Ljc4NTQ3IDExLjY5ODUgOS40Njg4OCAxMS44OTM3IDkuMjczNjJMMTMuMDIxNSA4LjE0NTg1TDEzLjA1MTUgOC4xMTU1MUMxNC4zMDA1IDYuODM0NDIgMTQuMzAwNSA0Ljc4OTM3IDEzLjA1MTUgMy41MDgyN0wxMy4wMjE1IDMuNDc3OTNaIiAvPjxwYXRoIGQ9Ik0xMC4wMjE5IDUuODY2MzJMMTAuMDQwNiA1Ljg0ODU4QzEwLjIzNjkgNS42NzEyNCAxMC41Mzk5IDUuNjc3MTYgMTAuNzI5IDUuODY2MzJDMTAuOTE4MiA2LjA1NTQ4IDEwLjkyNDEgNi4zNTg0NiAxMC43NDY4IDYuNTU0NzRMMTAuNzI5IDYuNTczNDJMNi4xNDU4OCAxMS4xNTY2QzUuOTUwNjIgMTEuMzUxOCA1LjYzNDAzIDExLjM1MTggNS40Mzg3NyAxMS4xNTY2QzUuMjQzNTEgMTAuOTYxMyA1LjI0MzUxIDEwLjY0NDcgNS40Mzg3NyAxMC40NDk1TDEwLjAyMTkgNS44NjYzMloiIC8+PC9zdmc+" class="anchor-icon" /><span class="copied-indicator docsearch-exclude" aria-live="polite" aria-atomic="true"></span></span></a>

</div>

Establishing an <a href="https://snyk.io/articles/ai-security/ai-bill-of-materials-aibom/" class="text-primary hover:underline" target="_blank" rel="noopener noreferrer">AI Bill of Materials (AI-BOM)</a> is crucial for gaining visibility and governance over the AI components used in your projects. Just as a Software Bill of Materials (SBOM) tracks traditional software dependencies, an AIBOM provides a comprehensive inventory of the AI models, data sets, and other AI-specific elements integrated into your applications. This allows you to track their provenance, identify potential vulnerabilities, and verifies compliance with internal policies and external regulations. In the Kiro terminal, you can run the command `snyk aibom --html > ~<DESTINATION-HTLM-REPORT-PATH> && open ~<DESTINATION-HTML-REPORT-PATH>`

<div>

<div class="my-8">

<figure class="overflow-hidden rounded-2xl border border-[#4a464f] bg-muted/30">
<span class="group relative inline-block transition-all duration-200 cursor-zoom-in" style="display:block" tabindex="0" role="button" aria-label="Open image lightbox: Example of the Snyk AI-BOM diagram output with AI components used in the application"><span class="relative overflow-hidden h-auto w-full border-0"><span class="absolute inset-0 flex animate-pulse items-center justify-center bg-muted"><span class="sr-only">Loading image...</span></span><img src="/images/blogs/kiro-and-snyk-guardrails/5.png?h=58d47bb1" class="transition-opacity duration-300 opacity-0" style="color:transparent" loading="lazy" decoding="async" data-nimg="1" width="1200" height="600" alt="Example of the Snyk AI-BOM diagram output with AI components used in the application" /></span><span class="absolute bottom-2 right-2 z-10 flex items-center justify-center rounded-full bg-prey-600/60 p-2.5 transition-opacity duration-200 opacity-100 group-hover:opacity-100" aria-hidden="true"><img src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdib3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48cGF0aCBkPSJNMTUuNjIyIDAuMDA5MTU3NTFDMTUuNzEyMyAwLjAyNzEzMzUgMTUuNzk1OSAwLjA3MTM0IDE1Ljg2MiAwLjEzNzM2M0MxNS45NSAwLjIyNTQzNiAxNS45OTk1IDAuMzQ1MjI2IDE1Ljk5OTMgMC40Njk3OEwxNS45OTI5IDUuNDIzMDhMMTUuOTgzNyA1LjUxNzRDMTUuOTM5OSA1LjczMTA2IDE1Ljc1MDYgNS44OTIwNCAxNS41MjQgNS44OTE5NEMxNS4yNjUxIDUuODkxNjIgMTUuMDU0OSA1LjY4MTA2IDE1LjA1NTIgNS40MjIxNkwxNS4wNTk3IDEuNjAxNjVMMTAuMTc2OSA2LjQ4NTM1QzkuOTkzODQgNi42Njg0NSA5LjY5NzA0IDYuNjY4NDUgOS41MTM5NCA2LjQ4NTM1QzkuMzMwODMgNi4zMDIyNCA5LjMzMDgzIDYuMDA1NDUgOS41MTM5NCA1LjgyMjM0TDE0LjM5NjcgMC45Mzg2NDVMMTAuNTc3MSAwLjk0NDEzOUwxMC40ODI4IDAuOTM0OTgyQzEwLjI2OSAwLjg5MTU4NCAxMC4xMDc2IDAuNzAxOTAzIDEwLjEwNzMgMC40NzUyNzVDMTAuMTA3MiAwLjIxNjUwNyAxMC4zMTc0IDAuMDA2NzM0ODQgMTAuNTc2MiAwLjAwNjQxMDI2TDE1LjUyOTUgMEwxNS42MjIgMC4wMDkxNTc1MVoiIGZpbGw9ImN1cnJlbnRDb2xvciIgLz48cGF0aCBkPSJNMC4zNzcyOSAxNS45OTA4QzAuMjg3MDU3IDE1Ljk3MjkgMC4yMDMzODUgMTUuOTI4NyAwLjEzNzM2MiAxNS44NjI2QzAuMDQ5Mjg4OCAxNS43NzQ2IC0wLjAwMDE1NzAyNCAxNS42NTQ4IC04LjE4MjM1ZS0wNyAxNS41MzAyTDAuMDA2NDA5NDcgMTAuNTc2OUwwLjAxNTU2NyAxMC40ODI2QzAuMDU5Mzg5MSAxMC4yNjg5IDAuMjQ4NzQxIDEwLjEwOCAwLjQ3NTI3NiAxMC4xMDgxQzAuNzM0MTkxIDEwLjEwODQgMC45NDQ0MTUgMTAuMzE4OSAwLjk0NDE0MyAxMC41Nzc4TDAuOTM5NTY0IDE0LjM5ODRMNS44MjIzNyA5LjUxNDY1QzYuMDA1NDcgOS4zMzE1NSA2LjMwMjI3IDkuMzMxNTUgNi40ODUzOCA5LjUxNDY1QzYuNjY4NDggOS42OTc3NiA2LjY2ODQ4IDkuOTk0NTUgNi40ODUzOCAxMC4xNzc3TDEuNjAyNTcgMTUuMDYxNEw1LjQyMjE4IDE1LjA1NTlMNS41MTY1MSAxNS4wNjVDNS43MzAyOSAxNS4xMDg0IDUuODkxNjggMTUuMjk4MSA1Ljg5MTk3IDE1LjUyNDdDNS44OTIwOCAxNS43ODM1IDUuNjgxOTIgMTUuOTkzMyA1LjQyMzEgMTUuOTkzNkwwLjQ2OTc4MSAxNkwwLjM3NzI5IDE1Ljk5MDhaIiBmaWxsPSJjdXJyZW50Q29sb3IiIC8+PC9zdmc+" /></span></span>
</figure>

</div>

</div>

<div>

<div class="my-8">

<figure class="overflow-hidden rounded-2xl border border-[#4a464f] bg-muted/30">
<span class="group relative inline-block transition-all duration-200 cursor-zoom-in" style="display:block" tabindex="0" role="button" aria-label="Open image lightbox: Example of Kiro chat agent summarizing the Snyk AI-BOM output"><span class="relative overflow-hidden h-auto w-full border-0"><span class="absolute inset-0 flex animate-pulse items-center justify-center bg-muted"><span class="sr-only">Loading image...</span></span><img src="/images/blogs/kiro-and-snyk-guardrails/6.png?h=6d9e61e7" class="transition-opacity duration-300 opacity-0" style="color:transparent" loading="lazy" decoding="async" data-nimg="1" width="1200" height="600" alt="Example of Kiro chat agent summarizing the Snyk AI-BOM output" /></span><span class="absolute bottom-2 right-2 z-10 flex items-center justify-center rounded-full bg-prey-600/60 p-2.5 transition-opacity duration-200 opacity-100 group-hover:opacity-100" aria-hidden="true"><img src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdib3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48cGF0aCBkPSJNMTUuNjIyIDAuMDA5MTU3NTFDMTUuNzEyMyAwLjAyNzEzMzUgMTUuNzk1OSAwLjA3MTM0IDE1Ljg2MiAwLjEzNzM2M0MxNS45NSAwLjIyNTQzNiAxNS45OTk1IDAuMzQ1MjI2IDE1Ljk5OTMgMC40Njk3OEwxNS45OTI5IDUuNDIzMDhMMTUuOTgzNyA1LjUxNzRDMTUuOTM5OSA1LjczMTA2IDE1Ljc1MDYgNS44OTIwNCAxNS41MjQgNS44OTE5NEMxNS4yNjUxIDUuODkxNjIgMTUuMDU0OSA1LjY4MTA2IDE1LjA1NTIgNS40MjIxNkwxNS4wNTk3IDEuNjAxNjVMMTAuMTc2OSA2LjQ4NTM1QzkuOTkzODQgNi42Njg0NSA5LjY5NzA0IDYuNjY4NDUgOS41MTM5NCA2LjQ4NTM1QzkuMzMwODMgNi4zMDIyNCA5LjMzMDgzIDYuMDA1NDUgOS41MTM5NCA1LjgyMjM0TDE0LjM5NjcgMC45Mzg2NDVMMTAuNTc3MSAwLjk0NDEzOUwxMC40ODI4IDAuOTM0OTgyQzEwLjI2OSAwLjg5MTU4NCAxMC4xMDc2IDAuNzAxOTAzIDEwLjEwNzMgMC40NzUyNzVDMTAuMTA3MiAwLjIxNjUwNyAxMC4zMTc0IDAuMDA2NzM0ODQgMTAuNTc2MiAwLjAwNjQxMDI2TDE1LjUyOTUgMEwxNS42MjIgMC4wMDkxNTc1MVoiIGZpbGw9ImN1cnJlbnRDb2xvciIgLz48cGF0aCBkPSJNMC4zNzcyOSAxNS45OTA4QzAuMjg3MDU3IDE1Ljk3MjkgMC4yMDMzODUgMTUuOTI4NyAwLjEzNzM2MiAxNS44NjI2QzAuMDQ5Mjg4OCAxNS43NzQ2IC0wLjAwMDE1NzAyNCAxNS42NTQ4IC04LjE4MjM1ZS0wNyAxNS41MzAyTDAuMDA2NDA5NDcgMTAuNTc2OUwwLjAxNTU2NyAxMC40ODI2QzAuMDU5Mzg5MSAxMC4yNjg5IDAuMjQ4NzQxIDEwLjEwOCAwLjQ3NTI3NiAxMC4xMDgxQzAuNzM0MTkxIDEwLjEwODQgMC45NDQ0MTUgMTAuMzE4OSAwLjk0NDE0MyAxMC41Nzc4TDAuOTM5NTY0IDE0LjM5ODRMNS44MjIzNyA5LjUxNDY1QzYuMDA1NDcgOS4zMzE1NSA2LjMwMjI3IDkuMzMxNTUgNi40ODUzOCA5LjUxNDY1QzYuNjY4NDggOS42OTc3NiA2LjY2ODQ4IDkuOTk0NTUgNi40ODUzOCAxMC4xNzc3TDEuNjAyNTcgMTUuMDYxNEw1LjQyMjE4IDE1LjA1NTlMNS41MTY1MSAxNS4wNjVDNS43MzAyOSAxNS4xMDg0IDUuODkxNjggMTUuMjk4MSA1Ljg5MTk3IDE1LjUyNDdDNS44OTIwOCAxNS43ODM1IDUuNjgxOTIgMTUuOTkzMyA1LjQyMzEgMTUuOTkzNkwwLjQ2OTc4MSAxNkwwLjM3NzI5IDE1Ljk5MDhaIiBmaWxsPSJjdXJyZW50Q29sb3IiIC8+PC9zdmc+" /></span></span>
</figure>

</div>

</div>

<div class="heading-anchor-wrapper">

## 3. Behavioral security for AI-specific vulnerabilities: toxic flow analysis

<a href="#3-behavioral-security-for-ai-specific-vulnerabilities-toxic-flow-analysis" class="anchor-link" aria-label="Copy link to 3 behavioral security for ai specific vulnerabilities toxic flow analysis section"><span class="anchor-icon-wrapper"><img src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iYW5jaG9yLWljb24iIHZpZXdib3g9IjAgMCAxNiAxNyIgd2lkdGg9IjE2IiBoZWlnaHQ9IjE3IiBmaWxsPSJjdXJyZW50Q29sb3IiPjxwYXRoIGQ9Ik0yLjI3MTQzIDE0LjIyOEMwLjU5MTg5NyAxMi41NDg1IDAuNTkxODk3IDkuODI1MzkgMi4yNzE0MyA4LjE0NTg1TDMuNDIzMjQgNi45OTQwNEwzLjQ0MTg4IDYuOTc2MzVDMy42MzgxNiA2Ljc5OSAzLjk0MTE4IDYuODA0ODggNC4xMzAzNSA2Ljk5NDA0QzQuMzE5NTEgNy4xODMyMSA0LjMyNTM5IDcuNDg2MjMgNC4xNDgwNCA3LjY4MjVMNC4xMzAzNSA3LjcwMTE1TDIuOTc4NTQgOC44NTI5NkMxLjY4OTUzIDEwLjE0MiAxLjY4OTUzIDEyLjIzMTkgMi45Nzg1NCAxMy41MjA5TDMuMDA4ODggMTMuNTUwOUM0LjMwMDE0IDE0LjgwOTggNi4zNjc1MSAxNC43OTk4IDcuNjQ2NDYgMTMuNTIwOUw4Ljc5ODI3IDEyLjM2OTFMOC44MTY5MSAxMi4zNTE0QzkuMDEzMTkgMTIuMTc0IDkuMzE2MjEgMTIuMTc5OSA5LjUwNTM4IDEyLjM2OTFDOS42OTQ1NCAxMi41NTgyIDkuNzAwNDYgMTIuODYxMyA5LjUyMzExIDEzLjA1NzZMOS41MDUzOCAxMy4wNzYyTDguMzUzNTYgMTQuMjI4QzYuNjg3MTUgMTUuODk0NCAzLjk5MzQ3IDE1LjkwNzQgMi4zMTEgMTQuMjY3TDIuMjcxNDMgMTQuMjI4Wk0xMy4wMjE1IDMuNDc3OTNDMTEuNzQyNSAyLjE5ODk5IDkuNjc1MTcgMi4xODg5NiA4LjM4MzkgMy40NDc5NEw4LjM1MzU2IDMuNDc3OTNMNy4yMjU3OSA0LjYwNTdDNy4wMzA1MyA0LjgwMDk2IDYuNzEzOTUgNC44MDA5NiA2LjUxODY5IDQuNjA1N0M2LjMyMzQyIDQuNDEwNDQgNi4zMjM0MiA0LjA5Mzg2IDYuNTE4NjkgMy44OTg1OUw3LjY0NjQ2IDIuNzcwODJMNy42ODYwMyAyLjczMTc3QzkuMzY4NSAxLjA5MTM4IDEyLjA2MjIgMS4xMDQ0MSAxMy43Mjg2IDIuNzcwODJMMTMuNzY3NyAyLjgxMDM2QzE1LjM5NTIgNC40Nzk1OCAxNS4zOTUxIDcuMTQ0MTcgMTMuNzY3NyA4LjgxMzM4TDEzLjcyODYgOC44NTI5NkwxMi42MDA4IDkuOTgwNzNDMTIuNDA1NiAxMC4xNzYgMTIuMDg5IDEwLjE3NiAxMS44OTM3IDkuOTgwNzNDMTEuNjk4NSA5Ljc4NTQ3IDExLjY5ODUgOS40Njg4OCAxMS44OTM3IDkuMjczNjJMMTMuMDIxNSA4LjE0NTg1TDEzLjA1MTUgOC4xMTU1MUMxNC4zMDA1IDYuODM0NDIgMTQuMzAwNSA0Ljc4OTM3IDEzLjA1MTUgMy41MDgyN0wxMy4wMjE1IDMuNDc3OTNaIiAvPjxwYXRoIGQ9Ik0xMC4wMjE5IDUuODY2MzJMMTAuMDQwNiA1Ljg0ODU4QzEwLjIzNjkgNS42NzEyNCAxMC41Mzk5IDUuNjc3MTYgMTAuNzI5IDUuODY2MzJDMTAuOTE4MiA2LjA1NTQ4IDEwLjkyNDEgNi4zNTg0NiAxMC43NDY4IDYuNTU0NzRMMTAuNzI5IDYuNTczNDJMNi4xNDU4OCAxMS4xNTY2QzUuOTUwNjIgMTEuMzUxOCA1LjYzNDAzIDExLjM1MTggNS40Mzg3NyAxMS4xNTY2QzUuMjQzNTEgMTAuOTYxMyA1LjI0MzUxIDEwLjY0NDcgNS40Mzg3NyAxMC40NDk1TDEwLjAyMTkgNS44NjYzMloiIC8+PC9zdmc+" class="anchor-icon" /><span class="copied-indicator docsearch-exclude" aria-live="polite" aria-atomic="true"></span></span></a>

</div>

AI-powered development introduces novel threat vectors. <a href="https://labs.snyk.io/resources/toxic-flow-analysis/" class="text-primary hover:underline" target="_blank" rel="noopener noreferrer">Toxic Flow Analysis</a> is a critical security layer designed to detect complex, AI-specific vulnerabilities like prompt injection. By tracking how the user inputs flow through the AI systems, Toxic Flow Analysis identifies points where malicious prompts could influence model behavior, thereby protecting your applications from potential AI-driven threats.

<div>

<div class="my-8">

<figure class="overflow-hidden rounded-2xl border border-[#4a464f] bg-muted/30">
<span class="group relative inline-block transition-all duration-200 cursor-zoom-in" style="display:block" tabindex="0" role="button" aria-label="Open image lightbox: The Snyk Toxic Flow Analysis output example "><span class="relative overflow-hidden h-auto w-full border-0"><span class="absolute inset-0 flex animate-pulse items-center justify-center bg-muted"><span class="sr-only">Loading image...</span></span><img src="/images/blogs/kiro-and-snyk-guardrails/7.png?h=d81caa0e" class="transition-opacity duration-300 opacity-0" style="color:transparent" loading="lazy" decoding="async" data-nimg="1" width="1200" height="600" alt="The Snyk Toxic Flow Analysis output example " /></span><span class="absolute bottom-2 right-2 z-10 flex items-center justify-center rounded-full bg-prey-600/60 p-2.5 transition-o

[truncated]
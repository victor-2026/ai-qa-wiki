# Source: https://kiro.dev/blog/property-based-testing-fixed-security-bug/

**URL:** https://kiro.dev/blog/property-based-testing-fixed-security-bug/
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

December 18, 2025

</div>

# Property-Based Testing Caught a Security Bug I Never Would Have Found

<div class="flex items-center gap-2">

<span class="text-sm text-muted-foreground">By</span>

<div class="flex flex-wrap items-center gap-4">

<div class="flex items-center gap-2">

<span class="relative flex shrink-0 overflow-hidden rounded-full h-8 w-8"><span class="flex h-full w-full items-center justify-center rounded-full bg-muted">KR</span></span>

<div>

Krishiv Dakwala

Software Development Engineer

</div>

</div>

</div>

</div>

</div>

<div class="blog-content changelog prose-prey prose max-w-none dark:prose-invert prose-code:before:content-none prose-code:after:content-none">

<div class="heading-anchor-wrapper">

### When Targeted Random Testing Finds Real Security Vulnerabilities

<a href="#when-targeted-random-testing-finds-real-security-vulnerabilities" class="anchor-link" aria-label="Copy link to When targeted random testing finds real security vulnerabilities section"><span class="anchor-icon-wrapper"><img src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iYW5jaG9yLWljb24iIHZpZXdib3g9IjAgMCAxNiAxNyIgd2lkdGg9IjE2IiBoZWlnaHQ9IjE3IiBmaWxsPSJjdXJyZW50Q29sb3IiPjxwYXRoIGQ9Ik0yLjI3MTQzIDE0LjIyOEMwLjU5MTg5NyAxMi41NDg1IDAuNTkxODk3IDkuODI1MzkgMi4yNzE0MyA4LjE0NTg1TDMuNDIzMjQgNi45OTQwNEwzLjQ0MTg4IDYuOTc2MzVDMy42MzgxNiA2Ljc5OSAzLjk0MTE4IDYuODA0ODggNC4xMzAzNSA2Ljk5NDA0QzQuMzE5NTEgNy4xODMyMSA0LjMyNTM5IDcuNDg2MjMgNC4xNDgwNCA3LjY4MjVMNC4xMzAzNSA3LjcwMTE1TDIuOTc4NTQgOC44NTI5NkMxLjY4OTUzIDEwLjE0MiAxLjY4OTUzIDEyLjIzMTkgMi45Nzg1NCAxMy41MjA5TDMuMDA4ODggMTMuNTUwOUM0LjMwMDE0IDE0LjgwOTggNi4zNjc1MSAxNC43OTk4IDcuNjQ2NDYgMTMuNTIwOUw4Ljc5ODI3IDEyLjM2OTFMOC44MTY5MSAxMi4zNTE0QzkuMDEzMTkgMTIuMTc0IDkuMzE2MjEgMTIuMTc5OSA5LjUwNTM4IDEyLjM2OTFDOS42OTQ1NCAxMi41NTgyIDkuNzAwNDYgMTIuODYxMyA5LjUyMzExIDEzLjA1NzZMOS41MDUzOCAxMy4wNzYyTDguMzUzNTYgMTQuMjI4QzYuNjg3MTUgMTUuODk0NCAzLjk5MzQ3IDE1LjkwNzQgMi4zMTEgMTQuMjY3TDIuMjcxNDMgMTQuMjI4Wk0xMy4wMjE1IDMuNDc3OTNDMTEuNzQyNSAyLjE5ODk5IDkuNjc1MTcgMi4xODg5NiA4LjM4MzkgMy40NDc5NEw4LjM1MzU2IDMuNDc3OTNMNy4yMjU3OSA0LjYwNTdDNy4wMzA1MyA0LjgwMDk2IDYuNzEzOTUgNC44MDA5NiA2LjUxODY5IDQuNjA1N0M2LjMyMzQyIDQuNDEwNDQgNi4zMjM0MiA0LjA5Mzg2IDYuNTE4NjkgMy44OTg1OUw3LjY0NjQ2IDIuNzcwODJMNy42ODYwMyAyLjczMTc3QzkuMzY4NSAxLjA5MTM4IDEyLjA2MjIgMS4xMDQ0MSAxMy43Mjg2IDIuNzcwODJMMTMuNzY3NyAyLjgxMDM2QzE1LjM5NTIgNC40Nzk1OCAxNS4zOTUxIDcuMTQ0MTcgMTMuNzY3NyA4LjgxMzM4TDEzLjcyODYgOC44NTI5NkwxMi42MDA4IDkuOTgwNzNDMTIuNDA1NiAxMC4xNzYgMTIuMDg5IDEwLjE3NiAxMS44OTM3IDkuOTgwNzNDMTEuNjk4NSA5Ljc4NTQ3IDExLjY5ODUgOS40Njg4OCAxMS44OTM3IDkuMjczNjJMMTMuMDIxNSA4LjE0NTg1TDEzLjA1MTUgOC4xMTU1MUMxNC4zMDA1IDYuODM0NDIgMTQuMzAwNSA0Ljc4OTM3IDEzLjA1MTUgMy41MDgyN0wxMy4wMjE1IDMuNDc3OTNaIiAvPjxwYXRoIGQ9Ik0xMC4wMjE5IDUuODY2MzJMMTAuMDQwNiA1Ljg0ODU4QzEwLjIzNjkgNS42NzEyNCAxMC41Mzk5IDUuNjc3MTYgMTAuNzI5IDUuODY2MzJDMTAuOTE4MiA2LjA1NTQ4IDEwLjkyNDEgNi4zNTg0NiAxMC43NDY4IDYuNTU0NzRMMTAuNzI5IDYuNTczNDJMNi4xNDU4OCAxMS4xNTY2QzUuOTUwNjIgMTEuMzUxOCA1LjYzNDAzIDExLjM1MTggNS40Mzg3NyAxMS4xNTY2QzUuMjQzNTEgMTAuOTYxMyA1LjI0MzUxIDEwLjY0NDcgNS40Mzg3NyAxMC40NDk1TDEwLjAyMTkgNS44NjYzMloiIC8+PC9zdmc+" class="anchor-icon" /><span class="copied-indicator docsearch-exclude" aria-live="polite" aria-atomic="true"></span></span></a>

</div>

Security vulnerabilities often hide in the corners of our code that we never think to test. We write unit tests for the happy path, maybe a few edge cases we can imagine, but what about the inputs we'd never consider? Many times we assume that LLMs are handling these scenarios by default, however LLM-generated code can be as prone to contain bugs or vulnerabilities as human-written code. What happens when a user enters a malicious string into your application?

This is exactly what happened when we tested building a storage service for a chat application using AI with Kiro’s <a href="/blog/property-based-testing/" class="text-primary hover:underline">latest GA features</a>. Following a <a href="/docs/specs/" class="text-primary hover:underline">specification-driven development (SDD) workflow</a>, Kiro carefully defined the requirements, extracted testable properties, and implemented what seemed like straightforward code for storing and retrieving API keys. The implementation looked solid. Code review would likely have approved it. Traditional unit tests would have passed.

But on the 75th iteration of a property-based test, something unexpected happened: the entire round-trip property failed. What should have been a simple save-and-retrieve operation instead exposed a mishandling of javascript prototypes—a bug that can lead to security issues in the future if you’re not careful to eliminate the flaw early on.

This post tells the story of how Property-Based Testing (PBT) caught a security bug that human intuition and traditional testing methods would likely have missed. We'll walk through:

- The specification and property that Kiro defined
- The seemingly innocent implementation that contained a critical flaw
- How PBT's systematic exploration of the input space uncovered the vulnerability
- The fix that addresses the vulnerability
- Why this matters for building secure software

This isn't just a theoretical exercise—it's a real example of how automated testing techniques can find the edge cases that keep security researchers up at night, before they make it to production.

<div class="heading-anchor-wrapper">

### Background

<a href="#background" class="anchor-link" aria-label="Copy link to Background section"><span class="anchor-icon-wrapper"><img src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iYW5jaG9yLWljb24iIHZpZXdib3g9IjAgMCAxNiAxNyIgd2lkdGg9IjE2IiBoZWlnaHQ9IjE3IiBmaWxsPSJjdXJyZW50Q29sb3IiPjxwYXRoIGQ9Ik0yLjI3MTQzIDE0LjIyOEMwLjU5MTg5NyAxMi41NDg1IDAuNTkxODk3IDkuODI1MzkgMi4yNzE0MyA4LjE0NTg1TDMuNDIzMjQgNi45OTQwNEwzLjQ0MTg4IDYuOTc2MzVDMy42MzgxNiA2Ljc5OSAzLjk0MTE4IDYuODA0ODggNC4xMzAzNSA2Ljk5NDA0QzQuMzE5NTEgNy4xODMyMSA0LjMyNTM5IDcuNDg2MjMgNC4xNDgwNCA3LjY4MjVMNC4xMzAzNSA3LjcwMTE1TDIuOTc4NTQgOC44NTI5NkMxLjY4OTUzIDEwLjE0MiAxLjY4OTUzIDEyLjIzMTkgMi45Nzg1NCAxMy41MjA5TDMuMDA4ODggMTMuNTUwOUM0LjMwMDE0IDE0LjgwOTggNi4zNjc1MSAxNC43OTk4IDcuNjQ2NDYgMTMuNTIwOUw4Ljc5ODI3IDEyLjM2OTFMOC44MTY5MSAxMi4zNTE0QzkuMDEzMTkgMTIuMTc0IDkuMzE2MjEgMTIuMTc5OSA5LjUwNTM4IDEyLjM2OTFDOS42OTQ1NCAxMi41NTgyIDkuNzAwNDYgMTIuODYxMyA5LjUyMzExIDEzLjA1NzZMOS41MDUzOCAxMy4wNzYyTDguMzUzNTYgMTQuMjI4QzYuNjg3MTUgMTUuODk0NCAzLjk5MzQ3IDE1LjkwNzQgMi4zMTEgMTQuMjY3TDIuMjcxNDMgMTQuMjI4Wk0xMy4wMjE1IDMuNDc3OTNDMTEuNzQyNSAyLjE5ODk5IDkuNjc1MTcgMi4xODg5NiA4LjM4MzkgMy40NDc5NEw4LjM1MzU2IDMuNDc3OTNMNy4yMjU3OSA0LjYwNTdDNy4wMzA1MyA0LjgwMDk2IDYuNzEzOTUgNC44MDA5NiA2LjUxODY5IDQuNjA1N0M2LjMyMzQyIDQuNDEwNDQgNi4zMjM0MiA0LjA5Mzg2IDYuNTE4NjkgMy44OTg1OUw3LjY0NjQ2IDIuNzcwODJMNy42ODYwMyAyLjczMTc3QzkuMzY4NSAxLjA5MTM4IDEyLjA2MjIgMS4xMDQ0MSAxMy43Mjg2IDIuNzcwODJMMTMuNzY3NyAyLjgxMDM2QzE1LjM5NTIgNC40Nzk1OCAxNS4zOTUxIDcuMTQ0MTcgMTMuNzY3NyA4LjgxMzM4TDEzLjcyODYgOC44NTI5NkwxMi42MDA4IDkuOTgwNzNDMTIuNDA1NiAxMC4xNzYgMTIuMDg5IDEwLjE3NiAxMS44OTM3IDkuOTgwNzNDMTEuNjk4NSA5Ljc4NTQ3IDExLjY5ODUgOS40Njg4OCAxMS44OTM3IDkuMjczNjJMMTMuMDIxNSA4LjE0NTg1TDEzLjA1MTUgOC4xMTU1MUMxNC4zMDA1IDYuODM0NDIgMTQuMzAwNSA0Ljc4OTM3IDEzLjA1MTUgMy41MDgyN0wxMy4wMjE1IDMuNDc3OTNaIiAvPjxwYXRoIGQ9Ik0xMC4wMjE5IDUuODY2MzJMMTAuMDQwNiA1Ljg0ODU4QzEwLjIzNjkgNS42NzEyNCAxMC41Mzk5IDUuNjc3MTYgMTAuNzI5IDUuODY2MzJDMTAuOTE4MiA2LjA1NTQ4IDEwLjkyNDEgNi4zNTg0NiAxMC43NDY4IDYuNTU0NzRMMTAuNzI5IDYuNTczNDJMNi4xNDU4OCAxMS4xNTY2QzUuOTUwNjIgMTEuMzUxOCA1LjYzNDAzIDExLjM1MTggNS40Mzg3NyAxMS4xNTY2QzUuMjQzNTEgMTAuOTYxMyA1LjI0MzUxIDEwLjY0NDcgNS40Mzg3NyAxMC40NDk1TDEwLjAyMTkgNS44NjYzMloiIC8+PC9zdmc+" class="anchor-icon" /><span class="copied-indicator docsearch-exclude" aria-live="polite" aria-atomic="true"></span></span></a>

</div>

When working through building an application with some customers and walking through their prompts for a Spec, Kiro was implementing a storage system for a chat application that saves user data to browser localStorage. One key feature was storing API keys for different LLM providers (like OpenAI, Anthropic, etc.). Users could save their API keys using a provider name as the key. This object would have API like the following:

<div class="my-6 rounded-md bg-muted-foreground/10 p-4">

Loading code example...

</div>

Kiro, following SDD formulated the following requirement:

<div class="promptBox">

<div class="my-6 rounded-md bg-muted-foreground/10 p-4">

Loading code example...

</div>

</div>

Let’s drill down on acceptance criteria `2`, which Kiro decided to pick as a key correctness property:

<div class="promptBox">

<div class="my-6 rounded-md bg-muted-foreground/10 p-4">

Loading code example...

</div>

</div>

Kiro calls this a “round-trip” property. Round-trips are a common shape for correctness properties, where you start with an arbitrary value, perform some sequence of operations, and end up with the same value. In this case, we’re asserting that if we start with an arbitrary string values `provider` and `key`:

1.  Store the `key` under `provider` in storage
2.  Retrieve the value associated with `provider`

Then the value we get back should be equal to `key`. If this isn’t true (say, we get back a different value, or an exception is thrown), then clearly something is wrong with our implementation. This spec looks great, so we’ll sign off on it, and have Kiro implement our api.

The LLM produced the following code as part of our API:

<div class="my-6 rounded-md bg-muted-foreground/10 p-4">

Loading code example...

</div>

Kiro then proceeded to test this code using property-based testing, to gather evidence that the property we expect to hold, actually does. To check Property 2, Kiro wrote the following test, using the <a href="https://fast-check.dev/" class="text-primary hover:underline" target="_blank" rel="noopener noreferrer">fast-check</a> library for TypeScript:

<div class="my-6 rounded-md bg-muted-foreground/10 p-4">

Loading code example...

</div>

Kiro runs this test, and on trial \#75 → we get a failure! Kiro proceeds to shrink the failure and then reports to us the following counterexample: the provider `"__proto__"` and and the apikey `" "`.

<div>

<div class="my-8">

<figure class="overflow-hidden rounded-2xl border border-[#4a464f] bg-muted/30">
<span class="group relative inline-block transition-all duration-200 cursor-zoom-in" style="display:block" tabindex="0" role="button" aria-label="Open image lightbox: kiro-pbt-failure"><span class="relative overflow-hidden h-auto w-full border-0"><span class="absolute inset-0 flex animate-pulse items-center justify-center bg-muted"><span class="sr-only">Loading image...</span></span><img src="/images/blogs/migrated/1cbb87f99fb4792967c3fa9a2464efd9-kiro-pbt-failure.png?h=75c75f97" class="transition-opacity duration-300 opacity-0" style="color:transparent" loading="lazy" decoding="async" data-nimg="1" width="1200" height="600" alt="kiro-pbt-failure" /></span><span class="absolute bottom-2 right-2 z-10 flex items-center justify-center rounded-full bg-prey-600/60 p-2.5 transition-opacity duration-200 opacity-100 group-hover:opacity-100" aria-hidden="true"><img src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdib3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48cGF0aCBkPSJNMTUuNjIyIDAuMDA5MTU3NTFDMTUuNzEyMyAwLjAyNzEzMzUgMTUuNzk1OSAwLjA3MTM0IDE1Ljg2MiAwLjEzNzM2M0MxNS45NSAwLjIyNTQzNiAxNS45OTk1IDAuMzQ1MjI2IDE1Ljk5OTMgMC40Njk3OEwxNS45OTI5IDUuNDIzMDhMMTUuOTgzNyA1LjUxNzRDMTUuOTM5OSA1LjczMTA2IDE1Ljc1MDYgNS44OTIwNCAxNS41MjQgNS44OTE5NEMxNS4yNjUxIDUuODkxNjIgMTUuMDU0OSA1LjY4MTA2IDE1LjA1NTIgNS40MjIxNkwxNS4wNTk3IDEuNjAxNjVMMTAuMTc2OSA2LjQ4NTM1QzkuOTkzODQgNi42Njg0NSA5LjY5NzA0IDYuNjY4NDUgOS41MTM5NCA2LjQ4NTM1QzkuMzMwODMgNi4zMDIyNCA5LjMzMDgzIDYuMDA1NDUgOS41MTM5NCA1LjgyMjM0TDE0LjM5NjcgMC45Mzg2NDVMMTAuNTc3MSAwLjk0NDEzOUwxMC40ODI4IDAuOTM0OTgyQzEwLjI2OSAwLjg5MTU4NCAxMC4xMDc2IDAuNzAxOTAzIDEwLjEwNzMgMC40NzUyNzVDMTAuMTA3MiAwLjIxNjUwNyAxMC4zMTc0IDAuMDA2NzM0ODQgMTAuNTc2MiAwLjAwNjQxMDI2TDE1LjUyOTUgMEwxNS42MjIgMC4wMDkxNTc1MVoiIGZpbGw9ImN1cnJlbnRDb2xvciIgLz48cGF0aCBkPSJNMC4zNzcyOSAxNS45OTA4QzAuMjg3MDU3IDE1Ljk3MjkgMC4yMDMzODUgMTUuOTI4NyAwLjEzNzM2MiAxNS44NjI2QzAuMDQ5Mjg4OCAxNS43NzQ2IC0wLjAwMDE1NzAyNCAxNS42NTQ4IC04LjE4MjM1ZS0wNyAxNS41MzAyTDAuMDA2NDA5NDcgMTAuNTc2OUwwLjAxNTU2NyAxMC40ODI2QzAuMDU5Mzg5MSAxMC4yNjg5IDAuMjQ4NzQxIDEwLjEwOCAwLjQ3NTI3NiAxMC4xMDgxQzAuNzM0MTkxIDEwLjEwODQgMC45NDQ0MTUgMTAuMzE4OSAwLjk0NDE0MyAxMC41Nzc4TDAuOTM5NTY0IDE0LjM5ODRMNS44MjIzNyA5LjUxNDY1QzYuMDA1NDcgOS4zMzE1NSA2LjMwMjI3IDkuMzMxNTUgNi40ODUzOCA5LjUxNDY1QzYuNjY4NDggOS42OTc3NiA2LjY2ODQ4IDkuOTk0NTUgNi40ODUzOCAxMC4xNzc3TDEuNjAyNTcgMTUuMDYxNEw1LjQyMjE4IDE1LjA1NTlMNS41MTY1MSAxNS4wNjVDNS43MzAyOSAxNS4xMDg0IDUuODkxNjggMTUuMjk4MSA1Ljg5MTk3IDE1LjUyNDdDNS44OTIwOCAxNS43ODM1IDUuNjgxOTIgMTUuOTkzMyA1LjQyMzEgMTUuOTkzNkwwLjQ2OTc4MSAxNkwwLjM3NzI5IDE1Ljk5MDhaIiBmaWxsPSJjdXJyZW50Q29sb3IiIC8+PC9zdmc+" /></span></span>
</figure>

</div>

</div>

<div class="heading-anchor-wrapper">

### What’s going on?

<a href="#whats-going-on" class="anchor-link" aria-label="Copy link to Whats going on section"><span class="anchor-icon-wrapper"><img src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iYW5jaG9yLWljb24iIHZpZXdib3g9IjAgMCAxNiAxNyIgd2lkdGg9IjE2IiBoZWlnaHQ9IjE3IiBmaWxsPSJjdXJyZW50Q29sb3IiPjxwYXRoIGQ9Ik0yLjI3MTQzIDE0LjIyOEMwLjU5MTg5NyAxMi41NDg1IDAuNTkxODk3IDkuODI1MzkgMi4yNzE0MyA4LjE0NTg1TDMuNDIzMjQgNi45OTQwNEwzLjQ0MTg4IDYuOTc2MzVDMy42MzgxNiA2Ljc5OSAzLjk0MTE4IDYuODA0ODggNC4xMzAzNSA2Ljk5NDA0QzQuMzE5NTEgNy4xODMyMSA0LjMyNTM5IDcuNDg2MjMgNC4xNDgwNCA3LjY4MjVMNC4xMzAzNSA3LjcwMTE1TDIuOTc4NTQgOC44NTI5NkMxLjY4OTUzIDEwLjE0MiAxLjY4OTUzIDEyLjIzMTkgMi45Nzg1NCAxMy41MjA5TDMuMDA4ODggMTMuNTUwOUM0LjMwMDE0IDE0LjgwOTggNi4zNjc1MSAxNC43OTk4IDcuNjQ2NDYgMTMuNTIwOUw4Ljc5ODI3IDEyLjM2OTFMOC44MTY5MSAxMi4zNTE0QzkuMDEzMTkgMTIuMTc0IDkuMzE2MjEgMTIuMTc5OSA5LjUwNTM4IDEyLjM2OTFDOS42OTQ1NCAxMi41NTgyIDkuNzAwNDYgMTIuODYxMyA5LjUyMzExIDEzLjA1NzZMOS41MDUzOCAxMy4wNzYyTDguMzUzNTYgMTQuMjI4QzYuNjg3MTUgMTUuODk0NCAzLjk5MzQ3IDE1LjkwNzQgMi4zMTEgMTQuMjY3TDIuMjcxNDMgMTQuMjI4Wk0xMy4wMjE1IDMuNDc3OTNDMTEuNzQyNSAyLjE5ODk5IDkuNjc1MTcgMi4xODg5NiA4LjM4MzkgMy40NDc5NEw4LjM1MzU2IDMuNDc3OTNMNy4yMjU3OSA0LjYwNTdDNy4wMzA1MyA0LjgwMDk2IDYuNzEzOTUgNC44MDA5NiA2LjUxODY5IDQuNjA1N0M2LjMyMzQyIDQuNDEwNDQgNi4zMjM0MiA0LjA5Mzg2IDYuNTE4NjkgMy44OTg1OUw3LjY0NjQ2IDIuNzcwODJMNy42ODYwMyAyLjczMTc3QzkuMzY4NSAxLjA5MTM4IDEyLjA2MjIgMS4xMDQ0MSAxMy43Mjg2IDIuNzcwODJMMTMuNzY3NyAyLjgxMDM2QzE1LjM5NTIgNC40Nzk1OCAxNS4zOTUxIDcuMTQ0MTcgMTMuNzY3NyA4LjgxMzM4TDEzLjcyODYgOC44NTI5NkwxMi42MDA4IDkuOTgwNzNDMTIuNDA1NiAxMC4xNzYgMTIuMDg5IDEwLjE3NiAxMS44OTM3IDkuOTgwNzNDMTEuNjk4NSA5Ljc4NTQ3IDExLjY5ODUgOS40Njg4OCAxMS44OTM3IDkuMjczNjJMMTMuMDIxNSA4LjE0NTg1TDEzLjA1MTUgOC4xMTU1MUMxNC4zMDA1IDYuODM0NDIgMTQuMzAwNSA0Ljc4OTM3IDEzLjA1MTUgMy41MDgyN0wxMy4wMjE1IDMuNDc3OTNaIiAvPjxwYXRoIGQ9Ik0xMC4wMjE5IDUuODY2MzJMMTAuMDQwNiA1Ljg0ODU4QzEwLjIzNjkgNS42NzEyNCAxMC41Mzk5IDUuNjc3MTYgMTAuNzI5IDUuODY2MzJDMTAuOTE4MiA2LjA1NTQ4IDEwLjkyNDEgNi4zNTg0NiAxMC43NDY4IDYuNTU0NzRMMTAuNzI5IDYuNTczNDJMNi4xNDU4OCAxMS4xNTY2QzUuOTUwNjIgMTEuMzUxOCA1LjYzNDAzIDExLjM1MTggNS40Mzg3NyAxMS4xNTY2QzUuMjQzNTEgMTAuOTYxMyA1LjI0MzUxIDEwLjY0NDcgNS40Mzg3NyAxMC40NDk1TDEwLjAyMTkgNS44NjYzMloiIC8+PC9zdmc+" class="anchor-icon" /><span class="copied-indicator docsearch-exclude" aria-live="polite" aria-atomic="true"></span></span></a>

</div>

The property-based test generated random strings for provider names, and after 75 test runs, it generated the string `"__proto__"` as a provider name. This caused the test to fail with this counterexample:

<div class="promptBox">

<div class="my-6 rounded-md bg-muted-foreground/10 p-4">

Loading code example...

</div>

</div>

When we try to save an API key with provider name `__proto__`, then load it back, something strange happens and we don’t get the value we expect. Kiro helps us localize the problem by using shrinking, to remove extraneous details from the problem. In this case it reduces our apiKey string to the smallest string allowed by our generators, only containing spaces. This tells us that the problem probably isn’t with the value, but instead that the weird key is what’s causing the issue. If you’re familiar with JavaScript, then this error probably sticks right out at you, but if you’re not read on.

This is a feature of how JavaScript implements its object system. More traditional object oriented programming languages (such as Java, Python, and SmallTalk), use the idea of classes. Each class is a static member of the codebase that describes how to build an object, and describes the inheritance relationship between different objects. JavaScript uses an alternative approach, called “prototypes”. In a prototype-based object system, there are no classes. Instead, every object contains a special field called its prototype that points to a parent object from which it should inherent code and data. This lets the inheritance relationship be configured dynamically. In JavaScript, this prototype lives in the `__proto__` field. When we tried to set the field to a string, the JavaScript engine rejected this, and kept the original prototype in place. This results in us getting back the original prototype (an empty object) when we look up the `provider` in the second step of the property test.

Not all writes to the prototype are as benign as this one. Since the `provider` and `apiKey` are under attacker control, if the attacker found a way to get a non-string value into `apiKey` they could have injected values into the prototype, resulting in further reads from the objects properties potentially returning attacker controlled values.

<div>

<div class="my-8">

<figure class="overflow-hidden rounded-2xl border border-[#4a464f] bg-muted/30">
<span class="group relative inline-block transition-all duration-200 cursor-zoom-in" style="display:block" tabindex="0" role="button" aria-label="Open image lightbox: An example of prototype manipulation"><span class="relative overflow-hidden h-auto w-full border-0"><span class="absolute inset-0 flex animate-pulse items-center justify-center bg-muted"><span class="sr-only">Loading image...</span></span><img src="/images/blogs/migrated/6f7e424ec64096381343813548de311f-Property-Based_Testing_Security_Bug.png?h=fa9d72f2" class="transition-opacity duration-300 opacity-0" style="color:transparent" loading="lazy" decoding="async" data-nimg="1" width="1200" height="600" alt="An example of prototype manipulation" /></span><span class="absolute bottom-2 right-2 z-10 flex items-center justify-center rounded-full bg-prey-600/60 p-2.5 transition-opacity duration-200 opacity-100 group-hover:opacity-100" aria-hidden="true"><img src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdib3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48cGF0aCBkPSJNMTUuNjIyIDAuMDA5MTU3NTFDMTUuNzEyMyAwLjAyNzEzMzUgMTUuNzk1OSAwLjA3MTM0IDE1Ljg2MiAwLjEzNzM2M0MxNS45NSAwLjIyNTQzNiAxNS45OTk1IDAuMzQ1MjI2IDE1Ljk5OTMgMC40Njk3OEwxNS45OTI5IDUuNDIzMDhMMTUuOTgzNyA1LjUxNzRDMTUuOTM5OSA1LjczMTA2IDE1Ljc1MDYgNS44OTIwNCAxNS41MjQgNS44OTE5NEMxNS4yNjUxIDUuODkxNjIgMTUuMDU0OSA1LjY4MTA2IDE1LjA1NTIgNS40MjIxNkwxNS4wNTk3IDEuNjAxNjVMMTAuMTc2OSA2LjQ4NTM1QzkuOTkzODQgNi42Njg0NSA5LjY5NzA0IDYuNjY4NDUgOS41MTM5NCA2LjQ4NTM1QzkuMzMwODMgNi4zMDIyNCA5LjMzMDgzIDYuMDA1NDUgOS41MTM5NCA1LjgyMjM0TDE0LjM5NjcgMC45Mzg2NDVMMTAuNTc3MSAwLjk0NDEzOUwxMC40ODI4IDAuOTM0OTgyQzEwLjI2OSAwLjg5MTU4NCAxMC4xMDc2IDAuNzAxOTAzIDEwLjEwNzMgMC40NzUyNzVDMTAuMTA3MiAwLjIxNjUwNyAxMC4zMTc0IDAuMDA2NzM0ODQgMTAuNTc2MiAwLjAwNjQxMDI2TDE1LjUyOTUgMEwxNS42MjIgMC4wMDkxNTc1MVoiIGZpbGw9ImN1cnJlbnRDb2xvciIgLz48cGF0aCBkPSJNMC4zNzcyOSAxNS45OTA4QzAuMjg3MDU3IDE1Ljk3MjkgMC4yMDMzODUgMTUuOTI4NyAwLjEzNzM2MiAxNS44NjI2QzAuMDQ5Mjg4OCAxNS43NzQ2IC0wLjAwMDE1NzAyNCAxNS42NTQ4IC04LjE4MjM1ZS0wNyAxNS41MzAyTDAuMDA2NDA5NDcgMTAuNTc2OUwwLjAxNTU2NyAxMC40ODI2QzAuMDU5Mzg5MSAxMC4yNjg5IDAuMjQ4NzQxIDEwLjEwOCAwLjQ3NTI3NiAxMC4xMDgxQzAuNzM0MTkxIDEwLjEwODQgMC45NDQ0MTUgMTAuMzE4OSAwLjk0NDE0MyAxMC41Nzc4TDAuOTM5NTY0IDE0LjM5ODRMNS44MjIzNyA5LjUxNDY1QzYuMDA1NDcgOS4zMzE1NSA2LjMwMjI3IDkuMzMxNTUgNi40ODUzOCA5LjUxNDY1QzYuNjY4NDggOS42OTc3NiA2LjY2ODQ4IDkuOTk0NTUgNi40ODUzOCAxMC4xNzc3TDEuNjAyNTcgMTUuMDYxNEw1LjQyMjE4IDE1LjA1NTlMNS41MTY1MSAxNS4wNjVDNS43MzAyOSAxNS4xMDg0IDUuODkxNjggMTUuMjk4MSA1Ljg5MTk3IDE1LjUyNDdDNS44OTIwOCAxNS43ODM1IDUuNjgxOTIgMTUuOTkzMyA1LjQyMzEgMTUuOTkzNkwwLjQ2OTc4MSAxNkwwLjM3NzI5IDE1Ljk5MDhaIiBmaWxsPSJjdXJyZW50Q29sb3IiIC8+PC9zdmc+" /></span></span>
</figure>

</div>

</div>

Is this exploitable? No. The `apiKeys` object doesn’t live long enough, it’s immediately freed after serializing it, and `JSON.stringify` knows to skip the `__proto__` field. We’re also only overwriting the prototype of `apiKeys`, not mutating a global prototype. However, refactors to the code could introduce new code paths that turn this un-exploitable vulnerability in one that could have wider impact. The testing power offered by property-based testing catches this now, helping prevent subtle incorrectness and sharp edge cases from growing in your code base.

<div class="heading-anchor-wrapper">

### How did Kiro test this?

<a href="#how-did-kiro-test-this" class="anchor-link" aria-label="Copy link to How did kiro test this section"><span class="anchor-icon-wrapper"><img src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iYW5jaG9yLWljb24iIHZpZXdib3g9IjAgMCAxNiAxNyIgd2lkdGg9IjE2IiBoZWlnaHQ9IjE3IiBmaWxsPSJjdXJyZW50Q29sb3IiPjxwYXRoIGQ9Ik0yLjI3MTQzIDE0LjIyOEMwLjU5MTg5NyAxMi41NDg1IDAuNTkxODk3IDkuODI1MzkgMi4yNzE0MyA4LjE0NTg1TDMuNDIzMjQgNi45OTQwNEwzLjQ0MTg4IDYuOTc2MzVDMy42MzgxNiA2Ljc5OSAzLjk0MTE4IDYuODA0ODggNC4xMzAzNSA2Ljk5NDA0QzQuMzE5NTEgNy4xODMyMSA0LjMyNTM5IDcuNDg2MjMgNC4xNDgwNCA3LjY4MjVMNC4xMzAzNSA3LjcwMTE1TDIuOTc4NTQgOC44NTI5NkMxLjY4OTUzIDEwLjE0MiAxLjY4OTUzIDEyLjIzMTkgMi45Nzg1NCAxMy41MjA5TDMuMDA4ODggMTMuNTUwOUM0LjMwMDE0IDE0LjgwOTggNi4zNjc1MSAxNC43OTk4IDcuNjQ2NDYgMTMuNTIwOUw4Ljc5ODI3IDEyLjM2OTFMOC44MTY5MSAxMi4zNTE0QzkuMDEzMTkgMTIuMTc0IDkuMzE2MjEgMTIuMTc5OSA5LjUwNTM4IDEyLjM2OTFDOS42OTQ1NCAxMi41NTgyIDkuNzAwNDYgMTIuODYxMyA5LjUyMzExIDEzLjA1NzZMOS41MDUzOCAxMy4wNzYyTDguMzUzNTYgMTQuMjI4QzYuNjg3MTUgMTUuODk0NCAzLjk5MzQ3IDE1LjkwNzQgMi4zMTEgMTQuMjY3TDIuMjcxNDMgMTQuMjI4Wk0xMy4wMjE1IDMuNDc3OTNDMTEuNzQyNSAyLjE5ODk5IDkuNjc1MTcgMi4xODg5NiA4LjM4MzkgMy40NDc5NEw4LjM1MzU2IDMuNDc3OTNMNy4yMjU3OSA0LjYwNTdDNy4wMzA1MyA0LjgwMDk2IDYuNzEzOTUgNC44MDA5NiA2LjUxODY5IDQuNjA1N0M2LjMyMzQyIDQuNDEwNDQgNi4zMjM0MiA0LjA5Mzg2IDYuNTE4NjkgMy44OTg1OUw3LjY0NjQ2IDIuNzcwODJMNy42ODYwMyAyLjczMTc3QzkuMzY4NSAxLjA5MTM4IDEyLjA2MjIgMS4xMDQ0MSAxMy43Mjg2IDIuNzcwODJMMTMuNzY3NyAyLjgxMDM2QzE1LjM5NTIgNC40Nzk1OCAxNS4zOTUxIDcuMTQ0MTcgMTMuNzY3NyA4LjgxMzM4TDEzLjcyODYgOC44NTI5NkwxMi42MDA4IDkuOTgwNzNDMTIuNDA1NiAxMC4xNzYgMTIuMDg5IDEwLjE3NiAxMS44OTM3IDkuOTgwNzNDMTEuNjk4NSA5Ljc4NTQ3IDExLjY5ODUgOS40Njg4OCAxMS44OTM3IDkuMjczNjJMMTMuMDIxNSA4LjE0NTg1TDEzLjA1MTUgOC4xMTU1MUMxNC4zMDA1IDYuODM0NDIgMTQuMzAwNSA0Ljc4OTM3IDEzLjA1MTUgMy41MDgyN0wxMy4wMjE1IDMuNDc3OTNaIiAvPjxwYXRoIGQ9Ik0xMC4wMjE5IDUuODY2MzJMMTAuMDQwNiA1Ljg0ODU4QzEwLjIzNjkgNS42NzEyNCAxMC41Mzk5IDUuNjc3MTYgMTAuNzI5IDUuODY2MzJDMTAuOTE4MiA2LjA1NTQ4IDEwLjkyNDEgNi4zNTg0NiAxMC43NDY4IDYuNTU0NzRMMTAuNzI5IDYuNTczNDJMNi4xNDU4OCAxMS4xNTY2QzUuOTUwNjIgMTEuMzUxOCA1LjYzNDAzIDExLjM1MTggNS40Mzg3NyAxMS4xNTY2QzUuMjQzNTEgMTAuOTYxMyA1LjI0MzUxIDEwLjY0NDcgNS40Mzg3NyAxMC40NDk1TDEwLjAyMTkgNS44NjYzMloiIC8+PC9zdmc+" class="anchor-icon" /><span class="copied-indicator docsearch-exclude" aria-live="polite" aria-atomic="true"></span></span></a>

</div>

When we tried to save an API key with provider name `__proto__`, then load it back, we got an empty object `{}` instead of the API key we saved. Why did this happen? Let’s understand a bit more background on what happened under the covers.

One of the advantages of PBTs we often talk about is bias. With unit tests, whoever wrote the tests (model or human) tried to account for edge cases, but they are limited by their own internal biases. Since the same (model/person) wrote the implementation, it stands to reason they are going to have a hard time coming up with edge cases they didn’t think about during the implementation. In this case, using property-based tests allows us to access the collective wisdom of those who have contributed to the testing framework. In this case we are injecting institutional knowledge of common bug types to the process. (`__proto__` is one of the common bug strings encoded into the PBT generator by the fast-check community authors) into your testing process.

Before moving on, one thing to note is the PBT code had `{ numRuns: 100 }` which means that there were 100 iterations by the generator to try and find a bug. Kiro defaults to this but you can raise or lower this value depending on what level of confidence you’re looking for in your program. Sometimes you want more, but it also might be the case that an implementation takes a bit of time to test and therefore the performance of running 100 or more input tests isn’t valuable yet in that phase of your development lifecycle. The good thing is you can always raise or lower this as necessary.

<div class="heading-anchor-wrapper">

### The fix

<a href="#the-fix" class="anchor-link" aria-label="Copy link to The fix section"><span class="anchor-icon-wrapper"><img src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iYW5jaG9yLWljb24iIHZpZXdib3g9IjAgMCAxNiAxNyIgd2lkdGg9IjE2IiBoZWlnaHQ9IjE3IiBmaWxsPSJjdXJyZW50Q29sb3IiPjxwYXRoIGQ9Ik0yLjI3MTQzIDE0LjIyOEMwLjU5MTg5NyAxMi41NDg1IDAuNTkxODk3IDkuODI1MzkgMi4yNzE0MyA4LjE0NTg1TDMuNDIzMjQgNi45OTQwNEwzLjQ0MTg4IDYuOTc2MzVDMy42MzgxNiA2Ljc5OSAzLjk0MTE4IDYuODA0ODggNC4xMzAzNSA2Ljk5NDA0QzQuMzE5NTEgNy4xODMyMSA0LjMyNTM5IDcuNDg2MjMgNC4xNDgwNCA3LjY4MjVMNC4xMzAzNSA3LjcwMTE1TDIuOTc4NTQgOC44NTI5NkMxLjY4OTUzIDEwLjE0MiAxLjY4OTUzIDEyLjIzMTkgMi45Nzg1NCAxMy41MjA5TDMuMDA4ODggMTMuNTUwOUM0LjMwMDE0IDE0LjgwOTggNi4zNjc1MSAxNC43OTk4IDcuNjQ2NDYgMTMuNTIwOUw4Ljc5ODI3IDEyLjM2OTFMOC44MTY5MSAxMi4zNTE0QzkuMDEzMTkgMTIuMTc0IDkuMzE2MjEgMTIuMTc5OSA5LjUwNTM4IDEyLjM2OTFDOS42OTQ1NCAxMi41NTgyIDkuNzAwNDYgMTIuODYxMyA5LjUyMzExIDEzLjA1NzZMOS41MDUzOCAxMy4wNzYyTDguMzUzNTYgMTQuMjI4QzYuNjg3MTUgMTUuODk0NCAzLjk5MzQ3IDE1LjkwNzQgMi4zMTEgMTQuMjY3TDIuMjcxNDMgMTQuMjI4Wk0xMy4wMjE1IDMuNDc3OTNDMTEuNzQyNSAyLjE5ODk5IDkuNjc1MTcgMi4xODg5NiA4LjM4MzkgMy40NDc5NEw4LjM1MzU2IDMuNDc3OTNMNy4yMjU3OSA0LjYwNTdDNy4wMzA1MyA0LjgwMDk2IDYuNzEzOTUgNC44MDA5NiA2LjUxODY5IDQuNjA1N0M2LjMyMzQyIDQuNDEwNDQgNi4zMjM0MiA0LjA5Mzg2IDYuNTE4NjkgMy44OTg1OUw3LjY0NjQ2IDIuNzcwODJMNy42ODYwMyAyLjczMTc3QzkuMzY4NSAxLjA5MTM4IDEyLjA2MjIgMS4xMDQ0MSAxMy43Mjg2IDIuNzcwODJMMTMuNzY3NyAyLjgxMDM2QzE1LjM5NTIgNC40Nzk1OCAxNS4zOTUxIDcuMTQ0MTcgMTMuNzY3NyA4LjgxMzM4TDEzLjcyODYgOC44NTI5NkwxMi42MDA4IDkuOTgwNzNDMTIuNDA1NiAxMC4xNzYgMTIuMDg5IDEwLjE3NiAxMS44OTM3IDkuOTgwNzNDMTEuNjk4NSA5Ljc4NTQ3IDExLjY5ODUgOS40Njg4OCAxMS44OTM3IDkuMjczNjJMMTMuMDIxNSA4LjE0NTg1TDEzLjA1MTUgOC4xMTU1MUMxNC4zMDA1IDYuODM0NDIgMTQuMzAwNSA0Ljc4OTM3IDEzLjA1MTUgMy41MDgyN0wxMy4wMjE1IDMuNDc3OTNaIiAvPjxwYXRoIGQ9Ik0xMC4wMjE5IDUuODY2MzJMMTAuMDQwNiA1Ljg0ODU4QzEwLjIzNjkgNS42NzEyNCAxMC41Mzk5IDUuNjc3MTYgMTAuNzI5IDUuODY2MzJDMTAuOTE4MiA2LjA1NTQ4IDEwLjkyNDEgNi4zNTg0NiAxMC43NDY4IDYuNTU0NzRMMTAuNzI5IDYuNTczNDJMNi4xNDU4OCAxMS4xNTY2QzUuOTUwNjIgMTEuMzUxOCA1LjYzNDAzIDExLjM1MTggNS40Mzg3NyAxMS4xNTY2QzUuMjQzNTEgMTAuOTYxMyA1LjI0MzUxIDEwLjY0NDcgNS40Mzg3NyAxMC40NDk1TDEwLjAyMTkgNS44NjYzMloiIC8+PC9zdmc+" class="anchor-icon" /><span class="copied-indicator docsearch-exclude" aria-live="polite" aria-atomic="true"></span></span></a>

</div>

Kiro implemented two defensive measures based on <a href="https://cwe.mitre.org/data/definitions/1321.html" class="text-primary hover:underline" target="_blank" rel="noopener noreferrer">MITRE's highly effective mitigation strategies</a>:

1.  Safe Storage (in `saveApiKey`):

<div class="my-6 rounded-md bg-muted-foreground/10 p-4">

Loading code example...

</div>

Objects created with `Object.create(null)` have no prototype chain, so `__proto__` becomes just a regular property.

2.  Safe Retrieval (in loadApiKey):

<div class="my-6 rounded-md bg-muted-foreground/10 p-4">

Loading code example...

</div>

<div class="heading-anchor-wrapper">

## The Bigger Picture

<a href="#the-bigger-picture" class="anchor-link" aria-label="Copy link to The bigger picture section"><span class="anchor-icon-wrapper"><img src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iYW5jaG9yLWljb24iIHZpZXdib3g9IjAgMCAxNiAxNyIgd2lkdGg9IjE2IiBoZWlnaHQ9IjE3IiBmaWxsPSJjdXJyZW50Q29sb3IiPjxwYXRoIGQ9Ik0yLjI3MTQzIDE0LjIyOEMwLjU5MTg5NyAxMi41NDg1IDAuNTkxODk3IDkuODI1MzkgMi4yNzE0MyA4LjE0NTg1TDMuNDIzMjQgNi45OTQwNEwzLjQ0MTg4IDYuOTc2MzVDMy42MzgxNiA2Ljc5OSAzLjk0MTE4IDYuODA0ODggNC4xMzAzNSA2Ljk5NDA0QzQuMzE5NTEgNy4xODMyMSA0LjMyNTM5IDcuNDg2MjMgNC4xNDgwNCA3LjY4MjVMNC4xMzAzNSA3LjcwMTE1TDIuOTc4NTQgOC44NTI5NkMxLjY4OTUzIDEwLjE0MiAxLjY4OTUzIDEyLjIzMTkgMi45Nzg1NCAxMy41MjA5TDMuMDA4ODggMTMuNTUwOUM0LjMwMDE0IDE0LjgwOTggNi4zNjc1MSAxNC43OTk4IDcuNjQ2NDYgMTMuNTIwOUw4Ljc5ODI3IDEyLjM2OTFMOC44MTY5MSAxMi4zNTE0QzkuMDEzMTkgMTIuMTc0IDkuMzE2MjEgMTIuMTc5OSA5LjUwNTM4IDEyLjM2OTFDOS42OTQ1NCAxMi41NTgyIDkuNzAwNDYgMTIuODYxMyA5LjUyMzExIDEzLjA1NzZMOS41MDUzOCAxMy4wNzYyTDguMzUzNTYgMTQuMjI4QzYuNjg3MTUgMTUuODk0NCAzLjk5MzQ3IDE1LjkwNzQgMi4zMTEgMTQuMjY3TDIuMjcxNDMgMTQuMjI4Wk0xMy4wMjE1IDMuNDc3OTNDMTEuNzQyNSAyLjE5ODk5IDkuNjc1MTcgMi4xODg5NiA4LjM4MzkgMy40NDc5NEw4LjM1MzU2IDMuNDc3OTNMNy4yMjU3OSA0LjYwNTdDNy4wMzA1MyA0LjgwMDk2IDYuNzEzOTUgNC44MDA5NiA2LjUxODY5IDQuNjA1N0M2LjMyMzQyIDQuNDEwNDQgNi4zMjM0MiA0LjA5Mzg2IDYuNTE4NjkgMy44OTg1OUw3LjY0NjQ2IDIuNzcwODJMNy42ODYwMyAyLjczMTc3QzkuMzY4NSAxLjA5MTM4IDEyLjA2MjIgMS4xMDQ0MSAxMy43Mjg2IDIuNzcwODJMMTMuNzY3NyAyLjgxMDM2QzE1LjM5NTIgNC40Nzk1OCAxNS4zOTUxIDcuMTQ0MTcgMTMuNzY3NyA4LjgxMzM4TDEzLjcyODYgOC44NTI5NkwxMi42MDA4IDkuOTgwNzNDMTIuNDA1NiAxMC4xNzYgMTIuMDg5IDEwLjE3NiAxMS44OTM3IDkuOTgwNzNDMTEuNjk4NSA5Ljc4NTQ3IDExLjY5ODUgOS40Njg4OCAxMS44OTM3IDkuMjczNjJMMTMuMDIxNSA4LjE0NTg1TDEzLjA1MTUgOC4xMTU1MUMxNC4zMDA1IDYuODM0NDIgMTQuMzAwNSA0Ljc4OTM3IDEzLjA1MTUgMy41MDgyN0wxMy4wMjE1IDMuNDc3OTNaIiAvPjxwYXRoIGQ9Ik0xMC4wMjE5IDUuODY2MzJMMTAuMDQwNiA1Ljg0ODU4QzEwLjIzNjkgNS42NzEyNCAxMC41Mzk5IDUuNjc3MTYgMTAuNzI5IDUuODY2MzJDMTAuOTE4MiA2LjA1NTQ4IDEwLjkyNDEgNi4zNTg0NiAxMC43NDY4IDYuNTU0NzRMMTAuNzI5IDYuNTczNDJMNi4xNDU4OCAxMS4xNTY2QzUuOTUwNjIgMTEuMzUxOCA1LjYzNDAzIDExLjM1MTggNS40Mzg3NyAxMS4xNTY2QzUuMjQzNTEgMTAuOTYxMyA1LjI0MzUxIDEwLjY0NDcgNS40Mzg3NyAxMC40NDk1TDEwLjAyMTkgNS44NjYzMloiIC8+PC9zdmc+" class="anchor-icon" /><span class="copied-indicator docsearch-exclude" aria-live="polite" aria-atomic="true"></span></span></a>

</div>

This story illustrates why Kiro uses property-based testing as part of SDD:

1.  **Properties connect directly to requirements** - The property "for any provider name, round-trip should work" is a direct translation of the requirement. When the property passes, we have evidence the requirement is satisfied.
2.  **Random generation finds unexpected edge cases** - Humans and LLMs have biases about what inputs to test. Random generation explores the space more thoroughly.
3.  **Executable specifications** - Properties are specifications you can run. They bridge the gap between "what should the code do" (requirements) and "does the code actually do it" (tests).
4.  **Tight feedback loops** - When a property fails, you get a minimal counterexample that makes debugging easier. Kiro can use this to fix the code, creating a rapid iteration cycle.

This bug was found during real development with Kiro. The property-based test caught a security weakness that would have been very difficult to find through:

- Manual code review
- Traditional unit tests with hand-picked examples
- Integration testing

</div>

<div class="mt-12">

<div class="flex w-full items-stretch justify-between gap-3 self-stretch md:gap-4">

<div class="flex flex-1 sm:w-80">

<a href="/blog/multi-root-workspaces/" class="group/nav flex w-full flex-col justify-start gap-3 self-stretch rounded-2xl bg-prey-900 px-4 py-3 transition-colors md:gap-4 md:px-6 md:py-4"></a>

<div class="flex items-center gap-1">

<span class="font-display text-[18px] leading-[16px] text-purple-500" aria-hidden="true">{</span><span class="leading-[16px] mt-[1px] uppercase text-secondary"><span class="text-utility-sm">PREVIOUS</span></span><span class="font-display text-[18px] leading-[16px] text-purple-500" aria-hidden="true">}</span>

</div>

### Multi-root workspaces in Kiro: work across projects, not just inside one

</div>

<div class="flex flex-1 sm:w-80">

<a href="/blog/empowering-kiro-with-ide-diagnostics/" class="group/nav flex w-full flex-col justify-start gap-3 self-stretch rounded-2xl bg-prey-900 px-4 py-3 transition-colors md:gap-4 md:px-6 md:py-4"></a>

<div class="flex w-full justify-end">

<div class="flex items-center gap-1">

<span class="font-display text-[18px] leading-[16px] text-purple-500" aria-hidden="true">{</span><span class="leading-[16px] mt-[1px] uppercase text-secondary"><span class="text-utility-sm">NEXT</span></span><span class="font-display text-[18px] leading-[16px] text-purple-500" aria-hidden="true">}</span>

</div>

</div>

### Empowering Kiro with IDE diagnostics

</div>

</div>

</div>

</div>

</div>

</div>

</div>

</div>

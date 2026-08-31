# Source: https://kiro.dev/blog/bug-fix-paradox/

**URL:** https://kiro.dev/blog/bug-fix-paradox/
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

February 19, 2026

</div>

# The bug fix paradox: why AI agents keep breaking working code

<div class="flex items-center gap-2">

<span class="text-sm text-muted-foreground">By</span>

<div class="flex flex-wrap items-center gap-4">

<a href="https://scholar.google.com/citations?user=ot53EycAAAAJ&amp;hl=en" class="flex cursor-pointer items-center gap-2 transition-opacity hover:opacity-80"><span class="relative flex shrink-0 overflow-hidden rounded-full h-8 w-8"><span class="flex h-full w-full items-center justify-center rounded-full bg-muted">JA</span></span></a>

<div>

Jatin Arora

Applied Science

</div>

</div>

</div>

</div>

<div class="blog-content changelog prose-prey prose max-w-none dark:prose-invert prose-code:before:content-none prose-code:after:content-none">

<div class="heading-anchor-wrapper">

## The sledgehammer problem

<a href="#the-sledgehammer-problem" class="anchor-link" aria-label="Copy link to The sledgehammer problem section"><span class="anchor-icon-wrapper"><img src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iYW5jaG9yLWljb24iIHZpZXdib3g9IjAgMCAxNiAxNyIgd2lkdGg9IjE2IiBoZWlnaHQ9IjE3IiBmaWxsPSJjdXJyZW50Q29sb3IiPjxwYXRoIGQ9Ik0yLjI3MTQzIDE0LjIyOEMwLjU5MTg5NyAxMi41NDg1IDAuNTkxODk3IDkuODI1MzkgMi4yNzE0MyA4LjE0NTg1TDMuNDIzMjQgNi45OTQwNEwzLjQ0MTg4IDYuOTc2MzVDMy42MzgxNiA2Ljc5OSAzLjk0MTE4IDYuODA0ODggNC4xMzAzNSA2Ljk5NDA0QzQuMzE5NTEgNy4xODMyMSA0LjMyNTM5IDcuNDg2MjMgNC4xNDgwNCA3LjY4MjVMNC4xMzAzNSA3LjcwMTE1TDIuOTc4NTQgOC44NTI5NkMxLjY4OTUzIDEwLjE0MiAxLjY4OTUzIDEyLjIzMTkgMi45Nzg1NCAxMy41MjA5TDMuMDA4ODggMTMuNTUwOUM0LjMwMDE0IDE0LjgwOTggNi4zNjc1MSAxNC43OTk4IDcuNjQ2NDYgMTMuNTIwOUw4Ljc5ODI3IDEyLjM2OTFMOC44MTY5MSAxMi4zNTE0QzkuMDEzMTkgMTIuMTc0IDkuMzE2MjEgMTIuMTc5OSA5LjUwNTM4IDEyLjM2OTFDOS42OTQ1NCAxMi41NTgyIDkuNzAwNDYgMTIuODYxMyA5LjUyMzExIDEzLjA1NzZMOS41MDUzOCAxMy4wNzYyTDguMzUzNTYgMTQuMjI4QzYuNjg3MTUgMTUuODk0NCAzLjk5MzQ3IDE1LjkwNzQgMi4zMTEgMTQuMjY3TDIuMjcxNDMgMTQuMjI4Wk0xMy4wMjE1IDMuNDc3OTNDMTEuNzQyNSAyLjE5ODk5IDkuNjc1MTcgMi4xODg5NiA4LjM4MzkgMy40NDc5NEw4LjM1MzU2IDMuNDc3OTNMNy4yMjU3OSA0LjYwNTdDNy4wMzA1MyA0LjgwMDk2IDYuNzEzOTUgNC44MDA5NiA2LjUxODY5IDQuNjA1N0M2LjMyMzQyIDQuNDEwNDQgNi4zMjM0MiA0LjA5Mzg2IDYuNTE4NjkgMy44OTg1OUw3LjY0NjQ2IDIuNzcwODJMNy42ODYwMyAyLjczMTc3QzkuMzY4NSAxLjA5MTM4IDEyLjA2MjIgMS4xMDQ0MSAxMy43Mjg2IDIuNzcwODJMMTMuNzY3NyAyLjgxMDM2QzE1LjM5NTIgNC40Nzk1OCAxNS4zOTUxIDcuMTQ0MTcgMTMuNzY3NyA4LjgxMzM4TDEzLjcyODYgOC44NTI5NkwxMi42MDA4IDkuOTgwNzNDMTIuNDA1NiAxMC4xNzYgMTIuMDg5IDEwLjE3NiAxMS44OTM3IDkuOTgwNzNDMTEuNjk4NSA5Ljc4NTQ3IDExLjY5ODUgOS40Njg4OCAxMS44OTM3IDkuMjczNjJMMTMuMDIxNSA4LjE0NTg1TDEzLjA1MTUgOC4xMTU1MUMxNC4zMDA1IDYuODM0NDIgMTQuMzAwNSA0Ljc4OTM3IDEzLjA1MTUgMy41MDgyN0wxMy4wMjE1IDMuNDc3OTNaIiAvPjxwYXRoIGQ9Ik0xMC4wMjE5IDUuODY2MzJMMTAuMDQwNiA1Ljg0ODU4QzEwLjIzNjkgNS42NzEyNCAxMC41Mzk5IDUuNjc3MTYgMTAuNzI5IDUuODY2MzJDMTAuOTE4MiA2LjA1NTQ4IDEwLjkyNDEgNi4zNTg0NiAxMC43NDY4IDYuNTU0NzRMMTAuNzI5IDYuNTczNDJMNi4xNDU4OCAxMS4xNTY2QzUuOTUwNjIgMTEuMzUxOCA1LjYzNDAzIDExLjM1MTggNS40Mzg3NyAxMS4xNTY2QzUuMjQzNTEgMTAuOTYxMyA1LjI0MzUxIDEwLjY0NDcgNS40Mzg3NyAxMC40NDk1TDEwLjAyMTkgNS44NjYzMloiIC8+PC9zdmc+" class="anchor-icon" /><span class="copied-indicator docsearch-exclude" aria-live="polite" aria-atomic="true"></span></span></a>

</div>

Here’s a pattern most teams run into: you ask an AI agent to fix a bug. It refactors three helper functions, adds defensive null checks, and writes dozens of new tests for edge cases that were already passing. Even worse, it changes parts of the application that were working just fine. You wanted a scalpel but got a sledgehammer.

Agents are <a href="https://stackoverflow.blog/2026/01/28/are-bugs-and-incidents-inevitable-with-ai-coding-agents/" class="text-primary hover:underline" target="_blank" rel="noopener noreferrer">nearly twice as likely as humans</a> to add guard clauses and defensive error handling. Where we'd ask “why is this null?”, the agent adds `if (x == null)` and moves on. Iteration makes it worse: without proper constraints, <a href="https://arxiv.org/pdf/2510.07777" class="text-primary hover:underline" target="_blank" rel="noopener noreferrer">the more you talk to an agent, the more it drifts from the original intent.</a> The actual fix, if discovered, is buried under changes that weren’t necessary.

The problem is that you and the agent aren’t working with the same boundary between what to fix and what to leave alone. We built Kiro’s bug-fixing workflow to make that boundary explicit. It’s based on an approach we call *property-aware code evolution.*

<div class="heading-anchor-wrapper">

## Property-aware code evolution

<a href="#property-aware-code-evolution" class="anchor-link" aria-label="Copy link to Property aware code evolution section"><span class="anchor-icon-wrapper"><img src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iYW5jaG9yLWljb24iIHZpZXdib3g9IjAgMCAxNiAxNyIgd2lkdGg9IjE2IiBoZWlnaHQ9IjE3IiBmaWxsPSJjdXJyZW50Q29sb3IiPjxwYXRoIGQ9Ik0yLjI3MTQzIDE0LjIyOEMwLjU5MTg5NyAxMi41NDg1IDAuNTkxODk3IDkuODI1MzkgMi4yNzE0MyA4LjE0NTg1TDMuNDIzMjQgNi45OTQwNEwzLjQ0MTg4IDYuOTc2MzVDMy42MzgxNiA2Ljc5OSAzLjk0MTE4IDYuODA0ODggNC4xMzAzNSA2Ljk5NDA0QzQuMzE5NTEgNy4xODMyMSA0LjMyNTM5IDcuNDg2MjMgNC4xNDgwNCA3LjY4MjVMNC4xMzAzNSA3LjcwMTE1TDIuOTc4NTQgOC44NTI5NkMxLjY4OTUzIDEwLjE0MiAxLjY4OTUzIDEyLjIzMTkgMi45Nzg1NCAxMy41MjA5TDMuMDA4ODggMTMuNTUwOUM0LjMwMDE0IDE0LjgwOTggNi4zNjc1MSAxNC43OTk4IDcuNjQ2NDYgMTMuNTIwOUw4Ljc5ODI3IDEyLjM2OTFMOC44MTY5MSAxMi4zNTE0QzkuMDEzMTkgMTIuMTc0IDkuMzE2MjEgMTIuMTc5OSA5LjUwNTM4IDEyLjM2OTFDOS42OTQ1NCAxMi41NTgyIDkuNzAwNDYgMTIuODYxMyA5LjUyMzExIDEzLjA1NzZMOS41MDUzOCAxMy4wNzYyTDguMzUzNTYgMTQuMjI4QzYuNjg3MTUgMTUuODk0NCAzLjk5MzQ3IDE1LjkwNzQgMi4zMTEgMTQuMjY3TDIuMjcxNDMgMTQuMjI4Wk0xMy4wMjE1IDMuNDc3OTNDMTEuNzQyNSAyLjE5ODk5IDkuNjc1MTcgMi4xODg5NiA4LjM4MzkgMy40NDc5NEw4LjM1MzU2IDMuNDc3OTNMNy4yMjU3OSA0LjYwNTdDNy4wMzA1MyA0LjgwMDk2IDYuNzEzOTUgNC44MDA5NiA2LjUxODY5IDQuNjA1N0M2LjMyMzQyIDQuNDEwNDQgNi4zMjM0MiA0LjA5Mzg2IDYuNTE4NjkgMy44OTg1OUw3LjY0NjQ2IDIuNzcwODJMNy42ODYwMyAyLjczMTc3QzkuMzY4NSAxLjA5MTM4IDEyLjA2MjIgMS4xMDQ0MSAxMy43Mjg2IDIuNzcwODJMMTMuNzY3NyAyLjgxMDM2QzE1LjM5NTIgNC40Nzk1OCAxNS4zOTUxIDcuMTQ0MTcgMTMuNzY3NyA4LjgxMzM4TDEzLjcyODYgOC44NTI5NkwxMi42MDA4IDkuOTgwNzNDMTIuNDA1NiAxMC4xNzYgMTIuMDg5IDEwLjE3NiAxMS44OTM3IDkuOTgwNzNDMTEuNjk4NSA5Ljc4NTQ3IDExLjY5ODUgOS40Njg4OCAxMS44OTM3IDkuMjczNjJMMTMuMDIxNSA4LjE0NTg1TDEzLjA1MTUgOC4xMTU1MUMxNC4zMDA1IDYuODM0NDIgMTQuMzAwNSA0Ljc4OTM3IDEzLjA1MTUgMy41MDgyN0wxMy4wMjE1IDMuNDc3OTNaIiAvPjxwYXRoIGQ9Ik0xMC4wMjE5IDUuODY2MzJMMTAuMDQwNiA1Ljg0ODU4QzEwLjIzNjkgNS42NzEyNCAxMC41Mzk5IDUuNjc3MTYgMTAuNzI5IDUuODY2MzJDMTAuOTE4MiA2LjA1NTQ4IDEwLjkyNDEgNi4zNTg0NiAxMC43NDY4IDYuNTU0NzRMMTAuNzI5IDYuNTczNDJMNi4xNDU4OCAxMS4xNTY2QzUuOTUwNjIgMTEuMzUxOCA1LjYzNDAzIDExLjM1MTggNS40Mzg3NyAxMS4xNTY2QzUuMjQzNTEgMTAuOTYxMyA1LjI0MzUxIDEwLjY0NDcgNS40Mzg3NyAxMC40NDk1TDEwLjAyMTkgNS44NjYzMloiIC8+PC9zdmc+" class="anchor-icon" /><span class="copied-indicator docsearch-exclude" aria-live="polite" aria-atomic="true"></span></span></a>

</div>

Every bug fix has a dual intent: fix the buggy behavior, preserve everything else. That intent partitions the input space, but the partition usually stays implicit. We can make it explicit and testable.

<div class="heading-anchor-wrapper">

### Bug condition

<a href="#bug-condition" class="anchor-link" aria-label="Copy link to Bug condition section"><span class="anchor-icon-wrapper"><img src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iYW5jaG9yLWljb24iIHZpZXdib3g9IjAgMCAxNiAxNyIgd2lkdGg9IjE2IiBoZWlnaHQ9IjE3IiBmaWxsPSJjdXJyZW50Q29sb3IiPjxwYXRoIGQ9Ik0yLjI3MTQzIDE0LjIyOEMwLjU5MTg5NyAxMi41NDg1IDAuNTkxODk3IDkuODI1MzkgMi4yNzE0MyA4LjE0NTg1TDMuNDIzMjQgNi45OTQwNEwzLjQ0MTg4IDYuOTc2MzVDMy42MzgxNiA2Ljc5OSAzLjk0MTE4IDYuODA0ODggNC4xMzAzNSA2Ljk5NDA0QzQuMzE5NTEgNy4xODMyMSA0LjMyNTM5IDcuNDg2MjMgNC4xNDgwNCA3LjY4MjVMNC4xMzAzNSA3LjcwMTE1TDIuOTc4NTQgOC44NTI5NkMxLjY4OTUzIDEwLjE0MiAxLjY4OTUzIDEyLjIzMTkgMi45Nzg1NCAxMy41MjA5TDMuMDA4ODggMTMuNTUwOUM0LjMwMDE0IDE0LjgwOTggNi4zNjc1MSAxNC43OTk4IDcuNjQ2NDYgMTMuNTIwOUw4Ljc5ODI3IDEyLjM2OTFMOC44MTY5MSAxMi4zNTE0QzkuMDEzMTkgMTIuMTc0IDkuMzE2MjEgMTIuMTc5OSA5LjUwNTM4IDEyLjM2OTFDOS42OTQ1NCAxMi41NTgyIDkuNzAwNDYgMTIuODYxMyA5LjUyMzExIDEzLjA1NzZMOS41MDUzOCAxMy4wNzYyTDguMzUzNTYgMTQuMjI4QzYuNjg3MTUgMTUuODk0NCAzLjk5MzQ3IDE1LjkwNzQgMi4zMTEgMTQuMjY3TDIuMjcxNDMgMTQuMjI4Wk0xMy4wMjE1IDMuNDc3OTNDMTEuNzQyNSAyLjE5ODk5IDkuNjc1MTcgMi4xODg5NiA4LjM4MzkgMy40NDc5NEw4LjM1MzU2IDMuNDc3OTNMNy4yMjU3OSA0LjYwNTdDNy4wMzA1MyA0LjgwMDk2IDYuNzEzOTUgNC44MDA5NiA2LjUxODY5IDQuNjA1N0M2LjMyMzQyIDQuNDEwNDQgNi4zMjM0MiA0LjA5Mzg2IDYuNTE4NjkgMy44OTg1OUw3LjY0NjQ2IDIuNzcwODJMNy42ODYwMyAyLjczMTc3QzkuMzY4NSAxLjA5MTM4IDEyLjA2MjIgMS4xMDQ0MSAxMy43Mjg2IDIuNzcwODJMMTMuNzY3NyAyLjgxMDM2QzE1LjM5NTIgNC40Nzk1OCAxNS4zOTUxIDcuMTQ0MTcgMTMuNzY3NyA4LjgxMzM4TDEzLjcyODYgOC44NTI5NkwxMi42MDA4IDkuOTgwNzNDMTIuNDA1NiAxMC4xNzYgMTIuMDg5IDEwLjE3NiAxMS44OTM3IDkuOTgwNzNDMTEuNjk4NSA5Ljc4NTQ3IDExLjY5ODUgOS40Njg4OCAxMS44OTM3IDkuMjczNjJMMTMuMDIxNSA4LjE0NTg1TDEzLjA1MTUgOC4xMTU1MUMxNC4zMDA1IDYuODM0NDIgMTQuMzAwNSA0Ljc4OTM3IDEzLjA1MTUgMy41MDgyN0wxMy4wMjE1IDMuNDc3OTNaIiAvPjxwYXRoIGQ9Ik0xMC4wMjE5IDUuODY2MzJMMTAuMDQwNiA1Ljg0ODU4QzEwLjIzNjkgNS42NzEyNCAxMC41Mzk5IDUuNjc3MTYgMTAuNzI5IDUuODY2MzJDMTAuOTE4MiA2LjA1NTQ4IDEwLjkyNDEgNi4zNTg0NiAxMC43NDY4IDYuNTU0NzRMMTAuNzI5IDYuNTczNDJMNi4xNDU4OCAxMS4xNTY2QzUuOTUwNjIgMTEuMzUxOCA1LjYzNDAzIDExLjM1MTggNS40Mzg3NyAxMS4xNTY2QzUuMjQzNTEgMTAuOTYxMyA1LjI0MzUxIDEwLjY0NDcgNS40Mzg3NyAxMC40NDk1TDEwLjAyMTkgNS44NjYzMloiIC8+PC9zdmc+" class="anchor-icon" /><span class="copied-indicator docsearch-exclude" aria-live="polite" aria-atomic="true"></span></span></a>

</div>

The ***bug condition*** C identifies when the bug triggers. It partitions the input space in two:

- **Scenarios satisfying C** → where the bug manifests. You want change to happen here.
- **Scenarios not satisfying C** → where behavior is correct. You want preservation here.

<div>

<div class="my-8">

<figure class="overflow-hidden rounded-2xl border border-[#4a464f] bg-muted/30">
<span class="group relative inline-block transition-all duration-200 cursor-zoom-in" style="display:block" tabindex="0" role="button" aria-label="Open image lightbox: Diagram showing input space partitioned by bug condition C into buggy scenarios and working scenarios"><span class="relative overflow-hidden h-auto w-full border-0"><span class="absolute inset-0 flex animate-pulse items-center justify-center bg-muted"><span class="sr-only">Loading image...</span></span><img src="/images/blogs/bug-fix-paradox/input.png?h=d41765f9" class="transition-opacity duration-300 opacity-0" style="color:transparent" loading="lazy" decoding="async" data-nimg="1" width="1200" height="600" alt="Diagram showing input space partitioned by bug condition C into buggy scenarios and working scenarios" /></span><span class="absolute bottom-2 right-2 z-10 flex items-center justify-center rounded-full bg-prey-600/60 p-2.5 transition-opacity duration-200 opacity-100 group-hover:opacity-100" aria-hidden="true"><img src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdib3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48cGF0aCBkPSJNMTUuNjIyIDAuMDA5MTU3NTFDMTUuNzEyMyAwLjAyNzEzMzUgMTUuNzk1OSAwLjA3MTM0IDE1Ljg2MiAwLjEzNzM2M0MxNS45NSAwLjIyNTQzNiAxNS45OTk1IDAuMzQ1MjI2IDE1Ljk5OTMgMC40Njk3OEwxNS45OTI5IDUuNDIzMDhMMTUuOTgzNyA1LjUxNzRDMTUuOTM5OSA1LjczMTA2IDE1Ljc1MDYgNS44OTIwNCAxNS41MjQgNS44OTE5NEMxNS4yNjUxIDUuODkxNjIgMTUuMDU0OSA1LjY4MTA2IDE1LjA1NTIgNS40MjIxNkwxNS4wNTk3IDEuNjAxNjVMMTAuMTc2OSA2LjQ4NTM1QzkuOTkzODQgNi42Njg0NSA5LjY5NzA0IDYuNjY4NDUgOS41MTM5NCA2LjQ4NTM1QzkuMzMwODMgNi4zMDIyNCA5LjMzMDgzIDYuMDA1NDUgOS41MTM5NCA1LjgyMjM0TDE0LjM5NjcgMC45Mzg2NDVMMTAuNTc3MSAwLjk0NDEzOUwxMC40ODI4IDAuOTM0OTgyQzEwLjI2OSAwLjg5MTU4NCAxMC4xMDc2IDAuNzAxOTAzIDEwLjEwNzMgMC40NzUyNzVDMTAuMTA3MiAwLjIxNjUwNyAxMC4zMTc0IDAuMDA2NzM0ODQgMTAuNTc2MiAwLjAwNjQxMDI2TDE1LjUyOTUgMEwxNS42MjIgMC4wMDkxNTc1MVoiIGZpbGw9ImN1cnJlbnRDb2xvciIgLz48cGF0aCBkPSJNMC4zNzcyOSAxNS45OTA4QzAuMjg3MDU3IDE1Ljk3MjkgMC4yMDMzODUgMTUuOTI4NyAwLjEzNzM2MiAxNS44NjI2QzAuMDQ5Mjg4OCAxNS43NzQ2IC0wLjAwMDE1NzAyNCAxNS42NTQ4IC04LjE4MjM1ZS0wNyAxNS41MzAyTDAuMDA2NDA5NDcgMTAuNTc2OUwwLjAxNTU2NyAxMC40ODI2QzAuMDU5Mzg5MSAxMC4yNjg5IDAuMjQ4NzQxIDEwLjEwOCAwLjQ3NTI3NiAxMC4xMDgxQzAuNzM0MTkxIDEwLjEwODQgMC45NDQ0MTUgMTAuMzE4OSAwLjk0NDE0MyAxMC41Nzc4TDAuOTM5NTY0IDE0LjM5ODRMNS44MjIzNyA5LjUxNDY1QzYuMDA1NDcgOS4zMzE1NSA2LjMwMjI3IDkuMzMxNTUgNi40ODUzOCA5LjUxNDY1QzYuNjY4NDggOS42OTc3NiA2LjY2ODQ4IDkuOTk0NTUgNi40ODUzOCAxMC4xNzc3TDEuNjAyNTcgMTUuMDYxNEw1LjQyMjE4IDE1LjA1NTlMNS41MTY1MSAxNS4wNjVDNS43MzAyOSAxNS4xMDg0IDUuODkxNjggMTUuMjk4MSA1Ljg5MTk3IDE1LjUyNDdDNS44OTIwOCAxNS43ODM1IDUuNjgxOTIgMTUuOTkzMyA1LjQyMzEgMTUuOTkzNkwwLjQ2OTc4MSAxNkwwLjM3NzI5IDE1Ljk5MDhaIiBmaWxsPSJjdXJyZW50Q29sb3IiIC8+PC9zdmc+" /></span></span>
</figure>

</div>

</div>

For example, if deleting a node from a Binary Search Tree (BST) crashes when the right child has no left subtree, C is: node has two children AND node.right.left is None. Every other delete scenario falls outside C and should be untouched.

Every experienced engineer reasons about C, often implicitly. But without C as an explicit, shared artifact, there's no guarantee the agent’s boundary matches yours. When C stays implicit, three things can go wrong:

1.  **The agent drifts from the boundary.** Even when the bug report is precise, the agent has no persistent record of the boundary. At each step, it re-interprets this boundary from scratch and over multiple steps those interpretations drift away from the original intent.
2.  **The agent invents a boundary.** When the bug report is vague, the agent fills the gaps with its best guesses, like any engineer would. The difference is the agent doesn’t show them explicitly. By the time you see the mismatch in code review, the patch is already built around it.
3.  **The agent can**’**t check that it respected the boundary.** Without an explicit C, there is no systematic way to check if everything else still works. The agent can check its fix, but it can’t check if it stayed within the boundary.

So C draws the boundary. But alone, it isn’t enough. C tells us when the bug triggers, but not what "fixed" means. The ***postcondition*** P fills that gap: it defines what the code should do for inputs where C holds, i.e., what should happen for the buggy inputs. For a BST delete that crashes, P is: the delete operation does not crash, removes the node, and preserves the BST invariant.

Without P, the agent can suppress the error with a try/except and call it fixed. P forces it to align with what correct means.

<div class="heading-anchor-wrapper">

### Fix and preservation properties

<a href="#fix-and-preservation-properties" class="anchor-link" aria-label="Copy link to Fix and preservation properties section"><span class="anchor-icon-wrapper"><img src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iYW5jaG9yLWljb24iIHZpZXdib3g9IjAgMCAxNiAxNyIgd2lkdGg9IjE2IiBoZWlnaHQ9IjE3IiBmaWxsPSJjdXJyZW50Q29sb3IiPjxwYXRoIGQ9Ik0yLjI3MTQzIDE0LjIyOEMwLjU5MTg5NyAxMi41NDg1IDAuNTkxODk3IDkuODI1MzkgMi4yNzE0MyA4LjE0NTg1TDMuNDIzMjQgNi45OTQwNEwzLjQ0MTg4IDYuOTc2MzVDMy42MzgxNiA2Ljc5OSAzLjk0MTE4IDYuODA0ODggNC4xMzAzNSA2Ljk5NDA0QzQuMzE5NTEgNy4xODMyMSA0LjMyNTM5IDcuNDg2MjMgNC4xNDgwNCA3LjY4MjVMNC4xMzAzNSA3LjcwMTE1TDIuOTc4NTQgOC44NTI5NkMxLjY4OTUzIDEwLjE0MiAxLjY4OTUzIDEyLjIzMTkgMi45Nzg1NCAxMy41MjA5TDMuMDA4ODggMTMuNTUwOUM0LjMwMDE0IDE0LjgwOTggNi4zNjc1MSAxNC43OTk4IDcuNjQ2NDYgMTMuNTIwOUw4Ljc5ODI3IDEyLjM2OTFMOC44MTY5MSAxMi4zNTE0QzkuMDEzMTkgMTIuMTc0IDkuMzE2MjEgMTIuMTc5OSA5LjUwNTM4IDEyLjM2OTFDOS42OTQ1NCAxMi41NTgyIDkuNzAwNDYgMTIuODYxMyA5LjUyMzExIDEzLjA1NzZMOS41MDUzOCAxMy4wNzYyTDguMzUzNTYgMTQuMjI4QzYuNjg3MTUgMTUuODk0NCAzLjk5MzQ3IDE1LjkwNzQgMi4zMTEgMTQuMjY3TDIuMjcxNDMgMTQuMjI4Wk0xMy4wMjE1IDMuNDc3OTNDMTEuNzQyNSAyLjE5ODk5IDkuNjc1MTcgMi4xODg5NiA4LjM4MzkgMy40NDc5NEw4LjM1MzU2IDMuNDc3OTNMNy4yMjU3OSA0LjYwNTdDNy4wMzA1MyA0LjgwMDk2IDYuNzEzOTUgNC44MDA5NiA2LjUxODY5IDQuNjA1N0M2LjMyMzQyIDQuNDEwNDQgNi4zMjM0MiA0LjA5Mzg2IDYuNTE4NjkgMy44OTg1OUw3LjY0NjQ2IDIuNzcwODJMNy42ODYwMyAyLjczMTc3QzkuMzY4NSAxLjA5MTM4IDEyLjA2MjIgMS4xMDQ0MSAxMy43Mjg2IDIuNzcwODJMMTMuNzY3NyAyLjgxMDM2QzE1LjM5NTIgNC40Nzk1OCAxNS4zOTUxIDcuMTQ0MTcgMTMuNzY3NyA4LjgxMzM4TDEzLjcyODYgOC44NTI5NkwxMi42MDA4IDkuOTgwNzNDMTIuNDA1NiAxMC4xNzYgMTIuMDg5IDEwLjE3NiAxMS44OTM3IDkuOTgwNzNDMTEuNjk4NSA5Ljc4NTQ3IDExLjY5ODUgOS40Njg4OCAxMS44OTM3IDkuMjczNjJMMTMuMDIxNSA4LjE0NTg1TDEzLjA1MTUgOC4xMTU1MUMxNC4zMDA1IDYuODM0NDIgMTQuMzAwNSA0Ljc4OTM3IDEzLjA1MTUgMy41MDgyN0wxMy4wMjE1IDMuNDc3OTNaIiAvPjxwYXRoIGQ9Ik0xMC4wMjE5IDUuODY2MzJMMTAuMDQwNiA1Ljg0ODU4QzEwLjIzNjkgNS42NzEyNCAxMC41Mzk5IDUuNjc3MTYgMTAuNzI5IDUuODY2MzJDMTAuOTE4MiA2LjA1NTQ4IDEwLjkyNDEgNi4zNTg0NiAxMC43NDY4IDYuNTU0NzRMMTAuNzI5IDYuNTczNDJMNi4xNDU4OCAxMS4xNTY2QzUuOTUwNjIgMTEuMzUxOCA1LjYzNDAzIDExLjM1MTggNS40Mzg3NyAxMS4xNTY2QzUuMjQzNTEgMTAuOTYxMyA1LjI0MzUxIDEwLjY0NDcgNS40Mzg3NyAxMC40NDk1TDEwLjAyMTkgNS44NjYzMloiIC8+PC9zdmc+" class="anchor-icon" /><span class="copied-indicator docsearch-exclude" aria-live="polite" aria-atomic="true"></span></span></a>

</div>

With property-aware code evolution, we define properties before writing the code. A ***property*** is a testable claim: for all inputs satisfying some condition, some guarantee holds. We use the bug condition C and postcondition P to define two properties:

- **Fix property (C ⟹ P):** When C holds, the patched code satisfies P.
  - Example: The Fix property claims "delete satisfies P on trees where node has two children and node.right.left is None." We can check this by running delete on such trees. If one crashes, the property fails.
- **Preservation property (not C ⟹ unchanged):** When C doesn't hold, the patched code behaves identically to the original.
  - Example: The Preservation property claims "delete behaves identically on all other trees." Check it by running delete on trees outside C before and after the fix. If the behavior changes, the property fails.

Together, these two properties cover the entire input space and constrain how the agent writes the fix. Any patch must pass the fix property without breaking the preservation property. We call this methodology ***property-aware code evolution***.

Kiro's bug-fixing workflow uses this methodology under the hood. Kiro proposes the bug condition, the postcondition, and the fix and preservation properties. You refine them together, and the resulting spec, tests, and fix that Kiro generates all flow from those properties.

<div class="heading-anchor-wrapper">

## Kiro’s bug fix workflow in practice: a BST delete bug

<a href="#kiros-bug-fix-workflow-in-practice-a-bst-delete-bug" class="anchor-link" aria-label="Copy link to Kiros bug fix workflow in practice a bst delete bug section"><span class="anchor-icon-wrapper"><img src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iYW5jaG9yLWljb24iIHZpZXdib3g9IjAgMCAxNiAxNyIgd2lkdGg9IjE2IiBoZWlnaHQ9IjE3IiBmaWxsPSJjdXJyZW50Q29sb3IiPjxwYXRoIGQ9Ik0yLjI3MTQzIDE0LjIyOEMwLjU5MTg5NyAxMi41NDg1IDAuNTkxODk3IDkuODI1MzkgMi4yNzE0MyA4LjE0NTg1TDMuNDIzMjQgNi45OTQwNEwzLjQ0MTg4IDYuOTc2MzVDMy42MzgxNiA2Ljc5OSAzLjk0MTE4IDYuODA0ODggNC4xMzAzNSA2Ljk5NDA0QzQuMzE5NTEgNy4xODMyMSA0LjMyNTM5IDcuNDg2MjMgNC4xNDgwNCA3LjY4MjVMNC4xMzAzNSA3LjcwMTE1TDIuOTc4NTQgOC44NTI5NkMxLjY4OTUzIDEwLjE0MiAxLjY4OTUzIDEyLjIzMTkgMi45Nzg1NCAxMy41MjA5TDMuMDA4ODggMTMuNTUwOUM0LjMwMDE0IDE0LjgwOTggNi4zNjc1MSAxNC43OTk4IDcuNjQ2NDYgMTMuNTIwOUw4Ljc5ODI3IDEyLjM2OTFMOC44MTY5MSAxMi4zNTE0QzkuMDEzMTkgMTIuMTc0IDkuMzE2MjEgMTIuMTc5OSA5LjUwNTM4IDEyLjM2OTFDOS42OTQ1NCAxMi41NTgyIDkuNzAwNDYgMTIuODYxMyA5LjUyMzExIDEzLjA1NzZMOS41MDUzOCAxMy4wNzYyTDguMzUzNTYgMTQuMjI4QzYuNjg3MTUgMTUuODk0NCAzLjk5MzQ3IDE1LjkwNzQgMi4zMTEgMTQuMjY3TDIuMjcxNDMgMTQuMjI4Wk0xMy4wMjE1IDMuNDc3OTNDMTEuNzQyNSAyLjE5ODk5IDkuNjc1MTcgMi4xODg5NiA4LjM4MzkgMy40NDc5NEw4LjM1MzU2IDMuNDc3OTNMNy4yMjU3OSA0LjYwNTdDNy4wMzA1MyA0LjgwMDk2IDYuNzEzOTUgNC44MDA5NiA2LjUxODY5IDQuNjA1N0M2LjMyMzQyIDQuNDEwNDQgNi4zMjM0MiA0LjA5Mzg2IDYuNTE4NjkgMy44OTg1OUw3LjY0NjQ2IDIuNzcwODJMNy42ODYwMyAyLjczMTc3QzkuMzY4NSAxLjA5MTM4IDEyLjA2MjIgMS4xMDQ0MSAxMy43Mjg2IDIuNzcwODJMMTMuNzY3NyAyLjgxMDM2QzE1LjM5NTIgNC40Nzk1OCAxNS4zOTUxIDcuMTQ0MTcgMTMuNzY3NyA4LjgxMzM4TDEzLjcyODYgOC44NTI5NkwxMi42MDA4IDkuOTgwNzNDMTIuNDA1NiAxMC4xNzYgMTIuMDg5IDEwLjE3NiAxMS44OTM3IDkuOTgwNzNDMTEuNjk4NSA5Ljc4NTQ3IDExLjY5ODUgOS40Njg4OCAxMS44OTM3IDkuMjczNjJMMTMuMDIxNSA4LjE0NTg1TDEzLjA1MTUgOC4xMTU1MUMxNC4zMDA1IDYuODM0NDIgMTQuMzAwNSA0Ljc4OTM3IDEzLjA1MTUgMy41MDgyN0wxMy4wMjE1IDMuNDc3OTNaIiAvPjxwYXRoIGQ9Ik0xMC4wMjE5IDUuODY2MzJMMTAuMDQwNiA1Ljg0ODU4QzEwLjIzNjkgNS42NzEyNCAxMC41Mzk5IDUuNjc3MTYgMTAuNzI5IDUuODY2MzJDMTAuOTE4MiA2LjA1NTQ4IDEwLjkyNDEgNi4zNTg0NiAxMC43NDY4IDYuNTU0NzRMMTAuNzI5IDYuNTczNDJMNi4xNDU4OCAxMS4xNTY2QzUuOTUwNjIgMTEuMzUxOCA1LjYzNDAzIDExLjM1MTggNS40Mzg3NyAxMS4xNTY2QzUuMjQzNTEgMTAuOTYxMyA1LjI0MzUxIDEwLjY0NDcgNS40Mzg3NyAxMC40NDk1TDEwLjAyMTkgNS44NjYzMloiIC8+PC9zdmc+" class="anchor-icon" /><span class="copied-indicator docsearch-exclude" aria-live="polite" aria-atomic="true"></span></span></a>

</div>

Here’s a concrete bug report showing a classic data structures bug:

<div class="promptBox">

<div class="my-6 rounded-md bg-muted-foreground/10 p-4">

Loading code example...

</div>

</div>

You paste this into Kiro and opt into the bugfix workflow. Kiro doesn’t jump to a patch. It partitions the buggy and non-buggy scenarios, formulates a root cause hypothesis, and tests that hypothesis, before writing a single line of code.

<div class="heading-anchor-wrapper">

### Bugfix doc

<a href="#bugfix-doc" class="anchor-link" aria-label="Copy link to Bugfix doc section"><span class="anchor-icon-wrapper"><img src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iYW5jaG9yLWljb24iIHZpZXdib3g9IjAgMCAxNiAxNyIgd2lkdGg9IjE2IiBoZWlnaHQ9IjE3IiBmaWxsPSJjdXJyZW50Q29sb3IiPjxwYXRoIGQ9Ik0yLjI3MTQzIDE0LjIyOEMwLjU5MTg5NyAxMi41NDg1IDAuNTkxODk3IDkuODI1MzkgMi4yNzE0MyA4LjE0NTg1TDMuNDIzMjQgNi45OTQwNEwzLjQ0MTg4IDYuOTc2MzVDMy42MzgxNiA2Ljc5OSAzLjk0MTE4IDYuODA0ODggNC4xMzAzNSA2Ljk5NDA0QzQuMzE5NTEgNy4xODMyMSA0LjMyNTM5IDcuNDg2MjMgNC4xNDgwNCA3LjY4MjVMNC4xMzAzNSA3LjcwMTE1TDIuOTc4NTQgOC44NTI5NkMxLjY4OTUzIDEwLjE0MiAxLjY4OTUzIDEyLjIzMTkgMi45Nzg1NCAxMy41MjA5TDMuMDA4ODggMTMuNTUwOUM0LjMwMDE0IDE0LjgwOTggNi4zNjc1MSAxNC43OTk4IDcuNjQ2NDYgMTMuNTIwOUw4Ljc5ODI3IDEyLjM2OTFMOC44MTY5MSAxMi4zNTE0QzkuMDEzMTkgMTIuMTc0IDkuMzE2MjEgMTIuMTc5OSA5LjUwNTM4IDEyLjM2OTFDOS42OTQ1NCAxMi41NTgyIDkuNzAwNDYgMTIuODYxMyA5LjUyMzExIDEzLjA1NzZMOS41MDUzOCAxMy4wNzYyTDguMzUzNTYgMTQuMjI4QzYuNjg3MTUgMTUuODk0NCAzLjk5MzQ3IDE1LjkwNzQgMi4zMTEgMTQuMjY3TDIuMjcxNDMgMTQuMjI4Wk0xMy4wMjE1IDMuNDc3OTNDMTEuNzQyNSAyLjE5ODk5IDkuNjc1MTcgMi4xODg5NiA4LjM4MzkgMy40NDc5NEw4LjM1MzU2IDMuNDc3OTNMNy4yMjU3OSA0LjYwNTdDNy4wMzA1MyA0LjgwMDk2IDYuNzEzOTUgNC44MDA5NiA2LjUxODY5IDQuNjA1N0M2LjMyMzQyIDQuNDEwNDQgNi4zMjM0MiA0LjA5Mzg2IDYuNTE4NjkgMy44OTg1OUw3LjY0NjQ2IDIuNzcwODJMNy42ODYwMyAyLjczMTc3QzkuMzY4NSAxLjA5MTM4IDEyLjA2MjIgMS4xMDQ0MSAxMy43Mjg2IDIuNzcwODJMMTMuNzY3NyAyLjgxMDM2QzE1LjM5NTIgNC40Nzk1OCAxNS4zOTUxIDcuMTQ0MTcgMTMuNzY3NyA4LjgxMzM4TDEzLjcyODYgOC44NTI5NkwxMi42MDA4IDkuOTgwNzNDMTIuNDA1NiAxMC4xNzYgMTIuMDg5IDEwLjE3NiAxMS44OTM3IDkuOTgwNzNDMTEuNjk4NSA5Ljc4NTQ3IDExLjY5ODUgOS40Njg4OCAxMS44OTM3IDkuMjczNjJMMTMuMDIxNSA4LjE0NTg1TDEzLjA1MTUgOC4xMTU1MUMxNC4zMDA1IDYuODM0NDIgMTQuMzAwNSA0Ljc4OTM3IDEzLjA1MTUgMy41MDgyN0wxMy4wMjE1IDMuNDc3OTNaIiAvPjxwYXRoIGQ9Ik0xMC4wMjE5IDUuODY2MzJMMTAuMDQwNiA1Ljg0ODU4QzEwLjIzNjkgNS42NzEyNCAxMC41Mzk5IDUuNjc3MTYgMTAuNzI5IDUuODY2MzJDMTAuOTE4MiA2LjA1NTQ4IDEwLjkyNDEgNi4zNTg0NiAxMC43NDY4IDYuNTU0NzRMMTAuNzI5IDYuNTczNDJMNi4xNDU4OCAxMS4xNTY2QzUuOTUwNjIgMTEuMzUxOCA1LjYzNDAzIDExLjM1MTggNS40Mzg3NyAxMS4xNTY2QzUuMjQzNTEgMTAuOTYxMyA1LjI0MzUxIDEwLjY0NDcgNS40Mzg3NyAxMC40NDk1TDEwLjAyMTkgNS44NjYzMloiIC8+PC9zdmc+" class="anchor-icon" /><span class="copied-indicator docsearch-exclude" aria-live="polite" aria-atomic="true"></span></span></a>

</div>

Kiro analyzes the bug report and generates a Bugfix document with three requirement categories: the current defective behavior, the expected fix, and unchanged behavior that must be preserved.

<div>

<div class="my-8">

<figure class="overflow-hidden rounded-2xl border border-[#4a464f] bg-muted/30">
<span class="group relative inline-block transition-all duration-200 cursor-zoom-in" style="display:block" tabindex="0" role="button" aria-label="Open image lightbox: Kiro&#39;s BST Delete Crash Bugfix Requirements document showing current defective behavior, expected behavior, and unchanged behavior sections"><span class="relative overflow-hidden h-auto w-full border-0"><span class="absolute inset-0 flex animate-pulse items-center justify-center bg-muted"><span class="sr-only">Loading image...</span></span><img src="/images/blogs/bug-fix-paradox/ide.png?h=9529bcd8" class="transition-opacity duration-300 opacity-0" style="color:transparent" loading="lazy" decoding="async" data-nimg="1" width="1200" height="600" alt="Kiro&#39;s BST Delete Crash Bugfix Requirements document showing current defective behavior, expected behavior, and unchanged behavior sections" /></span><span class="absolute bottom-2 right-2 z-10 flex items-center justify-center rounded-full bg-prey-600/60 p-2.5 transition-opacity duration-200 opacity-100 group-hover:opacity-100" aria-hidden="true"><img src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdib3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48cGF0aCBkPSJNMTUuNjIyIDAuMDA5MTU3NTFDMTUuNzEyMyAwLjAyNzEzMzUgMTUuNzk1OSAwLjA3MTM0IDE1Ljg2MiAwLjEzNzM2M0MxNS45NSAwLjIyNTQzNiAxNS45OTk1IDAuMzQ1MjI2IDE1Ljk5OTMgMC40Njk3OEwxNS45OTI5IDUuNDIzMDhMMTUuOTgzNyA1LjUxNzRDMTUuOTM5OSA1LjczMTA2IDE1Ljc1MDYgNS44OTIwNCAxNS41MjQgNS44OTE5NEMxNS4yNjUxIDUuODkxNjIgMTUuMDU0OSA1LjY4MTA2IDE1LjA1NTIgNS40MjIxNkwxNS4wNTk3IDEuNjAxNjVMMTAuMTc2OSA2LjQ4NTM1QzkuOTkzODQgNi42Njg0NSA5LjY5NzA0IDYuNjY4NDUgOS41MTM5NCA2LjQ4NTM1QzkuMzMwODMgNi4zMDIyNCA5LjMzMDgzIDYuMDA1NDUgOS41MTM5NCA1LjgyMjM0TDE0LjM5NjcgMC45Mzg2NDVMMTAuNTc3MSAwLjk0NDEzOUwxMC40ODI4IDAuOTM0OTgyQzEwLjI2OSAwLjg5MTU4NCAxMC4xMDc2IDAuNzAxOTAzIDEwLjEwNzMgMC40NzUyNzVDMTAuMTA3MiAwLjIxNjUwNyAxMC4zMTc0IDAuMDA2NzM0ODQgMTAuNTc2MiAwLjAwNjQxMDI2TDE1LjUyOTUgMEwxNS42MjIgMC4wMDkxNTc1MVoiIGZpbGw9ImN1cnJlbnRDb2xvciIgLz48cGF0aCBkPSJNMC4zNzcyOSAxNS45OTA4QzAuMjg3MDU3IDE1Ljk3MjkgMC4yMDMzODUgMTUuOTI4NyAwLjEzNzM2MiAxNS44NjI2QzAuMDQ5Mjg4OCAxNS43NzQ2IC0wLjAwMDE1NzAyNCAxNS42NTQ4IC04LjE4MjM1ZS0wNyAxNS41MzAyTDAuMDA2NDA5NDcgMTAuNTc2OUwwLjAxNTU2NyAxMC40ODI2QzAuMDU5Mzg5MSAxMC4yNjg5IDAuMjQ4NzQxIDEwLjEwOCAwLjQ3NTI3NiAxMC4xMDgxQzAuNzM0MTkxIDEwLjEwODQgMC45NDQ0MTUgMTAuMzE4OSAwLjk0NDE0MyAxMC41Nzc4TDAuOTM5NTY0IDE0LjM5ODRMNS44MjIzNyA5LjUxNDY1QzYuMDA1NDcgOS4zMzE1NSA2LjMwMjI3IDkuMzMxNTUgNi40ODUzOCA5LjUxNDY1QzYuNjY4NDggOS42OTc3NiA2LjY2ODQ4IDkuOTk0NTUgNi40ODUzOCAxMC4xNzc3TDEuNjAyNTcgMTUuMDYxNEw1LjQyMjE4IDE1LjA1NTlMNS41MTY1MSAxNS4wNjVDNS43MzAyOSAxNS4xMDg0IDUuODkxNjggMTUuMjk4MSA1Ljg5MTk3IDE1LjUyNDdDNS44OTIwOCAxNS43ODM1IDUuNjgxOTIgMTUuOTkzMyA1LjQyMzEgMTUuOTkzNkwwLjQ2OTc4MSAxNkwwLjM3NzI5IDE1Ljk5MDhaIiBmaWxsPSJjdXJyZW50Q29sb3IiIC8+PC9zdmc+" /></span></span>
</figure>

</div>

</div>

This mirrors the partition defined by the bug condition C. Defect and fix requirements target buggy inputs. Preservation requirements identify specific behaviors that must not change.

<div class="heading-anchor-wrapper">

### Design: bug condition and root cause hypothesis

<a href="#design-bug-condition-and-root-cause-hypothesis" class="anchor-link" aria-label="Copy link to Design bug condition and root cause hypothesis section"><span class="anchor-icon-wrapper"><img src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iYW5jaG9yLWljb24iIHZpZXdib3g9IjAgMCAxNiAxNyIgd2lkdGg9IjE2IiBoZWlnaHQ9IjE3IiBmaWxsPSJjdXJyZW50Q29sb3IiPjxwYXRoIGQ9Ik0yLjI3MTQzIDE0LjIyOEMwLjU5MTg5NyAxMi41NDg1IDAuNTkxODk3IDkuODI1MzkgMi4yNzE0MyA4LjE0NTg1TDMuNDIzMjQgNi45OTQwNEwzLjQ0MTg4IDYuOTc2MzVDMy42MzgxNiA2Ljc5OSAzLjk0MTE4IDYuODA0ODggNC4xMzAzNSA2Ljk5NDA0QzQuMzE5NTEgNy4xODMyMSA0LjMyNTM5IDcuNDg2MjMgNC4xNDgwNCA3LjY4MjVMNC4xMzAzNSA3LjcwMTE1TDIuOTc4NTQgOC44NTI5NkMxLjY4OTUzIDEwLjE0MiAxLjY4OTUzIDEyLjIzMTkgMi45Nzg1NCAxMy41MjA5TDMuMDA4ODggMTMuNTUwOUM0LjMwMDE0IDE0LjgwOTggNi4zNjc1MSAxNC43OTk4IDcuNjQ2NDYgMTMuNTIwOUw4Ljc5ODI3IDEyLjM2OTFMOC44MTY5MSAxMi4zNTE0QzkuMDEzMTkgMTIuMTc0IDkuMzE2MjEgMTIuMTc5OSA5LjUwNTM4IDEyLjM2OTFDOS42OTQ1NCAxMi41NTgyIDkuNzAwNDYgMTIuODYxMyA5LjUyMzExIDEzLjA1NzZMOS41MDUzOCAxMy4wNzYyTDguMzUzNTYgMTQuMjI4QzYuNjg3MTUgMTUuODk0NCAzLjk5MzQ3IDE1LjkwNzQgMi4zMTEgMTQuMjY3TDIuMjcxNDMgMTQuMjI4Wk0xMy4wMjE1IDMuNDc3OTNDMTEuNzQyNSAyLjE5ODk5IDkuNjc1MTcgMi4xODg5NiA4LjM4MzkgMy40NDc5NEw4LjM1MzU2IDMuNDc3OTNMNy4yMjU3OSA0LjYwNTdDNy4wMzA1MyA0LjgwMDk2IDYuNzEzOTUgNC44MDA5NiA2LjUxODY5IDQuNjA1N0M2LjMyMzQyIDQuNDEwNDQgNi4zMjM0MiA0LjA5Mzg2IDYuNTE4NjkgMy44OTg1OUw3LjY0NjQ2IDIuNzcwODJMNy42ODYwMyAyLjczMTc3QzkuMzY4NSAxLjA5MTM4IDEyLjA2MjIgMS4xMDQ0MSAxMy43Mjg2IDIuNzcwODJMMTMuNzY3NyAyLjgxMDM2QzE1LjM5NTIgNC40Nzk1OCAxNS4zOTUxIDcuMTQ0MTcgMTMuNzY3NyA4LjgxMzM4TDEzLjcyODYgOC44NTI5NkwxMi42MDA4IDkuOTgwNzNDMTIuNDA1NiAxMC4xNzYgMTIuMDg5IDEwLjE3NiAxMS44OTM3IDkuOTgwNzNDMTEuNjk4NSA5Ljc4NTQ3IDExLjY5ODUgOS40Njg4OCAxMS44OTM3IDkuMjczNjJMMTMuMDIxNSA4LjE0NTg1TDEzLjA1MTUgOC4xMTU1MUMxNC4zMDA1IDYuODM0NDIgMTQuMzAwNSA0Ljc4OTM3IDEzLjA1MTUgMy41MDgyN0wxMy4wMjE1IDMuNDc3OTNaIiAvPjxwYXRoIGQ9Ik0xMC4wMjE5IDUuODY2MzJMMTAuMDQwNiA1Ljg0ODU4QzEwLjIzNjkgNS42NzEyNCAxMC41Mzk5IDUuNjc3MTYgMTAuNzI5IDUuODY2MzJDMTAuOTE4MiA2LjA1NTQ4IDEwLjkyNDEgNi4zNTg0NiAxMC43NDY4IDYuNTU0NzRMMTAuNzI5IDYuNTczNDJMNi4xNDU4OCAxMS4xNTY2QzUuOTUwNjIgMTEuMzUxOCA1LjYzNDAzIDExLjM1MTggNS40Mzg3NyAxMS4xNTY2QzUuMjQzNTEgMTAuOTYxMyA1LjI0MzUxIDEwLjY0NDcgNS40Mzg3NyAxMC40NDk1TDEwLjAyMTkgNS44NjYzMloiIC8+PC9zdmc+" class="anchor-icon" /><span class="copied-indicator docsearch-exclude" aria-live="polite" aria-atomic="true"></span></span></a>

</div>

The Bugfix doc partitions the scenarios in natural language. Kiro now formalizes it and investigates why the bug exists.

**Formalizing the partition***.* Kiro extracts the bug condition C from the defect and fix requirements:

<div class="my-6 rounded-md bg-muted-foreground/10 p-4">

Loading code example...

</div>

Kiro also formalizes what “fixed” means as a postcondition P:

<div class="my-6 rounded-md bg-muted-foreground/10 p-4">

Loading code example...

</div>

**Tracing the root cause.** With C and P established, Kiro reads the codebase to build a root cause hypothesis: why do inputs satisfying C crash instead of satisfying P? It traces the execution flow for an input where C holds:

<div class="my-6 rounded-md bg-muted-foreground/10 p-4">

Loading code example...

</div>

For an input where C holds, say deleting 5 from \[5, 3, 7\], the trace evaluates:

<div class="my-6 rounded-md bg-muted-foreground/10 p-4">

Loading code example...

</div>

The hypothesis: `_find_min` receives `node.right.left` instead of `node.right`. When C holds, `node.right.left` is None by definition, so the call always crashes.

**The Checkpoint.** Before writing any code or tests, Kiro presents C, P, and the hypothesis for your review. Nothing has been generated yet. If C is too narrow, too broad, or targets the wrong scenario, you get a chance to push back and refine it. If the hypothesis is wrong, the next phase catches it: tests for the fix property should fail on the unfixed code with an AttributeError. If they fail for a different reason, or don’t fail at all, the hypothesis is refuted and Kiro re-analyzes before writing any fix.

The root cause hypothesis makes the design phase more than documentation. It’s a falsifiable prediction. The entire testing strategy that follows is designed to confirm or refute it.

<div class="heading-anchor-wrapper">

### The task plan: testing the hypothesis

<a href="#the-task-plan-testing-the-hypothesis" class="anchor-link" aria-label="Copy link to The task plan testing the hypothesis section"><span class="anchor-icon-wrapper"><img src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iYW5jaG9yLWljb24iIHZpZXdib3g9IjAgMCAxNiAxNyIgd2lkdGg9IjE2IiBoZWlnaHQ9IjE3IiBmaWxsPSJjdXJyZW50Q29sb3IiPjxwYXRoIGQ9Ik0yLjI3MTQzIDE0LjIyOEMwLjU5MTg5NyAxMi41NDg1IDAuNTkxODk3IDkuODI1MzkgMi4yNzE0MyA4LjE0NTg1TDMuNDIzMjQgNi45OTQwNEwzLjQ0MTg4IDYuOTc2MzVDMy42MzgxNiA2Ljc5OSAzLjk0MTE4IDYuODA0ODggNC4xMzAzNSA2Ljk5NDA0QzQuMzE5NTEgNy4xODMyMSA0LjMyNTM5IDcuNDg2MjMgNC4xNDgwNCA3LjY4MjVMNC4xMzAzNSA3LjcwMTE1TDIuOTc4NTQgOC44NTI5NkMxLjY4OTUzIDEwLjE0MiAxLjY4OTUzIDEyLjIzMTkgMi45Nzg1NCAxMy41MjA5TDMuMDA4ODggMTMuNTUwOUM0LjMwMDE0IDE0LjgwOTggNi4zNjc1MSAxNC43OTk4IDcuNjQ2NDYgMTMuNTIwOUw4Ljc5ODI3IDEyLjM2OTFMOC44MTY5MSAxMi4zNTE0QzkuMDEzMTkgMTIuMTc0IDkuMzE2MjEgMTIuMTc5OSA5LjUwNTM4IDEyLjM2OTFDOS42OTQ1NCAxMi41NTgyIDkuNzAwNDYgMTIuODYxMyA5LjUyMzExIDEzLjA1NzZMOS41MDUzOCAxMy4wNzYyTDguMzUzNTYgMTQuMjI4QzYuNjg3MTUgMTUuODk0NCAzLjk5MzQ3IDE1LjkwNzQgMi4zMTEgMTQuMjY3TDIuMjcxNDMgMTQuMjI4Wk0xMy4wMjE1IDMuNDc3OTNDMTEuNzQyNSAyLjE5ODk5IDkuNjc1MTcgMi4xODg5NiA4LjM4MzkgMy40NDc5NEw4LjM1MzU2IDMuNDc3OTNMNy4yMjU3OSA0LjYwNTdDNy4wMzA1MyA0LjgwMDk2IDYuNzEzOTUgNC44MDA5NiA2LjUxODY5IDQuNjA1N0M2LjMyMzQyIDQuNDEwNDQgNi4zMjM0MiA0LjA5Mzg2IDYuNTE4NjkgMy44OTg1OUw3LjY0NjQ2IDIuNzcwODJMNy42ODYwMyAyLjczMTc3QzkuMzY4NSAxLjA5MTM4IDEyLjA2MjIgMS4xMDQ0MSAxMy43Mjg2IDIuNzcwODJMMTMuNzY3NyAyLjgxMDM2QzE1LjM5NTIgNC40Nzk1OCAxNS4zOTUxIDcuMTQ0MTcgMTMuNzY3NyA4LjgxMzM4TDEzLjcyODYgOC44NTI5NkwxMi42MDA4IDkuOTgwNzNDMTIuNDA1NiAxMC4xNzYgMTIuMDg5IDEwLjE3NiAxMS44OTM3IDkuOTgwNzNDMTEuNjk4NSA5Ljc4NTQ3IDExLjY5ODUgOS40Njg4OCAxMS44OTM3IDkuMjczNjJMMTMuMDIxNSA4LjE0NTg1TDEzLjA1MTUgOC4xMTU1MUMxNC4zMDA1IDYuODM0NDIgMTQuMzAwNSA0Ljc4OTM3IDEzLjA1MTUgMy41MDgyN0wxMy4wMjE1IDMuNDc3OTNaIiAvPjxwYXRoIGQ9Ik0xMC4wMjE5IDUuODY2MzJMMTAuMDQwNiA1Ljg0ODU4QzEwLjIzNjkgNS42NzEyNCAxMC41Mzk5IDUuNjc3MTYgMTAuNzI5IDUuODY2MzJDMTAuOTE4MiA2LjA1NTQ4IDEwLjkyNDEgNi4zNTg0NiAxMC43NDY4IDYuNTU0NzRMMTAuNzI5IDYuNTczNDJMNi4xNDU4OCAxMS4xNTY2QzUuOTUwNjIgMTEuMzUxOCA1LjYzNDAzIDExLjM1MTggNS40Mzg3NyAxMS4xNTY2QzUuMjQzNTEgMTAuOTYxMyA1LjI0MzUxIDEwLjY0NDcgNS40Mzg3NyAxMC40NDk1TDEwLjAyMTkgNS44NjYzMloiIC8+PC9zdmc+" class="anchor-icon" /><span class="copied-indicator docsearch-exclude" aria-live="polite" aria-atomic="true"></span></span></a>

</div>

Kiro now has a hypothesis: inputs satisfying C crash because `_find_min` receives `None`. The task plan tests it before writing any fix.

<div>

<div class="my-8">

<figure class="overflow-hidden rounded-2xl border border-[#4a464f] bg-muted/30">
<span class="group relative inline-block transition-all duration-200 cursor-zoom-in" style="display:block" tabindex="0" role="button" aria-label="Open image lightbox: Kiro&#39;s three-task bug fix plan: bug condition tests, preservation tests, then implement fix"><span class="relative overflow-hidden h-auto w-full border-0"><span class="absolute inset-0 flex animate-pulse items-center justify-center bg-muted"><span class="sr-only">Loading image...</span></span><img src="/images/blogs/bug-fix-paradox/flow.png?h=1a912944" class="transition-opacity duration-300 opacity-0" style="color:transparent" loading="lazy" decoding="async" data-nimg="1" width="1200" height="600" alt="Kiro&#39;s three-task bug fix plan: bug condition tests, preservation tests, then implement fix" /></span><span class="absolute bottom-2 right-2 z-10 flex items-center justify-center rounded-full bg-prey-600/60 p-2.5 transition-opacity duration-200 opacity-100 group-hover:opacity-100" aria-hidden="true"><img src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdib3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48cGF0aCBkPSJNMTUuNjIyIDAuMDA5MTU3NTFDMTUuNzEyMyAwLjAyNzEzMzUgMTUuNzk1OSAwLjA3MTM0IDE1Ljg2MiAwLjEzNzM2M0MxNS45NSAwLjIyNTQzNiAxNS45OTk1IDAuMzQ1MjI2IDE1Ljk5OTMgMC40Njk3OEwxNS45OTI5IDUuNDIzMDhMMTUuOTgzNyA1LjUxNzRDMTUuOTM5OSA1LjczMTA2IDE1Ljc1MDYgNS44OTIwNCAxNS41MjQgNS44OTE5NEMxNS4yNjUxIDUuODkxNjIgMTUuMDU0OSA1LjY4MTA2IDE1LjA1NTIgNS40MjIxNkwxNS4wNTk3IDEuNjAxNjVMMTAuMTc2OSA2LjQ4NTM1QzkuOTkzODQgNi42Njg0NSA5LjY5NzA0IDYuNjY4NDUgOS41MTM5NCA2LjQ4NTM1QzkuMzMwODMgNi4zMDIyNCA5LjMzMDgzIDYuMDA1NDUgOS41MTM5NCA1LjgyMjM0TDE0LjM5NjcgMC45Mzg2NDVMMTAuNTc3MSAwLjk0NDEzOUwxMC40ODI4IDAuOTM0OTgyQzEwLjI2OSAwLjg5MTU4NCAxMC4xMDc2IDAuNzAxOTAzIDEwLjEwNzMgMC40NzUyNzVDMTAuMTA3MiAwLjIxNjUwNyAxMC4zMTc0IDAuMDA2NzM0ODQgMTAuNTc2MiAwLjAwNjQxMDI2TDE1LjUyOTUgMEwxNS42MjIgMC4wMDkxNTc1MVoiIGZpbGw9ImN1cnJlbnRDb2xvciIgLz48cGF0aCBkPSJNMC4zNzcyOSAxNS45OTA4QzAuMjg3MDU3IDE1Ljk3MjkgMC4yMDMzODUgMTUuOTI4NyAwLjEzNzM2MiAxNS44NjI2QzAuMDQ5Mjg4OCAxNS43NzQ2IC0wLjAwMDE1NzAyNCAxNS42NTQ4IC04LjE4MjM1ZS0wNyAxNS41MzAyTDAuMDA2NDA5NDcgMTAuNTc2OUwwLjAxNTU2NyAxMC40ODI2QzAuMDU5Mzg5MSAxMC4yNjg5IDAuMjQ4NzQxIDEwLjEwOCAwLjQ3NTI3NiAxMC4xMDgxQzAuNzM0MTkxIDEwLjEwODQgMC45NDQ0MTUgMTAuMzE4OSAwLjk0NDE0MyAxMC41Nzc4TDAuOTM5NTY0IDE0LjM5ODRMNS44MjIzNyA5LjUxNDY1QzYuMDA1NDcgOS4zMzE1NSA2LjMwMjI3IDkuMzMxNTUgNi40ODUzOCA5LjUxNDY1QzYuNjY4NDggOS42OTc3NiA2LjY2ODQ4IDkuOTk0NTUgNi40ODUzOCAxMC4xNzc3TDEuNjAyNTcgMTUuMDYxNEw1LjQyMjE4IDE1LjA1NTlMNS41MTY1MSAxNS4wNjVDNS43MzAyOSAxNS4xMDg0IDUuODkxNjggMTUuMjk4MSA1Ljg5MTk3IDE1LjUyNDdDNS44OTIwOCAxNS43ODM1IDUuNjgxOTIgMTUuOTkzMyA1LjQyMzEgMTUuOTkzNkwwLjQ2OTc4MSAxNkwwLjM3NzI5IDE1Ljk5MDhaIiBmaWxsPSJjdXJyZW50Q29sb3IiIC8+PC9zdmc+" /></span></span>
</figure>

</div>

</div>

Kiro runs every test against the unfixed code first, applies the fix, then retests. It structures the plan into three tasks:

**Task 1**. Kiro writes bug-condition tests for inputs inside C and encodes the expected behavior (P). Kiro runs them against the unfixed code. They fail. That confirms the bug exists exactly where C predicts.

**Task 2.** Kiro runs the unfixed code on inputs outside C, records the actual behavior, and writes preservation tests asserting that behavior. Each test should pass against unfixed code.

**Task 3**. Kiro patches the code according to the root cause hypothesis and reruns the bug-condition and preservation tests. The bug-condition test that failed now passes—the fix works. The preservation tests still pass because nothing else should have changed. If instead, the bug-condition test fails, then the hypothesis was wrong and Kiro flags it and re-investigates before trying another fix. If a preservation test flips, the fix has side effects and Kiro narrows the scope of the patch. Either outcome is actionable.

This is test-driven development’s red-green cycle combined with <a href="https://en.wikipedia.org/wiki/Differential_testing" class="text-primary hover:underline" target="_blank" rel="noopener noreferrer">differential testing</a>. Bug-condition tests are red before the fix, green after. Preservation tests record the unfixed code’s behavior and assert that fixed code behaves the same way on the same inputs; the unfixed code acts as the spec.

<div class="heading-anchor-wrapper">

### Testing before the fix

<a href="#testing-before-the-fix" class="anchor-link" aria-label="Copy link to Testing before the fix section"><span class="anchor-icon-wrapper"><img src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iYW5jaG9yLWljb24iIHZpZXdib3g9IjAgMCAxNiAxNyIgd2lkdGg9IjE2IiBoZWlnaHQ9IjE3IiBmaWxsPSJjdXJyZW50Q29sb3IiPjxwYXRoIGQ9Ik0yLjI3MTQzIDE0LjIyOEMwLjU5MTg5NyAxMi41NDg1IDAuNTkxODk3IDkuODI1MzkgMi4yNzE0MyA4LjE0NTg1TDMuNDIzMjQgNi45OTQwNEwzLjQ0MTg4IDYuOTc2MzVDMy42MzgxNiA2Ljc5OSAzLjk0MTE4IDYuODA0ODggNC4xMzAzNSA2Ljk5NDA0QzQuMzE5NTEgNy4xODMyMSA0LjMyNTM5IDcuNDg2MjMgNC4xNDgwNCA3LjY4MjVMNC4xMzAzNSA3LjcwMTE1TDIuOTc4NTQgOC44NTI5NkMxLjY4OTUzIDEwLjE0MiAxLjY4OTUzIDEyLjIzMTkgMi45Nzg1NCAxMy41MjA5TDMuMDA4ODggMTMuNTUwOUM0LjMwMDE0IDE0LjgwOTgg

[truncated]
# Source: https://kiro.dev/blog/root-cause-in-33s/

**URL:** https://kiro.dev/blog/root-cause-in-33s/
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

April 16, 2026

</div>

# Root cause in 33 seconds: How Kiro CLI saved 4 years of build time

<div class="flex items-center gap-2">

<span class="text-sm text-muted-foreground">By</span>

<div class="flex flex-wrap items-center gap-4">

<div class="flex items-center gap-2">

<span class="relative flex shrink-0 overflow-hidden rounded-full h-8 w-8"><span class="flex h-full w-full items-center justify-center rounded-full bg-muted">CA</span></span>

<div>

Cameron Conradt

Developer

</div>

</div>

<div class="flex items-center gap-2">

<span class="relative flex shrink-0 overflow-hidden rounded-full h-8 w-8"><span class="flex h-full w-full items-center justify-center rounded-full bg-muted">SA</span></span>

<div>

Sameer Bansal

Developer

</div>

</div>

</div>

</div>

</div>

<div class="blog-content changelog prose-prey prose max-w-none dark:prose-invert prose-code:before:content-none prose-code:after:content-none">

33 seconds. That’s all it took Kiro CLI to investigate a gnarly performance bottleneck, identify the root cause buried deep in a legacy codebase, and implement a fix which ended up saving about **4 years of compute time per month** across 381 packages that are built 550,000 times every month within EC2 and many other AWS teams.

<div class="heading-anchor-wrapper">

## The problem: build times that eat your day

<a href="#the-problem-build-times-that-eat-your-day" class="anchor-link" aria-label="Copy link to The problem build times that eat your day section"><span class="anchor-icon-wrapper"><img src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iYW5jaG9yLWljb24iIHZpZXdib3g9IjAgMCAxNiAxNyIgd2lkdGg9IjE2IiBoZWlnaHQ9IjE3IiBmaWxsPSJjdXJyZW50Q29sb3IiPjxwYXRoIGQ9Ik0yLjI3MTQzIDE0LjIyOEMwLjU5MTg5NyAxMi41NDg1IDAuNTkxODk3IDkuODI1MzkgMi4yNzE0MyA4LjE0NTg1TDMuNDIzMjQgNi45OTQwNEwzLjQ0MTg4IDYuOTc2MzVDMy42MzgxNiA2Ljc5OSAzLjk0MTE4IDYuODA0ODggNC4xMzAzNSA2Ljk5NDA0QzQuMzE5NTEgNy4xODMyMSA0LjMyNTM5IDcuNDg2MjMgNC4xNDgwNCA3LjY4MjVMNC4xMzAzNSA3LjcwMTE1TDIuOTc4NTQgOC44NTI5NkMxLjY4OTUzIDEwLjE0MiAxLjY4OTUzIDEyLjIzMTkgMi45Nzg1NCAxMy41MjA5TDMuMDA4ODggMTMuNTUwOUM0LjMwMDE0IDE0LjgwOTggNi4zNjc1MSAxNC43OTk4IDcuNjQ2NDYgMTMuNTIwOUw4Ljc5ODI3IDEyLjM2OTFMOC44MTY5MSAxMi4zNTE0QzkuMDEzMTkgMTIuMTc0IDkuMzE2MjEgMTIuMTc5OSA5LjUwNTM4IDEyLjM2OTFDOS42OTQ1NCAxMi41NTgyIDkuNzAwNDYgMTIuODYxMyA5LjUyMzExIDEzLjA1NzZMOS41MDUzOCAxMy4wNzYyTDguMzUzNTYgMTQuMjI4QzYuNjg3MTUgMTUuODk0NCAzLjk5MzQ3IDE1LjkwNzQgMi4zMTEgMTQuMjY3TDIuMjcxNDMgMTQuMjI4Wk0xMy4wMjE1IDMuNDc3OTNDMTEuNzQyNSAyLjE5ODk5IDkuNjc1MTcgMi4xODg5NiA4LjM4MzkgMy40NDc5NEw4LjM1MzU2IDMuNDc3OTNMNy4yMjU3OSA0LjYwNTdDNy4wMzA1MyA0LjgwMDk2IDYuNzEzOTUgNC44MDA5NiA2LjUxODY5IDQuNjA1N0M2LjMyMzQyIDQuNDEwNDQgNi4zMjM0MiA0LjA5Mzg2IDYuNTE4NjkgMy44OTg1OUw3LjY0NjQ2IDIuNzcwODJMNy42ODYwMyAyLjczMTc3QzkuMzY4NSAxLjA5MTM4IDEyLjA2MjIgMS4xMDQ0MSAxMy43Mjg2IDIuNzcwODJMMTMuNzY3NyAyLjgxMDM2QzE1LjM5NTIgNC40Nzk1OCAxNS4zOTUxIDcuMTQ0MTcgMTMuNzY3NyA4LjgxMzM4TDEzLjcyODYgOC44NTI5NkwxMi42MDA4IDkuOTgwNzNDMTIuNDA1NiAxMC4xNzYgMTIuMDg5IDEwLjE3NiAxMS44OTM3IDkuOTgwNzNDMTEuNjk4NSA5Ljc4NTQ3IDExLjY5ODUgOS40Njg4OCAxMS44OTM3IDkuMjczNjJMMTMuMDIxNSA4LjE0NTg1TDEzLjA1MTUgOC4xMTU1MUMxNC4zMDA1IDYuODM0NDIgMTQuMzAwNSA0Ljc4OTM3IDEzLjA1MTUgMy41MDgyN0wxMy4wMjE1IDMuNDc3OTNaIiAvPjxwYXRoIGQ9Ik0xMC4wMjE5IDUuODY2MzJMMTAuMDQwNiA1Ljg0ODU4QzEwLjIzNjkgNS42NzEyNCAxMC41Mzk5IDUuNjc3MTYgMTAuNzI5IDUuODY2MzJDMTAuOTE4MiA2LjA1NTQ4IDEwLjkyNDEgNi4zNTg0NiAxMC43NDY4IDYuNTU0NzRMMTAuNzI5IDYuNTczNDJMNi4xNDU4OCAxMS4xNTY2QzUuOTUwNjIgMTEuMzUxOCA1LjYzNDAzIDExLjM1MTggNS40Mzg3NyAxMS4xNTY2QzUuMjQzNTEgMTAuOTYxMyA1LjI0MzUxIDEwLjY0NDcgNS40Mzg3NyAxMC40NDk1TDEwLjAyMTkgNS44NjYzMloiIC8+PC9zdmc+" class="anchor-icon" /><span class="copied-indicator docsearch-exclude" aria-live="polite" aria-atomic="true"></span></span></a>

</div>

If you’ve ever stared at a build that’s been running for 30 minutes and wondered whether something went wrong, you know the feeling. That was the reality for a suite of internal configuration build packages our team maintained. P99 build times had crept past 25 minutes — sometimes exceeding 30. With hundreds of packages being built hundreds of thousands of times per month, those minutes were adding up fast.

We needed to figure out why. The usual approach of manually reading through profiling data, cross-referencing it with an unfamiliar codebase, forming a hypothesis, and then implementing a fix could easily take days. We decided to try something different.

<div class="heading-anchor-wrapper">

## Why Kiro CLI?

<a href="#why-kiro-cli" class="anchor-link" aria-label="Copy link to Why kiro cli section"><span class="anchor-icon-wrapper"><img src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iYW5jaG9yLWljb24iIHZpZXdib3g9IjAgMCAxNiAxNyIgd2lkdGg9IjE2IiBoZWlnaHQ9IjE3IiBmaWxsPSJjdXJyZW50Q29sb3IiPjxwYXRoIGQ9Ik0yLjI3MTQzIDE0LjIyOEMwLjU5MTg5NyAxMi41NDg1IDAuNTkxODk3IDkuODI1MzkgMi4yNzE0MyA4LjE0NTg1TDMuNDIzMjQgNi45OTQwNEwzLjQ0MTg4IDYuOTc2MzVDMy42MzgxNiA2Ljc5OSAzLjk0MTE4IDYuODA0ODggNC4xMzAzNSA2Ljk5NDA0QzQuMzE5NTEgNy4xODMyMSA0LjMyNTM5IDcuNDg2MjMgNC4xNDgwNCA3LjY4MjVMNC4xMzAzNSA3LjcwMTE1TDIuOTc4NTQgOC44NTI5NkMxLjY4OTUzIDEwLjE0MiAxLjY4OTUzIDEyLjIzMTkgMi45Nzg1NCAxMy41MjA5TDMuMDA4ODggMTMuNTUwOUM0LjMwMDE0IDE0LjgwOTggNi4zNjc1MSAxNC43OTk4IDcuNjQ2NDYgMTMuNTIwOUw4Ljc5ODI3IDEyLjM2OTFMOC44MTY5MSAxMi4zNTE0QzkuMDEzMTkgMTIuMTc0IDkuMzE2MjEgMTIuMTc5OSA5LjUwNTM4IDEyLjM2OTFDOS42OTQ1NCAxMi41NTgyIDkuNzAwNDYgMTIuODYxMyA5LjUyMzExIDEzLjA1NzZMOS41MDUzOCAxMy4wNzYyTDguMzUzNTYgMTQuMjI4QzYuNjg3MTUgMTUuODk0NCAzLjk5MzQ3IDE1LjkwNzQgMi4zMTEgMTQuMjY3TDIuMjcxNDMgMTQuMjI4Wk0xMy4wMjE1IDMuNDc3OTNDMTEuNzQyNSAyLjE5ODk5IDkuNjc1MTcgMi4xODg5NiA4LjM4MzkgMy40NDc5NEw4LjM1MzU2IDMuNDc3OTNMNy4yMjU3OSA0LjYwNTdDNy4wMzA1MyA0LjgwMDk2IDYuNzEzOTUgNC44MDA5NiA2LjUxODY5IDQuNjA1N0M2LjMyMzQyIDQuNDEwNDQgNi4zMjM0MiA0LjA5Mzg2IDYuNTE4NjkgMy44OTg1OUw3LjY0NjQ2IDIuNzcwODJMNy42ODYwMyAyLjczMTc3QzkuMzY4NSAxLjA5MTM4IDEyLjA2MjIgMS4xMDQ0MSAxMy43Mjg2IDIuNzcwODJMMTMuNzY3NyAyLjgxMDM2QzE1LjM5NTIgNC40Nzk1OCAxNS4zOTUxIDcuMTQ0MTcgMTMuNzY3NyA4LjgxMzM4TDEzLjcyODYgOC44NTI5NkwxMi42MDA4IDkuOTgwNzNDMTIuNDA1NiAxMC4xNzYgMTIuMDg5IDEwLjE3NiAxMS44OTM3IDkuOTgwNzNDMTEuNjk4NSA5Ljc4NTQ3IDExLjY5ODUgOS40Njg4OCAxMS44OTM3IDkuMjczNjJMMTMuMDIxNSA4LjE0NTg1TDEzLjA1MTUgOC4xMTU1MUMxNC4zMDA1IDYuODM0NDIgMTQuMzAwNSA0Ljc4OTM3IDEzLjA1MTUgMy41MDgyN0wxMy4wMjE1IDMuNDc3OTNaIiAvPjxwYXRoIGQ9Ik0xMC4wMjE5IDUuODY2MzJMMTAuMDQwNiA1Ljg0ODU4QzEwLjIzNjkgNS42NzEyNCAxMC41Mzk5IDUuNjc3MTYgMTAuNzI5IDUuODY2MzJDMTAuOTE4MiA2LjA1NTQ4IDEwLjkyNDEgNi4zNTg0NiAxMC43NDY4IDYuNTU0NzRMMTAuNzI5IDYuNTczNDJMNi4xNDU4OCAxMS4xNTY2QzUuOTUwNjIgMTEuMzUxOCA1LjYzNDAzIDExLjM1MTggNS40Mzg3NyAxMS4xNTY2QzUuMjQzNTEgMTAuOTYxMyA1LjI0MzUxIDEwLjY0NDcgNS40Mzg3NyAxMC40NDk1TDEwLjAyMTkgNS44NjYzMloiIC8+PC9zdmc+" class="anchor-icon" /><span class="copied-indicator docsearch-exclude" aria-live="polite" aria-atomic="true"></span></span></a>

</div>

We’d been using Kiro CLI for a while, and this felt like the kind of task it was built for. This wasn’t a simple code generation job but a complex, open-ended investigation. We needed an agent that could reason across multiple files, interpret profiling output, and connect the dots between runtime behavior and source code.

Tools purpose-built for code generation are great at what they do, but for root cause analysis across an unfamiliar codebase, we wanted a more generalist agent. Kiro CLI was the right call.

<div class="heading-anchor-wrapper">

## Kiro in action: from profiling data to fix in 33 seconds

<a href="#kiro-in-action-from-profiling-data-to-fix-in-33-seconds" class="anchor-link" aria-label="Copy link to Kiro in action from profiling data to fix in 33 seconds section"><span class="anchor-icon-wrapper"><img src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iYW5jaG9yLWljb24iIHZpZXdib3g9IjAgMCAxNiAxNyIgd2lkdGg9IjE2IiBoZWlnaHQ9IjE3IiBmaWxsPSJjdXJyZW50Q29sb3IiPjxwYXRoIGQ9Ik0yLjI3MTQzIDE0LjIyOEMwLjU5MTg5NyAxMi41NDg1IDAuNTkxODk3IDkuODI1MzkgMi4yNzE0MyA4LjE0NTg1TDMuNDIzMjQgNi45OTQwNEwzLjQ0MTg4IDYuOTc2MzVDMy42MzgxNiA2Ljc5OSAzLjk0MTE4IDYuODA0ODggNC4xMzAzNSA2Ljk5NDA0QzQuMzE5NTEgNy4xODMyMSA0LjMyNTM5IDcuNDg2MjMgNC4xNDgwNCA3LjY4MjVMNC4xMzAzNSA3LjcwMTE1TDIuOTc4NTQgOC44NTI5NkMxLjY4OTUzIDEwLjE0MiAxLjY4OTUzIDEyLjIzMTkgMi45Nzg1NCAxMy41MjA5TDMuMDA4ODggMTMuNTUwOUM0LjMwMDE0IDE0LjgwOTggNi4zNjc1MSAxNC43OTk4IDcuNjQ2NDYgMTMuNTIwOUw4Ljc5ODI3IDEyLjM2OTFMOC44MTY5MSAxMi4zNTE0QzkuMDEzMTkgMTIuMTc0IDkuMzE2MjEgMTIuMTc5OSA5LjUwNTM4IDEyLjM2OTFDOS42OTQ1NCAxMi41NTgyIDkuNzAwNDYgMTIuODYxMyA5LjUyMzExIDEzLjA1NzZMOS41MDUzOCAxMy4wNzYyTDguMzUzNTYgMTQuMjI4QzYuNjg3MTUgMTUuODk0NCAzLjk5MzQ3IDE1LjkwNzQgMi4zMTEgMTQuMjY3TDIuMjcxNDMgMTQuMjI4Wk0xMy4wMjE1IDMuNDc3OTNDMTEuNzQyNSAyLjE5ODk5IDkuNjc1MTcgMi4xODg5NiA4LjM4MzkgMy40NDc5NEw4LjM1MzU2IDMuNDc3OTNMNy4yMjU3OSA0LjYwNTdDNy4wMzA1MyA0LjgwMDk2IDYuNzEzOTUgNC44MDA5NiA2LjUxODY5IDQuNjA1N0M2LjMyMzQyIDQuNDEwNDQgNi4zMjM0MiA0LjA5Mzg2IDYuNTE4NjkgMy44OTg1OUw3LjY0NjQ2IDIuNzcwODJMNy42ODYwMyAyLjczMTc3QzkuMzY4NSAxLjA5MTM4IDEyLjA2MjIgMS4xMDQ0MSAxMy43Mjg2IDIuNzcwODJMMTMuNzY3NyAyLjgxMDM2QzE1LjM5NTIgNC40Nzk1OCAxNS4zOTUxIDcuMTQ0MTcgMTMuNzY3NyA4LjgxMzM4TDEzLjcyODYgOC44NTI5NkwxMi42MDA4IDkuOTgwNzNDMTIuNDA1NiAxMC4xNzYgMTIuMDg5IDEwLjE3NiAxMS44OTM3IDkuOTgwNzNDMTEuNjk4NSA5Ljc4NTQ3IDExLjY5ODUgOS40Njg4OCAxMS44OTM3IDkuMjczNjJMMTMuMDIxNSA4LjE0NTg1TDEzLjA1MTUgOC4xMTU1MUMxNC4zMDA1IDYuODM0NDIgMTQuMzAwNSA0Ljc4OTM3IDEzLjA1MTUgMy41MDgyN0wxMy4wMjE1IDMuNDc3OTNaIiAvPjxwYXRoIGQ9Ik0xMC4wMjE5IDUuODY2MzJMMTAuMDQwNiA1Ljg0ODU4QzEwLjIzNjkgNS42NzEyNCAxMC41Mzk5IDUuNjc3MTYgMTAuNzI5IDUuODY2MzJDMTAuOTE4MiA2LjA1NTQ4IDEwLjkyNDEgNi4zNTg0NiAxMC43NDY4IDYuNTU0NzRMMTAuNzI5IDYuNTczNDJMNi4xNDU4OCAxMS4xNTY2QzUuOTUwNjIgMTEuMzUxOCA1LjYzNDAzIDExLjM1MTggNS40Mzg3NyAxMS4xNTY2QzUuMjQzNTEgMTAuOTYxMyA1LjI0MzUxIDEwLjY0NDcgNS40Mzg3NyAxMC40NDk1TDEwLjAyMTkgNS44NjYzMloiIC8+PC9zdmc+" class="anchor-icon" /><span class="copied-indicator docsearch-exclude" aria-live="polite" aria-atomic="true"></span></span></a>

</div>

We started by capturing performance data using `perf` and reformatting it into a clear, structured format. (More on that in the lessons section — this step matters.) Then we gave Kiro a single prompt:

<div class="promptBox">

<div class="my-6 rounded-md bg-muted-foreground/10 p-4">

Loading code example...

</div>

</div>

What followed was a fully autonomous investigation.

The profiling data told a clear story once you knew how to read it. The call tree showed that the config file parser was consuming a massive share of CPU time — nearly 80% of the execution path traced back through the parser’s core routines:

<div class="my-6 rounded-md bg-muted-foreground/10 p-4">

Loading code example...

</div>

Kiro read this output, mapped it against the configuration build tool’s source code, and identified the culprit: the config parser was being **re-initialized on every single function call** across multiple subroutines. Each call spun up a brand new parser instance, re-reading and re-parsing the same config files from disk every time.

The fix was elegant: introduce a shared cache keyed on the relevant config parameters. Parse once, reuse everywhere.

<div class="heading-anchor-wrapper">

### The tools that made it possible

<a href="#the-tools-that-made-it-possible" class="anchor-link" aria-label="Copy link to The tools that made it possible section"><span class="anchor-icon-wrapper"><img src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iYW5jaG9yLWljb24iIHZpZXdib3g9IjAgMCAxNiAxNyIgd2lkdGg9IjE2IiBoZWlnaHQ9IjE3IiBmaWxsPSJjdXJyZW50Q29sb3IiPjxwYXRoIGQ9Ik0yLjI3MTQzIDE0LjIyOEMwLjU5MTg5NyAxMi41NDg1IDAuNTkxODk3IDkuODI1MzkgMi4yNzE0MyA4LjE0NTg1TDMuNDIzMjQgNi45OTQwNEwzLjQ0MTg4IDYuOTc2MzVDMy42MzgxNiA2Ljc5OSAzLjk0MTE4IDYuODA0ODggNC4xMzAzNSA2Ljk5NDA0QzQuMzE5NTEgNy4xODMyMSA0LjMyNTM5IDcuNDg2MjMgNC4xNDgwNCA3LjY4MjVMNC4xMzAzNSA3LjcwMTE1TDIuOTc4NTQgOC44NTI5NkMxLjY4OTUzIDEwLjE0MiAxLjY4OTUzIDEyLjIzMTkgMi45Nzg1NCAxMy41MjA5TDMuMDA4ODggMTMuNTUwOUM0LjMwMDE0IDE0LjgwOTggNi4zNjc1MSAxNC43OTk4IDcuNjQ2NDYgMTMuNTIwOUw4Ljc5ODI3IDEyLjM2OTFMOC44MTY5MSAxMi4zNTE0QzkuMDEzMTkgMTIuMTc0IDkuMzE2MjEgMTIuMTc5OSA5LjUwNTM4IDEyLjM2OTFDOS42OTQ1NCAxMi41NTgyIDkuNzAwNDYgMTIuODYxMyA5LjUyMzExIDEzLjA1NzZMOS41MDUzOCAxMy4wNzYyTDguMzUzNTYgMTQuMjI4QzYuNjg3MTUgMTUuODk0NCAzLjk5MzQ3IDE1LjkwNzQgMi4zMTEgMTQuMjY3TDIuMjcxNDMgMTQuMjI4Wk0xMy4wMjE1IDMuNDc3OTNDMTEuNzQyNSAyLjE5ODk5IDkuNjc1MTcgMi4xODg5NiA4LjM4MzkgMy40NDc5NEw4LjM1MzU2IDMuNDc3OTNMNy4yMjU3OSA0LjYwNTdDNy4wMzA1MyA0LjgwMDk2IDYuNzEzOTUgNC44MDA5NiA2LjUxODY5IDQuNjA1N0M2LjMyMzQyIDQuNDEwNDQgNi4zMjM0MiA0LjA5Mzg2IDYuNTE4NjkgMy44OTg1OUw3LjY0NjQ2IDIuNzcwODJMNy42ODYwMyAyLjczMTc3QzkuMzY4NSAxLjA5MTM4IDEyLjA2MjIgMS4xMDQ0MSAxMy43Mjg2IDIuNzcwODJMMTMuNzY3NyAyLjgxMDM2QzE1LjM5NTIgNC40Nzk1OCAxNS4zOTUxIDcuMTQ0MTcgMTMuNzY3NyA4LjgxMzM4TDEzLjcyODYgOC44NTI5NkwxMi42MDA4IDkuOTgwNzNDMTIuNDA1NiAxMC4xNzYgMTIuMDg5IDEwLjE3NiAxMS44OTM3IDkuOTgwNzNDMTEuNjk4NSA5Ljc4NTQ3IDExLjY5ODUgOS40Njg4OCAxMS44OTM3IDkuMjczNjJMMTMuMDIxNSA4LjE0NTg1TDEzLjA1MTUgOC4xMTU1MUMxNC4zMDA1IDYuODM0NDIgMTQuMzAwNSA0Ljc4OTM3IDEzLjA1MTUgMy41MDgyN0wxMy4wMjE1IDMuNDc3OTNaIiAvPjxwYXRoIGQ9Ik0xMC4wMjE5IDUuODY2MzJMMTAuMDQwNiA1Ljg0ODU4QzEwLjIzNjkgNS42NzEyNCAxMC41Mzk5IDUuNjc3MTYgMTAuNzI5IDUuODY2MzJDMTAuOTE4MiA2LjA1NTQ4IDEwLjkyNDEgNi4zNTg0NiAxMC43NDY4IDYuNTU0NzRMMTAuNzI5IDYuNTczNDJMNi4xNDU4OCAxMS4xNTY2QzUuOTUwNjIgMTEuMzUxOCA1LjYzNDAzIDExLjM1MTggNS40Mzg3NyAxMS4xNTY2QzUuMjQzNTEgMTAuOTYxMyA1LjI0MzUxIDEwLjY0NDcgNS40Mzg3NyAxMC40NDk1TDEwLjAyMTkgNS44NjYzMloiIC8+PC9zdmc+" class="anchor-icon" /><span class="copied-indicator docsearch-exclude" aria-live="polite" aria-atomic="true"></span></span></a>

</div>

The investigation relied on a few key capabilities:

- **Code intelligence tools** (`generate_codebase_overview`, `search_codebase_map`) for understanding unfamiliar codebases quickly
- **File system tools** (`fs_read`, `fs_write`, `glob`) for reading profiling data, inspecting source code, and implementing changes
- **Subagent delegation** (`use_subagent`) for offloading focused analysis tasks without polluting the main context

<div class="heading-anchor-wrapper">

## Under the hood: how Kiro investigated the problem

<a href="#under-the-hood-how-kiro-investigated-the-problem" class="anchor-link" aria-label="Copy link to Under the hood how kiro investigated the problem section"><span class="anchor-icon-wrapper"><img src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iYW5jaG9yLWljb24iIHZpZXdib3g9IjAgMCAxNiAxNyIgd2lkdGg9IjE2IiBoZWlnaHQ9IjE3IiBmaWxsPSJjdXJyZW50Q29sb3IiPjxwYXRoIGQ9Ik0yLjI3MTQzIDE0LjIyOEMwLjU5MTg5NyAxMi41NDg1IDAuNTkxODk3IDkuODI1MzkgMi4yNzE0MyA4LjE0NTg1TDMuNDIzMjQgNi45OTQwNEwzLjQ0MTg4IDYuOTc2MzVDMy42MzgxNiA2Ljc5OSAzLjk0MTE4IDYuODA0ODggNC4xMzAzNSA2Ljk5NDA0QzQuMzE5NTEgNy4xODMyMSA0LjMyNTM5IDcuNDg2MjMgNC4xNDgwNCA3LjY4MjVMNC4xMzAzNSA3LjcwMTE1TDIuOTc4NTQgOC44NTI5NkMxLjY4OTUzIDEwLjE0MiAxLjY4OTUzIDEyLjIzMTkgMi45Nzg1NCAxMy41MjA5TDMuMDA4ODggMTMuNTUwOUM0LjMwMDE0IDE0LjgwOTggNi4zNjc1MSAxNC43OTk4IDcuNjQ2NDYgMTMuNTIwOUw4Ljc5ODI3IDEyLjM2OTFMOC44MTY5MSAxMi4zNTE0QzkuMDEzMTkgMTIuMTc0IDkuMzE2MjEgMTIuMTc5OSA5LjUwNTM4IDEyLjM2OTFDOS42OTQ1NCAxMi41NTgyIDkuNzAwNDYgMTIuODYxMyA5LjUyMzExIDEzLjA1NzZMOS41MDUzOCAxMy4wNzYyTDguMzUzNTYgMTQuMjI4QzYuNjg3MTUgMTUuODk0NCAzLjk5MzQ3IDE1LjkwNzQgMi4zMTEgMTQuMjY3TDIuMjcxNDMgMTQuMjI4Wk0xMy4wMjE1IDMuNDc3OTNDMTEuNzQyNSAyLjE5ODk5IDkuNjc1MTcgMi4xODg5NiA4LjM4MzkgMy40NDc5NEw4LjM1MzU2IDMuNDc3OTNMNy4yMjU3OSA0LjYwNTdDNy4wMzA1MyA0LjgwMDk2IDYuNzEzOTUgNC44MDA5NiA2LjUxODY5IDQuNjA1N0M2LjMyMzQyIDQuNDEwNDQgNi4zMjM0MiA0LjA5Mzg2IDYuNTE4NjkgMy44OTg1OUw3LjY0NjQ2IDIuNzcwODJMNy42ODYwMyAyLjczMTc3QzkuMzY4NSAxLjA5MTM4IDEyLjA2MjIgMS4xMDQ0MSAxMy43Mjg2IDIuNzcwODJMMTMuNzY3NyAyLjgxMDM2QzE1LjM5NTIgNC40Nzk1OCAxNS4zOTUxIDcuMTQ0MTcgMTMuNzY3NyA4LjgxMzM4TDEzLjcyODYgOC44NTI5NkwxMi42MDA4IDkuOTgwNzNDMTIuNDA1NiAxMC4xNzYgMTIuMDg5IDEwLjE3NiAxMS44OTM3IDkuOTgwNzNDMTEuNjk4NSA5Ljc4NTQ3IDExLjY5ODUgOS40Njg4OCAxMS44OTM3IDkuMjczNjJMMTMuMDIxNSA4LjE0NTg1TDEzLjA1MTUgOC4xMTU1MUMxNC4zMDA1IDYuODM0NDIgMTQuMzAwNSA0Ljc4OTM3IDEzLjA1MTUgMy41MDgyN0wxMy4wMjE1IDMuNDc3OTNaIiAvPjxwYXRoIGQ9Ik0xMC4wMjE5IDUuODY2MzJMMTAuMDQwNiA1Ljg0ODU4QzEwLjIzNjkgNS42NzEyNCAxMC41Mzk5IDUuNjc3MTYgMTAuNzI5IDUuODY2MzJDMTAuOTE4MiA2LjA1NTQ4IDEwLjkyNDEgNi4zNTg0NiAxMC43NDY4IDYuNTU0NzRMMTAuNzI5IDYuNTczNDJMNi4xNDU4OCAxMS4xNTY2QzUuOTUwNjIgMTEuMzUxOCA1LjYzNDAzIDExLjM1MTggNS40Mzg3NyAxMS4xNTY2QzUuMjQzNTEgMTAuOTYxMyA1LjI0MzUxIDEwLjY0NDcgNS40Mzg3NyAxMC40NDk1TDEwLjAyMTkgNS44NjYzMloiIC8+PC9zdmc+" class="anchor-icon" /><span class="copied-indicator docsearch-exclude" aria-live="polite" aria-atomic="true"></span></span></a>

</div>

To understand what made this investigation so fast, it’s worth looking at how Kiro actually worked through the problem. Over the course of 10 autonomous turns, Kiro used a combination of code intelligence and file system tools to navigate an unfamiliar codebase, correlate profiling data with source code, and implement a fix.

<div class="heading-anchor-wrapper">

### Understanding the codebase structure

<a href="#understanding-the-codebase-structure" class="anchor-link" aria-label="Copy link to Understanding the codebase structure section"><span class="anchor-icon-wrapper"><img src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iYW5jaG9yLWljb24iIHZpZXdib3g9IjAgMCAxNiAxNyIgd2lkdGg9IjE2IiBoZWlnaHQ9IjE3IiBmaWxsPSJjdXJyZW50Q29sb3IiPjxwYXRoIGQ9Ik0yLjI3MTQzIDE0LjIyOEMwLjU5MTg5NyAxMi41NDg1IDAuNTkxODk3IDkuODI1MzkgMi4yNzE0MyA4LjE0NTg1TDMuNDIzMjQgNi45OTQwNEwzLjQ0MTg4IDYuOTc2MzVDMy42MzgxNiA2Ljc5OSAzLjk0MTE4IDYuODA0ODggNC4xMzAzNSA2Ljk5NDA0QzQuMzE5NTEgNy4xODMyMSA0LjMyNTM5IDcuNDg2MjMgNC4xNDgwNCA3LjY4MjVMNC4xMzAzNSA3LjcwMTE1TDIuOTc4NTQgOC44NTI5NkMxLjY4OTUzIDEwLjE0MiAxLjY4OTUzIDEyLjIzMTkgMi45Nzg1NCAxMy41MjA5TDMuMDA4ODggMTMuNTUwOUM0LjMwMDE0IDE0LjgwOTggNi4zNjc1MSAxNC43OTk4IDcuNjQ2NDYgMTMuNTIwOUw4Ljc5ODI3IDEyLjM2OTFMOC44MTY5MSAxMi4zNTE0QzkuMDEzMTkgMTIuMTc0IDkuMzE2MjEgMTIuMTc5OSA5LjUwNTM4IDEyLjM2OTFDOS42OTQ1NCAxMi41NTgyIDkuNzAwNDYgMTIuODYxMyA5LjUyMzExIDEzLjA1NzZMOS41MDUzOCAxMy4wNzYyTDguMzUzNTYgMTQuMjI4QzYuNjg3MTUgMTUuODk0NCAzLjk5MzQ3IDE1LjkwNzQgMi4zMTEgMTQuMjY3TDIuMjcxNDMgMTQuMjI4Wk0xMy4wMjE1IDMuNDc3OTNDMTEuNzQyNSAyLjE5ODk5IDkuNjc1MTcgMi4xODg5NiA4LjM4MzkgMy40NDc5NEw4LjM1MzU2IDMuNDc3OTNMNy4yMjU3OSA0LjYwNTdDNy4wMzA1MyA0LjgwMDk2IDYuNzEzOTUgNC44MDA5NiA2LjUxODY5IDQuNjA1N0M2LjMyMzQyIDQuNDEwNDQgNi4zMjM0MiA0LjA5Mzg2IDYuNTE4NjkgMy44OTg1OUw3LjY0NjQ2IDIuNzcwODJMNy42ODYwMyAyLjczMTc3QzkuMzY4NSAxLjA5MTM4IDEyLjA2MjIgMS4xMDQ0MSAxMy43Mjg2IDIuNzcwODJMMTMuNzY3NyAyLjgxMDM2QzE1LjM5NTIgNC40Nzk1OCAxNS4zOTUxIDcuMTQ0MTcgMTMuNzY3NyA4LjgxMzM4TDEzLjcyODYgOC44NTI5NkwxMi42MDA4IDkuOTgwNzNDMTIuNDA1NiAxMC4xNzYgMTIuMDg5IDEwLjE3NiAxMS44OTM3IDkuOTgwNzNDMTEuNjk4NSA5Ljc4NTQ3IDExLjY5ODUgOS40Njg4OCAxMS44OTM3IDkuMjczNjJMMTMuMDIxNSA4LjE0NTg1TDEzLjA1MTUgOC4xMTU1MUMxNC4zMDA1IDYuODM0NDIgMTQuMzAwNSA0Ljc4OTM3IDEzLjA1MTUgMy41MDgyN0wxMy4wMjE1IDMuNDc3OTNaIiAvPjxwYXRoIGQ9Ik0xMC4wMjE5IDUuODY2MzJMMTAuMDQwNiA1Ljg0ODU4QzEwLjIzNjkgNS42NzEyNCAxMC41Mzk5IDUuNjc3MTYgMTAuNzI5IDUuODY2MzJDMTAuOTE4MiA2LjA1NTQ4IDEwLjkyNDEgNi4zNTg0NiAxMC43NDY4IDYuNTU0NzRMMTAuNzI5IDYuNTczNDJMNi4xNDU4OCAxMS4xNTY2QzUuOTUwNjIgMTEuMzUxOCA1LjYzNDAzIDExLjM1MTggNS40Mzg3NyAxMS4xNTY2QzUuMjQzNTEgMTAuOTYxMyA1LjI0MzUxIDEwLjY0NDcgNS40Mzg3NyAxMC40NDk1TDEwLjAyMTkgNS44NjYzMloiIC8+PC9zdmc+" class="anchor-icon" /><span class="copied-indicator docsearch-exclude" aria-live="polite" aria-atomic="true"></span></span></a>

</div>

Kiro started by getting oriented. It used `generate_codebase_overview` to build a high-level map of the repository structure, followed by `search_codebase_map` to identify key directories and packages. These tools gave Kiro a mental model of the project layout without having to read every file.

Then it used `fs_read` in Directory mode to list the contents of the target directory, confirming the presence of the performance report file.

**Why this matters:** Before diving into profiling data, Kiro needed to understand what it was working with. These reconnaissance tools let it build context efficiently, the same way an engineer would skim a README and browse the file tree before digging into code.

<div class="heading-anchor-wrapper">

### Reading and interpreting the profiling data

<a href="#reading-and-interpreting-the-profiling-data" class="anchor-link" aria-label="Copy link to Reading and interpreting the profiling data section"><span class="anchor-icon-wrapper"><img src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iYW5jaG9yLWljb24iIHZpZXdib3g9IjAgMCAxNiAxNyIgd2lkdGg9IjE2IiBoZWlnaHQ9IjE3IiBmaWxsPSJjdXJyZW50Q29sb3IiPjxwYXRoIGQ9Ik0yLjI3MTQzIDE0LjIyOEMwLjU5MTg5NyAxMi41NDg1IDAuNTkxODk3IDkuODI1MzkgMi4yNzE0MyA4LjE0NTg1TDMuNDIzMjQgNi45OTQwNEwzLjQ0MTg4IDYuOTc2MzVDMy42MzgxNiA2Ljc5OSAzLjk0MTE4IDYuODA0ODggNC4xMzAzNSA2Ljk5NDA0QzQuMzE5NTEgNy4xODMyMSA0LjMyNTM5IDcuNDg2MjMgNC4xNDgwNCA3LjY4MjVMNC4xMzAzNSA3LjcwMTE1TDIuOTc4NTQgOC44NTI5NkMxLjY4OTUzIDEwLjE0MiAxLjY4OTUzIDEyLjIzMTkgMi45Nzg1NCAxMy41MjA5TDMuMDA4ODggMTMuNTUwOUM0LjMwMDE0IDE0LjgwOTggNi4zNjc1MSAxNC43OTk4IDcuNjQ2NDYgMTMuNTIwOUw4Ljc5ODI3IDEyLjM2OTFMOC44MTY5MSAxMi4zNTE0QzkuMDEzMTkgMTIuMTc0IDkuMzE2MjEgMTIuMTc5OSA5LjUwNTM4IDEyLjM2OTFDOS42OTQ1NCAxMi41NTgyIDkuNzAwNDYgMTIuODYxMyA5LjUyMzExIDEzLjA1NzZMOS41MDUzOCAxMy4wNzYyTDguMzUzNTYgMTQuMjI4QzYuNjg3MTUgMTUuODk0NCAzLjk5MzQ3IDE1LjkwNzQgMi4zMTEgMTQuMjY3TDIuMjcxNDMgMTQuMjI4Wk0xMy4wMjE1IDMuNDc3OTNDMTEuNzQyNSAyLjE5ODk5IDkuNjc1MTcgMi4xODg5NiA4LjM4MzkgMy40NDc5NEw4LjM1MzU2IDMuNDc3OTNMNy4yMjU3OSA0LjYwNTdDNy4wMzA1MyA0LjgwMDk2IDYuNzEzOTUgNC44MDA5NiA2LjUxODY5IDQuNjA1N0M2LjMyMzQyIDQuNDEwNDQgNi4zMjM0MiA0LjA5Mzg2IDYuNTE4NjkgMy44OTg1OUw3LjY0NjQ2IDIuNzcwODJMNy42ODYwMyAyLjczMTc3QzkuMzY4NSAxLjA5MTM4IDEyLjA2MjIgMS4xMDQ0MSAxMy43Mjg2IDIuNzcwODJMMTMuNzY3NyAyLjgxMDM2QzE1LjM5NTIgNC40Nzk1OCAxNS4zOTUxIDcuMTQ0MTcgMTMuNzY3NyA4LjgxMzM4TDEzLjcyODYgOC44NTI5NkwxMi42MDA4IDkuOTgwNzNDMTIuNDA1NiAxMC4xNzYgMTIuMDg5IDEwLjE3NiAxMS44OTM3IDkuOTgwNzNDMTEuNjk4NSA5Ljc4NTQ3IDExLjY5ODUgOS40Njg4OCAxMS44OTM3IDkuMjczNjJMMTMuMDIxNSA4LjE0NTg1TDEzLjA1MTUgOC4xMTU1MUMxNC4zMDA1IDYuODM0NDIgMTQuMzAwNSA0Ljc4OTM3IDEzLjA1MTUgMy41MDgyN0wxMy4wMjE1IDMuNDc3OTNaIiAvPjxwYXRoIGQ9Ik0xMC4wMjE5IDUuODY2MzJMMTAuMDQwNiA1Ljg0ODU4QzEwLjIzNjkgNS42NzEyNCAxMC41Mzk5IDUuNjc3MTYgMTAuNzI5IDUuODY2MzJDMTAuOTE4MiA2LjA1NTQ4IDEwLjkyNDEgNi4zNTg0NiAxMC43NDY4IDYuNTU0NzRMMTAuNzI5IDYuNTczNDJMNi4xNDU4OCAxMS4xNTY2QzUuOTUwNjIgMTEuMzUxOCA1LjYzNDAzIDExLjM1MTggNS40Mzg3NyAxMS4xNTY2QzUuMjQzNTEgMTAuOTYxMyA1LjI0MzUxIDEwLjY0NDcgNS40Mzg3NyAxMC40NDk1TDEwLjAyMTkgNS44NjYzMloiIC8+PC9zdmc+" class="anchor-icon" /><span class="copied-indicator docsearch-exclude" aria-live="polite" aria-atomic="true"></span></span></a>

</div>

Next, Kiro read the profiling report file using `fs_read` in Line mode.

The profiling data showed that 79.41% of CPU time was spent in the parser’s core function, with significant overhead in token parsing and I/O operations. This was the smoking gun, but Kiro still needed to figure out *why* the parser was consuming so much time.

**Why this matters:** Profiling data is dense and hard to interpret. Kiro didn’t just read the file but the entire call tree, identified the hottest code paths, and connected them to specific function names. This is where a generalist agent shines: it can reason about structured data formats like `perf` output without needing a specialized parser.

<div class="heading-anchor-wrapper">

### Delegating code analysis to a specialized subagent

<a href="#delegating-code-analysis-to-a-specialized-subagent" class="anchor-link" aria-label="Copy link to Delegating code analysis to a specialized subagent section"><span class="anchor-icon-wrapper"><img src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iYW5jaG9yLWljb24iIHZpZXdib3g9IjAgMCAxNiAxNyIgd2lkdGg9IjE2IiBoZWlnaHQ9IjE3IiBmaWxsPSJjdXJyZW50Q29sb3IiPjxwYXRoIGQ9Ik0yLjI3MTQzIDE0LjIyOEMwLjU5MTg5NyAxMi41NDg1IDAuNTkxODk3IDkuODI1MzkgMi4yNzE0MyA4LjE0NTg1TDMuNDIzMjQgNi45OTQwNEwzLjQ0MTg4IDYuOTc2MzVDMy42MzgxNiA2Ljc5OSAzLjk0MTE4IDYuODA0ODggNC4xMzAzNSA2Ljk5NDA0QzQuMzE5NTEgNy4xODMyMSA0LjMyNTM5IDcuNDg2MjMgNC4xNDgwNCA3LjY4MjVMNC4xMzAzNSA3LjcwMTE1TDIuOTc4NTQgOC44NTI5NkMxLjY4OTUzIDEwLjE0MiAxLjY4OTUzIDEyLjIzMTkgMi45Nzg1NCAxMy41MjA5TDMuMDA4ODggMTMuNTUwOUM0LjMwMDE0IDE0LjgwOTggNi4zNjc1MSAxNC43OTk4IDcuNjQ2NDYgMTMuNTIwOUw4Ljc5ODI3IDEyLjM2OTFMOC44MTY5MSAxMi4zNTE0QzkuMDEzMTkgMTIuMTc0IDkuMzE2MjEgMTIuMTc5OSA5LjUwNTM4IDEyLjM2OTFDOS42OTQ1NCAxMi41NTgyIDkuNzAwNDYgMTIuODYxMyA5LjUyMzExIDEzLjA1NzZMOS41MDUzOCAxMy4wNzYyTDguMzUzNTYgMTQuMjI4QzYuNjg3MTUgMTUuODk0NCAzLjk5MzQ3IDE1LjkwNzQgMi4zMTEgMTQuMjY3TDIuMjcxNDMgMTQuMjI4Wk0xMy4wMjE1IDMuNDc3OTNDMTEuNzQyNSAyLjE5ODk5IDkuNjc1MTcgMi4xODg5NiA4LjM4MzkgMy40NDc5NEw4LjM1MzU2IDMuNDc3OTNMNy4yMjU3OSA0LjYwNTdDNy4wMzA1MyA0LjgwMDk2IDYuNzEzOTUgNC44MDA5NiA2LjUxODY5IDQuNjA1N0M2LjMyMzQyIDQuNDEwNDQgNi4zMjM0MiA0LjA5Mzg2IDYuNTE4NjkgMy44OTg1OUw3LjY0NjQ2IDIuNzcwODJMNy42ODYwMyAyLjczMTc3QzkuMzY4NSAxLjA5MTM4IDEyLjA2MjIgMS4xMDQ0MSAxMy43Mjg2IDIuNzcwODJMMTMuNzY3NyAyLjgxMDM2QzE1LjM5NTIgNC40Nzk1OCAxNS4zOTUxIDcuMTQ0MTcgMTMuNzY3NyA4LjgxMzM4TDEzLjcyODYgOC44NTI5NkwxMi42MDA4IDkuOTgwNzNDMTIuNDA1NiAxMC4xNzYgMTIuMDg5IDEwLjE3NiAxMS44OTM3IDkuOTgwNzNDMTEuNjk4NSA5Ljc4NTQ3IDExLjY5ODUgOS40Njg4OCAxMS44OTM3IDkuMjczNjJMMTMuMDIxNSA4LjE0NTg1TDEzLjA1MTUgOC4xMTU1MUMxNC4zMDA1IDYuODM0NDIgMTQuMzAwNSA0Ljc4OTM3IDEzLjA1MTUgMy41MDgyN0wxMy4wMjE1IDMuNDc3OTNaIiAvPjxwYXRoIGQ9Ik0xMC4wMjE5IDUuODY2MzJMMTAuMDQwNiA1Ljg0ODU4QzEwLjIzNjkgNS42NzEyNCAxMC41Mzk5IDUuNjc3MTYgMTAuNzI5IDUuODY2MzJDMTAuOTE4MiA2LjA1NTQ4IDEwLjkyNDEgNi4zNTg0NiAxMC43NDY4IDYuNTU0NzRMMTAuNzI5IDYuNTczNDJMNi4xNDU4OCAxMS4xNTY2QzUuOTUwNjIgMTEuMzUxOCA1LjYzNDAzIDExLjM1MTggNS40Mzg3NyAxMS4xNTY2QzUuMjQzNTEgMTAuOTYxMyA1LjI0MzUxIDEwLjY0NDcgNS40Mzg3NyAxMC40NDk1TDEwLjAyMTkgNS44NjYzMloiIC8+PC9zdmc+" class="anchor-icon" /><span class="copied-indicator docsearch-exclude" aria-live="polite" aria-atomic="true"></span></span></a>

</div>

At this point, Kiro had identified the bottleneck (the config parser) but needed to locate where in the codebase the parser was being instantiated. Kiro delegated this task to a specialized **code-analyzer agent** using `use_subagent`.

The subagent was given a focused query: "Identify build tool package locations where we can implement performance optimizations based on perf data analysis."

**Why this matters:** This is one of Kiro’s most powerful features. By delegating to a specialized subagent, Kiro kept its own context clean while offloading a focused subtask to an agent optimized for code analysis. The subagent ran in parallel, analyzed the codebase, and returned results — all without cluttering the main conversation.

<div class="heading-anchor-wrapper">

### Locating the problematic code

<a href="#locating-the-problematic-code" class="anchor-link" aria-label="Copy link to Locating the problematic code section"><span class="anchor-icon-wrapper"><img src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iYW5jaG9yLWljb24iIHZpZXdib3g9IjAgMCAxNiAxNyIgd2lkdGg9IjE2IiBoZWlnaHQ9IjE3IiBmaWxsPSJjdXJyZW50Q29sb3IiPjxwYXRoIGQ9Ik0yLjI3MTQzIDE0LjIyOEMwLjU5MTg5NyAxMi41NDg1IDAuNTkxODk3IDkuODI1MzkgMi4yNzE0MyA4LjE0NTg1TDMuNDIzMjQgNi45OTQwNEwzLjQ0MTg4IDYuOTc2MzVDMy42MzgxNiA2Ljc5OSAzLjk0MTE4IDYuODA0ODggNC4xMzAzNSA2Ljk5NDA0QzQuMzE5NTEgNy4xODMyMSA0LjMyNTM5IDcuNDg2MjMgNC4xNDgwNCA3LjY4MjVMNC4xMzAzNSA3LjcwMTE1TDIuOTc4NTQgOC44NTI5NkMxLjY4OTUzIDEwLjE0MiAxLjY4OTUzIDEyLjIzMTkgMi45Nzg1NCAxMy41MjA5TDMuMDA4ODggMTMuNTUwOUM0LjMwMDE0IDE0LjgwOTggNi4zNjc1MSAxNC43OTk4IDcuNjQ2NDYgMTMuNTIwOUw4Ljc5ODI3IDEyLjM2OTFMOC44MTY5MSAxMi4zNTE0QzkuMDEzMTkgMTIuMTc0IDkuMzE2MjEgMTIuMTc5OSA5LjUwNTM4IDEyLjM2OTFDOS42OTQ1NCAxMi41NTgyIDkuNzAwNDYgMTIuODYxMyA5LjUyMzExIDEzLjA1NzZMOS41MDUzOCAxMy4wNzYyTDguMzUzNTYgMTQuMjI4QzYuNjg3MTUgMTUuODk0NCAzLjk5MzQ3IDE1LjkwNzQgMi4zMTEgMTQuMjY3TDIuMjcxNDMgMTQuMjI4Wk0xMy4wMjE1IDMuNDc3OTNDMTEuNzQyNSAyLjE5ODk5IDkuNjc1MTcgMi4xODg5NiA4LjM4MzkgMy40NDc5NEw4LjM1MzU2IDMuNDc3OTNMNy4yMjU3OSA0LjYwNTdDNy4wMzA1MyA0LjgwMDk2IDYuNzEzOTUgNC44MDA5NiA2LjUxODY5IDQuNjA1N0M2LjMyMzQyIDQuNDEwNDQgNi4zMjM0MiA0LjA5Mzg2IDYuNTE4NjkgMy44OTg1OUw3LjY0NjQ2IDIuNzcwODJMNy42ODYwMyAyLjczMTc3QzkuMzY4NSAxLjA5MTM4IDEyLjA2MjIgMS4xMDQ0MSAxMy43Mjg2IDIuNzcwODJMMTMuNzY3NyAyLjgxMDM2QzE1LjM5NTIgNC40Nzk1OCAxNS4zOTUxIDcuMTQ0MTcgMTMuNzY3NyA4LjgxMzM4TDEzLjcyODYgOC44NTI5NkwxMi42MDA4IDkuOTgwNzNDMTIuNDA1NiAxMC4xNzYgMTIuMDg5IDEwLjE3NiAxMS44OTM3IDkuOTgwNzNDMTEuNjk4NSA5Ljc4NTQ3IDExLjY5ODUgOS40Njg4OCAxMS44OTM3IDkuMjczNjJMMTMuMDIxNSA4LjE0NTg1TDEzLjA1MTUgOC4xMTU1MUMxNC4zMDA1IDYuODM0NDIgMTQuMzAwNSA0Ljc4OTM3IDEzLjA1MTUgMy41MDgyN0wxMy4wMjE1IDMuNDc3OTNaIiAvPjxwYXRoIGQ9Ik0xMC4wMjE5IDUuODY2MzJMMTAuMDQwNiA1Ljg0ODU4QzEwLjIzNjkgNS42NzEyNCAxMC41Mzk5IDUuNjc3MTYgMTAuNzI5IDUuODY2MzJDMTAuOTE4MiA2LjA1NTQ4IDEwLjkyNDEgNi4zNTg0NiAxMC43NDY4IDYuNTU0NzRMMTAuNzI5IDYuNTczNDJMNi4xNDU4OCAxMS4xNTY2QzUuOTUwNjIgMTEuMzUxOCA1LjYzNDAzIDExLjM1MTggNS40Mzg3NyAxMS4xNTY2QzUuMjQzNTEgMTAuOTYxMyA1LjI0MzUxIDEwLjY0NDcgNS40Mzg3NyAxMC40NDk1TDEwLjAyMTkgNS44NjYzMloiIC8+PC9zdmc+" class="anchor-icon" /><span class="copied-indicator docsearch-exclude" aria-live="polite" aria-atomic="true"></span></span></a>

</div>

Armed with the subagent’s findings, Kiro used `glob` to find all files in the build tool package, then used `fs_read` to inspect the relevant source modules.

It read the plugin and configuration modules, scanning for where the parser was being instantiated. The pattern became clear: every function in the configuration module was creating a new parser instance with identical parameters.

**Why this matters:** Kiro didn’t just grep for the parser class and call it a day. It read the actual code, analyzed the control flow, and identified the repeated instantiation pattern. This required reasoning about the codes behavior, not just pattern matching.

<div class="heading-anchor-wrapper">

### Turn 10: Implementing the fix

<a href="#turn-10-implementing-the-fix" class="anchor-link" aria-label="Copy link to Turn 10 implementing the fix section"><span class="anchor-icon-wrapper"><img src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iYW5jaG9yLWljb24iIHZpZXdib3g9IjAgMCAxNiAxNyIgd2lkdGg9IjE2IiBoZWlnaHQ9IjE3IiBmaWxsPSJjdXJyZW50Q29sb3IiPjxwYXRoIGQ9Ik0yLjI3MTQzIDE0LjIyOEMwLjU5MTg5NyAxMi41NDg1IDAuNTkxODk3IDkuODI1MzkgMi4yNzE0MyA4LjE0NTg1TDMuNDIzMjQgNi45OTQwNEwzLjQ0MTg4IDYuOTc2MzVDMy42MzgxNiA2Ljc5OSAzLjk0MTE4IDYuODA0ODggNC4xMzAzNSA2Ljk5NDA0QzQuMzE5NTEgNy4xODMyMSA0LjMyNTM5IDcuNDg2MjMgNC4xNDgwNCA3LjY4MjVMNC4xMzAzNSA3LjcwMTE1TDIuOTc4NTQgOC44NTI5NkMxLjY4OTUzIDEwLjE0MiAxLjY4OTUzIDEyLjIzMTkgMi45Nzg1NCAxMy41MjA5TDMuMDA4ODggMTMuNTUwOUM0LjMwMDE0IDE0LjgwOTggNi4zNjc1MSAxNC43OTk4IDcuNjQ2NDYgMTMuNTIwOUw4Ljc5ODI3IDEyLjM2OTFMOC44MTY5MSAxMi4zNTE0QzkuMDEzMTkgMTIuMTc0IDkuMzE2MjEgMTIuMTc5OSA5LjUwNTM4IDEyLjM2OTFDOS42OTQ1NCAxMi41NTgyIDkuNzAwNDYgMTIuODYxMyA5LjUyMzExIDEzLjA1NzZMOS41MDUzOCAxMy4wNzYyTDguMzUzNTYgMTQuMjI4QzYuNjg3MTUgMTUuODk0NCAzLjk5MzQ3IDE1LjkwNzQgMi4zMTEgMTQuMjY3TDIuMjcxNDMgMTQuMjI4Wk0xMy4wMjE1IDMuNDc3OTNDMTEuNzQyNSAyLjE5ODk5IDkuNjc1MTcgMi4xODg5NiA4LjM4MzkgMy40NDc5NEw4LjM1MzU2IDMuNDc3OTNMNy4yMjU3OSA0LjYwNTdDNy4wMzA1MyA0LjgwMDk2IDYuNzEzOTUgNC44MDA5NiA2LjUxODY5IDQuNjA1N0M2LjMyMzQyIDQuNDEwNDQgNi4zMjM0MiA0LjA5Mzg2IDYuNTE4NjkgMy44OTg1OUw3LjY0NjQ2IDIuNzcwODJMNy42ODYwMyAyLjczMTc3QzkuMzY4NSAxLjA5MTM4IDEyLjA2MjIgMS4xMDQ0MSAxMy43Mjg2IDIuNzcwODJMMTMuNzY3NyAyLjgxMDM2QzE1LjM5NTIgNC40Nzk1OCAxNS4zOTUxIDcuMTQ0MTcgMTMuNzY3NyA4LjgxMzM4TDEzLjcyODYgOC44NTI5NkwxMi42MDA4IDkuOTgwNzNDMTIuNDA1NiAxMC4xNzYgMTIuMDg5IDEwLjE3NiAxMS44OTM3IDkuOTgwNzNDMTEuNjk4NSA5Ljc4NTQ3IDExLjY5ODUgOS40Njg4OCAxMS44OTM3IDkuMjczNjJMMTMuMDIxNSA4LjE0NTg1TDEzLjA1MTUgOC4xMTU1MUMxNC4zMDA1IDYuODM0NDIgMTQuMzAwNSA0Ljc4OTM3IDEzLjA1MTUgMy41MDgyN0wxMy4wMjE1IDMuNDc3OTNaIiAvPjxwYXRoIGQ9Ik0xMC4wMjE5IDUuODY2MzJMMTAuMDQwNiA1Ljg0ODU4QzEwLjIzNjkgNS42NzEyNCAxMC41Mzk5IDUuNjc3MTYgMTAuNzI5IDUuODY2MzJDMTAuOTE4MiA2LjA1NTQ4IDEwLjkyNDEgNi4zNTg0NiAxMC43NDY4IDYuNTU0NzRMMTAuNzI5IDYuNTczNDJMNi4xNDU4OCAxMS4xNTY2QzUuOTUwNjIgMTEuMzUxOCA1LjYzNDAzIDExLjM1MTggNS40Mzg3NyAxMS4xNTY2QzUuMjQzNTEgMTAuOTYxMyA1LjI0MzUxIDEwLjY0NDcgNS40Mzg3NyAxMC40NDk1TDEwLjAyMTkgNS44NjYzMloiIC8+PC9zdmc+" class="anchor-icon" /><span class="copied-indicator docsearch-exclude" aria-live="polite" aria-atomic="true"></span></span></a>

</div>

Finally, Kiro implemented the solution. It used `fs_write` with the `str_replace` command to modify the configuration module, introducing a caching mechanism:

- Added a cache hash to store parser instances
- Created a helper function that checks the cache before instantiating a new parser
- Refactored all existing functions to use the cached parser

The fix was surgical: it preserved all existing behavior while eliminating the redundant re-initialization.

**Why this matters:** Kiro didn’t just suggest a fix, it wrote the code and implemented it. The `str_replace` operation required understanding the existing code structure, identifying the exact lines to change, and generating syntactically correct code that integrated seamlessly with the existing codebase.

Kiro implemented **80–90% of the required code changes directly**. We reviewed, validated, and ran a build to confirm the hypothesis. The results were immediate: P99 build times dropped from over 30 minutes to **under 1 minute**.

<div class="heading-anchor-wrapper">

## What we Learned

<a href="#what-we-learned" class="anchor-link" aria-label="Copy link to What we learned section"><span class="anchor-icon-wrapper"><img src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iYW5jaG9yLWljb24iIHZpZXdib3g9IjAgMCAxNiAxNyIgd2lkdGg9IjE2IiBoZWlnaHQ9IjE3IiBmaWxsPSJjdXJyZW50Q29sb3IiPjxwYXRoIGQ9Ik0yLjI3MTQzIDE0LjIyOEMwLjU5MTg5NyAxMi41NDg1IDAuNTkxODk3IDkuODI1MzkgMi4yNzE0MyA4LjE0NTg1TDMuNDIzMjQgNi45OTQwNEwzLjQ0MTg4IDYuOTc2MzVDMy42MzgxNiA2Ljc5OSAzLjk0MTE4IDYuODA0ODggNC4xMzAzNSA2Ljk5NDA0QzQuMzE5NTEgNy4xODMyMSA0LjMyNTM5IDcuNDg2MjMgNC4xNDgwNCA3LjY4MjVMNC4xMzAzNSA3LjcwMTE1TDIuOTc4NTQgOC44NTI5NkMxLjY4OTUzIDEwLjE0MiAxLjY4OTUzIDEyLjIzMTkgMi45Nzg1NCAxMy41MjA5TDMuMDA4ODggMTMuNTUwOUM0LjMwMDE0IDE0LjgwOTggNi4zNjc1MSAxNC43OTk4IDcuNjQ2NDYgMTMuNTIwOUw4Ljc5ODI3IDEyLjM2OTFMOC44MTY5MSAxMi4zNTE0QzkuMDEzMTkgMTIuMTc0IDkuMzE2MjEgMTIuMTc5OSA5LjUwNTM4IDEyLjM2OTFDOS42OTQ1NCAxMi41NTgyIDkuNzAwNDYgMTIuODYxMyA5LjUyMzExIDEzLjA1NzZMOS41MDUzOCAxMy4wNzYyTDguMzUzNTYgMTQuMjI4QzYuNjg3MTUgMTUuODk0NCAzLjk5MzQ3IDE1LjkwNzQgMi4zMTEgMTQuMjY3TDIuMjcxNDMgMTQuMjI4Wk0xMy4wMjE1IDMuNDc3OTNDMTEuNzQyNSAyLjE5ODk5IDkuNjc1MTcgMi4xODg5NiA4LjM4MzkgMy40NDc5NEw4LjM1MzU2IDMuNDc3OTNMNy4yMjU3OSA0LjYwNTdDNy4wMzA1MyA0LjgwMDk2IDYuNzEzOTUgNC44MDA5NiA2LjUxODY5IDQuNjA1N0M2LjMyMzQyIDQuNDEwNDQgNi4zMjM0MiA0LjA5Mzg2IDYuNTE4NjkgMy44OTg1OUw3LjY0NjQ2IDIuNzcwODJMNy42ODYwMyAyLjczMTc3QzkuMzY4NSAxLjA5MTM4IDEyLjA2MjIgMS4xMDQ0MSAxMy43Mjg2IDIuNzcwODJMMTMuNzY3NyAyLjgxMDM2QzE1LjM5NTIgNC40Nzk1OCAxNS4zOTUxIDcuMTQ0MTcgMTMuNzY3NyA4LjgxMzM4TDEzLjcyODYgOC44NTI5NkwxMi42MDA4IDkuOTgwNzNDMTIuNDA1NiAxMC4xNzYgMTIuMDg5IDEwLjE3NiAxMS44OTM3IDkuOTgwNzNDMTEuNjk4NSA5Ljc4NTQ3IDExLjY5ODUgOS40Njg4OCAxMS44OTM3IDkuMjczNjJMMTMuMDIxNSA4LjE0NTg1TDEzLjA1MTUgOC4xMTU1MUMxNC4zMDA1IDYuODM0NDIgMTQuMzAwNSA0Ljc4OTM3IDEzLjA1MTUgMy41MDgyN0wxMy4wMjE1IDMuNDc3OTNaIiAvPjxwYXRoIGQ9Ik0xMC4wMjE5IDUuODY2MzJMMTAuMDQwNiA1Ljg0ODU4QzEwLjIzNjkgNS42NzEyNCAxMC41Mzk5IDUuNjc3MTYgMTAuNzI5IDUuODY2MzJDMTAuOTE4MiA2LjA1NTQ4IDEwLjkyNDEgNi4zNTg0NiAxMC43NDY4IDYuNTU0NzRMMTAuNzI5IDYuNTczNDJMNi4xNDU4OCAxMS4xNTY2QzUuOTUwNjIgMTEuMzUxOCA1LjYzNDAzIDExLjM1MTggNS40Mzg3NyAxMS4xNTY2QzUuMjQzNTEgMTAuOTYxMyA1LjI0MzUxIDEwLjY0NDcgNS40Mzg3NyAxMC40NDk1TDEwLjAyMTkgNS44NjYzMloiIC8+PC9zdmc+" class="anchor-icon" /><span class="copied-indicator docsearch-exclude" aria-live="polite" aria-atomic="true"></span></span></a>

</div>

**Use a generalist agent for investigation tasks.** When the problem is open-ended — "why is this slow?" rather than "write me a function that does X" — a generalist agent that can reason across files, tools, and data formats is the right choice. Kiro CLI’s ability to chain tool calls autonomously made it well-suited for this kind of exploratory work.

**Trust the agent to go deep, but verify the output.** Kiro implemented the majority of the fix autonomously, but we still built the package and validated the results before shipping. AI-assisted development accelerates the investigation and implementation phases dramatically but shouldn’t replace the engineer’s judgment on correctness and safety.

**The ROI compounds at scale.** A 30-minute build feels like a personal inconvenience. Multiply it across hundreds of thousands of builds per month, and it becomes an infrastructure cost problem. Kiro helped surface and fix an issue of a scale that only becomes visible in aggregate.

**What made this work wasn**’**t any single tool,** it was Kiro’s ability to chain them together autonomously. Kiro built context, formed a hypothesis, validated it against the code, and implemented a fix, all without human intervention beyond the initial prompt.

</div>

<div class="mt-12">

<div class="flex w-full items-stretch justify-between gap-3 self-stretch md:gap-4">

<div class="flex flex-1 sm:w-80">

<a href="/blog/introducing-headless-mode/" class="group/nav flex w-full flex-col justify-start gap-3 self-stretch rounded-2xl bg-prey-900 px-4 py-3 transition-colors md:gap-4 md:px-6 md:py-4"></a>

<div class="flex items-center gap-1">

<span class="font-display text-[18px] leading-[16px] text-purple-500" aria-hidden="true">{</span><span class="leading-[16px] mt-[1px] uppercase text-secondary"><span class="text-utility-sm">PREVIOUS</span></span><span class="font-display text-[18px] leading-[16px] text-purple-500" aria-hidden="true">}</span>

</div>

### Run Kiro CLI programmatically: introducing headless mode

</div>

<div class="flex flex-1 sm:w-80">

<a href="/blog/opus-4-7/" class="group/nav flex w-full flex-col justify-start gap-3 self-stretch rounded-2xl bg-prey-900 px-4 py-3 transition-colors md:gap-4 md:px-6 md:py-4"></a>

<div class="flex w-full justify-end">

<div class="flex items-center gap-1">

<span class="font-display text-[18px] leading-[16px] text-purple-500" aria-hidden="true">{</span><span class="leading-[16px] mt-[1px] uppercase text-secondary"><span class="text-utility-sm">NEXT</span></span><span class="font-display text-[18px] leading-[16px] text-purple-500" aria-hidden="true">}</span>

</div>

</div>

### Opus 4.7 is now available in Kiro

</div>

</div>

</div>

</div>

</div>

</div>

</div>

</div>

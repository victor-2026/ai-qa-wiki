# Source: https://kiro.dev/blog/continuous-prompt-evaluation/

**URL:** https://kiro.dev/blog/continuous-prompt-evaluation/
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

August 21, 2026

</div>

# Continuous Prompt Evaluation: How We Use LLM Judges and Live Signals to Improve Kiro Agent Quality

<div class="flex items-center gap-2">

<span class="text-sm text-muted-foreground">By</span>

<div class="flex flex-wrap items-center gap-4">

<a href="https://scholar.google.com/citations?user=2nZhRosAAAAJ" class="flex cursor-pointer items-center gap-2 transition-opacity hover:opacity-80"><span class="relative flex shrink-0 overflow-hidden rounded-full h-8 w-8"><span class="flex h-full w-full items-center justify-center rounded-full bg-muted">MY</span></span></a>

<div>

Myeongsoo Kim

Applied Science

</div>

<a href="https://scholar.google.com/citations?user=E9uE6VcAAAAJ" class="flex cursor-pointer items-center gap-2 transition-opacity hover:opacity-80"><span class="relative flex shrink-0 overflow-hidden rounded-full h-8 w-8"><span class="flex h-full w-full items-center justify-center rounded-full bg-muted">PA</span></span></a>

<div>

Patrick Chapman

Applied Science

</div>

<div class="flex items-center gap-2">

<span class="relative flex shrink-0 overflow-hidden rounded-full h-8 w-8"><span class="flex h-full w-full items-center justify-center rounded-full bg-muted">SA</span></span>

<div>

Sai Srinivas Somarouthu

Developer

</div>

</div>

<div class="flex items-center gap-2">

<span class="relative flex shrink-0 overflow-hidden rounded-full h-8 w-8"><span class="flex h-full w-full items-center justify-center rounded-full bg-muted">JA</span></span>

<div>

Jay Agrawal

Developer

</div>

</div>

<a href="https://scholar.google.com/citations?user=iw1GQj0AAAAJ&amp;hl=en&amp;oi=ao" class="flex cursor-pointer items-center gap-2 transition-opacity hover:opacity-80"><span class="relative flex shrink-0 overflow-hidden rounded-full h-8 w-8"><span class="flex h-full w-full items-center justify-center rounded-full bg-muted">MU</span></span></a>

<div>

Murali Krishna Ramanathan

Applied Science

</div>

</div>

</div>

</div>

<div class="blog-content changelog prose-prey prose max-w-none dark:prose-invert prose-code:before:content-none prose-code:after:content-none">

<div class="heading-anchor-wrapper">

## The problem: system prompt behavior is hard to predict

<a href="#the-problem-system-prompt-behavior-is-hard-to-predict" class="anchor-link" aria-label="Copy link to The problem system prompt behavior is hard to predict section"><span class="anchor-icon-wrapper"><img src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iYW5jaG9yLWljb24iIHZpZXdib3g9IjAgMCAxNiAxNyIgd2lkdGg9IjE2IiBoZWlnaHQ9IjE3IiBmaWxsPSJjdXJyZW50Q29sb3IiPjxwYXRoIGQ9Ik0yLjI3MTQzIDE0LjIyOEMwLjU5MTg5NyAxMi41NDg1IDAuNTkxODk3IDkuODI1MzkgMi4yNzE0MyA4LjE0NTg1TDMuNDIzMjQgNi45OTQwNEwzLjQ0MTg4IDYuOTc2MzVDMy42MzgxNiA2Ljc5OSAzLjk0MTE4IDYuODA0ODggNC4xMzAzNSA2Ljk5NDA0QzQuMzE5NTEgNy4xODMyMSA0LjMyNTM5IDcuNDg2MjMgNC4xNDgwNCA3LjY4MjVMNC4xMzAzNSA3LjcwMTE1TDIuOTc4NTQgOC44NTI5NkMxLjY4OTUzIDEwLjE0MiAxLjY4OTUzIDEyLjIzMTkgMi45Nzg1NCAxMy41MjA5TDMuMDA4ODggMTMuNTUwOUM0LjMwMDE0IDE0LjgwOTggNi4zNjc1MSAxNC43OTk4IDcuNjQ2NDYgMTMuNTIwOUw4Ljc5ODI3IDEyLjM2OTFMOC44MTY5MSAxMi4zNTE0QzkuMDEzMTkgMTIuMTc0IDkuMzE2MjEgMTIuMTc5OSA5LjUwNTM4IDEyLjM2OTFDOS42OTQ1NCAxMi41NTgyIDkuNzAwNDYgMTIuODYxMyA5LjUyMzExIDEzLjA1NzZMOS41MDUzOCAxMy4wNzYyTDguMzUzNTYgMTQuMjI4QzYuNjg3MTUgMTUuODk0NCAzLjk5MzQ3IDE1LjkwNzQgMi4zMTEgMTQuMjY3TDIuMjcxNDMgMTQuMjI4Wk0xMy4wMjE1IDMuNDc3OTNDMTEuNzQyNSAyLjE5ODk5IDkuNjc1MTcgMi4xODg5NiA4LjM4MzkgMy40NDc5NEw4LjM1MzU2IDMuNDc3OTNMNy4yMjU3OSA0LjYwNTdDNy4wMzA1MyA0LjgwMDk2IDYuNzEzOTUgNC44MDA5NiA2LjUxODY5IDQuNjA1N0M2LjMyMzQyIDQuNDEwNDQgNi4zMjM0MiA0LjA5Mzg2IDYuNTE4NjkgMy44OTg1OUw3LjY0NjQ2IDIuNzcwODJMNy42ODYwMyAyLjczMTc3QzkuMzY4NSAxLjA5MTM4IDEyLjA2MjIgMS4xMDQ0MSAxMy43Mjg2IDIuNzcwODJMMTMuNzY3NyAyLjgxMDM2QzE1LjM5NTIgNC40Nzk1OCAxNS4zOTUxIDcuMTQ0MTcgMTMuNzY3NyA4LjgxMzM4TDEzLjcyODYgOC44NTI5NkwxMi42MDA4IDkuOTgwNzNDMTIuNDA1NiAxMC4xNzYgMTIuMDg5IDEwLjE3NiAxMS44OTM3IDkuOTgwNzNDMTEuNjk4NSA5Ljc4NTQ3IDExLjY5ODUgOS40Njg4OCAxMS44OTM3IDkuMjczNjJMMTMuMDIxNSA4LjE0NTg1TDEzLjA1MTUgOC4xMTU1MUMxNC4zMDA1IDYuODM0NDIgMTQuMzAwNSA0Ljc4OTM3IDEzLjA1MTUgMy41MDgyN0wxMy4wMjE1IDMuNDc3OTNaIiAvPjxwYXRoIGQ9Ik0xMC4wMjE5IDUuODY2MzJMMTAuMDQwNiA1Ljg0ODU4QzEwLjIzNjkgNS42NzEyNCAxMC41Mzk5IDUuNjc3MTYgMTAuNzI5IDUuODY2MzJDMTAuOTE4MiA2LjA1NTQ4IDEwLjkyNDEgNi4zNTg0NiAxMC43NDY4IDYuNTU0NzRMMTAuNzI5IDYuNTczNDJMNi4xNDU4OCAxMS4xNTY2QzUuOTUwNjIgMTEuMzUxOCA1LjYzNDAzIDExLjM1MTggNS40Mzg3NyAxMS4xNTY2QzUuMjQzNTEgMTAuOTYxMyA1LjI0MzUxIDEwLjY0NDcgNS40Mzg3NyAxMC40NDk1TDEwLjAyMTkgNS44NjYzMloiIC8+PC9zdmc+" class="anchor-icon" /><span class="copied-indicator docsearch-exclude" aria-live="polite" aria-atomic="true"></span></span></a>

</div>

Prompt behavior is difficult to validate exhaustively. A system prompt operates across combinations of models, tools, codebases, tasks, and users that no test suite can fully cover. An instruction that looks reasonable in isolation can cause unintended behavior in cases the prompt author did not anticipate, and a change that improves one scenario can regress another.

Prompt staleness is one instance of this broader problem. An instruction may already cause rare or hard-to-observe issues, then become more visibly harmful when a newer model follows it more strictly. New tools, workflows, and user patterns can expose the same latent defects.

Benchmarks remain an important quality signal, but they cannot capture every behavior that appears in everyday development work. We needed a process that detects issues on real workflows, categorizes recurring patterns, traces them to prompt instructions, and validates fixes as models and usage evolve.

<div class="heading-anchor-wrapper">

## The system at a glance

<a href="#the-system-at-a-glance" class="anchor-link" aria-label="Copy link to The system at a glance section"><span class="anchor-icon-wrapper"><img src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iYW5jaG9yLWljb24iIHZpZXdib3g9IjAgMCAxNiAxNyIgd2lkdGg9IjE2IiBoZWlnaHQ9IjE3IiBmaWxsPSJjdXJyZW50Q29sb3IiPjxwYXRoIGQ9Ik0yLjI3MTQzIDE0LjIyOEMwLjU5MTg5NyAxMi41NDg1IDAuNTkxODk3IDkuODI1MzkgMi4yNzE0MyA4LjE0NTg1TDMuNDIzMjQgNi45OTQwNEwzLjQ0MTg4IDYuOTc2MzVDMy42MzgxNiA2Ljc5OSAzLjk0MTE4IDYuODA0ODggNC4xMzAzNSA2Ljk5NDA0QzQuMzE5NTEgNy4xODMyMSA0LjMyNTM5IDcuNDg2MjMgNC4xNDgwNCA3LjY4MjVMNC4xMzAzNSA3LjcwMTE1TDIuOTc4NTQgOC44NTI5NkMxLjY4OTUzIDEwLjE0MiAxLjY4OTUzIDEyLjIzMTkgMi45Nzg1NCAxMy41MjA5TDMuMDA4ODggMTMuNTUwOUM0LjMwMDE0IDE0LjgwOTggNi4zNjc1MSAxNC43OTk4IDcuNjQ2NDYgMTMuNTIwOUw4Ljc5ODI3IDEyLjM2OTFMOC44MTY5MSAxMi4zNTE0QzkuMDEzMTkgMTIuMTc0IDkuMzE2MjEgMTIuMTc5OSA5LjUwNTM4IDEyLjM2OTFDOS42OTQ1NCAxMi41NTgyIDkuNzAwNDYgMTIuODYxMyA5LjUyMzExIDEzLjA1NzZMOS41MDUzOCAxMy4wNzYyTDguMzUzNTYgMTQuMjI4QzYuNjg3MTUgMTUuODk0NCAzLjk5MzQ3IDE1LjkwNzQgMi4zMTEgMTQuMjY3TDIuMjcxNDMgMTQuMjI4Wk0xMy4wMjE1IDMuNDc3OTNDMTEuNzQyNSAyLjE5ODk5IDkuNjc1MTcgMi4xODg5NiA4LjM4MzkgMy40NDc5NEw4LjM1MzU2IDMuNDc3OTNMNy4yMjU3OSA0LjYwNTdDNy4wMzA1MyA0LjgwMDk2IDYuNzEzOTUgNC44MDA5NiA2LjUxODY5IDQuNjA1N0M2LjMyMzQyIDQuNDEwNDQgNi4zMjM0MiA0LjA5Mzg2IDYuNTE4NjkgMy44OTg1OUw3LjY0NjQ2IDIuNzcwODJMNy42ODYwMyAyLjczMTc3QzkuMzY4NSAxLjA5MTM4IDEyLjA2MjIgMS4xMDQ0MSAxMy43Mjg2IDIuNzcwODJMMTMuNzY3NyAyLjgxMDM2QzE1LjM5NTIgNC40Nzk1OCAxNS4zOTUxIDcuMTQ0MTcgMTMuNzY3NyA4LjgxMzM4TDEzLjcyODYgOC44NTI5NkwxMi42MDA4IDkuOTgwNzNDMTIuNDA1NiAxMC4xNzYgMTIuMDg5IDEwLjE3NiAxMS44OTM3IDkuOTgwNzNDMTEuNjk4NSA5Ljc4NTQ3IDExLjY5ODUgOS40Njg4OCAxMS44OTM3IDkuMjczNjJMMTMuMDIxNSA4LjE0NTg1TDEzLjA1MTUgOC4xMTU1MUMxNC4zMDA1IDYuODM0NDIgMTQuMzAwNSA0Ljc4OTM3IDEzLjA1MTUgMy41MDgyN0wxMy4wMjE1IDMuNDc3OTNaIiAvPjxwYXRoIGQ9Ik0xMC4wMjE5IDUuODY2MzJMMTAuMDQwNiA1Ljg0ODU4QzEwLjIzNjkgNS42NzEyNCAxMC41Mzk5IDUuNjc3MTYgMTAuNzI5IDUuODY2MzJDMTAuOTE4MiA2LjA1NTQ4IDEwLjkyNDEgNi4zNTg0NiAxMC43NDY4IDYuNTU0NzRMMTAuNzI5IDYuNTczNDJMNi4xNDU4OCAxMS4xNTY2QzUuOTUwNjIgMTEuMzUxOCA1LjYzNDAzIDExLjM1MTggNS40Mzg3NyAxMS4xNTY2QzUuMjQzNTEgMTAuOTYxMyA1LjI0MzUxIDEwLjY0NDcgNS40Mzg3NyAxMC40NDk1TDEwLjAyMTkgNS44NjYzMloiIC8+PC9zdmc+" class="anchor-icon" /><span class="copied-indicator docsearch-exclude" aria-live="polite" aria-atomic="true"></span></span></a>

</div>

This article focuses on evaluating human-authored system prompt and configuration changes. It does not cover automated trajectory mining, change generation, or broader harness self-improvement. The workflow pairs benchmark results with an LLM-based analysis of thousands of Kiro conversations with our internal developers to identify opportunities in task completion, verification, and tool use. It has four stages:

- **Diagnose** high-frequency complaint categories and trace them to prompt instructions
- **Design** targeted prompt changes for isolated evaluation
- **Test** the changes in controlled cohorts on internal traffic
- **Evaluate** each cohort with the LLM judge for changes in dissatisfaction and behavioral quality issues

<div class="my-8">

<figure class="overflow-hidden rounded-2xl border border-[#4a464f] bg-muted/30">
<span class="group relative inline-block transition-all duration-200 cursor-zoom-in" style="display:block" tabindex="0" role="button" aria-label="Open image lightbox: Diagram titled &#39;Prompt Engineering Methodology&#39; with four stages left to right—Diagnose, Design, Test in Parallel, and Evaluate &amp; Decide—joined by a dashed continuous-improvement loop back to the start, with a &#39;Why This Works&#39; panel beneath."><span class="relative overflow-hidden h-auto w-full border-0"><span class="absolute inset-0 flex animate-pulse items-center justify-center bg-muted"><span class="sr-only">Loading image...</span></span><img src="/images/blogs/continuous-prompt-evaluation/prompt-evaluation-cycle.png?h=08717e46" class="transition-opacity duration-300 opacity-0" style="color:transparent" loading="lazy" decoding="async" data-nimg="1" width="1200" height="600" alt="Diagram titled &#39;Prompt Engineering Methodology&#39; with four stages left to right—Diagnose, Design, Test in Parallel, and Evaluate &amp; Decide—joined by a dashed continuous-improvement loop back to the start, with a &#39;Why This Works&#39; panel beneath." /></span><span class="absolute bottom-2 right-2 z-10 flex items-center justify-center rounded-full bg-prey-600/60 p-2.5 transition-opacity duration-200 opacity-100 group-hover:opacity-100" aria-hidden="true"><img src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdib3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48cGF0aCBkPSJNMTUuNjIyIDAuMDA5MTU3NTFDMTUuNzEyMyAwLjAyNzEzMzUgMTUuNzk1OSAwLjA3MTM0IDE1Ljg2MiAwLjEzNzM2M0MxNS45NSAwLjIyNTQzNiAxNS45OTk1IDAuMzQ1MjI2IDE1Ljk5OTMgMC40Njk3OEwxNS45OTI5IDUuNDIzMDhMMTUuOTgzNyA1LjUxNzRDMTUuOTM5OSA1LjczMTA2IDE1Ljc1MDYgNS44OTIwNCAxNS41MjQgNS44OTE5NEMxNS4yNjUxIDUuODkxNjIgMTUuMDU0OSA1LjY4MTA2IDE1LjA1NTIgNS40MjIxNkwxNS4wNTk3IDEuNjAxNjVMMTAuMTc2OSA2LjQ4NTM1QzkuOTkzODQgNi42Njg0NSA5LjY5NzA0IDYuNjY4NDUgOS41MTM5NCA2LjQ4NTM1QzkuMzMwODMgNi4zMDIyNCA5LjMzMDgzIDYuMDA1NDUgOS41MTM5NCA1LjgyMjM0TDE0LjM5NjcgMC45Mzg2NDVMMTAuNTc3MSAwLjk0NDEzOUwxMC40ODI4IDAuOTM0OTgyQzEwLjI2OSAwLjg5MTU4NCAxMC4xMDc2IDAuNzAxOTAzIDEwLjEwNzMgMC40NzUyNzVDMTAuMTA3MiAwLjIxNjUwNyAxMC4zMTc0IDAuMDA2NzM0ODQgMTAuNTc2MiAwLjAwNjQxMDI2TDE1LjUyOTUgMEwxNS42MjIgMC4wMDkxNTc1MVoiIGZpbGw9ImN1cnJlbnRDb2xvciIgLz48cGF0aCBkPSJNMC4zNzcyOSAxNS45OTA4QzAuMjg3MDU3IDE1Ljk3MjkgMC4yMDMzODUgMTUuOTI4NyAwLjEzNzM2MiAxNS44NjI2QzAuMDQ5Mjg4OCAxNS43NzQ2IC0wLjAwMDE1NzAyNCAxNS42NTQ4IC04LjE4MjM1ZS0wNyAxNS41MzAyTDAuMDA2NDA5NDcgMTAuNTc2OUwwLjAxNTU2NyAxMC40ODI2QzAuMDU5Mzg5MSAxMC4yNjg5IDAuMjQ4NzQxIDEwLjEwOCAwLjQ3NTI3NiAxMC4xMDgxQzAuNzM0MTkxIDEwLjEwODQgMC45NDQ0MTUgMTAuMzE4OSAwLjk0NDE0MyAxMC41Nzc4TDAuOTM5NTY0IDE0LjM5ODRMNS44MjIzNyA5LjUxNDY1QzYuMDA1NDcgOS4zMzE1NSA2LjMwMjI3IDkuMzMxNTUgNi40ODUzOCA5LjUxNDY1QzYuNjY4NDggOS42OTc3NiA2LjY2ODQ4IDkuOTk0NTUgNi40ODUzOCAxMC4xNzc3TDEuNjAyNTcgMTUuMDYxNEw1LjQyMjE4IDE1LjA1NTlMNS41MTY1MSAxNS4wNjVDNS43MzAyOSAxNS4xMDg0IDUuODkxNjggMTUuMjk4MSA1Ljg5MTk3IDE1LjUyNDdDNS44OTIwOCAxNS43ODM1IDUuNjgxOTIgMTUuOTkzMyA1LjQyMzEgMTUuOTkzNkwwLjQ2OTc4MSAxNkwwLjM3NzI5IDE1Ljk5MDhaIiBmaWxsPSJjdXJyZW50Q29sb3IiIC8+PC9zdmc+" /></span></span>
<figcaption>Figure 1: The four-stage prompt-evaluation cycle, repeated as prompts, user behavior, and model capabilities change.</figcaption>
</figure>

</div>

<div class="heading-anchor-wrapper">

## The four-stage prompt-evaluation cycle

<a href="#the-four-stage-prompt-evaluation-cycle" class="anchor-link" aria-label="Copy link to The four stage prompt evaluation cycle section"><span class="anchor-icon-wrapper"><img src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iYW5jaG9yLWljb24iIHZpZXdib3g9IjAgMCAxNiAxNyIgd2lkdGg9IjE2IiBoZWlnaHQ9IjE3IiBmaWxsPSJjdXJyZW50Q29sb3IiPjxwYXRoIGQ9Ik0yLjI3MTQzIDE0LjIyOEMwLjU5MTg5NyAxMi41NDg1IDAuNTkxODk3IDkuODI1MzkgMi4yNzE0MyA4LjE0NTg1TDMuNDIzMjQgNi45OTQwNEwzLjQ0MTg4IDYuOTc2MzVDMy42MzgxNiA2Ljc5OSAzLjk0MTE4IDYuODA0ODggNC4xMzAzNSA2Ljk5NDA0QzQuMzE5NTEgNy4xODMyMSA0LjMyNTM5IDcuNDg2MjMgNC4xNDgwNCA3LjY4MjVMNC4xMzAzNSA3LjcwMTE1TDIuOTc4NTQgOC44NTI5NkMxLjY4OTUzIDEwLjE0MiAxLjY4OTUzIDEyLjIzMTkgMi45Nzg1NCAxMy41MjA5TDMuMDA4ODggMTMuNTUwOUM0LjMwMDE0IDE0LjgwOTggNi4zNjc1MSAxNC43OTk4IDcuNjQ2NDYgMTMuNTIwOUw4Ljc5ODI3IDEyLjM2OTFMOC44MTY5MSAxMi4zNTE0QzkuMDEzMTkgMTIuMTc0IDkuMzE2MjEgMTIuMTc5OSA5LjUwNTM4IDEyLjM2OTFDOS42OTQ1NCAxMi41NTgyIDkuNzAwNDYgMTIuODYxMyA5LjUyMzExIDEzLjA1NzZMOS41MDUzOCAxMy4wNzYyTDguMzUzNTYgMTQuMjI4QzYuNjg3MTUgMTUuODk0NCAzLjk5MzQ3IDE1LjkwNzQgMi4zMTEgMTQuMjY3TDIuMjcxNDMgMTQuMjI4Wk0xMy4wMjE1IDMuNDc3OTNDMTEuNzQyNSAyLjE5ODk5IDkuNjc1MTcgMi4xODg5NiA4LjM4MzkgMy40NDc5NEw4LjM1MzU2IDMuNDc3OTNMNy4yMjU3OSA0LjYwNTdDNy4wMzA1MyA0LjgwMDk2IDYuNzEzOTUgNC44MDA5NiA2LjUxODY5IDQuNjA1N0M2LjMyMzQyIDQuNDEwNDQgNi4zMjM0MiA0LjA5Mzg2IDYuNTE4NjkgMy44OTg1OUw3LjY0NjQ2IDIuNzcwODJMNy42ODYwMyAyLjczMTc3QzkuMzY4NSAxLjA5MTM4IDEyLjA2MjIgMS4xMDQ0MSAxMy43Mjg2IDIuNzcwODJMMTMuNzY3NyAyLjgxMDM2QzE1LjM5NTIgNC40Nzk1OCAxNS4zOTUxIDcuMTQ0MTcgMTMuNzY3NyA4LjgxMzM4TDEzLjcyODYgOC44NTI5NkwxMi42MDA4IDkuOTgwNzNDMTIuNDA1NiAxMC4xNzYgMTIuMDg5IDEwLjE3NiAxMS44OTM3IDkuOTgwNzNDMTEuNjk4NSA5Ljc4NTQ3IDExLjY5ODUgOS40Njg4OCAxMS44OTM3IDkuMjczNjJMMTMuMDIxNSA4LjE0NTg1TDEzLjA1MTUgOC4xMTU1MUMxNC4zMDA1IDYuODM0NDIgMTQuMzAwNSA0Ljc4OTM3IDEzLjA1MTUgMy41MDgyN0wxMy4wMjE1IDMuNDc3OTNaIiAvPjxwYXRoIGQ9Ik0xMC4wMjE5IDUuODY2MzJMMTAuMDQwNiA1Ljg0ODU4QzEwLjIzNjkgNS42NzEyNCAxMC41Mzk5IDUuNjc3MTYgMTAuNzI5IDUuODY2MzJDMTAuOTE4MiA2LjA1NTQ4IDEwLjkyNDEgNi4zNTg0NiAxMC43NDY4IDYuNTU0NzRMMTAuNzI5IDYuNTczNDJMNi4xNDU4OCAxMS4xNTY2QzUuOTUwNjIgMTEuMzUxOCA1LjYzNDAzIDExLjM1MTggNS40Mzg3NyAxMS4xNTY2QzUuMjQzNTEgMTAuOTYxMyA1LjI0MzUxIDEwLjY0NDcgNS40Mzg3NyAxMC40NDk1TDEwLjAyMTkgNS44NjYzMloiIC8+PC9zdmc+" class="anchor-icon" /><span class="copied-indicator docsearch-exclude" aria-live="polite" aria-atomic="true"></span></span></a>

</div>

The diagram above summarizes the same four stages described below. We repeat this cycle as prompts, user behavior, and model capabilities change:

**1. Diagnose.** We run the judge on current internal traffic to identify and categorize recurring complaint patterns, then trace each high-frequency cluster to a contributing prompt instruction or missing instruction. For example, recurring "incomplete task" complaints pointed to guidance that encouraged the agent to explain its plan rather than execute it.

**2. Design.** We write targeted candidate changes for the diagnosed issue. Candidates commonly address safety, verification, tone, or behavior, and each candidate states the intended behavior and regression risk before testing.

**3. Test.** We compare candidates with the control in isolated cohorts and, when useful, in a combined cohort that can reveal interactions. The experiment design and sample size determine whether a result is only directional or supports a broader conclusion.

**4. Evaluate.** We apply the same LLM-judge rubric to each cohort, compare dissatisfaction and behavioral-quality rates, and use the available evidence to ship, revise, or reject each candidate.

<div class="heading-anchor-wrapper">

## LLM-as-judge: measuring what matters

<a href="#llm-as-judge-measuring-what-matters" class="anchor-link" aria-label="Copy link to Llm as judge measuring what matters section"><span class="anchor-icon-wrapper"><img src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iYW5jaG9yLWljb24iIHZpZXdib3g9IjAgMCAxNiAxNyIgd2lkdGg9IjE2IiBoZWlnaHQ9IjE3IiBmaWxsPSJjdXJyZW50Q29sb3IiPjxwYXRoIGQ9Ik0yLjI3MTQzIDE0LjIyOEMwLjU5MTg5NyAxMi41NDg1IDAuNTkxODk3IDkuODI1MzkgMi4yNzE0MyA4LjE0NTg1TDMuNDIzMjQgNi45OTQwNEwzLjQ0MTg4IDYuOTc2MzVDMy42MzgxNiA2Ljc5OSAzLjk0MTE4IDYuODA0ODggNC4xMzAzNSA2Ljk5NDA0QzQuMzE5NTEgNy4xODMyMSA0LjMyNTM5IDcuNDg2MjMgNC4xNDgwNCA3LjY4MjVMNC4xMzAzNSA3LjcwMTE1TDIuOTc4NTQgOC44NTI5NkMxLjY4OTUzIDEwLjE0MiAxLjY4OTUzIDEyLjIzMTkgMi45Nzg1NCAxMy41MjA5TDMuMDA4ODggMTMuNTUwOUM0LjMwMDE0IDE0LjgwOTggNi4zNjc1MSAxNC43OTk4IDcuNjQ2NDYgMTMuNTIwOUw4Ljc5ODI3IDEyLjM2OTFMOC44MTY5MSAxMi4zNTE0QzkuMDEzMTkgMTIuMTc0IDkuMzE2MjEgMTIuMTc5OSA5LjUwNTM4IDEyLjM2OTFDOS42OTQ1NCAxMi41NTgyIDkuNzAwNDYgMTIuODYxMyA5LjUyMzExIDEzLjA1NzZMOS41MDUzOCAxMy4wNzYyTDguMzUzNTYgMTQuMjI4QzYuNjg3MTUgMTUuODk0NCAzLjk5MzQ3IDE1LjkwNzQgMi4zMTEgMTQuMjY3TDIuMjcxNDMgMTQuMjI4Wk0xMy4wMjE1IDMuNDc3OTNDMTEuNzQyNSAyLjE5ODk5IDkuNjc1MTcgMi4xODg5NiA4LjM4MzkgMy40NDc5NEw4LjM1MzU2IDMuNDc3OTNMNy4yMjU3OSA0LjYwNTdDNy4wMzA1MyA0LjgwMDk2IDYuNzEzOTUgNC44MDA5NiA2LjUxODY5IDQuNjA1N0M2LjMyMzQyIDQuNDEwNDQgNi4zMjM0MiA0LjA5Mzg2IDYuNTE4NjkgMy44OTg1OUw3LjY0NjQ2IDIuNzcwODJMNy42ODYwMyAyLjczMTc3QzkuMzY4NSAxLjA5MTM4IDEyLjA2MjIgMS4xMDQ0MSAxMy43Mjg2IDIuNzcwODJMMTMuNzY3NyAyLjgxMDM2QzE1LjM5NTIgNC40Nzk1OCAxNS4zOTUxIDcuMTQ0MTcgMTMuNzY3NyA4LjgxMzM4TDEzLjcyODYgOC44NTI5NkwxMi42MDA4IDkuOTgwNzNDMTIuNDA1NiAxMC4xNzYgMTIuMDg5IDEwLjE3NiAxMS44OTM3IDkuOTgwNzNDMTEuNjk4NSA5Ljc4NTQ3IDExLjY5ODUgOS40Njg4OCAxMS44OTM3IDkuMjczNjJMMTMuMDIxNSA4LjE0NTg1TDEzLjA1MTUgOC4xMTU1MUMxNC4zMDA1IDYuODM0NDIgMTQuMzAwNSA0Ljc4OTM3IDEzLjA1MTUgMy41MDgyN0wxMy4wMjE1IDMuNDc3OTNaIiAvPjxwYXRoIGQ9Ik0xMC4wMjE5IDUuODY2MzJMMTAuMDQwNiA1Ljg0ODU4QzEwLjIzNjkgNS42NzEyNCAxMC41Mzk5IDUuNjc3MTYgMTAuNzI5IDUuODY2MzJDMTAuOTE4MiA2LjA1NTQ4IDEwLjkyNDEgNi4zNTg0NiAxMC43NDY4IDYuNTU0NzRMMTAuNzI5IDYuNTczNDJMNi4xNDU4OCAxMS4xNTY2QzUuOTUwNjIgMTEuMzUxOCA1LjYzNDAzIDExLjM1MTggNS40Mzg3NyAxMS4xNTY2QzUuMjQzNTEgMTAuOTYxMyA1LjI0MzUxIDEwLjY0NDcgNS40Mzg3NyAxMC40NDk1TDEwLjAyMTkgNS44NjYzMloiIC8+PC9zdmc+" class="anchor-icon" /><span class="copied-indicator docsearch-exclude" aria-live="polite" aria-atomic="true"></span></span></a>

</div>

We built an evaluation framework that scores internal conversations across 15 behavioral dimensions, including:

- *Task completeness*
- *Claim accuracy* (did the agent verify before asserting?)
- *Code style adherence*
- *Recognition of repeated unsuccessful approaches*
- *Destructive-action flagging*
- *Tool use appropriateness*
- *Verification behavior* (running tests, checking compilation)

The judge requires explicit evidence from the conversation: corrections, complaints, abandoned tasks, or confirmations. Ambiguous conversations do not count against either variant, keeping comparisons consistent and conservative to avoid excessive false-positive judgments.

<div class="my-8">

<figure class="overflow-hidden rounded-2xl border border-[#4a464f] bg-muted/30">
<span class="group relative inline-block transition-all duration-200 cursor-zoom-in" style="display:block" tabindex="0" role="button" aria-label="Open image lightbox: Three connected panels: a Conversation showing a user, Kiro&#39;s edits, and a red-highlighted &#39;Did you read the files first?!&#39; complaint; a User Dissatisfaction Judge listing behavioral failure categories; and a User Dissatisfaction output card with the evidence quote and its assigned category."><span class="relative overflow-hidden h-auto w-full border-0"><span class="absolute inset-0 flex animate-pulse items-center justify-center bg-muted"><span class="sr-only">Loading image...</span></span><img src="/images/blogs/continuous-prompt-evaluation/dissatisfaction-judge-workflow.png?h=c2927056" class="transition-opacity duration-300 opacity-0" style="color:transparent" loading="lazy" decoding="async" data-nimg="1" width="1200" height="600" alt="Three connected panels: a Conversation showing a user, Kiro&#39;s edits, and a red-highlighted &#39;Did you read the files first?!&#39; complaint; a User Dissatisfaction Judge listing behavioral failure categories; and a User Dissatisfaction output card with the evidence quote and its assigned category." /></span><span class="absolute bottom-2 right-2 z-10 flex items-center justify-center rounded-full bg-prey-600/60 p-2.5 transition-opacity duration-200 opacity-100 group-hover:opacity-100" aria-hidden="true"><img src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdib3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48cGF0aCBkPSJNMTUuNjIyIDAuMDA5MTU3NTFDMTUuNzEyMyAwLjAyNzEzMzUgMTUuNzk1OSAwLjA3MTM0IDE1Ljg2MiAwLjEzNzM2M0MxNS45NSAwLjIyNTQzNiAxNS45OTk1IDAuMzQ1MjI2IDE1Ljk5OTMgMC40Njk3OEwxNS45OTI5IDUuNDIzMDhMMTUuOTgzNyA1LjUxNzRDMTUuOTM5OSA1LjczMTA2IDE1Ljc1MDYgNS44OTIwNCAxNS41MjQgNS44OTE5NEMxNS4yNjUxIDUuODkxNjIgMTUuMDU0OSA1LjY4MTA2IDE1LjA1NTIgNS40MjIxNkwxNS4wNTk3IDEuNjAxNjVMMTAuMTc2OSA2LjQ4NTM1QzkuOTkzODQgNi42Njg0NSA5LjY5NzA0IDYuNjY4NDUgOS41MTM5NCA2LjQ4NTM1QzkuMzMwODMgNi4zMDIyNCA5LjMzMDgzIDYuMDA1NDUgOS41MTM5NCA1LjgyMjM0TDE0LjM5NjcgMC45Mzg2NDVMMTAuNTc3MSAwLjk0NDEzOUwxMC40ODI4IDAuOTM0OTgyQzEwLjI2OSAwLjg5MTU4NCAxMC4xMDc2IDAuNzAxOTAzIDEwLjEwNzMgMC40NzUyNzVDMTAuMTA3MiAwLjIxNjUwNyAxMC4zMTc0IDAuMDA2NzM0ODQgMTAuNTc2MiAwLjAwNjQxMDI2TDE1LjUyOTUgMEwxNS42MjIgMC4wMDkxNTc1MVoiIGZpbGw9ImN1cnJlbnRDb2xvciIgLz48cGF0aCBkPSJNMC4zNzcyOSAxNS45OTA4QzAuMjg3MDU3IDE1Ljk3MjkgMC4yMDMzODUgMTUuOTI4NyAwLjEzNzM2MiAxNS44NjI2QzAuMDQ5Mjg4OCAxNS43NzQ2IC0wLjAwMDE1NzAyNCAxNS42NTQ4IC04LjE4MjM1ZS0wNyAxNS41MzAyTDAuMDA2NDA5NDcgMTAuNTc2OUwwLjAxNTU2NyAxMC40ODI2QzAuMDU5Mzg5MSAxMC4yNjg5IDAuMjQ4NzQxIDEwLjEwOCAwLjQ3NTI3NiAxMC4xMDgxQzAuNzM0MTkxIDEwLjEwODQgMC45NDQ0MTUgMTAuMzE4OSAwLjk0NDE0MyAxMC41Nzc4TDAuOTM5NTY0IDE0LjM5ODRMNS44MjIzNyA5LjUxNDY1QzYuMDA1NDcgOS4zMzE1NSA2LjMwMjI3IDkuMzMxNTUgNi40ODUzOCA5LjUxNDY1QzYuNjY4NDggOS42OTc3NiA2LjY2ODQ4IDkuOTk0NTUgNi40ODUzOCAxMC4xNzc3TDEuNjAyNTcgMTUuMDYxNEw1LjQyMjE4IDE1LjA1NTlMNS41MTY1MSAxNS4wNjVDNS43MzAyOSAxNS4xMDg0IDUuODkxNjggMTUuMjk4MSA1Ljg5MTk3IDE1LjUyNDdDNS44OTIwOCAxNS43ODM1IDUuNjgxOTIgMTUuOTkzMyA1LjQyMzEgMTUuOTkzNkwwLjQ2OTc4MSAxNkwwLjM3NzI5IDE1Ljk5MDhaIiBmaWxsPSJjdXJyZW50Q29sb3IiIC8+PC9zdmc+" /></span></span>
<figcaption>Figure 2: How the LLM judge reads a conversation—chat exchanges on the left, dissatisfaction criteria in the middle, and categorized behavioral-quality output on the right.</figcaption>
</figure>

</div>

*The judge prompts represented in the figure are minimal illustrative examples and are not what is actually used during evaluation.*

The judge measures two primary signals:

- **Explicit dissatisfaction:** Did the user explicitly express frustration, abandon the conversation, or redo the agent's work? This is inferred only from explicit feedback in the conversation, not from implied tool results or survey scores.
- **Behavioral quality issues:** Did the agent miss one of the 15 quality standards? Examples include making claims without first reading the code, stopping before completing the task, or disregarding the project's existing patterns.

Both metrics use the same rubric across control and treatment groups, supporting consistent comparisons between configurations within the same evaluation design.

<div class="my-8">

<figure class="overflow-hidden rounded-2xl border border-[#4a464f] bg-muted/30">
<span class="group relative inline-block transition-all duration-200 cursor-zoom-in" style="display:block" tabindex="0" role="button" aria-label="Open image lightbox: Flowchart: a &#39;Conversations for Analysis&#39; cylinder on the left, stacked groups for Cohort 1, Cohort 2, through Cohort N in the middle feeding a central Dissatisfaction Judge box, and a result card for each cohort on the right."><span class="relative overflow-hidden h-auto w-full border-0"><span class="absolute inset-0 flex animate-pulse items-center justify-center bg-muted"><span class="sr-only">Loading image...</span></span><img src="/images/blogs/continuous-prompt-evaluation/dissatisfaction-judge-high-level.png?h=22d6f93a" class="transition-opacity duration-300 opacity-0" style="color:transparent" loading="lazy" decoding="async" data-nimg="1" width="1200" height="600" alt="Flowchart: a &#39;Conversations for Analysis&#39; cylinder on the left, stacked groups for Cohort 1, Cohort 2, through Cohort N in the middle feeding a central Dissatisfaction Judge box, and a result card for each cohort on the right." /></span><span class="absolute bottom-2 right-2 z-10 flex items-center justify-center rounded-full bg-prey-600/60 p-2.5 transition-opacity duration-200 opacity-100 group-hover:opacity-100" aria-hidden="true"><img src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdib3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48cGF0aCBkPSJNMTUuNjIyIDAuMDA5MTU3NTFDMTUuNzEyMyAwLjAyNzEzMzUgMTUuNzk1OSAwLjA3MTM0IDE1Ljg2MiAwLjEzNzM2M0MxNS45NSAwLjIyNTQzNiAxNS45OTk1IDAuMzQ1MjI2IDE1Ljk5OTMgMC40Njk3OEwxNS45OTI5IDUuNDIzMDhMMTUuOTgzNyA1LjUxNzRDMTUuOTM5OSA1LjczMTA2IDE1Ljc1MDYgNS44OTIwNCAxNS41MjQgNS44OTE5NEMxNS4yNjUxIDUuODkxNjIgMTUuMDU0OSA1LjY4MTA2IDE1LjA1NTIgNS40MjIxNkwxNS4wNTk3IDEuNjAxNjVMMTAuMTc2OSA2LjQ4NTM1QzkuOTkzODQgNi42Njg0NSA5LjY5NzA0IDYuNjY4NDUgOS41MTM5NCA2LjQ4NTM1QzkuMzMwODMgNi4zMDIyNCA5LjMzMDgzIDYuMDA1NDUgOS41MTM5NCA1LjgyMjM0TDE0LjM5NjcgMC45Mzg2NDVMMTAuNTc3MSAwLjk0NDEzOUwxMC40ODI4IDAuOTM0OTgyQzEwLjI2OSAwLjg5MTU4NCAxMC4xMDc2IDAuNzAxOTAzIDEwLjEwNzMgMC40NzUyNzVDMTAuMTA3MiAwLjIxNjUwNyAxMC4zMTc0IDAuMDA2NzM0ODQgMTAuNTc2MiAwLjAwNjQxMDI2TDE1LjUyOTUgMEwxNS42MjIgMC4wMDkxNTc1MVoiIGZpbGw9ImN1cnJlbnRDb2xvciIgLz48cGF0aCBkPSJNMC4zNzcyOSAxNS45OTA4QzAuMjg3MDU3IDE1Ljk3MjkgMC4yMDMzODUgMTUuOTI4NyAwLjEzNzM2MiAxNS44NjI2QzAuMDQ5Mjg4OCAxNS43NzQ2IC0wLjAwMDE1NzAyNCAxNS42NTQ4IC04LjE4MjM1ZS0wNyAxNS41MzAyTDAuMDA2NDA5NDcgMTAuNTc2OUwwLjAxNTU2NyAxMC40ODI2QzAuMDU5Mzg5MSAxMC4yNjg5IDAuMjQ4NzQxIDEwLjEwOCAwLjQ3NTI3NiAxMC4xMDgxQzAuNzM0MTkxIDEwLjEwODQgMC45NDQ0MTUgMTAuMzE4OSAwLjk0NDE0MyAxMC41Nzc4TDAuOTM5NTY0IDE0LjM5ODRMNS44MjIzNyA5LjUxNDY1QzYuMDA1NDcgOS4zMzE1NSA2LjMwMjI3IDkuMzMxNTUgNi40ODUzOCA5LjUxNDY1QzYuNjY4NDggOS42OTc3NiA2LjY2ODQ4IDkuOTk0NTUgNi40ODUzOCAxMC4xNzc3TDEuNjAyNTcgMTUuMDYxNEw1LjQyMjE4IDE1LjA1NTlMNS41MTY1MSAxNS4wNjVDNS43MzAyOSAxNS4xMDg0IDUuODkxNjggMTUuMjk4MSA1Ljg5MTk3IDE1LjUyNDdDNS44OTIwOCAxNS43ODM1IDUuNjgxOTIgMTUuOTkzMyA1LjQyMzEgMTUuOTkzNkwwLjQ2OTc4MSAxNkwwLjM3NzI5IDE1Ljk5MDhaIiBmaWxsPSJjdXJyZW50Q29sb3IiIC8+PC9zdmc+" /></span></span>
<figcaption>Figure 3: Conversations flow from storage through per-cohort buckets into the dissatisfaction judge, which outputs dissatisfaction rates and behavioral-issue counts per cohort.</figcaption>
</figure>

</div>

<div class="heading-anchor-wrapper">

## A/B experiment infrastructure

<a href="#ab-experiment-infrastructure" class="anchor-link" aria-label="Copy link to Ab experiment infrastructure section"><span class="anchor-icon-wrapper"><img src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iYW5jaG9yLWljb24iIHZpZXdib3g9IjAgMCAxNiAxNyIgd2lkdGg9IjE2IiBoZWlnaHQ9IjE3IiBmaWxsPSJjdXJyZW50Q29sb3IiPjxwYXRoIGQ9Ik0yLjI3MTQzIDE0LjIyOEMwLjU5MTg5NyAxMi41NDg1IDAuNTkxODk3IDkuODI1MzkgMi4yNzE0MyA4LjE0NTg1TDMuNDIzMjQgNi45OTQwNEwzLjQ0MTg4IDYuOTc2MzVDMy42MzgxNiA2Ljc5OSAzLjk0MTE4IDYuODA0ODggNC4xMzAzNSA2Ljk5NDA0QzQuMzE5NTEgNy4xODMyMSA0LjMyNTM5IDcuNDg2MjMgNC4xNDgwNCA3LjY4MjVMNC4xMzAzNSA3LjcwMTE1TDIuOTc4NTQgOC44NTI5NkMxLjY4OTUzIDEwLjE0MiAxLjY4OTUzIDEyLjIzMTkgMi45Nzg1NCAxMy41MjA5TDMuMDA4ODggMTMuNTUwOUM0LjMwMDE0IDE0LjgwOTggNi4zNjc1MSAxNC43OTk4IDcuNjQ2NDYgMTMuNTIwOUw4Ljc5ODI3IDEyLjM2OTFMOC44MTY5MSAxMi4zNTE0QzkuMDEzMTkgMTIuMTc0IDkuMzE2MjEgMTIuMTc5OSA5LjUwNTM4IDEyLjM2OTFDOS42OTQ1NCAxMi41NTgyIDkuNzAwNDYgMTIuODYxMyA5LjUyMzExIDEzLjA1NzZMOS41MDUzOCAxMy4wNzYyTDguMzUzNTYgMTQuMjI4QzYuNjg3MTUgMTUuODk0NCAzLjk5MzQ3IDE1LjkwNzQgMi4zMTEgMTQuMjY3TDIuMjcxNDMgMTQuMjI4Wk0xMy4wMjE1IDMuNDc3OTNDMTEuNzQyNSAyLjE5ODk5IDkuNjc1MTcgMi4xODg5NiA4LjM4MzkgMy40NDc5NEw4LjM1MzU2IDMuNDc3OTNMNy4yMjU3OSA0LjYwNTdDNy4wMzA1MyA0LjgwMDk2IDYuNzEzOTUgNC44MDA5NiA2LjUxODY5IDQuNjA1N0M2LjMyMzQyIDQuNDEwNDQgNi4zMjM0MiA0LjA5Mzg2IDYuNTE4NjkgMy44OTg1OUw3LjY0NjQ2IDIuNzcwODJMNy42ODYwMyAyLjczMTc3QzkuMzY4NSAxLjA5MTM4IDEyLjA2MjIgMS4xMDQ0MSAxMy43Mjg2IDIuNzcwODJMMTMuNzY3NyAyLjgxMDM2QzE1LjM5NTIgNC40Nzk1OCAxNS4zOTUxIDcuMTQ0MTcgMTMuNzY3NyA4LjgxMzM4TDEzLjcyODYgOC44NTI5NkwxMi42MDA4IDkuOTgwNzNDMTIuNDA1NiAxMC4xNzYgMTIuMDg5IDEwLjE3NiAxMS44OTM3IDkuOTgwNzNDMTEuNjk4NSA5Ljc4NTQ3IDExLjY5ODUgOS40Njg4OCAxMS44OTM3IDkuMjczNjJMMTMuMDIxNSA4LjE0NTg1TDEzLjA1MTUgOC4xMTU1MUMxNC4zMDA1IDYuODM0NDIgMTQuMzAwNSA0Ljc4OTM3IDEzLjA1MTUgMy41MDgyN0wxMy4wMjE1IDMuNDc3OTNaIiAvPjxwYXRoIGQ9Ik0xMC4wMjE5IDUuODY2MzJMMTAuMDQwNiA1Ljg0ODU4QzEwLjIzNjkgNS42NzEyNCAxMC41Mzk5IDUuNjc3MTYgMTAuNzI5IDUuODY2MzJDMTAuOTE4MiA2LjA1NTQ4IDEwLjkyNDEgNi4zNTg0NiAxMC43NDY4IDYuNTU0NzRMMTAuNzI5IDYuNTczNDJMNi4xNDU4OCAxMS4xNTY2QzUuOTUwNjIgMTEuMzUxOCA1LjYzNDAzIDExLjM1MTggNS40Mzg3NyAxMS4xNTY2QzUuMjQzNTEgMTAuOTYxMyA1LjI0MzUxIDEwLjY0NDcgNS40Mzg3NyAxMC40NDk1TDEwLjAyMTkgNS44NjYzMloiIC8+PC9zdmc+" class="anchor-icon" /><span class="copied-indicator docsearch-exclude" aria-live="polite" aria-atomic="true"></span></span></a>

</div>

Before shipping a prompt change, we compare configurations in separate cohorts on internal traffic. For these experiments, the service assigns eligible internal developers to stable user buckets using a deterministic hash of user identity, independent of observed conversation outcomes. Each bucket maps to one prompt variant for a given experiment.

The judge pipeline analyzes conversations by their recorded experiment allocation and applies the same rubric to every cohort. Stable assignment controls cohort selection within the prompt experiment, but it does not eliminate every source of bias or interaction in live traffic. Exact allocation and sample size vary by experiment, so the strength of a conclusion depends on the evidence available for that comparison. Small isolated candidate cohorts remain directional diagnostics rather than precise estimates of production impact.

In one accelerated internal deployment, we screened 27 candidate prompt changes across four categories: safety, verification, tone, and behavior. We compared a stable control with isolated candidate cohorts and a cohort that combined the candidates. The small isolated cohorts were directional diagnostics for localizing possible regressions, not individually powered estimates of impact. Candidates that showed degradation were revised or removed, while combined and larger follow-up comparisons supported broader conclusions.

Because the judge pipeline scores conversation outcomes, it can also compare user-visible configuration choices. We have used it to evaluate default reasoning effort levels, where common tasks such as code modification and debugging showed gains from higher effort levels. For more information on configuring reasoning effort levels, see the <a href="/docs/models/effort/" class="text-primary hover:underline">reasoning effort documentation</a>.

<div class="heading-anchor-wrapper">

## Results from recent cycles

<a href="#results-from-recent-cycles" class="anchor-link" aria-label="Copy link to Results from recent cycles section"><span class="anchor-icon-wrapper"><img src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iYW5jaG9yLWljb24iIHZpZXdib3g9IjAgMCAxNiAxNyIgd2lkdGg9IjE2IiBoZWlnaHQ9IjE3IiBmaWxsPSJjdXJyZW50Q29sb3IiPjxwYXRoIGQ9Ik0yLjI3MTQzIDE0LjIyOEMwLjU5MTg5NyAxMi41NDg1IDAuNTkxODk3IDkuODI1MzkgMi4yNzE0MyA4LjE0NTg1TDMuNDIzMjQgNi45OTQwNEwzLjQ0MTg4IDYuOTc2MzVDMy42MzgxNiA2Ljc5OSAzLjk0MTE4IDYuODA0ODggNC4xMzAzNSA2Ljk5NDA0QzQuMzE5NTEgNy4xODMyMSA0LjMyNTM5IDcuNDg2MjMgNC4xNDgwNCA3LjY4MjVMNC4xMzAzNSA3LjcwMTE1TDIuOTc4NTQgOC44NTI5NkMxLjY4OTUzIDEwLjE0MiAxLjY4OTUzIDEyLjIzMTkgMi45Nzg1NCAxMy41MjA5TDMuMDA4ODggMTMuNTUwOUM0LjMwMDE0IDE0LjgwOTggNi4zNjc1MSAxNC43OTk4IDcuNjQ2NDYgMTMuNTIwOUw4Ljc5ODI3IDEyLjM2OTFMOC44MTY5MSAxMi4zNTE0QzkuMDEzMTkgMTIuMTc0IDkuMzE2MjEgMTIuMTc5OSA5LjUwNTM4IDEyLjM2OTFDOS42OTQ1NCAxMi41NTgyIDkuNzAwNDYgMTIuODYxMyA5LjUyMzExIDEzLjA1NzZMOS41MDUzOCAxMy4wNzYyTDguMzUzNTYgMTQuMjI4QzYuNjg3MTUgMTUuODk0NCAzLjk5MzQ3IDE1LjkwNzQgMi4zMTEgMTQuMjY3TDIuMjcxNDMgMTQuMjI4Wk0xMy4wMjE1IDMuNDc3OTNDMTEuNzQyNSAyLjE5ODk5IDkuNjc1MTcgMi4xODg5NiA4LjM4MzkgMy40NDc5NEw4LjM1MzU2IDMuNDc3OTNMNy4yMjU3OSA0LjYwNTdDNy4wMzA1MyA0LjgwMDk2IDYuNzEzOTUgNC44MDA5NiA2LjUxODY5IDQuNjA1N0M2LjMyMzQyIDQuNDEwNDQgNi4zMjM0MiA0LjA5Mzg2IDYuNTE4NjkgMy44OTg1OUw3LjY0NjQ2IDIuNzcwODJMNy42ODYwMyAyLjczMTc3QzkuMzY4NSAxLjA5MTM4IDEyLjA2MjIgMS4xMDQ0MSAxMy43Mjg2IDIuNzcwODJMMTMuNzY3NyAyLjgxMDM2QzE1LjM5NTIgNC40Nzk1OCAxNS4zOTUxIDcuMTQ0MTcgMTMuNzY3NyA4LjgxMzM4TDEzLjcyODYgOC44NTI5NkwxMi42MDA4IDkuOTgwNzNDMTIuNDA1NiAxMC4xNzYgMTIuMDg5IDEwLjE3NiAxMS44OTM3IDkuOTgwNzNDMTEuNjk4NSA5Ljc4NTQ3IDExLjY5ODUgOS40Njg4OCAxMS44OTM3IDkuMjczNjJMMTMuMDIxNSA4LjE0NTg1TDEzLjA1MTUgOC4xMTU1MUMxNC4zMDA1IDYuODM0NDIgMTQuMzAwNSA0Ljc4OTM3IDEzLjA1MTUgMy41MDgyN0wxMy4wMjE1IDMuNDc3OTNaIiAvPjxwYXRoIGQ9Ik0xMC4wMjE5IDUuODY2MzJMMTAuMDQwNiA1Ljg0ODU4QzEwLjIzNjkgNS42NzEyNCAxMC41Mzk5IDUuNjc3MTYgMTAuNzI5IDUuODY2MzJDMTAuOTE4MiA2LjA1NTQ4IDEwLjkyNDEgNi4zNTg0NiAxMC43NDY4IDYuNTU0NzRMMTAuNzI5IDYuNTczNDJMNi4xNDU4OCAxMS4xNTY2QzUuOTUwNjIgMTEuMzUxOCA1LjYzNDAzIDExLjM1MTggNS40Mzg3NyAxMS4xNTY2QzUuMjQzNTEgMTAuOTYxMyA1LjI0MzUxIDEwLjY0NDcgNS40Mzg3NyAxMC40NDk1TDEwLjAyMTkgNS44NjYzMloiIC8+PC9zdmc+" class="anchor-icon" /><span class="copied-indicator docsearch-exclude" aria-live="polite" aria-atomic="true"></span></span></a>

</div>

The figures below are observed deltas from internal experiment-level comparisons. They describe these evaluation samples and should not be read as universal production-effect estimates.

<div class="heading-anchor-wrapper">

### Initial model-and-prompt experiments

<a href="#initial-model-and-prompt-experiments" class="anchor-link" aria-label="Copy link to Initial model and prompt experiments section"><span class="anchor-icon-wrapper"><img src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iYW5jaG9yLWljb24iIHZpZXdib3g9IjAgMCAxNiAxNyIgd2lkdGg9IjE2IiBoZWlnaHQ9IjE3IiBmaWxsPSJjdXJyZW50Q29sb3IiPjxwYXRoIGQ9Ik0yLjI3MTQzIDE0LjIyOEMwLjU5MTg5NyAxMi41NDg1IDAuNTkxODk3IDkuODI1MzkgMi4yNzE0MyA4LjE0NTg1TDMuNDIzMjQgNi45OTQwNEwzLjQ0MTg4IDYuOTc2MzVDMy42MzgxNiA2Ljc5OSAzLjk0MTE4IDYuODA0ODggNC4xMzAzNSA2Ljk5NDA0QzQuMzE5NTEgNy4xODMyMSA0LjMyNTM5IDcuNDg2MjMgNC4xNDgwNCA3LjY4MjVMNC4xMzAzNSA3LjcwMTE1TDIuOTc4NTQgOC44NTI5NkMxLjY4OTUzIDEwLjE0MiAxLjY4OTUzIDEyLjIzMTkgMi45Nzg1NCAxMy41MjA5TDMuMDA4ODggMTMuNTUwOUM0LjMwMDE0IDE0LjgwOTggNi4zNjc1MSAxNC43OTk4IDcuNjQ2NDYgMTMuNTIwOUw4Ljc5ODI3IDEyLjM2OTFMOC44MTY5MSAxMi4zNTE0QzkuMDEzMTkgMTIuMTc0IDkuMzE2MjEgMTIuMTc5OSA5LjUwNTM4IDEyLjM2OTFDOS42OTQ1NCAxMi41NTgyIDkuNzAwNDYgMTIuODYxMyA5LjUyMzExIDEzLjA1NzZMOS41MDUzOCAxMy4wNzYyTDguMzUzNTYgMTQuMjI4QzYuNjg3MTUgMTUuODk0NCAzLjk5MzQ3IDE1LjkwNzQgMi4zMTEgMTQuMjY3TDIuMjcxNDMgMTQuMjI4Wk0xMy4wMjE1IDMuNDc3OTNDMTEuNzQyNSAyLjE5ODk5IDkuNjc1MTcgMi4xODg5NiA4LjM4MzkgMy40NDc5NEw4LjM1MzU2IDMuNDc3OTNMNy4yMjU3OSA0LjYwNTdDNy4wMzA1MyA0LjgwMDk2IDYuNzEzOTUgNC44MDA5NiA2LjUxODY5IDQuNjA1N0M2LjMyMzQyIDQuNDEwNDQgNi4zMjM0MiA0LjA5Mzg2IDYuNTE4NjkgMy44OTg1OUw3LjY0NjQ2IDIuNzcwODJMNy42ODYwMyAyLjczMTc3QzkuMzY4NSAxLjA5MTM4IDEyLjA2MjIgMS4xMDQ0MSAxMy43Mjg2IDIuNzcwODJMMTMuNzY3NyAyLjgxMDM2QzE1LjM5NTIgNC40Nzk1OCAxNS4zOTUxIDcuMTQ0MTcgMTMuNzY3NyA4LjgxMzM4TDEzLjcyODYgOC44NTI5NkwxMi42MDA4IDkuOTgwNzNDMTIuNDA1NiAxMC4xNzYgMTIuMDg5IDEwLjE3NiAxMS44OTM3IDkuOTgwNzNDMTEuNjk4NSA5Ljc4NTQ3IDExLjY5ODUgOS40Njg4OCAxMS44OTM3IDkuMjczNjJMMTMuMDIxNSA4LjE0NTg1TDEzLjA1MTUgOC4xMTU1MUMxNC4zMDA1IDYuODM0NDIgMTQuMzAwNSA0Ljc4OTM3IDEzLjA1MTUgMy41MDgyN0wxMy4wMjE1IDMuNDc3OTNaIiAvPjxwYXRoIGQ9Ik0xMC4wMjE5IDUuODY2MzJMMTAuMDQwNiA1Ljg0ODU4QzEwLjIzNjkgNS42NzEyNCAxMC41Mzk5IDUuNjc3MTYgMTAuNzI5IDUuODY2MzJDMTAuOTE4MiA2LjA1NTQ4IDEwLjkyNDEgNi4zNTg0NiAxMC43NDY4IDYuNTU0NzRMMTAuNzI5IDYuNTczNDJMNi4xNDU4OCAxMS4xNTY2QzUuOTUwNjIgMTEuMzUxOCA1LjYzNDAzIDExLjM1MTggNS40Mzg3NyAxMS4xNTY2QzUuMjQzNTEgMTAuOTYxMyA1LjI0MzUxIDEwLjY0NDcgNS40Mzg3NyAxMC40NDk1TDEwLjAyMTkgNS44NjYzMloiIC8+PC9zdmc+" class="anchor-icon" /><span class="copied-indicator docsearch-exclude" aria-live="polite" aria-atomic="true"></span></span></a>

</div>

<a href="/cli/" class="text-primary hover:underline"><strong>Kiro CLI</strong></a> (first evaluated model-and-prompt configuration):

- Explicit dissatisfaction signals: **down 5%**
- Behavioral quality issues: **down 32%**
- Task completeness issues: **down 10.6%**

<a href="/ide/" class="text-primary hover:underline"><strong>Kiro IDE</strong></a> (first evaluated model-and-prompt configuration):

- Behavioral quality issues: **down 20%**
- Incomplete task delivery: **down 21%**
- Repeated unsuccessful approaches: **down 36%**
- Style mismatches: **down 54%**

<div class="heading-anchor-wrapper">

### Re-validation on a newer model

<a href="#re-validation-on-a-newer-model" class="anchor-link" aria-label="Copy link to Re validation on a newer model section"><span class="anchor-icon-wrapper"><img src="data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iYW5jaG9yLWljb24iIHZpZXdib3g9IjAgMCAxNiAxNyIgd2lkdGg9IjE2IiBoZWlnaHQ9IjE3IiBmaWxsPSJjdXJyZW50Q29sb3IiPjxwYXRoIGQ9Ik0yLjI3MTQzIDE0LjIyOEMwLjU5MTg5NyAxMi41NDg1IDAuNTkxODk3IDkuODI1MzkgMi4yNzE0MyA4LjE0NTg1TDMuNDIzMjQgNi45OTQwNEwzLjQ0MTg4IDYuOTc2MzVDMy42MzgxNiA2Ljc5OSAzLjk0MTE4IDYuODA0ODggNC4xMzAzNSA2Ljk5NDA0QzQuMzE5NTEgNy4xODMyMSA0LjMyNTM5IDcuNDg2MjMgNC4xNDgwNCA3LjY4MjVMNC4xMzAzNSA3LjcwMTE1TDIuOTc4NTQgOC44NTI5NkMxLjY4OTUzIDEwLjE0MiAxLjY4OTUzIDEyLjIzMTkgMi45Nzg1NCAxMy41MjA5TDMuMDA4ODggMTMuNTUwOUM0LjMwMDE0IDE0LjgwOTggNi4zNjc1MSAxNC43OTk4IDcuNjQ2NDYgMTMuNTIwOUw4Ljc5ODI3IDEyLjM2OTFMOC44MTY5MSAxMi4zNTE0QzkuMDEzMTkgMTIuMTc0IDkuMzE2MjEgMTIuMTc5OSA5LjUwNTM4IDEyLjM2OTFDOS42OTQ1NCAxMi41NTgyIDkuNzAwNDYgMTIuODYxMyA5LjUyMzExIDEzLjA1NzZMOS41MDUzOCAxMy4wNzYyTDguMzUzNTYgMTQuMjI4QzYuNjg3MTUgMTUuODk0NCAzLjk5MzQ3IDE1LjkwNzQgMi4zMTEgMTQuMjY3TDIuMjcxNDMgMTQuMjI4Wk0xMy4wMjE1IDMuNDc3OTNDMTEuNzQyNSAyLjE5ODk5IDkuNjc1MTcgMi4xODg5NiA4LjM4MzkgMy40NDc5NEw4LjM1MzU2IDMuNDc3OTNMNy4yMjU3OSA0LjYwNTdDNy4wMzA1MyA0LjgwMDk2IDYuNzEzOTUgNC44MDA5NiA2LjUxODY5IDQuNjA1N0M2LjMyMzQyIDQuNDEwNDQgNi4zMjM0MiA0LjA5Mzg2IDYuNTE4NjkgMy44OTg1OUw3LjY0NjQ2IDIuNzcwODJMNy42ODYwMyAyLjczMTc3QzkuMzY4NSAxLjA5MTM4IDEyLjA2MjIgMS4xMDQ0MSAxMy43Mjg2IDIuNzcwODJMMTMuNzY3NyAyLjgxMDM2QzE1LjM5NTIgNC40Nzk1OCAxNS4zOTUxIDcuMTQ0MTcgMTMuNzY3NyA4LjgxMzM4TDEzLjcyODYgOC44NTI5NkwxMi42MDA4IDkuOTgwNzNDMTIuNDA1NiAxMC4xNzYgMTIuMDg5IDEwLjE3NiAxMS44OTM3IDkuOTgwNzNDMTEuNjk4NSA5Ljc4NTQ3IDExLjY5ODUgOS40Njg4OCAxMS44OTM3IDkuMjczNjJMMTMuMDIxNSA4LjE0NTg1TDEzLjA1MTUgOC4xMTU1MUMxNC4zMDA1IDYuODM0NDIgMTQuMzAwNSA0Ljc4OTM3IDEzLjA1MTUgMy41MDgyN0wxMy4wMjE1IDMuNDc3OTNaIiAvPjxwYXRoIGQ9Ik0xMC4wMjE5IDUuODY2MzJMMTAuMDQwNiA1Ljg0ODU4QzEwLjIzNjkgNS42NzEyNCAxMC41Mzk5IDUuNjc3MTYgMTAuNzI5IDUuODY2MzJDMTAuOTE4MiA2LjA1NTQ4IDEwLjkyNDEgNi4zNTg0NiAxMC43NDY4IDYuNTU0NzRMMTAuNzI5IDYuNTczNDJMNi4xNDU4OCAxMS4xNTY2QzUuOTUwNjIgMTEuMzUxOCA1LjYzNDAzIDExLjM1MTggNS40Mzg3NyAxMS4xNTY2QzUuMjQzNTEgMTAuOTYxMyA1LjI0MzUxIDEwLjY0NDcgNS40Mzg3NyAxMC40NDk1TDEwLjAyMTkgNS44NjYzMloiIC8+PC9zdmc+" class="anchor-icon" /><span class="copied-indicator docsearch-exclude" aria-live="polite" aria-atomic="true"></span></span></a>

</div>

Re-validation answers a different question from the initial 

[truncated]
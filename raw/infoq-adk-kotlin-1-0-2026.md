# InfoQ — Google ADK for Kotlin Reaches Feature Parity with Python, Supports On-Device AI (2026-09-20)

**Author:** Sergio De Simone (InfoQ)
**Source:** https://www.infoq.com/news/2026/09/google-adk-1-0-released/
**Context:** InfoQ news on Google Agent Development Kit (ADK) 1.0 for Kotlin. Relevant to multi-agent orchestration, HITL tool confirmation, SKILL.md progressive disclosure. Date 2026-09-20.

---
Google released the Agent Development Kit (ADK) for Kotlin 1.0, a production-ready framework for building AI agents across Kotlin, Android, and JVM/server applications. Brings Kotlin to feature parity with ADK for Python and Java, adding Android-specific capabilities for on-device and hybrid AI.

No longer need Python for agentic logic: idiomatic Kotlin APIs for orchestration, tool support, persistence, memory, human-in-the-loop workflows. Built on Kotlin Multiplatform, runs from server-side to mobile. Architecture "completely agnostic to specific model backends, session providers, or memory systems".

ADK for Kotlin 1.0 features:
- hierarchical multi-agent systems (parent agent can delegate tasks to a child)
- context compaction and multi-turn conversation (automatic context management and history summarization to reduce token usage)
- session management (agent state paused, serialized, restored)
- first-class Java interoperability

Tools & HITL: tools declared via annotations `@Tool` and `@Param`, KSP generates Kotlin function schemas at compile time (no runtime reflection — type-safety + performance). PiNCAMP Android engineer Arjun Kumar: "handling tool schemas at compile time with KSP keeps startup fast on mobile targets".

Human-in-the-loop: `requireConfirmation` in a tool's declaration forces explicit human confirmation before sensitive actions (e.g. bank transfer):

```kotlin
@Tool(name = "transferFunds", requireConfirmation = true)
fun transferFunds(...)
```

- Android persistence: chat sessions in Room, indexed memory in AppSearch, files in Android storage.

Joske Vermeulen (AI Dev Weekly): "Start with one resumable agent and explicit tool confirmation before reaching for a hierarchy of agents. Production readiness depends more on lifecycle recovery and deterministic tool boundaries than on agent count."

Skills: procedural knowledge in `SKILL.md` files, loaded dynamically only when needed — *progressive disclosure* — domain playbooks without including the entire playbook in model context every time.

On-device inference: LiteRT-LM and ML Kit (beta); cloud/hybrid via Firebase AI Logic. Open source: https://github.com/google/adk-kotlin
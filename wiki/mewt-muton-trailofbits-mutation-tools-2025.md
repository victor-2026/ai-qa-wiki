---
source: "mewt-muton-trailofbits-mutation-tools-2025.md"
ingested: "2026-10-01"
title: "mewt and muton: Trail of Bits Mutation Testing Tools"
type: article
tags: [mutation-testing, tools, trail-of-bits, agentic]
---

## Summary

mewt and muton are open-source mutation testing tools optimized for agentic use, released by Trail of Bits. mewt supports Go, JS/TS, Rust, Solidity. muton targets TON smart contracts. Both use SQLite for resumable campaigns and severity-based skip optimization.

## mewt

| Feature | Value |
|---------|-------|
| Languages | Go, JS/TS, Rust, Solidity |
| Storage | SQLite |
| Resumable | Yes |
| Skip optimization | Yes |
| License | AGPL-3.0 |

## muton

| Feature | Value |
|---------|-------|
| Languages | FunC, Tact, Tolk (TON) |
| Storage | SQLite |
| Install | npm install -g @trailofbits/muton |
| License | AGPL-3.0 |

## Shared Architecture

- SQLite database for persistent, resumable campaigns
- Severity-based skip optimization (--comprehensive to disable)
- Multi-language project support
- Pre-built binaries (macOS aarch64, Linux x86_64)

## Key Insights

- Designed for agentic/AI-assisted mutation testing workflows
- SQLite enables persistent campaigns (critical for long runs)
- TON smart contract coverage fills blockchain testing gap
- Open source (AGPL-3.0)

## See also

- [[mutation-testing-vs-code-coverage-autonoma]] - Tools landscape
- [[secmutbench-security-mutation-testing-2026]] - Security MT
- [[quantum-mutation-testing-2025]] - Quantum MT
- [[witness-predictive-mutation-testing-2026]] - Predictive MT

---
*Source: [raw/mewt-muton-trailofbits-mutation-tools-2025.md](../raw/mewt-muton-trailofbits-mutation-tools-2025.md) · Trail of Bits 2025-2026*

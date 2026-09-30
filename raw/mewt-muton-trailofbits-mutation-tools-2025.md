# mewt and muton: Trail of Bits Mutation Testing Tools for Agentic Era

**Source:** https://github.com/trailofbits/mewt + https://github.com/trailofbits/muton
**Published:** 2025-2026

## Summary

mewt and muton are open-source mutation testing tools optimized for agentic use, released by Trail of Bits. mewt supports Go, JavaScript/TypeScript, Rust, and Solidity. muton targets TON smart contracts (FunC, Tact, Tolk). Both use SQLite for resumable campaigns and feature skip optimization.

## mewt - Key Features

- **Languages:** Go, JavaScript/TypeScript, Rust, Solidity
- **Storage:** SQLite (muton.sqlite)
- **Resumable:** Interrupted campaigns resume where left off
- **Skip optimization:** Less-severe mutants on a line skipped if more-severe mutant already uncaught
- **Config:** mewt.toml (walks up from cwd)
- **Install:** curl installer or cargo build
- **Use case:** Agentic mutation testing campaigns (can run overnight)

## muton - Key Features

- **Languages:** FunC (.fc, .func), Tact (.tact), Tolk (.tolk)
- **Target:** TON blockchain smart contracts
- **Storage:** SQLite (muton.sqlite)
- **Install:** npm install -g @trailofbits/muton
- **Config:** muton.toml
- **Test command:** Pass --test.cmd (e.g., "npx blueprint test")
- **Use case:** Smart contract mutation testing

## Shared Architecture

- **SQLite database:** Targets, mutants, results in single file
- **Resume capability:** Campaigns can be interrupted and resumed
- **Severity-based skip:** Configurable via --comprehensive flag
- **Multi-language:** Mixed-language projects supported
- **Pre-built binaries:** macOS (aarch64) and Linux (x86_64)

## Configuration Example (muton)

```toml
[test]
timeout = 120
```

## CLI Commands (muton)

```bash
muton init
muton run path/to/contract.tact --test.cmd "npx blueprint test"
muton status
muton results --all
muton results --status uncaught --severity high,medium
muton print mutations --language tact
muton print mutants --target path/to/contract.tact
muton print mutant --id 42
```

## Key Insights

- Designed for agentic/AI-assisted mutation testing workflows
- SQLite enables persistent, resumable campaigns (critical for long runs)
- Skip optimization reduces unnecessary test executions
- TON smart contract coverage fills gap in blockchain testing
- Open source (AGPL-3.0)

## Related

- Mutation testing tools landscape
- Agentic mutation testing
- Smart contract security testing
- Trail of Bits security research

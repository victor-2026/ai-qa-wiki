# Integration Testing — Systems Stitching Guide

> TestMu AI (Sep 2026). URL: https://testmu.ai/testing/integration-testing/

Comprehensive guide on integration testing strategies: when, why, and how to test component interactions in modern applications.

## Definition
> "Integration testing is a level of software testing where individual units, modules, or services are combined and tested as a group."

## When to Perform Integration Testing
- After unit testing
- When combining third-party APIs
- After refactoring existing code
- During continuous integration
- Before system or acceptance testing

## Key Insight
> "Integration tests are not second-class citizens."

Integration tests catch problems that unit tests miss: data format mismatches between services, state management bugs across boundaries, and broken contracts that work in isolation but fail when stitched together.

## Testing Pyramid Context
- **Unit**: individual components
- **Integration**: component interactions ← this page
- **E2E**: full user flows

Integration tests sit in the middle — more realistic than unit, faster than E2E.

## Service Virtualization
Mocking external dependencies to test integration points without full dependency availability.

## Source
- URL: https://testmu.ai/testing/integration-testing/
- Tags: #integration-testing, #service-virtualization, #testing-pyramid, #contract-testing
- See also: [[API-Testing]], [[Contract-Testing]], [[Test-Reliability]]

# Example Software Supply Chain Assessment

> Synthetic demonstration output. No production repository or package data is represented.

## Executive Summary

The synthetic release workflow presents material supply-chain exposure because release trust controls are incomplete. The highest-priority issue is use of long-lived build credentials, followed by missing provenance, unsigned artifacts, excessive CI permissions, and mutable third-party automation.

## Priority Findings

| Control | Severity | Component | Observation |
|---|---|---|---|
| SCS-106 | Critical | release-workflow | Long-lived credentials exposed to build jobs |
| SCS-102 | High | release-workflow | Build provenance/attestation missing |
| SCS-103 | High | release-workflow | Release artifact unsigned |
| SCS-104 | High | release-workflow | Workflow uses write-all permissions |
| SCS-105 | High | release-workflow | Third-party actions not commit-pinned |
| SCS-001 | High | payments-api/library-a | Mutable dependency reference |
| SCS-003 | High | payments-api/library-a | Unapproved registry |
| SCS-004 | High | orders-api/library-b | Unsupported component |

## Recommended Remediation Order

1. Eliminate long-lived CI credentials and move to short-lived workload identity.
2. Restrict workflow permissions to least privilege.
3. Pin third-party actions and mutable dependencies to reviewed immutable references.
4. Generate and retain SBOM plus build provenance.
5. Sign release artifacts and enforce protected release approval.
6. Move dependencies to approved registries.
7. Replace unsupported components or apply time-bound exceptions.

## Validation Criteria

The next assessment should show no Critical findings, no unapproved registries, immutable build inputs, and retained release-integrity evidence. Any accepted residual High findings should have named ownership, documented compensating controls, and expiry-bound exceptions.

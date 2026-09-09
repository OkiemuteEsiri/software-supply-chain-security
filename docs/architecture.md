# Architecture

## Objective

Provide a dependency-light, deterministic assessment pipeline for software supply-chain controls using normalized metadata rather than production integrations.

## Components

1. **Inventory layer** — JSON records for components and build workflows.
2. **Control layer** — deterministic checks in `src/controls.py`.
3. **Risk layer** — severity weighting and posture scoring in `src/analyzer.py`.
4. **Reporting layer** — structured JSON and Markdown rendering.
5. **Validation layer** — unit tests plus CI execution.

## Trust Boundaries

The project models the following trust boundaries:

- source repository to CI runner
- CI runner to package registry
- CI runner to artifact registry
- package registry to application build
- release workflow to protected environment
- release artifact to downstream consumer

## Design Principles

- deterministic controls over opaque scoring
- least privilege for build identity
- immutable references where feasible
- traceable provenance for releases
- evidence-backed remediation closure
- synthetic data only for public demonstration

## Non-Goals

The lab does not perform live package retrieval, signature generation, secret access, production workflow modification, or exploit simulation.

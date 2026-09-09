# Software Supply Chain Security

A defensive DevSecOps engineering project for assessing software supply-chain posture across dependencies, build provenance, CI controls, artifact integrity, secret handling, and release governance.

> **Scope:** synthetic package/build metadata only. No production repositories, credentials, signing keys, proprietary packages, or exploit payloads are included.

## Problem Statement

Modern applications depend on third-party packages, build automation, registries, reusable CI actions, and release artifacts. A compromise anywhere in that chain can introduce risk before code reaches production. This project turns software-supply-chain controls into an explainable, testable assessment engine that produces prioritized findings and remediation evidence.

## Architecture

```text
Synthetic component/build inventory
             |
             v
        Normalization
             |
             v
       Control Engine
   /        |         \
Dependencies  CI      Provenance
   \        |         /
        Risk Scoring
             |
             v
 Findings -> Reports -> Remediation -> Revalidation
```

## Controls Implemented

The current engine evaluates:

- unpinned or mutable dependency versions
- dependencies without integrity hashes
- packages from unapproved registries
- missing SBOM generation
- missing build provenance/attestation
- unsigned release artifacts
- CI workflows with broad write permissions
- unpinned third-party actions
- build jobs that expose long-lived credentials
- missing protected-release approval
- end-of-life or unsupported components
- critical components without named ownership

Each finding includes a control ID, severity, affected component, evidence, business/security impact, remediation guidance, and validation criteria.

## Repository Structure

```text
.
├── src/
│   ├── models.py
│   ├── controls.py
│   ├── analyzer.py
│   └── reporting.py
├── data/
│   └── synthetic-supply-chain.json
├── tests/
│   └── test_analyzer.py
├── docs/
│   ├── architecture.md
│   ├── methodology.md
│   └── remediation-validation.md
├── reports/
│   └── example-assessment.md
└── .github/workflows/tests.yml
```

## Usage

```bash
python -m src.analyzer data/synthetic-supply-chain.json
python -m unittest discover -s tests -v
```

## Risk Model

Findings use four operational tiers:

| Severity | Interpretation | Default action |
|---|---|---|
| Critical | Material release/build trust failure | Block release |
| High | Strong compromise or tampering opportunity | Remediate before promotion |
| Medium | Important control weakness | Track to engineering SLA |
| Low | Hardening or governance improvement | Address through backlog |

The engine also calculates a 0–100 posture score from weighted control failures. The score is intentionally explainable and should complement, not replace, engineering judgment.

## MITRE ATT&CK Context

Defensive mappings include:

- **T1195 — Supply Chain Compromise**
- **T1552 — Unsecured Credentials**
- **T1078 — Valid Accounts**
- **T1588.006 — Obtain Capabilities: Vulnerabilities**

ATT&CK is used for defensive coverage and threat-model context only.

## Security Engineering Workflow

1. Inventory packages, build jobs, registries, actions, and release artifacts.
2. Normalize metadata into a common assessment model.
3. Evaluate deterministic policy controls.
4. Prioritize high-impact trust and provenance failures.
5. Assign remediation ownership and due dates.
6. Collect remediation evidence.
7. Re-run the assessment.
8. Close findings only when validation criteria are satisfied.

## Skills Demonstrated

- software supply-chain security
- DevSecOps control engineering
- SBOM/provenance concepts
- CI/CD security review
- dependency governance
- artifact-integrity controls
- Python security automation
- unit testing
- risk scoring
- remediation validation
- security reporting

## Limitations

This repository performs static assessment of synthetic metadata. It does not claim live registry scanning, cryptographic signing, runtime admission enforcement, malware analysis, production CI access, or guaranteed compromise detection.

## Roadmap

- CycloneDX/SPDX ingestion
- SLSA control mapping
- SARIF export
- policy-exception expiry controls
- dependency graph risk propagation
- OpenSSF Scorecard ingestion
- artifact-signature verification adapters
- dashboard-ready JSON metrics

## Ethical Use

Use only with systems, repositories, build environments, and metadata you own or are explicitly authorized to assess.
# Assessment Methodology

## 1. Establish Scope

Define the software product, repositories, dependency inventories, build workflows, registries, release environments, and accountable owners that are authorized for review.

## 2. Normalize Evidence

Translate source metadata into the lab schema:

- component name and type
- immutable version/digest
- integrity metadata
- registry approval state
- support lifecycle
- criticality and ownership
- SBOM status
- provenance/attestation status
- artifact-signing state
- CI permissions
- action pinning
- credential lifetime
- release approvals

## 3. Evaluate Controls

Each control is deterministic and produces evidence plus explicit validation criteria. Control failures are not treated as proof of compromise; they represent exposure or governance weakness requiring review.

## 4. Prioritize

Critical findings represent release/build trust failures that should normally block promotion. High findings require remediation before release unless a documented exception with compensating controls exists. Medium and Low findings are managed through engineering SLAs.

## 5. Remediate and Validate

Closure requires evidence that the configuration or process changed, followed by re-execution of the relevant control. Exceptions should identify owner, rationale, compensating controls, approver, and expiry date.

## 6. Report

Report both technical findings and governance metrics: open findings by severity, affected products, overdue remediation, exception age, and revalidation status.

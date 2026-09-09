# Remediation and Validation Playbook

## Dependency Integrity

**Remediation**
- replace mutable dependency references with reviewed immutable versions
- use lockfiles or approved integrity metadata
- restrict package acquisition to governed registries

**Validation**
- re-run the assessment
- verify immutable versions/digests are recorded
- confirm integrity metadata is populated
- confirm registry approval is true

## Build Identity and Permissions

**Remediation**
- replace long-lived CI credentials with short-lived workload identity
- scope workflow/job permissions to the minimum required actions
- limit secret exposure to jobs that explicitly require it

**Validation**
- confirm `long_lived_credentials` is false
- verify permissions are explicitly scoped
- inspect release workflow evidence for short-lived identity use

## Provenance and Release Integrity

**Remediation**
- generate an SBOM during release
- generate build provenance/attestation
- sign release artifacts using an approved mechanism
- require protected-environment approval before promotion

**Validation**
- confirm SBOM, attestation, and signature evidence exists
- verify the release approval control is enabled
- re-run policy evaluation and ensure affected findings close

## Unsupported Components

**Remediation**
- upgrade or replace unsupported dependencies
- if immediate replacement is impossible, document compensating controls and an expiry-bound exception

**Validation**
- verify the replacement is supported
- confirm exception ownership, rationale, controls, approval, and expiry when applicable

## Closure Standard

A finding is not closed merely because a ticket is resolved. Closure requires technical evidence plus successful revalidation of the failed control.

from typing import Dict, List

from .models import Finding


def evaluate_component(component: Dict) -> List[Finding]:
    findings: List[Finding] = []
    name = component.get("name", "unknown")

    def add(control_id: str, severity: str, evidence: str, impact: str, remediation: str, validation: str) -> None:
        findings.append(Finding(control_id, severity, name, evidence, impact, remediation, validation))

    version = str(component.get("version", ""))
    if version in {"latest", "*", "", "main", "master"}:
        add("SCS-001", "HIGH", f"Mutable/unpinned version: {version or '<empty>'}",
            "Build inputs can change without review, weakening reproducibility and trust.",
            "Pin the dependency or build input to an immutable version, commit, or digest.",
            "Re-run assessment and confirm an immutable version is recorded.")

    if component.get("type") == "dependency" and not component.get("integrity_hash"):
        add("SCS-002", "MEDIUM", "No integrity hash recorded",
            "Package content cannot be independently matched to the approved artifact metadata.",
            "Record and verify a trusted package integrity hash or lockfile integrity value.",
            "Confirm the approved dependency metadata contains a non-empty integrity hash.")

    if component.get("registry_approved") is False:
        add("SCS-003", "HIGH", f"Unapproved registry: {component.get('registry', 'unknown')}",
            "Unapproved distribution channels increase package-substitution and governance risk.",
            "Move the component to an approved registry or formally approve the source.",
            "Confirm registry_approved is true and ownership is documented.")

    if component.get("supported") is False:
        add("SCS-004", "HIGH", "Component marked unsupported/end-of-life",
            "Unsupported components may retain publicly known weaknesses without vendor remediation.",
            "Upgrade, replace, or isolate the unsupported component under an approved exception.",
            "Confirm the component is supported or has a documented compensating-control exception.")

    if component.get("critical") and not component.get("owner"):
        add("SCS-005", "MEDIUM", "Critical component has no named owner",
            "Security and remediation accountability may be unclear during urgent response.",
            "Assign an accountable engineering or product owner.",
            "Confirm the component inventory contains a valid owner.")

    return findings


def evaluate_build(build: Dict) -> List[Finding]:
    findings: List[Finding] = []
    name = build.get("name", "build-pipeline")

    def add(control_id: str, severity: str, evidence: str, impact: str, remediation: str, validation: str) -> None:
        findings.append(Finding(control_id, severity, name, evidence, impact, remediation, validation))

    if not build.get("sbom_generated"):
        add("SCS-101", "MEDIUM", "SBOM generation disabled",
            "Incident response and dependency exposure analysis lack an authoritative component inventory.",
            "Generate an SBOM for release artifacts and retain it with build evidence.",
            "Confirm sbom_generated is true for the release workflow.")

    if not build.get("provenance_attested"):
        add("SCS-102", "HIGH", "Build provenance/attestation missing",
            "Consumers cannot reliably validate how or where the artifact was produced.",
            "Generate verifiable build provenance or attestation in the release pipeline.",
            "Confirm provenance_attested is true and evidence is retained.")

    if not build.get("artifact_signed"):
        add("SCS-103", "HIGH", "Release artifact is unsigned",
            "Artifact integrity and publisher authenticity are harder to establish.",
            "Sign release artifacts using an approved signing mechanism and protected identity.",
            "Confirm artifact_signed is true and signature verification succeeds in the release process.")

    if build.get("workflow_permissions") == "write-all":
        add("SCS-104", "HIGH", "CI workflow grants write-all permissions",
            "A compromised build step could have unnecessarily broad repository or release privileges.",
            "Apply least-privilege workflow and job permissions.",
            "Confirm permissions are explicitly scoped to required read/write operations.")

    if build.get("third_party_actions_pinned") is False:
        add("SCS-105", "HIGH", "Third-party CI actions are not commit-pinned",
            "Mutable external automation can change independently of repository review.",
            "Pin third-party actions to reviewed immutable commit SHAs and track updates deliberately.",
            "Confirm all third-party actions resolve to approved immutable commits.")

    if build.get("long_lived_credentials"):
        add("SCS-106", "CRITICAL", "Long-lived credentials exposed to build jobs",
            "Credential theft from CI could enable persistent unauthorized access to release systems.",
            "Replace long-lived credentials with short-lived workload identity and restrict secret exposure.",
            "Confirm long_lived_credentials is false and short-lived identity is enforced.")

    if build.get("protected_release_approval") is False:
        add("SCS-107", "MEDIUM", "Protected release approval is absent",
            "High-impact releases may be promoted without independent authorization.",
            "Require protected environment approval for release promotion.",
            "Confirm protected_release_approval is true for the release environment.")

    return findings

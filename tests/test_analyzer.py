import unittest

from src.analyzer import analyze


class SupplyChainAnalyzerTests(unittest.TestCase):
    def test_hardened_build_has_no_findings(self):
        payload = {
            "components": [{
                "name": "safe-lib",
                "type": "dependency",
                "version": "1.2.3",
                "integrity_hash": "sha256:demo",
                "registry": "approved.example.invalid",
                "registry_approved": True,
                "supported": True,
                "critical": True,
                "owner": "team-a",
            }],
            "builds": [{
                "name": "safe-build",
                "sbom_generated": True,
                "provenance_attested": True,
                "artifact_signed": True,
                "workflow_permissions": "read-minimal",
                "third_party_actions_pinned": True,
                "long_lived_credentials": False,
                "protected_release_approval": True,
            }],
        }
        result = analyze(payload)
        self.assertEqual(result["finding_count"], 0)
        self.assertEqual(result["posture_score"], 100)

    def test_mutable_dependency_is_high(self):
        result = analyze({"components": [{"name": "lib", "type": "dependency", "version": "latest", "integrity_hash": "x", "registry_approved": True, "supported": True}], "builds": []})
        controls = {f["control_id"]: f for f in result["findings"]}
        self.assertEqual(controls["SCS-001"]["severity"], "HIGH")

    def test_long_lived_ci_credential_is_critical(self):
        build = {
            "name": "build",
            "sbom_generated": True,
            "provenance_attested": True,
            "artifact_signed": True,
            "workflow_permissions": "read-minimal",
            "third_party_actions_pinned": True,
            "long_lived_credentials": True,
            "protected_release_approval": True,
        }
        result = analyze({"components": [], "builds": [build]})
        self.assertEqual(result["severity_counts"].get("CRITICAL"), 1)

    def test_unapproved_registry_is_reported(self):
        component = {"name": "lib", "type": "dependency", "version": "1.0.0", "integrity_hash": "x", "registry_approved": False, "supported": True}
        result = analyze({"components": [component], "builds": []})
        self.assertIn("SCS-003", {f["control_id"] for f in result["findings"]})

    def test_unsupported_component_is_high(self):
        component = {"name": "old-lib", "type": "dependency", "version": "2.0.0", "integrity_hash": "x", "registry_approved": True, "supported": False}
        result = analyze({"components": [component], "builds": []})
        finding = next(f for f in result["findings"] if f["control_id"] == "SCS-004")
        self.assertEqual(finding["severity"], "HIGH")


if __name__ == "__main__":
    unittest.main()

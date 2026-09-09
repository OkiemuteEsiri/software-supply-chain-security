from typing import Dict


def markdown_report(result: Dict) -> str:
    lines = [
        "# Software Supply Chain Assessment",
        "",
        f"**Posture score:** {result['posture_score']}/100",
        f"**Findings:** {result['finding_count']}",
        "",
        "## Severity Summary",
    ]
    for severity in ("CRITICAL", "HIGH", "MEDIUM", "LOW"):
        lines.append(f"- {severity}: {result['severity_counts'].get(severity, 0)}")
    lines.extend(["", "## Findings"])
    for finding in result["findings"]:
        lines.extend([
            "",
            f"### {finding['control_id']} — {finding['severity']}",
            f"- **Component:** {finding['component']}",
            f"- **Evidence:** {finding['evidence']}",
            f"- **Impact:** {finding['impact']}",
            f"- **Remediation:** {finding['remediation']}",
            f"- **Validation:** {finding['validation']}",
        ])
    return "\n".join(lines) + "\n"

import json
import sys
from collections import Counter
from pathlib import Path
from typing import Dict, List

from .controls import evaluate_build, evaluate_component
from .models import Finding

WEIGHTS = {"CRITICAL": 25, "HIGH": 12, "MEDIUM": 5, "LOW": 2}


def analyze(payload: Dict) -> Dict:
    findings: List[Finding] = []
    for component in payload.get("components", []):
        findings.extend(evaluate_component(component))
    for build in payload.get("builds", []):
        findings.extend(evaluate_build(build))

    counts = Counter(f.severity for f in findings)
    penalty = sum(WEIGHTS.get(f.severity, 0) for f in findings)
    score = max(0, 100 - min(100, penalty))
    return {
        "posture_score": score,
        "finding_count": len(findings),
        "severity_counts": dict(counts),
        "findings": [f.to_dict() for f in findings],
    }


def load_and_analyze(path: str) -> Dict:
    payload = json.loads(Path(path).read_text(encoding="utf-8"))
    return analyze(payload)


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python -m src.analyzer <inventory.json>")
        return 2
    result = load_and_analyze(sys.argv[1])
    print(json.dumps(result, indent=2))
    return 1 if result["severity_counts"].get("CRITICAL", 0) else 0


if __name__ == "__main__":
    raise SystemExit(main())

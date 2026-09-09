from dataclasses import dataclass, asdict
from typing import Any, Dict


@dataclass(frozen=True)
class Finding:
    control_id: str
    severity: str
    component: str
    evidence: str
    impact: str
    remediation: str
    validation: str

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

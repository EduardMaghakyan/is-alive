from dataclasses import asdict, dataclass
from enum import Enum
from typing import Any, Dict, Set


class CheckStatus(Enum):
    SUCCESS = "SUCCESS"
    FAIL = "FAIL"


@dataclass
class Check:
    status: CheckStatus

    def get_status(self) -> CheckStatus:
        return self.status

    def to_dict(self, fields: Set[str] = None) -> Dict[str, Any]:
        if not fields:
            return asdict(self)
        res = {}
        for f in fields:
            res[f] = getattr(self, f)
        return res

from dataclasses import dataclass, asdict
from enum import Enum
from typing import Set, Dict, Any


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

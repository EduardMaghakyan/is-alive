from dataclasses import asdict, dataclass
from enum import Enum
from typing import Any, Dict, Set, Tuple


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

    def to_tuple(self) -> Tuple:
        return self.status.value  # type: ignore

    @staticmethod
    def from_dict(fields: Dict):
        status = fields.get("status")
        if not status:
            raise KeyError("Missing required key `status`")
        return Check(status=CheckStatus[status])

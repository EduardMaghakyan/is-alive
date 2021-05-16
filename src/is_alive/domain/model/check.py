from dataclasses import dataclass
from enum import Enum


class CheckStatus(Enum):
    SUCCESS = "SUCCESS"
    FAIL = "FAIL"


@dataclass
class Check:
    status: CheckStatus

    def get_status(self) -> CheckStatus:
        return self.status

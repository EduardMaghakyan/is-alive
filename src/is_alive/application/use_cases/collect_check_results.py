from dataclasses import dataclass
from typing import Dict

from is_alive.application.repositories.check_repository import CheckRepository
from is_alive.domain.model import Check


@dataclass
class CollectCheckResults(object):
    repository: CheckRepository

    def __call__(self, check: Dict):
        check = Check.from_dict(check)
        self.repository.add(check)

from dataclasses import dataclass

from is_alive.application.ports import Requester
from is_alive.domain.model import Check


@dataclass
class CheckAvailability(object):
    requester: Requester

    def __call__(self, url) -> Check:
        response = Check()
        response.status = self.requester.get(url).status
        return response

from dataclasses import dataclass

from is_alive.application.ports import Requester
from is_alive.domain.model import Availability


@dataclass
class CheckAvailability(object):
    requester: Requester

    def __call__(self, url) -> Availability:
        response = Availability()
        response.status = self.requester.get(url).status
        return response

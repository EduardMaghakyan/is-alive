from dataclasses import dataclass

from is_alive.application.ports import Requester
from is_alive.application.ports.event_publisher import EventPublisher
from is_alive.domain.event import CheckedEvent
from is_alive.domain.exception import DomainException
from is_alive.domain.model import Check
from is_alive.domain.model.check import CheckStatus


@dataclass
class CheckAvailability(object):
    requester: Requester
    publisher: EventPublisher

    def __call__(self, url) -> Check:
        try:
            self.requester.get(url)
            checked = Check(CheckStatus.SUCCESS)
        except DomainException:
            checked = Check(CheckStatus.FAIL)

        self.publisher.publish(CheckedEvent(checked))
        return checked

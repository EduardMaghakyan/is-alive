from dataclasses import dataclass

from is_alive.application.ports import Requester
from is_alive.application.ports.event_publisher import EventPublisher
from is_alive.domain.event import CheckedEvent
from is_alive.domain.exception import DomainException
from is_alive.domain.model import Check


@dataclass
class CheckAvailability(object):
    requester: Requester
    publisher: EventPublisher

    def __call__(self, url) -> Check:
        try:
            checked = Check()
            checked.status_code = self.requester.get(url).status_code
        except DomainException as e:
            checked = Check()
            checked.status_code = 408

        self.publisher.publish(CheckedEvent(checked))
        return checked

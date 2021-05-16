from dataclasses import dataclass

from is_alive.application.ports import Requester
from is_alive.application.ports.event_publisher import EventPublisher
from is_alive.domain.event import CheckedEvent
from is_alive.domain.model import Check


@dataclass
class CheckAvailability(object):
    requester: Requester
    publisher: EventPublisher

    def __call__(self, url) -> Check:
        checked = Check()
        checked.status = self.requester.get(url).status
        self.publisher.publish(CheckedEvent(checked))
        return checked

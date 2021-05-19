from dataclasses import dataclass
from typing import Dict

from is_alive.application.ports.event_subscriber import EventSubscriber
from is_alive.application.repositories.check_repository import CheckRepository
from is_alive.domain.model import Check


@dataclass
class CollectCheckResults(object):
    repository: CheckRepository
    subscriber: EventSubscriber

    def __call__(self):
        self.subscriber.subscribe(self.handle_event)

    def handle_event(self, message: Dict):
        check = Check.from_dict(message)
        self.repository.add(check)

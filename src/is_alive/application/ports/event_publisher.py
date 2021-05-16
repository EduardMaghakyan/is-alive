import abc

from is_alive.domain.event import DomainEvent


class EventPublisher:
    @abc.abstractmethod
    def publish(self, event: DomainEvent, **attributes) -> None:
        pass

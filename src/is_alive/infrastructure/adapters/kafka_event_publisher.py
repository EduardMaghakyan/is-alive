from dataclasses import dataclass
from typing import List

from kafka import KafkaProducer  # type: ignore
from kafka.errors import KafkaTimeoutError  # type: ignore

from is_alive.application.ports.event_publisher import EventPublisher
from is_alive.domain.event import DomainEvent


class MemoryProducer:
    events: List = []

    def send(self, topic, message):
        self.events.append(message)


class MemoryEventPublisher(EventPublisher):
    producer: MemoryProducer
    topic: str

    def __init__(self, producer, topic):
        self.producer = producer
        self.topic = topic

    def publish(self, event: DomainEvent, **attributes) -> None:
        self.producer.send("topic", event.serialize())


@dataclass
class KafkaEventPublisher(EventPublisher):
    producer: KafkaProducer
    topic: str

    def publish(self, event: DomainEvent, **attributes) -> None:
        try:
            future = self.producer.send(self.topic, event.serialize().encode("utf-8"))
            future.get(timeout=60)
        except KafkaTimeoutError as e:
            # properly log and maybe raise domain exception
            print(e)

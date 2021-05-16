from kafka import KafkaProducer
from kafka.errors import KafkaTimeoutError

from is_alive.application.ports.event_publisher import EventPublisher
from is_alive.domain.event import DomainEvent


class KafkaEventPublisher(EventPublisher):
    producer: KafkaProducer
    topic: str

    def __init__(self, producer, topic):
        self.producer = producer
        self.topic = topic

    def publish(self, event: DomainEvent, **attributes) -> None:
        try:
            self.producer.send("topic", event.serialize())
        except KafkaTimeoutError as e:
            # properly log and maybe raise domain exception
            pass

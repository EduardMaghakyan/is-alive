from unittest.mock import Mock

from kafka.errors import KafkaTimeoutError  # type: ignore

from is_alive.domain.event import DomainEvent
from is_alive.infrastructure.adapters.kafka_event_publisher import KafkaEventPublisher


def test_kafka_event_publisher__publish():
    producer = Mock()
    dummy_event = DomainEvent()
    publisher = KafkaEventPublisher(producer, "topic")
    publisher.publish(dummy_event)

    producer.send.assert_called_once()
    producer.send.assert_called_with("topic", dummy_event.serialize().encode("utf-8"))


def test_kafka_event_publisher__handle_exception():
    producer = Mock()
    producer.send.side_effect = KafkaTimeoutError

    dummy_event = DomainEvent()
    publisher = KafkaEventPublisher(producer, "topic")
    publisher.publish(dummy_event)

    producer.send.assert_called_with("topic", dummy_event.serialize().encode("utf-8"))

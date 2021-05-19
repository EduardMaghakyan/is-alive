import json
from dataclasses import dataclass
from typing import Callable

from kafka import KafkaConsumer  # type: ignore

from is_alive.application.ports.event_subscriber import EventSubscriber


@dataclass
class KafkaEventSubscriber(EventSubscriber):
    consumer: KafkaConsumer

    def subscribe(self, handler: Callable):
        for msg in self.consumer:
            # proper deserialization is needed
            message = json.loads(msg.value.decode("utf-8"))
            try:
                handler({"status": message["body"]["checked"]["status"]})
            except Exception as e:
                print("exception")
                print(e)

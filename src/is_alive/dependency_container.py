import pinject  # type: ignore
import psycopg2
from kafka import KafkaProducer  # type: ignore

import is_alive.infrastructure.adapters as adapters
import is_alive.infrastructure.repositories as repositories
from is_alive.application.use_cases import CheckAvailability
from is_alive.config import CONFIG
from is_alive.infrastructure.adapters.kafka_event_publisher import MemoryProducer


class ChecksReponsitorySpec(pinject.BindingSpec):
    def configure(self, bind):
        conf = CONFIG["repositories"]["check_repository"]
        connection = psycopg2.connect(
            database=conf["db_name"],
            user=conf["user"],
            password=conf["password"],
            host=conf["host"],
        )
        bind("repository", to_instance=repositories.PostgresqlCheckRepository(connection))


class RequesterSpec(pinject.BindingSpec):
    def configure(self, bind):
        bind("requester", to_instance=adapters.HttpRequester())


class EventPublisherSpec(pinject.BindingSpec):
    def configure(self, bind):
        publisher_cofig = CONFIG["ports"]["event_publisher"]
        if publisher_cofig["type"] == "memory":
            producer = MemoryProducer()
            bind(
                "publisher",
                to_instance=adapters.MemoryEventPublisher(
                    producer=producer, topic=publisher_cofig["topic"]
                ),
            )
        elif publisher_cofig["type"] == "kafka":
            producer = KafkaProducer(bootstrap_servers=publisher_cofig["server"])
            bind(
                "publisher",
                to_instance=adapters.KafkaEventPublisher(
                    producer=producer, topic=publisher_cofig["topic"]
                ),
            )


object_graph = pinject.new_object_graph(
    modules=None,
    binding_specs=[EventPublisherSpec(), RequesterSpec(), ChecksReponsitorySpec()],
)


class Application:
    check_availability: CheckAvailability

    def __init__(self):
        self.check_availability = object_graph.provide(CheckAvailability)

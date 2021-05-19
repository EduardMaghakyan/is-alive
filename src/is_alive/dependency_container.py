import pinject  # type: ignore
import psycopg2  # type: ignore
from kafka import KafkaConsumer, KafkaProducer  # type: ignore

import is_alive.infrastructure.adapters as adapters
import is_alive.infrastructure.repositories as repositories
from is_alive.application.use_cases import CheckAvailability, CollectCheckResults
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
        connection.autocommit = True
        bind(
            "repository", to_instance=repositories.PostgresqlCheckRepository(connection)
        )


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


class EventSubscriberSpec(pinject.BindingSpec):
    def configure(self, bind):
        subscriber_config = CONFIG["ports"]["event_subscriber"]
        consumer = KafkaConsumer(
            subscriber_config["topic"], bootstrap_servers=subscriber_config["server"]
        )
        bind(
            "subscriber",
            to_instance=adapters.KafkaEventSubscriber(consumer=consumer),
        )


object_graph = pinject.new_object_graph(
    modules=None,
    binding_specs=[
        EventPublisherSpec(),
        RequesterSpec(),
        ChecksReponsitorySpec(),
        EventSubscriberSpec(),
    ],
)


class Application:
    check_availability: CheckAvailability
    collect_check_results: CollectCheckResults

    def __init__(self):
        self.check_availability = object_graph.provide(CheckAvailability)
        self.collect_check_results = object_graph.provide(CollectCheckResults)

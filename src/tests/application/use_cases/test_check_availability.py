from typing import List

import pytest

from is_alive.application.ports import Requester
from is_alive.application.ports.event_publisher import EventPublisher
from is_alive.application.ports.requester import ResponseDto
from is_alive.application.use_cases import CheckAvailability
from is_alive.domain.event import CheckedEvent, DomainEvent
from is_alive.domain.model import Check


class SpyRequester(Requester):
    calls: int = 0

    def get(
        self,
        url: str,
    ) -> ResponseDto:
        self.calls += 1

        if url == "https://available.com":
            return ResponseDto(200)

        return ResponseDto(404)


class SpyPublisher(EventPublisher):
    event_bus: List = []
    calls: int = 0

    def publish(self, event: DomainEvent, **attributes) -> None:
        # It's LIFO queue it should be enough
        self.calls += 1
        self.event_bus.append(event)


@pytest.fixture
def use_case():
    return CheckAvailability(requester=SpyRequester(), publisher=SpyPublisher())


def test_check_availability__available(use_case):
    result = use_case("https://available.com")

    assert 1 == use_case.requester.calls
    assert isinstance(result, Check)
    assert 200 == result.get_status()


def test_check_availability__unavailable(use_case):
    result = use_case("https://unavailable.com")

    assert 1 == use_case.requester.calls
    assert isinstance(result, Check)
    assert 404 == result.get_status()


def test_check_availability__published_event(use_case):
    result = use_case("https://available.com")
    expected_event = CheckedEvent(result)
    assert 1 == use_case.publisher.calls
    assert expected_event == use_case.publisher.event_bus.pop()

import pytest

from is_alive.application.ports import Requester
from is_alive.application.ports.requester import ResponseDto
from is_alive.application.use_cases import CheckAvailability
from is_alive.domain.model import Availability


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


@pytest.fixture
def use_case():
    return CheckAvailability(SpyRequester())


def test_check_availability__available(use_case):
    result = use_case("https://available.com")

    assert 1 == use_case.requester.calls
    assert isinstance(result, Availability)
    assert 200 == result.get_status()


def test_check_availability__unavailable(use_case):
    result = use_case("https://unavailable.com")

    assert 1 == use_case.requester.calls
    assert isinstance(result, Availability)
    assert 404 == result.get_status()

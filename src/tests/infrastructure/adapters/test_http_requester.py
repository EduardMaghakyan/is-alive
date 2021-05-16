from unittest.mock import MagicMock, Mock, patch

import pytest as pytest
from requests.exceptions import Timeout

from is_alive.application.ports.requester import ResponseDto
from is_alive.domain.exception.domain_exception import DomainException
from is_alive.infrastructure.adapters.http_requester import HttpRequester

requests = Mock()


@pytest.fixture
def mocked_response() -> MagicMock:
    response_mock = Mock()
    response_mock.status_code = 200
    return response_mock


@patch("is_alive.infrastructure.adapters.http_requester.requests")
def test_get_http_requester__get(mock_requests: MagicMock, mocked_response):
    available_url = "https://dummy-url.com"
    mock_requests.get.return_value = mocked_response

    http_requester = HttpRequester()
    response = http_requester.get(available_url)

    mock_requests.get.assert_called_once()
    mock_requests.get.assert_called_with(available_url)
    assert isinstance(response, ResponseDto)
    assert 200 == response.status


@patch("is_alive.infrastructure.adapters.http_requester.requests")
def test_get_http_requester__handle_timeout(mock_requests: MagicMock):
    available_url = "https://dummy-url.com"
    mock_requests.get.side_effect = Timeout(response="Request timed out")

    http_requester = HttpRequester()

    with pytest.raises(DomainException) as ex:
        http_requester.get(available_url)

    assert "Request timed out" == ex.value.response
    mock_requests.get.assert_called_once()
    mock_requests.get.assert_called_with(available_url)

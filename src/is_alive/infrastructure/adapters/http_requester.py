import requests
from requests import RequestException

from is_alive.application.ports import Requester
from is_alive.application.ports.requester import ResponseDto
from is_alive.domain.exception.domain_exception import DomainException


class HttpRequester(Requester):
    def get(self, url: str) -> ResponseDto:
        try:
            r = requests.get(url)
            return ResponseDto(status_code=r.status_code)
        except RequestException as e:
            raise DomainException(response=e.response)

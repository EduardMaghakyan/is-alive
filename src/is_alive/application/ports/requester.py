import abc
from dataclasses import dataclass


@dataclass
class ResponseDto:
    status_code: int


class Requester:
    @abc.abstractmethod
    def get(self, url: str) -> ResponseDto:
        pass

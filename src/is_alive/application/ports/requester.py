import abc
from dataclasses import dataclass


@dataclass
class ResponseDto:
    status: int


class Requester:
    @abc.abstractmethod
    def get(self, url: str) -> ResponseDto:
        pass

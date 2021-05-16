from is_alive.application.ports import Requester
from is_alive.application.ports.requester import ResponseDto


class HttpRequester(Requester):
    def get(self, url: str) -> ResponseDto:
        pass

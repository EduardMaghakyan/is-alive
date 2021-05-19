import abc
from typing import Callable


class EventSubscriber(abc.ABC):
    @abc.abstractmethod
    def subscribe(self, handler: Callable):
        pass

import abc

from is_alive.domain.model import Check


class CheckRepository(abc.ABC):
    @abc.abstractmethod
    def add(self, check: Check) -> int:
        pass

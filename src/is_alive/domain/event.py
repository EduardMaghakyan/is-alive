import json
from datetime import datetime, timezone

from is_alive.domain.model import Check


class DomainEvent:
    def __init__(self, **kwargs):
        self.timestamp = datetime.now(timezone.utc).replace(microsecond=0)
        self.__dict__.update(kwargs)

    def __repr__(self):
        body = ", ".join(f"{item[0]}={item[1]!r}" for item in self.__dict__.items())
        return f"{self.__class__.__qualname__}({body})"

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def serialize(self):
        return json.dumps(self.as_dict())

    def as_dict(self):
        return {
            "timestamp": self.timestamp,
            "body": self.get_body(),
        }

    def get_body(self):
        return {k: v for (k, v) in self.__dict__.items() if k not in ["timestamp"]}


class CheckedEvent(DomainEvent):
    def __init__(self, check: Check):
        super().__init__(checked=check)

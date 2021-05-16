from dataclasses import dataclass


@dataclass
class Availability:
    status: int = -1

    def get_status(self):
        return self.status

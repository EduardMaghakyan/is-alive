from dataclasses import dataclass


@dataclass
class Check:
    status_code: int = -1

    def get_status_code(self):
        return self.status_code

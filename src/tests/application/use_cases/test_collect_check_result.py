from dataclasses import dataclass
from typing import Callable, List
from unittest.mock import Mock

import pytest

from is_alive.application.ports.event_subscriber import EventSubscriber
from is_alive.application.use_cases.collect_check_results import CollectCheckResults
from is_alive.domain.model.check import Check, CheckStatus


@pytest.fixture
def check_message():
    return {"status": CheckStatus.SUCCESS.value}


@dataclass
class DummySubscriber(EventSubscriber):
    messages: List

    def subscribe(self, handler: Callable):
        for msg in self.messages:
            handler(msg)


def test_collect_check_result__persist(check_message):
    repo = Mock()
    subscriber = DummySubscriber(messages=[check_message])

    use_case = CollectCheckResults(repository=repo, subscriber=subscriber)
    use_case()
    repo.add.assert_called_once_with(Check.from_dict(check_message))

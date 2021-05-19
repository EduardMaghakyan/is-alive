from unittest.mock import Mock

from is_alive.application.use_cases.collect_check_results import CollectCheckResults
from is_alive.domain.model import Check
from is_alive.domain.model.check import CheckStatus


def test_collect_check_result__persist():
    repo = Mock()
    check = Check(status=CheckStatus.SUCCESS)
    use_case = CollectCheckResults(repository=repo)
    use_case(check.to_dict())
    repo.add.assert_called_once_with(check)

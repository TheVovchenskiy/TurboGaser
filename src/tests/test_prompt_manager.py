from dataclasses import dataclass
from unittest.mock import patch

import pytest

from src.prompt_manager import PromptManager


@dataclass
class YesNoTestSuccessData:
    users_input: str
    expected: bool


def test_yes_no_sucess_true(mocker):
    test_data = [
        YesNoTestSuccessData('yes', True),
        YesNoTestSuccessData('Yes', True),
        YesNoTestSuccessData('YES', True),
        YesNoTestSuccessData('YeS', True),
        YesNoTestSuccessData('y', True),
        YesNoTestSuccessData('Y', True),
        # YesNoTestSuccessData('no', False),
        # YesNoTestSuccessData('No', False),
        # YesNoTestSuccessData('nO', False),
        # YesNoTestSuccessData('NO', False),
        # YesNoTestSuccessData('n', False),
        # YesNoTestSuccessData('N', False),
    ]

    for test_case in test_data:
        mocker = mocker.patch(
            'src.prompt_manager.input',
            return_value=test_case.users_input,
        )
        actual = PromptManager.yes_no('')
        assert test_case.expected == actual


def test_yes_no_sucess_false(mocker):
    test_data = [
        YesNoTestSuccessData('no', False),
        YesNoTestSuccessData('No', False),
        YesNoTestSuccessData('nO', False),
        YesNoTestSuccessData('NO', False),
        YesNoTestSuccessData('n', False),
        YesNoTestSuccessData('N', False),
    ]

    for test_case in test_data:
        mocker = mocker.patch(
            'src.prompt_manager.input',
            return_value=test_case.users_input,
        )
        actual = PromptManager.yes_no('')
        assert test_case.expected == actual


# @pytest.mark.timeout(3)
# @patch('src.prompt_manager.input', return_value='fsdfsd')
# def test_yes_no_infinite(mocker):
#     PromptManager.yes_no('')

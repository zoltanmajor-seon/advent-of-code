import pytest

from day_3.day_3_task_1 import get_joltage


@pytest.mark.parametrize("bank, expected_joltage", [["91111111111111198", 99],
                                                    ["111111", 11],
                                                    ["2132225222222331233221342122122132221232221232321232221222129222222222122221422223223222272222222221",
                                                     97],
                                                    ["3562433533563245323438323433411123433324332336533472132253433543363323234135233413133324733323254353",
                                                     87],

                                                    ])
def test_get_joltage(bank, expected_joltage):
    joltage = get_joltage(bank)
    assert joltage == expected_joltage

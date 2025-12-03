import pytest

from day_3.day_3_task_2 import get_joltage


@pytest.mark.parametrize("bank, expected_joltage", [["987654321111111", 987654321111],
                                                    ["811111111111119", 811111111119],
                                                    ["234234234234278", 434234234278],
                                                    ["818181911112111", 888911112111],
                                                    ["111111123456789", 111123456789],
                                                    ])
def test_get_joltage(bank, expected_joltage):
    joltage = get_joltage(bank, 12)
    assert joltage == expected_joltage

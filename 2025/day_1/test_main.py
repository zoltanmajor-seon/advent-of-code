import pytest

from main import calculate_zero_crossed_upgraded

@pytest.mark.parametrize("current_point, previous_point, expected_zero_crossed, expected_current_point", [
    [0, 50, 1, 0],
    [100, 50, 1, 0],
    [101, 50, 1, 1],
    [-1, 50, 1, 99],
    [-101, 50, 2, 99],
    [100, 0, 1, 0],
    [101, 0, 1, 1],
    [-1, 0, 0, 99],
    [-101, 0, 1, 99],
])
def test_calculate_zero_crossed_upgraded(current_point, previous_point, expected_zero_crossed, expected_current_point):

    zero_crossed_in_rotation, current_point = calculate_zero_crossed_upgraded(current_point, previous_point)
    assert zero_crossed_in_rotation == expected_zero_crossed, f"{zero_crossed_in_rotation=} {expected_zero_crossed=}"
    assert current_point == expected_current_point
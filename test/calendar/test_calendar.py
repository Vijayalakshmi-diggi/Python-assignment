import pytest
from src.Calendar.util import get_day

@pytest.mark.parametrize(
    "month, day, year, expected",
    [
        (8, 5, 2015, "WEDNESDAY"),
        (12, 25, 2024, "WEDNESDAY"),
        (2, 29, 2024, "THURSDAY"),
        (1, 1, 2023, "SUNDAY"),
        (12, 31, 2022, "SATURDAY"),
    ],
)
def test_get_day(month, day, year, expected):
    assert get_day(month, day, year) == expected
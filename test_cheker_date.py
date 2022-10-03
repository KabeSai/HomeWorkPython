"""Test in cheker date."""
from cheker_date import check_date
import pytest


test_date = [(28, 2, 1900, True), (29, 2, 1900, False)]


@pytest.mark.parametrize('test_day, test_month, test_year, result_valid', test_date)
def test_cheker_date_l(test_day, test_month, test_year, result_valid):
    """Test in chek_date.Takes year, month, day and checks does the date exist.

    Args:
        test_year(int) : int - some year.
        test_month(int) : int - some month.
        test_day(int) : int - some day.
    """
    assert check_date(test_day, test_month, test_year) == result_valid

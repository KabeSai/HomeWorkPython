"""Test in cheker date."""
from low_or_up import loworup
import pytest


test_text = [('ABc dbE FRl Ama', '50%'), ('NDp Lka nuR vtE', '25%')]


@pytest.mark.parametrize('test_txt, result_valid', test_text)
def test_loworup(test_txt, result_valid):
    """Test in chek_date.Takes year, month, day and checks does the date exist.

    Args:
        test_txt(str) : str - some text.
    """
    assert loworup(test_txt) == result_valid

"""Test in captain."""
import captain
import pytest


test_captain = [(['first', \
                  'Two', \
                  'Free'], \
                 captain.datetime.strptime('2022-10-20', '%Y-%m-%d'), True),(['f1rst', 'Tw0', '3-ee'], captain.datetime.strptime('2022-11-20', '%Y-%m-%d'), True)]


@pytest.mark.parametrize('test_diary, test_date_start, result_valid', test_captain)
def test_captain_diary(test_diary, test_date_start, result_valid):
    """Test in captain.

    Args:
        test_diary(list): list - some text.
        test_date_start(datetime): datetime - format yyyy-mm-dd.
    """
    assert captain.check_valid(test_diary, test_date_start) == result_valid
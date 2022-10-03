"""Test valid date."""
full_month = [1, 3, 5, 7, 8, 10, 12]
no_full_month = [4, 6, 9, 11]
magic_numbers = [400, 28, 29, 31, 30]


def check_date(day: int, month: int, year: int) -> bool:
    """Takes year, month, day and checks does the date exist.

    Args:
        year(int) : int - some year.
        month(int) : int - some month.
        day(int) : int - some day.

    Return:
        expect : bool -  true if the date exist else false.
    """
    if bool(month in full_month) & bool(0 < day <= magic_numbers[3]):
        return True
    if bool(month in no_full_month) & bool(0 < day <= magic_numbers[4]):
        return True
    if month == 2:
        hight_year = (bool(year % 100 == 0) & bool(year % magic_numbers[0] == 0)) \
            | (bool(year % 4 == 0) & bool(year % 100 != 0))
        if bool(not (hight_year)) & bool(day <= magic_numbers[1]):
            return True
        if bool(hight_year) & bool(day <= magic_numbers[2]):
            return True
    return False

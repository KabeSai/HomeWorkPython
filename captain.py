"""This code creates the captain's diary."""
from datetime import datetime, timedelta


def captain_diary(diary: list, date_start: datetime):
    """This code returns the percentage of capital letters in a string.

    Args:
        diary(list): list - some text.
        date_start(datetime): datetime - format yyyy-mm-dd.
    """
    with open('Diary.txt', 'a') as diary_file:
        for time_to_start in enumerate(diary):
            diary_file.write("{1} -- {0}\n".format(date_start.strftime('%Y-%m-%d'), diary[time_to_start[0]]))
            date_start = date_start + timedelta(days=1)
    return True

def check_valid(test_diary, test_date_start):
    captain_diary(test_diary, test_date_start)
    with open('Diary.txt', 'r') as file_captain:
        lines = file_captain.readlines()
        # test_date_start = test_date_start + timedelta(days=1)
        for line in lines:
            line_diary = line.split(' -- ')
            line_diary = str(line_diary[1])
            if line_diary == '{0}\n'.format(test_date_start.strftime('%Y-%m-%d')):
                test_date_start = test_date_start + timedelta(days=1)
                line_date = line.split(' -- ')
                line_date = str(line_date[0])
                if line_date == '{0}'.format(test_diary[0]): 
                    return True
    return False
print(check_valid(['Today the chefs cooked fish soup','We swam into the bay', 'Defeated the pirates'], datetime.strptime('2022-10-20', '%Y-%m-%d')))                        
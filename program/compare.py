from parse import parse_cal, scheduler, is_conflicting
from users import *
from events import *
from datetime import *

testing_mode = False

if __name__ == "__main__" and testing_mode:
    s = datetime.today() #aware datetime
    temp = timedelta(days=3)
    e = datetime.today() + temp #aware datetime

    me = User("sarah", "seidman", "sarahseidman", "pass12345", "test_files/calendar.ics", s, e)

    friend = User("joanna", "miral", "jnmiral", "pass23423", "test_files/cal2.ics", s, e)

    print scheduler(me, friend, 25)
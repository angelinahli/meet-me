from Parse import parseCal, scheduler, isConflicting
from User import *
from Event import *
from datetime import *

s = datetime.today() #aware datetime
temp = timedelta(days=3)
e = datetime.today() + temp #aware datetime

me = User("sarah", "seidman", "sarahseidman", "pass12345", "test_files/calendar.ics", s, e)

friend = User("joanna", "miral", "jnmiral", "pass23423", "test_files/cal2.ics", s, e)

print scheduler(me, friend, 25)
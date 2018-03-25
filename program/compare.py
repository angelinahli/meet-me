from Parse import parseCal, scheduler, isConflicting
from User import *
from Event import *
from datetime import datetime, timedelta

s = datetime.today()
temp = timedelta(days=3)
e = datetime.today() + temp

me = User("sarah", "seidman", "sarah4di@gmail.com", "sarahseidman", "pass12345", "test_files/calendar.ics", s, e)

friend = User("joanna", "miral", "jnm@aol.com", "jnmiral", "pass23423", "test_files/cal2.ics", s, e)

print scheduler(me, friend, 25)
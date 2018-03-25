from Parse import parseCal, scheduler, isConflicting
from User import *
from Event import *
from datetime import datetime, timedelta

s = datetime.today()
temp = timedelta(days=3)
e = datetime.today() + temp

me = User(firstName="sarah", lastName="seidman", email="sarah4di@gmail.com", username="sarahseidman", password="pass12345", link="test_files/calendar.ics", start=s, end=e)

friend = User("joanna", "miral", "jnm@aol.com", "jnmiral", "pass23423", "test_files/cal2.ics", s, e)

print scheduler(me, friend, 25)
from Parse import parseCal, scheduler, isConflicting
from User import *
from Event import *
from datetime import *

today = datetime.today()
temp = timedelta(days=-6)
s = today + temp
temp2 = timedelta(days=3)
e = s + temp2

me = User("sarah", "seidman", "sarahseidman", "pass12345", "test_files/testcal1.ics", s, e)

friend = User("joanna", "miral", "jnmiral", "pass23423", "test_files/testcal2.ics", s, e)

for x in scheduler(me, friend, 25):
	print x.name, x.start.strftime("%A, %d. %B %Y %I:%M%p"), x.end.strftime("%A, %d. %B %Y %I:%M%p")
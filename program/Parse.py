from icalendar import Calendar, Event
from datetime import datetime
from pytz import UTC # timezone
from Event import Event
from datetime import datetime, timedelta


def parseCal(link):

	list = []

	c = open(link, "rb")
	cal = Calendar.from_ical(c.read())
	for component in cal.walk("vevent"):
	    name = component.get('summary')
	    start = component.decoded('dtstart')
	    end = component.decoded('dtend')
	    temp = Event(name, start, end)
	    
	    list.append(temp)
	        
	c.close()

	return list

def scheduler(user1, user2, length):

	if(user1.getStart()>user2.getStart()):
		start = user1.getStart()
	else:
		start = user2.getStart()

	if(user1.getEnd()<user2.getEnd()):
		end = user2.getEnd()
	else:
		end = user1.getEnd()

	leng = timedelta(minutes=length)

	pos = []
	i=start
	while(i<end-leng): #populates list with all possible appointments
		temp = Event("", i, (i+leng))
		pos.append(temp)
		i = i+leng

	sched = [] #empty list, will be filled with times that work

	u1 = user1.getEvents()
	u2 = user2.getEvents()
	conflicts = u1 + u2

	for element in pos:
		conflicts = False
		for l in conflicts:
			if isConflicting(element, l):
				conflicts = True
				break
		if not conflicts:
			sched.append(element)


	return sched



def isConflicting(evt1, evt2):
	conflicting = False

	if(evt1.getStart() < evt2.getEnd() and evt1.getEnd() > evt2.getStart()): #not 100% confident in logic
		conflicting = True

	return conflicting




















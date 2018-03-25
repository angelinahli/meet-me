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

	if(user1.getStart()>user2.getStart()): #make sure these methods exist in user class
		start = user1.getStart()
	else:
		start = user2.getStart()

	if(user1.getEnd()<user2.getEnd()):
		end = user2.getEnd()
	else:
		end = user1.getEnd()

	pos = []
	i=start
	while(i<end): #populates list with all possible appointments
		temp = Event("free", i, i+length)
		pos.append(temp)
		i=i+length

	sched = [] #empty list, will be filled with times that work

	j=start
	k=0
	while(j<end):
		if(user1.getEvents[k].getStart() - pos[k].getEnd() >= length):
			if(user2.getEvents[k].getStart()-pos[k].getEnd() >= length):
				sched.append(pos[k]) #if the time slot doesn't conflict with either user, it is added to the schedule
		k=k+1

	return sched


















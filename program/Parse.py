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
	#ask for timeframe, only consider events within that timeframe
	#length is mtg time
	#create list of all possible appointments in timeframe, and then do smthg like in scheduler.java

	pos = []
	i=start
	while(i<end): #populates list with all possible appointments
		temp = Event("free", i, i+length)
		pos.append(temp)
		i=i+length






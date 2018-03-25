from icalendar import Calendar, Event
from datetime import datetime
from pytz import UTC # timezone
from Event import Event
from datetime import datetime, timedelta

def parseCal(link):
	"""Returns a list of all events in someone's calendar"""
	lst = []
	with open(link, "rb") as c:
		all_text = c.read()
	
	cal = Calendar.from_ical(all_text)
	for component in cal.walk("vevent"):
	    name = component.get('summary')
	    start = component.decoded('dtstart') #aware datetime
	    end = component.decoded('dtend') #aware datetime
	    temp = Event(name, start, end)
	    lst.append(temp)
	return lst

def isConflicting(evt1, evt2):
	return (evt1.start < evt2.end) and (evt1.end > evt2.start)

def scheduler(user1, user2, length):
	start = max(user1.start, user2.start)
	end = min(user1.end, user2.end)
	leng = timedelta(minutes=length)

	pos = []
	time = start
	while(time < end - leng):
		new_event = Event("free", time, time + leng)
		pos.append(new_event)
		i += leng

	sched = [] # empty list, will be filled with times that work
	conflicts = user1.events + user2.events

	for candidate in pos:
		has_conflict = False
		for event in conflicts:
			if isConflicting(candidate, event):
				has_conflict = True
				break
		if not has_conflict:
			sched.append(element)
	return sched
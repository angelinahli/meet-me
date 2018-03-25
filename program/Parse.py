"""
This class contains methods to take in calendar data from .ics files and to
generate a schedule of free meeting times based on the calendar input from 2
users.
"""

from icalendar import Calendar, Event
from datetime import datetime
from pytz import utc # timezone
from datetime import datetime, timedelta

import events

def parse_cal(link):
	"""Returns a list of all events in someone's calendar"""
	lst = []
	with open(link, "rb") as c:
		all_text = c.read()
	
	cal = Calendar.from_ical(all_text)
	for component in cal.walk("vevent"):
	    name = component.get('summary')
	    start = component.decoded('dtstart') #aware datetime
	    end = component.decoded('dtend') #aware datetime
	    temp = events.Event(name, start, end)
	    lst.append(temp)
	return lst

def is_conflicting(evt1, evt2):
	return (evt1.start < evt2.end) and (evt1.end > evt2.start)

def schedule(start_time, end_time, minutes, user_list):
	"""Return list of events that work for all users"""
	leng = timedelta(minutes=minutes)

	pos = []
	time = start
	while(time < end - leng):
		new_event = events.Event("free", utc.localize(time), utc.localize(time + leng))
		pos.append(new_event)
		time += leng

	sched = []
	conflicts = []
	for user in user_list:
		conflicts += user.events

	for candidate in pos:
		has_conflict = False
		for event in conflicts:
			if is_conflicting(candidate, event):
				has_conflict = True
				break
		if not has_conflict:
			sched.append(candidate)
	return sched
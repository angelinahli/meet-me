from icalendar import Calendar, Event
from datetime import datetime
from pytz import UTC # timezone
from Event import Event
# import time
# from datetime import date

#person = User()

c = open("test_files/calendar.ics", "rb")
cal = Calendar.from_ical(c.read())
for component in cal.walk("vevent"):
    name = component.get('summary')
    s = component.decoded('dtstart')

    year = s[:3]
    print year

    end = component.decoded('dtend')
    temp = Event(name, start, end)
    print start
    print end
    #add temp event to user's list of events
        
c.close()

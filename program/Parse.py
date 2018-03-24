from icalendar import Calendar, Event
from datetime import datetime
from pytz import UTC # timezone
from Event import Event


#person = User()

c = open("test_files/calendar.ics", "rb")
cal = Calendar.from_ical(c.read())
for component in cal.walk("vevent"):
    name = component.get('summary')
    start = component.decoded('dtstart')
    end = component.decoded('dtend')
    print type(end)
    temp = Event(name, start, end)
    print temp
    #add temp event to user's list of events
        
c.close()

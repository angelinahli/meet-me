from icalendar import Calendar, Event
from datetime import datetime
from pytz import UTC # timezone
from Event import Event

#person = User()

c = open("test_files/calendar.ics", "rb")
cal = Calendar.from_ical(c.read())
for component in cal.walk("vevent"):
    name = component.get('summary')
    start = component.get('dtstart')
    end = component.get('dtend')
    temp = Event(name, start, end)
    print name
    print start
    print end

    # add temp event to user's array of events

        
c.close()

# import vobject

# data = open("test_files/calendar.ics").read()

# cal = vobject.readOne(data)

# for component in cal.walk():
# 	print cal.vevent.summary.valueRepr()


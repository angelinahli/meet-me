from icalendar import Calendar, Event #no module named icalendar?
from datetime import datetime
from pytz import UTC # timezone

person = User()

c = open("test_files/calendar.ics", "rb")
cal = Calendar.from_ical(c.read())
for component in cal.walk():
    if component.name == "VEVENT":
        name = component.get('summary')
        start = component.get('dtstart')
        end = component.get('dtend')
        temp = Event(name, start, end)

        # add temp event to user's array of events

        
g.close()
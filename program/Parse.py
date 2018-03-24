from icalendar import Calendar, Event
from datetime import datetime
from pytz import UTC # timezone

c = open("officehours_barnard.edu_hm1tda6qdc9t2t4qs6v00n5kog@group.calendar.google.com.ics", "rb")
cal = Calendar.from_ical(c.read())
for component in cal.walk():
    if component.name == "VEVENT":
        print(component.get('summary'))
        print(component.get('dtstart'))
        print(component.get('dtend'))
        print(component.get('dtstamp'))
        print("hey")
        print hey
g.close()
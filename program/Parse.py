from icalendar import Calendar, Event
from datetime import datetime
from pytz import UTC # timezone

c = open("test_files/calendar.ics", "rb")
cal = Calendar.from_ical(c.read())
for component in cal.walk():
    if component.name == "VEVENT":
        print(component.get('summary'))
        print(component.get('dtstart'))
        print(component.get('dtend'))
        print(component.get('dtstamp'))
        print("hey")


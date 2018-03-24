from icalendar import Calendar, Event #no module named icalendar?
from datetime import datetime
from pytz import UTC # timezone
from Event import Event


person = User()

<<<<<<< HEAD
class Parse{
	
	c = open("test_files/calendar.ics", "rb")
	cal = Calendar.from_ical(c.read())
	for component in cal.walk("vevent"):
	    name = component.get('summary')
	    start = component.decoded('dtstart')
	    end = component.decoded('dtend')
	    temp = Event(name, start, end)
	    #add temp event to user's list of events
	        
	c.close()
}
=======
c = open("test_files/calendar.ics", "rb")
cal = Calendar.from_ical(c.read())
<<<<<<< HEAD
for component in cal.walk():
    if component.name == "VEVENT":
        name = component.get('summary')
        start = component.get('dtstart')
        end = component.get('dtend')
        temp = Event(name, start, end)

        # add temp event to user's array of events

        
g.close()
=======
for component in cal.walk("vevent"):
    name = component.get('summary')
    start = component.decoded('dtstart')
    end = component.decoded('dtend')
    print type(end)
    temp = Event(name, start, end)
    print temp
    #add temp event to user's list of events
        
c.close()
>>>>>>> 0608d6f6f2d7fa5b7e25c0cfce42489d7cf9cf74
>>>>>>> c8d78a2a75d04e4f5ce85f7d0a4fffa79c8bb548

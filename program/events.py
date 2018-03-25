from datetime import datetime, timedelta
from pytz import utc # timezone

# helper functions

def get_datetime(date_text):
    return utc.localize(datetime.strptime(date_text, "%Y-%m-%d %H:%M:%S"))

def valid_start_endtime(start, end):
    return get_datetime(end) > get_datetime(start)

# class object

class Event(object):

    def __init__(self, name, start, end):
        self.name = name
        self.start = start # start and end are datetime objects
        self.end = end
        self.length = self.end - self.start

    def get_formatted_start(self):
        return self.start.strftime("%I:%M%p")
    
    def get_formatted_end(self):
        return self.end.strftime("%A, %d. %B %Y %I:%M%p")

class MiniCalendar(object):
    """Just a really mini, NBD calendar that will store events based on their date."""

    def __init__(self, events):
        self.events = events
        self.calendar = {}
        for event in self.events:
            event_date = event.start.date().strftime("%A, %d %B %Y")
            updated_events = self.calendar.get(event_date, [])

            diff_end = event.end.date() != event.start.date()
            start = event.start.strftime("%I:%M%p")
            end = event.end.strftime("%I:%M%p") if not diff_end else event.end.strftime("%A, %d %B %I:%M%p")
            new_event = {"start": start, "end": end}

            updated_events.append(new_event)
            self.calendar[event_date] = updated_events

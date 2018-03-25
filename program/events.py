from datetime import datetime, timedelta, strftime
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
        return self.start.strftime("%A, %d. %B %Y %I:%M%p")
    
    def get_formatted_end(self):
        return self.end.strftime("%A, %d. %B %Y %I:%M%p")
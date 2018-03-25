from datetime import datetime, timedelta

class Event(object):

	def __init__(self, name, start, end):
		self.name = name
		self.start = start #start and end are datetime objects
		self.end = end
		self.length = self.end - self.start
		
	def __str__(self):
		out = self.start.srftime("%A, %d. %B %Y %I:%M%p") + " to " + self.end.strftime("%A, %d. %B %Y %I:%M%p")
		return out

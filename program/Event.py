from datetime import datetime, timedelta

class Event(object):

	def __init__(self, name, start, end):
		self.name = name
		self.start = start #start and end are datetime objects
		self.end = end

	def getLength(self):
		length = self.end-self.start
		return length #this should be timedelta

	def getStart(self):
		return self.start

	def getEnd(self):
		return self.end

	def __str__(self):
		out = strftime(start) + " to " + strftime(end)
		return out
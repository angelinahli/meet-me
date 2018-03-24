from datetime import datetime, timedelta

class Event(object):

	def __init__(self, name, start, end):
		self.name = name
		self.start = start
		self.end = end

	def getLength(self):
		length = self.end-self.start
		return length

	def getStart(self):
		return self.start

	def getEnd(self):
		return self.end

	# def parseStart(self, time):
	# 	year = time[0:4]
	# 	month = time[5:7]
	# 	day = time[8:10]
	# 	hour = time[11:13]
	# 	minute = time[14:16]

	# 	temp = datetime(year, month, day, hour, minute)
	# 	return temp





	#(year, month, day[, hour[, minute)

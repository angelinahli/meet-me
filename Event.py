class Event(object):

	def __init__(self, name, start, end):
		self.name = name
		self.start = start
		self.end = end

	def getLength(self):
		length = end-start
		return length

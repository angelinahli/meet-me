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

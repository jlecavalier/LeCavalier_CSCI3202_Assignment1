class StackEmptyException(Exception):
	pass

class StackTypeException(Exception):
	pass

class IntStack(object):
	s = list()

	def __init__(self):
		pass

	def checkSize(self):
		return len(self.s)

	def push(self, item):
		if not type(item) is int:
			raise StackTypeException("Stack items must be integers")
		else:
			self.s.append(item)

	def pop(self):
		if len(self.s) == 0:
			raise StackEmptyException("Nothing to pop!")
		else:
			popped = self.s[-1]
			del self.s[-1]
			return popped

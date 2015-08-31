import Queue

class QueueException(Exception):
    pass

class IntQueue(object):
	q = Queue.Queue(maxsize=0)

	def __init__(self):
		pass

	def qsize(self):
		return self.q.qsize()

	def empty(self):
		return self.q.empty()

	def put(self, item):
		if not type(item) is int:
			raise QueueException("Queue items must be integers")
		else:
			self.q.put(item)

	def get(self):
		return self.q.get()

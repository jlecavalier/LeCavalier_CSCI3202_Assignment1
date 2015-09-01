class GraphTypeException(Exception):
	pass

class IntGraph(object):
	vertices = {}

	def __init__(self):
		pass

	def addVertex(self, value):
		if not type(value) is int:
			raise GraphTypeException("Graph vertices must be integers")
		if value in self.vertices:
			print("Vertex %d already exists" % value)
		else:
			self.vertices[value] = []

	def addEdge(self, value1, value2):
		if value1 == value2:
			print("Self edges not allowed.")
		elif not (value1 in self.vertices and value2 in self.vertices):
			print("One or more vertices not found")
		else:
			if value2 in self.vertices[value1]:
				print("edge from {0} to {1} already exists".format(value1, value2))
			else:
				self.vertices[value1].append(value2)
			if value1 in self.vertices[value2]:
				print("edge from {0} to {1} already exists".format(value2, value1))
			else:	
				self.vertices[value2].append(value1)

	def findVertex(self, value):
		if value in self.vertices:
			print(self.vertices[value])
		else:
			print("Vertex %d not found" % value)
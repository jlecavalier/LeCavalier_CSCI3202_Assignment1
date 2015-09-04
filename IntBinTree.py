class TreeTypeException(Exception):
	pass

class IntBinTree(object):
	parent = None
	lchild = None
	rchild = None
	key = None

	def __init__(self, k):
		self.key = k

	def add(self, val, parent_val):
		if not type(val) is int:
			raise TreeTypeException("Tree nodes must be integers")
		if not self.add_helper(val, parent_val):
			print("Parent %d not found" % parent_val)

	def add_helper(self, val, parent_val):
		if self.key == parent_val:
			if self.lchild == None:
				self.lchild = IntBinTree(val)
				self.lchild.parent = self
				return True
			elif self.rchild == None:
				self.rchild = IntBinTree(val)
				self.rchild.parent = self
				return True
			else:
				print("Parent has two children. Node not added")
				return True
		else:
			if self.lchild != None:
				if self.rchild != None:
					return (self.lchild.add_helper(val, parent_val) or self.rchild.add_helper(val, parent_val))
				else:
					return self.lchild.add_helper(val, parent_val)
			elif self.rchild != None:
				return self.rchild.add_helper(val, parent_val)
			else:
				return False

	def delete(self, val):
		if not self.delete_helper(val):
			print("Node %d not found" % val)

	def delete_helper(self, val):
		if self.key == val:
			if self.lchild != None or self.rchild != None:
				print("Node %d not deleted. Has children" % val)
				return True
			else:
				if self.parent.lchild == self:
					self.parent.lchild = None
				elif self.parent.rchild == self:
					self.parent.rchild = None
				del self
				return True
		else:
			if self.lchild != None:
				if self.rchild != None:
					return (self.lchild.delete_helper(val) or self.rchild.delete_helper(val))
				else:
					return self.lchild.delete_helper(val)
			elif self.rchild != None:
				return self.rchild.delete_helper(val)
			else:
				return False

	def tprint(self):
		print(self.key)
		if self.lchild != None:
			self.lchild.tprint()
		if self.rchild != None:
			self.rchild.tprint()
		if self.lchild == None and self.rchild == None:
			print("")
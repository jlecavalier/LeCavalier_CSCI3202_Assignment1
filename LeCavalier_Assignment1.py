from IntQueue import *
from IntStack import *
from IntBinTree import *

'''
INTQUEUE TEST
'''
print("\n\n\n")
print("INTQUEUE TEST")
q = IntQueue()
print("Enqueueing in following order:")
for i in range(10):
	print(i)
	q.put(i)
print("Dequeueing in following order:")
while not q.empty():
	print(q.get())
del q

'''
INTSTACK TEST
'''

print("\n\n\n")
print("INTSTACK TEST")
s = IntStack()
print("Pushing in following order:")
for i in range(10):
	print(i)
	s.push(i)
print("Popping in following order:")
while s.checkSize() != 0:
	print(s.pop())
del s

'''
INTBINTREE TEST
'''

print("\n\n\n")
print("INTBINTREE TEST")
t = IntBinTree(5)
print("Tree initialized with root value %d" % t.key)
print("Adding 0-8 to tree")
t.add(4,5)
t.add(6,5)
t.add(2,4)
t.add(3,4)
t.add(1,2)
t.add(0,1)
t.add(7,6)
t.add(8,7)
t.add(9,8)
print("Tree nodes, starting with root.")
print("The value of the current node is printed first, and then")
print("The value of the left child (if any), and then the value")
print("of the right child (if any).")
print("an empty line is printed if the previously printed node had no children")
t.tprint()
print("deleting 1 and 9")
t.delete(0)
t.delete(9)
print("Tree nodes, again")
t.tprint()
del t

'''
INTGRAPH TEST
'''

print("\n\n\n")
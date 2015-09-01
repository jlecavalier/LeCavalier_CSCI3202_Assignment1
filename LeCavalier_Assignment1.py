from IntQueue import *
from IntStack import *
from IntBinTree import *
from IntGraph import *

raw_input("press Enter to begin.")

'''
INTQUEUE TEST
'''
print("\n\n\n")
print("INTQUEUE TEST\n")
q = IntQueue()
print("Enqueueing in following order:")
for i in range(10):
	print(i)
	q.put(i)
print("\nEnqueueing 3.5:")
try:
	q.put(3.5)
except QueueException:
	print("QueueException raised\n")
print("Dequeueing in following order until queue is empty:")
while not q.empty():
	print(q.get())
del q

'''
INTSTACK TEST
'''
raw_input("\nPress Enter to continue.")
print("\n\n\n")
print("INTSTACK TEST\n")
s = IntStack()
print("Pushing in following order:")
for i in range(10):
	print(i)
	s.push(i)
print("\nAttempting to push 3.5")
try:
	s.push(3.5)
except StackTypeException:
	print("StackTypeException raised\n")
print("Popping in following order:")
while s.checkSize() != 0:
	print(s.pop())
print("\nAttempting to pop off empty stack:")
try:
	s.pop()
except StackEmptyException:
	print("StackEmptyException raised")
del s

'''
INTBINTREE TEST
'''
raw_input("\nPress Enter to continue.")
print("\n\n\n")
print("INTBINTREE TEST\n")
t = IntBinTree(5)
print("Tree initialized with root value %d \n" % t.key)
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
print("\nAttempting to add 3.5 to tree:")
try:
	t.add(3.5,9)
except TreeTypeException:
	print("TreeTypeException raised\n")
print("Adding 10 to tree with parent 666:")
t.add(10,666)
print("\nAdding 10 to tree with parent 5:")
t.add(10,5)
print("\nTree nodes, starting with root.")
print("The value of the current node is printed first, and then")
print("The value of the left child (if any), and then the value")
print("of the right child (if any).")
print("an empty line is printed if the previously printed node had no children")
t.tprint()
print("\ndeleting 1 and 9")
t.delete(0)
t.delete(9)
print("\ndeleting 666")
t.delete(666)
print("\ndeleting 5")
t.delete(5)
print("\nTree nodes, again")
t.tprint()
del t

'''
INTGRAPH TEST
'''
raw_input("\nPress Enter to continue.")
print("\n\n\n")
print("INTGRAPH TEST\n")
g = IntGraph()
print("Adding the following vertices to the graph:")
for i in range(10):
	g.addVertex(i)
	print(i)
print("\nAttempting to add 3.5 as a vertex:")
try:
	g.addVertex(3.5)
except GraphTypeException:
	print("GraphTypeException raised\n")
print("Adding 0 to graph:")
g.addVertex(0)
print("\nadding the following edges:")
for i in range(1,10):
	g.addEdge(0,i)
	print("(0, %d)" % i)
for i in range(2,10):
	g.addEdge(1,i)
	print("(1, %d)" % i)
g.addEdge(8,9)
g.addEdge(7,8)
g.addEdge(6,7)
print("(8, 9)")
print("(7, 8)")
print("(6, 7)")
print("\nAdding edge (0,0)")
g.addEdge(0,0)
print("\nAdding edge (0, 666)")
g.addEdge(0,666)
print("\nAdding edge (0,1)")
g.addEdge(0,1)
print("\nfinding 0:")
g.findVertex(0)
print("\nfinding 8:")
g.findVertex(8)
print("\nfinding 1")
g.findVertex(1)
print("\nfinding 2")
g.findVertex(2)
print("\nfinding 666")
g.findVertex(666)
del g











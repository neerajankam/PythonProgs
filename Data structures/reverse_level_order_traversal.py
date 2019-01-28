class Node:
	def __init__(self,value):
		self.value = value
		self.left = None
		self.right = None

class BinaryTree:
	def __init__(self,root):
		self.root = Node(root)
#                         1
#			/   \
#		       2     3
#		     /   \  /	
#		    4 	 5 6
b = BinaryTree(1)
b.root.left = Node(2)
b.root.right = Node(3)
b.root.left.left = Node(4)
b.root.left.right = Node(5)
b.root.right.left = Node(6)

#Level order traversal Expected output:  1-2-3-4-5-6
def reverse_level_order_traversal(start,traversal):
	import sys
	is_py2 = sys.version[0]
	if is_py2:
		import Queue as queue
	else:
		import queue as queue
	q = queue.Queue(maxsize=10)     
	s = queue.LifoQueue(maxsize=10)	#Using LifoQueue as a stack
	q.put(start) #Enqueue the root element

	while not q.empty():  #Dequeue the elements and append them onto the stack. Each iteration  
		cur = q.get()	  #dequeues one element from the queue, pushes it onto the stack and enqueues its	 
		s.put(cur)        #left and right children
		if cur.left:                                                        
			q.put(cur.left)
		if cur.right:
			q.put(cur.right)

	while not s.empty(): #Pop the elements of the stack and append their values to the traversal string
		cur = s.get()
		traversal += str(cur.value) + '-'

	return traversal #Return the traversal string which contains the reverse level order.


print(reverse_level_order_traversal(b.root,""))

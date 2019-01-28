class Node:
	def __init__(self,value):
		self.value = value
		self.left = None
		self.right = None

class BinaryTree:
	def __init__(self,root):
		self.root = Node(root)
#             1
#			/   \
#		   2     3
#		  / \	/	
#		4 	 5 6
b = BinaryTree(1)
b.root.left = Node(2)
b.root.right = Node(3)
b.root.left.left = Node(4)
b.root.left.right = Node(5)
b.root.right.left = Node(6)

#Level order traversal Expected output:  1-2-3-4-5-6
def level_order_traversal(start,traversal):
	import sys
	is_py2 = sys.version[0]
	if is_py2:
		import Queue as queue
	else:
		import queue as queue
	q = queue.Queue(maxsize=10)
	q.put(start)
	while not q.empty():
		cur = q.get()
		traversal += str(cur.value) + '-'
		if cur.left:
			q.put(cur.left)
		if cur.right:
			q.put(cur.right)
	return traversal


print(level_order_traversal(b.root,""))

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

#Root-left-right Expected output:  1-2-4-5-3-6
def pre_order_traversal(start,traversal):
	if start:
		traversal += str(start.value) + '-'
		traversal = pre_order_traversal(start.left,traversal)
		traversal = pre_order_traversal(start.right,traversal)
	return traversal
#Left,Root,Right  Expected output: 4-2-5-1-6-3
def in_order_traversal(start,traversal):
	if start:
		traversal = in_order_traversal(start.left,traversal)
		traversal += str(start.value) + '-'
		traversal = in_order_traversal(start.right,traversal)
	return traversal
#Left,Right,Root  Expected output: 4-5-2-6-3-1
def post_order_traversal(start,traversal):
	if start:
		traversal = post_order_traversal(start.left,traversal)
		traversal = post_order_traversal(start.right,traversal)
		traversal += str(start.value) + '-'
	return traversal


print(pre_order_traversal(b.root,""))
print(in_order_traversal(b.root,""))
print(post_order_traversal(b.root,""))
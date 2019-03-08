class Node:
	def __init__(self,value=None):
		self.value = value
		self.left=None
		self.right=None

class BST:
    def __init__(self):
        self.root=None
    def insert(self,value):
        if self.root == None:
         self.root = Node(value)
        else:
         self._insert(self.root,value)
    def _insert(self,cur_node,value):
        if value < cur_node.value:
         if cur_node.left==None:
          cur_node.left =Node(value)
         else:
          self._insert(cur_node.left,value)
        elif value> cur_node.right:
         if cur_node.right == None:
          cur_node.right=Node(value)
         else:
          self._insert(cur_node.right,value)
        elif value==cur_node.value:
         print('Value already exists!')  

    def printTree(self):
        if self.root != None:
        	self._printTree(self.root)
    def _printTree(self,cur_node):
        if cur_node != None:
         self._printTree(cur_node.left)
         print str(cur_node.value)
         self._printTree(cur_node.right)
tree=BST()
tree.insert(33)
tree.insert(50)            	
tree.insert(11)
tree.insert(3)
tree.insert(10)
tree.insert(24)
tree.insert(19)
tree.insert(8)

tree.printTree()
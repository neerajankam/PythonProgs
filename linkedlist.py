class Node:
    def __init__(self,value=None):
      	self.value=value
      	self.left=None
      	self.right=None

class BST:
    def __init__(self):
    	self.root=None
    def insert(self,value):
    	if self.root==None:
    		self.root=Node(value)
    	else
    	   return self._insert(value,self.root)
    def _insert(self,value,cur_node):
        if value< cur_node.value:
         if cur_node.left == None:
          cur_node.left = Node(value)
         else:
          self._insert(self,value,cur_node.left)
        elif value> cur_node.right:
         if cur_node.right==None:
          cur_node.right = Node(value)
         else
          self._insert(self,value,cur_node.right) 
        else
         print('value already in tree!')

    def printTree(self):
        if self.root!=None:
         self._printTree(self.root)
    def _printTree(self,cur_node):
        self._printTree(self,cur_node.left)
        print(cur_node.value)
        self._printTree(self,cur_node.right)
tree=BST()
tree.insert(15)
tree.insert(20)                       	   	
tree.insert(1)
tree.insert(13)
tree.insert(8)
tree.insert(21)

tree.printTree()
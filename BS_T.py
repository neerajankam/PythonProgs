class Node:
	def __init__(self,val=None):
		self.val=val
		self.left=None
		self.right=None

class BST:
    def __init__(self):
        self.root=None

    def insert(self,val):
        if self.root==None:
         self.root=Node(val)
        else:
         self._insert(val,self.root)
    def _insert(self,val,cur_node):
        if val< cur_node.val:
         if cur_node.left == None:
          cur_node.left=Node(val)
         else:
          self._insert(self,val,cur_node.left)
        elif val> cur_node.val:
         if cur_node.right == None:
          cur_node.right=Node(val)
         else:
          self._insert(self,val,cur_node.right)
        else:
         print('Value Already in Tree!')  
    def printTree(self):
        if self.root!=None:
         self._printTree(self.root)
    def _printTree(self,cur_node):
        if cur_node != None:
         self._printTree(cur_node.left)
         print(str(cur_node.val))
         self._printTree(cur_node.right) 

b=BST()
b.insert(5)
b.insert(6)
b.insert(6)
b.printTree()                                  		
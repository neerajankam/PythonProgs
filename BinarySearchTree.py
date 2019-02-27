class Node:
    def __init__(self,value=None):
      	self.value=value
      	self.left=None
      	self.right=None

class BST:
    def __init__(self):
    	self.root=None
    
    def insert(self,value):
    	if self.root == None:
    		self.root = Node(value)
    	else:
    	    self._insert(value,self.root)
    def _insert(self,value,cur_node):
        if value < cur_node.value:
         if cur_node.left == None:
          cur_node.left = Node(value)
         else:
          self._insert(value,cur_node.left)
        elif value > cur_node.value:
         if cur_node.right == None:
          cur_node.right = Node(value)
         else:
          self._insert(value,cur_node.right) 
        elif value = =cur_node.value:
         print('value already in tree!')
   
    def height(self):
    	if self.root != None:
          return self._height(self.root,0)
        else: 
          return 0
    
    def _height(self,cur_node,cur_height):
    	if cur_node == None: 
            return cur_height
        left_height = self._height(cur_node.left,cur_height+1)
        right_height = self._height(cur_node.right,cur_height+1)
        return max(left_height,right_height)      

    def printTree(self):
        if self.root != None:
         self._printTree(self.root)
    
    def _printTree(self,cur_node):
    	if cur_node != None:
         self._printTree(cur_node.left)
         print str(cur_node.value)
         self._printTree(cur_node.right)

    def fillTree(tree,no_of_vals,max_value):
    	from random import randint
        for _ in range(no_of_vals):
          cur_elem = randint(0,max_value)
          tree.insert(cur_elem)
        return tree     

    def search(self,value):
    	if self.root != None:
    		return self._search(value,self.root)
    	else:
    	    return False
    
    def _search(self,value,cur_node):
        if value == cur_node.value:
         return True	    	
        elif value > cur_node.value and cur_node.right != None:
         return self._search(value,cur_node.right)
        elif value < cur_node.value and cur_node.left != None:
         return self._search(value,cur_node.left)
        return False  

tree = BST()
tree.fillTree(30,100)
tree.insert(6)
tree.printTree()
print('Tree height:' +str(tree.height()))
print(tree.search(6))

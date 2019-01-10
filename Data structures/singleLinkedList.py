#Node class is used to create an individual node with 'data' element
class Node:
	def __init__(self,data):
		self.data = data
		self.next = None

#SingleLinkedList class is used as a wrapper class around the Node class. The user does not directly interact with the Node class
class SingleLinkedList:
	def __init__(self):
		#Initializes the head of the linked list to None
		self.head = None

	def insert(self,data):
		#If the linked list has no elements(self.head = None), then create a node and make it the head.
		if self.head is None:
			self.head = Node(data)
		#Else, traverse to the end of the list and then insert the new node at the end of the list
		else:
			cur = self.head
			while cur.next != None:
				cur = cur.next
			cur.next = Node(data)
	
	def delete(self,data):
		#If there is no element in the linked list, just return None
		if self.head is None:
			return 
		#If the head of the linked list is the element to be deleted, make the next element the head of the list
		else:	
			cur = self.head
			if cur.data == data:
				self.head = cur.next
			#Else, keep traversing the list until the element to be deleted is found and delete it
			else:	
				while cur.data != data:
					prev = cur
					cur = cur.next
				prev.next = cur.next
				cur.next = None

	def length(self):
		#Find the number of nodes in the linked list and return it
		cur = self.head
		length = 0
		while cur:
			length += 1
			cur = cur.next
		return length				

	def printLinkedList(self):
		#Print all the elements of the linked list
		cur = self.head
		while cur.next != None:
			print(cur.data)
			cur = cur.next
		print(cur.data)

	def swap_nodes(self,key1,key2):
		# If both the nodes to be swapped are the same, then just return
		if key1 == key2:
			return
		# Set pointers and traverse until you find the previous element and current element with data value 'key1'	
		prev1 = None
		cur1 = self.head
	
		while cur1.data != key1:
			prev1 = cur1
			cur1 = cur1.next
      	# Set pointers and traverse until you find the previous element and current element with data value 'key2'
		prev2 = None
		cur2 = self.head

		while cur2.data != key2:
			prev2 = cur2
			cur2 = cur2.next
		#If previous element exists for element with data value key1, set its next value to node with data value key2
		if prev1:
			prev1.next = cur2
		#Else node1 is a head node and swap it with the node with data value key2
		else:	
			self.head = cur2
		if prev2:
			prev2.next = cur1
		else:
			self.head = cur1
		#Swapping the next values of nodes cur1 and cur2
		cur1.next,cur2.next = cur2.next,cur1.next	

	def reverse(self):
		#Reverse the nodes of the linked list by realligining the next pointer for each node
		prev = None
		cur = self.head
		while cur:
			nxt = cur.next
			cur.next = prev
			prev = cur
			cur = nxt
		#Prev points to the current element and hence make it the head of the linked list	
		self.head = prev

	def remove_dupes(self):
		#Use a dictionary to keep track of the occurences of data values. If value is already present in the dict, delete it.
		count = dict()
		cur = self.head
		while cur:
			if cur.data not in count:
				count[cur.data] = 1
			else:
				self.delete(cur.data)
			cur = cur.next	
					

l = SingleLinkedList()
l.insert(1)
l.insert(2)
l.insert(1)
l.insert(3)
l.insert(5)
l.insert(5)
l.swap_nodes(1,3)	
l.remove_dupes()	
l.printLinkedList()


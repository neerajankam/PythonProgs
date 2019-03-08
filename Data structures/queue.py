<<<<<<< HEAD
#	                          0  1  2  3 
#                             ___ __ __ __
#  Inserted from this side -  ___|__|__|__ - Element is popped from this side

class Queue:
	def __init__(self):
		#Initializing an empty list that replicates the functioning of a Queue
		self.items = []

	def size(self):
		#Returns the size of the queue
		return len(self.items)

	def isEmpty(self):
		#Checks if the queue is empty or not
		return self.items == []

	def enqueue(self,ele):
		#New element is inserted at the 0th index each time
		self.items.insert(0,ele)

	def dequeue(self):	
		#Returns the last element if the queue is not empty
		if not self.isEmpty():
			return self.items.pop()

	def printQueue(self):
		#Print all the elements of the queue
		if not self.isEmpty():
			for ele in reversed(self.items):
				print ele		


q = Queue()
q.enqueue(1)
q.enqueue(4)
q.enqueue(7)
q.enqueue(10)
q.enqueue(9)
q.dequeue()
q.printQueue()




=======
#	                          0  1  2  3 
#                             ___ __ __ __
#  Inserted from this side -  ___|__|__|__ - Element is popped from this side

class Queue:
	def __init__(self):
		#Initializing an empty list that replicates the functioning of a Queue
		self.items = []

	def size(self):
		#Returns the size of the queue
		return len(self.items)

	def isEmpty(self):
		#Checks if the queue is empty or not
		return self.items == []

	def enqueue(self,ele):
		#New element is inserted at the 0th index each time
		self.items.insert(0,ele)

	def dequeue(self):	
		#Returns the last element if the queue is not empty
		if not self.isEmpty():
			return self.items.pop()

	def printQueue(self):
		#Print all the elements of the queue
		if not self.isEmpty():
			for ele in reversed(self.items):
				print ele		


q = Queue()
q.enqueue(1)
q.enqueue(4)
q.enqueue(7)
q.enqueue(10)
q.enqueue(9)
q.dequeue()
q.printQueue()




>>>>>>> 757d76ade453e60a94c141c4ce17658c227e35e8

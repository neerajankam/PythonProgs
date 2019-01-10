class Stack:
	def __init__(self):
		#Creating an empty list which will be used to replicate the stack functionality
		self.items = [] 

	def length(self):
		return len(self.items)

	def isEmpty(self):
		return self.items == []

	def push(self,ele):
		#Appends element onto the top of the stack
		self.items.append(ele)

	def pop(self):
		#Pops an element from the stack if it is not empty
		if not self.isEmpty():
			return self.items.pop()

	def peek(self):
		#Returns the topmost element of the stack
		return self.items[-1]

	def printStack(self):
		#Prints the elements of the stack
		if not self.isEmpty():
			for ele in reversed(self.items):
				print ele	

s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.pop()
print(s.peek())
s.printStack()		
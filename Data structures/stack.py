<<<<<<< HEAD
class Stack:
	def __init__(self):
		#Creating an empty list which will be used to replicate the stack functionality
		self.items = [] 

	def size(self):
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

def is_match(p1,p2):
	if p1 == "(" and p2 == ")":
		return True
	elif p1 == "{" and p2 == "}":
		return True
	elif p1 == "[" and p2 == "]":
		return True
	else:
		return False							

def is_paren_balanced(parenString):
	st = Stack()
	is_balanced = True
	index = 0
	while index < len(parenString):
		paren = parenString[index]
		if paren in "{[(":
			st.push(paren)
		else:
			if st.isEmpty():
				return False
			else:
				top = st.pop()
				if not is_match(top,paren):
					is_balanced = False
		index += 1
	
	if st.isEmpty() and is_balanced:
		return True
	else:
		return False							
					

print(is_paren_balanced("({[]})"))
=======
class Stack:
	def __init__(self):
		#Creating an empty list which will be used to replicate the stack functionality
		self.items = [] 

	def size(self):
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
>>>>>>> 757d76ade453e60a94c141c4ce17658c227e35e8

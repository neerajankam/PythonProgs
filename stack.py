class Stack:
	def __init__(self):
		self.elems=[]
	def push(self,val):
	    return self.elems.append(val)
	def pop(self):
	    return self.elems.pop()
	def isEmpty(self):
	    return self.elems == []
	def peek(self):
	    return self.elems[len(self.elems)-1]
	def size(self):
	    return len(self.elems)    
s=Stack()
s.push(1)
s.push(123)
s.push(44)
s.push(22)
s.push(98)
s.push(14)
s.pop()
print(s.isEmpty())
print(s.peek())

s.pop()
print(s.peek())



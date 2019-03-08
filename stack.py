class Queue:
	def __init__(self):
		self.elems=[]
<<<<<<< HEAD
	def enqueue(self,val):
	    return self.elems.append(0,val)
	def dequeue(self):
=======
		
	def push(self,val):
	    return self.elems.append(val)
	
	def pop(self):
>>>>>>> 757d76ade453e60a94c141c4ce17658c227e35e8
	    return self.elems.pop()
	
	def isEmpty(self):
	    return self.elems == []
	
	def peek(self):
	    return self.elems[len(self.elems)-1]
	
	def size(self):
<<<<<<< HEAD
	    return len(self.elems)    
q=Queue()
q.enqueue(9)
q.enqueue(10)
q.enqueue(18)
q.enqueue(55)
q.enqueue(412)
q.enqueue(12)
q.enqueue(41)
q.dequeue()
=======
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

>>>>>>> 757d76ade453e60a94c141c4ce17658c227e35e8

print(d.peek())
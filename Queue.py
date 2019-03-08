class Queue:
	def __init__(self):
		self.elems=[]
	
	def enqueue(self,val):
	    return self.elems.insert(0,val)
	
	def dequeue(self):
	    return self.elems.pop()
	
	def isEmpty(self):
	    return self.elems == []
	
	def size(self):
	    return len(self.elems)  

q=Queue()
q.enqueue(9)
q.enqueue(10)
q.enqueue(18)
q.enqueue(55)
q.enqueue(412)
q.enqueue(12)
q.enqueue(41)
print(q.dequeue())




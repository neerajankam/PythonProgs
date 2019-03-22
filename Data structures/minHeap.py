class MinHeap:
  def __init__(self, array):
    self.heap = self.heapify(array)
  
  #Time complexity: O(n) since we're running through each element of the array and trickling it down till it reaches the 
  #appropriate position. At first glance, it looks like the time is O(n log n) but this is incorrect because most of the
  #elements aare the bottom of the heap and they do not sift down many levels. Only the 0th element sifts down log n levels
  #Hence it is O(n) 
  #Space: O(1) since we use no extra space and heapify the array in-place.   
  def heapify(self, array):
    firstParentIdx = (len(array) - 2) // 2
    for i in reversed(range(1,firstParentIdx+1)):
      self.siftDown(i, len(array) - 1, array)
    return array

  #Time: O(log n)
  def siftDown(self, curIdx, endIdx, array):
    childOneIdx = curIdx * 2 + 1
    while childOneIdx <= endIdx:
      childTwoIdx = curIdx * 2 + 2 if curIdx * 2 + 2 <= endIdx else -1
      if childTwoIdx != -1 and array[childTwoIdx] < array[childOneIdx]:
        idxToSwap = childTwoIdx
      else:
        idxToSwap = childOneIdx
      curIdx = idxToSwap
      childOneIdx = curIdx * 2 + 1

      self.swap(curIdx, idxToSwap, array)
    return array
  
  #Time: O(log n)
  def siftUp(self, curIdx, heap):
    parentIdx = (curIdx - 1)//2
    while parentIdx >= 0:
      if heap[curIdx] < heap[parentIdx]:
        self.swap(curIdx, parentIdx, heap)
      curIdx = parentIdx
      parentIdx = (curIdx - 1)// 2
  
  #Time: O(log n)
  def insert(self, ele):
    self.heap.append(ele)
    self.siftUp(len(self.heap) - 1, self.heap)
  
  #Time:O(log n)
  def remove(self):
    self.swap(0, len(self.heap) - 1, self.heap)
    popped = self.heap.pop()
    self.siftDown(0, len(self.heap) - 1, self.heap)
    return popped

  #Time:O(1)  
  def swap(self, a, b, array):
    array[a], array[b] = array[b], array[a]


h = MinHeap([6,1,12,10,5,7,3,20])
h.insert(100)
h.insert(5)
#In a heap you can only remove the first element and hence you cannot remove any random element. 
h.remove() 
print(h.heap)
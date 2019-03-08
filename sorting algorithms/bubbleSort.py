def bubbleSort(arr):
	isSorted = False
	while not isSorted:
		isSorted = True
		for i in range(1,len(arr)):
			if arr[i] < arr[i-1]:
				arr[i], arr[i-1] = arr[i-1], arr[i]
				isSorted = False
	return arr
		


arr = [64, 34, 25, 12, 22, 11, 90]
print(bubbleSort(arr))

#Time complexity: O(n^2) in average and worst cases. O(1) in the best case where all elements are sorted.
#Space: O(1) since it does not used any extra space.
from collections import defaultdict

class Graph:
	def __init__(self, vertices, edges):
		self.graph = defaultdict(list)
		self.V = vertices
		for edge in edges:
			self.addEdge(edge[0], edge[1])

	def addEdge(self, u, v):
		self.graph[u].append(v)

	def topologicalSortUtil(self, v, visited, stack):
		visited[v] = True

		for i in self.graph[v]:
			if visited[i] == False:
				self.topologicalSortUtil(i, visited, stack)
		stack.insert(0,v)

	def topologicalSort(self):
		visited = [False] * (len(self.V) + 1)
		stack = []

		for i in self.V:
			if visited[i] == False:
				self.topologicalSortUtil(i, visited, stack)
		return stack

g = Graph([1,2,3,4], [[1,2],[1,3],[3,2],[4,2],[4,3]])
print(g.topologicalSort())

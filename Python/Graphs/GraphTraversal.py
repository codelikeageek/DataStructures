class Graph:
    def __init__(self):
        self.adjacencyList = {}

    def addVertex(self, v):
        if v not in self.adjacencyList:
            self.adjacencyList[v] = []

    def addEdge(self, v1, v2):
        if v1 not in self.adjacencyList:
            self.addVertex(v1)
        if v2 not in self.adjacencyList:
            self.addVertex(v2)
        self.adjacencyList[v1].append(v2)
        self.adjacencyList[v2].append(v1)

    def depthFirstIterative(self, vertex):
        output = []
        stack = []
        visited = {}
        if vertex not in self.adjacencyList or len(self.adjacencyList) == 0:
            return
        stack.append(vertex)
        visited[vertex] = True
        while len(stack) != 0:
            vertex = stack.pop()
            output.append(vertex)
            for v in self.adjacencyList[vertex]:
                if v not in visited:
                    stack.append(v)
                    visited[v] = True
        return output

    def depthFirstRecursive(self, vertex):
        output = []
        visited = {}
        def helper(vertex):
            if vertex not in self.adjacencyList or len(self.adjacencyList) == 0:
                return
            visited[vertex] = True
            output.append(vertex)
            for v in self.adjacencyList[vertex]:
                if v not in visited:
                    helper(v)
        helper(vertex)
        return output

    def breadthFristSearch(self, vertex):
        output = []
        visited = {}
        queue = []
        queue.append(vertex)
        visited[vertex] = True
        while len(queue) != 0:
            vertex = queue.pop(0)
            output.append(vertex)
            for v in self.adjacencyList[vertex]:
                if v not in visited:
                    visited[v] = True
                    queue.append(v)
        return output

g = Graph()
g.addVertex('Tokyo')
g.addVertex('Cairo')
g.addVertex('Dallas')
g.addEdge('Tokyo', 'Cairo')
g.addEdge('Dallas', 'Tokyo')
g.addVertex('Hyderabad')
g.addEdge('Hyderabad', 'Cairo')
g.addEdge('Dallas', 'Hyderabad')
g.addEdge('Chicago', 'Mason')
g.addEdge('Dallas', 'Mason')
print(g.depthFirstIterative('Tokyo'))
print(g.depthFirstRecursive('Tokyo'))
print(g.breadthFristSearch('Tokyo'))
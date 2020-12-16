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

    def filter(self, list, vertex):
        output = []
        for i in list:
            if i != vertex:
                output.append(i)
        return output

    def removeEdge(self, v1, v2):
        if self.adjacencyList[v1]:
            self.adjacencyList[v1] = self.filter(self.adjacencyList[v1],v2)
        if self.adjacencyList[v2]:
            self.adjacencyList[v2] = self.filter(self.adjacencyList[v2], v1)
        #return self.adjacencyList

    def removeVertex(self, v):
        if not self.adjacencyList[v]:
            return
        else:
            for vertex in self.adjacencyList[v]:
                self.removeEdge(vertex, v)
            del self.adjacencyList[v]
        #return self.adjacencyList

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
print(g.adjacencyList)
g.removeEdge('Dallas', 'Tokyo')
print(g.adjacencyList)
g.removeVertex('Dallas')
print(g.adjacencyList)
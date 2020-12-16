class Graph {
    constructor() {
        this.adjacencyList = {};
    }

    addVertex(v1) {
        if (!this.adjacencyList[v1]) {
            this.adjacencyList[v1] = [];
        }
    }

    addEdge(v1, v2) {
        if (this.adjacencyList[v1]) {
            this.adjacencyList[v1].push(v2);
        }
        if (this.adjacencyList[v2]) {
            this.adjacencyList[v2].push(v1);
        }
    }

    depthFirstRecursive(vertex) {
        let output = [];
        let visited = {};
        let list = this.adjacencyList;
        function helper(vertex) {
            if (!list[vertex] || list[vertex].length === 0) {
                return;
            } else {
                visited[vertex] = true;
                output.push(vertex);
                for (let i = 0; i < list[vertex].length; i++) {
                    if (!visited[list[vertex][i]]) {
                        helper(list[vertex][i]);
                    }
                }
            }
        }
        helper(vertex);
        return output;
    }

    depthFirstIterative(vertex) {
        let output = [];
        let stack = [];
        let visited = {};
        let currentVertex;

        stack.push(vertex);
        visited[vertex] = true;
        while (stack.length !== 0) {
            currentVertex = stack.pop();
            output.push(currentVertex);
            this.adjacencyList[currentVertex].forEach(element => {
                if (!visited[element]) {
                    stack.push(element);
                    visited[element] = true;
                }
            });
        }
        return output;
    }

    breadthFirstTraversal(vertex) {
        let output = [];
        let visited = {};
        let queue = [];
        let currentVertex;

        queue.push(vertex);
        while (queue.length !== 0) {
            currentVertex = queue.shift();
            if (!visited[currentVertex]) {
                visited[currentVertex] = true;
                output.push(currentVertex);
                queue.push(...this.adjacencyList[currentVertex]);
            }
        }
        return output;
    }
}

let g = new Graph();
g.addVertex("A");
g.addVertex("B");
g.addVertex("C");
g.addVertex("D");
g.addVertex("E");
g.addVertex("F");
g.addVertex("G");
g.addEdge("A", "B");
g.addEdge("A", "C");
g.addEdge("B", "D");
g.addEdge("C", "E");
g.addEdge("D", "E");
g.addEdge("D", "F");
g.addEdge("E", "F");
console.log(g);
console.log(g.depthFirstRecursive("A"));
console.log(g.depthFirstIterative("A"));
console.log(g.breadthFirstTraversal("A"));
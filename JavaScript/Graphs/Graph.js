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

    removeEdge(v1, v2) {
        if (this.adjacencyList[v1]) {
            this.adjacencyList[v1] = this.adjacencyList[v1].filter(v => v !== v2);
        }
        if (this.adjacencyList[v2]) {
            this.adjacencyList[v2] = this.adjacencyList[v2].filter(v => v !== v1);
        }
    }

    removeVertex(v1) {
        for (let i = 0; i < this.adjacencyList[v1].length; i++) {
            this.removeEdge(v1, this.adjacencyList[v1][i]);
        }
        delete this.adjacencyList[v1];
    }
}

let g = new Graph();
g.addVertex("Tokyo");
g.addVertex("Cairo");
g.addVertex("Dallas");
g.addEdge("Tokyo", "Cairo");
g.addEdge("Dallas", "Tokyo");
g.addVertex("Hyderabad");
g.addEdge("Hyderabad", "Cairo");
console.log(g);
//g.removeEdge("Dallas", "Tokyo");
g.removeVertex("Dallas");
console.log(g);
"""
Find the shortest path
(A combination of BFS and Dijkstra's algorithm)
Input:
    Starting vertex
    Final vertex
    Visted vertices (List)
    Shortest path table (Key: Each vertex, Value: the vertex before proceeding to the key)
Output:
    The precise shortest path

1. Initialize a queue and a variable called count with value of 0
2. Add the starting vertex to the queue and visted vertices list
3. While queue is not empty:
    1. Dequeue the first vertex to currentVertex
    2. If currentVertex is the final vertex:
        1. Break out the while loop
    3. Iterate over the adjacent vertices of current vertex:
        1. If the vertex is not visited:
            1. Append this vertex to the queue
            2. Append this vertex to the visited vertices list
            3. Assign {vertex: currentVertex} to the shortest path count table
4. Assign final vertex to the currentVertex, and initialize a list named path
5. While currentVertex is not the starting vertex:
    1. Append currentVertex to the path list
    2. Assign shortestPathTable[currentVertex] to currentVertex
6. Append starting vertex to the path list
7. Return the reversed path list           
"""

# Adapted from https://medium.com/geekculture/how-to-represent-a-graph-data-structure-in-python-9f0df57e33a2#:~:text=E%27%2C%2013)%5D%0AE%2D%2D%3E%5B%5D-,The%20Graph%20Class,-Now%20it%27s%20time
class undirectedGraph:    
    def __init__(self):
        self.graph = dict()

    def addEdge(self, node1, node2):
        if node1 not in self.graph:
            self.graph[node1] = []
        if node2 not in self.graph:
            self.graph[node2] = []

        self.graph[node1].append(node2)
        self.graph[node2].append(node1)

    def printGraph(self):
        for source, destination in self.graph.items():
            print(f"{source}-->{destination}")
    
    def bfs(self, startingVertex, searchValue, visitedVertices = []):
        queue = []
        queue.append(startingVertex)
        visitedVertices.append(startingVertex)
        while len(queue) != 0:
            currentVertex = queue[0]
            if currentVertex == searchValue:
                return currentVertex
            queue.remove(currentVertex)
            for vertex in self.graph[currentVertex]:
                if vertex not in visitedVertices:
                    queue.append(vertex)
                    visitedVertices.append(vertex)
        return None

    def find_shortest_path(self, startingVertex, finalVertex, visitedVertices = [], shortestPathTable = {}):
        queue = []
        queue.append(startingVertex)
        visitedVertices.append(startingVertex)
        while len(queue) != 0:
            currentVertex = queue[0]
            if currentVertex == finalVertex:
                break
            queue.remove(currentVertex)
            for vertex in self.graph[currentVertex]:
                if vertex not in visitedVertices:
                    queue.append(vertex)
                    visitedVertices.append(vertex)
                    shortestPathTable[vertex] = currentVertex
        
        currentVertex = finalVertex
        path = []
        while currentVertex != startingVertex:
            path.append(currentVertex)
            currentVertex = shortestPathTable[currentVertex]
        path.append(startingVertex)
        path.reverse()
        return path


def main():
    g = undirectedGraph()

    g.addEdge("Idris", "Kamil")
    g.addEdge("Idris", "Talia")
    g.addEdge("Kamil", "Lina")
    g.addEdge("Lina", "Sasha")
    g.addEdge("Talia", "Ken")
    g.addEdge("Ken", "Marco")
    g.addEdge("Marco", "Sasha")


    # g.printGraph()
    print(g.find_shortest_path("Idris", "Lina"))

    
if __name__=="__main__":
    main()
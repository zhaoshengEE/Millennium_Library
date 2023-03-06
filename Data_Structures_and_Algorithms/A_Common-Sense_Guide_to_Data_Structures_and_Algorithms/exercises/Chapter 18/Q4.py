"""
BFS over a graph
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
    print(g.bfs("Idris", "Marco"))
    print(g.bfs("Idris", "Jerry"))

    
if __name__=="__main__":
    main()
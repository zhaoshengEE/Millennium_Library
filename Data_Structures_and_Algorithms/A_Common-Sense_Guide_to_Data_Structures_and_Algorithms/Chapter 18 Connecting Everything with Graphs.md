# Chapter 18. Connecting Everything with Graphs

## Fundamentals of Graph

In "graph speak":

- `Node` -> `Vertex`
- `The line between vertices` -> `Edge`
- Vertices are connected by an edge is referred to as `adjacent vertices` or `neighbors`.

- A graph where are the vertices are connected is called `connected graph`.
- `Trees` are a type of graph. For a graph to be considered as a tree, it cannot have cycles, and all nodes must be connected. While it is possible for a graph to not be fully connected.
- Relationships are mutual -> `Undirected graph`
- Relationships are not mutual -> `Directed graph`
- There is additional information on the edges of the graph -> `Weighted graph`
- Specific sequence of edges to get from one vertex to another -> `Path`


## Depth-First Search (DFS) & Breadth-First Search (BFS)

- `DFS`:
    - Implement via `recursion`
    - Use `graph` to keep track of which vertex has been visited

- `BFS`:
    - Implement via `nested loop`
    - Use `queue` to store all the adjacent vertices of current vertex and figure out which vertex to be visited in the next step.
    - For the implementation of BFS, please refer to the [Exercise Question in this chapter](./exercises/Chapter%2018/Q4.py)

`BFS` traverses all the vertices closest to the starting vertex before moving further away, whereas `DFS` immediately moves as far away from the starting vertex as it can.

Time efficiency of graph search is O(V + E), where V refers to the number of vertices and E is the number of edges in the graph.


## Dijkstra's Algorithm

A general description of the approach for finding the shortest path within a  weighted graph, but it doesn't specify the precise code implementation.

Take the example demonstrated in the book: Find the cheapest path in the city flights, where three hash tables and a list are being used:

- `visited_city`: 
    - Key: All the cities **including** the starting city
    - Value: True
    - This hash table keeps track of the cities we have visited.

- `cheapest_prices_table`: 
    - Key: All the cities **including** the starting city
    - Value: Cheapest price of flight from starting city to the key

- `cheapest_previous_stopover_city_table`: 
    - Key: All the cities **excluding** the starting city
    - Value: The second-to-last stop before the key to earn the cheapest price, given flying from the starting
    - This hash table can help us get the path which gets us the cheapest price.

- `unvisited_city`:
    - Store the adjacent city that has not been visited and will be visited in the next iteration.

> 1. Visit the starting city, add `{"starting city": 0}` to the `cheapest_prices_table`, make the starting city our `current_city`.
> 2. While the `current_city` is not None:
>     1. Assign `{"current_city: True}` to the `visited_city` table.
>     2. Remove the `current_city` from the `unvisited_city` list.
>     3. Iterate over the price from the current city to each of its adjacent cities:
>           1. If the adjacent city is not in the `visited_city`, append it to the `unvisited_city` list.
>           2. price_through_current_city = cheapest_prices_table + price.
>           3. If `price_through_current_city` is cheaper than the price currently in the `cheapest_prices_table` OR the adjacent city is not in the `cheapest_prices_table` at all:
>                   1. Assign `{"adjacent city": price_through_current_city}` to the `cheapest_prices_table`.
>                   2. Assign `{"adjacent city": "current_city"}` to the `cheapest_previous_stopover_city_table`.
>       4. Choose the one from the `unvisited_city` list that is cheapest, and make it the `current_city` to be visited in the next iteration.

For the implementation of Dijkstra's algorithm and BFS, please refer to the [Exercise Question in this chapter](./exercises/Chapter%2018/Q5.py)


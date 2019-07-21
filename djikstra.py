# import sys 
  
class Graph(): 
  
    def __init__(self, vertices): 
        self.vertices = vertices 
        self.graph = [[0 for column in range(vertices)]  
                      for row in range(vertices)] 
  
    def printSolution(self, dist): 
        for node in range(self.vertices): 
            print(node, "to", dist[node])
  
    # A utility function to find the vertex with  
    # minimum distance value, from the set of vertices  
    # not yet included in shortest path tree 
    def minDistance(self, dist, sptSet): 
  
        # Initilaize minimum distance for next node 
        min = float("inf") 
  
        # Search not nearest vertex not in the  
        # shortest path tree 
        for v in range(self.vertices): 
            if dist[v] < min and sptSet[v] == False: 
                min = dist[v] 
                min_index = v 
  
        return min_index 
  
    # Funtion that implements Dijkstra's single source  
    # shortest path algorithm for a graph represented  
    # using adjacency matrix representation 
    def dijkstra(self, first_vertex): 
  
        distances = [float("inf")] * self.vertices # all start as infinity
        distances[first_vertex] = 0
        shortest_path_tree = [False] * self.vertices 
  
        for _ in range(self.vertices): 
            print(distances, shortest_path_tree)
  
            # Pick the minimum distance vertex from  
            # the set of vertices not yet processed.  
            # u is always equal to first_vertex in first iteration 
            u = self.minDistance(distances, shortest_path_tree) 
  
            # Put the minimum distance vertex in the  
            # shortest path tree 
            shortest_path_tree[u] = True
  
            # Update distances value of the adjacent vertices  
            # of the picked vertex only if the current  
            # distance is greater than new distance and 
            # the vertex in not in the shortest path tree 
            for v in range(self.vertices): 
                if self.graph[u][v] > 0 and shortest_path_tree[v] == False and distances[v] > distances[u] + self.graph[u][v]: 
                        distances[v] = distances[u] + self.graph[u][v] 
  
        self.printSolution(distances) 
  
# Driver program 
g = Graph(9) 
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0], 
           [4, 0, 8, 0, 0, 0, 0, 11, 0], 
           [0, 8, 0, 7, 0, 4, 0, 0, 2], 
           [0, 0, 7, 0, 9, 14, 0, 0, 0], 
           [0, 0, 0, 9, 0, 10, 0, 0, 0], 
           [0, 0, 4, 14, 10, 0, 2, 0, 0], 
           [0, 0, 0, 0, 0, 2, 0, 1, 6], 
           [8, 11, 0, 0, 0, 0, 1, 0, 7], 
           [0, 0, 2, 0, 0, 0, 6, 7, 0] 
          ]; 
  
g.dijkstra(0); 



"""
Now we need to implement our algorithm.

At our starting node (X), we have the following choice:

Visit A next at a cost of 7
Visit B next at a cost of 2
Visit C next at a cost of 3
Visit E next at a cost of 4
We choose the lowest cost option, to visit node B at a cost of 2.
We then have the following options:

Visit A from X at a cost of 7
Visit A from B at a cost of (2 + 3) = 5
Visit D from B at a cost of (2 + 4) = 6
Visit H from B at a cost of (2 + 5) = 7
Visit C from X at a cost of 3
Visit E from X at a cost of 4
The next lowest cost item is visiting C from X, so we try that and then we are left with the above options, as well as:

Visit L from C at a cost of (3 + 2) = 5
Next we would visit E from X as the next lowest cost is 4.

For each destination node that we visit, we note the possible next destinations and the total weight to visit that destination. If a destination is one we have seen before and the weight to visit is lower than it was previously, this new weight will take its place. For example

Visiting A from X is a cost of 7
But visiting A from X via B is a cost of 5
Therefore we note that the shortest route to X is via B
We only need to keep a note of the previous destination node and the total weight to get there.

We continue evaluating until the destination node weight is the lowest total weight of all possible options.

In this trivial case it is easy to work out that the shortest path will be:
X -> B -> H -> G -> Y

For a total weight of 11.

In this case, we will end up with a note of:

The shortest path to Y being via G at a weight of 11
The shortest path to G is via H at a weight of 9
The shortest path to H is via B at weight of 7
The shortest path to B is directly from X at weight of 2
And we can work backwards through this path to get all the nodes on the shortest path from X to Y.

Once we have reached our destination, we continue searching until all possible paths are greater than 11; at that point we are certain that the shortest path is 11.
"""

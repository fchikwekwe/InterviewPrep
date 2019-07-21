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

def can_visit_all_rooms(rooms):
    graph = {i: val for i, val in enumerate(rooms)}
    
    # since nodes are 0 to n - 1, we can start with node 0
    return dfs(graph, 0)

def dfs(graph, node, visited=set()):
    if node not in visited:
        visited.add(node)

        for neighbor in graph[node]:
            dfs(graph, neighbor, visited)

    # if not all nodes were visited, return False; otherwise True
    if len(visited) < len(graph):
        return False
    return True

if __name__ == "__main__":
    # uncomment one rooms variable below to test
    # rooms = [[1], [2], [3], []] # true
    rooms = [[1, 3], [3, 0, 1], [2], [0]] # false
    print(can_visit_all_rooms(rooms))

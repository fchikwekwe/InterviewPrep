"""
org_chart = [
    'A, B, C, D',
    'B, E, F',
    'F, G, H'
    'G, I'
]

Output: 
A
....B
........E
........F
............G
................I
............H
....C
....D

"""

org_chart = [
    'A,B,C,D',
    'B,E,F',
    'F,G,H',
    'G,I'
]

graph = {}

for string in org_chart: 
    string_list = string.split(',')
    graph[string_list[0]] = string_list[1:]

print(graph)

def dfs(graph, vertex, level=0):
    dots = "...." * level
    print(dots + vertex)

    if vertex in graph: 
        val = graph[vertex]
    else: 
        # base case; not a key in graph
        return

    # change level every node away from start
    level += 1
    for child in val: 
        # recursive case 
        dfs(graph, child, level)




dfs(graph, 'A')

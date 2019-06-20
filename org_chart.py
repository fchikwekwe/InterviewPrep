"""
org_chart = [
    'A, B, C, D',
    'B, E, F',
    'F, G, H'
    'G, I'
]
{

}

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

def make_graph(org_chart):
    graph = {}
    for string in org_chart: 
        string_list = string.split(',')
        # turn the values into sets if the order doesn't matter
        graph[string_list[0]] = set(string_list[1:])

    return graph

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

def find_start_node(graph):
    values = {val for v in graph.values() for val in v}
    
    for key in graph.keys():
        if key not in values: 
            return graph.keys()
    return None # no starting node


# def find_start_node(graph):
#     counter = 0 
#     for key, value in graph: 
#         counter = 1
#         while counter != len(graph):

            
graph = make_graph(org_chart)
start = find_start_node(graph)
if start: 
    dfs(graph, 'A')
else: 
    print("Please provide a valid organization chart.")

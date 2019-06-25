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
    all_reports = set()
    for string in org_chart: 
        string_list = string.split(',')
        # turn the values into sets if the order doesn't matter
        manager = string_list[0]
        reports = string_list[1:]
        graph[manager] = reports
        for report in reports: # look up if there is extend-like func for sets
            all_reports.add(report)

    return graph, all_reports

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

def find_start_node(graph, all_reports):
    for key in graph.keys():
        if key not in all_reports: 
            return key
    return None # no starting node


# def find_start_node(graph):
#     counter = 0 
#     for key, _ in graph: 
        
            
        

            
graph, all_reports = make_graph(org_chart)
start = find_start_node(graph, all_reports)
print(start)
if start: 
    dfs(graph, 'A')
else: 
    print("Please provide a valid organization chart.")


"""
Given an arr 
"""
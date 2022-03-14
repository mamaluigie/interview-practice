import pdb
graph = {
    'A' : ['B','C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : ['H'],
    'E' : ['F'],
    'F' : [],
    'H' : ['Z'],
    'Z' : []
}

def depthFirstSearch(visited, graph, root):
    if root not in visited: 
        print(root)
        visited.add(root)
        for neighbor in graph[root]:
            depthFirstSearch(visited, graph, neighbor)


visited = set()
depthFirstSearch(visited, graph, 'A')

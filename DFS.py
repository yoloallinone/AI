#implement DFS

graph1={
    'A' : ['B','S'],
    'B' : ['A'],
    'C' : ['D','E','F','S'],
    'D' : ['C'],
    'E' : ['C','H'],
    'F' : ['C','G'],
    'G' : ['F','S'],
    'H' : ['E','G'],
    'S' : ['A','C','G']
    }
visited=[]

def  dfs(graph,node):
    global visted
    if node not in visited:
        visited.append(node)
        for n in graph[node]:
            dfs(graph,n)
            
dfs(graph1,'A')
print(visited)

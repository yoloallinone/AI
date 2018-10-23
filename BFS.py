visited=[]
import collections
def bfs(graph,root):
    visited,queue=set(),collections.deque([root])
    visited.add(root)
    while queue:
        vertex=queue.popleft()
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                print(visited)
                queue.append(neighbour)

if __name__=='__main__':
    graph={0:[1,2],1:[0],2:[0,3],3:[2]} 
    bfs(graph,0)


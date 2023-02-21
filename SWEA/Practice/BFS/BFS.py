from collections import deque

def BFS(G, v, n):
    visited = [0] * (n+1)
    queue = deque([])
    queue.append(v)
    visited[v] = 1
    print(v, end = ' ')
    while queue:
        t = queue.popleft()
        for i in range(len(G[t])):
            if G[t][i] and not visited[i]:
                queue.append(i)
                visited[i] = 1
                print(i, end = ' ')

n, m = 7, 8
route = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]
graph = [[0] * (n+1) for i in range(n+1)]

for i in range(0, len(route), 2):
    graph[route[i]][route[i+1]] = 1

BFS(graph, 1, 7)
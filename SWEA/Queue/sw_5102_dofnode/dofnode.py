import sys
sys.stdin = open('sample_input.txt')

from collections import deque

def BFS(graph, S, G, n):
    visited = [0] * (n+1)
    queue = deque([])
    queue.append(S)
    visited[S] = 0
    while queue:
        t = queue.popleft()
        if t == G:
            return visited[t]
        for i in range(V+1):
            if graph[t][i] and not visited[i]:
                queue.append(i)
                visited[i] = visited[t] + 1
    else:
        return 0

t = int(input())

for tc in range(1, t+1):
    V, E = map(int, input().split())
    route = [[0] * (V+1) for _ in range(V+1)]
    for _ in range(E):
        y, x = map(int, input().split())
        route[y][x] = 1
        route[x][y] = 1
    S, G = map(int, input().split())
    print(f'#{tc}', BFS(route, S, G, V))
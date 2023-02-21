import sys
sys.stdin = open('input.txt')

from collections import deque

def BFS_maze(graph, n):
    di = [0, 0, 1, -1]
    dj = [1, -1, 0, 0]
    visited = [[0] * (n+1) for _ in range(n+1)]
    q = deque([])
    visited[1][1] = 1
    q.append([1, 1])

    while q:
        t = q.popleft()
        for k in range(4):
            ni = t[0] + di[k]
            nj = t[1] + dj[k]
            if 0 <= ni < n and 0 <= nj < n:
                if graph[ni][nj] == 3:
                    return 1
                if not graph[ni][nj] and not visited[ni][nj]:
                    q.append([ni, nj])
                    visited[ni][nj] = 1
    else:
        return 0

for t in range(10):
    tc = int(input())
    maze = [list(map(int,input())) for _ in range(16)]
    print(f'#{tc}', BFS_maze(maze, 16))

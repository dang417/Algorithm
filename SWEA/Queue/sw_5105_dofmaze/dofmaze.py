import sys
sys.stdin = open('sample_input.txt')

from collections import deque

di = [0, 0, -1, 1]
dj = [-1, 1, 0, 0]

def distance_BFS(g, v, n):
    visited = [[0] * n for _ in range(n)]
    queue = deque([])
    queue.append(v)
    visited[v[0]][v[1]] = 0
    while queue:
        t = queue.popleft()
        for k in range(4):
            ni = t[0] + di[k]
            nj = t[1] + dj[k]
            if 0 <= ni < n and 0 <= nj < n:
                if maze[ni][nj] == 3:
                    return visited[t[0]][t[1]]
                if not g[ni][nj] and not visited[ni][nj]:
                    queue.append([ni, nj])
                    visited[ni][nj] = visited[t[0]][t[1]] + 1
    else:
        return 0

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    maze = [list(map(int, input())) for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if maze[i][j] == 2:
                v = [i, j]
    print(f'#{tc}', distance_BFS(maze, v, n))

import sys
sys.stdin = open('input.txt')

import sys
from collections import deque
input = sys.stdin.readline

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

def BFS(r, c):
    q = deque()
    q.append((r, c))
    union = [(r, c)]
    while q:
        i, j = q.popleft()
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj]:
                if L <= abs(A[ni][nj] - A[i][j]) <= R:
                    visited[ni][nj] = 1
                    q.append((ni, nj))
                    union.append((ni, nj))
    return union

N, L, R = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

rlt = 0
while True:
    visited = [[0] * (N+1) for _ in range(N+1)]
    flag = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                visited[i][j] = 1
                nations = BFS(i, j)
                if len(nations) > 1:
                    flag = 1
                    avg = sum([A[x][y] for x, y, in nations]) // len(nations)
                    for x, y in nations:
                        A[x][y] = avg
    if flag == 0:
        break

    rlt += 1

print(rlt)
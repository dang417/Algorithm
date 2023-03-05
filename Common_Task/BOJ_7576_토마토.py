import sys
sys.stdin = open('input.txt')

import sys
input = sys.stdin.readline
from collections import deque

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

def BFS(r, c):
    q = deque()
    q.append((r, c))
    while q:
        i, j = q.popleft()
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < N and 0 <= nj < M and not farm[ni][nj]:
                if farm[ni][nj] == 0:
                    farm[ni][nj] = 1
                    tomato.append((ni, nj))

M, N = map(int, input().split())
farm = [list(map(int, input().split())) for _ in range(N)]
tomato = deque()
rlt = 0

for i in range(N):
    for j in range(M):
        if farm[i][j] == 1:
            tomato.append((i, j))

while tomato:
    for i in range(len(tomato)):
        r, c = tomato.popleft()
        BFS(r, c)
    rlt += 1

for i in range(N):
    if not all(farm[i]):
        break
else:
    print(rlt-1)
    exit()
print(-1)
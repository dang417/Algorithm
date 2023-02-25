import sys
sys.stdin = open('sample_input.txt')

from collections import deque

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

t = int(input())

for tc in range(1, t+1):
    n, m = map(int, input().split())
    arr = [list(input()) for _ in range(n)]
    q = deque([])
    distance = [[1000000] * m for _ in range(n)]
    rlt = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 'W':
                distance[i][j] = 0
                q.append(i)
                q.append(j)

    while q:
        y = q.popleft()
        x = q.popleft()
        for k in range(4):
            ni = y + di[k]
            nj = x + dj[k]
            if 0 <= ni < n and 0 <= nj < m:
                if distance[ni][nj] > (distance[y][x] + 1):
                    q.append(ni)
                    q.append(nj)
                    distance[ni][nj] = distance[y][x] + 1

    for i in range(n):
        rlt += sum(distance[i])
    print(f'#{tc}', rlt)
import sys
sys.stdin = open('input.txt')

di = [0, 0, -1, 1]
dj = [-1, 1, 0, 0]

def DFS(arr):
    visited = [[0] * m for _ in range(n)]
    stack = []
    cnt = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] and not visited[i][j]:
                stack.append((i, j))
                visited[i][j] = 1
                while stack:
                    y, x = stack.pop()
                    for k in range(4):
                        ni = y + di[k]
                        nj = x + dj[k]
                        if 0 <= ni < n and 0 <= nj < m:
                            if arr[ni][nj] and not visited[ni][nj]:
                                stack.append((ni, nj))
                                visited[ni][nj] = 1
                cnt += 1
    return cnt

t = int(input())
for tc in range(1, t+1):
    m, n, k = map(int, input().split())
    arr = [[0] * m for _ in range(n)]
    for i in range(k):
        x, y = map(int, input().split())
        arr[y][x] = 1

    print(DFS(arr))
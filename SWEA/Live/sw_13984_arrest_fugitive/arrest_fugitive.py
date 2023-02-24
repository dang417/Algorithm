import sys
sys.stdin = open('sample_input.txt')

from collections import deque

t = int(input())
for tc in range(1, t+1): #상 하 좌 우
    tunnel_type = {1 : [[-1, 1, 0, 0], [0, 0, -1, 1]],
                   2 : [[-1, 1, 0, 0], [0, 0, 0, 0]],
                   3 : [[0, 0, 0, 0], [0, 0, -1, 1]],
                   4 : [[-1, 0, 0, 0], [0, 0, 0, 1]],
                   5 : [[0, 1, 0, 0], [0, 0, 0, 1]],
                   6 : [[0, 1, 0, 0], [0, 0, -1, 0]],
                   7 : [[-1, 0, 0, 0], [0, 0, -1, 0]]
                   }
    n, m, r, c, l = map(int, input().split())
    tunnel_map = [list(map(int, input().split())) for _ in range(n)]
    fugitive = [[0] * m for _ in range(n)]
    fugitive[r][c] = 1
    q = deque((r, c))
    rlt = 0
    while q:
        i = q.popleft()
        j = q.popleft()
        if tunnel_map[i][j]:
            di = tunnel_type[tunnel_map[i][j]][0]
            dj = tunnel_type[tunnel_map[i][j]][1]
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni < n and 0 <= nj < m:
                    if tunnel_map[ni][nj] and not fugitive[ni][nj]:
                        q.append(ni)
                        q.append(nj)
                        fugitive[ni][nj] = fugitive[i][j] + 1
    for i in range(n):
        for j in range(m):
            if 0 < fugitive[i][j] <= l:
                rlt += 1
    print(rlt)
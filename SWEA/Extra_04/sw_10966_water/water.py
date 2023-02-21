import sys
sys.stdin = open('sample_input.txt')

from collections import deque
#
# def BFS_water(graph, start):
#     di = [0, 0, 1, -1]
#     dj = [1, -1, 0, 0]
#     visited[start[0]][start[1]] = 0
#     q = deque([])
#     q.append(start)
#     while q:
#         t = q.popleft()
#         for k in range(4):
#             ni = t[0] + di[k]
#             nj = t[1] + dj[k]
#             if 0 <= ni < n and 0 <= nj < m:
#                 if graph[ni][nj] == 'L' and visited[ni][nj] > 0:
#                     if visited[t[0]][t[1]] + 1 <= visited[ni][nj]:
#                         q.append([ni, nj])
#                         visited[ni][nj] = visited[t[0]][t[1]] + 1
#
# t = int(input())
# for tc in range(1, t+1):
#     n, m = map(int, input().split())
#     map_arr = [list(input()) for _ in range(n)]
#     visited = [[1000000] * m for _ in range(n)]
#     S = []
#     rlt = 0
#     for i in range(n):
#         for j in range(m):
#             if map_arr[i][j] == 'W':
#                 S.append([i, j])
#     for s in S:
#         BFS_water(map_arr, s)
#
#     for i in range(n):
#         rlt += sum(visited[i])
#
#     print(f'#{tc}', rlt)

t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    map_arr = [list(input()) for _ in range(n)]
    distance_arr = [[0] * m for _ in range(n)]
    water_list = []
    for i in range(n):
        for j in range(m):
            if map_arr[i][j] == 'W':
                water_list.append([i, j])


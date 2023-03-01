import sys
sys.stdin = open('input.txt')

# 델타 탐색을 진행하며 방문 기록 저장하고, 집의 개수를 +1
# # 델타 탐색이 끝난 후 집의 개수를 rlt에 저장, 단지 수 +1
# 단지의 개수 프린트
# 단지의 개수만큼 rlt를 순회하며 집의 개수를 프린트

from collections import deque

def BFS(arr):
    rlt = []
    group_cnt = 0
    di = [0, 0, -1, 1]
    dj = [-1, 1, 0, 0]
    q = deque([])
    visited = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 1 and not visited[i][j]:
                q.append(i)
                q.append(j)
                visited[i][j] = 1
                home_cnt = 1
                while q:
                    y = q.popleft()
                    x = q.popleft()
                    for k in range(4):
                        ni = y + di[k]
                        nj = x + dj[k]
                        if 0 <= ni < n and 0 <= nj < n:
                            if arr[ni][nj] and not visited[ni][nj]:
                                q.append(ni)
                                q.append(nj)
                                visited[ni][nj] = 1
                                home_cnt += 1
                else:
                    group_cnt += 1
                    rlt.append(home_cnt)
    print(group_cnt)
    rlt = sorted(rlt)
    for i in range(group_cnt):
        print(rlt[i])

n = int(input())
arr = [list(map(int, input())) for _ in range(n)]
BFS(arr)
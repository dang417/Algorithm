import sys
sys.stdin = open('input.txt')

def DFS(i, j, cnt, tmp):
    global rlt
    if tmp > rlt:
        return
    if cnt == N:
        if rlt >= tmp:
            rlt = tmp
        return
    x, y = i, j
    for z in (x, 6 - (x + y)):
        tmp_1 = tmp
        tmp_1 += house[cnt][z]
        x = y
        y = z
        DFS(x, y, cnt + 1, tmp_1)

N = int(input())
house = [0] * N
rlt = 1000000000000000

for i in range(N):
    house[i] = [0] + list(map(int, input().split()))

for i in range(1, 4):
    for j in range(1, 4):
        if i != j:
            sum_num = house[0][i] + house[1][j]
            DFS(i, j, 2, sum_num)

print(rlt)
# DFS 로 풀기
# 1번집과 2번집의 색을 정한다
# R, G, R, B, G, R, G, B, B, R, B, G
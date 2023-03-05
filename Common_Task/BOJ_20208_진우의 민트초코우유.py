import sys
sys.stdin = open('input.txt')

N, M, H = map(int, input().split())
village = [list(map(int, input().split())) for _ in range(N)]
mincho = []
cnt = 0

for i in range(N):
    for j in range(N):
        if village[i][j] == 1:
            start = [i, j]

for i in range(N):
    for j in range(N):
        if village[i][j] == 2:
            mincho.append([i, j, abs(start[0] - i) + abs(start[1] - j)])
mincho = sorted(mincho, key= lambda x : x[2])
now = start

for milk in mincho:
    M -= abs(now[0] - milk[0]) + abs(now[1] - milk[1])
    M += H
    now = [milk[0], milk[1]]
    cnt += 1
    if milk[2] > M:
        print(cnt-1)
        break
else:
    print(cnt)

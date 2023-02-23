import sys
sys.stdin = open('s_input.txt')

t = int(input())

di = [0, 0, -1, 1]
dj = [-1, 1, 0, 0]

for tc in range(1, t+1):
    n = int(input())
    room = [list(map(int, input().split())) for _ in range(n)]
    rlt = [0] * ((n**2)+1)
    for i in range(n):
        for j in range(n):
            y, x = i, j
            cnt = 1
            while True:
                for k in range(4):
                    ni = y + di[k]
                    nj = x + dj[k]
                    if 0 <= ni < n and 0 <= nj < n:
                        if room[y][x] + 1 == room[ni][nj]:
                            y, x = ni, nj
                            cnt += 1
                            break
                else:
                    rlt[room[i][j]] = cnt
                    break
    print(f'#{tc}', rlt.index(max(rlt)), max(rlt))
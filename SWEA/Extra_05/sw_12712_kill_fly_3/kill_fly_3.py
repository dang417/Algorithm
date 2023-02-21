import sys
sys.stdin = open('in1.txt')

plus_di = [0, 0, -1, 1]
plus_dj = [-1, 1, 0, 0]

mult_di = [1, 1, -1, -1]
mult_dj = [1, -1, 1, -1]

t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    rlt = 0
    # + 검사
    for i in range(n):
        for j in range(n):
            tmp = arr[i][j]
            for l in range(1, m):
                for k in range(4):
                    ni = i + (plus_di[k] * l)
                    nj = j + (plus_dj[k] * l)
                    if 0 <= ni < n and 0 <= nj < n:
                        tmp += arr[ni][nj]
            if rlt <= tmp:
                rlt = tmp
    # * 검사
    for i in range(n):
        for j in range(n):
            tmp = arr[i][j]
            for l in range(1, m):
                for k in range(4):
                    ni = i + (mult_di[k] * l)
                    nj = j + (mult_dj[k] * l)
                    if 0 <= ni < n and 0 <= nj < n:
                        tmp += arr[ni][nj]
            if rlt <= tmp:
                rlt = tmp

    print(f'#{tc}', rlt)




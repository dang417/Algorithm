import sys
sys.stdin = open('input2.txt')

t = int(input())

di = [1, -1, 0, 0, 1, -1, 1, -1]
dj = [1, -1, 1, -1, 0, 0, -1, 1]

for tc in range(1, t+1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    rlt = []
    ans = 0
    for i in range(n):
        for j in range(m):
            cnt = 0
            for k in range(8):
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni < n and 0 <= nj < m and arr[i][j] > arr[ni][nj]:
                    cnt += 1
            rlt.append(cnt)
    for i in range(n*m):
        if rlt[i] >= 4:
            ans += 1
    print(f'#{tc}', ans)

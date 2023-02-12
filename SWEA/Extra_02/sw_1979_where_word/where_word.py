import sys
sys.stdin = open('input.txt')

t = int(input())

for tc in range(1, t+1):
    N, K = map(int, input().split())
    rows = []
    cols = []
    cnt = 0
    for i in range(N):
        row = list(map(int, input().split()))
        rows.append(row)
    for i in range(N):
        col = []
        for j in range(N):
            col.append(rows[j][i])
        cols.append(col)
    for i in range(N):
        for j in range(N-K+1):
            if rows[i][j:j+K] == [1] * K and rows[i][j+1:j+K+1] != [1] * K and rows[i][j-1:j+K-1] != [1] * K:
                cnt += 1
            if cols[i][j:j+K] == [1] * K and cols[i][j+1:j+K+1] != [1] * K and cols[i][j-1:j+K-1] != [1] * K:
                cnt += 1
    print(f'#{tc} {cnt}')







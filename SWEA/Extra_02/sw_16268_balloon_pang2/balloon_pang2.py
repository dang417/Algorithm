import sys
sys.stdin = open('input1.txt')

t = int(input())

di = [0, 0, -1, 1]
dj = [-1, 1, 0, 0]

for tc in range(1, t+1):
    n, m = map(int, input().split())
    arr = [list(map(int,input().split())) for i in range(n)]
    cnt_list = 0
    for i in range(n):
        for j in range(m):
            i_j_cnt = arr[i][j]
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni < n and 0 <= nj < m:
                    i_j_cnt += arr[ni][nj]
            if cnt_list < i_j_cnt:
                cnt_list = i_j_cnt
    print(f'#{tc}', cnt_list)

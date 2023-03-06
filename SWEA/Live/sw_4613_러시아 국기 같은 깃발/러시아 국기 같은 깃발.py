import sys
sys.stdin = open('sample_input.txt')

t = int(input())
for tc in range(1, t+1):
    N, M = map(int, input().split())
    flag = [list(input()) for _ in range(N)]
    rlt = N*M
    tmp = 0
    for i in range(1, N-1):
        for j in range(i+1, N):
            for k in range(i):
                tmp += M - flag[k].count('W')
            for k in range(i, j):
                tmp += M - flag[k].count('B')
            for k in range(j, N):
                tmp += M - flag[k].count('R')
            if rlt >= tmp:
                rlt = tmp
            tmp = 0
    print(f'#{tc}', rlt)
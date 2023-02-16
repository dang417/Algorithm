import sys
sys.stdin = open('sample_input.txt')

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    min_sum = 10000000000000
    idx_list = list(range(n))
    for _ in range(n):
        i = 0
        rlt = 0
        while i < n:
            for j in idx_list:
                rlt += arr[i][j]
                i += 1
            if min_sum > rlt:
                min_sum = rlt
        for k in range(n-1):
            idx_list[k], idx_list[k+1] = idx_list[k+1], idx_list[k]


    print(f'#{tc}', min_sum)
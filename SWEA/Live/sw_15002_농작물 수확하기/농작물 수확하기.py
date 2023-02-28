import sys
sys.stdin = open('input.txt')

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    farm = [list(map(int, input())) for _ in range(n)]
    x = y = n//2
    k = n//2
    rlt = 0
    for i in range(-k, k+1):
        for j in range(-k, k+1):
            if abs(i) + abs(j) <= k:
                rlt += farm[y + i][x + j]

    print(f'#{tc}', rlt)

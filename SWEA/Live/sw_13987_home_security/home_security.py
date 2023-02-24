import sys
sys.stdin = open('sample_input.txt')

t = int(input())

for tc in range(1, t+1):
    n, m = map(int, input().split())
    city = [list(map(int, input().split())) for _ in range(n)]
    rlt = 0
    for k in range(1, n+2):
        cost = (k * k + (k - 1) * (k - 1))
        if n * n * m < cost:
            break
        for i in range(n):
            for j in range(n):
                cnt = 0
                pay = 0
                for y in range(-k+1, k):
                    for x in range(-k+1, k):
                        if abs(x) + abs(y) < k and 0 <= i + y < n and 0 <= j + x < n:
                            if city[i + y][j + x] == 1:
                                cnt += 1
                                pay += m
                if cost <= pay and rlt <= cnt:
                    rlt = cnt

    print(f'#{tc}', rlt)
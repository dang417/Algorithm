t = int(input())

for tc in range(1, t+1):
    n, m = map(int, input().split())
    cnt = 0
    for i in range(n):
        for j in range(i, m-n+1):
            cnt += 1
    print(cnt)
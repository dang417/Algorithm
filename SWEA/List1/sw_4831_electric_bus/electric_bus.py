t = int(input())

for tc in range(1, t+1):
    K, N, M = map(int, input().split())
    charge_list = list(map(int, input().split()))

    b = 0
    cnt = 0
    while b + K < N:
        for i in range(b+K, b, -1):
            if i in charge_list:
                b = i
                cnt += 1
                break
        else:
            cnt = 0
            b = N

    print(f'#{tc} {cnt}')

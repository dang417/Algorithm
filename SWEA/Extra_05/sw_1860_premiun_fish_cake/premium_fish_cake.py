import sys
sys.stdin = open('input.txt')

t = int(input())
for tc in range(1, t+1):
    n, m, k = map(int, input().split())
    time = list(map(int, input().split()))

    start = m
    fish_cake = k
    i = 0
    while True:
        if time[i] >= m and (len(time) - i) < fish_cake:
            i += k
            fish_cake -= 1
            if i >= len(time):
                print(f'#{tc} Possible')
                break
        else:
            print(f'#{tc} Impossible')
            break
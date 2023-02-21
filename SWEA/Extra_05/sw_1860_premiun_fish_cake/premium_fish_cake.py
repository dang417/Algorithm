import sys
sys.stdin = open('input.txt')

t = int(input())
for tc in range(1, t+1):
    n, m, k = map(int, input().split())
    times = sorted(list(map(int, input().split())))
    time = m
    fish_cake = k

    for i in range(0, n, k):
        if time > min(times[i:i+k]):
            print(f'#{tc} Impossible')
            break
        else:
            time += m
    else:
        print(f'#{tc} Possible')




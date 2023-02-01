import sys
sys.stdin = open('input.txt')

tc = int(input())

for t in range(1, tc+1):
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(n):
        for j in range(n-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    print(f'#{t} {a[-1] - a[0]}')

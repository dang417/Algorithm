import sys
sys.stdin = open('input.txt')

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    if n <= 3:
        print(1)
        continue
    p = [0] * (n + 1)
    p[1] = 1
    p[2] = 1
    for i in range(3, n+1):
        p[i] = p[i-2] + p[i-3]
    print(p[n])

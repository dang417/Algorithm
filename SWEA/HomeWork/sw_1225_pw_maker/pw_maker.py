import sys
sys.stdin = open('input.txt')

from collections import deque

for t in range(10):

    tc = int(input())
    num = deque(list(map(int, input().split())))
    A = True
    while A:
        k = 1
        for i in range(5):
            num[0] -= k
            num.rotate(-1)
            k += 1
            if num[-1] <= 0:
                num[-1] = 0
                A = False
                break

    print(f'#{tc}', *num)

import sys
sys.stdin = open('sample_input.txt')

from collections import deque

t = int(input())

for tc in range(1, t+1):
    n, m = map(int, input().split())
    pizza = list(map(int, input().split()))
    pizza_deque = deque(pizza[n:])
    oven = deque(pizza[0:n])

    while pizza_deque:
        if len(pizza_deque) <= n:
            break
        if oven[0] == 0 and pizza_deque:
            oven.popleft()
            oven.appendleft(pizza_deque.popleft())
        else:
            oven[0] = oven[0] // 2
        oven.rotate(-1)
    print(f'#{tc}', pizza.index(max(pizza_deque))+1)
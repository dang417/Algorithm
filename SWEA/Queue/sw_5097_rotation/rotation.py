import sys
sys.stdin = open('sample_input.txt')

from collections import deque

t = int(input())

for tc in range(1, t+1):
    n, m = map(int, input().split())
    data = list(map(int, input().split()))
    que = deque(data)

    # for i in range(m):
    #     que.append(que.popleft())

    que.rotate(-m)
    print(f'#{tc}', que[0])
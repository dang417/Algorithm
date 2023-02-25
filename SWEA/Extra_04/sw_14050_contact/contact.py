import sys
sys.stdin = open('input.txt')

from collections import deque

for tc in range(1, 11):
    n, s = map(int, input().split())
    data = list(map(int, input().split()))
    route = [[0] * (max(data)+1) for _ in range(max(data)+1)]
    visited = [0] * (max(data)+1)

    for i in range(0, n, 2):
        route[data[i]][data[i+1]] = 1

    visited[s] = 1
    now = s
    q = deque([s])
    while q:
        now = q.popleft()
        for next in range(max(data)+1):
            if route[now][next] and not visited[next]:
                visited[next] = visited[now] + 1
                q.append(next)

    rlt = []
    for i in range(max(data)+1):
        if visited[i] == max(visited):
            rlt.append(i)

    print(f'#{tc}', max(rlt))
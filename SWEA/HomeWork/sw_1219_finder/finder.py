import sys
sys.stdin = open('input.txt')

def DFS(start):
    # 첫 시작위치 아무튼 방문함
    visited[start] = 1
    stack = [start]
    while stack:
        start = stack.pop()
        if start == G: # 현재 지점이 도착지점이라면
            return 1

        for next in range(1, 100):
            if data[start][next] and not visited[next]:
                visited[next] = 1
                stack.append(next)
    return 0

for _ in range(10):
    tc, E = map(int, input().split())
    route = list(map(int, input().split()))
    data = [[0] * 100 for _ in range(100)]
    visited = [0] * 100

    for i in range(0, len(route) - 1, 2):
        data[route[i]][route[i+1]] = 1

    S, G = 0, 99
    print(f'#{tc}', DFS(S))
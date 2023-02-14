import sys
sys.stdin = open('sample_input.txt')

def DFS(start):
    # 첫 시작위치 아무튼 방문함
    visited[start] = 1
    stack = [start]
    while stack:
        start = stack.pop()
        if start == G: # 현재 지점이 도착지점이라면
            return 1

        for next in range(1, V+1):
            if data[start][next] and not visited[next]:
                visited[next] = 1
                stack.append(next)
    return 0

t = int(input())

for tc in  range(1, t+1):
    V, E = map(int, input().split())
    # 인접 행렬
    data = [[0]*(V+1) for _ in range(V+1)]
    # 방문 표시용 리스트
    visited = [0] * (V+1)

    for i in  range(E):
        x, y = map(int, input().split())
        data[x][y] = 1
    # 시작지점 S, 도착지점 G
    S, G = map(int, input().split())

    print(f'#{tc}',DFS(S))
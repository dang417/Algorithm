import sys

sys.stdin = open('input.txt')

T = int(input())

# 델타검색 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def search(x, y, N):
    cnt = 0

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N:  # 벽을 넘어가면 안됨
            cnt += abs(arr[nx][ny] - arr[x][y])
    return cnt


for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    for i in range(N):
        for j in range(N):
            result += search(i, j, N)
    print(f'#{tc} {result}')
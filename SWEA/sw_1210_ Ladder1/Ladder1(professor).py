import sys
sys.stdin = open('input.txt')

# 웬만한 델타 탐색의 경우 아래의 형태를 따르게 됨

dx = [1, 0, 0]
dy = [0, -1, 1]

def search(x, y):
    # 첫 출발 지점이 무엇인지 미리 기록
    original_y = y

    while x != 99: # 가장 아래층까지 도착하기 전까지
        # 조사 방향? 3방향 : 아래, 좌, 우
        for i in range(3):
            # 다음 지역 x 좌표 = 현재 x + 다음 방향
            nx = x + dx[i] # [-1, 0, 0]
            ny = y + dy[i] # [0, -1, 1]

            # 범위를 벗어나지 않고, 다음 조사 대상이 1이면 이동
            if 0 <= nx < 100 and 0 <= ny < 100 and data[nx][ny] == 1:
                # 위 조건을 만족했으니 이동
                x, y = nx, ny

    if data[x][y] == 2:
        return original_y
    else:
        return 0

for _ in range(1, 11):
    tc = int(input())
    data = [list(map(int, input().split())) for _ in range(100)]

    # 출발점을 찾아서 모든 출발점에서 시작
    for y in range(100):
        # 0번째 열(세로)의 y번째 행(가로)의 값이 1이면
        if data[0][y] == 1:
            search(0, y) # x, y 좌표를 0과 y로 조사

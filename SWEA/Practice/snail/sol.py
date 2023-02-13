import sys
sys.stdin = open('input.txt')

    # 우, 하, 좌, 상
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    arr = [[0]*N for _ in range(N)] # 답을 기록할 배열

    count = 1       # 점점 증가할 값을 담아두기 위한 변수
    x, y = 0, 0     # 시작 좌표 초기화
    dir = 0         # 이동할 방향
    arr[x][y] = count   # 시작 위치에 1을 기록하고 시작
    while count < N**2: # N*N 만큼의 크기가 만들어지니까 3*3 -> 9
        nx = x + dx[dir]    # nx = 0 + dx[0] -> 0
        ny = y + dy[dir]    # ny = 0 + dy[0] -> 1
        # 다음 조사 위치가 0보다 크거나 같고 N보다는 작다면
        if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == 0:
            # 이전에 한번이라도 다녀간적이 없다면
            count += 1  # 이전에 적은 수보다 더큰 수
            arr[nx][ny] = count # 새로 가려는 곳에 넣는다
            x, y = nx, ny       # 내 현재 위치를 바꿔준다.
        else:       # 위에서 찾은 모든 조건을 만족하지 못하는 언젠가
            dir += 1
            if dir >= 4:    # 방향은 4종류 뿐
                dir = 0
    for i in arr:
        print(i)

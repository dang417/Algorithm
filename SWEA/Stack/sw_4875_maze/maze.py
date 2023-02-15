import sys
sys.stdin = open('sample_input.txt')

t = int(input())

dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]

for tc in range(1, t+1):
    n = int(input())
    maze = [list(map(int, input())) for _ in range(n)]
    y, x = 0, 0
    stack = []
    rlt = 0

    for i in range(n):
        for j in range(n):
            if maze[i][j] == 2:
                y, x = i, j
                break

    start_y, start_x = y, x
    cnt = 0
    A = True

    print(f'#{tc}', rlt)
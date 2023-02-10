import sys
sys.stdin = open('sample_input(1).txt')

t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    board = []

    for i in range(n):
        row = [0] * n
        board.append(row)
    c = (n//2)-1
    board[c][c+1] = board[c+1][c] = 1
    board[c][c] = board[c+1][c+1] = 2

    for i in range(m):
        # 돌 두기
        x, y, p = map(int, input().split())
        board[y-1][x-1] = p
        
        # 가로 적용
        for j in range(1, n):
            if board[y-1][j] == p:
                if x-1 - j > 0:
                    for k in range(j, x-1):
                        board[y-1][k] = p
                    break
                else:
                    for k in range(x-1, j):
                        board[y-1][k] = p
                    break


        # 세로 적용
        for j in range(1, n):
            if board[j][x-1] == p:
                if y-1 - j > 0:
                    for k in range(j, y-1):
                        board[k][x-1] = p
                    break
                else:
                    for k in range(y-1, j):
                        board[k][x-1] = p
                    break

        # 대각선 적용
        # 인덱스를 나가지 않으면서 대각선을 탐색하는 방법..
        k = 0

        board[y - 1][x - 1] = p
        # 위쪽 검사
        j in range(1, y):
        j in range(1, 8-y):

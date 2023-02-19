import sys
sys.stdin = open('input.txt')

di = [0, 0, -1, 1]
dj = [-1, 1, 0, 0]

for t in range(10):
    tc = int(input())
    maze = [list(map(int, input())) for _ in range(100)]
    stack = []
    i = 1
    j = 1
    while True:
        if maze[i][j] == 3:
            print('sucess!')
            break
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < 100 and 0 <= nj < 100:
                if maze[ni][nj] == 0:
                    maze[ni][nj] = 1
                    stack.append(ni)
                    stack.append(nj)
                    i = ni
                    j = nj
                    break
                elif maze[ni][nj] == 3:
                    i = ni
                    j = nj
                    break
        else:
            j = stack.pop()
            i = stack.pop()
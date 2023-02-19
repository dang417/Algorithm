import sys
sys.stdin = open('input.txt')

t = int(input())

for tc in range(1, t+1):
    n, m = map(int, input().split())
    arr = [[0] * n for _ in range(n)]
    arr[(n-1)//2][(n-1)//2] = arr[((n-1)//2)+1][((n-1)//2)+1] = 2
    arr[(n-1)//2][((n-1)//2)+1] = arr[((n-1)//2)+1][(n-1)//2] = 1
    for _ in range(m):
        x, y, c = map(int, input().split())
        arr[y-1][x-1] = c
        stack = []
        while True:
             # 가로 탐색
            i, j = y-1, x-1
            while True:
                j += 1
                if j <= n-1:
                    if arr[i][j] != c:
                        stack.append(j)
                if j <= n-1:
                    if arr[i][j] == c and stack:
                        for _ in range(len(stack)):
                            arr[i][stack.pop()] = c
                        break
                if j >= n-1:
                    stack = []
                    break
            i, j = y-1, x-1
            while True:
                j -= 1
                if j >= 0:
                    if arr[i][j] != c:
                        stack.append(j)
                if j >= 0:
                    if arr[i][j] == c and stack:
                        for _ in range(len(stack)):
                            arr[i][stack.pop()] = c
                        break
                if j <= 0:
                    stack = []
                    break
            # 세로 탐색
            i, j = y-1, x-1
            while True:
                i += 1
                if i <= n-1:
                    if arr[i][j] != c:
                        stack.append(i)
                if i <= n-1:
                    if arr[i][j] == c and stack:
                        for _ in range(len(stack)):
                            arr[stack.pop()][j] = c
                        break
                if i >= n-1:
                    stack = []
                    break
            i, j = y-1, x-1
            while True:
                i -= 1
                if i >= 0:
                    if arr[i][j] != c:
                        stack.append(i)
                if i >= 0:
                    if arr[i][j] == c and stack:
                        for _ in range(len(stack)):
                            arr[stack.pop()][j] = c
                        break
                if i <= 0:
                    stack = []
                    break
            i, j = y-1, x-1
            # 대각선 탐색
            while True:
                i += 1
                j += 1
                if i <= n-1 and j <= n-1:
                    if arr[i][j] != c:
                        stack.append(j)
                        stack.append(i)
                if i <= n-1 and j <= n-1:
                    if arr[i][j] == c and stack:
                        for _ in range(len(stack)//2):
                            i = stack.pop()
                            j = stack.pop()
                            arr[i][j] = c
                        break
                if i >= n-1 or j >= n-1:
                    stack = []
                    break

            i, j = y-1, x-1
            while True:
                i -= 1
                j -= 1
                if i >= 0 and j >= 0:
                    if arr[i][j] != c:
                        stack.append(j)
                        stack.append(i)
                if i >= 0 and j >= 0:
                    if arr[i][j] == c and stack:
                        for _ in range(len(stack)//2):
                            i = stack.pop()
                            j = stack.pop()
                            arr[i][j] = c
                        break
                if i <= 0 or j <= 0:
                    stack = []
                    break

            i, j = y-1, x-1
            while True:
                i += 1
                j -= 1
                if i <= n-1 and j >= 0:
                    if arr[i][j] != c:
                        stack.append(j)
                        stack.append(i)
                if i <= n-1 and j >= 0:
                    if arr[i][j] == c and stack:
                        for _ in range(len(stack)//2):
                            i = stack.pop()
                            j = stack.pop()
                            arr[i][j] = c
                        break
                if i >= n-1 or j <= 0:
                    stack = []
                    break

            i, j = y-1, x-1
            while True:
                i -= 1
                j += 1
                if i >= 0 and j <= n-1:
                    if arr[i][j] != c:
                        stack.append(j)
                        stack.append(i)
                if i >= 0 and j <= n-1:
                    if arr[i][j] == c and stack:
                        for _ in range(len(stack)//2):
                            i = stack.pop()
                            j = stack.pop()
                            arr[i][j] = c
                        break
                if i <= 0 or j >= n-1:
                    stack = []
                    break
            break

    b_cnt = 0
    w_cnt = 0

    for rows in arr:
        b_cnt += rows.count(1)
        w_cnt += rows.count(2)

    print(f'#{tc}', b_cnt, w_cnt)
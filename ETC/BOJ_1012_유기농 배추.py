t = int(input())
di = [0, 0, -1, 1]
dj = [-1, 1, 0, 0]

for tc in range(1, t+1):
    m, n, k = map(int, input().split())
    arr = [[0] * m for _ in range(n)]
    for i in range(k):
        x, y = map(int, input().split())
        arr[y][x] = 1
    visited = [[0] * m for _ in range(n)]
    rlt = 0
    stack = []

    for i in range(n):
        for j in range(m):
            a, b = i, j
            if arr[a][b] == 1 and visited[a][b] == 0:
                visited[a][b] = 1
                stack.append(a)
                stack.append(b)
                
                while True:
                    for k in range(4):
                        ni = a + di[k]
                        nj = b + dj[k]
                        if 0 <= ni < n and 0 <= nj < m:
                            if arr[ni][nj] == 1 and visited[ni][nj] == 0:
                                visited[ni][nj] = 1
                                stack.append(ni)
                                stack.append(nj)
                                a = ni
                                b = nj
                                break
                    else:
                        if stack != []:
                            b = stack.pop()
                            a = stack.pop()
                        else:
                            rlt += 1
                            break
    print(rlt)
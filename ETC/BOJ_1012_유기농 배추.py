t = int(input())
di = [0, 0, -1, 1]
dj = [-1, 1, 0, 0]
# 배열 전체를 순회하며 만약 1이라면 DFS 실행
# 델타로 탐색하며 값을 1로 바꿔주고, stack 에 인덱스 저장
# 만약 델타 탐색후 주변에 1이 없다면 stack 에서 pop 하며
# 계속해서 탐색
# DFS 가 끝나면 하나의 그룹을 모두 찾은 것이므로 rlt += 1
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
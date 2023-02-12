t = int(input())

for tc in range(1, t+1):
    n = int(input())
    matrix = []
    rlt = 0
    for i in range(10):
        matrix.append([0]*10)

    for num in range(n):
        r1, c1, r2, c2, color = map(int, input().split())

        for i in range(r1, r2+1):
            for j in range(c1, c2+1):
                if matrix[i][j] != color and matrix[i][j] != 3:
                    matrix[i][j] += color